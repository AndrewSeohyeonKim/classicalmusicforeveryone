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

import os

import artifacts
import ledger
from icons import glyph
from layout import ROOT

ARROW = '<span class="arrow" aria-hidden="true"><i>&rarr;</i></span>'


# ---------------------------------------------------------------------------
# small pieces
# ---------------------------------------------------------------------------

def btn(href, label, kind="quiet"):
    return f'<a class="btn btn-{kind}" href="{href}">{label} {ARROW}</a>'


def go(href, label):
    return f'<a class="go" href="{href}">{label} {ARROW}</a>'


def eyebrow(text, no=None, cls=""):
    n = f'<span class="no">{no}</span>' if no else ""
    c = f"eyebrow {cls}".strip()
    return f'<p class="{c}">{n}{text}</p>'


def sh(label, h2, lead=None, no=None, split=False, cls=""):
    """A section head: a label in the margin, the heading, one paragraph."""
    lead_ = f'\n      <p class="sh-lead">{lead}</p>' if lead else ""
    c = "sh" + (" sh-split" if split else "") + (f" {cls}" if cls else "")
    if split:
        return (f'    <header class="{c}">\n      {eyebrow(label, no)}\n'
                f'      <div><h2>{h2}</h2>{lead_}</div>\n    </header>')
    return f'    <header class="{c}">\n      {eyebrow(label, no)}\n      <h2>{h2}</h2>{lead_}\n    </header>'


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
    return f' srcset="images/{small} 800w, images/{src} {w}w" sizes="{SIZES[sizes]}"'


def photo(img, ratio="", sizes=None):
    """img is (src, width, height, alt). The ratio class is optional where the
    component sets the shape. sizes is a key of SIZES. Since 2026-10-01 a
    photograph never carries a view-transition name: the programme covers do
    (cover() below), so what travels between pages is the same drawing."""
    src, w, h, alt = img
    r = f" photo-{ratio}" if ratio else ""
    return (f'<div class="photo{r}"><img src="images/{src}"{_srcset(src, w, sizes)} '
            f'width="{w}" height="{h}" alt="{alt}"></div>')


def caption(cap):
    """cap is (label, text) or a plain string or None."""
    if not cap:
        return ""
    if isinstance(cap, tuple):
        label, text = cap
        return f'<figcaption><span class="cap-label">{label}</span><span>{text}</span></figcaption>'
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


def pair(title, give, bring, labels):
    """What a host gives and what we bring, side by side."""
    li = lambda xs: "".join(f"<li>{x}</li>" for x in xs)
    return (f'<div class="pair"><h3>{title}</h3><div class="pair-cols">'
            f'<div><p class="pair-label">{labels[0]}</p><ul>{li(give)}</ul></div>'
            f'<div><p class="pair-label">{labels[1]}</p><ul>{li(bring)}</ul></div></div></div>')


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


def contents(items, label, icon_=None):
    """The contents line of a printed programme: a label in the margin, a
    title and the action in its own column. One pattern for every
    list of ways in (home, Get involved, Contact). items: (href, label,
    title, action)."""
    mark = ARROW if not icon_ else f'<span class="c-ico" aria-hidden="true">{glyph(icon_, "c-glyph")}</span>'
    rows = "\n".join(f"""      <li><a href="{href}">
        <span class="c-label">{lab}</span>
        <span class="c-row"><b>{title}</b><span class="c-go"><span class="c-act">{act}</span> {mark}</span></span>
      </a></li>""" for href, lab, title, act in items)
    return f'<nav class="contents" aria-label="{label}">\n    <ol>\n{rows}\n    </ol>\n  </nav>'


def status_tag(st, live=False):
    """A programme's state: green, with a dot that pulses three times, when it
    is running now; plain otherwise."""
    return f'<span class="tag{" tag-live" if live else ""}">{st}</span>'


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------

def prog_card(i, p, pillars):
    label, dot = pillars[p["pillar"]]
    pg = p["page"]
    return f"""      <li><a class="pc" href="programmes/{p["slug"]}.html">
        {cover(i, p)}
        <div class="pc-body">
          <span class="kicker"><i class="{dot}" aria-hidden="true"></i>{label}</span>
          <h3>{p["name"]}</h3>
          <p>{p["line"]}</p>
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


def _pairs(text, lang):
    """The Korean line under the home cards is two name-and-link pairs joined
    by a dot; on a phone it broke between a name and its link. Each pair
    takes its own line (the English says it in two sentences already)."""
    if lang == "ko" and " · " in text:
        return " ".join(f'<span class="sl">{x}</span>' for x in text.split(" · "))
    return text


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
    now = f"\n        {now_line(live[0], 'lift lift-4')}" if live else ""
    cta_lift = "lift-5" if live else "lift-4"
    return f"""<section class="hero">
  <div class="wrap">
    <p class="eyebrow lift">{h["eyebrow"]}</p>
    <h1 class="hero-title">{title_lines(h["title"])}</h1>
    <div class="hero-body">
      <div class="hero-copy">
        <p class="lead lift lift-3">{h["lead"]}</p>{now}
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
    <p class="progs-note rv">{_pairs(t["progs"]["others"], lang)}</p>
  </div>
</section>

<section class="band-ink figs-band" id="record">
  <div class="wrap">
    {eyebrow(nb["label"], "II")}
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
    {eyebrow(w["label"], "III")}
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
      {eyebrow(f["label"])}
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
      {eyebrow(idn["label"])}
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
    # where a page has no "In the room"
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
        <p class="eyebrow lift"><span class="no">{i + 1:02d}</span><i class="{dot}" aria-hidden="true"></i>{label}</p>
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
    <h2 class="eyebrow">{t["others_label"]}</h2>
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
        invite_body = ('      <div class="pairs">'
                       + "".join(pair(a, b, c, inv["pair_labels"]) for a, b, c in inv["pairs"])
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
    examples = "".join(f"<li><b>{a}</b><span>{b}</span><span>{c}</span></li>" for a, b, c in play["examples"])
    play_body = f"""      {facts(play["facts"], "facts-plain")}
      <h3 class="kicker examples-label">{play["examples_label"]}</h3>
      <ul class="examples">{examples}</ul>
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
      {facts(b["facts"], "facts-plain")}
      <div>
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
  {contents(t["ways"], t["ways_label"])}
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
CH_X0, CH_TOP, CH_COL, CH_ROW, CH_SQ, CH_GAP = 96, 34, 82, 58, 14, 5


def _chart_rows():
    return [r for r in ledger.ROWS if r[3] in CHART_KINDS and ledger.counted(r)]


def chart(lang, t):
    rows = _chart_rows()
    years = sorted({r[0] for r in rows})
    p = []
    for i, mon in enumerate(ledger.MONTH[lang]):
        x = CH_X0 + (i + .5) * CH_COL
        p.append(f'<text class="c-mon" x="{x:.0f}" y="{CH_TOP - 14}" text-anchor="middle">{mon}</text>')
    for yi, year in enumerate(years):
        y = CH_TOP + yi * CH_ROW
        p.append(f'<text class="c-year" x="0" y="{y + 31}">{year}</text>')
        for i in range(12):
            p.append(f'<rect class="c-cell" x="{CH_X0 + i * CH_COL + .5}" y="{y + .5}" width="{CH_COL - 1}" '
                     f'height="{CH_ROW - 9}" rx="1"/>')
        used = {}
        for r in [r for r in rows if r[0] == year]:
            m = r[1]
            k = used.get(m, 0)
            used[m] = k + 1
            col, row = k % 4, k // 4
            # four squares a row, centred in the month (QA40-09)
            inset = (CH_COL - 1 - (4 * CH_SQ + 3 * CH_GAP)) / 2
            sx = CH_X0 + (m - 1) * CH_COL + inset + col * (CH_SQ + CH_GAP)
            sy = y + 9 + row * (CH_SQ + CH_GAP)
            cls = "c-on" if r[3] == "lecture" else "c-open"
            label = ledger.public_label(r, lang)
            p.append(f'<g class="c-ev"><title>{label}</title><rect class="{cls}" x="{sx}" y="{sy}" '
                     f'width="{CH_SQ}" height="{CH_SQ}" rx="1"/></g>')
    h = CH_TOP + len(years) * CH_ROW
    talks = sum(1 for r in rows if r[3] == "lecture")
    perf = len(rows) - talks
    aria = t["aria"].format(n=len(rows), talks=talks, perf=perf)
    svg = (f'<svg viewBox="0 0 {CH_X0 + 12 * CH_COL + 2} {h}" role="img" aria-label="{aria}">'
           + "".join(p) + "</svg>")
    return f"""<figure class="chart rv">
      <div class="chart-wide">{svg}</div>
      <div class="chart-tall">{_chart_tall(lang, rows, years, aria)}</div>
      <figcaption class="chart-key"><span><i aria-hidden="true"></i>{t["key_talk"].format(n=talks)}</span><span><i class="o" aria-hidden="true"></i>{t["key_perf"].format(n=perf)}</span><span>{t["key_note"]}</span></figcaption>
    </figure>"""


TL_X0, TL_TOP, TL_COL, TL_ROW, TL_SQ, TL_GAP = 46, 30, 74, 30, 12, 4


def _chart_tall(lang, rows, years, aria):
    """The same forty squares turned on their side for a phone: one column per
    year, one row per month, so nothing has to scroll sideways. Only one of
    the two drawings is ever displayed, so a screen reader meets one."""
    p = []
    for yi, year in enumerate(years):
        x = TL_X0 + (yi + .5) * TL_COL
        p.append(f'<text class="c-year c-year-sm" x="{x:.0f}" y="{TL_TOP - 10}" text-anchor="middle">{year}</text>')
    for i, mon in enumerate(ledger.MONTH[lang]):
        y = TL_TOP + i * TL_ROW
        p.append(f'<text class="c-mon" x="0" y="{y + 19}">{mon}</text>')
        for yi in range(len(years)):
            p.append(f'<rect class="c-cell" x="{TL_X0 + yi * TL_COL + .5}" y="{y + .5}" width="{TL_COL - 1}" '
                     f'height="{TL_ROW - 1}" rx="1"/>')
    used = {}
    for r in rows:
        yi, m = years.index(r[0]), r[1]
        k = used.get((yi, m), 0)
        used[(yi, m)] = k + 1
        # four a row, then a second row in the same month, never into the
        # next year's column (QA40-09)
        col, row = k % 4, k // 4
        sx = TL_X0 + yi * TL_COL + (TL_COL - 1 - (4 * TL_SQ + 3 * TL_GAP)) / 2 + col * (TL_SQ + TL_GAP)
        sy = TL_TOP + (m - 1) * TL_ROW + (TL_ROW - TL_SQ) / 2 + row * (TL_SQ + 2)
        cls = "c-on" if r[3] == "lecture" else "c-open"
        p.append(f'<rect class="{cls}" x="{sx}" y="{sy:.1f}" width="{TL_SQ}" height="{TL_SQ}" rx="1"/>')
    h = TL_TOP + 12 * TL_ROW + 2
    return (f'<svg viewBox="0 0 {TL_X0 + len(years) * TL_COL + 2} {h}" role="img" aria-label="{aria}">'
            + "".join(p) + "</svg>")


def news(t, lang):
    latest = "\n".join(f"""      <article>
        <span class="kicker">{a}</span>
        <h3>{b}</h3>
        <p>{c}</p>
        <div class="btn-row">{go(d, e)}</div>
      </article>""" for a, b, c, d, e in t["latest"])
    tl = "\n".join(f"""      <li class="tl-item">
        <span class="tl-date">{a}</span>
        <div><h3>{b}</h3><p>{c}</p></div>
      </li>""" for a, b, c in t["timeline"]["rows"])
    gal = "\n".join(f"      <li>{plate(img, '', cap, sizes='gallery')}</li>" for img, cap in t["gallery"]["rows"])
    c, tm, g = t["chart"], t["timeline"], t["gallery"]
    figs = ""
    if c.get("figs"):
        # the forty in four figures with their period (4th pass): the counts
        # the page lead used to spell out in a sentence
        cells = "".join(f"<div><dt>{label}</dt><dd>{n}</dd></div>" for n, label in c["figs"])
        figs = (f'\n    <div class="mini-figs rv"><dl>{cells}</dl>'
                f'<p class="mini-period">{c["period"]}</p></div>')
    return f"""{page_head(t["head"])}

<section class="tight">
  <div class="wrap">
    <h2 class="sr-only">{t["latest_sr"]}</h2>
    <div class="latest rv-stagger">
{latest}
    </div>
  </div>
</section>

<section class="band-white" id="record">
  <div class="wrap">
{sh(c["label"], c["h2"], c["lead"], split=True)}{figs}
    {chart(lang, c)}
  </div>
</section>

<section id="timeline">
  <div class="wrap prose-split">
{sh(tm["label"], tm["h2"])}
    <ol class="timeline">
{tl}
    </ol>
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

def contact(t):
    rows = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in t["details"])
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

<section class="tight ct-topics">
  <div class="wrap">
    <h2 class="sr-only">{t["topics_h2"]}</h2>
  {contents(t["topics"], t["topics_h2"], icon_="mail")}
    <p class="direct rv"><span class="kicker">{t["direct_label"]}</span><span class="direct-links"><a href="{t["email_href"]}">{t["email"]}</a><a href="tel:{t["tel_href"]}">{t["tel"]}</a></span></p>
  </div>
</section>

<section class="band-white" id="details">
  <div class="wrap prose-split">
{sh(t["details_label"], t["details_h2"])}
    <div class="rv">
      <dl class="details">{rows}</dl>
    </div>
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
