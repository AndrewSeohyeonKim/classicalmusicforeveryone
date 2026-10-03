# -*- coding: utf-8 -*-
"""Typesetting check, in a real browser (typography pass, 2 Oct 2026).

    python3 _build/qa/typeset_check.py            # report
    python3 _build/qa/typeset_check.py --strict   # exit 1 on any fault

Run it after changing copy or type CSS. It serves the built site from this
repository on a free local port and opens one headless Chrome (one at a
time: this Mac sits near its open-file limit). It reports:

  fold   at 1024 or 1440, a lead block whose sentences balance folds into
         half lines: three lines or more, none wider than 65% of the column
         (the Contact head once read as four half lines), or a folded
         sentence beside a one-line sentence a quarter wider (a staircase).
         R10: rewrite the sentence to fit one line or to fill two.
  tail   a lead or short block whose last line is under a quarter of its
         widest line, or a single short word (under 35%)
  tie    a run the build tied (no-break space, word joiner) that still
         breaks across lines
  hero   the home title and its subtitle as one group (R15), measured from
         baselines, not from a descender: on a display title (72px and up)
         English title baseline to the subtitle 0.5 to 0.7 of the title,
         Korean (no descenders) 0.36 to 0.6; never under 36px of clear
         space from the lowest ink (R9; on a phone this floor is the
         measure); the space under the subtitle at least 1.25 times the
         space above it; the first button on screen at 1440x789, 1366x768,
         1280x720 and 390x844
  meet   the meeting drawings at 768 to 1440, text 100% and 200% (R18):
         the stem leaves each bracket at its middle (within 1px), each
         tick meets its ring, and the stem meets the event's ring
  leader Contact's island (R18): the leader from Dublin to "Based in" runs
         through the middle of Dublin's ring and starts at its edge (within
         1px), at 390 to 1440, text 100% and 200%
  axis   the home hero's title group stands on one ink edge (R28): the header
         logo's clef, the line over the title, both title lines (for "for",
         the body of the f; its tail may hang) and the subtitle meet within
         1px, at 1440x789, 1366x768, 1280x720 and 390x844
  width  the master line is as wide as "Classical Music" (R29): on a laptop its
         right end within 3px of the end of "Music" in line 1; on a phone
         (its 22px floor) never wider than that line
  group  a home card's three words stand under its name as one group (R30):
         the name's last line to the words' first line 8px or less, at 1024,
         1100, 1280 and 1440
  names  "Classical Music" in the master line (footer, hero) and the founder's
         name in Contact's signature stay on one line (R23), 390 to 1920
  rings  a page head's sound rings sit on no drawing's ring (doors, stations,
         the meeting, the route, numbered steps) and stop before the next
         band with another ground (R22), 768 to 1440
  wide   text at 200% the way a reader sets it, the browser's own text size
         doubled (so em media and container queries move too, unlike a
         doubled root size): no page scrolls sideways and nothing sticks
         out of the screen, every page, at 320, 390, 768 and 1280

"200%" below always means the browser's text size (Page.setFontSizes).

Known and accepted: a Korean date range in the narrow record column breaks
after its en dash (ALLOW below).
"""

import functools
import http.server
import json
import os
import socketserver
import sys
import threading

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cdp import Chrome  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGES = ["index", "about", "programmes", "get-involved", "news", "contact",
         "programmes/getting-to-know", "programmes/outreach-concerts", "programmes/recorder-ensemble",
         "programmes/letters-ensemble", "programmes/concert-companion"]
VIEWPORTS = [(320, 700), (390, 844), (1024, 768), (1440, 789)]
LEADS = (".lead,.ph-lead,.sh-lead,.figs-note,.pi-text,.founder-line,.play-note,"
         ".pp-say,.join-hint")
SHORT = (".pc p,.pi p,.steps p,.qa dd,.tl-item p,.latest p,.clause-list li,.notice-text p,.leadins li,"
         ".facts dd,.pp-glance dd,.pi-facts dd,.rec-what>span,.meet-t,.route dd,.route-plan dd,"
         ".played-name,.played-who,.seat,.table-top dd,.ct-option>span")
ALLOW = ("–",)  # a tied run may break after an en dash (a range in a narrow column)

JS = r"""((LEADS, SHORT, wide) => {
  const out = {fold: [], tail: [], tie: []};
  const lineRects = el => {
    const r = document.createRange(); r.selectNodeContents(el);
    const lines = new Map();
    for (const x of r.getClientRects()) {
      if (x.width < 1) continue;
      const k = Math.round(x.top);
      const l = lines.get(k) || {left: x.left, right: x.right};
      l.left = Math.min(l.left, x.left); l.right = Math.max(l.right, x.right); lines.set(k, l);
    }
    return [...lines.entries()].sort((a, b) => a[0] - b[0]).map(e => e[1]);
  };
  const words = el => {
    const r = document.createRange(); const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    const ws = []; let n;
    while ((n = walker.nextNode())) {
      const re = /[^\s]+/g; let m;
      while ((m = re.exec(n.data))) { r.setStart(n, m.index); r.setEnd(n, m.index + m[0].length);
        const b = r.getBoundingClientRect(); if (b.width) ws.push({t: m[0], top: Math.round(b.top)}); }
    }
    return ws;
  };
  const visible = el => el.offsetParent !== null && getComputedStyle(el).visibility !== 'hidden';
  // a short last line: English under a quarter, or one short word; Korean
  // ends on its predicate, often two words, so only one short word or a
  // fifth counts there
  const ko = document.documentElement.lang.startsWith('ko');
  const short = (last, max, n) => ko ? (last < max * 0.2 || (n === 1 && last < max * 0.35))
                                     : (last < max * 0.25 || (n === 1 && last < max * 0.35));
  // sentences of lead-type blocks: the .sl spans, or the block itself
  const sentences = [];
  document.querySelectorAll('main ' + LEADS.split(',').join(',main ')).forEach(b => {
    if (!visible(b)) return;
    const sl = [...b.querySelectorAll(':scope > .sl, :scope > span > .sl')].filter(s => getComputedStyle(s).display === 'block');
    if (sl.length) sentences.push(...sl); else if (!b.querySelector('.sl')) sentences.push(b);
  });
  // a block's lines, sentence by sentence
  if (wide) document.querySelectorAll('main ' + LEADS.split(',').join(',main ')).forEach(b => {
    if (!visible(b)) return;
    const col = b.getBoundingClientRect().width; if (!col) return;
    const sl = [...b.querySelectorAll('.sl')].filter(s => getComputedStyle(s).display === 'block');
    const parts = (sl.length ? sl : [b]).map(s => lineRects(s).map(l => (l.right - l.left) / col));
    const all = parts.flat(); if (!all.length) return;
    const pinched = all.length >= 3 && Math.max(...all) < 0.65;
    let stair = false;
    for (let i = 0; i < parts.length; i++) for (let j = 0; j < parts.length; j++)
      if (parts[i].length === 2 && parts[j].length === 1 && parts[j][0] > 1.25 * Math.max(...parts[i])) stair = true;
    if (pinched || stair) out.fold.push({text: b.textContent.trim().slice(0, 100), lines: all.map(x => +x.toFixed(2)),
                                          why: pinched ? 'half lines' : 'staircase'});
  });
  for (const s of sentences) {
    const lines = lineRects(s); if (lines.length < 2) continue;
    const w = lines.map(l => l.right - l.left), last = w[w.length - 1], max = Math.max(...w);
    const ws = words(s), lastTop = ws.length ? ws[ws.length - 1].top : 0;
    const lastWords = ws.filter(x => x.top === lastTop).length;
    if (short(last, max, lastWords))
      out.tail.push({text: s.textContent.trim().slice(-40), fill: +(last / max).toFixed(2), words: lastWords});
  }
  document.querySelectorAll('main ' + SHORT.split(',').join(',main ')).forEach(b => {
    if (!visible(b)) return;
    const lines = lineRects(b); if (lines.length < 2) return;
    const w = lines.map(l => l.right - l.left), last = w[w.length - 1], max = Math.max(...w);
    const ws = words(b), lastTop = ws.length ? ws[ws.length - 1].top : 0;
    const lastWords = ws.filter(x => x.top === lastTop).length;
    if (short(last, max, lastWords))
      out.tail.push({text: b.textContent.trim().slice(-40), fill: +(last / max).toFixed(2), words: lastWords});
  });
  // tied runs that still break
  const walker = document.createTreeWalker(document.querySelector('main'), NodeFilter.SHOW_TEXT); let n;
  while ((n = walker.nextNode())) {
    const re = /[^\s ]+(?:[ ][^\s ]+)+/g; let m;
    while ((m = re.exec(n.data))) {
      const r = document.createRange(); r.setStart(n, m.index); r.setEnd(n, m.index + m[0].length);
      const tops = new Set([...r.getClientRects()].filter(x => x.width > 0).map(x => Math.round(x.top)));
      if (tops.size > 1) out.tie.push(m[0].replace(/ /g, '_'));
    }
  }
  return out;
})"""

HERO = r"""(() => {
  const t = document.querySelector('.hero-title'); const ln = t.querySelectorAll('.ln'); const last = ln[ln.length - 1];
  const em = last.querySelector('em') || last; const lead = document.querySelector('.hero-sub, .hero-copy .lead');
  const cv = document.createElement('canvas').getContext('2d');
  const font = el => { const c = getComputedStyle(el); return `${c.fontStyle} ${c.fontWeight} ${c.fontSize} ${c.fontFamily}`; };
  const r = document.createRange(); r.selectNodeContents(em); const rs = [...r.getClientRects()]; const box = rs[rs.length - 1];
  cv.font = font(em); const m = cv.measureText(em.textContent.trim());
  const baseline = box.top + m.fontBoundingBoxAscent, inkBottom = baseline + m.actualBoundingBoxDescent;
  // on the Korean pages the subtitle is an English span: measure its own face
  const sub = lead.querySelector('[lang="en"]') || lead;
  const r2 = document.createRange(); r2.selectNodeContents(lead); const lines = [...r2.getClientRects()].filter(x => x.width > 1);
  cv.font = font(sub); const m2 = cv.measureText(lead.textContent.trim().split(/\s+/).slice(0, 3).join(' '));
  const capTop = lines[0].top + m2.fontBoundingBoxAscent - m2.actualBoundingBoxAscent;
  const subBase = lines[lines.length - 1].top + m2.fontBoundingBoxAscent;
  const size = parseFloat(getComputedStyle(t).fontSize);
  // R15: from the title's baseline to the subtitle, and from the subtitle's
  // baseline to the running-now block; a descender is not the measure
  const pill = document.querySelector('.hero .now-line, .hero-cta').getBoundingClientRect().top;
  const above = capTop - baseline, below = pill - subBase;
  return {size: Math.round(size), above: Math.round(above), ratio: +(above / size).toFixed(2),
          ink: Math.round(capTop - inkBottom), below: Math.round(below), group: +(below / above).toFixed(2),
          button: Math.round(document.querySelector('.hero-cta').getBoundingClientRect().bottom), height: innerHeight};
})()"""


MEET = r"""(() => {
  const out = [], mid = el => { const b = el.getBoundingClientRect(); return b.top + b.height / 2; };
  for (const ul of document.querySelectorAll('.meet-list')) {
    if (getComputedStyle(ul, '::after').display === 'none') continue;   // a phone: one spine, no stem
    const lis = [...ul.children], r = ul.getBoundingClientRect();
    const stem = r.top + r.height / 2, bracket = (mid(lis[0]) + mid(lis[lis.length - 1])) / 2;
    const hub = mid(ul.closest('.meet').querySelector('.meet-hub'));
    const ticks = Math.max(...lis.map(li => Math.abs(mid(li) - mid(li.querySelector('.meet-ico')))));
    const side = ul.parentElement.className.replace('meet-', '');
    if (Math.abs(stem - bracket) >= 1 || Math.abs(stem - hub) >= 1 || ticks >= 1)
      out.push({side, hub: ul.closest('.meet').querySelector('.meet-hub').textContent.trim(),
                stem_off: +(stem - bracket).toFixed(1), hub_off: +(stem - hub).toFixed(1), tick_off: +ticks.toFixed(1)});
  }
  return out;
})()"""


LEADER = r"""(() => { const dt = document.querySelector('.wa-based dt'); if (!dt) return null;
  const cs = getComputedStyle(dt, '::before'); if (cs.content === 'none') return null;   // stacked: no leader
  const r = dt.getBoundingClientRect(), y = r.top + parseFloat(cs.top) + .5;
  const x1 = r.left - (parseFloat(cs.right) - r.width) - parseFloat(cs.width);
  const h = document.querySelector('.wa-svg .m-halo').getBoundingClientRect();
  const dy = y - (h.top + h.height / 2), dx = x1 - h.right;
  return Math.abs(dy) < 1 && Math.abs(dx) < 1 ? null : {dy: +dy.toFixed(2), dx: +dx.toFixed(2)}; })()"""

WIDE = r"""(() => { const W = document.documentElement.clientWidth, out = [];
  for (const el of document.querySelectorAll('main *, .site-footer *, .site-header *')) {
    const r = el.getBoundingClientRect(); if (!r.width || !r.height) continue;
    if (el.closest('.sr-only,.hero-figure') || getComputedStyle(el).position === 'fixed') continue;
    if (r.right > W + 1 || r.left < -1) out.push(el.tagName.toLowerCase() + '.' + [...el.classList].join('.'));
  }
  const scroll = document.documentElement.scrollWidth - W;
  return scroll > 0 || out.length ? {scroll, els: out.slice(0, 4)} : null; })()"""


AXIS = r"""(() => {
  const cv = document.createElement('canvas').getContext('2d');
  const font = el => { const c = getComputedStyle(el); return `${c.fontStyle} ${c.fontWeight} ${c.fontSize} ${c.fontFamily}`; };
  const first = el => { const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT); let n;
    while ((n = w.nextNode())) { const i = n.textContent.search(/\S/); if (i >= 0 && !n.parentElement.closest('.sr-only')) return [n, i]; } };
  const ink = el => {
    const [n, i] = first(el); const p = n.parentElement; const r = document.createRange(); r.setStart(n, i); r.setEnd(n, i + 1);
    const box = r.getClientRects()[0]; let ch = n.textContent[i];
    if (getComputedStyle(p).textTransform === 'uppercase') ch = ch.toUpperCase();
    if (p.closest('.for')) {  // the f's body: its leftmost ink above its own baseline
      const c2 = document.createElement('canvas'); c2.width = 1400; c2.height = 1100; const x = c2.getContext('2d', {willReadFrequently: true});
      const s = getComputedStyle(p); x.font = `${s.fontStyle} ${s.fontWeight} 1000px ${s.fontFamily}`; x.fillText(ch, 400, 1100);
      const d = x.getImageData(0, 0, 1400, 1100).data; let best = 1e9;
      for (let y = 0; y < 1100; y++) for (let X = 0; X < 1400; X++) if (d[(y * 1400 + X) * 4 + 3] > 127) { if (X < best) best = X; break; }
      return box.left + (best - 400) / 1000 * parseFloat(s.fontSize);
    }
    cv.font = font(p); return box.left - cv.measureText(ch).actualBoundingBoxLeft;
  };
  const img = document.querySelector('.brand img').getBoundingClientRect();
  const k = Math.min(img.width / 341.04, img.height / 131.04);  // the file is drawn into its box with "meet"
  const edges = {clef: img.left + (img.width - 341.04 * k) / 2 + 19.626 * k,  // the clef's ink in logo-horizontal.svg
    eyebrow: ink(document.querySelector('.hero .eyebrow')),
    ...Object.fromEntries([...document.querySelectorAll('.hero-title .ln')].map((l, k) => ['line' + (k + 1), ink(l)])),
    subtitle: ink(document.querySelector('.hero-sub'))};
  const v = Object.values(edges);
  return {spread: +(Math.max(...v) - Math.min(...v)).toFixed(1), edges: Object.fromEntries(Object.entries(edges).map(([k, x]) => [k, +x.toFixed(1)]))};
})()"""


WIDTH = r"""(() => {
  const rects = el => { const r = document.createRange(); r.selectNodeContents(el);
    return [...r.getClientRects()].filter(x => x.width > 1); };
  const ln = document.querySelector('.hero-title .ln'); const w = document.createTreeWalker(ln, NodeFilter.SHOW_TEXT);
  let n, text = null; while ((n = w.nextNode())) { if (n.textContent.trim()) { text = n; break; } }
  const t = text.textContent, end = t.search(/[,，]?\s*$/);   // the line without its comma
  const r = document.createRange(); r.setStart(text, t.search(/\S/)); r.setEnd(text, end);
  const line = [...r.getClientRects()].filter(x => x.width > 1);
  const titleRight = Math.max(...line.map(x => x.right)), titleLeft = Math.min(...line.map(x => x.left));
  const sub = rects(document.querySelector('.hero-sub'));
  const subRight = Math.max(...sub.map(x => x.right));
  const tops = new Set(sub.map(x => Math.round(x.top)));
  return {lines: tops.size, d: +(subRight - titleRight).toFixed(1), sub: Math.round(subRight - titleLeft),
          title: Math.round(titleRight - titleLeft)}; })()"""

GROUP = r"""(() => [...document.querySelectorAll('.pc')].map(pc => {
    const r = el => { const g = document.createRange(); g.selectNodeContents(el); return [...g.getClientRects()].filter(x => x.width > 1); };
    const h = r(pc.querySelector('h3')), t = r(pc.querySelector('.pc-topics'));
    return {name: pc.querySelector('h3').textContent.trim(), gap: Math.round(t[0].top - h[h.length - 1].bottom)};
  }).filter(x => x.gap > 8))()"""

NAMES = r"""(() => { const lines = el => { const r = document.createRange(); r.selectNodeContents(el);
    return new Set([...r.getClientRects()].filter(x => x.width > 1).map(x => Math.round(x.top))).size; };
  const out = [];
  for (const el of document.querySelectorAll('.footer-line .cm, .hero-sub .cm, .wa-who .wa-st:first-child dd .sl:first-child'))
    if (lines(el) > 1) out.push(el.closest('p,dd').className + ': ' + el.textContent);
  return out; })()"""

RINGS = r"""(() => { const ph = document.querySelector('.ph, .pp-head'); if (!ph) return [];
  const cs = getComputedStyle(ph, '::before'); if (cs.content === 'none' || cs.display === 'none') return [];
  const pr = ph.getBoundingClientRect(), w = parseFloat(cs.width);
  const cx = pr.right - parseFloat(cs.right) - w / 2, cy = pr.top + parseFloat(cs.top) + w / 2;
  const rv = .75 * .62 * Math.SQRT1_2 * w, out = [];   // where the rings can still be seen
  for (const el of document.querySelectorAll('.d-ring,.wa-ring,.meet-ico,.meet-hub,.route-mark,.step-n')) {
    const r = el.getBoundingClientRect(); if (!r.width) continue;
    const d = Math.hypot(r.left + r.width / 2 - cx, r.top + r.height / 2 - cy);
    if (d < rv + r.width / 2) out.push('over ' + el.className.split(' ')[0]);
  }
  const bg = getComputedStyle(ph).backgroundColor; let sec = ph.nextElementSibling;
  while (sec && getComputedStyle(sec).backgroundColor === bg) sec = sec.nextElementSibling;
  if (sec && cy + rv > sec.getBoundingClientRect().top + 1) out.push('into ' + (sec.id || sec.className));
  return out; })()"""


def text_size(c, px):
    """The reader's text size: 16 is the browser's default, 32 is 200%."""
    c.call("Page.setFontSizes", fontSizes={"standard": px, "fixed": round(px * 13 / 16)})


class _Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def serve():
    handler = functools.partial(_Quiet, directory=ROOT)
    httpd = socketserver.TCPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, f"http://127.0.0.1:{httpd.server_address[1]}/"


def main(strict=False):
    httpd, base = serve()
    found = {"fold": [], "tail": [], "tie": [], "hero": [], "axis": [], "width": [], "group": [], "meet": [],
             "leader": [], "names": [], "rings": [], "wide": []}
    try:
        with Chrome(port=9371, width=1440, height=900) as c:
            for lang in ("en", "ko"):
                for pg in PAGES:
                    for w, h in VIEWPORTS:
                        mobile = w < 700
                        c.viewport(w, h, 2 if mobile else 1, mobile)
                        c.goto(base + ("" if lang == "en" else "ko/") + pg + ".html", settle=0.4)
                        c.js("document.fonts.ready.then(()=>1)")
                        r = c.js(f"({JS})({json.dumps(LEADS)}, {json.dumps(SHORT)}, {'true' if w >= 1024 else 'false'})")
                        for k in ("fold", "tail"):
                            found[k] += [(lang, pg, w, x) for x in r[k]]
                        found["tie"] += [(lang, pg, w, x) for x in r["tie"] if not any(a in x for a in ALLOW)]
                for w, h in ((1440, 789), (1366, 768), (1280, 720), (390, 844)):
                    c.viewport(w, h, 2 if w < 700 else 1, w < 700)
                    c.goto(base + ("" if lang == "en" else "ko/") + "index.html", settle=0.8)
                    c.js("document.fonts.ready.then(()=>1)")
                    hero = c.js(HERO)
                    lo, hi = (0.5, 0.7) if lang == "en" else (0.36, 0.6)
                    if ((hero["size"] >= 72 and not lo <= hero["ratio"] <= hi) or hero["ink"] < 36
                            or hero["group"] < 1.25 or hero["button"] > hero["height"]):
                        found["hero"].append((lang, w, h, hero))
                    axis = c.js(AXIS)
                    if axis["spread"] > 1:
                        found["axis"].append((lang, w, h, axis))
                    width = c.js(WIDTH)
                    if (width["lines"] == 1 and abs(width["d"]) > 3) or (width["lines"] > 1 and width["sub"] > width["title"] + 1):
                        found["width"].append((lang, w, h, width))
                for w in (1024, 1100, 1280, 1440):
                    c.viewport(w, 900, 1, False)
                    c.goto(base + ("" if lang == "en" else "ko/") + "index.html", settle=0.4)
                    c.js("document.fonts.ready.then(()=>1)")
                    found["group"] += [(lang, w, x) for x in c.js(GROUP)]
                # R23: names kept whole; R22: a head's rings on no drawing, in their own band
                for pg in ("index", "contact"):
                    for w in (390, 768, 1024, 1280, 1440, 1920):
                        c.viewport(w, 900, 2 if w < 700 else 1, w < 700)
                        c.goto(base + ("" if lang == "en" else "ko/") + pg + ".html", settle=0.4)
                        c.js("document.fonts.ready.then(()=>1)")
                        found["names"] += [(lang, pg, w, x) for x in c.js(NAMES)]
                for pg in PAGES[1:]:
                    for w in (768, 1024, 1280, 1366, 1440):
                        c.viewport(w, 900, 1, False)
                        c.goto(base + ("" if lang == "en" else "ko/") + pg + ".html", settle=0.4)
                        found["rings"] += [(lang, pg, w, x) for x in c.js(RINGS)]
                # R18: the meeting drawings and Contact's leader, text 100% and 200%
                for px in (16, 32):
                    text_size(c, px)
                    zoom = "100%" if px == 16 else "200%"
                    for w in (768, 1024, 1280, 1440):
                        c.viewport(w, 900, 1, False)
                        c.goto(base + ("" if lang == "en" else "ko/") + "get-involved.html", settle=0.4)
                        c.js("document.fonts.ready.then(()=>1)")
                        found["meet"] += [(lang, w, zoom, x) for x in c.js(MEET)]
                    for w in (390, 768, 1024, 1280, 1440):
                        c.viewport(w, 900, 2 if w < 700 else 1, w < 700)
                        c.goto(base + ("" if lang == "en" else "ko/") + "contact.html", settle=0.4)
                        c.js("document.fonts.ready.then(()=>1)")
                        r = c.js(LEADER)
                        if r:
                            found["leader"].append((lang, w, zoom, r))
                # text at 200%, every page: nothing past the edge of the screen
                text_size(c, 32)
                for pg in PAGES:
                    for w in (320, 390, 768, 1280):
                        c.viewport(w, 900, 2 if w < 700 else 1, w < 700)
                        c.goto(base + ("" if lang == "en" else "ko/") + pg + ".html", settle=0.4)
                        c.js("document.fonts.ready.then(()=>1)")
                        r = c.js(WIDE)
                        if r:
                            found["wide"].append((lang, pg, w, r))
                text_size(c, 16)
    finally:
        httpd.shutdown()
    for k, rows in found.items():
        print(f"{k}: {len(rows)}")
        for row in rows[:40]:
            print("   ", row)
    faults = sum(len(v) for v in found.values())
    print("typesetting: clean" if not faults else f"typesetting: {faults} to look at")
    return 1 if strict and faults else 0


if __name__ == "__main__":
    sys.exit(main(strict="--strict" in sys.argv))
