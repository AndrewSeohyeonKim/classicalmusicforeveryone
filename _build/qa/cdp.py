# -*- coding: utf-8 -*-
"""A Chrome DevTools Protocol driver in the standard library only.

    from cdp import Chrome
    with Chrome(port=9341, width=1440, height=900) as c:
        c.goto("http://127.0.0.1:8702/classicalmusicforeveryone/index.html")
        print(c.js("document.title"))
        c.shoot("/path/out.png")                 # the visible viewport
        c.tiles("/path/prefix", max_tiles=12)     # scroll and capture screen by screen

Run ONE Chrome per process and close it (the with-block does): this Mac sits
near its open-file limit when the Claude desktop VM is busy. Used by
typeset_check.py in this folder (not published: _build/ is never served).
"""

import base64
import json
import os
import shutil
import socket
import struct
import subprocess
import tempfile
import time
import urllib.request

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
HERE = os.path.dirname(os.path.abspath(__file__))


class WS:
    """The client half of RFC 6455, enough for CDP (text frames, ping)."""

    def __init__(self, url, timeout=90):
        assert url.startswith("ws://"), url
        hostport, path = url[5:].split("/", 1)
        host, port = hostport.rsplit(":", 1)
        self.sock = socket.create_connection((host, int(port)), timeout=timeout)
        key = base64.b64encode(os.urandom(16)).decode()
        req = (f"GET /{path} HTTP/1.1\r\nHost: {hostport}\r\nUpgrade: websocket\r\n"
               f"Connection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n")
        self.sock.sendall(req.encode())
        buf = bytearray()
        while b"\r\n\r\n" not in buf:
            chunk = self.sock.recv(4096)
            if not chunk:
                raise RuntimeError("websocket handshake failed")
            buf += chunk
        head, _, rest = bytes(buf).partition(b"\r\n\r\n")
        if b" 101 " not in head.split(b"\r\n")[0]:
            raise RuntimeError(head.decode(errors="replace"))
        self.buf = bytearray(rest)

    def _exact(self, n):
        while len(self.buf) < n:
            chunk = self.sock.recv(max(1 << 16, n - len(self.buf)))
            if not chunk:
                raise RuntimeError("websocket closed")
            self.buf += chunk
        out = bytes(self.buf[:n])
        del self.buf[:n]
        return out

    def _frame(self, op, data):
        hdr = bytearray([0x80 | op])
        n = len(data)
        if n < 126:
            hdr.append(0x80 | n)
        elif n < 65536:
            hdr.append(0x80 | 126)
            hdr += struct.pack(">H", n)
        else:
            hdr.append(0x80 | 127)
            hdr += struct.pack(">Q", n)
        mask = os.urandom(4)
        hdr += mask
        m = (mask * (n // 4 + 1))[:n]
        body = (int.from_bytes(data, "big") ^ int.from_bytes(m, "big")).to_bytes(n, "big") if n else b""
        self.sock.sendall(bytes(hdr) + body)

    def send(self, text):
        self._frame(0x1, text.encode())

    def recv(self):
        msg = bytearray()
        while True:
            b1, b2 = self._exact(2)
            fin, op, n = b1 & 0x80, b1 & 0x0F, b2 & 0x7F
            if n == 126:
                n = struct.unpack(">H", self._exact(2))[0]
            elif n == 127:
                n = struct.unpack(">Q", self._exact(8))[0]
            mask = self._exact(4) if b2 & 0x80 else None
            payload = self._exact(n)
            if mask:
                m = (mask * (n // 4 + 1))[:n]
                payload = (int.from_bytes(payload, "big") ^ int.from_bytes(m, "big")).to_bytes(n, "big")
            if op == 0x8:
                raise RuntimeError("websocket closed by peer")
            if op == 0x9:
                self._frame(0xA, payload)
                continue
            if op == 0xA:
                continue
            msg += payload
            if fin:
                return msg.decode("utf-8", errors="replace")

    def close(self):
        try:
            self.sock.close()
        except OSError:
            pass


class Chrome:
    def __init__(self, port=9341, width=1440, height=900, dpr=1, mobile=False, reduce_motion=True):
        self._start(port, width, height, dpr, mobile, reduce_motion)
        self.font_sizes = None

    def _start(self, port, width, height, dpr, mobile, reduce_motion):
        self.reduce_motion = reduce_motion
        self.port, self.width, self.height, self.dpr, self.mobile = port, width, height, dpr, mobile
        self.profile = tempfile.mkdtemp(prefix=f"cmfe-chrome{port}-")
        args = [CHROME, "--headless=new", f"--remote-debugging-port={port}", "--remote-allow-origins=*",
                f"--user-data-dir={self.profile}", "--no-first-run", "--no-default-browser-check",
                "--disable-extensions", "--disable-sync", "--disable-background-networking",
                "--hide-scrollbars", "--force-color-profile=srgb", "--mute-audio",
                f"--window-size={width},{height}", "about:blank"]
        self.proc = subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        page = None
        for _ in range(150):
            try:
                with urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list", timeout=1) as r:
                    pages = [t for t in json.load(r) if t.get("type") == "page"]
                if pages:
                    page = pages[0]
                    break
            except Exception:
                pass
            time.sleep(0.1)
        if not page:
            self.quit()
            raise RuntimeError("Chrome did not start (open-file limit? port in use?)")
        self.ws = WS(page["webSocketDebuggerUrl"])
        self.n = 0
        self.events = []
        for m in ("Page.enable", "Runtime.enable", "Network.enable"):
            self.call(m)
        self.call("Network.setCacheDisabled", cacheDisabled=True)
        self.viewport(width, height, dpr, mobile)
        self.motion(not reduce_motion)

    # --- protocol -----------------------------------------------------------
    def call(self, method, **params):
        if method == "Page.setFontSizes":
            self.font_sizes = params.get("fontSizes")
        self.n += 1
        mid = self.n
        self.ws.send(json.dumps({"id": mid, "method": method, "params": params}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == mid:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error']}")
                return msg.get("result", {})
            self.events.append(msg)
            if len(self.events) > 4000:
                del self.events[:2000]

    def wait_event(self, name, timeout=30):
        end = time.time() + timeout
        for i, e in enumerate(self.events):
            if e.get("method") == name:
                del self.events[:i + 1]
                return e
        self.ws.sock.settimeout(1)
        try:
            while time.time() < end:
                try:
                    msg = json.loads(self.ws.recv())
                except (socket.timeout, TimeoutError):
                    continue
                if msg.get("method") == name:
                    return msg
                self.events.append(msg)
        finally:
            self.ws.sock.settimeout(90)
        return None

    # --- setup --------------------------------------------------------------
    def viewport(self, width, height, dpr=1, mobile=False):
        self.width, self.height, self.dpr, self.mobile = width, height, dpr, mobile
        self.call("Emulation.setDeviceMetricsOverride", width=width, height=height,
                  deviceScaleFactor=dpr, mobile=mobile)

    def motion(self, on=True):
        self.reduce_motion = not on
        self.call("Emulation.setEmulatedMedia",
                  features=[{"name": "prefers-reduced-motion", "value": "no-preference" if on else "reduce"}])

    # --- pages --------------------------------------------------------------
    def restart(self):
        """A renderer that stopped answering (it happens, rarely, on this Mac):
        a new Chrome on the same port, with the same viewport, motion and text size."""
        fs = self.font_sizes
        self.quit()
        self._start(self.port, self.width, self.height, self.dpr, self.mobile, self.reduce_motion)
        if fs:
            self.call("Page.setFontSizes", fontSizes=fs)
        self.font_sizes = fs

    def goto(self, url, settle=0.8):
        for attempt in range(3):
            try:
                return self._goto(url, settle)
            except (TimeoutError, OSError, ConnectionError) as e:
                if attempt == 2:
                    raise
                print(f"  (Chrome did not answer on {url}: {type(e).__name__}; restarting)", flush=True)
                self.restart()

    def _goto(self, url, settle=0.8):
        self.events.clear()
        self.call("Page.navigate", url=url)
        self.wait_event("Page.loadEventFired", timeout=30)
        # never wait on the fonts for ever: a page whose font promise stalls (it has
        # happened, intermittently) gives up after 5s instead of hanging the run
        self.js("document.fonts ? Promise.race([document.fonts.ready.then(()=>1),"
                " new Promise(r=>setTimeout(()=>r(0),5000))]) : 1", awaitp=True)
        time.sleep(settle)

    def js(self, expr, awaitp=True):
        r = self.call("Runtime.evaluate", expression=expr, returnByValue=True, awaitPromise=awaitp)
        if "exceptionDetails" in r:
            raise RuntimeError(json.dumps(r["exceptionDetails"])[:800])
        return r.get("result", {}).get("value")

    def shoot(self, path, clip=None):
        params = {"format": "png"}
        if clip:
            params["clip"] = dict(clip, scale=1)
        data = self.call("Page.captureScreenshot", **params)["data"]
        with open(path, "wb") as fh:
            fh.write(base64.b64decode(data))
        return path

    def eager_images(self):
        self.js("""Promise.all([...document.images].map(i=>{i.loading='eager';
          return i.complete?1:new Promise(r=>{i.onload=i.onerror=r;setTimeout(r,4000)})}))""")

    def tiles(self, prefix, max_tiles=40, settle=0.35):
        """Scroll one screen at a time and capture what a reader sees."""
        self.eager_images()
        total = self.js("Math.max(document.documentElement.scrollHeight, document.body.scrollHeight)")
        out, y, k = [], 0, 0
        while y < total and k < max_tiles:
            self.js(f"window.scrollTo(0,{y})")
            time.sleep(settle)
            out.append(self.shoot(f"{prefix}-{k:02d}.png"))
            k += 1
            y += self.height - 60
        self.js("window.scrollTo(0,0)")
        return out

    def quit(self):
        try:
            self.ws.close()
        except Exception:
            pass
        try:
            self.proc.terminate()
            self.proc.wait(timeout=5)
        except Exception:
            try:
                self.proc.kill()
            except Exception:
                pass
        shutil.rmtree(self.profile, ignore_errors=True)

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.quit()
