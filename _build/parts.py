# -*- coding: utf-8 -*-
"""The markup of the six pages, written once for both languages.

Since 2026-10-01 the content files hold copy and nothing else: each language
fills the same deck of strings, and the functions here turn a deck into a
page. The two languages therefore cannot drift apart in structure, which is
how the Korean pages fell behind the English ones more than once. A section
added here appears in both languages, and a missing string fails the build
rather than shipping a half-empty block.

Every path is written root-relative (`images/x.jpg`, `programmes.html`);
layout.py adds the prefix each page needs. Class names are the contract with
styles.css; the sections of that file follow the order of this one.
"""

import math
import os
import re

import artifacts
import ledger
from icons import glyph
from layout import ROOT, STR

# One arrow on the whole site, drawn (v5). "\u2192" is in none of the font
# subsets the site loads, so every device drew it from its own fonts: Times
# after a Garamond name, the system sans elsewhere, Noto on Korean pages. The
# second arrow waits 1.3em to the left and slides in on hover (styles.css).
ARROW = ('<span class="arrow" aria-hidden="true"><i><svg viewBox="0 0 16 16" focusable="false">'
         '<path d="M2.4 9h10.4M9.4 5.4 13 9l-3.6 3.6"/><path d="M-18.4 9h10.4M-11.4 5.4-7.8 9l-3.6 3.6"/>'
         '</svg></i></span>')


# ---------------------------------------------------------------------------
# small pieces
# ---------------------------------------------------------------------------

def btn(href, label, kind="quiet"):
    return f'<a class="btn btn-{kind}" href="{href}">{label} {ARROW}</a>'


def go(href, label):
    return f'<a class="go" href="{href}">{label} {ARROW}</a>'


def eyebrow(text, no=None, cls="", hidden=False):
    # a Roman numeral takes a full stop, as in a concert programme ("I. What
    # we do"): at the label's size a bare "I" could be read as the word
    # (chief designer v2, P3-3)
    n = f'<span class="no">{no}{"." if no and not no.strip("IVX") else ""}</span>' if no else ""
    c = f"eyebrow {cls}".strip()
    h = ' aria-hidden="true"' if hidden else ""
    return f'<p class="{c}"{h}>{n}{text}</p>'


def sh(label, h2, lead=None, no=None, split=False, cls=""):
    """A section head: a label in the margin, the heading, one paragraph.
    The label names the section (Andrew, 2 Oct 2026 evening: it is what tells
    a reader where they are, so it is set to be read, styles.css
    .section-label). A screen reader hears it as part of the heading ("What
    we do: Five programmes."); the visible copy is hidden from it, so it is
    not read twice."""
    lead_ = f'\n      <p class="sh-lead">{lead}</p>' if lead else ""
    c = "sh" + (" sh-split" if split else "") + (f" {cls}" if cls else "")
    label_ = eyebrow(label, no, "section-label", hidden=True)
    h2_ = f'<h2><span class="sr-only">{label}: </span>{h2}</h2>'
    if split:
        return (f'    <header class="{c}">\n      {label_}\n'
                f'      <div>{h2_}{lead_}</div>\n    </header>')
    return f'    <header class="{c}">\n      {label_}\n      {h2_}{lead_}\n    </header>'


# How wide each kind of photograph is drawn, for the browser to pick a file.
# Every photograph has an 800px copy beside it (images/<name>-800.jpg, made
# by _build/add-photo.sh); a card 240px wide on a laptop takes that one
# instead of the 1400px original.
SIZES = {
    "card": "(max-width:40em) 92vw, (max-width:64em) 46vw, 240px",
    "half": "(max-width:55em) 92vw, 46vw",
    "gallery": "(max-width:35em) 92vw, (max-width:55em) 46vw, 33vw",
    "wide": "100vw",
    "hero": "(max-width:55em) 100vw, 54vw",
    "founder": "(max-width:55em) 440px, 34vw",
    "head": "(max-width:55em) 100vw, 66vw",
    # nine of twelve columns of the wrap (at most about 880px); a portrait plate
    # stops at 460px
    "room": "(max-width:55em) 92vw, min(65vw, 880px)",
    "room-portrait": "(max-width:55em) 92vw, 460px",
}


def _srcset(src, w, sizes):
    small = src[:-4] + "-800.jpg"
    if not sizes or w <= 800 or not os.path.exists(os.path.join(ROOT, "images", small)):
        return ""
    # a key of SIZES, or a sizes list worked out for one photograph (the gallery)
    return f' srcset="images/{small} 800w, images/{src} {w}w" sizes="{SIZES.get(sizes, sizes)}"'


def photo(img, ratio="", sizes=None):
    """img is (src, width, height, alt). The ratio class is optional where the
    component sets the shape. sizes is a key of SIZES. Since 2026-10-01 a
    photograph never carries a view-transition name: the programme covers do
    (cover() below), so what travels between pages is the same drawing."""
    src, w, h, alt = img
    r = f" photo-{ratio}" if ratio else ""
    return (f'<div class="photo{r}"><img src="images/{src}"{_srcset(src, w, sizes)} '
            f'width="{w}" height="{h}" alt="{alt}"></div>')


_CREDIT = re.compile(r"\s·\s((?:photo|사진):\s.+)$")


def _credited(text):
    """The photographer's credit on a line of its own, without the dot that
    joined it ("…August 2026 · / photo: …" broke at the dot, CD v6)."""
    m = _CREDIT.search(text)
    if not m:
        return f"<span>{text}</span>"
    return f'<span>{text[:m.start()]}</span><span class="cap-credit">{m.group(1)}</span>'


def caption(cap):
    """cap is (label, text) or a plain string or None."""
    if not cap:
        return ""
    if isinstance(cap, tuple):
        label, text = cap
        return f'<figcaption><span class="cap-label">{label}</span>{_credited(text)}</figcaption>'
    if _CREDIT.search(cap):
        return f"<figcaption>{_credited(cap)}</figcaption>"
    return f"<figcaption>{cap}</figcaption>"


def plate(img, ratio="", cap=None, cls="", sizes="half"):
    """A photograph as a printed plate, with its true caption."""
    c = f"plate {cls}".strip()
    return f'<figure class="{c}">{photo(img, ratio, sizes)}{caption(cap)}</figure>'


def facts(rows, cls=""):
    """Label above or beside its value. cls "facts-plain" sets them without
    rules, label above value (the 4th pass, 2 Oct 2026)."""
    c = f"facts {cls}".strip()
    if "facts-plain" in cls:
        # each pair in its own group, so a pair can sit in a column or a row
        return (f'<dl class="{c}">' + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in rows)
                + "</dl>")
    return (f'<dl class="{c}">' + "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in rows)
            + "</dl>")


# ---------------------------------------------------------------------------
# Patterns that replace running text (the 4th pass, 2 Oct 2026). Andrew: too
# much running text, hard to read. Each of these says in structure what a
# paragraph used to say in sentences; the reading budget (readability.py)
# keeps the copy inside them short. None needs a box, a tint or a script.
# ---------------------------------------------------------------------------

def leadins(items, cls=""):
    """Three to six parallel points, each with a lead-in in bold: rules,
    rights, principles. items: (lead-in, text)."""
    c = f"leadins {cls}".strip()
    return (f'<ul class="{c}">' + "".join(f"<li><strong>{a}</strong> {b}</li>" for a, b in items)
            + "</ul>")


# ---------------------------------------------------------------------------
# Drawings in place of lists (Andrew, 2 Oct 2026 evening: "not text listed
# one after another, but diagrams and design"). Art direction, v2: one kit of
# stations (a ring holding a line icon), 1px strokes and open rings, drawn in
# HTML and CSS so the words wrap and zoom. Nothing in them is new copy: every
# word is a fact the deck already held.
# ---------------------------------------------------------------------------

# One icon per line of "You provide / We bring", by position and the same in
# both languages; the build stops if a list and its icons differ in length.
MEET_ICONS = ((("room", "calendar", "person"), ("people", "stand", "score")),
              (("room", "person", "announce"), ("recorder", "score")))


def meet(k, title, give, bring, labels):
    """What a host provides and what we bring, drawn: two columns of stations
    bracketed into one stem each, meeting at the event (a concert, a class).
    The DOM reads the event, then each side with its list."""
    gi, bi = MEET_ICONS[k]
    if len(gi) != len(give) or len(bi) != len(bring):
        raise ValueError(f"meet {k}: one icon per line")
    def li(xs, ic, start):
        return "".join(f'<li style="--i:{start + j}"><span class="meet-ico" aria-hidden="true">'
                       f'{glyph(i, "meet-glyph")}</span><span class="meet-t">{x}</span></li>'
                       for j, (x, i) in enumerate(zip(xs, ic)))
    return (f'<div class="meet">'
            f'<h3 class="meet-hub" id="meet-{k}">{title}</h3>'
            f'<div class="meet-side meet-give"><p class="meet-label" id="meet-{k}-g">{labels[0]}</p>'
            f'<ul class="meet-list" aria-labelledby="meet-{k}-g">{li(give, gi, 0)}</ul></div>'
            f'<div class="meet-side meet-bring"><p class="meet-label" id="meet-{k}-b">{labels[1]}</p>'
            f'<ul class="meet-list" aria-labelledby="meet-{k}-b">{li(bring, bi, len(give))}</ul></div>'
            f'</div>')


ROUTE_ICONS = ("people", "mail", "building")   # For, How, Garda vetting; the last station shows its year


def route(rows):
    """The facts of CMFE Artists as a route of stations: who, how and what a
    venue may ask, which are true now. The plan (a row whose name holds a
    year) is not on the route: a line into it read as "register now and it
    leads to paid concerts in 2027" (chief designer v2, R19). It stands
    apart under the route, its year in a ring, joined to nothing. A <dl>:
    the icon sits inside each <dt>, hidden from screen readers."""
    now = [r for r in rows if not re.search(r"\d{4}", r[0])]
    plans = [r for r in rows if re.search(r"\d{4}", r[0])]
    out = []
    for k, (a, b) in enumerate(now):
        mark = f'<span class="route-mark" aria-hidden="true">{glyph(ROUTE_ICONS[k], "route-glyph")}</span>'
        out.append(f'<div class="route-st" style="--i:{k}"><dt>{mark}{a}</dt><dd>{b}</dd></div>')
    plan = "".join(f'<dl class="route-plan"><dt><span class="route-mark route-year" aria-hidden="true">'
                   f'{re.search(r"\d{4}", a).group(0)}</span>{a}</dt><dd>{b}</dd></dl>' for a, b in plans)
    return '<dl class="route">' + "".join(out) + "</dl>" + plan


def played(label, examples):
    """Example programmes on one line of time, oldest first (a line of time
    reads forward; the deck lists them newest first), each on the open dot
    the record strip uses for a performance."""
    sep = '<span class="sr-only">, </span>'
    rows = "".join(f'<li style="--i:{k}"><span class="played-when">{c}</span>{sep}<b class="played-name">{a}</b>'
                   f'{sep}<span class="played-who">{b}</span></li>' for k, (a, b, c) in enumerate(reversed(examples)))
    return f'<h3 class="played-label">{label}</h3><ol class="played">{rows}</ol>'


# a 40 x 21 drawing: the seats stand 6.75/40 of its width from the centre
SEAT_R = 16.875    # cqw: the names stand on a circle this far out from the table's centre
TABLE_R = 12.5     # cqw: the table itself is 25cqw across
# the room a name needs around its point (cqw): the top name stands above it,
# a side name is centred on it (two lines at most); 2cqw clear above and below
NAME_ABOVE, NAME_HALF, TABLE_CLEAR = 5.6, 4.1, 2


def table(roles, roles_label, cond):
    """The board's roles set around a round table, the conditions lying on
    the table. Names, not chairs: five drawn chairs read as a five-member
    board, and no number of seats is said (chief designer v2, R19). The
    build places the names and sizes the box to hug them (a fixed 40:21 box
    left a band of empty table under the lowest names); styles.css draws the
    table, and in a narrow column lists the names under "Roles". The label
    stands on the content line, the drawing in the middle of the column (R2,
    R20)."""
    pts = []
    for k, r in enumerate(roles):
        a = math.radians(-90 + k * 360 / len(roles))
        dx, dy, c = math.cos(a) * SEAT_R, math.sin(a) * SEAT_R, math.cos(a)
        side = "t" if k == 0 else "r" if c > .01 else "l" if c < -.01 else "b"
        above, below = {"t": (NAME_ABOVE, 0), "b": (0, NAME_ABOVE)}.get(side, (NAME_HALF, NAME_HALF))
        pts.append((k, r, a, dx, dy, side, dy - above, dy + below))
    up = max(TABLE_R, -min(p[6] for p in pts)) + TABLE_CLEAR
    h = up + max(TABLE_R, max(p[7] for p in pts)) + TABLE_CLEAR
    seats = "".join(f'<li class="seat seat-{side}" style="--x:{50 + dx:.2f}%;--y:{(up + dy) / h * 100:.2f}%;'
                    f'--a:{math.degrees(a):.0f}deg;--i:{k}">{r}</li>'
                    for k, r, a, dx, dy, side, _, _ in pts)
    return (f'<div class="table-wrap"><p class="seats-label" id="board-roles">{roles_label}</p>'
            f'<div class="table-box"><div class="table" style="--th:{h:.2f};--cy:{up / h * 100:.2f}%">'
            f'<ul class="seats" aria-labelledby="board-roles">{seats}</ul>'
            f'<dl class="table-top"><dt>{cond[0]}</dt><dd>{cond[1]}</dd></dl></div></div></div>')


# who answers, in the order the heading asks it: the person, the languages
# they answer in, what they hold (one icon each, by position)
WHO_ICONS = ("person", "speech", "certificate")


def whereabouts(rows):
    """Contact's details as a drawing (Andrew, 2 Oct 2026 night: "not only
    text"; art direction v3). The island with Dublin marked, a leader from
    the mark to "Based in"; "We travel to" under it, a size up, in the master
    line's roman face (v6: one style a line); the three facts about who answers as stations with no line
    between them (they are not steps). rows: the deck's five pairs in its
    order (Based in, We travel to, Languages, Insurance, Who answers). The
    island is decorative: the two <dl> say every fact in words."""
    if len(rows) != 5:
        raise ValueError("whereabouts: five facts")
    based, travel, langs, insur, who = rows
    svg, place = artifacts.locator()
    st = "".join(f'<div class="wa-st" style="--i:{k + 1}"><dt><span class="wa-ring" aria-hidden="true">'
                 f'{glyph(WHO_ICONS[k], "wa-glyph")}</span>{a}</dt><dd class="wa-v">{b}</dd></div>'
                 for k, (a, b) in enumerate((who, langs, insur)))
    return (f'<div class="wa rv"><div class="wa-top" style="{place}">'
            f'<div class="wa-map">{svg}</div>'
            f'<dl class="wa-where"><div class="wa-based"><dt>{based[0]}</dt><dd>{based[1]}</dd></div>'
            f'<div class="wa-travel"><dt>{travel[0]}</dt><dd>{travel[1]}</dd></div></dl></div>'
            f'<dl class="wa-who">{st}</dl></div>')


def fold(summary, inner, cls=""):
    """Reference most readers do not need, folded: the summary says what is
    inside and how many. Never used for when, where, status or the action."""
    c = f"fold {cls}".strip()
    return f'<details class="{c}"><summary>{summary}</summary>{inner}</details>'


def now_line(p, cls=""):
    """The one programme running now, in two lines: its state and name, then
    when (the value people scan for, in bold) and where."""
    g = p["page"]
    when, where = g["glance"][2][1], g["glance"][1][1]
    c = f"now-line {cls}".strip()
    return (f'<div class="{c}">'
            f'<p class="now-head">{status_tag(g["now"][0], True)}'
            f'<a class="now-name" href="programmes/{p["slug"]}.html">{p["name"]} {ARROW}</a></p>'
            f'<p class="now-when"><strong>{when}</strong><span class="sr-only">, </span>'
            f'<span>{where}</span></p></div>')


def title_lines(lines):
    """A page heading broken where the copy breaks, each line its own mask."""
    return "".join(f'<span class="ln"><span>{ln}</span></span>' for ln in lines)


# ---------------------------------------------------------------------------
# the interior page head, shared by five pages
# ---------------------------------------------------------------------------

def page_head(t):
    """t: eyebrow, title (list of lines), lead, and optionally img + cap. The
    photograph, when a page has one, sits across the text columns at 3:2 (it
    used to stretch 2:1 across the screen and upscale the file)."""
    fig = ""
    if t.get("img"):
        fig = (f'\n  <div class="wrap"><figure class="ph-figure open" data-first>{photo(t["img"], sizes="head")}'
               f'{caption(t.get("cap"))}</figure></div>')
    plain = "" if t.get("img") else " ph-plain"
    return f"""<section class="ph{plain}">
  <div class="wrap">
    <p class="eyebrow lift">{t["eyebrow"]}</p>
    <div class="ph-head">
      <h1 class="ph-title">{title_lines(t["title"])}</h1>
      <p class="ph-lead lift lift-3">{t["lead"]}</p>
    </div>
  </div>{fig}
</section>"""


# ---------------------------------------------------------------------------
# shared pieces added 2026-10-01: the programme covers, the contents line,
# the status pill
# ---------------------------------------------------------------------------

def cover(i, p, size=""):
    """A programme's cover: its number, its emblem inside rings, and three
    words of its own vocabulary, on ink. The five covers replace the five
    programme photographs as the matched set (there is no truthful photograph
    of Concert Guide & Companion, and a set of four photographs and a gap is
    not a set). Decorative: the card or heading beside it carries the name.
    The cover carries the view-transition name, so the cover a reader follows
    from the home page or the index opens their programme's page."""
    c = f" cover-{size}" if size else ""
    return (f'<div class="cover{c}" style="view-transition-name:prog-{p["slug"]};view-transition-class:prog-cover" '
            f'aria-hidden="true">'
            f'<span class="cover-no">{i + 1:02d}</span>{glyph(p["icon"])}'
            f'<span class="cover-line">{_vocab(p["vocab"])}</span></div>')


# who each way is for, as a picture: the people who join, a venue, a
# performer's stand, a hand put up to help (same order in both languages)
WAY_ICONS = ("people", "building", "stand", "hand")


def doors(items, label):
    """The ways in as four doors (Andrew, 2 Oct 2026 night: "more readable,
    with diagram and design"; art direction v3). A station, who the way is
    for, the title in Garamond (the heading of the section it leads to) and
    where it leads. No line joins them: the four are parallel and in no
    order (R19), so the list is unordered. Each door is one link, read with
    pauses. items: (href, label, title, action)."""
    if len(items) != len(WAY_ICONS):
        raise ValueError("doors: one icon per way")
    sep = '<span class="sr-only">, </span>'
    cells = "\n".join(
        f'      <li style="--i:{k}"><a href="{href}">'
        f'<span class="d-ring" aria-hidden="true">{glyph(WAY_ICONS[k], "d-glyph")}</span>'
        f'<span class="d-label">{lab}</span>{sep}<b class="d-title">{title}</b>{sep}'
        f'<span class="d-go"><span class="d-act">{act}</span> {ARROW}</span></a></li>'
        for k, (href, lab, title, act) in enumerate(items))
    return f'<nav class="doors" aria-label="{label}">\n    <ul>\n{cells}\n    </ul>\n  </nav>'


# The same doors, two of them, under the five programmes on the home page:
# the third and fourth ways in, in the order of WAY_ICONS
PAIR_ICONS = WAY_ICONS[2:]


def door_pair(items):
    """The two ways in that the five cards do not cover, for artists and for
    volunteers (Andrew, 3 Oct 2026: two links inside two sentences did not
    read as actions; evening: align them and let them catch the eye). Two
    panels under the cards, edge to edge with the row of five: the station,
    who the way is for, the action in Garamond, one line on what it is, and
    a round arrow at the end. Each panel is one link, read with pauses
    ("Artists, Register your interest, ..."); a list, unordered, no line
    between them (R19). items: (href, label, title[, note])."""
    if len(items) != len(PAIR_ICONS):
        raise ValueError("door_pair: one icon per way")
    sep = '<span class="sr-only">, </span>'
    cells = []
    for k, item in enumerate(items):
        href, lab, title = item[:3]
        note = item[3] if len(item) > 3 else ""
        note_ = f'{sep}<span class="d-note">{note}</span>' if note else ""
        cells.append(
            f'      <li style="--i:{k}"><a href="{href}">'
            f'<span class="d-ring" aria-hidden="true">{glyph(PAIR_ICONS[k], "d-glyph")}</span>'
            f'<span class="d-text"><span class="d-label">{lab}</span>{sep}<b class="d-title">{title}</b>{note_}</span>'
            f'<span class="d-cta" aria-hidden="true">{ARROW}</span></a></li>')
    return '    <ul class="doors doors-pair">\n' + "\n".join(cells) + '\n    </ul>'


def status_tag(st, live=False):
    """A programme's state: green, with a dot that pulses three times, when it
    is running now; plain otherwise."""
    return f'<span class="tag{" tag-live" if live else ""}">{st}</span>'


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------

def _unmark(text):
    """Five cards side by side, each with a highlight, scattered: none stood
    out (chief designer v2, R16). The cards drop it; the Programmes index,
    where each line is read on its own row, keeps it."""
    return text.replace("<mark>", "").replace("</mark>", "")


def prog_card(i, p, pillars):
    label, dot = pillars[p["pillar"]]
    pg = p["page"]
    return f"""      <li><a class="pc" href="programmes/{p["slug"]}.html">
        {cover(i, p)}
        <div class="pc-body">
          <span class="kicker"><i class="{dot}" aria-hidden="true"></i>{label}</span>
          <div class="pc-name"><h3>{p["name"]}</h3>
          <p class="pc-topics">{_vocab(p["vocab"])}</p></div>
          <p>{_unmark(p["line"])}</p>
          {status_tag(pg["now"][0], pg.get("live"))}
        </div>
      </a></li>"""


def _fig(n, label, period, plus=False):
    # The real number is in the markup; where the counter can run it is
    # hidden and the counter prints instead. The "+" is never part of the
    # counted span, so it is printed exactly once either way.
    suffix = '<span class="plus">+</span>' if plus else ""
    return (f'      <div class="fig"><b><span class="count" style="--n:{n}"><span>{n}</span></span>{suffix}</b>'
            f'<span class="fig-label">{label}</span>'
            f'<span class="fig-period">{period}</span></div>')


def _vocab(words):
    """A cover's three words: each stays whole, the line may turn only after a
    dot ("Your / own part" split on the home card)."""
    return " · ".join(w.replace(" ", "\u00a0") for w in words.split(" · "))


def home(t, programmes, pillars, lang):
    """Hero, the five programmes, the record (the page's one ink band), then
    why we exist on white, so the ink band never runs into the ink footer
    (chief designer, 2 Oct 2026) and the page ends on "So we go to them",
    which the footer's master line answers."""
    h, w, nb = t["hero"], t["why"], t["numbers"]
    cards = "\n".join(prog_card(i, p, pillars) for i, p in enumerate(programmes))
    figs = "\n".join(_fig(*f) for f in nb["figs"])
    reasons = "\n".join(f"        <li>{x}</li>" for x in w["reasons"])
    # what is running now, said once at the top (4th pass): it replaced the
    # Ways-in list and section IV, which said it again further down
    live = [p for p in programmes if p["page"].get("live")]
    now = f"\n        {now_line(live[0], 'lift lift-3')}" if live else ""
    cta_lift = "lift-4" if live else "lift-3"
    # the master line is the title's subtitle (Andrew, 2 Oct 2026 evening), in
    # the title's group; the string is the footer's (layout.STR), so the two
    # cannot drift
    return f"""<section class="hero">
  <div class="wrap">
    <p class="eyebrow lift">{h["eyebrow"]}</p>
    <hgroup class="hero-head">
      <h1 class="hero-title">{title_lines(h["title"])}</h1>
      <p class="hero-sub lift lift-2">{STR[lang]["tagline"]}</p>
    </hgroup>
    <div class="hero-body">
      <div class="hero-copy">{now}
        <div class="btn-row hero-cta lift {cta_lift}">{btn(h["cta"][0], h["cta"][1], "primary")}{go(h["more"][0], h["more"][1])}</div>
      </div>
      <figure class="hero-figure open" data-first>
        <span class="rings" aria-hidden="true"></span>
        {photo(h["img"], "4x3", sizes="hero")}
        {caption(h["cap"])}
      </figure>
    </div>
  </div>
</section>

<section id="programmes">
  <div class="wrap">
{sh(t["progs"]["label"], t["progs"]["h2"], t["progs"]["lead"], no="I", split=True)}
    <ul class="progs rv-stagger">
{cards}
    </ul>
{door_pair(t["progs"]["others"])}
  </div>
</section>

<section class="band-ink figs-band" id="record">
  <div class="wrap">
    {eyebrow(nb["label"], "II", "section-label")}
    <h2 class="sr-only">{nb["sr"]}</h2>
    <div class="figs" style="--figs:{len(nb["figs"])}">
{figs}
    </div>
    {artifacts.forty(lang, nb["forty"])}
    <p class="figs-note">{nb["note"]}</p>
  </div>
</section>

<section class="manifesto band-white" aria-labelledby="why-h">
  <div class="wrap why">
    {eyebrow(w["label"], "III", "section-label")}
    <div>
      <h2 class="why-premise" id="why-h"><span class="ink">{w["premise"]}</span></h2>
      <ul class="why-reasons rv-stagger">
{reasons}
      </ul>
      <p class="why-resolve">{w["resolve"]}</p>
      <div class="btn-row">{go("about.html", w["link"])}</div>
    </div>
  </div>
</section>"""


# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------

def _places(pl, lang):
    """The places as the real content (grouped by the kind of place, with
    where each is), and beside them the island with the Irish places on it.
    The map is the picture of the list, not a second copy of it."""
    groups = []
    for title, rows in pl["groups"]:
        items = "".join(f'<li><span class="pl-name">{a}</span><small>{b}</small></li>' for a, b in rows)
        groups.append(f'<div class="places-group"><h3>{title}<span class="pl-n">{len(rows)}</span></h3>'
                      f'<ul>{items}</ul></div>')
    m = pl["map"]
    return f"""<div class="places rv">
      <figure class="places-map">{artifacts.ireland(m["labels"], m)}<figcaption>{m["caption"]}</figcaption></figure>
      <div class="places-list">{"".join(groups)}</div>
    </div>"""


def about(t, lang):
    glance = "".join(f"<div><dt>{a}</dt><dd>{b}<small>{c}</small></dd></div>" for a, b, c in t["glance"])
    story = "\n".join(f"        <p>{p}</p>" for p in t["story"]["text"])
    f, r, pl, idn = t["founder"], t["run"], t["places"], t["identity"]
    pr = t.get("promise")
    promise = ""
    if pr:
        items = "\n".join(f"      <li><strong>{a}</strong>{b}</li>" for a, b in pr["items"])
        promise = f"""<section class="band-sunken" id="promise">
  <div class="wrap">
{sh(pr["label"], pr["h2"], pr["lead"], split=True)}
    <ol class="promise rv">
{items}
    </ol>
  </div>
</section>

"""
    if r.get("items"):
        trust = f"    {leadins(r['items'], 'rv')}"
    else:
        trust = '    <div class="trust rv-stagger">\n' + "\n".join(f"""      <div>
        <h3>{a}</h3>
        <p>{b}</p>
      </div>""" for a, b in r["cols"]) + "\n    </div>"
    if f.get("facts"):
        fbody = f'<p class="founder-line">{f["line"]}</p>\n      {facts(f["facts"], "facts-plain")}'
    else:
        fbody = f'<div class="prose mt-3"><p>{f["text"]}</p></div>'

    links = " ".join(go(h, l) for h, l in r["links"])
    return f"""{page_head(t["head"])}

<section class="tight">
  <div class="wrap">
    <h2 class="sr-only">{t["glance_sr"]}</h2>
    <dl class="glance rv">{glance}</dl>
  </div>
</section>

<section id="story" class="tight">
  <div class="wrap prose-split">
{sh(t["story"]["label"], t["story"]["h2"])}
    <div class="prose rv">
{story}
      <div class="btn-row">{go("news.html#timeline", t["story"]["link"])}</div>
    </div>
  </div>
</section>

<section id="founder" class="band-white">
  <div class="wrap founder">
    {plate(f["img"], "", f.get("cap"), sizes="founder")}
    <div class="rv">
      {eyebrow(f["label"], cls="section-label")}
      <h2>{f["name"]}</h2>
      <p class="founder-role">{f["role"]}</p>
      {fbody}
    </div>
  </div>
</section>

<section id="run">
  <div class="wrap">
{sh(r["label"], r["h2"], r["lead"], split=True)}
    <div class="run-body">
{trust}
      <div class="btn-row rv">{links}</div>
    </div>
  </div>
</section>

{promise}<section id="places" class="band-white">
  <div class="wrap">
{sh(pl["label"], pl["h2"], pl["lead"], split=True)}
    {_places(pl, lang)}
  </div>
</section>

<section id="identity">
  <div class="wrap mark">
    <div class="rv">
      {eyebrow(idn["label"], cls="section-label")}
      <h2>{idn["h2"]}</h2>
      <p class="lead mt-3">{idn["text"]}</p>
    </div>
    <figure class="mark-plate rv">
      <img src="assets/logo-horizontal.svg" width="341" height="131" alt="{idn["alt"]}">
    </figure>
  </div>
</section>"""


# ---------------------------------------------------------------------------
# PROGRAMMES: the index of the five
# ---------------------------------------------------------------------------

# On the index, the talks' When ("On request") and the outings' When ("we
# will email you") repeat their status word for word or nearly; the row says
# it once (UX review, 2 Oct 2026).
WHEN_IN_STATUS = ("getting-to-know", "concert-companion")


def prog_row(i, p, pillars):
    """One row of the index. The name is the one link, stretched over its
    row. The row keeps the id the old long block had, so an old address
    such as programmes.html#recorder-ensemble still lands on its programme,
    and says so in gold."""
    label, dot = pillars[p["pillar"]]
    pg = p["page"]
    when = pg["glance"][2]
    # the status first, then When, unless the status already says it
    facts_ = ("" if p["slug"] in WHEN_IN_STATUS else
              f'<dl class="pi-facts"><div><dt>{when[0]}</dt><dd>{when[1]}</dd></div></dl>')
    return f"""      <li class="pi" id="{p["slug"]}">
        {cover(i, p, "sm")}
        <div class="pi-main">
          <span class="kicker"><i class="{dot}" aria-hidden="true"></i>{label}</span>
          <h2><a href="programmes/{p["slug"]}.html">{p["name"]}</a></h2>
          <p>{p["line"]}</p>
        </div>
        <div class="pi-state">{status_tag(pg["now"][0], pg.get("live"))}{facts_}</div>
        <div class="pi-end">{ARROW}</div>
      </li>"""


def programmes(t, programmes_, pillars):
    rows = "\n".join(prog_row(i, p, pillars) for i, p in enumerate(programmes_))
    a = t["artists"]
    return f"""{page_head(t["head"])}

<section class="tight pi-section">
  <div class="wrap">
    <h2 class="sr-only">{t["list_sr"]}</h2>
    <ol class="prog-index rv-stagger">
{rows}
    </ol>
    <p class="pi-note rv" id="cmfe-artists"><span class="kicker">{a["label"]}</span><span class="pi-text">{a["text"]}</span></p>
  </div>
</section>"""


# ---------------------------------------------------------------------------
# A PROGRAMME'S OWN PAGE (programmes/<slug>.html), added 2026-10-01
#
# One function draws all five, so the five cannot differ in structure: the
# same sections in the same order, four facts at a glance, three steps,
# three answers. What differs is the copy (the deck's `page` dict) and the
# record, which comes from the ledger rather than from the copy, so a page
# can never list a session the ledger does not hold. "In the room" appears
# where there is a photograph or a video of that programme, and only there.
# ---------------------------------------------------------------------------

def _record(slug, lang, t):
    """The programme's rows from the ledger. A titled programme prints the
    row's name over its place; an outreach row prints its place and what was
    played (ledger.TITLED says why). Only public notes are printed."""
    rows = ledger.for_programme(slug)
    items = []
    for r in rows:
        title = r[4] if lang == "en" else r[5]
        venue = r[6] if lang == "en" else r[7]
        q = ledger.qualifier(r, lang)
        att = r[8].get("att")
        extra = (f'<span class="rec-att">{t["people"].format(n=att)}</span>'
                 if att and slug == "getting-to-know" else "")
        if slug in ledger.TITLED:
            what = f"<b>{title}</b><span>{venue}</span>" + (f"<small>{q}</small>" if q else "")
        else:
            what = f"<b>{venue}</b>" + (f"<span>{q}</span>" if q else "")
        items.append(f"""        <li>
          <span class="rec-when">{ledger.when(r, lang)}</span>
          <span class="rec-what">{what}</span>{extra}
        </li>""")
    return len(rows), items


# A long record shows its newest rows and folds the earlier ones (4th pass,
# 2 Oct 2026). The strip above it still draws every session, and the fold
# keeps the order: earlier rows first, then the newest six.
REC_OPEN, REC_FOLD_OVER = 6, 8


def record_list(n, items, t):
    rows = "\n".join(items)
    if n <= REC_FOLD_OVER:
        return f'    <ol class="rec rec-short rv">\n{rows}\n    </ol>'
    early, late = "\n".join(items[:-REC_OPEN]), "\n".join(items[-REC_OPEN:])
    inner = f'<ol class="rec rec-long">\n{early}\n    </ol>'
    return (f'    <div class="rec-wrap rv">\n    {fold(t.get("earlier", "Earlier: {n} more").format(n=n - REC_OPEN), inner, "rec-fold")}\n'
            f'    <ol class="rec rec-long">\n{late}\n    </ol>\n    </div>')


def mail_alt(t):
    """The address and the phone under a mail button, as selectable text: on
    a shared desk or a tablet with no mail app, the button alone does
    nothing (UX review, 1 Oct 2026)."""
    return (f'<p class="mail-alt"><span>{t["or_write"]}</span> <a href="mailto:{t["email"]}">{t["email"]}</a>'
            f' <a href="tel:{t["tel_href"]}">{t["tel"]}</a></p>')


def programme_page(t, i, p, programmes, pillars, lang):
    g = p["page"]
    label, dot = pillars[p["pillar"]]
    # the third fact is always When, the one people scan for; it is bolded
    # unless the head already bolds the time or the status already says it
    bold_when = "<strong>" not in g["now"][1] and p["slug"] not in WHEN_IN_STATUS
    glance = "".join(f'<div{" class=\"is-when\"" if k == 2 and bold_when else ""}><dt>{a}</dt><dd>{b}</dd></div>'
                     for k, (a, b) in enumerate(g["glance"]))
    steps = "\n".join(f"""      <li style="--i:{k}">
        <span class="step-n" aria-hidden="true">{k + 1}</span>
        <h3>{a}</h3>
        <p>{b}</p>
      </li>""" for k, (a, b) in enumerate(g["steps"]))
    faq = "\n".join(f"""      <div>
        <dt>{q}</dt>
        <dd>{a}</dd>
      </div>""" for q, a in g["faq"])
    n, record = _record(p["slug"], lang, t)
    reclist = record_list(n, record, t)
    rows = ledger.for_programme(p["slug"])
    strip = f"""
    <figure class="strip rv">{artifacts.strip(rows, lang, t["strip"])}
      <figcaption class="strip-key"><span><i aria-hidden="true"></i>{t["strip"]["learn"]}</span><span><i class="o" aria-hidden="true"></i>{t["strip"]["share"]}</span><span>{t["strip"]["note"]}</span></figcaption>
    </figure>"""
    chart = ""
    if p["slug"] == "getting-to-know":
        a = t["att"]
        chart = f"""
    <figure class="att rv">
      <figcaption class="att-head"><b>{a["h3"]}</b><span>{a["lead"]}</span></figcaption>
      <div class="att-plot">{artifacts.attendance(lang, a)}</div>
    </figure>"""
    vid = artifacts.video(g.get("video"), t["video_label"].format(name=p["name"]), t["play"])
    has_room = g.get("room", True) or bool(vid)
    # the sections are numbered in the margin, in reading order, with no gap
    # where a page has no "In the room". The programme's own number is not in
    # the head's eyebrow: the cover beside the title carries it in Garamond, and
    # repeated in the label's face it was one number in two faces (R33)
    seq = iter(f"{k:02d}" for k in range(1, 9))
    no_how, no_exp = next(seq), next(seq)
    no_room = next(seq) if has_room else None
    no_rec, no_join = next(seq), next(seq)
    room = ""
    if has_room:
        ph = p["img"]
        portrait = ph[2] > ph[1] * 1.1
        pic = plate(ph, "4x5" if portrait else "3x2", g.get("cap"),
                    "room-plate" + (" room-portrait" if portrait else ""),
                    sizes="room-portrait" if portrait else "room")
        body = pic
        if vid:
            v = g["video"]
            vlabel, vtext = v["cap"]
            out = artifacts.watch_url(v)
            link = (f' <a class="link" href="{out[1]}">{t["watch"].format(service=out[0])}</a>'
                    if out else "")
            body = (f'<figure class="video">{vid}<figcaption><span class="cap-label">{vlabel}</span>'
                    f'<span>{vtext}{link}</span></figcaption></figure>')
        room = f"""

<section class="band-white" id="room">
  <div class="wrap">
{sh(t["room_label"], g.get("room_h2", t["room_h2"]), no=no_room, split=True)}
    <div class="room rv">{body}</div>
  </div>
</section>"""
    # a programme running now says so here too, so every page points to it
    others = "\n".join(f"""      <li><a href="programmes/{q["slug"]}.html"><span class="toc-n">{k + 1:02d}</span><b>{q["name"]}</b>{status_tag(q["page"]["now"][0], True) if q["page"].get("live") else ""}{ARROW}</a></li>"""
                       for k, q in enumerate(programmes) if q["slug"] != p["slug"])
    return f"""<section class="pp-head">
  <div class="wrap">
    <nav class="crumbs lift" aria-label="{t["crumbs_label"]}">
      <ol><li><a href="programmes.html">{t["crumb"]}</a></li><li><span aria-current="page">{p["short"]}</span></li></ol>
    </nav>
    <div class="pp-top">
      <div class="pp-intro">
        <p class="eyebrow lift"><i class="{dot}" aria-hidden="true"></i>{label}</p>
        <h1 class="pp-title">{title_lines([p["name"]])}</h1>
        <p class="lead lift lift-3">{g["lead"]}</p>
        <div class="pp-now{" is-live" if g.get("live") else ""} lift lift-4">
          <p>{status_tag(g["now"][0], g.get("live"))}<span class="pp-say">{g["now"][1]}</span></p>
          <div class="btn-row">{btn(g["mail"], g["join_btn"], "primary")}{go("#join", t["how_join"])}</div>
        </div>
      </div>
      <div class="pp-cover lift lift-2">{cover(i, p)}</div>
    </div>
    <dl class="pp-glance lift lift-5">{glance}</dl>
  </div>
</section>

<section class="band-white" id="how">
  <div class="wrap">
{sh(t["how_label"], g["how_h2"], no=no_how, split=True)}
    <ol class="steps steps-{p["slug"]} rv-stagger">
{steps}
    </ol>
  </div>
</section>

<section id="expect">
  <div class="wrap">
{sh(t["expect_label"], g["expect_h2"], no=no_exp, split=True)}
    <dl class="qa rv-stagger">
{faq}
    </dl>
  </div>
</section>{room}

<section class="band-ink" id="record">
  <div class="wrap">
{sh(t["record_label"], g["record_h2"], g["record_lead"], no=no_rec, split=True)}{strip}{chart}
{reclist}
  </div>
</section>

<section id="join">
  <div class="wrap">
{sh(t["join_label"], g["join_h2"], g.get("join_text") or None, no=no_join, split=True)}
    <div class="join-body rv">
      <p class="join-hint">{t["mail_hint"]}</p>
      <ul class="join-fields">{"".join(f"<li>{x}</li>" for x in g["mail_fields"])}</ul>
      <div class="btn-row">{btn(g["mail"], g["join_btn"], "primary")}</div>
      {mail_alt(t)}
    </div>
  </div>
</section>

<section class="tight band-white" id="more">
  <div class="wrap">
    <h2 class="eyebrow section-label">{t["others_label"]}</h2>
    <ul class="others">
{others}
    </ul>
    <div class="btn-row">{go("programmes.html", t["all_label"])}</div>
  </div>
</section>"""


# ---------------------------------------------------------------------------
# GET INVOLVED
# ---------------------------------------------------------------------------

def get_involved(t, icon):
    inv, play, sup = t["invite"], t["play"], t["support"]
    if inv.get("pairs"):
        # what a host gives and what we bring (4th pass, 2 Oct 2026); the
        # steps of a visit live on the Outreach Concerts page, one click away
        invite_body = ('      <div class="meets">'
                       + "".join(meet(k, a, b, c, inv["pair_labels"]) for k, (a, b, c) in enumerate(inv["pairs"]))
                       + "</div>")
        more_href = "programmes/outreach-concerts.html#how"
    else:
        visit = "\n".join(f"""        <li style="--i:{k}">
          <span class="step-n" aria-hidden="true">{k + 1}</span>
          <h3>{a}</h3>
          <p>{b}</p>
        </li>""" for k, (a, b) in enumerate(inv["steps"]))
        invite_body = f"""      <ol class="steps steps-compact rv-stagger">
{visit}
      </ol>"""
        more_href = "programmes/outreach-concerts.html"
    # interest is taken freely, from any field (Andrew, 2 Oct 2026): who it
    # is for, how to begin and what a venue may ask, as facts; then what a
    # performance with us has looked like, from the record, in place of the
    # eleven-item form
    play_body = f"""      {route(play["facts"])}
      {played(play["examples_label"], play["examples"])}
      <div class="btn-row">{btn(play["href"], play["btn"], "primary")}</div>
      {mail_alt(t["alt"])}
      <p class="small play-note">{play["note"]}</p>"""
    if sup.get("helps"):
        # giving is open: three ways to help, side by side, and the promise
        helps = "\n".join(f"""      <div class="help" id="{h["id"]}">
        {icon(h["icon"])}
        <span class="kicker">{h["kicker"]}</span>
        <h3>{h["h3"]}</h3>
        <p>{h["text"]}</p>
        <div class="btn-row">{btn(h["href"], h["btn"], "quiet")}</div>
      </div>""" for h in sup["helps"])
        support = f"""<section class="band-white" id="support">
  <div class="wrap">
{sh(sup["label"], sup["h2"], sup["lead"], no="03", split=True)}
    <div class="helps rv-stagger">
{helps}
    </div>
    <div class="btn-row rv">{go("about.html#promise", sup["promise_link"])}</div>
  </div>
</section>"""
    else:
        # giving is closed: the founding board is the one way to help, and
        # the page says plainly that no gifts are asked for or accepted
        b = sup["board"]
        support = f"""<section class="band-white" id="support">
  <div class="wrap" id="board">
{sh(sup["label"], b["h2"], b["lead"], no="03", split=True)}
    <div class="board rv">
      {table(b["roles"], b["facts"][0][0], b["facts"][1])}
      <div class="board-act">
        <div class="btn-row">{btn(b["href"], b["btn"], "primary")}</div>
        {mail_alt(t["alt"])}
        <p class="small mt-3">{sup["gifts"]}</p>
      </div>
    </div>
  </div>
</section>"""
    j = t.get("join")
    join = (f"""

<section class="tight band-white" id="join">
  <div class="wrap">
    <h2 class="sr-only">{j["tag"]}</h2>
    <div class="callout rv">
      <span class="kicker">{j["tag"]}</span>
      <p>{j["text"]}</p>
    </div>
  </div>
</section>""" if j else "")
    return f"""{page_head(t["head"])}

<section class="tight gi-ways">
  <div class="wrap">
    <h2 class="sr-only">{t["ways_label"]}</h2>
  {doors(t["ways"], t["ways_label"])}
  </div>
</section>

<section class="band-white" id="invite">
  <div class="wrap">
{sh(inv["label"], inv["h2"], inv.get("lead") or inv.get("text"), no="01", split=True)}
    <div class="invite rv">
{invite_body}
      <div class="invite-act">
        <div class="btn-row">{btn(inv["href"], inv["btn"], "primary")}{go(more_href, inv["more"])}</div>
        {mail_alt(t["alt"])}
      </div>
    </div>
  </div>
</section>

<section id="play">
  <div class="wrap">
{sh(play["label"], play["h2"], play["lead"], no="02", split=True)}
    <div class="play rv">
{play_body}
    </div>
  </div>
</section>

{support}{join}"""


# ---------------------------------------------------------------------------
# NEWS & ARCHIVE
# ---------------------------------------------------------------------------

# the forty on the record (03 §1): talks, outreach and Letters Ensemble
# concerts, the pilot's Easter concert and the two South Dublin Live concerts.
# Outings and the courses are part of the work but not of that count, so
# they are not drawn; a row the ledger marks as scheduled is never drawn.
CHART_KINDS = ("lecture", "outreach", "ensemble", "concert")


def _chart_rows():
    return [r for r in ledger.ROWS if r[3] in CHART_KINDS and ledger.counted(r)]


# a pause for a screen reader between parts drawn apart on screen
SEP = '<span class="sr-only">, </span>'


def _rec_lines(r, lang):
    """A row of the record as two lines: what (a talk's title, a concert's
    title, or an outreach concert's place) and where or with what (the place,
    or what was played). The rule of ledger.public_label: an outreach row is
    its place and its instruments (ledger.TITLED says why)."""
    i = 0 if lang == "en" else 1
    title, venue = r[4 + i], r[6 + i]
    if r[3] == "outreach" or "outreach-concerts" in r[8].get("progs", ()):
        return venue, ledger.qualifier(r, lang)
    return title, venue


# a month's whole name, for a screen reader (the list draws three letters)
MONTH_NAME = {"en": ["January", "February", "March", "April", "May", "June", "July", "August",
                     "September", "October", "November", "December"]}


def record_years(lang, t):
    """The forty on the record, a year at a time (Andrew, 3 Oct 2026 evening:
    the squares did not say what was done, and a tooltip on hover was an
    awkward tool). The year stands at the page edge, like the timeline's year
    beside its months (R2), and the year's months flow in two balanced
    columns from the content line: each month once, then its events, each a
    dot of its kind (filled: a talk; open: a performance, the key is the
    figures above) and two lines, what and where. Nothing to hover: every
    event can be read, by every reader; a screen reader hears each event's
    kind, which the dot only draws."""
    rows = _chart_rows()
    years = sorted({r[0] for r in rows})
    out = []
    for y in years:
        mine = [r for r in rows if r[0] == y]
        months = []
        for m in sorted({r[1] for r in mine}):
            evs = []
            for r in (r for r in mine if r[1] == m):
                talk = r[3] == "lecture"
                # the dot is the item's own mark (::before), so the month can
                # stand on the first title's baseline (an empty dot first in
                # the row gave the row no text baseline)
                cls = "ry-t" if talk else "ry-p"
                kind = t["row_talk"] if talk else t["row_perf"]
                what, where = _rec_lines(r, lang)
                where_ = f'{SEP}<span>{where}</span>' if where else ""
                evs.append(f'              <li class="{cls}"><span class="ry-what">'
                           f'<span class="sr-only">{kind}: </span><b>{what}</b>{where_}</span></li>')
            short = ledger.MONTH[lang][m - 1]
            full = MONTH_NAME.get(lang, ledger.MONTH[lang])[m - 1]
            name = short if full == short else f'<span aria-hidden="true">{short}</span><span class="sr-only">{full}</span>'
            months.append(f'          <li class="ry-mo"><span class="ry-m">{name}</span>\n'
                          f'            <ol class="ry-list">\n' + "\n".join(evs) + "\n            </ol>\n          </li>")
        head = f'{y}{SEP}<span class="ry-n">{t["year_count"].format(n=len(mine))}</span>'
        body = '        <ol class="ry-months">\n' + "\n".join(months) + "\n        </ol>"
        if y != years[-1]:
            # a past year folds on a phone (Andrew, 4 Oct 2026: the record ran
            # to about 4,150px there); from 40em it is always open and the
            # summary is not drawn (styles.css, ::details-content)
            more = t["year_more"].format(n=len(mine), y=y)
            body = f'        <details class="fold ry-fold"><summary>{more}</summary>\n{body}\n        </details>'
        out.append(f'      <div class="ry">\n        <h3 class="ry-y">{head}</h3>\n{body}\n      </div>')
    return '<div class="record-years rv">\n' + "\n".join(out) + "\n    </div>"


# the three latest items' stations: the raised hand of the board, the class's
# recorder, the concert's piano (the covers' own emblems, the same meaning)
LATEST_ICONS = ("hand", "recorder", "piano")


def _latest(items):
    """The latest three as panels (Andrew, 3 Oct 2026 evening: "News and
    archive does not catch the eye"): a station, what kind of news and when,
    the title, one line, and where to go, each part level across the three
    (subgrid). items: (kind, date, title, line, href, action), or the older
    (date, title, line, href, action) with no kind."""
    out = []
    for k, it in enumerate(items):
        kind, date, title, line, href, action = it if len(it) == 6 else ("",) + tuple(it)
        ico = LATEST_ICONS[k] if k < len(LATEST_ICONS) else "mail"
        kind_ = f'<span class="lt-kind">{kind}</span>{SEP}' if kind else ""
        out.append(f'      <article class="lt">\n'
                   f'        <div class="lt-top"><span class="d-ring" aria-hidden="true">{glyph(ico, "d-glyph")}</span>'
                   f'<span class="lt-when">{kind_}<span class="lt-date">{date}</span></span></div>\n'
                   f'        <h3>{title}</h3>\n'
                   f'        <p>{line}</p>\n'
                   f'        <div class="lt-go">{go(href, action)}</div>\n'
                   f'      </article>')
    return "\n".join(out)


def _timeline(tm):
    """How it grew, one year at a time (Andrew, 3 Oct 2026 evening: "the year
    once, on the left, and only the month in each row"). tm["years"]:
    [(year, [(when, title, text), ...]), ...]; a deck with the older flat
    rows [(date, title, text)] is drawn as before."""
    # each sentence its own line (layout.SENTENCE_BLOCKS "tl-text"): the Korean
    # rows turned mid-sentence (「첫 강의에 / 여섯 명이」, CD v6)
    item = ('{i}<li class="tl-item">\n{i}  <span class="tl-date">{a}</span>\n'
            '{i}  <div><h3>{b}</h3><p class="tl-text">{c}</p></div>\n{i}</li>')
    if "years" not in tm:
        rows = "\n".join(item.format(i="      ", a=a, b=b, c=c) for a, b, c in tm["rows"])
        return '    <ol class="timeline">\n' + rows + "\n    </ol>"
    years = []
    for y, rows in tm["years"]:
        items = "\n".join(item.format(i="          ", a=a, b=b, c=c) for a, b, c in rows)
        years.append(f'      <li class="tl-year"><span class="tl-y">{y}</span>\n'
                     f'        <ol class="tl-items">\n{items}\n        </ol>\n      </li>')
    return '    <ol class="timeline timeline-years">\n' + "\n".join(years) + "\n    </ol>"


def _gallery_rows(ars, sizes=(3, 4), width=1168, gap=24):
    """The photographs in rows that each fill the measure (v6; Andrew, 3 Oct
    2026 evening: "the heights are all different, align them"). Order stays
    newest first; each row holds sizes[0] to sizes[1] photographs (three or
    four on a wide screen, two or three on a narrower one, where four left a
    portrait too narrow for its caption), and of the ways to cut the list,
    the one whose rows change least in height from one row to the next (then
    the narrowest spread) wins. A row's height is the measure over the sum of
    its shapes, so no photograph is cropped."""
    n = len(ars)

    def cuts(i):
        if i == n:
            yield []
            return
        for k in range(sizes[0], sizes[1] + 1):
            if i + k <= n:
                for rest in cuts(i + k):
                    yield [(i, i + k)] + rest

    def score(rows):
        h = [(width - (b - a - 1) * gap) / sum(ars[a:b]) for a, b in rows]
        return sum(abs(x - y) for x, y in zip(h, h[1:])) + max(h) - min(h)

    best = min(cuts(0), key=score, default=None)
    # a list no cut fits (too few photographs): one row
    return best or [(0, n)]


def _whole_parts(text, room):
    """A gallery caption's parts (between its dots) each stay whole when they
    fit the narrowest width the photograph is ever given ("Chapel · Tallaght
    University / Hospital" split the name, CD v6); a part that would not fit
    keeps its spaces. Widths are estimated at the caption size, 14px: a Latin
    letter about 7.2px, a Hangul syllable 14px."""
    def est(x):
        return sum(14 if "\uac00" <= ch <= "\ud7a3" else 7.2 for ch in x)
    return " · ".join(x.replace(" ", "\u00a0") if " " in x and est(x) <= room else x for x in text.split(" · "))


def news(t, lang):
    shots = t["gallery"]["rows"]
    ars = [img[1] / img[2] for img, _ in shots]
    # each photograph's share of its row in the wide cut (--w, --n) and in
    # the narrower one (--w2, --n2)
    share = [{}, {}]
    for j, (sizes, width, gap) in enumerate((((3, 4), 1168, 24), ((2, 3), 930, 18))):
        for a, b in _gallery_rows(ars, sizes, width, gap):
            for k in range(a, b):
                share[j][k] = (ars[k] / sum(ars[a:b]), b - a)
    items = []
    for k, (img, cap) in enumerate(shots):
        (w, n), (w2, n2) = share[0][k], share[1][k]
        # its own sizes: its share of the measure in each cut (a two-up row at
        # 1024 drew the 800px file 1006px wide on a 2x screen); the wrap's
        # measure is at most 1168px, and about 91vw under 75em
        sz = f"(max-width:40em) 92vw, (max-width:75em) {round(w2 * 91)}vw, {round(w * 1168)}px"
        # the narrowest width this photograph's caption gets: a phone's line
        # (280px at 320), its share of a row at 641px (582px measure) and at
        # 1200px (1090px)
        room = min(280, (582 - (n2 - 1) * 14) * w2, (1090 - (n - 1) * 19) * w)
        items.append(f'      <li style="--ar:{ars[k]:.4f};--w:{w:.5f};--n:{n};--w2:{w2:.5f};--n2:{n2}">'
                     f'{plate(img, "", _whole_parts(cap, room), sizes=sz)}</li>')
    gal = "\n".join(items)
    c, tm, g = t["chart"], t["timeline"], t["gallery"]
    figs = ""
    if c.get("figs"):
        # the forty in four figures with their period (4th pass): the counts
        # the page lead used to spell out in a sentence
        # each figure's label carries the dot its rows wear below, so the
        # figures are the record's key (v6)
        def cell(f):
            n, label, kind = f if len(f) == 3 else (*f, "")
            dot = {"talk": '<i class="dot" aria-hidden="true"></i>',
                   "perf": '<i class="dot dot-open" aria-hidden="true"></i>'}.get(kind, "")
            return f"<div><dt>{dot}{label}</dt><dd>{n}</dd></div>"
        cells = "".join(cell(f) for f in c["figs"])
        figs = (f'\n    <div class="mini-figs rv"><dl>{cells}</dl>'
                f'<p class="mini-period">{c["period"]}</p></div>')
    return f"""{page_head(t["head"])}

<section class="tight">
  <div class="wrap">
    <h2 class="sr-only">{t["latest_sr"]}</h2>
    <div class="latest rv-stagger">
{_latest(t["latest"])}
    </div>
  </div>
</section>

<section class="band-white" id="record">
  <div class="wrap">
{sh(c["label"], c["h2"], c["lead"], split=True)}{figs}
    {record_years(lang, c)}
  </div>
</section>

<section id="timeline">
  <div class="wrap prose-split">
{sh(tm["label"], tm["h2"])}
{_timeline(tm)}
  </div>
</section>

<section class="band-white" id="gallery">
  <div class="wrap">
{sh(g["label"], g["h2"], g["lead"], split=True)}
    <ul class="gallery">
{gal}
    </ul>
  </div>
</section>"""


# ---------------------------------------------------------------------------
# CONTACT, with the privacy notice
# ---------------------------------------------------------------------------

def contact_form(f, email):
    """One contact form (Andrew, 2 Oct 2026 evening), with no server: a mailto
    form. Six radios named "subject" (their values are the subject lines the
    old buttons used) and one textarea named "body", the only two fields mail
    apps can be relied on to read; submitted with GET, the browser builds
    mailto:…?subject=…&body=… and the visitor's own email app opens with it.
    Nothing is required and nothing is preselected (GOV.UK). The hint for the
    chosen topic is shown with CSS (:has), inside one container the textarea
    points to, so a screen reader hears only the hint that is shown."""
    options = "\n".join(
        f'          <label class="ct-option"><input type="radio" name="subject" value="{subj}" class="t-{key}">'
        f'<span>{label}</span></label>' for key, subj, label, _ in f["topics"])
    def hint(key, prompts):
        if not prompts:
            return ""
        items = "".join(f"<li>{x}</li>" for x in prompts)
        return f'<div class="ct-hint t-{key}"><p>{f["helps"]}</p><ol class="ct-fields">{items}</ol></div>'
    hints = "".join(hint(key, prompts) for key, _, _, prompts in f["topics"])
    rows = (len(f["topics"]) + 1) // 2
    return f"""    <form class="ct-form rv" action="mailto:{email}" method="get">
      <fieldset class="ct-topics">
        <legend>{f["topic_label"]}</legend>
        <div class="ct-options" style="--rows:{rows}">
{options}
        </div>
      </fieldset>
      <div class="ct-field">
        <label for="ct-msg" class="ct-label">{f["message_label"]}</label>
        <div class="ct-hints" id="ct-hint"><p class="ct-hint is-general">{f["general"]}</p>{hints}</div>
        <textarea id="ct-msg" name="body" rows="7" aria-describedby="ct-hint ct-how"></textarea>
      </div>
      <div class="ct-act">
        <button class="btn btn-primary" type="submit">{f["button"]} {ARROW}</button>
        <p class="ct-how" id="ct-how">{f["note"]} <a class="link" href="mailto:{email}">{email}</a></p>
      </div>
    </form>"""


def contact(t):
    pv = t["privacy"]
    def clause(b):
        """A clause is a paragraph, a list or label/value rows (4th pass:
        services and rights read faster as lists), with an optional closing
        sentence. The old two-part form (title, paragraph) still works."""
        if len(b) == 2:
            title, body = b[0], f"<p>{b[1]}</p>"
        else:
            title, kind, content, after = b
            if kind == "list":
                body = '<ul class="clause-list">' + "".join(f"<li>{x}</li>" for x in content) + "</ul>"
            elif kind == "rows":
                body = facts(content, "facts-plain facts-rows")
            else:
                body = f"<p>{content}</p>"
            if after:
                body += f"<p>{after}</p>"
        return f"""      <li>
        <h3>{title}</h3>
        {body}
      </li>"""
    blocks = "\n".join(clause(b) for b in pv["blocks"])
    none = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in pv["none"])
    return f"""{page_head(t["head"])}

<section class="tight ct-write">
  <div class="wrap">
    <h2 class="sr-only">{t["form"]["h2"]}</h2>
{contact_form(t["form"], t["email"])}
    <p class="direct rv"><span class="kicker">{t["direct_label"]}</span><span class="direct-links"><a href="{t["email_href"]}">{t["email"]}</a><a href="tel:{t["tel_href"]}">{t["tel"]}</a></span></p>
  </div>
</section>

<section class="band-white" id="details">
  <div class="wrap prose-split">
{sh(t["details_label"], t["details_h2"])}
    {whereabouts(t["details"])}
  </div>
</section>

<section class="band-sunken" id="privacy">
  <div class="wrap prose-split">
{sh(pv["label"], pv["h2"])}
    <div class="notice-text rv">
      <p>{pv["intro"]}</p>
      <dl class="none-glance">{none}</dl>
      <ol class="notice-list">
{blocks}
      </ol>
    </div>
  </div>
</section>"""
