# -*- coding: utf-8 -*-
"""Drawings made from data at build time: the attendance at the talks, the
map of the places we have played, and the video slot.

Added on 2026-10-01, when the site was asked to lean less on photographs.
Each drawing is plain inline SVG with its numbers in the markup, so it needs
no script, prints, and reads the same with or without motion. Every drawing
sits beside a real list or table that carries the same facts as text: the
SVG is the picture of the list, never the only copy of it.

Colours are never written here. Each mark has a class and styles.css paints
it from the semantic tokens (--accent-mark for data marks, --line for rules,
--fg-muted for axis text), so the drawings follow the palette.
"""

import html
import os

import geo_ireland as geo
import ledger
from layout import ROOT, SITE_URL


# ---------------------------------------------------------------------------
# Attendance at the talks: one column per session where it was recorded
# (dataviz: one series, so no legend box; columns no wider than 24px with a
# rounded data end and a square foot; hairline grid; the first, the largest
# and the last value labelled, every value in the column's tooltip and in
# the record list beside the chart).
# ---------------------------------------------------------------------------

AT_L, AT_R, AT_T, AT_B = 30, 6, 24, 40      # margins
AT_SLOT, AT_COL, AT_UNIT = 30, 16, 10       # slot width, column width, px per person
AT_MAX = 15                                  # the axis runs 0 to 15


def _column(x, y, w, h, r=4):
    """A column with a rounded top and a square foot."""
    r = min(r, w / 2, h)
    return (f"M{x:.1f},{y + h:.1f}V{y + r:.1f}Q{x:.1f},{y:.1f} {x + r:.1f},{y:.1f}"
            f"H{x + w - r:.1f}Q{x + w:.1f},{y:.1f} {x + w:.1f},{y + r:.1f}V{y + h:.1f}Z")


def attendance(lang, t):
    """t: aria (with {n}, {lo}, {hi}), people (with {n}), note."""
    rows = [r for r in ledger.for_programme("getting-to-know") if r[8].get("att")]
    n = len(rows)
    plot_w, plot_h = n * AT_SLOT, AT_MAX * AT_UNIT
    w, h = AT_L + plot_w + AT_R, AT_T + plot_h + AT_B
    base = AT_T + plot_h
    p = []
    for v in (0, 5, 10, 15):
        y = base - v * AT_UNIT
        p.append(f'<line class="c-grid" x1="{AT_L}" x2="{AT_L + plot_w}" y1="{y + .5}" y2="{y + .5}"/>')
        p.append(f'<text class="c-tick" x="{AT_L - 8}" y="{y + 4}" text-anchor="end">{v}</text>')
    atts = [r[8]["att"] for r in rows]
    hi, lo = max(atts), min(atts)
    first_hi = atts.index(hi)
    label_at = {0, first_hi, n - 1}
    years = {}
    for i, r in enumerate(rows):
        att = r[8]["att"]
        x = AT_L + i * AT_SLOT + (AT_SLOT - AT_COL) / 2
        y = base - att * AT_UNIT
        title = r[4] if lang == "en" else r[5]
        venue = r[6] if lang == "en" else r[7]
        tip = f"{ledger.when(r, lang)} · {title} · {venue} · {t['people'].format(n=att)}"
        p.append(f'<g class="c-col" style="--i:{i}"><title>{tip}</title>'
                 f'<rect class="c-hit" x="{AT_L + i * AT_SLOT}" y="{AT_T}" width="{AT_SLOT}" height="{plot_h}"/>'
                 f'<path class="c-bar" d="{_column(x, y, AT_COL, att * AT_UNIT)}"/></g>')
        if i in label_at:
            p.append(f'<text class="c-val" x="{x + AT_COL / 2:.1f}" y="{y - 7}" text-anchor="middle">{att}</text>')
        years.setdefault(r[0], []).append(i)
    # the years under the columns, with a hairline where one year ends
    for k, (year, idx) in enumerate(sorted(years.items())):
        x0 = AT_L + idx[0] * AT_SLOT
        x1 = AT_L + (idx[-1] + 1) * AT_SLOT
        p.append(f'<text class="c-year" x="{(x0 + x1) / 2:.1f}" y="{base + 26}" text-anchor="middle">{year}</text>')
        if k:
            p.append(f'<line class="c-sep" x1="{x0 + .5}" x2="{x0 + .5}" y1="{base + 6}" y2="{base + 32}"/>')
    aria = t["aria"].format(n=n, lo=lo, hi=hi)
    return (f'<svg class="att-svg" viewBox="0 0 {w} {h}" role="img" aria-label="{html.escape(aria)}">'
            + "".join(p) + "</svg>")


# ---------------------------------------------------------------------------
# A programme's record as one strip of months, January 2024 to December 2026
#
# The same drawing on all five programme pages, so the five read alike. One
# mark per session in its month (filled for the Learning kinds, open for the
# Sharing ones, as everywhere on the site); sessions in the same month stack
# upwards; a course that runs over several months is a bar across them.
# ---------------------------------------------------------------------------

ST_Y0, ST_Y1 = 2024, 2026
ST_L, ST_R, ST_SLOT = 6, 6, 20             # margins and the width of one month
ST_AXIS, ST_STEP, ST_DOT = 70, 14, 4.4     # axis line, stack step, dot radius


def strip(rows, lang, t):
    months = (ST_Y1 - ST_Y0 + 1) * 12
    w = ST_L + months * ST_SLOT + ST_R
    h = ST_AXIS + 34
    def mx(year, month):
        return ST_L + ((year - ST_Y0) * 12 + month - 1) * ST_SLOT + ST_SLOT / 2
    p = [f'<line class="s-axis" x1="{ST_L}" x2="{w - ST_R}" y1="{ST_AXIS + .5}" y2="{ST_AXIS + .5}"/>']
    for year in range(ST_Y0, ST_Y1 + 1):
        x = ST_L + (year - ST_Y0) * 12 * ST_SLOT
        p.append(f'<line class="s-year-tick" x1="{x + .5}" x2="{x + .5}" y1="{ST_AXIS - 6}" y2="{ST_AXIS + 12}"/>')
        p.append(f'<text class="s-year" x="{x + 6 * ST_SLOT}" y="{ST_AXIS + 27}" text-anchor="middle">{year}</text>')
    # a month covered by a bar (a course of weekly sessions) lifts its dots
    # clear of the bar, so a concert inside a course reads as its own mark
    # (QA40-04, 2 Oct 2026)
    barred = set()
    for r in rows:
        if "until" in r[8]:
            y, m = r[0], r[1]
            m2 = r[8]["until"][0]
            y2 = y if m2 >= m else y + 1
            yy, mm = y, m
            while (yy, mm) <= (y2, m2):
                barred.add((yy, mm))
                yy, mm = (yy + 1, 1) if mm == 12 else (yy, mm + 1)
    stack = {}
    for i, r in enumerate(rows):
        y, m = r[0], r[1]
        tip = html.escape(html.unescape(ledger.public_label(r, lang)))
        learn = r[3] in ledger.LEARN
        cls = "s-on" if learn else "s-open"
        if "until" in r[8]:
            m2 = r[8]["until"][0]
            y2 = y if m2 >= m else y + 1
            x1, x2 = mx(y, m) - ST_SLOT / 2 + 2, mx(y2, m2) + ST_SLOT / 2 - 2
            p.append(f'<g class="s-ev" style="--i:{i}"><title>{tip}</title><rect class="s-span {cls}" '
                     f'x="{x1:.1f}" y="{ST_AXIS - 15}" width="{x2 - x1:.1f}" height="7" rx="3.5"/></g>')
            continue
        k = stack.get((y, m), 0)
        stack[(y, m)] = k + 1
        lift = ST_STEP if (y, m) in barred else 0
        cy = ST_AXIS - 11 - lift - k * ST_STEP
        p.append(f'<g class="s-ev" style="--i:{i}"><title>{tip}</title>'
                 f'<circle class="{cls}" cx="{mx(y, m):.1f}" cy="{cy:.1f}" r="{ST_DOT}"/></g>')
    aria = t["aria"].format(n=len(rows))
    return (f'<svg class="strip-svg" viewBox="0 0 {w} {h}" role="img" aria-label="{html.escape(aria)}">'
            + "".join(p) + "</svg>")


# ---------------------------------------------------------------------------
# The forty on the record, one square each, in date order (the home page)
#
# The same forty the News chart draws by month, set as one row: a talk is a
# filled square, a performance an open one. Plain spans in a figure with one
# label, so a screen reader hears the sentence, not forty squares.
# ---------------------------------------------------------------------------

FORTY_KINDS = ("lecture", "outreach", "ensemble", "concert")


def forty(lang, t):
    rows = [r for r in ledger.ROWS if r[3] in FORTY_KINDS and ledger.counted(r)]
    talks = sum(1 for r in rows if r[3] == "lecture")
    sq = "".join(f'<span class="{"f-on" if r[3] == "lecture" else "f-open"}" style="--i:{i}" '
                 f'title="{html.escape(html.unescape(ledger.public_label(r, lang)))}"></span>'
                 for i, r in enumerate(rows))
    aria = t["aria"].format(n=len(rows), talks=talks, perf=len(rows) - talks)
    return (f'<figure class="forty"><div class="forty-row" role="img" aria-label="{html.escape(aria)}">{sq}</div>'
            f'<figcaption><span><i aria-hidden="true"></i>{t["talks"].format(n=talks)}</span>'
            f'<span><i class="o" aria-hidden="true"></i>{t["perf"].format(n=len(rows) - talks)}</span>'
            f'<span>{t["period"]}</span></figcaption></figure>')


# ---------------------------------------------------------------------------
# The places we have played and taught, on the island of Ireland
#
# The outline is Natural Earth's (public domain): the whole island as one
# path, its fill the land and its stroke the coast, with no border drawn. A place is a dot at its own
# latitude and longitude; the Dublin places sit so close together that they
# are drawn as one dot with a ring and a count. No distance rings: drawn round
# Dublin they read as a service area we promise, which they are not.
# ---------------------------------------------------------------------------

MAP_PAD_R = 170              # sea to the east, for the labels


# Where the Irish places on About are, rounded to two decimals (about a
# kilometre): some of them are religious houses, and a map needs no more.
PLACES_GEO = {
    "dublin": [(53.29, -6.38), (53.29, -6.37), (53.32, -6.39), (53.34, -6.28), (53.40, -6.40),
               (53.36, -6.29), (53.35, -6.28), (53.35, -6.28), (53.33, -6.29), (53.31, -6.27),
               # Methodist Centenary Church (Ranelagh), Blessed Sacrament Chapel (Dublin 1),
               # Franciscan Missionaries of Mary (Dublin 5, the area), Carmelite Community Centre
               (53.33, -6.25), (53.35, -6.26), (53.38, -6.19), (53.34, -6.27)],
    "meath": [(53.62, -6.66), (53.56, -6.62)],
    "wicklow": [(52.95, -6.05)],
    "westmeath": [(53.49, -7.47)],
}


def ireland(labels, t):
    """labels: {key: (label, sub)} for dublin, meath, wicklow and westmeath;
    a sub of None on Dublin prints the count of its places. t: aria."""
    clusters = []
    for key in ("dublin", "meath", "wicklow", "westmeath"):
        label, sub = labels[key]
        pts = PLACES_GEO[key]
        if sub is None:
            sub = t["count"].format(n=len(pts))
        clusters.append((key, label, sub, pts))
    hub = clusters[0]
    hx = sum(geo.project(a, b)[0] for a, b in hub[3]) / len(hub[3])
    hy = sum(geo.project(a, b)[1] for a, b in hub[3]) / len(hub[3])
    w, h = geo.W + MAP_PAD_R, geo.H
    p = [f'<path class="m-land" d="{geo.ISLAND}"/>']
    # the places: Dublin's ten as one dot with a ring, the others one each
    lab = []
    for k, (key, label, sub, pts) in enumerate(clusters):
        xs = [geo.project(a, b) for a, b in pts]
        x = sum(q[0] for q in xs) / len(xs)
        y = sum(q[1] for q in xs) / len(xs)
        if k == 0:
            p.append(f'<circle class="m-halo" cx="{x:.1f}" cy="{y:.1f}" r="11"/>')
            p.append(f'<circle class="m-dot m-hub" cx="{x:.1f}" cy="{y:.1f}" r="5.5"/>')
        else:
            p.append(f'<circle class="m-dot" cx="{x:.1f}" cy="{y:.1f}" r="3.6"/>')
        lab.append((key, x, y, label, sub))
    # Labels: the east-coast places hang out at sea on leaders, top to bottom
    # in the order of their dots, so no two leaders cross; a place inland to
    # the west is labelled on the land beside its own dot.
    lx = geo.W + 18
    east = {"meath": hy - 66, "dublin": hy - 2, "wicklow": hy + 70}
    for key, x, y, label, sub in lab:
        if key in east:
            ly = east[key]
            p.append(f'<path class="m-lead" d="M{x + (12 if key == "dublin" else 6):.1f},{y:.1f}'
                     f'C{x + 40:.1f},{y:.1f} {lx - 40:.1f},{ly:.1f} {lx - 6:.1f},{ly:.1f}"/>')
            p.append(f'<text class="m-label" x="{lx}" y="{ly + 5:.1f}">{label}</text>')
            if sub:
                p.append(f'<text class="m-sub" x="{lx}" y="{ly + 24:.1f}">{sub}</text>')
        else:
            p.append(f'<text class="m-label" x="{x - 10:.1f}" y="{y - 4:.1f}" text-anchor="end">{label}</text>')
            if sub:
                p.append(f'<text class="m-sub" x="{x - 10:.1f}" y="{y + 15:.1f}" text-anchor="end">{sub}</text>')
    return (f'<svg class="map-svg" viewBox="-6 -4 {w + 12:.0f} {h + 8:.0f}" role="img" '
            f'aria-label="{html.escape(t["aria"])}">' + "".join(p) + "</svg>")


# ---------------------------------------------------------------------------
# The video slot. Empty until a link is given (layout.VIDEOS), and then the
# page loads nothing from the video service until the reader asks: the frame
# opens on our own still and a play button (srcdoc), and only a click loads
# the player. No script on our side, and no request to YouTube or Vimeo for
# a reader who never presses play.
# ---------------------------------------------------------------------------

def watch_url(v):
    """The video's own page on its service, linked under the player for anyone
    the embedded player does not work for; None for a file we host."""
    if not v or v["kind"] == "file":
        return None
    if v["kind"] == "youtube":
        return "YouTube", f"https://www.youtube.com/watch?v={v['id']}"
    return "Vimeo", f"https://vimeo.com/{v['id']}"


def video(v, label, play):
    if not v:
        return ""
    if v["kind"] == "file":
        poster = f' poster="images/{v["poster"]}"' if v.get("poster") else ""
        return (f'<video class="video-file" controls preload="none"{poster}>'
                f'<source src="{v["src"]}" type="video/mp4"></video>')
    if v["kind"] == "youtube":
        src = f"https://www.youtube-nocookie.com/embed/{v['id']}?autoplay=1&amp;rel=0"
    else:
        src = f"https://player.vimeo.com/video/{v['id']}?autoplay=1&amp;dnt=1"
    # the 800px copy where there is one: the frame is never wider than that
    small = v["poster"][:-4] + "-800.jpg"
    name = small if os.path.exists(os.path.join(ROOT, "images", small)) else v["poster"]
    poster = f"{SITE_URL}/images/{name}"
    doc = ("<style>*{margin:0}html,body{height:100%}a{position:relative;display:block;height:100%;"
           "background:#1D2430}img{width:100%;height:100%;object-fit:cover;opacity:.88}"
           "i{position:absolute;inset:0;margin:auto;width:72px;height:72px;border-radius:50%;"
           "background:#FAF5EE;box-shadow:0 0 0 1px #B8893A}i::before{content:'';position:absolute;"
           "left:29px;top:24px;border-left:20px solid #1D2430;border-top:12px solid transparent;"
           "border-bottom:12px solid transparent}b{position:absolute;width:1px;height:1px;overflow:hidden;"
           "clip-path:inset(50%)}a:focus{outline:none}a:focus-visible{box-shadow:inset 0 0 0 4px #1D2430,"
           "inset 0 0 0 7px #FAF5EE}a:focus-visible i{box-shadow:0 0 0 3px #1D2430,0 0 0 6px #FAF5EE}</style>"
           f"<a href='{src}'><img src='{poster}' alt=''><i></i><b>{play}</b></a>")
    return (f'<iframe class="video-frame" title="{label}" loading="lazy" src="{src}" '
            f'srcdoc="{html.escape(doc)}" allow="autoplay; fullscreen; picture-in-picture"></iframe>')
