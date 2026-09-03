# -*- coding: utf-8 -*-
"""One detail page per programme.

The five pages share a renderer rather than five copies of markup, for the
same reason the five cards on the home page share a class: the moment one of
them can be laid out differently from the others, one of them starts to look
like the main one. Structure, section order and the number of fact rows are
therefore fixed here; only the prose differs, and it is written natively in
each language rather than translated.

Facts follow the canonical set (00_최종본, 2026-08-27). Where the standard
specification we propose to a new venue differs from what is actually running
this term, both are given and labelled — conflating them is a documented past
error (02 — Programmes §3).
"""

import diagrams as dg

# slug ← the order is the order of the five cards everywhere else on the site
ORDER = ["recorder-ensemble", "getting-to-know", "concert-companion",
         "outreach-concerts", "letters-ensemble"]

PHOTO = {
    "recorder-ensemble": ("conducting.jpg",
                          "A weekly class in a community room in Dublin"),
    "getting-to-know": ("lecture-recital.jpg", "A lecture-recital in progress"),
    "concert-companion": ("quartet-hall.jpg", "An ensemble performing in a bright hall"),
    "outreach-concerts": ("care-christmas.jpg",
                          "A quartet performing in a care setting at Christmas"),
    "letters-ensemble": ("letters-ensemble.jpg", "The Letters Ensemble with their instruments"),
}

DIAGRAM = {
    "recorder-ensemble": dg.term,
    "getting-to-know": dg.lecture_arc,
    "concert-companion": dg.outing,
    "outreach-concerts": dg.visit,
    "letters-ensemble": dg.rehearsals,
}

UI = {
    "en": dict(
        pillar_learn="Learning", pillar_share="Sharing",
        s_how="How it works", s_who="Who it is for", s_session="What happens",
        s_record="On the record", s_next="Next step", cta2="Other ways in",
        s_others="The other four", others_note=(
            "Five programmes, described at the same length. None of them is the main one."),
        back="All five programmes", ask="Ask about this programme",
        honest="What we do not claim",
    ),
    "ko": dict(
        pillar_learn="배움", pillar_share="나눔",
        s_how="어떻게 굴러가는가", s_who="누구를 위한 것인가", s_session="무슨 일이 일어나는가",
        s_record="기록", s_next="다음 걸음", cta2="다른 참여 방법",
        s_others="나머지 넷", others_note=(
            "다섯 프로그램을 같은 분량으로 적었습니다. 그 가운데 주된 것은 없습니다."),
        back="다섯 프로그램 전체", ask="이 프로그램 문의하기",
        honest="주장하지 않는 것",
    ),
}


def _rows(pairs):
    return "\n".join(f"        <dt>{a}</dt><dd>{b}</dd>" for a, b in pairs)


def _list(items, cls="checklist"):
    return "\n".join(f"          <li>{i}</li>" for i in items)


def _table(head, rows):
    th = "".join(f'<th scope="col">{h}</th>' for h in head)
    tr = "\n".join("          <tr>" + "".join(
        f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f"""    <div class="table-scroll">
      <table>
        <thead><tr>{th}</tr></thead>
        <tbody>
{tr}
        </tbody>
      </table>
    </div>"""


def _others(lang, slug, data):
    u = UI[lang]
    cards = []
    for other in ORDER:
        if other == slug:
            continue
        d = data[other]
        img, alt = PHOTO[other]
        pillar = u["pillar_learn"] if d["pillar"] == "learn" else u["pillar_share"]
        cards.append(f"""      <a class="prog" href="programmes/{other}.html">
        <div class="photo photo-3x2"><img src="images/{img}" width="1400" height="933" alt="{alt}"></div>
        <div class="prog-body">
          <span class="kicker">{pillar}</span>
          <h3>{d['name']}</h3>
          <p>{d['one_line']}</p>
          <div class="meta">{d['meta']}</div>
        </div>
      </a>""")
    return f"""<section class="band-sunken">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">{u['s_others']}</p>
      <h2 class="h-md">{u['others_note']}</h2>
    </div>
    <div class="grid grid-4 stagger">
{chr(10).join(cards)}
    </div>
    <div class="btn-row reveal"><a class="btn btn-quiet" href="programmes.html">{u['back']} <span class="arrow">&rarr;</span></a></div>
  </div>
</section>"""


def render(lang, slug, data):
    """One programme page, from the shared skeleton."""
    d, u = data[slug], UI[lang]
    img, alt = PHOTO[slug]
    pillar = u["pillar_learn"] if d["pillar"] == "learn" else u["pillar_share"]

    honest = ""
    if d.get("honest"):
        honest = f"""
    <div class="callout reveal mt-4">
      <h3 class="h-sub">{u['honest']}</h3>
      <p class="small mt-1">{d['honest']}</p>
    </div>"""

    return f"""<section class="page-hero page-hero-lead">
  <div class="wrap">
    <p class="eyebrow lift lift-1"><a class="crumb" href="programmes.html">{u['back']}</a> <span aria-hidden="true">/</span> {pillar}</p>
    <h1 class="lift lift-2">{d['name']}</h1>
    <p class="lift lift-3">{d['lead']}</p>
    <div class="btn-row lift lift-4">
      <a class="btn btn-accent" href="{d['cta_href']}">{d['cta']} <span class="arrow">&rarr;</span></a>
      <a class="btn btn-on-dark" href="get-involved.html">{u['cta2']}</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap split split-wide split-center">
    <figure class="reveal">
      <div class="photo photo-4x3">
        <img src="images/{img}" width="1400" height="1050" alt="{alt}">
      </div>
      <figcaption>{d['caption']}</figcaption>
    </figure>
    <div class="reveal">
      <h2 class="h-md">{d['intro_head']}</h2>
      <p class="lead mt-2">{d['intro']}</p>
      <p class="mt-2">{d['intro2']}</p>
      <dl class="facts">
{_rows(d['facts'])}
      </dl>
    </div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">{u['s_how']}</p>
      <h2>{d['how_head']}</h2>
      <p>{d['how']}</p>
    </div>
    <div class="reveal">{DIAGRAM[slug](lang)}</div>
  </div>
</section>

<section>
  <div class="wrap split split-center">
    <div class="reveal">
      <h2 class="h-md">{u['s_who']}</h2>
      <ul class="checklist mt-3">
{_list(d['who'])}
      </ul>
    </div>
    <div class="reveal">
      <h2 class="h-md">{u['s_session']}</h2>
      <ol class="steps mt-3">
{_list(d['session'])}
      </ol>
    </div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">{u['s_record']}</p>
      <h2 class="h-md">{d['record_head']}</h2>
    </div>
    <div class="reveal">
{_table(d['record_head_row'], d['record'])}
    </div>{honest}
  </div>
</section>

<section class="band-photo">
  <img src="images/{img}" alt="" width="1400" height="788">
  <div class="wrap narrow center reveal">
    <p class="eyebrow center-row">{u['s_next']}</p>
    <h2 class="h-lg">{d['next_head']}</h2>
    <p class="lead mt-2">{d['next']}</p>
    <div class="btn-row center-row">
      <a class="btn btn-accent" href="{d['cta_href']}">{d['cta']} <span class="arrow">&rarr;</span></a>
      <a class="btn btn-on-dark" href="contact.html">{u['ask']}</a>
    </div>
  </div>
</section>

{_others(lang, slug, data)}"""
