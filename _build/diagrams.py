# -*- coding: utf-8 -*-
"""Hand-authored inline SVG diagrams.

Each one draws a mechanism the prose would otherwise have to describe:
what feeds what, what moves between the parts, and what would break if a
part were removed. Labels come in per-language dictionaries so the English
and Korean pages draw the same figure.

Colour comes from `currentColor` plus the accent, so a diagram works on the
cream, white and navy bands without a second copy.
"""

ARROW_DEFS = """  <defs>
    <marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5"
            markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/>
    </marker>
    <marker id="{mid}-q" viewBox="0 0 10 10" refX="9" refY="5"
            markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="currentColor" opacity=".55"/>
    </marker>
  </defs>"""


# ---------------------------------------------------------------------------
# 1. The loop — why the two pillars are not two departments
# ---------------------------------------------------------------------------

LOOP = {
    "en": dict(
        caption=("The two pillars are one circuit. Take either box away and the other "
                 "stops being fed: without playing for people we never meet the person "
                 "who asks, and without a class there is nowhere to send them."),
        aria=("A cycle: Sharing produces a question, which becomes Learning; "
              "Learning produces players, who go back out with Sharing."),
        a_title="Learning", a_1="Recorder ensemble course",
        a_2="Lecture-recitals · concert companions",
        b_title="Sharing", b_1="Outreach concerts",
        b_2="Letters Ensemble · sacred places",
        top="a player, ready for the room",
        bottom="“could I do that?”",
        note_a="we put the instrument in the hand",
        note_b="we carry the music to the room",
    ),
    "ko": dict(
        caption=("두 축은 하나의 회로입니다. 한쪽을 떼면 다른 쪽이 먹이를 잃습니다 — "
                 "찾아가 연주하지 않으면 묻는 사람을 만나지 못하고, "
                 "수업이 없으면 그 사람을 보낼 곳이 없습니다."),
        aria="나눔이 질문을 낳고 그 질문이 배움이 되며, 배움이 연주자를 만들어 다시 나눔으로 나가는 순환.",
        a_title="배움", a_1="리코더 앙상블 과정",
        a_2="강의·연주 · 공연 동행",
        b_title="나눔", b_1="찾아가는 음악회",
        b_2="Letters Ensemble · 성지와 본당",
        top="그 방에 설 준비가 된 연주자",
        bottom="“나도 해 볼 수 있을까?”",
        note_a="손에 악기를 쥐여 준다",
        note_b="그 방으로 음악을 가져간다",
    ),
}


def loop(lang):
    t = LOOP[lang]
    return f"""<figure class="diagram">
  <svg viewBox="0 0 720 306" role="img" aria-label="{t['aria']}">
{ARROW_DEFS.format(mid='loop-arrow')}
    <rect class="dg-fill-soft dg-box" x="16" y="104" rx="10" width="252" height="108"/>
    <rect class="dg-fill-accent dg-box" x="452" y="104" rx="10" width="252" height="108"/>

    <text class="dg-label" x="40" y="138" style="font-size:16px">{t['a_title']}</text>
    <text class="dg-sub"   x="40" y="164">{t['a_1']}</text>
    <text class="dg-sub"   x="40" y="186">{t['a_2']}</text>

    <text class="dg-label" x="476" y="138" style="font-size:16px">{t['b_title']}</text>
    <text class="dg-sub"   x="476" y="164">{t['b_1']}</text>
    <text class="dg-sub"   x="476" y="186">{t['b_2']}</text>

    <path class="dg-stroke-accent" d="M270 128 C 330 46, 392 46, 450 128"
          marker-end="url(#loop-arrow)"/>
    <text class="dg-edge" x="360" y="40" text-anchor="middle">{t['top']}</text>

    <path class="dg-stroke-accent" d="M450 188 C 392 270, 330 270, 270 188"
          marker-end="url(#loop-arrow)"/>
    <text class="dg-edge" x="360" y="290" text-anchor="middle">{t['bottom']}</text>

    <text class="dg-sub" x="40" y="240">{t['note_a']}</text>
    <text class="dg-sub" x="476" y="240">{t['note_b']}</text>
  </svg>
  <figcaption>{t['caption']}</figcaption>
</figure>"""


# ---------------------------------------------------------------------------
# 2. Theory of change — what turns money and time into a changed room
# ---------------------------------------------------------------------------

TOC = {
    "en": dict(
        caption=("Read left to right: what goes in, what we do with it, what can be "
                 "counted, and what we believe changes. Only the first three columns "
                 "are evidenced — the fourth rests on what participants told us."),
        aria="Inputs feed activities, activities produce countable outputs, outputs point to change.",
        cols=[("Inputs", ["Tutor and musicians", "Recorders and scores", "A room, weekly", "Grants and fees"]),
              ("Activities", ["A term-long class", "Playing together", "Concerts in the room", "Going to concerts"]),
              ("Outputs", ["Sessions delivered", "People who completed", "Venues reached", "Concerts given"]),
              ("Change", ["Less isolation", "Dignity and achievement", "Ties across age", "Work for educators"])],
        edges=["buys", "produces", "points to"],
        evidenced="counted and recorded",
        claimed="reported, not yet measured",
    ),
    "ko": dict(
        caption=("왼쪽에서 오른쪽으로 읽습니다 — 무엇이 들어가고, 그것으로 무엇을 하고, "
                 "무엇을 셀 수 있고, 무엇이 달라진다고 믿는가. 앞의 세 칸만 증빙이 있고, "
                 "네 번째 칸은 참가자들이 해 준 말에 기대고 있습니다."),
        aria="투입이 활동을 낳고, 활동이 셀 수 있는 산출을 만들고, 산출이 변화를 가리킨다.",
        cols=[("투입", ["교육가와 연주자", "리코더와 악보", "주 1회 쓸 방", "보조금과 참가비"]),
              ("활동", ["한 학기 수업", "함께 연주하기", "그 방에서의 음악회", "공연에 함께 가기"]),
              ("산출", ["진행한 세션", "수료한 사람", "닿은 공간", "연 음악회"]),
              ("변화", ["덜해진 고립", "존엄과 성취", "세대를 잇는 관계", "교육가의 일자리"])],
        edges=["쓰여서", "만들고", "가리킨다"],
        evidenced="세어서 기록함",
        claimed="증언에 근거, 아직 측정 안 됨",
    ),
}


def theory_of_change(lang):
    t = TOC[lang]
    x0, w, gap = 14, 208, 68
    parts = [ARROW_DEFS.format(mid="toc-arrow")]
    for i, (title, rows) in enumerate(t["cols"]):
        x = x0 + i * (w + gap)
        cls = "dg-fill-accent" if i == 3 else "dg-fill-soft"
        parts.append(f'    <rect class="{cls} dg-box" x="{x}" y="40" rx="10" width="{w}" height="180"/>')
        parts.append(f'    <text class="dg-label" x="{x + 18}" y="70" style="font-size:15px">{title}</text>')
        for j, row in enumerate(rows):
            parts.append(f'    <text class="dg-sub" x="{x + 18}" y="{102 + j * 26}">· {row}</text>')
        if i < 3:
            ax, bx = x + w + 10, x + w + gap - 10
            parts.append(f'    <line class="dg-stroke-accent" x1="{ax}" y1="140" x2="{bx}" y2="140" '
                         f'marker-end="url(#toc-arrow)"/>')
            parts.append(f'    <text class="dg-edge" x="{(ax + bx) / 2}" y="128" text-anchor="middle">'
                         f'{t["edges"][i]}</text>')

    # what is evidenced, and what is not — a bracket under each span
    span_end = x0 + 2 * (w + gap) + w              # right edge of the "Outputs" column
    last_x = x0 + 3 * (w + gap)
    parts.append(f'    <path class="dg-stroke" d="M{x0} 236 v10 H{span_end} v-10"/>')
    parts.append(f'    <text class="dg-sub" x="{(x0 + span_end) / 2}" y="266" text-anchor="middle">'
                 f'{t["evidenced"]}</text>')
    parts.append(f'    <path class="dg-stroke" d="M{last_x} 236 v10 H{last_x + w} v-10" '
                 f'stroke-dasharray="3 4"/>')
    parts.append(f'    <text class="dg-sub" x="{last_x + w / 2}" y="266" text-anchor="middle">'
                 f'{t["claimed"]}</text>')
    body = "\n".join(parts)
    return f"""<figure class="diagram">
  <svg viewBox="0 0 1042 282" role="img" aria-label="{t['aria']}">
{body}
  </svg>
  <figcaption>{t['caption']}</figcaption>
</figure>"""


# ---------------------------------------------------------------------------
# 3. The term — what a complete beginner actually does, week by week
# ---------------------------------------------------------------------------

TERM = {
    "en": dict(
        caption=("A term is designed so that the first satisfying sound arrives in week one, "
                 "not in week six. Nothing here assumes prior music reading, and every step "
                 "is reached by the whole group together."),
        aria="Four rising steps across a term: first notes, reading music, playing in harmony, a concert.",
        steps=[("Week 1", "Play your first notes", "Hold it, breathe, play."),
               ("Weeks 2–5", "Read music from zero", "Small steps, every week."),
               ("Weeks 6–11", "Play your own part", "The moment it clicks."),
               ("Final week", "Perform a concert", "For family and friends.")],
        axis_start="No experience assumed",
        axis_end="A concert, in public",
    ),
    "ko": dict(
        caption=("한 학기는 만족스러운 첫 소리가 6주차가 아니라 1주차에 나오도록 설계돼 있습니다. "
                 "악보를 읽을 줄 안다고 전제하지 않고, 모든 단계를 그룹 전체가 함께 넘습니다."),
        aria="한 학기에 걸친 네 단계 — 첫 소리, 악보 읽기, 자기 파트 연주, 음악회.",
        steps=[("1주차", "첫 소리를 냅니다", "잡고, 숨을 넣고, 붑니다."),
               ("2–5주차", "악보를 처음부터", "매주 조금씩."),
               ("6–11주차", "내 파트를 맡습니다", "맞아떨어지는 순간."),
               ("마지막 주", "음악회를 엽니다", "가족과 친구 앞에서.")],
        axis_start="경험 없어도 됩니다",
        axis_end="사람들 앞에서 여는 음악회",
    ),
}


def term(lang):
    t = TERM[lang]
    x0, w, gap = 16, 236, 32
    base, top_max = 250, 62
    parts = [ARROW_DEFS.format(mid="term-arrow")]
    parts.append('    <line class="dg-stroke" x1="16" y1="258" x2="1040" y2="258"/>')
    for i, (when, what, note) in enumerate(t["steps"]):
        x = x0 + i * (w + gap)
        h = 66 + i * 40                     # each step stands taller than the last
        y = base - h
        cls = "dg-fill-accent" if i == 3 else "dg-fill-soft"
        parts.append(f'    <rect class="{cls} dg-box" x="{x}" y="{y}" rx="9" width="{w}" height="{h}"/>')
        parts.append(f'    <text class="dg-edge" x="{x + 18}" y="{y + 26}">{when}</text>')
        parts.append(f'    <text class="dg-label" x="{x + 18}" y="{y + 48}">{what}</text>')
        if h >= 106:
            parts.append(f'    <text class="dg-sub" x="{x + 18}" y="{y + 70}">{note}</text>')
        if i < 3:
            ax = x + w + 4
            parts.append(f'    <line class="dg-stroke-accent" x1="{ax}" y1="{base - 22}" '
                         f'x2="{ax + gap - 10}" y2="{base - 22}" marker-end="url(#term-arrow)"/>')
    parts.append(f'    <text class="dg-sub" x="16" y="280">{t["axis_start"]}</text>')
    parts.append(f'    <text class="dg-sub" x="1040" y="280" text-anchor="end">{t["axis_end"]}</text>')
    parts.append(f'    <text class="dg-edge" x="{top_max}" y="44" opacity=".0">.</text>')
    body = "\n".join(parts)
    return f"""<figure class="diagram">
  <svg viewBox="0 0 1056 292" role="img" aria-label="{t['aria']}">
{body}
  </svg>
  <figcaption>{t['caption']}</figcaption>
</figure>"""


# ---------------------------------------------------------------------------
# 4. Cross-subsidy — how a paid booking keeps a free seat free
# ---------------------------------------------------------------------------

SUBSIDY = {
    "en": dict(
        caption=("Money enters from two directions and leaves as places nobody paid for. "
                 "Remove the paid tier and the free tier does not shrink gracefully — "
                 "it is the first thing that disappears."),
        aria=("Institutions and contributing participants pay into CMFE; CMFE pays out free "
              "places, and any surplus is reinvested in more sessions."),
        in_title="Money in",
        in_rows=[("Institutions", "care homes, parishes, councils, schools — a fee from their own budget"),
                 ("Participants who can", "a small termly contribution"),
                 ("Grants and gifts", "commissions, donations, in-kind rooms")],
        hub="Classical Music for Everyone",
        hub_note="volunteer-led · no private profit",
        out_title="What it buys",
        out_rows=[("Free places", "older people, people with disabilities, anyone for whom cost decides"),
                  ("More rooms", "surplus goes back into sessions, venues and lower fees")],
        edge_in="pays a rate",
        edge_out="funds",
        loop="surplus reinvested",
    ),
    "ko": dict(
        caption=("돈은 두 방향에서 들어와, 아무도 값을 치르지 않은 자리로 나갑니다. "
                 "유료 층을 걷어내면 무료 층이 조금씩 줄어드는 게 아니라 가장 먼저 사라집니다."),
        aria="기관과 낼 수 있는 참가자가 CMFE에 지불하고, CMFE는 무료 자리를 내놓으며 잉여는 다시 세션에 투입된다.",
        in_title="들어오는 돈",
        in_rows=[("기관", "요양시설·본당·지자체·학교 — 자체 예산에서 지불"),
                 ("낼 수 있는 참가자", "학기당 소액 기여"),
                 ("보조금과 후원", "위촉, 기부, 현물로 내어 주는 공간")],
        hub="Classical Music for Everyone",
        hub_note="자원봉사 운영 · 사적 이익 배분 없음",
        out_title="그 돈이 사는 것",
        out_rows=[("무료 자리", "어르신, 장애가 있는 분, 비용이 참여를 가르는 모든 사람"),
                  ("더 많은 방", "잉여는 세션·공간·더 낮은 수강료로 되돌아감")],
        edge_in="비용을 지불",
        edge_out="자리를 만듦",
        loop="잉여 재투자",
    ),
}


def subsidy(lang):
    t = SUBSIDY[lang]
    parts = [ARROW_DEFS.format(mid="sub-arrow")]
    # left column
    parts.append(f'    <text class="dg-edge" x="16" y="30">{t["in_title"]}</text>')
    for i, (label, note) in enumerate(t["in_rows"]):
        y = 44 + i * 76
        parts.append(f'    <rect class="dg-fill-soft dg-box" x="16" y="{y}" rx="9" width="330" height="62"/>')
        parts.append(f'    <text class="dg-label" x="34" y="{y + 26}">{label}</text>')
        parts.append(f'    <text class="dg-sub"   x="34" y="{y + 46}">{note}</text>')
        parts.append(f'    <path class="dg-stroke-accent" d="M348 {y + 31} C 392 {y + 31}, 400 152, 434 152" '
                     f'marker-end="url(#sub-arrow)"/>')
    parts.append(f'    <text class="dg-edge" x="392" y="30" text-anchor="middle">{t["edge_in"]}</text>')

    # hub
    parts.append('    <rect class="dg-fill-accent dg-box" x="436" y="112" rx="12" width="212" height="80" '
                 'stroke-width="1.8"/>')
    parts.append(f'    <text class="dg-label" x="542" y="146" text-anchor="middle" '
                 f'style="font-size:14px">{t["hub"]}</text>')
    parts.append(f'    <text class="dg-sub" x="542" y="168" text-anchor="middle">{t["hub_note"]}</text>')

    # right column
    parts.append(f'    <text class="dg-edge" x="1040" y="30" text-anchor="end">{t["out_title"]}</text>')
    for i, (label, note) in enumerate(t["out_rows"]):
        y = 82 + i * 108
        parts.append(f'    <rect class="dg-fill-soft dg-box" x="712" y="{y}" rx="9" width="328" height="76"/>')
        parts.append(f'    <text class="dg-label" x="730" y="{y + 28}">{label}</text>')
        parts.append(f'    <text class="dg-sub"   x="730" y="{y + 50}">{note}</text>')
        parts.append(f'    <path class="dg-stroke-accent" d="M650 152 C 682 152, 686 {y + 38}, 710 {y + 38}" '
                     f'marker-end="url(#sub-arrow)"/>')
    parts.append(f'    <text class="dg-edge" x="680" y="106" text-anchor="middle">{t["edge_out"]}</text>')

    # reinvestment loop back into the hub
    parts.append('    <path class="dg-stroke" d="M876 268 C 876 320, 542 322, 542 196" '
                 'stroke-dasharray="4 5" marker-end="url(#sub-arrow-q)"/>')
    parts.append(f'    <text class="dg-sub" x="700" y="318" text-anchor="middle">{t["loop"]}</text>')

    body = "\n".join(parts)
    return f"""<figure class="diagram">
  <svg viewBox="0 0 1056 336" role="img" aria-label="{t['aria']}">
{body}
  </svg>
  <figcaption>{t['caption']}</figcaption>
</figure>"""
