# -*- coding: utf-8 -*-
"""Hand-authored inline SVG diagrams.

Each one draws a mechanism the prose would otherwise have to describe: what
feeds what, what moves between the parts, and what would break if a part were
removed. Labels come in per-language dictionaries so the English and Korean
pages draw the same figure.

The visual vocabulary is deliberately musical and shared by all four figures,
so they read as one set rather than four flowcharts:

    the stave      four quiet ruled lines and one that carries the weight
    the note-head  the unit — always the same size, whatever it stands for
    the bracket    what groups with what, and what is only claimed
    the wedge      a crescendo: the one thing in the set that means "grows"

Colour comes from `currentColor` plus the accent, so a figure works on the
cream, white and navy bands without a second copy. Long connectors carry
`pathLength="1"` and the `dg-draw` class, which lets styles.css draw them in
on scroll from a single keyframe — see section 4 of styles.css.
"""


# ---------------------------------------------------------------------------
# Shared primitives
# ---------------------------------------------------------------------------

NOTE_RX, NOTE_RY = 11.0, 8.0


def stave(x, w, y, gap=22, n=5):
    """n ruled lines from x to x+w, the last one carrying the accent."""
    out = []
    for i in range(n):
        cls = "dg-stave-base" if i == n - 1 else "dg-stave"
        yy = y + i * gap
        out.append(f'    <line class="{cls}" x1="{x}" y1="{yy}" x2="{x + w}" y2="{yy}"/>')
    return out


def note(cx, cy, open_=False):
    """A note-head: an ellipse tilted the way an engraver tilts one."""
    cls = "dg-note-open" if open_ else "dg-note"
    return (f'    <ellipse class="{cls}" cx="{cx}" cy="{cy}" '
            f'rx="{NOTE_RX}" ry="{NOTE_RY}" transform="rotate(-20 {cx} {cy})"/>')


def tri(x, y, rot=0):
    """An arrowhead as a real element, so it can fade in after its line draws."""
    return (f'    <path class="dg-tri dg-late" d="M{x} {y} l-10 -6 v12 z" '
            f'transform="rotate({rot} {x} {y})"/>')


def draw(d, width=2, dash=False, cls="dg-stroke-accent"):
    """A connector that draws itself in as the figure enters the viewport."""
    extra = ' stroke-dasharray="5 6"' if dash else ""
    klass = cls if dash else f"{cls} dg-draw"
    return (f'    <path class="{klass}" d="{d}" pathLength="1" '
            f'stroke-width="{width}"{extra} fill="none"/>')


def bracket(x1, x2, y, depth=9, dashed=False, below=False):
    """A span marker — ticks toward the thing it groups."""
    v = depth if below else -depth
    dash = ' stroke-dasharray="3 4"' if dashed else ""
    return (f'    <path class="dg-stroke" d="M{x1} {y + v} V{y} H{x2} V{y + v}"'
            f'{dash} fill="none"/>')


def lines(x, y, rows, cls="dg-label", step=19, anchor="start"):
    """A short stack of text lines — labels are pre-wrapped per language."""
    return [f'    <text class="{cls}" x="{x}" y="{y + i * step}" '
            f'text-anchor="{anchor}">{t}</text>' for i, t in enumerate(rows)]


def figure(view, aria, body, caption, title=None):
    head = f'  <p class="diagram-title">{title}</p>\n' if title else ""
    return f"""<figure class="diagram">
{head}  <div class="diagram-canvas">
  <svg viewBox="{view}" role="img" aria-label="{aria}">
{body}
  </svg>
  </div>
  <figcaption>{caption}</figcaption>
</figure>"""


# ---------------------------------------------------------------------------
# 1. The map — five programmes at parity, and the circuit between two pillars
# ---------------------------------------------------------------------------

MAP = {
    "en": dict(
        title="The whole of what we run",
        caption=("Five programmes, one stave. None of them is the main one: the two pillars "
                 "are a single circuit, and taking any note off the stave leaves the other "
                 "side unfed. Without playing for people we never meet the person who asks, "
                 "and without a class there is nowhere to send them."),
        aria=("Five programmes shown as five note-heads of equal size on one stave. Three sit "
              "under the Learning pillar, two under Sharing. An arc from Learning to Sharing is "
              "labelled 'a player, ready for the room'; an arc back from Sharing to Learning is "
              "labelled 'could I do that?'."),
        pillar_a="Learning", pillar_b="Sharing",
        top="a player, ready for the room",
        bottom="“could I do that?”",
        progs=[(["Recorder", "Ensemble course"], "a term, weekly"),
               (["Getting to Know", "Classical Music"], "roughly monthly"),
               (["Concert Guide", "&amp; Companion"], "small groups"),
               (["Outreach", "Concerts"], "care homes · parishes"),
               (["Letters", "Ensemble"], "weekly rehearsals")],
    ),
    "ko": dict(
        title="우리가 하는 일 전체",
        caption=("다섯 개의 프로그램, 하나의 오선. 그 가운데 주된 것은 없습니다. 두 축은 하나의 "
                 "회로이고, 오선에서 음표 하나를 떼면 반대쪽이 먹이를 잃습니다 — 찾아가 연주하지 "
                 "않으면 묻는 사람을 만나지 못하고, 수업이 없으면 그 사람을 보낼 곳이 없습니다."),
        aria=("다섯 프로그램을 같은 크기의 음표 다섯 개로 하나의 오선 위에 그린 도식. 셋은 배움 축, "
              "둘은 나눔 축 아래에 있다. 배움에서 나눔으로 가는 곡선은 ‘그 방에 설 준비가 된 연주자’, "
              "나눔에서 배움으로 돌아오는 곡선은 ‘나도 해 볼 수 있을까?’로 표시된다."),
        pillar_a="배움", pillar_b="나눔",
        top="그 방에 설 준비가 된 연주자",
        bottom="“나도 해 볼 수 있을까?”",
        progs=[(["리코더", "앙상블 과정"], "한 학기 · 주 1회"),
               (["클래식 음악과", "친해지기"], "대략 월 1회"),
               (["함께하는", "음악여행"], "소그룹 동행"),
               (["찾아가는", "음악회"], "요양시설 · 본당"),
               (["Letters", "Ensemble"], "주 1회 정기연습")],
    ),
}

# x of each note-head, and its pitch on the stave — varied so the figure reads
# as music, not as a bar chart. The heads are all the same size on purpose.
MAP_X = [150, 330, 510, 760, 940]
MAP_Y = [242, 220, 187, 198, 165]
STAVE_TOP = 165


def programme_map(lang):
    t = MAP[lang]
    p = []
    p += stave(40, 1000, STAVE_TOP)

    # the two pillars, bracketed above the notes they group
    p.append(f'    <text class="dg-h" x="94" y="112">{t["pillar_a"]}</text>')
    p.append(bracket(80, 580, 130))
    p.append(f'    <text class="dg-h" x="704" y="112">{t["pillar_b"]}</text>')
    p.append(bracket(690, 1000, 130))

    # the circuit: out along the top, back along the bottom
    p.append(draw("M470 116 C 540 58, 640 58, 700 116"))
    p.append(tri(700, 116, 44))
    p.append(f'    <text class="dg-edge dg-late" x="585" y="40" text-anchor="middle">{t["top"]}</text>')

    p.append(draw("M700 386 C 640 448, 540 448, 470 386"))
    p.append(tri(470, 386, 136))
    p.append(f'    <text class="dg-edge dg-late" x="585" y="474" text-anchor="middle">{t["bottom"]}</text>')

    # the five programmes
    for i, ((rows, meta), x, y) in enumerate(zip(t["progs"], MAP_X, MAP_Y)):
        p.append(note(x, y, open_=(i >= 3)))
        p.append(f'    <line class="dg-stroke" x1="{x}" y1="{y + 11}" x2="{x}" y2="288"/>')
        p += lines(x, 312, rows, anchor="middle")
        p.append(f'    <text class="dg-sub" x="{x}" y="354" text-anchor="middle">{meta}</text>')

    return figure("0 0 1080 490", t["aria"], "\n".join(p), t["caption"], t["title"])


# a name the content files already use
def loop(lang):
    return programme_map(lang)


# ---------------------------------------------------------------------------
# 2. Theory of change — what turns money and time into a changed room
# ---------------------------------------------------------------------------

TOC = {
    "en": dict(
        title="From what goes in to what changes",
        caption=("Read left to right. The solid bracket is what we count and can show you; "
                 "the dashed one is what participants and hosts tell us, which we have not "
                 "yet measured. We would rather mark the join than blur it."),
        aria=("Four stages left to right: inputs buy activities, activities produce outputs, "
              "outputs point to change. A solid bracket marks the first three stages as "
              "counted and recorded; a dashed bracket marks the fourth as reported but not "
              "yet measured."),
        cols=[("Inputs", ["Tutor and musicians", "Recorders and scores",
                          "A room, weekly", "Grants and fees"]),
              ("Activities", ["A term-long class", "Playing together",
                              "Concerts in the room", "Going to concerts"]),
              ("Outputs", ["Sessions delivered", "People who completed",
                           "Venues reached", "Concerts given"]),
              ("Change", ["Less isolation", "Dignity and achievement",
                          "Ties across age", "Work for educators"])],
        edges=["buys", "produces", "points to"],
        evidenced="counted and recorded",
        claimed="reported, not yet measured",
    ),
    "ko": dict(
        title="들어가는 것에서 달라지는 것까지",
        caption=("왼쪽에서 오른쪽으로 읽습니다. 실선 괄호는 우리가 세어서 보여 드릴 수 있는 것이고, "
                 "점선 괄호는 참가자와 공간이 해 준 말이지 아직 측정한 것이 아닙니다. "
                 "그 이음매를 흐리기보다 표시해 두는 편을 택했습니다."),
        aria=("왼쪽에서 오른쪽으로 네 단계 — 투입이 활동을 사고, 활동이 산출을 만들고, 산출이 변화를 "
              "가리킨다. 실선 괄호는 앞의 세 단계를 ‘세어서 기록함’으로, 점선 괄호는 네 번째를 "
              "‘증언에 근거, 아직 측정 안 됨’으로 표시한다."),
        cols=[("투입", ["교육가와 연주자", "리코더와 악보",
                        "주 1회 쓸 방", "보조금과 참가비"]),
              ("활동", ["한 학기 수업", "함께 연주하기",
                        "그 방에서의 음악회", "공연에 함께 가기"]),
              ("산출", ["진행한 세션", "수료한 사람",
                        "닿은 공간", "연 음악회"]),
              ("변화", ["덜해진 고립", "존엄과 성취",
                        "세대를 잇는 관계", "교육가의 일자리"])],
        edges=["쓰여서", "만들고", "가리킨다"],
        evidenced="세어서 기록함",
        claimed="증언에 근거 · 아직 측정 안 됨",
    ),
}


def theory_of_change(lang):
    t = TOC[lang]
    x0, w, gap = 8, 210, 72
    p = []
    for i, (title, rows) in enumerate(t["cols"]):
        x = x0 + i * (w + gap)
        # a gold rule instead of a box — the fourth is dashed, because it is claimed
        dash = ' stroke-dasharray="4 5"' if i == 3 else ""
        p.append(f'    <line class="dg-stroke-accent" x1="{x}" y1="42" x2="{x}" y2="198"'
                 f'{dash} stroke-width="2.5"/>')
        p.append(f'    <text class="dg-num" x="{x + 16}" y="38">0{i + 1}</text>')
        p.append(f'    <text class="dg-h" x="{x + 16}" y="70">{title}</text>')
        p += lines(x + 16, 104, [f"{r}" for r in rows], cls="dg-sub", step=26)
        if i < 3:
            a, b = x + w + 6, x + w + gap - 18
            p.append(draw(f"M{a} 120 H{b}", width=1.75))
            p.append(tri(b + 10, 120))
            p.append(f'    <text class="dg-edge dg-late" x="{(a + b) / 2 + 4}" y="104" '
                     f'text-anchor="middle">{t["edges"][i]}</text>')

    solid_end = x0 + 2 * (w + gap) + w
    last = x0 + 3 * (w + gap)
    p.append(bracket(x0, solid_end, 226, depth=10, below=True))
    p.append(f'    <text class="dg-sub" x="{(x0 + solid_end) / 2}" y="256" '
             f'text-anchor="middle">{t["evidenced"]}</text>')
    p.append(bracket(last, last + w, 226, depth=10, dashed=True, below=True))
    p.append(f'    <text class="dg-sub" x="{last + w / 2}" y="256" '
             f'text-anchor="middle">{t["claimed"]}</text>')

    return figure("0 0 1080 272", t["aria"], "\n".join(p), t["caption"], t["title"])


# ---------------------------------------------------------------------------
# 3. A term — four rising notes, and a crescendo underneath
# ---------------------------------------------------------------------------

TERM = {
    "en": dict(
        title="How one course is built",
        caption=("A course is designed so the first satisfying sound arrives in week one, not "
                 "in week six. Nothing assumes prior music reading, every step is reached by "
                 "the whole group together, and it ends the only way it can end — in front of "
                 "people."),
        aria=("Four rising note-heads across a term: first notes in week one, reading music in "
              "weeks two to five, playing your own part in weeks six to eleven, and a concert "
              "in the final week. A widening wedge underneath marks the growth from no "
              "experience to playing in public."),
        steps=[("Week 1", ["Play your first notes"], "Hold it, breathe, play."),
               ("Weeks 2–5", ["Read music from zero"], "Small steps, every week."),
               ("Weeks 6–11", ["Play your own part"], "The moment it clicks."),
               ("Final week", ["Perform a concert"], "For family and friends.")],
        axis_a="no experience assumed",
        axis_b="playing in public",
    ),
    "ko": dict(
        title="한 과정은 이렇게 만듭니다",
        caption=("한 과정은 만족스러운 첫 소리가 6주차가 아니라 1주차에 나오도록 설계돼 있습니다. "
                 "악보를 읽을 줄 안다고 전제하지 않고, 모든 단계를 그룹 전체가 함께 넘으며, "
                 "끝나는 방식은 하나뿐입니다 — 사람들 앞에서."),
        aria=("한 학기에 걸쳐 올라가는 음표 네 개 — 1주차 첫 소리, 2–5주차 악보 읽기, 6–11주차 "
              "자기 파트 연주, 마지막 주 음악회. 아래의 점점 넓어지는 쐐기는 경험 없음에서 "
              "사람들 앞에서 연주하기까지의 성장을 나타낸다."),
        steps=[("1주차", ["첫 소리를 냅니다"], "잡고, 숨을 넣고, 붑니다."),
               ("2–5주차", ["악보를 처음부터"], "매주 조금씩."),
               ("6–11주차", ["내 파트를 맡습니다"], "맞아떨어지는 순간."),
               ("마지막 주", ["음악회를 엽니다"], "가족과 친구 앞에서.")],
        axis_a="경험이 없어도 됩니다",
        axis_b="사람들 앞에서 연주합니다",
    ),
}

TERM_X = [170, 410, 650, 890]
TERM_Y = [198, 176, 143, 110]


def term(lang):
    t = TERM[lang]
    p = []
    p += stave(40, 1000, 110)

    # the line of the term, threaded through the note-heads
    p.append(draw("M170 198 C 290 198, 300 176, 410 176 "
                  "S 540 143, 650 143 S 790 110, 890 110", width=2.5))

    for (when, what, note_txt), x, y in zip(t["steps"], TERM_X, TERM_Y):
        p.append(note(x, y))
        p.append(f'    <line class="dg-stroke" x1="{x}" y1="{y + 11}" x2="{x}" y2="228"/>')
        p.append(f'    <text class="dg-edge" x="{x}" y="252" text-anchor="middle">{when}</text>')
        p += lines(x, 278, what, anchor="middle")
        p.append(f'    <text class="dg-sub" x="{x}" y="302" text-anchor="middle">{note_txt}</text>')

    # a crescendo: the one mark in the set that means "this grows"
    p.append('    <path class="dg-note" opacity=".28" '
             'd="M40 336 L1040 322 L1040 354 L40 340 Z"/>')
    p.append(f'    <text class="dg-sub" x="40" y="372">{t["axis_a"]}</text>')
    p.append(f'    <text class="dg-sub" x="1040" y="372" text-anchor="end">{t["axis_b"]}</text>')

    return figure("0 0 1080 384", t["aria"], "\n".join(p), t["caption"], t["title"])


# ---------------------------------------------------------------------------
# 4. Cross-subsidy — how a paid booking keeps a free seat free
# ---------------------------------------------------------------------------

SUBSIDY = {
    "en": dict(
        title="How a paid booking keeps a free seat free",
        caption=("Money enters from three directions and leaves as places nobody paid for. "
                 "The thickness of each line is its share, not a decoration. Remove the paid "
                 "tier and the free tier does not shrink gracefully — it is the first thing "
                 "that goes."),
        aria=("Institutions, contributing participants, and grants pay into Classical Music for "
              "Everyone. It pays out free places and more rooms, and any surplus loops back in."),
        in_title="Money in", out_title="What it buys",
        in_rows=[(["Institutions"],
                  ["care homes, parishes, councils and", "schools — from their own budget"], 5.5),
                 (["Participants who can"],
                  ["a small termly contribution"], 3.0),
                 (["Grants and gifts"],
                  ["commissions, donations,", "rooms given in kind"], 2.25)],
        hub=["Classical Music", "for Everyone"],
        hub_note="volunteer-led · no private profit",
        out_rows=[(["Free places"],
                   ["older people, people with disabilities,", "anyone for whom cost decides"], 5.5),
                  (["More rooms"],
                   ["surplus goes back into sessions,", "venues and lower fees"], 3.0)],
        edge_in="pays a rate", edge_out="funds", loop="surplus reinvested",
    ),
    "ko": dict(
        title="유료 예약 하나가 무료 자리를 지키는 방식",
        caption=("돈은 세 방향에서 들어와, 아무도 값을 치르지 않은 자리로 나갑니다. 선의 굵기는 "
                 "장식이 아니라 각자의 몫입니다. 유료 층을 걷어내면 무료 층이 조금씩 줄어드는 게 "
                 "아니라 가장 먼저 사라집니다."),
        aria=("기관과 낼 수 있는 참가자, 보조금이 CMFE에 지불하고, CMFE는 무료 자리와 더 많은 방을 "
              "내놓으며 잉여는 다시 안으로 돌아온다."),
        in_title="들어오는 돈", out_title="그 돈이 사는 것",
        in_rows=[(["기관"],
                  ["요양시설 · 본당 · 지자체 · 학교", "— 자체 예산에서"], 5.5),
                 (["낼 수 있는 참가자"],
                  ["학기당 소액 기여"], 3.0),
                 (["보조금과 후원"],
                  ["위촉, 기부,", "현물로 내어 주는 공간"], 2.25)],
        hub=["Classical Music", "for Everyone"],
        hub_note="자원봉사 운영 · 사적 이익 배분 없음",
        out_rows=[(["무료 자리"],
                   ["어르신, 장애가 있는 분,", "비용이 참여를 가르는 모든 사람"], 5.5),
                  (["더 많은 방"],
                   ["잉여는 세션 · 공간 ·", "더 낮은 수강료로"], 3.0)],
        edge_in="비용을 지불", edge_out="자리를 만듦", loop="잉여 재투자",
    ),
}


def subsidy(lang):
    t = SUBSIDY[lang]
    p = []
    hub_y = 190

    p.append(f'    <text class="dg-edge" x="0" y="26">{t["in_title"]}</text>')
    for (rows, notes, wt), y in zip(t["in_rows"], (66, 178, 290)):
        p.append(f'    <line class="dg-stroke-accent" x1="0" y1="{y - 22}" x2="0" y2="{y + 18}" '
                 f'stroke-width="2.5"/>')
        p += lines(16, y, rows)
        p += lines(16, y + 22, notes, cls="dg-sub", step=18)
        p.append(draw(f"M320 {y - 4} C 380 {y - 4}, 386 {hub_y}, 424 {hub_y}", width=wt))
    p.append(tri(430, hub_y))
    p.append(f'    <text class="dg-edge dg-late" x="372" y="44" '
             f'text-anchor="middle">{t["edge_in"]}</text>')

    p.append('    <rect class="dg-fill-accent dg-box" x="436" y="150" rx="12" '
             'width="212" height="84" stroke-width="1.8"/>')
    p += lines(542, 180, t["hub"], cls="dg-label", step=20, anchor="middle")
    p.append(f'    <text class="dg-sub" x="542" y="218" text-anchor="middle">{t["hub_note"]}</text>')

    p.append(f'    <text class="dg-edge" x="1080" y="26" text-anchor="end">{t["out_title"]}</text>')
    for (rows, notes, wt), y in zip(t["out_rows"], (110, 262)):
        p.append(f'    <line class="dg-stroke-accent" x1="770" y1="{y - 22}" x2="770" y2="{y + 18}" '
                 f'stroke-width="2.5"/>')
        p += lines(786, y, rows)
        p += lines(786, y + 22, notes, cls="dg-sub", step=18)
        p.append(draw(f"M652 {hub_y} C 700 {hub_y}, 706 {y - 4}, 754 {y - 4}", width=wt))
        p.append(tri(762, y - 4))
    p.append(f'    <text class="dg-edge dg-late" x="706" y="44" '
             f'text-anchor="middle">{t["edge_out"]}</text>')

    p.append('    <path class="dg-stroke" d="M900 300 C 900 356, 542 360, 542 238" '
             'stroke-dasharray="4 5" fill="none"/>')
    p.append(tri(542, 242, -90))
    p.append(f'    <text class="dg-sub" x="722" y="356" text-anchor="middle">{t["loop"]}</text>')

    return figure("0 0 1080 376", t["aria"], "\n".join(p), t["caption"], t["title"])
