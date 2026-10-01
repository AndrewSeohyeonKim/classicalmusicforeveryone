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

import ledger
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
    "gallery": "(max-width:48em) 92vw, 50vw",
    "wide": "100vw",
    "hero": "(max-width:55em) 100vw, 60vw",
    "founder": "(max-width:55em) 440px, 34vw",
}


def _srcset(src, w, sizes):
    small = src[:-4] + "-800.jpg"
    if not sizes or w <= 800 or not os.path.exists(os.path.join(ROOT, "images", small)):
        return ""
    return f' srcset="images/{small} 800w, images/{src} {w}w" sizes="{SIZES[sizes]}"'


def photo(img, ratio="", vt=None, vt_target=False, sizes=None):
    """img is (src, width, height, alt). The ratio class is optional where the
    component sets the shape (cards, page heads). vt names the photograph for
    the cross-page transition; a name may appear only once on a page. With
    vt_target the name is only offered, and styles.css takes it up only when
    the block is the page's :target, so only the photograph you followed
    travels and the other four stay where they are. sizes is a key of SIZES."""
    src, w, h, alt = img
    r = f" photo-{ratio}" if ratio else ""
    if vt and vt_target:
        v = f' style="--vt:{vt}"'
    elif vt:
        v = f' style="view-transition-name:{vt};view-transition-class:prog-photo"'
    else:
        v = ""
    return (f'<div class="photo{r}"{v}><img src="images/{src}"{_srcset(src, w, sizes)} '
            f'width="{w}" height="{h}" alt="{alt}"></div>')


def caption(cap):
    """cap is (label, text) or a plain string or None."""
    if not cap:
        return ""
    if isinstance(cap, tuple):
        label, text = cap
        return f'<figcaption><span class="cap-label">{label}</span><span>{text}</span></figcaption>'
    return f"<figcaption>{cap}</figcaption>"


def plate(img, ratio="", cap=None, cls="", vt=None, vt_target=False, sizes="half"):
    """A photograph as a printed plate: it rises into its frame on scroll."""
    c = f"plate {cls}".strip()
    return f'<figure class="{c}">{photo(img, ratio, vt, vt_target, sizes)}{caption(cap)}</figure>'


def facts(rows):
    return ('<dl class="facts">' + "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in rows)
            + "</dl>")


def title_lines(lines):
    """A page heading broken where the copy breaks, each line its own mask."""
    return "".join(f'<span class="ln"><span>{ln}</span></span>' for ln in lines)


# ---------------------------------------------------------------------------
# the interior page head, shared by five pages
# ---------------------------------------------------------------------------

def page_head(t):
    """t: eyebrow, title (list of lines), lead, and optionally img + cap."""
    fig = ""
    if t.get("img"):
        fig = (f'\n  <figure class="ph-figure wrap open">{photo(t["img"], sizes="wide")}'
               f'{caption(t.get("cap"))}</figure>')
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
# HOME
# ---------------------------------------------------------------------------

def _strip(items, label):
    out = []
    for href, kicker, title, line, cta, give in items:
        g = " strip-give" if give else ""
        out.append(f"""      <a class="strip-item{g}" href="{href}">
        <span class="kicker">{kicker}</span>
        <b>{title}</b>
        <span>{line}</span>
        <i>{cta} {ARROW}</i>
      </a>""")
    return (f'    <nav class="hero-strip lift lift-6" aria-label="{label}">\n'
            + "\n".join(out) + "\n    </nav>")


def prog_card(i, p, pillars):
    slug, pillar, name, img, line = p["slug"], p["pillar"], p["name"], p["img"], p["line"]
    label, dot = pillars[pillar]
    return f"""      <li><a class="pc" href="programmes.html#{slug}">
        <span class="pc-num">{i + 1:02d}</span>
        {photo(img, vt="prog-" + slug, sizes="card")}
        <div class="pc-body">
          <span class="kicker"><i class="{dot}" aria-hidden="true"></i>{label}</span>
          <h3>{name}</h3>
          <p>{line}</p>
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


def home(t, programmes, pillars):
    h = t["hero"]
    cards = "\n".join(prog_card(i, p, pillars) for i, p in enumerate(programmes))
    figs = "\n".join(_fig(*f) for f in t["numbers"]["figs"])
    b, n = t["bleed"], t["now"]
    return f"""<section class="hero">
  <div class="wrap">
    <p class="eyebrow lift">{h["eyebrow"]}</p>
    <h1 class="hero-title">{title_lines(h["title"])}</h1>
    <div class="hero-body">
      <div class="hero-copy">
        <p class="master-line lift lift-3">{h["master"]}</p>
        <p class="lead lift lift-4">{h["lead"]}</p>
        <div class="btn-row hero-cta lift lift-5">{btn(h["cta"][0], h["cta"][1], "primary")}{go(h["more"][0], h["more"][1])}</div>
      </div>
      <figure class="hero-figure open">
        <span class="rings" aria-hidden="true"></span>
        {photo(h["img"], "4x3", sizes="hero")}
        {caption(h["cap"])}
      </figure>
    </div>
{_strip(t["strip"], t["strip_label"])}
  </div>
</section>

<section id="programmes">
  <div class="wrap">
{sh(t["progs"]["label"], t["progs"]["h2"], t["progs"]["lead"], no="I", split=True)}
    <ul class="progs rv-stagger">
{cards}
    </ul>
    <p class="small mt-4 rv">{t["progs"]["artists"]}</p>
  </div>
</section>

<section class="manifesto band-white">
  <div class="wrap">
    {eyebrow(t["why"]["label"], "II")}
    <p class="statement"><span class="ink">{t["why"]["text"]}</span></p>
    <div class="btn-row">{go("about.html", t["why"]["link"])}</div>
  </div>
</section>

<section class="band-ink" id="record">
  <div class="wrap">
    {eyebrow(t["numbers"]["label"], "III")}
    <h2 class="sr-only">{t["numbers"]["sr"]}</h2>
    <div class="figs">
{figs}
    </div>
    <p class="figs-note">{t["numbers"]["note"]}</p>
  </div>
</section>

<figure class="bleed">
  {photo(b["img"], sizes="wide")}
  <figcaption><span class="wrap"><span class="cap-label">{b["cap"][0]}</span><span>{b["cap"][1]}</span></span></figcaption>
</figure>

<section id="now">
  <div class="wrap now">
    {plate(n["img"], "4x5")}
    <div class="rv">
      {eyebrow(n["label"], "IV")}
      <span class="tag tag-live">{n["tag"]}</span>
      <h2>{n["h2"]}</h2>
      {facts(n["facts"])}
      <div class="btn-row">{btn(n["href"], n["btn"], "primary")}</div>
    </div>
  </div>
</section>"""


# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------

def about(t):
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
    trust = "\n".join(f"""      <div>
        <h3>{a}</h3>
        <p>{b}</p>
      </div>""" for a, b in r["cols"])
    names = "".join(f"<li>{x}</li>" for x in pl["names"])
    links = " ".join(go(h, l) for h, l in r["links"])
    return f"""{page_head(t["head"])}

<section class="tight">
  <div class="wrap">
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
      <div class="prose mt-3"><p>{f["text"]}</p></div>
    </div>
  </div>
</section>

<section id="run">
  <div class="wrap">
{sh(r["label"], r["h2"], r["lead"], split=True)}
    <div class="trust rv-stagger">
{trust}
    </div>
    <div class="btn-row rv">{links}</div>
  </div>
</section>

{promise}<section id="places">
  <div class="wrap">
{sh(pl["label"], pl["h2"], pl["lead"], split=True)}
    <ul class="credits rv">{names}</ul>
  </div>
</section>

<section id="identity" class="band-white">
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
# PROGRAMMES
# ---------------------------------------------------------------------------

def prog_block(i, p, pillars, labels):
    label, dot = pillars[p["pillar"]]
    band = ' class="band-white"' if i % 2 else ""
    flip = " pb-flip" if i % 2 else ""
    rows = [(labels[0], p["who"]), (labels[1], p["what"]), (labels[2], p["where"]), (labels[3], p["how"])]
    return f"""<section{band} id="{p["slug"]}">
  <div class="wrap pb{flip}">
    {plate(p["img"], "4x3", vt="prog-" + p["slug"], vt_target=True)}
    <div class="rv">
      <span class="pb-no" aria-hidden="true">{i + 1:02d}</span>
      <span class="kicker"><i class="{dot}" aria-hidden="true"></i>{label}</span>
      <h2>{p["name"]}</h2>
      <p class="lead">{p["line"]}</p>
      {facts(rows)}
      <div class="btn-row">{btn(p["mail"], p["btn"], "quiet")}</div>
    </div>
  </div>
</section>"""


def programmes(t, programmes_, pillars):
    toc = "".join(f'<li><a href="#{p["slug"]}"><span class="toc-n">{i + 1:02d}</span>{p["short"]}</a></li>'
                  for i, p in enumerate(programmes_))
    blocks = "\n\n".join(prog_block(i, p, pillars, t["fact_labels"]) for i, p in enumerate(programmes_))
    a, d = t["artists"], t.get("dev")
    dev = ""
    if d:
        dev = f"""

<section class="tight">
  <div class="wrap">
    <div class="callout rv">
      <span class="tag">{d["tag"]}</span>
      <p>{d["text"]}</p>
    </div>
  </div>
</section>"""
    return f"""{page_head(t["head"])}

<nav class="toc" aria-label="{t["toc_label"]}">
  <div class="wrap"><ol>{toc}<li><a href="#cmfe-artists"><span class="toc-n">+</span>CMFE Artists</a></li></ol></div>
</nav>

{blocks}

<section class="band-sunken" id="cmfe-artists">
  <div class="wrap pb">
    {plate(a["img"], "4x3", a["cap"])}
    <div class="rv">
      <span class="kicker">{a["label"]}</span>
      <h2 class="mt-1">CMFE Artists</h2>
      <p class="lead">{a["lead"]}</p>
      {facts(a["facts"])}
      <div class="btn-row">{btn("get-involved.html#play", a["btn"], "gold")}</div>
    </div>
  </div>
</section>{dev}"""


# ---------------------------------------------------------------------------
# GET INVOLVED
# ---------------------------------------------------------------------------

def get_involved(t, icon):
    ways = "".join(f"""<li><a href="#{a}"><span class="toc-n">{i + 1:02d}</span><b>{b}</b><span>{c}</span>{ARROW}</a></li>"""
                   for i, (a, b, c) in enumerate(t["ways"]))
    inv, play, sup = t["invite"], t["play"], t["support"]
    fields = "\n".join(f"      <li>{x}</li>" for x in play["fields"])
    if sup.get("helps"):
        # giving is open: three ways to help, side by side, and the promise
        helps = "\n".join(f"""      <div class="help" id="{h["id"]}">
        {icon(h["icon"])}
        <span class="kicker">{h["kicker"]}</span>
        <h3>{h["h3"]}</h3>
        <p>{h["text"]}</p>
        <div class="btn-row">{btn(h["href"], h["btn"], "quiet")}</div>
      </div>""" for h in sup["helps"])
        support = f"""<section id="support">
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
        support = f"""<section id="support">
  <div class="wrap split">
    <div class="rv" id="board">
      {eyebrow(sup["label"], "03")}
      <h2>{b["h2"]}</h2>
      <p class="lead mt-3">{b["lead"]}</p>
      <div class="btn-row">{btn(b["href"], b["btn"], "primary")}</div>
    </div>
    <div class="rv">
      {facts(b["facts"])}
      <p class="small mt-3">{sup["gifts"]}</p>
    </div>
  </div>
</section>"""
    return f"""{page_head(t["head"])}

<section class="tight">
  <div class="wrap">
    <ul class="ways rv">{ways}</ul>
  </div>
</section>

<section id="invite">
  <div class="wrap split">
    <div class="rv">
      {eyebrow(inv["label"], "01")}
      <h2>{inv["h2"]}</h2>
      <div class="prose mt-3"><p>{inv["text"]}</p></div>
      <div class="btn-row">{btn(inv["href"], inv["btn"], "primary")}</div>
    </div>
    {plate(inv["img"], "4x3", inv.get("cap"))}
  </div>
</section>

<section class="band-white" id="play">
  <div class="wrap">
{sh(play["label"], play["h2"], play["lead"], no="02", split=True)}
    <div class="rv">
      <h3 class="kicker">{play["sub"]}</h3>
      <ol class="checklist mt-2">
{fields}
      </ol>
      <p class="small mt-3">{play["note"]}</p>
      <div class="btn-row">{btn(play["href"], play["btn"], "primary")}</div>
    </div>
  </div>
</section>

{support}

<section class="tight" id="join">
  <div class="wrap">
    <div class="callout rv">
      <span class="tag">{t["join"]["tag"]}</span>
      <p>{t["join"]["text"]}</p>
    </div>
  </div>
</section>"""


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
    rows = []
    for r in ledger.ROWS:
        flag = (r[8].get("flag") or ("", ""))[0]
        if r[3] in CHART_KINDS and "scheduled" not in flag:
            rows.append(r)
    return rows


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
            sx = CH_X0 + (m - 1) * CH_COL + 9 + col * (CH_SQ + CH_GAP)
            sy = y + 9 + row * (CH_SQ + CH_GAP)
            cls = "c-on" if r[3] == "lecture" else "c-open"
            title = r[4] if lang == "en" else r[5]
            venue = r[6] if lang == "en" else r[7]
            label = f"{ledger.when(r, lang)} · {title} · {venue}"
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


TL_X0, TL_TOP, TL_COL, TL_ROW, TL_SQ, TL_GAP = 46, 30, 74, 30, 13, 4


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
        sx = TL_X0 + yi * TL_COL + 6 + k * (TL_SQ + TL_GAP)
        sy = TL_TOP + (m - 1) * TL_ROW + (TL_ROW - TL_SQ) / 2
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
{sh(c["label"], c["h2"], c["lead"], split=True)}
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
# CONTACT
# ---------------------------------------------------------------------------

def contact(t):
    rows = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in t["details"])
    pv = t["privacy"]
    blocks = "\n".join(f"      <h3>{a}</h3>\n      <p>{b}</p>" for a, b in pv["blocks"])
    return f"""{page_head(t["head"])}

<section class="tight">
  <div class="wrap">
    <p class="eyebrow rv">{t["email_label"]}</p>
    <a class="email-big rv" href="{t["email_href"]}">{t["email"]}</a>
    <div class="btn-row rv">{btn(t["email_href"], t["btn"], "primary")}{go(t["tel_href"], t["tel"])}</div>
  </div>
</section>

<section class="tight band-white">
  <div class="wrap prose-split">
{sh(t["details_label"], t["details_h2"])}
    <div class="rv">
      <dl class="details">{rows}</dl>{f'{chr(10)}      <p class="small mt-3">{t["note"]}</p>' if t.get("note") else ""}
    </div>
  </div>
</section>

<section id="privacy">
  <div class="wrap prose-split">
{sh(pv["label"], pv["h2"])}
    <div class="notice-text rv">
      <p>{pv["intro"]}</p>
{blocks}
    </div>
  </div>
</section>"""
