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
        pillar_a="Learning", pillar_a_sub="we teach people to play",
        pillar_b="Sharing", pillar_b_sub="we bring the music to the room",
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
        pillar_a="배움", pillar_a_sub="직접 연주하도록 가르칩니다",
        pillar_b="나눔", pillar_b_sub="그 방으로 음악을 가져갑니다",
        top="그 방에 설 준비가 된 연주자",
        bottom="“나도 해 볼 수 있을까?”",
        progs=[(["리코더", "앙상블 과정"], "한 학기 · 주 1회"),
               (["클래식 음악과", "친해지기"], "대략 월 1회"),
               (["함께하는", "음악여행"], "소그룹 동행"),
               (["찾아가는", "음악회"], "요양시설 · 본당"),
               (["Letters", "Ensemble"], "주 1회 정기연습")],
    ),
}

# Geometry. Two named zones rather than two brackets: the pillars are the
# point of the figure, so they get panels and headings of their own instead of
# a hairline that the circuit arrow then has to dodge. Every note sits on the
# SAME stave line — five equal heads at one pitch is the plainest way to draw
# "none of these is the main one", and it also stops the figure reading as a
# scattered bar chart.
MAP_ZONE_A = (24, 510)          # Learning:  x, width   (three programmes)
MAP_ZONE_B = (684, 372)         # Sharing:   x, width   (two programmes)
MAP_X = [104, 274, 444, 778, 962]
MAP_NOTE_Y = 232
MAP_PANEL = (110, 262)          # y, height


def programme_map(lang):
    t = MAP[lang]
    py, ph = MAP_PANEL
    p = []

    # the two zones
    for (zx, zw), head, sub in ((MAP_ZONE_A, t["pillar_a"], t["pillar_a_sub"]),
                                (MAP_ZONE_B, t["pillar_b"], t["pillar_b_sub"])):
        p.append(f'    <rect class="dg-fill-soft" x="{zx}" y="{py}" width="{zw}" '
                 f'height="{ph}" rx="12"/>')
        p.append(f'    <text class="dg-h" x="{zx + 24}" y="{py + 38}">{head}</text>')
        p.append(f'    <text class="dg-sub" x="{zx + 24}" y="{py + 62}">{sub}</text>')

    # one stave across both zones — the circuit is a single line of music
    p += stave(24, 1032, 196, gap=18)

    # the five programmes, all at the same pitch and the same size
    for i, ((rows, meta), x) in enumerate(zip(t["progs"], MAP_X)):
        p.append(note(x, MAP_NOTE_Y, open_=(i >= 3)))
        p.append(f'    <line class="dg-stroke" x1="{x}" y1="{MAP_NOTE_Y + 10}" '
                 f'x2="{x}" y2="292"/>')
        p += lines(x, 314, rows, anchor="middle")
        p.append(f'    <text class="dg-sub" x="{x}" y="{314 + 19 * len(rows) + 8}" '
                 f'text-anchor="middle">{meta}</text>')

    # the circuit — one slur out above the zones, one return below them
    p.append(f'    <text class="dg-edge dg-late" x="568" y="30" '
             f'text-anchor="middle">{t["top"]}</text>')
    p.append(draw("M274 96 C 380 40, 760 40, 856 92"))
    p.append(tri(864, 96, 40))

    p.append(draw("M962 400 C 860 452, 380 452, 282 404"))
    p.append(tri(274, 400, 220))
    p.append(f'    <text class="dg-edge dg-late" x="568" y="480" '
             f'text-anchor="middle">{t["bottom"]}</text>')

    return figure("0 0 1080 500", t["aria"], "\n".join(p), t["caption"], t["title"])


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
    x0, w, gap = 24, 206, 64
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

    p.append(f'    <text class="dg-edge" x="24" y="26">{t["in_title"]}</text>')
    for (rows, notes, wt), y in zip(t["in_rows"], (66, 178, 290)):
        p.append(f'    <line class="dg-stroke-accent" x1="24" y1="{y - 22}" x2="24" y2="{y + 18}" '
                 f'stroke-width="2.5"/>')
        p += lines(40, y, rows)
        p += lines(40, y + 22, notes, cls="dg-sub", step=18)
        p.append(draw(f"M320 {y - 4} C 380 {y - 4}, 386 {hub_y}, 424 {hub_y}", width=wt))
    p.append(tri(430, hub_y))
    p.append(f'    <text class="dg-edge dg-late" x="372" y="44" '
             f'text-anchor="middle">{t["edge_in"]}</text>')

    p.append('    <rect class="dg-fill-accent dg-box" x="436" y="150" rx="12" '
             'width="212" height="84" stroke-width="1.8"/>')
    p += lines(542, 180, t["hub"], cls="dg-label", step=20, anchor="middle")
    p.append(f'    <text class="dg-sub" x="542" y="218" text-anchor="middle">{t["hub_note"]}</text>')

    p.append(f'    <text class="dg-edge" x="1056" y="26" text-anchor="end">{t["out_title"]}</text>')
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


# ---------------------------------------------------------------------------
# 5. The lecture series — what changes in the listener, not what is covered
# ---------------------------------------------------------------------------

ARC = {
    "en": dict(
        title="What the three stages actually move",
        caption=("The three stages are not three difficulty levels. They move ownership: "
                 "the music starts as somebody else&rsquo;s, becomes something shared in the "
                 "room, and ends up yours. Each session also stands on its own, so nobody "
                 "arrives having missed the beginning."),
        aria=("Three rising note-heads on a stave: Getting Closer, Experiencing Together and "
              "Discovering My Taste, with arrows labelled 'listen without being tested' and "
              "'say what you heard'. A dashed arc returns from the third stage to the entry "
              "point, marked 'every session stands alone — start at any one'."),
        entry="no prior knowledge",
        steps=[(["Getting Closer"], ["the music is", "somebody else&rsquo;s"]),
               (["Experiencing Together"], ["the music is", "the room&rsquo;s"]),
               (["Discovering My Taste"], ["the music is", "yours"])],
        edges=["listen without being tested", "say what you heard"],
        loopback="every session stands alone — start at any one",
    ),
    "ko": dict(
        title="세 단계가 실제로 옮기는 것",
        caption=("세 단계는 난이도 세 칸이 아닙니다. 옮기는 것은 소유입니다 — 음악은 처음에 "
                 "남의 것이었다가, 그 방이 함께 가진 것이 되고, 끝에는 내 것이 됩니다. "
                 "동시에 각 회차는 그 자체로 완결돼 있어, 늦게 온 사람이 앞부분을 놓친 채로 "
                 "앉아 있게 되지 않습니다."),
        aria=("오선 위로 올라가는 음표 셋 — 친해지기, 함께 경험하기, 내 취향 찾기. 화살표에는 "
              "‘평가받지 않고 듣기’와 ‘들은 것을 말해 보기’가 붙어 있고, 세 번째에서 입구로 "
              "돌아오는 점선은 ‘각 회차는 그 자체로 완결 — 아무 회차나 첫 회차’를 뜻한다."),
        entry="사전 지식 없이",
        steps=[(["친해지기"], ["음악은 아직", "남의 것입니다"]),
               (["함께 경험하기"], ["음악은 이 방이", "함께 가진 것입니다"]),
               (["내 취향 찾기"], ["음악은 이제", "내 것입니다"])],
        edges=["평가받지 않고 듣기", "들은 것을 말해 보기"],
        loopback="각 회차는 그 자체로 완결 — 아무 회차나 첫 회차입니다",
    ),
}

ARC_X = [300, 580, 860]
ARC_Y = [216, 183, 150]


def lecture_arc(lang):
    t = ARC[lang]
    p = []
    p += stave(40, 1000, 150)

    # the entry: an open note-head, because nothing is required to be there yet
    p.append(note(120, 238, open_=True))
    p.append(f'    <text class="dg-sub" x="120" y="278" text-anchor="middle">{t["entry"]}</text>')
    p.append(draw("M140 232 C 200 232, 220 216, 278 216", width=1.75))
    p.append(tri(286, 216))

    for i, ((head, sub), x, y) in enumerate(zip(t["steps"], ARC_X, ARC_Y)):
        p.append(note(x, y))
        p.append(f'    <line class="dg-stroke" x1="{x}" y1="{y + 11}" x2="{x}" y2="300"/>')
        p += lines(x, 326, head, cls="dg-h", anchor="middle")
        p += lines(x, 352, sub, cls="dg-sub", step=20, anchor="middle")
        if i < 2:
            a, b = x + 22, ARC_X[i + 1] - 30
            mid = (a + b) / 2
            p.append(draw(f"M{a} {y - 4} C {mid} {y - 26}, {mid} {ARC_Y[i + 1] - 4}, "
                          f"{b} {ARC_Y[i + 1] + 2}", width=1.75))
            p.append(tri(b + 8, ARC_Y[i + 1] + 2))
            p.append(f'    <text class="dg-edge dg-late" x="{mid}" y="{y - 34}" '
                     f'text-anchor="middle">{t["edges"][i]}</text>')

    # you can start anywhere — the series does not have a locked front door
    p.append('    <path class="dg-stroke" d="M860 404 C 860 456, 120 460, 120 262" '
             'stroke-dasharray="4 5" fill="none"/>')
    p.append(tri(120, 266, -90))
    p.append(f'    <text class="dg-sub" x="490" y="462" text-anchor="middle">{t["loopback"]}</text>')

    return figure("0 0 1080 480", t["aria"], "\n".join(p), t["caption"], t["title"])


# ---------------------------------------------------------------------------
# 6. An accompanied outing — the concert is only the middle third
# ---------------------------------------------------------------------------

OUTING = {
    "en": dict(
        title="Why an outing is three parts, not one",
        caption=("The ticket is rarely what stops someone. Not knowing what happens when you "
                 "get there, and having nobody to go with, is. So the concert is bracketed: "
                 "the two parts either side are the ones that make the middle possible."),
        aria=("Three note-heads under one bracket labelled 'one outing'. The middle one is the "
              "concert itself; the two on either side are preparation beforehand and reflection "
              "afterwards, and are marked as the parts that make the middle possible."),
        span="one outing",
        parts=[(["Before"], ["what the piece is,", "what the room will do"]),
               (["During"], ["we sit together;", "questions at the interval"]),
               (["After"], ["say what you heard —", "there is no wrong answer"])],
        mid_note="the concert itself",
        side_note="the parts that make the middle possible",
        edges=["prepare", "sit together"],
    ),
    "ko": dict(
        title="한 번의 동행이 왜 세 부분인가",
        caption=("사람을 멈춰 세우는 것은 대개 티켓 값이 아닙니다. 가서 무슨 일이 벌어지는지 "
                 "모른다는 것, 그리고 같이 갈 사람이 없다는 것입니다. 그래서 음악회는 괄호 "
                 "안에 놓입니다 — 양옆의 두 부분이 가운데를 가능하게 합니다."),
        aria=("‘한 번의 동행’이라는 괄호 아래 음표 셋. 가운데가 음악회 자체이고, 양옆은 사전 "
              "준비와 사후 나눔으로, 가운데를 가능하게 하는 부분으로 표시돼 있다."),
        span="한 번의 동행",
        parts=[(["가기 전"], ["어떤 곡인지,", "그 자리에서 무슨 일이 있는지"]),
               (["가서"], ["옆자리에 함께 앉고,", "쉬는 시간에 궁금한 것을"]),
               (["다녀와서"], ["들은 것을 말해 봅니다 —", "틀린 답은 없습니다"])],
        mid_note="음악회 그 자체",
        side_note="가운데를 가능하게 하는 부분",
        edges=["준비하고", "함께 앉고"],
    ),
}

OUT_X = [230, 540, 850]


def outing(lang):
    t = OUTING[lang]
    p = []
    p += stave(40, 1000, 128)

    p.append(bracket(180, 900, 96, depth=12))
    p.append(f'    <text class="dg-h" x="540" y="76" text-anchor="middle">{t["span"]}</text>')

    for i, ((head, sub), x) in enumerate(zip(t["parts"], OUT_X)):
        y = 172 if i == 1 else 194
        p.append(note(x, y, open_=(i != 1)))
        p.append(f'    <line class="dg-stroke" x1="{x}" y1="{y + 11}" x2="{x}" y2="246"/>')
        p += lines(x, 272, head, cls="dg-h", anchor="middle")
        p += lines(x, 300, sub, cls="dg-sub", step=20, anchor="middle")
        if i < 2:
            a, b = x + 22, OUT_X[i + 1] - 30
            p.append(draw(f"M{a} {y - 2} H{b}", width=1.75))
            p.append(tri(b + 8, y - 2))
            p.append(f'    <text class="dg-edge dg-late" x="{(a + b) / 2}" y="{y - 14}" '
                     f'text-anchor="middle">{t["edges"][i]}</text>')

    p.append(f'    <text class="dg-sub" x="540" y="352" text-anchor="middle">{t["mid_note"]}</text>')
    p.append(bracket(180, 330, 392, depth=9, below=True))
    p.append(bracket(750, 900, 392, depth=9, below=True))
    p.append(f'    <text class="dg-sub" x="540" y="424" text-anchor="middle">{t["side_note"]}</text>')

    return figure("0 0 1080 450", t["aria"], "\n".join(p), t["caption"], t["title"])


# ---------------------------------------------------------------------------
# 7. An outreach visit — what has to be true for a concert to happen in a room
# ---------------------------------------------------------------------------

VISIT = {
    "en": dict(
        title="What a room has to provide",
        caption=("Everything above the stave arrives in a car. Everything below it is already "
                 "in the building. That is the whole arrangement, and it is why a day room "
                 "with no piano, no stage and no budget can still host a concert."),
        aria=("Two brackets meet at a single note-head marked 'the concert'. The upper bracket, "
              "'we carry in', lists players, instruments, stands, the programme and insurance. "
              "The lower bracket, 'already in the building', lists the room, the people and one "
              "named contact."),
        in_title="we carry in",
        in_rows=["players and instruments", "stands, scores, programme",
                 "a programme built for the room", "insurance and paperwork"],
        room_title="already in the building",
        room_rows=["a room, any room", "the people who live or work there",
                   "one named contact"],
        hub="the concert",
        hub_note=["30–60 minutes · no stage, no piano,", "nothing for the audience to pay"],
    ),
    "ko": dict(
        title="그 방이 준비해야 하는 것",
        caption=("오선 위의 것은 전부 차에 실려 옵니다. 오선 아래의 것은 이미 그 건물 안에 "
                 "있습니다. 준비물은 그게 전부이고, 그래서 피아노도 무대도 예산도 없는 "
                 "휴게실이 음악회를 열 수 있습니다."),
        aria=("두 개의 괄호가 ‘음악회’라는 하나의 음표에서 만난다. 위쪽 괄호 ‘우리가 싣고 가는 것’은 "
              "연주자·악기·보면대·프로그램·보험을, 아래쪽 괄호 ‘이미 그 건물에 있는 것’은 방과 "
              "사람과 담당자 한 사람을 담고 있다."),
        in_title="우리가 싣고 가는 것",
        in_rows=["연주자와 악기", "보면대 · 악보 · 프로그램",
                 "그 방에 맞춰 짠 곡목", "보험과 서류"],
        room_title="이미 그 건물에 있는 것",
        room_rows=["방 하나, 어떤 방이든", "거기 살거나 일하는 사람들",
                   "담당자 한 사람"],
        hub="음악회",
        hub_note=["30–60분 · 무대도 피아노도 없이,", "관객이 낼 돈도 없이"],
    ),
}


# Two lists, each on its own leader rules, meeting at one note. The earlier
# version ran a stave straight through the words and set both headings hard on
# the frame edge; nothing here touches the margin now.
VISIT_LEFT = 24                 # left margin for both lists
VISIT_COLLECT = 520             # x of the gold rule each list arrives at
VISIT_HUB = (760, 250)


def visit(lang):
    t = VISIT[lang]
    hx, hy = VISIT_HUB
    x, cx = VISIT_LEFT, VISIT_COLLECT
    p = []

    def group(title, rows, y0, ytitle):
        ys = [y0 + i * 44 for i in range(len(rows))]
        out = [f'    <text class="dg-edge" x="{x}" y="{ytitle}">{title}</text>']
        for row, y in zip(rows, ys):
            out.append(note(x + 14, y - 5, open_=True))
            out.append(f'    <text class="dg-label" x="{x + 44}" y="{y}">{row}</text>')
            out.append(f'    <line class="dg-stroke" x1="{x}" y1="{y + 14}" '
                       f'x2="{cx}" y2="{y + 14}"/>')
        top, bot = ys[0] + 14, ys[-1] + 14
        out.append(f'    <line class="dg-stroke-accent" x1="{cx}" y1="{top}" '
                   f'x2="{cx}" y2="{bot}" stroke-width="2.5"/>')
        return out, (top + bot) / 2

    up, a = group(t["in_title"], t["in_rows"], 78, 44)
    down, b = group(t["room_title"], t["room_rows"], 330, 296)
    p += up + down

    # both lists converge on the same note-head
    p.append(draw(f"M{cx} {a} C {cx + 90} {a}, {cx + 110} {hy}, {hx - 34} {hy}", width=3))
    p.append(draw(f"M{cx} {b} C {cx + 90} {b}, {cx + 110} {hy}, {hx - 34} {hy}", width=3))
    p.append(tri(hx - 24, hy))

    p.append(note(hx, hy))
    p.append(f'    <text class="dg-h" x="{hx + 28}" y="{hy + 6}">{t["hub"]}</text>')
    p += lines(hx + 28, hy + 32, t["hub_note"], cls="dg-sub", step=20)

    return figure("0 0 1080 500", t["aria"], "\n".join(p), t["caption"], t["title"])


# ---------------------------------------------------------------------------
# 8. Letters Ensemble — what four concerts are actually resting on
# ---------------------------------------------------------------------------

REHEARSE = {
    "en": dict(
        title="What four concerts are resting on",
        caption=("Four concerts are the part of this that got written down. Underneath them is "
                 "weekly rehearsal since January 2024 — well over a hundred afternoons, none of "
                 "which we recorded. We are counting them from now on, because the rehearsal is "
                 "the programme and the concert is the receipt."),
        aria=("A long row of small equal note-heads under a bracket reading 'every Saturday since "
              "January 2024 — over one hundred, none of them recorded', with an arrow leading to "
              "four larger-spaced note-heads marked 'four formal concerts, documented'."),
        many="every Saturday since January 2024",
        many_sub="well over a hundred · none of them recorded",
        edge="what gets written down",
        few="four formal concerts",
        few_sub="programmes, photographs, dates",
        foot="amateur musicians living in Dublin · about two hours · open to new players",
    ),
    "ko": dict(
        title="네 번의 음악회가 딛고 선 것",
        caption=("네 번의 음악회는 기록으로 남은 부분입니다. 그 아래에는 2024년 1월부터의 주간 "
                 "연습이 있습니다 — 백 번이 훨씬 넘는 토요일이고, 그중 어느 것도 기록해 두지 "
                 "않았습니다. 이제부터는 셉니다. 연습이 프로그램이고 음악회는 영수증입니다."),
        aria=("‘2024년 1월부터 매주 토요일 — 백 회가 넘고, 기록된 것은 없음’이라는 괄호 아래 "
              "같은 크기의 작은 음표가 길게 늘어서 있고, 화살표가 ‘정식 음악회 네 번, 기록됨’으로 "
              "표시된 음표 네 개로 이어진다."),
        many="2024년 1월부터 매주 토요일",
        many_sub="백 회가 훨씬 넘습니다 · 기록해 둔 것은 없습니다",
        edge="기록으로 남는 것",
        few="정식 음악회 4회",
        few_sub="프로그램 · 사진 · 날짜",
        foot="더블린에 사는 아마추어 연주자들 · 약 2시간 · 새 연주자를 환영합니다",
    ),
}


def rehearsals(lang):
    t = REHEARSE[lang]
    p = []
    p += stave(24, 588, 120, gap=18, n=5)

    for i in range(16):
        p.append(note(46 + i * 33, 156 if i % 2 else 174))
    p.append(f'    <text class="dg-sub" x="562" y="170">···</text>')
    p.append(bracket(24, 612, 96, depth=11))
    p.append(f'    <text class="dg-h" x="24" y="74">{t["many"]}</text>')
    p.append(f'    <text class="dg-sub" x="24" y="232">{t["many_sub"]}</text>')

    p.append(draw("M636 165 H 752", width=2.5))
    p.append(tri(762, 165))
    p.append(f'    <text class="dg-edge dg-late" x="696" y="146" '
             f'text-anchor="middle">{t["edge"]}</text>')

    p += stave(792, 264, 120, gap=18, n=5)
    for i in range(4):
        p.append(note(832 + i * 62, 156))
    p.append(bracket(792, 1056, 96, depth=11))
    p.append(f'    <text class="dg-h" x="792" y="74">{t["few"]}</text>')
    p.append(f'    <text class="dg-sub" x="792" y="232">{t["few_sub"]}</text>')

    p.append(f'    <text class="dg-sub" x="540" y="286" text-anchor="middle">{t["foot"]}</text>')

    return figure("0 0 1080 300", t["aria"], "\n".join(p), t["caption"], t["title"])


# ---------------------------------------------------------------------------
# 9. Four ways in — one door, and permission to change your mind
# ---------------------------------------------------------------------------

WAYS = {
    "en": dict(
        title="Four ways in, one door",
        caption=("The four routes are not four application processes. They are four sentences "
                 "you might write in the same email, and people move between them all the time "
                 "— most of the players started as listeners, and two of the rooms we play in "
                 "were offered by someone who came to a concert."),
        aria=("Four note-heads threaded on one dashed vertical line — learn to play, come and "
              "listen, play with us, host or partner — labelled 'people move between these'. All "
              "four run right to a single gold rule, and one arrow leaves it for a note-head "
              "marked 'one email, one line'."),
        rows=[(["Learn to play"], ["you have never played anything"]),
              (["Come and listen"], ["you would rather start by listening"]),
              (["Play with us"], ["you already play something"]),
              (["Host or partner"], ["you have a room, or you know one"])],
        hub=["one email,", "one line"],
        hub_note="we answer with the practical details",
        move="people move between these",
        edge="whichever sounds like you",
    ),
    "ko": dict(
        title="네 가지 길, 하나의 문",
        caption=("네 갈래는 네 개의 신청 절차가 아닙니다. 같은 이메일에 쓸 수 있는 네 개의 문장이고, "
                 "사람들은 그 사이를 늘 오갑니다 — 지금 연주하는 사람 대부분이 처음에는 듣는 "
                 "사람이었고, 우리가 연주하는 방 중 둘은 음악회에 왔던 분이 내어 준 것입니다."),
        aria=("점선 하나에 꿰인 음표 네 개 — 배우러 오기, 들으러 오기, 함께 연주하기, 공간 열기. "
              "그 점선에는 ‘사람들은 이 사이를 오갑니다’라고 적혀 있다. 네 갈래는 모두 오른쪽의 "
              "금색 선에서 만나고, 거기서 화살표 하나가 ‘이메일 한 통, 한 줄’ 음표로 간다."),
        rows=[(["배우러 옵니다"], ["악기를 잡아 본 적이 없어도"]),
              (["들으러 옵니다"], ["듣는 것부터 시작하고 싶다면"]),
              (["함께 연주합니다"], ["이미 다루는 악기가 있다면"]),
              (["공간을 엽니다"], ["방이 있거나, 아는 방이 있다면"])],
        hub=["이메일 한 통,", "한 줄"],
        hub_note="실무적인 내용으로 답을 드립니다",
        move="사람들은 이 사이를 오갑니다",
        edge="당신에게 맞는 쪽으로",
    ),
}

# Four rows on one spine, a collector, and a single destination. The earlier
# version let the connectors start in mid-air and hung the four off dashed
# hooks that curled outside the frame; both read as decoration. Here the spine
# IS the "you can move between these" claim — the four note-heads sit on it —
# and every connector starts on a label and ends on the hub.
WAYS_Y = [88, 176, 264, 352]    # baseline of each row's heading
WAYS_SPINE = 60                 # x of the dashed spine the four heads sit on
WAYS_COLLECT = 520              # x of the gold rule every route arrives at
WAYS_RULE = 46                  # heading baseline -> the row's own leader rule


def pathways(lang):
    t = WAYS[lang]
    top, bottom = WAYS_Y[0] + WAYS_RULE, WAYS_Y[-1] + WAYS_RULE
    hy = (top + bottom) // 2
    hx = 760
    p = []

    # the spine: one dashed line through all four, because they are one family
    p.append(f'    <line class="dg-stroke" x1="{WAYS_SPINE}" y1="{WAYS_Y[0] - 36}" '
             f'x2="{WAYS_SPINE}" y2="{bottom + 16}" stroke-dasharray="3 5"/>')

    for (head, sub), y in zip(t["rows"], WAYS_Y):
        p.append(note(WAYS_SPINE, y - 6))
        p += lines(WAYS_SPINE + 30, y, head, cls="dg-h")
        p += lines(WAYS_SPINE + 30, y + 25, sub, cls="dg-sub", step=18)
        # the row's own rule runs under it and carries on into the collector,
        # so no connector begins in mid-air
        p.append(f'    <line class="dg-stroke" x1="{WAYS_SPINE}" y1="{y + WAYS_RULE}" '
                 f'x2="{WAYS_COLLECT}" y2="{y + WAYS_RULE}"/>')

    # the collector — four rules, one edge
    p.append(f'    <line class="dg-stroke-accent" x1="{WAYS_COLLECT}" y1="{top}" '
             f'x2="{WAYS_COLLECT}" y2="{bottom}" stroke-width="2.5"/>')
    p.append(draw(f"M{WAYS_COLLECT} {hy} H{hx - 34}", width=2.5))
    p.append(tri(hx - 24, hy))
    p.append(f'    <text class="dg-edge dg-late" x="{(WAYS_COLLECT + hx) // 2 - 12}" '
             f'y="{hy - 18}" text-anchor="middle">{t["edge"]}</text>')

    # the one destination
    p.append(note(hx, hy))
    p += lines(hx + 28, hy - 4, t["hub"], cls="dg-h", step=26)
    p.append(f'    <text class="dg-sub" x="{hx + 28}" y="{hy + 46}">{t["hub_note"]}</text>')

    # what the spine means, said once, at its foot
    p.append(f'    <text class="dg-sub" x="{WAYS_SPINE - 14}" y="{bottom + 44}">'
             f'{t["move"]}</text>')

    return figure("0 0 1080 460", t["aria"], "\n".join(p), t["caption"], t["title"])


# ---------------------------------------------------------------------------
# 10. The drawing vocabulary itself — the key to every other figure here
# ---------------------------------------------------------------------------

VOCAB = {
    "en": dict(
        title="How to read every diagram on this site",
        caption=("Four marks, borrowed from notation, used the same way in every figure. The "
                 "note-head is the load-bearing one: it is always the same size, so nothing on "
                 "a stave can be quietly ranked above anything else. That is a design decision "
                 "about the organisation, not about the drawing."),
        aria=("A key to four drawing marks: the stave, the note-head, the bracket and the "
              "crescendo wedge, each with the meaning it carries in the diagrams on this site."),
        items=[(["The stave"], ["four quiet lines and one", "that carries the weight"]),
               (["The note-head"], ["one unit — always the same", "size, whatever it stands for"]),
               (["The bracket"], ["what groups with what;", "dashed means still a claim"]),
               (["The crescendo"], ["the only mark here", "that means &lsquo;this grows&rsquo;"])],
    ),
    "ko": dict(
        title="이 사이트의 도식을 읽는 법",
        caption=("악보에서 빌려 온 네 개의 표시를 모든 도식에서 같은 뜻으로 씁니다. 무게를 지는 "
                 "것은 음표 머리입니다 — 무엇을 나타내든 크기가 같아서, 오선 위의 어떤 것도 "
                 "다른 것보다 슬그머니 높아질 수 없습니다. 이건 그림에 관한 결정이 아니라 "
                 "단체에 관한 결정입니다."),
        aria=("네 가지 표시의 범례 — 오선, 음표 머리, 괄호, 크레셴도 쐐기. 각각이 이 사이트의 "
              "도식에서 갖는 뜻이 함께 적혀 있다."),
        items=[(["오선"], ["조용한 네 줄과", "무게를 지는 다섯째 줄"]),
               (["음표 머리"], ["단위 — 무엇을 나타내든", "크기가 같습니다"]),
               (["괄호"], ["무엇이 무엇과 묶이는지;", "점선은 아직 주장입니다"]),
               (["크레셴도"], ["이 세트에서 ‘자란다’를", "뜻하는 유일한 표시"])],
    ),
}


def vocabulary(lang):
    t = VOCAB[lang]
    p = []
    x0, step = 8, 268

    for i, (head, sub) in enumerate(t["items"]):
        x = x0 + i * step
        if i == 0:
            p += stave(x, 180, 34, gap=13, n=5)
        elif i == 1:
            for j in range(3):
                p.append(note(x + 34 + j * 52, 62))
        elif i == 2:
            p.append(bracket(x + 10, x + 110, 74, depth=13))
            p.append(bracket(x + 124, x + 190, 74, depth=13, dashed=True))
        else:
            p.append(f'    <path class="dg-note" opacity=".3" '
                     f'd="M{x + 8} 62 L{x + 196} 44 L{x + 196} 84 L{x + 8} 66 Z"/>')
        p.append(f'    <line class="dg-stroke-accent" x1="{x}" y1="118" x2="{x + 200}" y2="118" '
                 f'stroke-width="2"/>')
        p += lines(x, 146, head, cls="dg-h")
        p += lines(x, 174, sub, cls="dg-sub", step=19)

    return figure("0 0 1080 210", t["aria"], "\n".join(p), t["caption"], t["title"])
