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
         sentence beside a one-line sentence a quarter wider (a staircase),
         or one sentence in two lines neither wider than 62% (v7: "Every
         outreach concert on the record, / with its date, place and music.").
         R10: rewrite the sentence to fit one line or to fill two.
  tail   a lead or short block whose last line is under a quarter of its
         widest line, or a single short word (under 35%)
  tie    a run the build tied (no-break space, word joiner) that still
         breaks across lines, and a long name kept whole by an inline block
         (over 20 letters, v7) that wraps where its line could hold it
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
  group  the parts of cards that stand in one row start level (R30, v6:
         Andrew, "each section the same height"): the five home cards'
         kicker, name, three words, sentence and status, and the three News
         panels' title, line and link, each within 1px across the row, at
         1024, 1100, 1280 and 1440
  names  "Classical Music" in the master line (footer, hero) and the founder's
         name in Contact's signature stay on one line (R23), 390 to 1920
  rings  a page head's sound rings sit on no drawing's ring (doors, stations,
         the meeting, the route, numbered steps), stop before the next band
         with another ground, and lie under nothing a reader reads below the
         head (a row, a card, a pill, an arrow, a form hint: v5) (R22), 768 to
         1440
  faces  one line, one face (R33): within a phrase (pieces on one baseline
         band, closer than 1.6 times the larger size; a dot or an icon between
         them belongs to the phrase) no two typefaces meet, every page at 320,
         390, 1024 and 1440: a number takes the face, size and weight of the
         words it leads ("I. What we do", "01 Learning", "02 Outreach
         Concerts"). Columns across a gutter (a date beside a title, a
         question beside its answer) may differ
  twins  a figure set in Garamond is the same size in both languages (R6,
         R13; v6: a Korean heading rule drew the record's years at 21px
         against 42px): the record's and the timeline's years, the News
         figures, the home figures, at 390, 1024 and 1440
  marks  a short highlight (20 letters, ten Korean syllables: one tied run,
         layout._mark_whole) never breaks across lines, every page, at 320,
         390, 1024 and 1440 (v6: 「부활 / 음악회는」)
  gallery the News gallery's rows fill its width and the photographs of a
         row share one height, each within 1px, at 390 to 1440 (v6)
  years  no line inside a timeline entry starts with a year: beside the gold
         year at the line's left it reads as a second year (CD v6: "…for
         South Dublin Live / 2026: two concerts"), every viewport
  venues the long place names stay on one line in English at 1024 to 1440
         (Mulhuddart Community Centre, Methodist Centenary Church, Tallaght
         University Hospital; v7 Carmelite Community Centre), every page (CD v6)
  yearline a year label (the timeline's, the record's) stands on one line inside
         its column with 3px to spare, at the four viewports and at 1512 and 1728 (v6: the timeline
         year wrapped from 1512px and on phones, and at line-height 0 its two
         lines drew over each other: "2024" read "202" with "4" on its "2")
  motion with motion on, the way most visitors see the site, every page is
         walked to its end and nothing it animates in is left unseen: no
         element under 99% opacity (a drawn arrow's waiting second stroke
         aside), every highlight drawn full width, every drawing's line at its
         full length (v7: the lines now draw), at 1440 and 390 (v6: the
         News panels' rings waited for a trigger declared nowhere above them
         and stayed at opacity 0; captures run with motion off never saw it)
  titlegap R9 measured (v7, QA): under every title of 40px or more, 36px of
         clear space from its lowest ink to the next text's highest ink in its
         column, and under a page's title not more than 1.5 times max(36px,
         0.6 x its size) (chief designer v7), every page at the eight viewports (QA found 22-34px under 23
         titles: section heads, the founder, stacked page heads)
  lang   the other language is one quiet word (v7; Andrew, 4 Oct 2026: the
         switch was "far too big"): one visible link at each width, to this
         page's twin, no capitals or tracking, weight 500 at most, smaller than
         the nav words, no rule until hovered, every page at the four viewports
  dots   every timeline dot is a filled dot at any scroll position with motion
         on (v7: dots drawn as open rings until the eye line reached them, the
         mark the record above uses for a performance; R17), at 1440 and 390
  inword no word breaks inside itself at the reader's usual text size (chief
         designer v7: "ADVERTISIN / G" on Contact, every English page above
         30em): a word's letters on two lines fails, every page at the eight
         viewports; a break after a hyphen, a slash or a list dot is a line
         break, and addresses (email, web) may break
  kinsoku no line starts with , . ; : ! ? ) or a closing quote or bracket, none
         ends with ( or an opening quote or bracket, and in English none ends
         with a, an or the (chief designer v7: a name kept whole by a block let
         "Area / ," and "‘ / Down by" happen), every page at the eight viewports
  colline the four facts under a head (About, programme pages) put their second
         column on the content line within 1px, from 1024 (R25, chief designer v7)
  lone   a long name's block that wraps in a column narrower than itself leaves
         no lone word on the line before it (chief designer v7: "At / the
         National Concert / Hall,")
  phrings the About head's rings lie under no word of the head (chief designer v7:
         behind "in Dublin." at 1440; on a laptop they now leave the photograph
         to the left), at the eight viewports
  sentences (and from 768 the blocks whose sentences sit side by side, once they wrap)
         no sentence starts in the middle of a line in a block that reads a
         sentence a line (R10, chief designer v7: "gifts yet. We / will never
         ask"): leads, answers, timeline lines, values, the privacy intro;
         after a one-word answer ("Yes." / 「네.」) the sentence runs on
  herorings the home hero's rings lie under no word of the hero, its caption
         included: on a phone they rise from the photograph's top edge (v7:
         Andrew, "the phone is all corners"), on a laptop they centre on it and
         fade out above its bottom edge (chief designer v7), at 320 to 1728
  shsize below 55em a page's section titles (.sh h2) are one size (chief designer v7
         round 5: the side column's smaller size outlived the column), every page under 880px
  steps  at 390, in the timeline and the record, no line is under 45% of its column
         before a longer line (a step), and the long venues stay on one line there, in
         both languages (chief designer v7 round 5: 「Methodist / Centenary Church에서 /
         열었습니다.」 in a 246px column)
  wide   text at 200% the way a reader sets it, the browser's own text size
         doubled (so em media and container queries move too, unlike a
         doubled root size): no page scrolls sideways and nothing sticks
         out of the screen, every page, at 320, 390, 768 and 1280

Since v7 the typesetting pass runs at eight viewports (320, 360, 390, 820,
1024, 1180, 1440, 1512: QA found faults that showed only at 360, 820, 1180 or
1512), the hero check also at three tablet screens, group also on the home
figures and the examples' line of time, and years also in timeline titles.
--strict gates the build: reviewed tails are listed in ACCEPT_TAIL.

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
VIEWPORTS = [(320, 700), (360, 740), (390, 844), (820, 1180), (1024, 768), (1180, 820), (1440, 789), (1512, 945)]
LEADS = (".lead,.ph-lead,.sh-lead,.figs-note,.pi-text,.founder-line,.play-note,"
         ".pp-say,.join-hint")
SHORT = (".pc p,.pi p,.steps p,.qa dt,.qa dd,.tl-item p,.latest p,.clause-list li,.notice-text p,.leadins li,"
         ".facts dd,.pp-glance dd,.pi-facts dd,.rec-what>span,.meet-t,.route dd,.route-plan dd,"
         ".played-name,.played-who,.seat,.table-top dd,.ct-option>span")
ALLOW = ("–",)  # a tied run may break after an en dash (a range in a narrow column)
# accepted short last lines (reviewed: a long proper noun in a narrow phone column,
# nothing to tie it to without breaking a word); --strict ignores these
ACCEPT_TAIL = (("programmes/getting-to-know", 320, "Carmelite"), ("about", 390, "BMus"),
               ("news", 320, "Mulhuddart"), ("about", 360, "BMus"),
               # v7 round 5: the Korean September line starts on the church's name, a block as wide
               # as the phone's timeline column, so its verb takes the next line alone
               ("news", 320, "Centenary Church에서"), ("news", 360, "Centenary Church에서"),
               ("news", 390, "Centenary Church에서"))

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
    // one sentence in two half lines: it is 1.0 to 1.3 times the column and
    // should be cut to one line or written to fill two (R10, v7)
    const halves = parts.some(x => x.length === 2 && Math.max(...x) < 0.62);
    let stair = false;
    for (let i = 0; i < parts.length; i++) for (let j = 0; j < parts.length; j++)
      if (parts[i].length === 2 && parts[j].length === 1 && parts[j][0] > 1.25 * Math.max(...parts[i])) stair = true;
    if (pinched || stair || halves) out.fold.push({text: b.textContent.trim().slice(0, 100), lines: all.map(x => +x.toFixed(2)),
                                          why: pinched ? 'half lines' : stair ? 'staircase' : 'two halves'});
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

GROUP = r"""((card, parts) => { const cards = [...document.querySelectorAll(card)]; if (cards.length < 2) return [];
  const tops = cards.map(c => Math.round(c.getBoundingClientRect().top));
  if (Math.max(...tops) - Math.min(...tops) > 1) return [];   // not one row: nothing to level
  const out = [];
  for (const sel of parts) {
    const ts = cards.map(c => c.querySelector(sel)).filter(Boolean).map(e => e.getBoundingClientRect().top);
    if (ts.length > 1 && Math.max(...ts) - Math.min(...ts) > 1) out.push(card + ' ' + sel + ' ' + Math.round(Math.max(...ts) - Math.min(...ts)) + 'px'); }
  return out; })"""
CARD_ROWS = ((".pc", ".kicker", "h3", ".pc-topics", ".pc-body>p:not(.pc-topics)", ".tag"),)
LATEST_ROWS = ((".lt", "h3", "p", ".lt-go"),)
FIGS_ROWS = ((".figs>.fig", ".fig-label", ".fig-period"),)
PLAYED_ROWS = ((".played>li", ".played-when", ".played-name", ".played-who"),)

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
  // the rings stay in their own head: nothing below it that a reader reads lies under them
  const meets = r => { const nx = Math.max(r.left, Math.min(cx, r.right)), ny = Math.max(r.top, Math.min(cy, r.bottom));
    return Math.hypot(nx - cx, ny - cy) < rv; };
  for (let n = ph.nextElementSibling, k = 0; n && k < 2; n = n.nextElementSibling, k++)
    for (const el of n.querySelectorAll('p,li,h2,h3,dt,dd,.tag,.arrow,.cover,figure,a')) {
      const r = el.getBoundingClientRect(); if (r.width && meets(r)) { out.push('under ' + (el.className || el.tagName)); break; } }
  return out; })()"""


FACES = r"""(() => {
  const fam = cs => cs.fontFamily.split(',')[0].replace(/["']/g, '').trim();
  const shown = el => { for (let e = el; e && e !== document.body; e = e.parentElement) {
      const cs = getComputedStyle(e);
      if (cs.display === 'none' || cs.visibility === 'hidden' || e.classList.contains('sr-only')) return false;
      if (e.parentElement && e.parentElement.tagName === 'DETAILS' && !e.parentElement.open && e.tagName !== 'SUMMARY') return false; }
    return true; };
  const f = [], add = (el, cs, b, text, face) => { if (b.width < 1 || b.height < 1) return;
    f.push({fam: face, fs: parseFloat(cs.fontSize), text, cls: el.className && el.className.baseVal === undefined ? el.className : el.tagName,
            x0: b.left, x1: b.right, y0: b.top, y1: b.bottom}); };
  const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {acceptNode: n => /[\p{L}\p{N}]/u.test(n.nodeValue) ? 1 : 2});
  for (let n; (n = w.nextNode());) { const el = n.parentElement;
    if (!el || el.closest('script,style,noscript,template,title') || !shown(el)) continue;
    const cs = getComputedStyle(el), r = document.createRange(); r.selectNodeContents(n);
    for (const b of r.getClientRects()) add(el, cs, b, n.nodeValue.trim().slice(0, 40), fam(cs)); }
  for (const el of document.querySelectorAll('body *')) { if (!shown(el)) continue;
    for (const ps of ['::before', '::after']) { const cs = getComputedStyle(el, ps), c = cs.content;
      if (!c || c === 'none' || c === 'normal' || !(/counter\(/.test(c) || /"[^"]*[\p{L}\p{N}][^"]*"/u.test(c))) continue;
      const b = el.getBoundingClientRect(), fs = parseFloat(cs.fontSize);
      add(el, cs, {left: b.left - 1, right: b.left + fs, top: b.top, bottom: b.top + fs * 1.3, width: fs, height: fs}, ps + c.slice(0, 20), fam(cs)); } }
  for (const t of document.querySelectorAll('svg text')) if (shown(t)) add(t, getComputedStyle(t), t.getBoundingClientRect(), t.textContent.trim().slice(0, 30), fam(getComputedStyle(t)));
  // a dot or a small icon inside a line joins the words either side of it
  for (const d of document.querySelectorAll('i.dot,i.dot-open,.arrow,p svg,h3 svg,a svg')) if (shown(d)) {
    const b = d.getBoundingClientRect(); if (b.width && b.width < 40) add(d, getComputedStyle(d), b, '', null); }
  const p = f.map((_, i) => i), find = i => p[i] === i ? i : (p[i] = find(p[i]));
  for (let i = 0; i < f.length; i++) for (let j = i + 1; j < f.length; j++) { const a = f[i], b = f[j];
    if (Math.min(a.y1, b.y1) - Math.max(a.y0, b.y0) < .5 * Math.min(a.y1 - a.y0, b.y1 - b.y0)) continue;
    const big = Math.max(a.fs, b.fs), small = Math.min(a.fs, b.fs);
    if (Math.max(a.x0, b.x0) - Math.min(a.x1, b.x1) > 1.6 * big || big > 2.2 * small) continue;
    p[find(i)] = find(j); }
  const g = {}; f.forEach((x, i) => (g[find(i)] ||= []).push(x));
  return Object.values(g).filter(x => new Set(x.map(y => y.fam).filter(Boolean)).size > 1)
    .map(x => x.filter(y => y.fam).sort((a, b) => a.x0 - b.x0).map(y => `${y.fam.split(' ')[0]}:${y.text}`).join(' | ')); })()"""


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


TWINS = (".ry-y", ".tl-y", ".mini-figs dd", ".fig b")
TWINS_JS = """((sels) => Object.fromEntries(sels.map(s => { const e = document.querySelector(s);
  return [s, e ? parseFloat(getComputedStyle(e).fontSize) : null]; })))"""
MARKS = """(() => { const out = [];
  for (const m of document.querySelectorAll('main mark')) {
    const t = m.textContent.replace(/\\s+/g, ' ').trim();
    const ko = (t.match(/[\\uac00-\\ud7a3]/g) || []).length;
    const short = ko ? ko + (t.match(/[A-Za-z0-9]/g) || []).length <= 10 : t.length <= 20;
    if (!short || !t.includes(' ')) continue;
    const r = m.getClientRects(); if (r.length < 2) continue;
    const tops = new Set([...r].map(x => Math.round(x.top)));
    if (tops.size > 1) out.push(t); }
  return out; })()"""
GALLERY = """(() => { const g = document.querySelector('.gallery'); if (!g) return [];
  const W = g.getBoundingClientRect().width, gap = parseFloat(getComputedStyle(g).columnGap) || 0;
  const rows = new Map();
  // every photograph drawn (a capture once showed alt text where a file was slow)
  const out = [...g.querySelectorAll('img')].filter(i => !(i.complete && i.naturalWidth > 0)).map(i => ({missing: i.getAttribute('src')}));
  for (const li of g.children) { const r = li.getBoundingClientRect(), p = li.querySelector('.photo').getBoundingClientRect();
    const k = Math.round(r.top); if (!rows.has(k)) rows.set(k, []); rows.get(k).push({w: r.width, h: p.height}); }
  for (const [top, items] of rows) {
    const span = items.reduce((a, x) => a + x.w, 0) + gap * (items.length - 1);
    const hs = items.map(x => x.h);
    if (Math.abs(span - W) > 1) out.push({row: top, n: items.length, span: Math.round(span), width: Math.round(W)});
    if (Math.max(...hs) - Math.min(...hs) > 1) out.push({row: top, heights: hs.map(Math.round)}); }
  return out; })()"""


YEARS = """(() => { const out = [];
  for (const p of document.querySelectorAll('.tl-item p, .tl-item h3')) {
    const w = document.createTreeWalker(p, NodeFilter.SHOW_TEXT); let n, top = null, line = ''; const lines = [];
    while ((n = w.nextNode())) for (let i = 0; i < n.length; i++) {
      const r = document.createRange(); r.setStart(n, i); r.setEnd(n, i + 1); const b = r.getClientRects()[0];
      if (!b) continue; const t = Math.round(b.top);
      if (top !== null && t !== top) { lines.push(line); line = ''; } top = t; line += n.textContent[i]; }
    lines.push(line);
    for (const l of lines.slice(1)) if (/^\\s*\\d{4}\\b/.test(l)) out.push(l.trim().slice(0, 40)); }
  return out; })()"""
VENUES = ("Mulhuddart Community Centre", "Methodist Centenary Church", "Tallaght University Hospital",
          "Carmelite Community Centre")
VENUES_JS = """((names, sel) => { const out = [];
  for (const root of document.querySelectorAll(sel || 'main')) {
  const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT); let n;
  while ((n = w.nextNode())) { if (n.parentElement.closest('.sr-only')) continue;
    const t = n.textContent.replace(/\\u00a0/g, ' ');
    for (const name of names) { let i = t.indexOf(name);
      while (i >= 0) { const r = document.createRange(); r.setStart(n, i); r.setEnd(n, i + name.length);
        const tops = new Set([...r.getClientRects()].filter(x => x.width > .5).map(x => Math.round(x.top)));
        if (tops.size > 1) out.push(t.slice(Math.max(0, i - 24), i + name.length + 8));
        i = t.indexOf(name, i + 1); } } } }
  return out; })"""

# v7 round 5 (chief designer): the phone timeline and record are read in a narrow column; no line
# there is cut short before a longer one (a step: 「Methodist / Centenary Church에서 / 열었습니다.」,
# 「The class / born from the pilot opens」). A sentence a line is a block of its own, so each .sl
# is measured alone; a line under 45% of the column before a longer line fails, at 390
STEP_SEL = ".tl-text, .tl-item h3, .ry-what b"
STEPS = r"""((sel) => { const out = [];
  for (const host of document.querySelectorAll(sel)) {
    const blocks = host.querySelector(':scope > .sl') ? [...host.querySelectorAll(':scope > .sl')] : [host];
    const W = host.clientWidth;
    for (const e of blocks) {
      const r = document.createRange(); r.selectNodeContents(e);
      const lines = [];
      for (const x of [...r.getClientRects()].filter(x => x.width > .5).sort((a, b) => a.top - b.top)) {
        const cy = (x.top + x.bottom) / 2, l = lines.find(v => Math.abs(v.cy - cy) < 6);
        if (l) { l.a = Math.min(l.a, x.left); l.b = Math.max(l.b, x.right); } else lines.push({cy, a: x.left, b: x.right}); }
      const ws = lines.map(v => v.b - v.a);
      for (let i = 0; i < ws.length - 1; i++)
        if (ws[i] < .45 * W && ws[i + 1] > ws[i]) { out.push(e.textContent.trim().slice(0, 60) + ' | line ' + (i + 1) + ': ' + Math.round(ws[i]) + ' of ' + W); break; } } }
  return out; })"""

# v7 round 5 (chief designer): below 55em the side column is gone, so a page's section titles are
# one size ("Since 2024." stood at 25.6px beside 32px titles: the side column's smaller size outlived it)
SHSIZE = r"""(() => { const s = [...document.querySelectorAll('main .sh h2')].filter(h => h.getClientRects().length)
  .map(h => Math.round(parseFloat(getComputedStyle(h).fontSize) * 10) / 10);
  const u = [...new Set(s)]; return u.length > 1 ? [u.join(' / ') + 'px'] : []; })()"""


YEARLINE = """(() => { const out = [];
  for (const y of document.querySelectorAll('.tl-y, .ry-y')) {
    const n = [...y.childNodes].find(x => x.nodeType === 3 && x.textContent.trim()); if (!n) continue;
    const r = document.createRange(); r.selectNodeContents(n); const rects = [...r.getClientRects()].filter(x => x.width > .5);
    const cs = getComputedStyle(y), b = y.getBoundingClientRect();
    const left = b.left + parseFloat(cs.paddingLeft), right = b.right - parseFloat(cs.paddingRight);
    const g = r.getBoundingClientRect();
    // three pixels to spare: another browser's figures may set a little wider
    const spare = (right - left) - g.width;
    if (rects.length > 1 || spare < 3 || g.left < left - .5 || g.right > right + .5)
      out.push({year: n.textContent.trim(), lines: rects.length, spare: Math.round(spare * 10) / 10}); }
  return out; })()"""
WALK = """(async () => { const step = Math.round(innerHeight * .4);
  for (let y = 0; y < document.documentElement.scrollHeight; y += step) { scrollTo(0, y); await new Promise(r => setTimeout(r, 90)); }
  scrollTo(0, document.documentElement.scrollHeight); await new Promise(r => setTimeout(r, 1800)); return 1; })()"""
# v7 (QA): R9 measured. Under a title of 40px or more, at least 36px of clear
# space from its lowest ink to the highest ink of the next text in its column
TITLEGAP = r"""(() => { const out = [], cvs = document.createElement('canvas').getContext('2d');
  const font = c => `${c.fontStyle} ${c.fontWeight} ${c.fontSize} ${c.fontFamily}`;
  const m = (c, t) => { cvs.font = font(c); const x = cvs.measureText(t || 'Hxgy');
    return {asc: x.fontBoundingBoxAscent, iasc: x.actualBoundingBoxAscent, idesc: x.actualBoundingBoxDescent}; };
  const closed = el => { for (let e = el; e; e = e.parentElement) { const d = e.parentElement;
    if (d && d.tagName === 'DETAILS' && !d.open && e.tagName !== 'SUMMARY'
        && getComputedStyle(d, '::details-content').contentVisibility !== 'visible') return true; } return false; };
  const T = [], r = document.createRange();
  const tw = document.createTreeWalker(document.querySelector('main'), NodeFilter.SHOW_TEXT, {acceptNode: n => /\S/.test(n.nodeValue) ? 1 : 2});
  for (let n; (n = tw.nextNode());) { const el = n.parentElement;
    if (el.closest('.sr-only,svg,.count>span') || closed(el) || getComputedStyle(el).visibility !== 'visible') continue;
    r.selectNodeContents(n); for (const b of r.getClientRects()) if (b.width > .5) T.push({b, el, n}); }
  for (const h of document.querySelectorAll('main h1, main h2:not(.sr-only), .hero-title, .ph-title, .pp-title')) {
    const hc = getComputedStyle(h); if (parseFloat(hc.fontSize) < 40 || !h.getClientRects().length) continue;
    const hr = h.getBoundingClientRect(); let next = null, best = 1e9;
    for (const t of T) { if (h.contains(t.el) || t.b.top < hr.bottom - 4 || t.b.right < hr.left || t.b.left > hr.right) continue;
      if (t.b.top - hr.bottom < best) { best = t.b.top - hr.bottom; next = t; } }
    if (!next || best > 400) continue;
    r.selectNodeContents(h); const rs = [...r.getClientRects()].filter(b => b.width > .5); const last = rs[rs.length - 1];
    let le = h; const w = document.createTreeWalker(h, NodeFilter.SHOW_TEXT); for (let n; (n = w.nextNode());) if (/\S/.test(n.nodeValue) && !n.parentElement.closest('.sr-only')) le = n.parentElement;
    const words = (le.textContent || '').trim().split(/\s+/).slice(-3).join(' ');
    const mh = m(getComputedStyle(le), words), inkB = last.top + mh.asc + mh.idesc;
    const nt = (next.n.nodeValue || '').trim().split(/\s+/).slice(0, 3).join(' ');
    const mn = m(getComputedStyle(next.el), nt), inkT = next.b.top + mn.asc - mn.iasc;
    const gap = inkT - inkB, size = parseFloat(hc.fontSize);
    if (gap < 35.5) out.push({h: (h.textContent || '').trim().slice(0, 30), size: Math.round(size), gap: Math.round(gap * 10) / 10});
    // and not more than half as much again under a page's title (chief designer v7: a
    // phone programme head's grid added 28px under the title and the lead)
    else if (h.matches('h1:not(.hero-title), .pp-title, .ph-title') && gap > 1.5 * Math.max(36, 0.6 * size)
             && next.el.closest('.ph, .pp-head') === h.closest('.ph, .pp-head'))   // the head's own next text
      out.push({h: (h.textContent || '').trim().slice(0, 30), size: Math.round(size), gap: Math.round(gap * 10) / 10, over: true});
  }
  return out; })()"""

# v7: the other language is one quiet word (Andrew, 4 Oct 2026: "far too big"):
# one visible link, to this page's twin, no capitals or tracking, weight 500 at
# most, smaller than the nav words, no rule until it is hovered
LANG = r"""(() => { const out = [];
  const vis = [...document.querySelectorAll('.lang')].filter(a => a.offsetParent !== null);
  if (vis.length !== 1) return [{visible: vis.length}];
  const a = vis[0], cs = getComputedStyle(a), size = parseFloat(cs.fontSize), weight = parseInt(cs.fontWeight);
  const twin = p => p.replace('/ko/', '/');
  if (twin(location.pathname) !== twin(new URL(a.href).pathname)) out.push({href: a.getAttribute('href')});
  if (weight > 500) out.push({weight});
  if (size > 15.5) out.push({size});
  if (cs.textTransform !== 'none' || parseFloat(cs.letterSpacing) > 0.5) out.push({transform: cs.textTransform, track: cs.letterSpacing});
  if (cs.textDecorationLine.includes('underline') && !/rgba\(0, 0, 0, 0\)|transparent/.test(cs.textDecorationColor))
    out.push({underline: cs.textDecorationColor});
  const nav = document.querySelector('.nav-link');
  if (nav && nav.offsetParent !== null && size >= parseFloat(getComputedStyle(nav).fontSize))
    out.push({size, nav: parseFloat(getComputedStyle(nav).fontSize)});
  return out; })()"""

# v7: a timeline dot is always a filled dot (R17: an open ring means a
# performance); with motion on, stand where some rows are above the middle of
# the screen and some below, and look at every dot
INWORD = r"""(() => { const out = [], seen = new Set();
  const roots = document.querySelectorAll('main, .site-header, .site-footer');
  for (const root of roots) {
    const tw = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    for (let n = tw.nextNode(); n; n = tw.nextNode()) {
      const el = n.parentElement; if (!el || el.closest('.sr-only,svg,script,style,textarea,option,[hidden],.count')) continue;
      const cs = getComputedStyle(el); if (cs.visibility === 'hidden' || cs.display === 'none') continue;
      const t = n.data; const re = /[^\s ⁠​]+/g; let m;
      while ((m = re.exec(t))) {
        const word = m[0]; if (word.length < 2 || /@|:\/\/|www\./.test(word)) continue;
        // a break after a hyphen, a dash, a slash, a list dot or a tilde is a line break
        // and so is a break before an opening bracket or quote
        const pieces = word.split(/(?<=[-‐‑–—\/·~])|(?=[(\[“‘「])/); let off = m.index;
        for (const pc of pieces) {
          if (pc.length >= 2) {
            const r = document.createRange(); r.setStart(n, off); r.setEnd(n, off + pc.length);
            const tops = new Set(); for (const x of r.getClientRects()) if (x.width > .5 && x.height > .5) tops.add(Math.round(x.top / 3));
            if (tops.size > 1) { const k = word + '|' + (el.className || el.tagName);
              if (!seen.has(k)) { seen.add(k); out.push(word + ' (' + (typeof el.className === 'string' && el.className ? el.className : el.tagName) + ')'); } }
          }
          off += pc.length;
        }
      }
    }
  }
  return out.slice(0, 20); })()"""

# a long name kept whole by an inline block (layout._name_tie) may wrap between its words only
# where the column is narrower than the name; anywhere else it should have moved down whole
TN = r"""(() => { const out = [];
  for (const e of document.querySelectorAll('main .tn, .site-footer .tn')) {
    const r = document.createRange(); r.selectNodeContents(e);
    const tops = new Set([...r.getClientRects()].filter(x => x.width > .5).map(x => Math.round(x.top / 3)));
    if (tops.size < 2) continue;
    const c = e.cloneNode(true); c.style.cssText = 'position:absolute;visibility:hidden;white-space:nowrap;display:inline-block';
    e.parentElement.appendChild(c); const w = c.getBoundingClientRect().width; c.remove();
    let b = e.parentElement; while (b && getComputedStyle(b).display.startsWith('inline')) b = b.parentElement;
    const cs = getComputedStyle(b), avail = b.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
    if (w <= avail - 1) out.push('tn ' + e.textContent + ' ' + Math.round(w) + '/' + Math.round(avail));
  }
  return out; })()"""

KINSOKU = r"""(() => { const out = [], ko = document.documentElement.lang.startsWith('ko');
  const START = /[,.;:!?)\u2019\u201d\u300d\u300f]/, END = /[(\u2018\u201c\u300c\u300e]/;
  const blockOf = el => { let b = el; while (b && getComputedStyle(b).display.startsWith('inline')) b = b.parentElement; return b; };
  const groups = new Map();
  for (const root of document.querySelectorAll('main, .site-footer')) {
    const tw = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    for (let n = tw.nextNode(); n; n = tw.nextNode()) {
      const el = n.parentElement; if (!el || el.closest('.sr-only,svg,script,style,textarea,option,[hidden],.count')) continue;
      const cs = getComputedStyle(el); if (cs.visibility === 'hidden' || cs.display === 'none') continue;
      const b = blockOf(el); if (!groups.has(b)) groups.set(b, []); groups.get(b).push(n);
    }
  }
  const rect = (n, i) => { const r = document.createRange(); r.setStart(n, i); r.setEnd(n, i + 1); return r.getClientRects()[0]; };
  const same = (a, b) => Math.abs((a.top + a.bottom) / 2 - (b.top + b.bottom) / 2) < Math.min(a.height, b.height) / 2;
  const say = (n, i) => n.data.slice(Math.max(0, i - 14), i + 14).replace(/\s+/g, ' ');
  for (const [b, nodes] of groups) {
    const cs = [], at = new Map();
    for (const n of nodes) { const idx = []; for (let i = 0; i < n.data.length; i++) {
      if (!/[\s\u00a0\u2060\u200b]/.test(n.data[i])) { idx[i] = cs.length; cs.push([n, i]); } } at.set(n, idx); }
    for (let k = 0; k < cs.length; k++) {
      const [n, i] = cs[k], ch = n.data[i];
      if (START.test(ch) && k > 0) { const a = rect(...cs[k - 1]), c = rect(n, i); if (a && c && !same(a, c)) out.push('starts ' + ch + ' | ' + say(n, i)); }
      if (END.test(ch) && k + 1 < cs.length) { const a = rect(n, i), c = rect(...cs[k + 1]); if (a && c && !same(a, c)) out.push('ends ' + ch + ' | ' + say(n, i)); }
    }
    if (ko) continue;
    for (const n of nodes) { const re = /\b(?:a|an|the|A|An|The)(?=[\s\u00a0])/g; let m;
      while ((m = re.exec(n.data))) { const last = at.get(n)[m.index + m[0].length - 1]; if (last === undefined || last + 1 >= cs.length) continue;
        const a = rect(n, m.index + m[0].length - 1), c = rect(...cs[last + 1]); if (a && c && !same(a, c)) out.push('ends with ' + m[0] + ' | ' + say(n, m.index)); } }
  }
  return [...new Set(out)].slice(0, 15); })()"""

# R25: the four facts under a head (About, programme pages) have their second column on
# the content line, within 1px (a probe set on --col4 in the same wrap gives the line)
COLLINE = r"""(() => { const out = [];
  for (const g of document.querySelectorAll('main :is(.glance,.pp-glance)')) {
    const cells = g.children; if (cells.length < 4 || getComputedStyle(g).gridTemplateColumns.split(' ').length < 4) continue;
    const p = document.createElement('div'); p.style.cssText = 'height:1px;margin-inline-start:var(--col4)'; g.parentElement.insertBefore(p, g);
    const line = p.getBoundingClientRect().left; p.remove();
    const x = cells[1].getBoundingClientRect().left; if (Math.abs(x - line) > 1) out.push((g.className || '') + ' ' + Math.round(x) + ' vs ' + Math.round(line));
  }
  return out; })()"""

# a long name's block that wraps (wider than its column) never leaves a word alone on the
# line before it (chief designer v7: "At / the National Concert / Hall," at 320px)
LONE = r"""(() => { const out = [];
  for (const e of document.querySelectorAll('main .tn')) {
    const r = document.createRange(); r.selectNodeContents(e);
    const rs = [...r.getClientRects()].filter(x => x.width > .5); if (!rs.length) continue;
    const tops = new Set(rs.map(x => Math.round(x.top / 3))); if (tops.size < 2) continue;
    let b = e.parentElement; while (b && getComputedStyle(b).display.startsWith('inline')) b = b.parentElement;
    const q = document.createRange(); q.setStart(b, 0); q.setEndBefore(e);
    const before = [...q.getClientRects()].filter(x => x.width > .5);
    if (!before.length) continue;
    const lastTop = Math.max(...before.map(x => x.top)), line = before.filter(x => Math.abs(x.top - lastTop) < 3);
    const words = q.toString().trim().split(/\s+/), w = line.reduce((s, x) => s + x.width, 0);
    if (rs[0].top > lastTop + 2 && w < 0.25 * b.clientWidth) out.push('lone word before ' + e.textContent.slice(0, 30) + ' | ' + words.slice(-2).join(' '));
  }
  return out; })()"""

# R22 inside the head: the About head's rings lie under no word of the head
PHRINGS = r"""(() => { const h = document.querySelector('.ph'); if (!h) return [];
  // the head's own rings (a phone), or on a laptop the ones that leave its photograph
  let src = h, ps = getComputedStyle(h, '::before');
  if (ps.content === 'none') { const f = h.querySelector('.ph-figure'); if (f) { src = f; ps = getComputedStyle(f, '::before'); } }
  if (ps.content === 'none' || ps.display === 'none') return [];
  const hb = src.getBoundingClientRect(), w = parseFloat(ps.width);
  const centred = ps.translate && ps.translate !== 'none';
  const cx = centred ? hb.left + parseFloat(ps.left) : hb.right - parseFloat(ps.right) - w / 2;
  const cy = centred ? hb.top + parseFloat(ps.top) : hb.top + parseFloat(ps.top) + w / 2;
  const stops = (ps.maskImage || ps.webkitMaskImage || '').match(/([\d.]+)%/g) || ['16%', '62%'];
  const a = parseFloat(stops[0]) / 100, z = parseFloat(stops[1]) / 100, rv = (a + .75 * (z - a)) * w * Math.SQRT1_2;
  const out = [], tw = document.createTreeWalker(h, NodeFilter.SHOW_TEXT);
  for (let n = tw.nextNode(); n; n = tw.nextNode()) {
    const el = n.parentElement; if (!el || el.closest('.photo,.sr-only') || !n.data.trim()) continue;
    const r = document.createRange(); r.selectNodeContents(n);
    for (const x of r.getClientRects()) { if (x.width < 1) continue;
      const dx = Math.max(x.left - cx, 0, cx - x.right), dy = Math.max(x.top - cy, 0, cy - x.bottom);
      if (Math.hypot(dx, dy) < rv) out.push(n.data.trim().slice(0, 24) + ' ' + Math.round(Math.hypot(dx, dy)) + '/' + Math.round(rv)); }
  }
  return out; })()"""

SENT = (".qa dd,.lead,.ph-lead,.sh-lead,.figs-note,.pi-text,.wa-v,.footer-status,.tl-text,.pv-intro,"
        ".step-t,.ct-how,.map-cap")
SENT_NARROW = ".pp-say,.join-hint,.ct-hint,.ct-help"   # a line each only below 48em
SENTENCES = r"""((sel, wrapped) => { const out = [], ko = document.documentElement.lang.startsWith('ko');
  const end = ko ? /[.!?][’”)]?\s+(?=\S)/g : /[.!?][’”)]?\s+(?=[A-Z0-9“‘(])/g;
  const abbr = /\b(Co|St|Dr|Mr|Mrs|Ms|Fr|Sr|Rev|No|approx|e\.g|i\.e|etc|vs)$/;
  for (const b of document.querySelectorAll(sel)) {
    const cs = getComputedStyle(b); if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    const box = b.getBoundingClientRect(); if (box.width < 2) continue;
    // a block whose sentences sit side by side where it fits one line is read only once it wraps
    if (wrapped) { const rr = document.createRange(); rr.selectNodeContents(b);
      if (new Set([...rr.getClientRects()].filter(x => x.width > .5).map(x => Math.round(x.top / 4))).size < 2) continue; }
    const nodes = [], tw = document.createTreeWalker(b, NodeFilter.SHOW_TEXT); let text = '';
    for (let n = tw.nextNode(); n; n = tw.nextNode()) { if (n.parentElement.closest('.sr-only')) continue;
      nodes.push([n, text.length]); text += n.data; }
    let m, prev = 0;
    while ((m = end.exec(text))) {
      const before = text.slice(prev, m.index + 1).trim(); const at = m.index + m[0].length;
      if (abbr.test(text.slice(Math.max(0, m.index - 8), m.index))) continue;
      const one = before.split(/\s+/).length <= 1; prev = at;
      if (one) continue;
      let node = null, off = 0;
      for (const [n, s0] of nodes) if (at >= s0 && at < s0 + n.data.length) { node = n; off = at - s0; }
      if (!node) continue;
      const r = document.createRange(); r.setStart(node, off); r.setEnd(node, Math.min(node.data.length, off + 1));
      const rc = r.getClientRects()[0]; if (!rc) continue;
      // the full stop before it, on the same line, whatever the block's alignment
      let pn = null, po = 0;
      for (const [n, s0] of nodes) if (m.index >= s0 && m.index < s0 + n.data.length) { pn = n; po = m.index - s0; }
      if (!pn) continue;
      const q = document.createRange(); q.setStart(pn, po); q.setEnd(pn, po + 1);
      const pc = q.getClientRects()[0]; if (!pc) continue;
      if (Math.abs((pc.top + pc.bottom) / 2 - (rc.top + rc.bottom) / 2) < Math.min(pc.height, rc.height) / 2)
        out.push(text.slice(at, at + 28) + ' (' + (b.className || b.tagName) + ')');
    }
  }
  return out.slice(0, 12); })"""

HERORINGS = r"""(() => { const f = document.querySelector('.hero-figure'); if (!f) return [];
  const ps = getComputedStyle(f, '::before'); if (ps.content === 'none' || ps.display === 'none') return [];
  const fb = f.getBoundingClientRect(), w = parseFloat(ps.width);
  const cx = fb.left + parseFloat(ps.left), cy = fb.top + parseFloat(ps.top) + (parseFloat(ps.marginTop) || 0);
  // the mask is opaque to 22% of the far corner and gone at its end (64% on a wide
  // screen, 56% below 75em): three quarters of the way the rings can still be seen
  const stops = (ps.maskImage || ps.webkitMaskImage || '').match(/([\d.]+)%/g) || ['22%', '64%'];
  const end = parseFloat(stops[1]) / 100;
  const rv = (.22 + .75 * (end - .22)) * w * Math.SQRT1_2;
  // and they fade out above the photograph's bottom edge: nothing below it is under them
  const cut = /linear-gradient/.test(ps.maskImage || ps.webkitMaskImage || '');
  const ph = f.querySelector('.photo').getBoundingClientRect(), out = [];
  const tw = document.createTreeWalker(document.querySelector('.hero'), NodeFilter.SHOW_TEXT);
  for (let n = tw.nextNode(); n; n = tw.nextNode()) {
    // the caption is read too (v7 D1 F10: centred on a full-width photograph the rings ran under it)
    const el = n.parentElement; if (!el || el.closest('.photo,.sr-only') || !n.data.trim()) continue;
    const btn = el.closest('.btn'); if (btn && getComputedStyle(btn).backgroundColor !== 'rgba(0, 0, 0, 0)') continue;
    const r = document.createRange(); r.selectNodeContents(n);
    for (const x of r.getClientRects()) {
      if (x.width < 1) continue;
      const dx = Math.max(x.left - cx, 0, cx - x.right), dy = Math.max(x.top - cy, 0, cy - x.bottom);
      const under = (x.top >= ph.top && x.bottom <= ph.bottom && x.left >= ph.left) || (cut && x.top >= ph.bottom - 1);
      if (!under && Math.hypot(dx, dy) < rv) out.push(n.data.trim().slice(0, 24) + ' ' + Math.round(Math.hypot(dx, dy)) + '/' + Math.round(rv));
    }
  }
  return out; })()"""

DOTS = r"""(() => { const tl = document.querySelector('.timeline'); if (!tl) return [];
  window.scrollTo(0, tl.getBoundingClientRect().top + scrollY - innerHeight * 0.3);
  return new Promise(r => setTimeout(() => { const out = [];
    const sec = tl.closest('section'), ground = getComputedStyle(sec).backgroundColor;
    const bg = /rgba\(0, 0, 0, 0\)/.test(ground) ? getComputedStyle(document.body).backgroundColor : ground;
    for (const li of tl.querySelectorAll('.tl-item')) {
      const c = getComputedStyle(li, '::before').backgroundColor;
      if (/rgba\(0, 0, 0, 0\)|transparent/.test(c) || c === bg) out.push((li.querySelector('h3') || li).textContent.slice(0, 30));
    }
    r(out); }, 900)); })()"""

UNSEEN = """(() => { const out = [];
  for (const e of document.querySelectorAll('main *')) {
    if (e.closest('.arrow, .sr-only, [hidden]')) continue;
    const fold = e.closest('details:not([open])'); if (fold && !e.closest('summary') && getComputedStyle(fold).display !== 'none'
        && !e.closest('.ry-fold')) continue;
    const cs = getComputedStyle(e); if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    const b = e.getBoundingClientRect(); if (b.width < 1 || b.height < 1) continue;
    if (parseFloat(cs.opacity) < .99) out.push((e.className && e.className.baseVal === undefined ? e.className : e.tagName) + ' ' + cs.opacity); }
  for (const m of document.querySelectorAll('main mark')) {
    const bs = getComputedStyle(m).backgroundSize; if (!/^100%/.test(bs)) out.push('mark "' + m.textContent.slice(0, 20) + '" ' + bs); }
  // v7: the drawings' lines draw themselves; none may be left short of its length
  for (const e of document.querySelectorAll('main :is(.meet-list li,.meet-list,.route-st,.played,.wa-based dt,.seat,.seats,.steps li,.tl-item)')) {
    for (const pe of ['::before', '::after']) {
      const cs = getComputedStyle(e, pe); if (cs.content === 'none' || cs.display === 'none') continue;
      const sc = cs.scale; if (sc && sc !== 'none' && sc.split(' ').some(v => parseFloat(v) < .99))
        out.push((typeof e.className === 'string' ? e.className : e.tagName) + pe + ' scale ' + sc); } }
  return [...new Set(out)].slice(0, 12); })()"""


def main(strict=False):
    httpd, base = serve()
    found = {"fold": [], "tail": [], "tie": [], "hero": [], "axis": [], "width": [], "group": [], "meet": [],
             "leader": [], "names": [], "rings": [], "faces": [], "twins": [], "marks": [], "gallery": [],
             "years": [], "venues": [], "yearline": [], "motion": [], "wide": [], "lang": [], "dots": [],
             "titlegap": [], "inword": [], "sentences": [], "herorings": [], "kinsoku": [], "colline": [],
             "lone": [], "phrings": [], "shsize": [], "steps": []}
    try:
        with Chrome(port=9371, width=1440, height=900) as c:
            for lang in ("en", "ko"):
                for pg in PAGES:
                    for w, h in VIEWPORTS:
                        mobile = w < 700
                        c.viewport(w, h, 2 if mobile else 1, mobile)
                        c.goto(base + ("" if lang == "en" else "ko/") + pg + ".html", settle=0.4)
                        c.js("Promise.race([document.fonts.ready.then(()=>1),new Promise(r=>setTimeout(()=>r(0),5000))])")
                        r = c.js(f"({JS})({json.dumps(LEADS)}, {json.dumps(SHORT)}, {'true' if w >= 1024 else 'false'})")
                        found["fold"] += [(lang, pg, w, x) for x in r["fold"]]
                        found["tail"] += [(lang, pg, w, x) for x in r["tail"]
                                          if not any(pg == a and w == b and c in x["text"] for a, b, c in ACCEPT_TAIL)]
                        found["tie"] += [(lang, pg, w, x) for x in r["tie"] if not any(a in x for a in ALLOW)]
                        found["tie"] += [(lang, pg, w, x) for x in c.js(TN)]
                        found["faces"] += [(lang, pg, w, x) for x in c.js(FACES)]
                        found["marks"] += [(lang, pg, w, x) for x in c.js(MARKS)]
                        found["years"] += [(lang, pg, w, x) for x in c.js(YEARS)]
                        found["yearline"] += [(lang, pg, w, x) for x in c.js(YEARLINE)]
                        found["lang"] += [(lang, pg, w, x) for x in c.js(LANG)]
                        found["titlegap"] += [(lang, pg, w, x) for x in c.js(TITLEGAP)]
                        found["inword"] += [(lang, pg, w, x) for x in c.js(INWORD)]
                        found["kinsoku"] += [(lang, pg, w, x) for x in c.js(KINSOKU)]
                        found["sentences"] += [(lang, pg, w, x) for x in c.js(f"({SENTENCES})({json.dumps(SENT + (',' + SENT_NARROW if w < 768 else ''))}, false)")]
                        if w >= 768:
                            found["sentences"] += [(lang, pg, w, x) for x in c.js(f"({SENTENCES})({json.dumps(SENT_NARROW)}, true)")]
                        if w >= 1024:
                            found["colline"] += [(lang, pg, w, x) for x in c.js(COLLINE)]
                        found["lone"] += [(lang, pg, w, x) for x in c.js(LONE)]
                        if w < 880:
                            found["shsize"] += [(lang, pg, w, x) for x in c.js(SHSIZE)]
                        if w == 390:
                            found["steps"] += [(lang, pg, w, x) for x in c.js(f"({STEPS})({json.dumps(STEP_SEL)})")]
                            found["venues"] += [(lang, pg, w, x) for x in c.js(f"({VENUES_JS})({json.dumps(VENUES)}, {json.dumps(STEP_SEL)})")]
                        if pg == "about":
                            found["phrings"] += [(lang, w, x) for x in c.js(PHRINGS)]
                        if lang == "en" and w >= 1024:
                            found["venues"] += [(pg, w, x) for x in c.js(f"({VENUES_JS})({json.dumps(VENUES)})")]
                for w, h in ((1440, 789), (1366, 768), (1280, 720), (1024, 768), (820, 1180), (768, 1024), (390, 844)):
                    c.viewport(w, h, 2 if w < 700 else 1, w < 700)
                    c.goto(base + ("" if lang == "en" else "ko/") + "index.html", settle=0.8)
                    c.js("Promise.race([document.fonts.ready.then(()=>1),new Promise(r=>setTimeout(()=>r(0),5000))])")
                    hero = c.js(HERO)
                    lo, hi = (0.5, 0.7) if lang == "en" else (0.36, 0.6)
                    # under 90px the 36px ink floor (R9) wins over R15's 0.7 (at 86px it asks 0.72)
                    hi = hi + .03 if hero["size"] < 90 else hi
                    if ((hero["size"] >= 72 and not lo <= hero["ratio"] <= hi) or hero["ink"] < 36
                            or hero["group"] < 1.25 or hero["button"] > hero["height"]):
                        found["hero"].append((lang, w, h, hero))
                    axis = c.js(AXIS)
                    if axis["spread"] > 1:
                        found["axis"].append((lang, w, h, axis))
                    width = c.js(WIDTH)
                    if (width["lines"] == 1 and abs(width["d"]) > 3) or (width["lines"] > 1 and width["sub"] > width["title"] + 1):
                        found["width"].append((lang, w, h, width))
                # the hero's rings on a phone and a tablet lie under no word
                for w, h in ((320, 700), (360, 740), (390, 844), (768, 1024), (820, 1180),
                             (1024, 768), (1280, 720), (1366, 768), (1440, 789), (1728, 1000)):
                    c.viewport(w, h, 2 if w < 700 else 1, w < 700)
                    c.goto(base + ("" if lang == "en" else "ko/") + "index.html", settle=0.4)
                    c.js("Promise.race([document.fonts.ready.then(()=>1),new Promise(r=>setTimeout(()=>r(0),5000))])")
                    found["herorings"] += [(lang, w, h, x) for x in c.js(HERORINGS)]
                for w in (1024, 1100, 1280, 1440):
                    c.viewport(w, 900, 1, False)
                    for pg, specs in (("index", CARD_ROWS + FIGS_ROWS), ("news", LATEST_ROWS),
                                      ("get-involved", PLAYED_ROWS), ("programmes", PLAYED_ROWS)):
                        c.goto(base + ("" if lang == "en" else "ko/") + pg + ".html", settle=0.4)
                        c.js("Promise.race([document.fonts.ready.then(()=>1),new Promise(r=>setTimeout(()=>r(0),5000))])")
                        for card, *parts in specs:
                            found["group"] += [(lang, w, x) for x in c.js(f"({GROUP})({json.dumps(card)}, {json.dumps(parts)})")]
                # R23: names kept whole; R22: a head's rings on no drawing, in their own band
                for pg in ("index", "contact"):
                    for w in (390, 768, 1024, 1280, 1440, 1920):
                        c.viewport(w, 900, 2 if w < 700 else 1, w < 700)
                        c.goto(base + ("" if lang == "en" else "ko/") + pg + ".html", settle=0.4)
                        c.js("Promise.race([document.fonts.ready.then(()=>1),new Promise(r=>setTimeout(()=>r(0),5000))])")
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
                        c.js("Promise.race([document.fonts.ready.then(()=>1),new Promise(r=>setTimeout(()=>r(0),5000))])")
                        found["meet"] += [(lang, w, zoom, x) for x in c.js(MEET)]
                    for w in (390, 768, 1024, 1280, 1440):
                        c.viewport(w, 900, 2 if w < 700 else 1, w < 700)
                        c.goto(base + ("" if lang == "en" else "ko/") + "contact.html", settle=0.4)
                        c.js("Promise.race([document.fonts.ready.then(()=>1),new Promise(r=>setTimeout(()=>r(0),5000))])")
                        r = c.js(LEADER)
                        if r:
                            found["leader"].append((lang, w, zoom, r))
                # back to the reader's usual text size: the drawings pass above ends
                # at 200%, and what follows is measured at 100% (v6: the gallery check
                # ran at 200% and measured a page that was not the one meant)
                text_size(c, 16)
                # R6, R13: a Garamond figure is one size in both languages (once,
                # with the Korean pass); v6: the News gallery's rows
                if lang == "ko":
                    for pg in ("index", "news"):
                        for w in (390, 1024, 1440):
                            sizes = {}
                            for l2 in ("en", "ko"):
                                c.viewport(w, 900, 2 if w < 700 else 1, w < 700)
                                c.goto(base + ("" if l2 == "en" else "ko/") + pg + ".html", settle=0.4)
                                sizes[l2] = c.js(f"({TWINS_JS})({json.dumps(TWINS)})")
                            for sel in TWINS:
                                a, b = sizes["en"].get(sel), sizes["ko"].get(sel)
                                if a and b and abs(a - b) > 0.5:
                                    found["twins"].append((pg, w, sel, {"en": a, "ko": b}))
                for w in (390, 768, 1024, 1280, 1440):
                    c.viewport(w, 900, 2 if w < 700 else 1, w < 700)
                    c.goto(base + ("" if lang == "en" else "ko/") + "news.html", settle=0.4)
                    # every photograph loaded; one the local server dropped is asked
                    # for again (twice) before it counts as missing
                    for _ in range(3):
                        c.js("""Promise.race([Promise.all([...document.querySelectorAll('.gallery img')].map(i => { i.loading = 'eager';
                          if (i.complete && i.naturalWidth === 0) { const s = i.srcset; i.srcset = ''; i.srcset = s; i.src = i.src; }
                          return (i.complete && i.naturalWidth) ? 1 : new Promise(r => { i.onload = i.onerror = r; }); })),
                          new Promise(r => setTimeout(r, 8000))])""")
                    found["gallery"] += [(lang, w, x) for x in c.js(GALLERY)]
                # the years on wide screens too (the timeline's grew to 2.1rem)
                for w in (1512, 1728):
                    c.viewport(w, 900, 1, False)
                    c.goto(base + ("" if lang == "en" else "ko/") + "news.html", settle=0.4)
                    found["yearline"] += [(lang, "news", w, x) for x in c.js(YEARLINE)]
                # with motion on, nothing animated in is left unseen
                c.motion(True)
                for pg in PAGES:
                    for w in (1440, 390):
                        c.viewport(w, 900 if w > 700 else 844, 2 if w < 700 else 1, w < 700)
                        c.goto(base + ("" if lang == "en" else "ko/") + pg + ".html", settle=0.4)
                        c.js(WALK)
                        found["motion"] += [(lang, pg, w, x) for x in c.js(UNSEEN)]
                        if pg == "news":
                            found["dots"] += [(lang, w, x) for x in c.js(DOTS)]
                c.motion(False)
                # text at 200%, every page: nothing past the edge of the screen
                text_size(c, 32)
                for pg in PAGES:
                    for w in (320, 390, 768, 1280):
                        c.viewport(w, 900, 2 if w < 700 else 1, w < 700)
                        c.goto(base + ("" if lang == "en" else "ko/") + pg + ".html", settle=0.4)
                        c.js("Promise.race([document.fonts.ready.then(()=>1),new Promise(r=>setTimeout(()=>r(0),5000))])")
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
