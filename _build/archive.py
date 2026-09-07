# -*- coding: utf-8 -*-
"""The year-by-year tables on the Archive page, rendered from ledger.py.

One renderer for both languages so the two pages cannot list different
rows. Column labels are the only thing passed in.
"""

import ledger

STR = {
    "en": dict(date="Date", what="What", where="Where", note="Note",
               bmsp="Sacred Places", le="Letters Ensemble concert", att="present",
               year_head={2023: "Before the founding", 2024: "The first year",
                          2025: "The year it spread", 2026: "The year the model opened"}),
    "ko": dict(date="날짜", what="무엇을", where="어디서", note="비고",
               bmsp="성지·본당 강", le="Letters Ensemble 음악회", att="명 참석",
               year_head={2023: "창립 이전", 2024: "첫해",
                          2025: "퍼져 나간 해", 2026: "모델을 공개한 해"}),
}


def _note(row, lang, s):
    n = row[8]
    bits = []
    flag = n.get("flag")
    if flag:
        bits.append(flag[0] if lang == "en" else flag[1])
    if "att" in n and row[3] == "lecture":
        bits.append(f"{n['att']} {s['att']}" if lang == "en" else f"{n['att']}{s['att']}")
    if n.get("le"):
        bits.append(f"{s['le']} {n['le']}" if lang == "en" else f"{s['le']} {n['le']}회")
    if n.get("bmsp"):
        bits.append(f'<span class="tag">{s["bmsp"]}</span>')
    return " &middot; ".join(bits)


def tables(lang):
    """One section per year, newest first."""
    s = STR[lang]
    out = []
    for year in sorted(ledger.by_year(), reverse=True):
        rows = ledger.by_year()[year]
        trs = []
        for r in rows:
            title = r[4] if lang == "en" else r[5]
            venue = r[6] if lang == "en" else r[7]
            kind = ledger.KIND[lang][r[3]]
            trs.append(
                f"          <tr><td><span class=\"tl-date\">{ledger.when(r, lang)}</span></td>"
                f"<td><strong>{title}</strong><br><span class=\"tiny\">{kind}</span></td>"
                f"<td>{venue}</td><td class=\"small\">{_note(r, lang, s)}</td></tr>")
        n = len(rows)
        count = (f"{n} {'entries' if n != 1 else 'entry'}" if lang == "en" else f"{n}건")
        out.append(f"""<section class="{'band-raised' if year % 2 else ''}" id="y{year}">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">{year} &middot; {count}</p>
      <h2 class="h-md">{s['year_head'][year]}</h2>
    </div>
    <div class="table-scroll reveal">
      <table class="ledger">
        <thead><tr><th scope="col">{s['date']}</th><th scope="col">{s['what']}</th>
          <th scope="col">{s['where']}</th><th scope="col">{s['note']}</th></tr></thead>
        <tbody>
{chr(10).join(trs)}
        </tbody>
      </table>
    </div>
  </div>
</section>""")
    return "\n\n".join(out)
