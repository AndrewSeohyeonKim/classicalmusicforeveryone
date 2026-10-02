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
  hero   the ink gap under the home title, as a share of the title size
         (R9: 0.4 to 0.6)

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
LEADS = (".lead,.ph-lead,.sh-lead,.figs-note,.progs-note,.pi-text,.founder-line,.play-note,"
         ".pp-say,.join-hint")
SHORT = (".pc p,.pi p,.steps p,.qa dd,.tl-item p,.latest p,.clause-list li,.notice-text p,.leadins li,"
         ".facts dd,.pp-glance dd,.pi-facts dd,.rec-what>span,.examples span")
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
  const em = last.querySelector('em') || last; const lead = document.querySelector('.hero-copy .lead');
  const cv = document.createElement('canvas').getContext('2d');
  const font = el => { const c = getComputedStyle(el); return `${c.fontStyle} ${c.fontWeight} ${c.fontSize} ${c.fontFamily}`; };
  const r = document.createRange(); r.selectNodeContents(em); const rs = [...r.getClientRects()]; const box = rs[rs.length - 1];
  cv.font = font(em); const m = cv.measureText(em.textContent.trim());
  const inkBottom = box.top + m.fontBoundingBoxAscent + m.actualBoundingBoxDescent;
  const r2 = document.createRange(); r2.selectNodeContents(lead); const lb = [...r2.getClientRects()].find(x => x.width > 1);
  cv.font = font(lead); const m2 = cv.measureText(lead.textContent.trim().split(/\s+/).slice(0, 3).join(' '));
  const leadTop = lb.top + m2.fontBoundingBoxAscent - m2.actualBoundingBoxAscent;
  const size = parseFloat(getComputedStyle(t).fontSize);
  return {size: Math.round(size), gap: Math.round(leadTop - inkBottom), ratio: +((leadTop - inkBottom) / size).toFixed(2),
          button: Math.round(document.querySelector('.hero-cta').getBoundingClientRect().bottom), height: innerHeight};
})()"""


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
    found = {"fold": [], "tail": [], "tie": [], "hero": []}
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
                for w, h in ((1440, 789), (1280, 720), (390, 844)):
                    c.viewport(w, h, 2 if w < 700 else 1, w < 700)
                    c.goto(base + ("" if lang == "en" else "ko/") + "index.html", settle=0.8)
                    c.js("document.fonts.ready.then(()=>1)")
                    hero = c.js(HERO)
                    low = 0.38 if lang == "en" else 0.45
                    if hero["ratio"] < low or hero["button"] > hero["height"]:
                        found["hero"].append((lang, w, h, hero))
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
