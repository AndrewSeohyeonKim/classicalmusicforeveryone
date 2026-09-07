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
        caption=("Five programmes, two halves, one circuit. None of them is the main one, and "
                 "removing any single item leaves the other side unfed. Without playing for "
                 "people we never meet the person who asks, and without a class there is "
                 "nowhere to send them."),
        aria=("Two panels of equal width. The left, Learning, lists three programmes; the "
              "right, Sharing, lists two. Every item carries a note-head of the same size. An "
              "arc from Learning to Sharing is labelled 'a player, ready for the room'; a "
              "mirrored arc back is labelled 'could I do that?'."),
        pillar_a="Learning", pillar_a_sub="we teach people to play",
        pillar_b="Sharing", pillar_b_sub="we bring the music to the room",
        top="a player, ready for the room",
        bottom="“could I do that?”",
        progs=[("Recorder Ensemble course", "a term, weekly"),
               ("Getting to Know Classical Music", "roughly monthly"),
               ("Concert Guide &amp; Companion", "small groups"),
               ("Outreach Concerts", "care homes · parishes"),
               ("Letters Ensemble", "weekly rehearsals")],
    ),
    "ko": dict(
        title="우리가 하는 일 전체",
        caption=("다섯 개의 프로그램이 두 갈래로 나뉘어 한 바퀴를 돕니다. 대표는 없습니다. "
                 "하나를 떼어 내면 반대쪽이 굶습니다. 찾아가 연주하지 않으면 묻는 사람을 "
                 "만날 일이 없고, 수업이 없으면 그 사람을 보낼 데가 없습니다."),
        aria=("같은 너비의 패널 둘. 왼쪽 ‘배움’에는 세 프로그램, 오른쪽 ‘나눔’에는 두 "
              "프로그램이 들어 있고, 모든 항목에 같은 크기의 음표가 붙어 있다. 배움에서 나눔으로 "
              "가는 곡선은 ‘그 방에 설 준비가 된 연주자’, 대칭으로 돌아오는 곡선은 ‘나도 해 볼 수 "
              "있을까?’로 표시된다."),
        pillar_a="배움", pillar_a_sub="악기를 직접 잡도록 가르칩니다",
        pillar_b="나눔", pillar_b_sub="그 방으로 음악을 들고 갑니다",
        top="그 방에 설 준비가 된 연주자",
        bottom="“나도 해 볼 수 있을까?”",
        progs=[("리코더 앙상블 과정", "한 학기 · 주 1회"),
               ("클래식 음악과 친해지기", "대략 월 1회"),
               ("함께하는 음악여행", "소그룹 동행"),
               ("찾아가는 음악회", "요양시설 · 본당"),
               ("Letters Ensemble", "주 1회 정기연습")],
    ),
}

# Geometry.
#
# The stave is gone from this one. It was doing two jobs badly: five heads at
# five pitches read as a misalignment before it read as music, and the ruled
# lines ran straight through the panel headings. What the figure has to say is
# simpler than that — two named halves, five equal items, and a circuit — so it
# says it with two panels of the same width and two arcs that are exact 180°
# rotations of each other about the centre of the figure. Mirrored geometry is
# why they now enter together instead of one arriving crooked after the other.
MAP_PANEL_Y, MAP_PANEL_H = 128, 264
MAP_ZONES = ((24, 486), (570, 486))          # x, width — deliberately equal
MAP_ROW_STEP = 52
MAP_MID = MAP_PANEL_Y + MAP_PANEL_H / 2      # 260 — both arcs mirror about this
MAP_ARC = MAP_PANEL_H / 2                    # the arcs leave the panel edge itself


def _map_rows(zx, zw, rows, open_):
    """One programme per row: an equal note-head, a name, and a right-set meta."""
    out, n = [], len(rows)
    top = 308 - (n - 1) * MAP_ROW_STEP / 2
    for i, (name, meta) in enumerate(rows):
        y = top + i * MAP_ROW_STEP
        out.append(note(zx + 40, y - 5, open_=open_))
        out.append(f'    <text class="dg-label" x="{zx + 70}" y="{y}">{name}</text>')
        out.append(f'    <text class="dg-sub" x="{zx + zw - 28}" y="{y}" '
                   f'text-anchor="end">{meta}</text>')
    return out


def programme_map(lang):
    t = MAP[lang]
    py, ph = MAP_PANEL_Y, MAP_PANEL_H
    p = []

    for (zx, zw), head, sub in zip(MAP_ZONES,
                                   (t["pillar_a"], t["pillar_b"]),
                                   (t["pillar_a_sub"], t["pillar_b_sub"])):
        p.append(f'    <rect class="dg-fill-soft" x="{zx}" y="{py}" width="{zw}" '
                 f'height="{ph}" rx="14"/>')
        p.append(f'    <text class="dg-h" x="{zx + 28}" y="{py + 44}">{head}</text>')
        p.append(f'    <text class="dg-sub" x="{zx + 28}" y="{py + 70}">{sub}</text>')
        p.append(f'    <line class="dg-stroke" x1="{zx + 28}" y1="{py + 90}" '
                 f'x2="{zx + zw - 28}" y2="{py + 90}"/>')

    p += _map_rows(*MAP_ZONES[0], t["progs"][:3], False)
    p += _map_rows(*MAP_ZONES[1], t["progs"][3:], True)

    # the circuit — one arc out, one back, each the other turned through 180°
    a = MAP_ZONES[0][0] + MAP_ZONES[0][1] / 2
    b = MAP_ZONES[1][0] + MAP_ZONES[1][1] / 2
    yt, yb = MAP_MID - MAP_ARC, MAP_MID + MAP_ARC

    p.append(f'    <text class="dg-edge dg-late" x="540" y="44" '
             f'text-anchor="middle">{t["top"]}</text>')
    p.append(draw(f"M{a} {yt} C {a} {yt - 74}, {b} {yt - 74}, {b} {yt - 12}"))
    p.append(tri(b, yt, 90))

    p.append(draw(f"M{b} {yb} C {b} {yb + 74}, {a} {yb + 74}, {a} {yb + 12}"))
    p.append(tri(a, yb, 270))
    p.append(f'    <text class="dg-edge dg-late" x="540" y="480" '
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
        caption=("왼쪽에서 오른쪽으로 읽습니다. 실선 괄호는 저희가 세어서 보여 드릴 수 있는 "
                 "것이고, 점선 괄호는 참가자와 공간이 해 준 말입니다. 아직 재 보지 않았습니다. "
                 "그 경계는 흐리지 않고 그어 둡니다."),
        aria=("왼쪽에서 오른쪽으로 네 단계 — 투입이 활동을 사고, 활동이 산출을 만들고, 산출이 변화를 "
              "가리킨다. 실선 괄호는 앞의 세 단계를 ‘세어서 기록함’으로, 점선 괄호는 네 번째를 "
              "‘증언에 근거, 아직 측정 안 됨’으로 표시한다."),
        cols=[("투입", ["교육가와 연주자", "리코더와 악보",
                        "주 1회 쓸 방", "보조금과 참가비"]),
              ("활동", ["한 학기 수업", "함께 연주하기",
                        "그 방에서의 음악회", "공연에 함께 가기"]),
              ("산출", ["진행한 세션", "수료한 사람",
                        "닿은 공간", "치른 음악회"]),
              ("변화", ["줄어든 고립", "존엄과 성취",
                        "세대를 잇는 관계", "교육가의 일자리"])],
        edges=["산다", "만든다", "가리킨다"],
        evidenced="세어서 기록함",
        claimed="증언에 근거 · 아직 측정 안 됨",
    ),
}


def theory_of_change(lang):
    t = TOC[lang]
    # The gap has to hold the edge label, not just the arrow. At 64px it did
    # not: "points to" is about 75px wide at 11.5px with .09em tracking, so it
    # ran straight through the gold rule of the column it was pointing at.
    x0, w, gap = 24, 189, 92
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
            a, b = x + w + 12, x + w + gap - 24
            p.append(draw(f"M{a} 120 H{b}", width=1.75))
            p.append(tri(b + 10, 120))
            p.append(f'    <text class="dg-edge dg-late" x="{(a + b) / 2 + 5}" y="102" '
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
        caption=("만족스러운 첫 소리가 6주차가 아니라 1주차에 나오도록 짜여 있습니다. "
                 "악보를 읽을 줄 안다고 전제하지 않고, 모든 단계를 그룹 전체가 함께 넘습니다. "
                 "끝나는 방식은 하나뿐입니다. 사람들 앞에서."),
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
        caption=("돈은 세 방향에서 들어와, 아무도 값을 치르지 않은 자리로 나갑니다. 선의 "
                 "굵기는 각자의 몫을 나타냅니다. 유료 층을 걷어내면 무료 층이 가장 먼저 "
                 "사라집니다."),
        aria=("기관과 낼 수 있는 참가자, 보조금이 Classical Music for Everyone에 지불하고, 그 돈이 "
              "무료 자리와 더 많은 방으로 나가며, 잉여는 다시 안으로 돌아온다."),
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
    """Money in, money out — every connector leaving a real panel edge.

    The earlier version started each curve at x=320, in the white space to the
    right of a ragged column of text, which is the one thing the figures here
    are not allowed to do: a line that begins in mid-air reads as unfinished.
    Each side is a panel of fixed width now, the same device `pathways` uses,
    so every line leaves an edge at the same x.
    """
    t = SUBSIDY[lang]
    p = []
    lx, lw = 24, 270                  # money in
    rx, rw = 780, 276                 # what it buys
    hx, hw = 430, 220                 # the hub
    hub_y = 196
    in_y = (86, 198, 310)
    out_y = (130, 282)
    ch = 80                           # panel height

    def panel(x, w, cy, rows, notes):
        out = [f'    <rect class="dg-fill-soft" x="{x}" y="{cy - ch / 2}" width="{w}" '
               f'height="{ch}" rx="12"/>',
               f'    <line class="dg-stroke-accent" x1="{x + 20}" y1="{cy - 20}" '
               f'x2="{x + 20}" y2="{cy + 20}" stroke-width="2.5"/>']
        out += lines(x + 36, cy - 4, rows)
        out += lines(x + 36, cy + 18, notes, cls="dg-sub", step=18)
        return out

    p.append(f'    <text class="dg-edge" x="{lx}" y="34">{t["in_title"]}</text>')
    for (rows, notes, wt), y in zip(t["in_rows"], in_y):
        p += panel(lx, lw, y, rows, notes)
        # control points on a single vertical, so the S never bulges backwards
        p.append(draw(f"M{lx + lw} {y} C {(lx + lw + hx) / 2} {y}, "
                      f"{(lx + lw + hx) / 2} {hub_y}, {hx - 30} {hub_y}", width=wt))
    p.append(tri(hx - 18, hub_y))
    # on the same baseline as the two section titles: every other place in this
    # gap is crossed by one of the three curves
    p.append(f'    <text class="dg-edge dg-late" x="{(lx + lw + hx) / 2}" y="34" '
             f'text-anchor="middle">{t["edge_in"]}</text>')

    p.append(f'    <rect class="dg-fill-accent dg-box" x="{hx}" y="{hub_y - 42}" rx="12" '
             f'width="{hw}" height="84" stroke-width="1.8"/>')
    p += lines(hx + hw / 2, hub_y - 14, t["hub"], cls="dg-label", step=20, anchor="middle")
    p.append(f'    <text class="dg-sub" x="{hx + hw / 2}" y="{hub_y + 24}" '
             f'text-anchor="middle">{t["hub_note"]}</text>')

    p.append(f'    <text class="dg-edge" x="{rx}" y="34">{t["out_title"]}</text>')
    for (rows, notes, wt), y in zip(t["out_rows"], out_y):
        p += panel(rx, rw, y, rows, notes)
        p.append(draw(f"M{hx + hw} {hub_y} C {(hx + hw + rx) / 2} {hub_y}, "
                      f"{(hx + hw + rx) / 2} {y}, {rx - 30} {y}", width=wt))
        p.append(tri(rx - 18, y))
    p.append(f'    <text class="dg-edge dg-late" x="{(hx + hw + rx) / 2}" y="34" '
             f'text-anchor="middle">{t["edge_out"]}</text>')

    # the surplus goes back in — dashed, because it is the part that only
    # happens in a good year
    p.append(f'    <path class="dg-stroke" d="M{rx + 40} {out_y[1] + ch / 2} '
             f'C {rx + 40} 398, {hx + hw / 2} 402, {hx + hw / 2} {hub_y + 56}" '
             'stroke-dasharray="4 5" fill="none"/>')
    p.append(tri(hx + hw / 2, hub_y + 48, -90))
    p.append(f'    <text class="dg-sub" x="{(hx + hw / 2 + rx + 40) / 2}" y="416" '
             f'text-anchor="middle">{t["loop"]}</text>')

    return figure("0 0 1080 440", t["aria"], "\n".join(p), t["caption"], t["title"])


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
        caption=("세 단계가 옮기는 것은 난이도가 아니라 소유입니다. 음악은 처음에 남의 "
                 "것이었다가, 그 방이 함께 가진 것이 되고, 끝에는 내 것이 됩니다. 각 회차는 "
                 "그 자체로 완결돼 있어서, 늦게 온 사람이 앞부분을 놓친 채 앉아 있을 일이 "
                 "없습니다."),
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
    p.append(f'    <text class="dg-sub" x="104" y="280">{t["entry"]}</text>')
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
            # above the stave, not between its lines: at 11.5px a label set
            # inside a 22px gap is struck through by the rule above it
            p.append(f'    <text class="dg-edge dg-late" x="{mid}" y="130" '
                     f'text-anchor="middle">{t["edges"][i]}</text>')

    # you can start anywhere — the series does not have a locked front door
    p.append('    <path class="dg-stroke" d="M860 404 C 860 456, 56 460, 56 238 H 90" '
             'stroke-dasharray="4 5" fill="none"/>')
    p.append(tri(100, 238))
    p.append(f'    <text class="dg-sub" x="500" y="462" text-anchor="middle">{t["loopback"]}</text>')

    return figure("0 100 1080 384", t["aria"], "\n".join(p), t["caption"], t["title"])


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
        caption=("발목을 잡는 것은 대개 티켓 값이 아닙니다. 가서 뭘 어떻게 해야 하는지 "
                 "모른다는 것, 같이 갈 사람이 없다는 것입니다. 그래서 음악회를 괄호 안에 "
                 "넣었습니다. 양옆의 두 부분이 가운데를 가능하게 합니다."),
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
    # the stave sits low enough that the edge labels can live above it. Set
    # between the rules they were struck through by the line above them.
    p += stave(40, 1000, 150)

    p.append(bracket(180, 900, 96, depth=12))
    p.append(f'    <text class="dg-h" x="540" y="76" text-anchor="middle">{t["span"]}</text>')

    ys = [216, 194, 216]
    for i, ((head, sub), x) in enumerate(zip(t["parts"], OUT_X)):
        y = ys[i]
        p.append(note(x, y, open_=(i != 1)))
        p.append(f'    <line class="dg-stroke" x1="{x}" y1="{y + 11}" x2="{x}" y2="268"/>')
        p += lines(x, 294, head, cls="dg-h", anchor="middle")
        p += lines(x, 322, sub, cls="dg-sub", step=20, anchor="middle")
        if i < 2:
            # the connector runs note to note, so the arrowhead lands on the
            # thing it points at rather than 22px under it
            a, b = x + 22, OUT_X[i + 1] - 32
            y2 = ys[i + 1]
            p.append(draw(f"M{a} {y - 2} L{b} {y2 - 2}", width=1.75))
            p.append(tri(b + 10, y2 - 2))
            p.append(f'    <text class="dg-edge dg-late" x="{(a + b) / 2}" y="138" '
                     f'text-anchor="middle">{t["edges"][i]}</text>')

    # the middle gets its label and the two sides get their bracket on the same
    # line, so the three read as one row rather than two stranded ticks
    p.append(f'    <text class="dg-sub" x="540" y="374" text-anchor="middle">{t["mid_note"]}</text>')
    p.append(bracket(180, 330, 366, depth=9, below=True))
    p.append(bracket(750, 900, 366, depth=9, below=True))
    p.append(f'    <text class="dg-sub" x="540" y="404" text-anchor="middle">{t["side_note"]}</text>')

    return figure("0 0 1080 428", t["aria"], "\n".join(p), t["caption"], t["title"])


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
        caption=("위쪽은 전부 차에 실려 옵니다. 아래쪽은 이미 그 건물 안에 있습니다. "
                 "준비물은 그게 전부입니다. 그래서 피아노도 무대도 예산도 없는 휴게실이 "
                 "음악회를 열 수 있습니다."),
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


# Two lists meeting at one note-head. The version before this ran a leader
# rule from every row out to a shared vertical, which drew four horizontals
# and a right-hand vertical — a comb that read as a table with its left side
# missing. Each row is a panel now, the same device as `pathways` and
# `subsidy`, so a connector leaves a real edge instead of the end of a word.
VISIT_LEFT, VISIT_W = 24, 420   # x and width of every row panel
VISIT_COLLECT = 520             # x of the gold rule each list arrives at
VISIT_HUB = (720, 232)
VISIT_ROW = 46                  # row pitch


def visit(lang):
    t = VISIT[lang]
    hx, hy = VISIT_HUB
    x, w, cx = VISIT_LEFT, VISIT_W, VISIT_COLLECT
    p = []

    def group(title, rows, y0, ytitle):
        ys = [y0 + i * VISIT_ROW for i in range(len(rows))]
        out = [f'    <text class="dg-edge" x="{x}" y="{ytitle}">{title}</text>']
        for row, y in zip(rows, ys):
            out.append(f'    <rect class="dg-fill-soft" x="{x}" y="{y - 18}" width="{w}" '
                       f'height="36" rx="10"/>')
            out.append(note(x + 26, y - 4, open_=True))
            out.append(f'    <text class="dg-label" x="{x + 52}" y="{y + 1}">{row}</text>')
            out.append(f'    <line class="dg-stroke" x1="{x + w}" y1="{y}" '
                       f'x2="{cx}" y2="{y}"/>')
        out.append(f'    <line class="dg-stroke-accent" x1="{cx}" y1="{ys[0]}" '
                   f'x2="{cx}" y2="{ys[-1]}" stroke-width="2.5"/>')
        return out, (ys[0] + ys[-1]) / 2

    up, a = group(t["in_title"], t["in_rows"], 76, 44)
    down, b = group(t["room_title"], t["room_rows"], 296, 264)
    p += up + down

    # both lists converge on the same note-head
    p.append(draw(f"M{cx} {a} C {cx + 80} {a}, {cx + 100} {hy}, {hx - 34} {hy}", width=3))
    p.append(draw(f"M{cx} {b} C {cx + 80} {b}, {cx + 100} {hy}, {hx - 34} {hy}", width=3))
    p.append(tri(hx - 22, hy))

    p.append(note(hx, hy))
    p.append(f'    <text class="dg-h" x="{hx + 28}" y="{hy + 6}">{t["hub"]}</text>')
    p += lines(hx + 28, hy + 32, t["hub_note"], cls="dg-sub", step=20)

    return figure("0 0 1080 432", t["aria"], "\n".join(p), t["caption"], t["title"])


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
        caption=("네 번의 음악회는 기록으로 남은 부분입니다. 그 아래에 2024년 1월부터의 주간 "
                 "연습이 있습니다. 백 번이 훨씬 넘는 토요일이고, 그중 어느 것도 기록해 두지 "
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
        p.append(note(46 + i * 33, 156))
    p.append(f'    <text class="dg-sub" x="568" y="161">···</text>')
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
        aria=("Four panels of equal size — learn to play, come and listen, play with us, host "
              "or partner — linked by dashed lines labelled 'people move between these'. All "
              "four run right to a single gold rule, and one arrow leaves it for a panel marked "
              "'one email, one line'."),
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
        caption=("네 갈래는 네 개의 신청 절차가 아닙니다. 같은 이메일에 쓸 수 있는 네 개의 "
                 "문장이고, 사람들은 그 사이를 늘 오갑니다. 지금 연주하는 사람 대부분이 "
                 "처음에는 듣는 사람이었고, 저희가 연주하는 방 중 둘은 음악회에 왔던 분이 "
                 "내어 준 것입니다."),
        aria=("같은 크기의 판 넷 — 배우러 오기, 들으러 오기, 함께 연주하기, 공간 열기 — 이 "
              "점선으로 이어져 있고 그 점선에는 ‘사람들은 이 사이를 오갑니다’라고 적혀 있다. "
              "네 갈래는 모두 오른쪽 금색 선에서 만나고, 거기서 화살표 하나가 ‘이메일 한 통, "
              "한 줄’ 판으로 간다."),
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
# Four chips, one collector, one destination.
#
# Earlier versions let the connectors begin in mid-air beside a ragged column
# of text, which is what made the figure look unfinished: the eye could not
# tell where a route started. Giving each route a chip of fixed width fixes
# that — every connector now leaves a real edge, at the same x, at the vertical
# centre of the thing it belongs to. The dashes in the gaps between the chips
# are the whole claim of the figure: these are not four separate doors.
WAYS_X, WAYS_W, WAYS_H = 24, 400, 76
WAYS_Y = [44, 144, 244, 344]      # top of each chip
WAYS_COLLECT = 496                # x of the gold rule every route arrives at
WAYS_HUB = (760, 296)             # x, width of the destination chip


def pathways(lang):
    t = WAYS[lang]
    x, w, h = WAYS_X, WAYS_W, WAYS_H
    cx, (hx, hw) = WAYS_COLLECT, WAYS_HUB
    mids = [y + h / 2 for y in WAYS_Y]
    hy = (mids[0] + mids[-1]) / 2
    p = []

    for (head, sub), y, my in zip(t["rows"], WAYS_Y, mids):
        p.append(f'    <rect class="dg-fill-soft" x="{x}" y="{y}" width="{w}" '
                 f'height="{h}" rx="12"/>')
        p.append(note(x + 34, my - 4))
        p += lines(x + 64, my, head, cls="dg-h")
        p += lines(x + 64, my + 25, sub, cls="dg-sub", step=18)
        p.append(f'    <line class="dg-stroke" x1="{x + w}" y1="{my}" x2="{cx}" y2="{my}"/>')

    # the dashes live in the gaps: you can move from any chip to any other
    for a, b in zip(WAYS_Y[:-1], WAYS_Y[1:]):
        p.append(f'    <line class="dg-stroke" x1="{x + 34}" y1="{a + h}" '
                 f'x2="{x + 34}" y2="{b}" stroke-dasharray="3 4"/>')
    p.append(f'    <text class="dg-sub" x="{x}" y="{WAYS_Y[-1] + h + 34}">{t["move"]}</text>')

    # four routes, one edge, one arrow
    p.append(f'    <line class="dg-stroke-accent" x1="{cx}" y1="{mids[0]}" '
             f'x2="{cx}" y2="{mids[-1]}" stroke-width="2.5"/>')
    p.append(draw(f"M{cx} {hy} H{hx - 34}", width=2.5))
    p.append(tri(hx - 22, hy))
    p.append(f'    <text class="dg-edge dg-late" x="{(cx + hx - 34) / 2}" y="{hy - 16}" '
             f'text-anchor="middle">{t["edge"]}</text>')

    # the destination
    p.append(f'    <rect class="dg-fill-accent dg-box" x="{hx}" y="{hy - 62}" width="{hw}" '
             f'height="124" rx="12" stroke-width="1.6"/>')
    p += lines(hx + 32, hy - 18, t["hub"], cls="dg-h", step=27)
    p.append(f'    <text class="dg-sub" x="{hx + 32}" y="{hy + 38}">{t["hub_note"]}</text>')

    return figure("0 0 1080 470", t["aria"], "\n".join(p), t["caption"], t["title"])


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
        caption=("악보에서 빌려 온 네 개의 표시를 모든 도식에서 같은 뜻으로 씁니다. 무게를 "
                 "지는 것은 음표 머리입니다. 무엇을 나타내든 크기가 같아서, 오선 위의 어떤 "
                 "것도 다른 것보다 슬그머니 높아질 수 없습니다. 그림 때문에 정한 규칙이 "
                 "아니라 단체 때문에 정한 규칙입니다."),
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


# ---------------------------------------------------------------------------
# 11. The chronicle — four years on four staves, one note-head per activity
# ---------------------------------------------------------------------------

import ledger as _ledger

CHRON = {
    "en": dict(
        title="Every session and performance, 2023 to date",
        caption=("One stave a year, one note-head an activity, placed on the day it happened. "
                 "Filled heads are Learning — a lecture, an outing, a class; open heads are "
                 "Sharing — a concert in somebody else&rsquo;s room. A tie under the stave is a "
                 "course that met weekly. Two heads stacked on one day are a chord: two things "
                 "happened. Hover a head for the name. The table below is the same record in words."),
        aria=("Four staves, one for each year from 2023 to 2026, with months across the top. "
              "Note-heads are placed on the day of each activity: filled for learning, open for "
              "sharing. Ties under the staves mark weekly courses. The density rises year by year."),
        legend=[("learning — a lecture, an outing, a class", False),
                ("sharing — a concert in someone&rsquo;s room", True)],
        tie="a course, weekly",
    ),
    "ko": dict(
        title="2023년부터 지금까지, 모든 회차와 연주",
        caption=("한 해에 오선 하나, 활동 하나에 음표 하나를 그날 자리에 놓았습니다. 채운 "
                 "음표는 배움 — 강의, 동행, 수업 — 이고, 빈 음표는 나눔 — 누군가의 방에서 "
                 "연 음악회 — 입니다. 오선 아래 붙임줄은 매주 모인 과정입니다. 같은 날 두 "
                 "음표가 겹쳐 있으면 화음입니다. 그날 두 가지가 있었다는 뜻입니다. 음표에 "
                 "마우스를 올리면 이름이 보입니다. 아래 표는 같은 기록을 글로 적은 것입니다."),
        aria=("2023년부터 2026년까지 해마다 오선 하나, 위쪽에 열두 달. 활동이 있던 날에 음표를 "
              "놓았고, 배움은 채운 음표, 나눔은 빈 음표다. 오선 아래 붙임줄은 주간 과정을 뜻한다. "
              "해가 갈수록 음표가 촘촘해진다."),
        legend=[("배움 — 강의, 동행, 수업", False),
                ("나눔 — 누군가의 방에서 연 음악회", True)],
        tie="매주 모인 과정",
    ),
}

CH_X0, CH_W = 92, 964          # the twelve months run across this width
CH_MONTH = CH_W / 12
CH_TOP, CH_STEP, CH_GAP = 72, 124, 12   # first stave, pitch between years, line gap
CH_STACK = 20                            # a stacked head sits a space above the last


def _ch_x(m, d):
    """x for a date; a row with no day sits at the middle of its month."""
    return CH_X0 + ((m - 1) + ((d - 1) / 31 if d else 0.5)) * CH_MONTH


def chronicle(lang):
    t = CHRON[lang]
    p = []
    years = sorted(_ledger.by_year())

    # month rule along the top, once
    for i, mon in enumerate(_ledger.MONTH[lang]):
        x = CH_X0 + (i + 0.5) * CH_MONTH
        p.append(f'    <text class="dg-sub" x="{x:.1f}" y="46" text-anchor="middle">{mon}</text>')

    for yi, year in enumerate(years):
        y0 = CH_TOP + yi * CH_STEP
        mid = y0 + 2 * CH_GAP                       # the middle line carries the notes
        p += stave(CH_X0, CH_W, y0, gap=CH_GAP)
        p.append(f'    <text class="dg-h" x="24" y="{mid + 7}">{year}</text>')

        # Heads that would touch stack upward instead, a space apart, so a
        # busy fortnight reads as a chord rather than as a smear. Placed
        # heads are remembered as (x, level).
        placed = []
        for r in _ledger.by_year()[year]:
            _, m, d, kind, en_t, ko_t, en_v, ko_v, note_ = r
            title = en_t if lang == "en" else ko_t
            venue = en_v if lang == "en" else ko_v
            x = _ch_x(m, d)
            lift = 0
            while any(lv == lift and abs(px - x) < 2 * NOTE_RX + 3 for px, lv in placed):
                lift += 1
            placed.append((x, lift))
            cy = mid - lift * CH_STACK
            open_ = kind not in _ledger.LEARN
            label = f"{_ledger.when(r, lang)} &middot; {title} &middot; {venue}"
            p.append(f'    <g class="dg-ev"><title>{label}</title>'
                     + note(round(x, 1), cy, open_=open_).strip() + '</g>')
            if "until" in note_ and kind == "course":
                m2, d2 = note_["until"]
                x2 = _ch_x(m2, d2)
                yb = y0 + 4 * CH_GAP + 12
                p.append(f'    <path class="dg-stroke-accent" d="M{x:.1f} {yb} '
                         f'Q {(x + x2) / 2:.1f} {yb + 16} {x2:.1f} {yb}" '
                         f'fill="none" stroke-width="1.75"/>')

    # legend
    ly = CH_TOP + len(years) * CH_STEP + 8
    lx = CH_X0
    for text, open_ in t["legend"]:
        p.append(note(lx + 11, ly - 4, open_=open_))
        p.append(f'    <text class="dg-sub" x="{lx + 32}" y="{ly}">{text}</text>')
        lx += 400 if lang == "en" else 300
    p.append(f'    <path class="dg-stroke-accent" d="M{lx} {ly - 8} Q {lx + 22} {ly + 8} {lx + 44} {ly - 8}" '
             f'fill="none" stroke-width="1.75"/>')
    p.append(f'    <text class="dg-sub" x="{lx + 56}" y="{ly}">{t["tie"]}</text>')

    return figure(f"0 0 1080 {ly + 30}", t["aria"], "\n".join(p), t["caption"], t["title"])


# ---------------------------------------------------------------------------
# 12. Lecture attendance — fifteen sessions, the stave as the axis
# ---------------------------------------------------------------------------

ATT = {
    "en": dict(
        title="Who came to the lecture-recitals, session by session",
        caption=("Six people came to the first session in January 2024; fourteen came to the "
                 "eleventh. The stave is the axis: each line is four people. The fifteenth "
                 "session, drawn open, was not a lecture but a concert at the National Concert "
                 "Hall attended together, and six came. Sessions sixteen and seventeen were held "
                 "in 2026 but their attendance was not recorded, so they are not drawn."),
        aria=("A column chart drawn as note-heads on stems over a stave. Fifteen sessions from "
              "January 2024 to December 2025; attendance rises from six to fourteen, dips to six "
              "at the fifteenth, which was a concert outing."),
        venues=[(1, 1, "Dublin 18"), (2, 6, "Dolphin&rsquo;s Barn"), (7, 14, "TU Dublin &middot; once at the Carmelite centre"),
                (15, 15, "NCH")],
        axis="people",
        session="session",
    ),
    "ko": dict(
        title="강의·연주에 온 사람, 회차별로",
        caption=("2024년 1월 첫 회차에 여섯 명이 왔고, 열한 번째 회차에는 열네 명이 왔습니다. "
                 "오선이 눈금입니다. 한 줄이 네 사람입니다. 빈 음표로 그린 열다섯 번째 회차는 "
                 "강의 대신 국립 콘서트홀에 함께 간 날이고, 여섯 명이 왔습니다. 2026년의 "
                 "열여섯·열일곱 번째 회차는 참석 인원이 기록되지 않아 그리지 않았습니다."),
        aria=("오선 위에 기둥 달린 음표로 그린 막대 그래프. 2024년 1월부터 2025년 12월까지 "
              "열다섯 회차, 참석이 6명에서 14명으로 늘고, 동행 관람이었던 열다섯 번째에서 6명으로 "
              "내려간다."),
        venues=[(1, 1, "더블린 18"), (2, 6, "돌핀스 반"), (7, 14, "TU 더블린 · 한 번은 가르멜 센터"),
                (15, 15, "NCH")],
        axis="명",
        session="회차",
    ),
}

ATT_X0, ATT_STEP = 132, 64
ATT_BASE, ATT_UNIT = 262, 7        # y of zero, px per person (a stave line = 4 people)


def attendance(lang):
    t = ATT[lang]
    rows = [r for r in _ledger.ROWS if r[3] == "lecture" and "att" in r[8]]
    p = []
    p += stave(ATT_X0 - 40, len(rows) * ATT_STEP + 40, ATT_BASE - 16 * ATT_UNIT, gap=4 * ATT_UNIT)
    for k in (0, 4, 8, 12, 16):
        y = ATT_BASE - k * ATT_UNIT
        p.append(f'    <text class="dg-sub" x="{ATT_X0 - 52}" y="{y + 4}" text-anchor="end">{k}</text>')
    p.append(f'    <text class="dg-sub" x="{ATT_X0 - 52}" y="{ATT_BASE - 16 * ATT_UNIT - 18}" '
             f'text-anchor="end">{t["axis"]}</text>')

    for i, r in enumerate(rows):
        x = ATT_X0 + i * ATT_STEP
        v = r[8]["att"]
        y = ATT_BASE - v * ATT_UNIT
        outing = "outing" in (r[8].get("flag", ("", ""))[0])
        p.append(f'    <line class="dg-stroke-accent" x1="{x}" y1="{ATT_BASE}" x2="{x}" y2="{y + 6}" '
                 f'stroke-width="2"/>')
        p.append(note(x, y, open_=outing))
        p.append(f'    <text class="dg-num" x="{x}" y="{y - 16}" text-anchor="middle">{v}</text>')
        p.append(f'    <text class="dg-sub" x="{x}" y="{ATT_BASE + 24}" text-anchor="middle">{i + 1}</text>')
    p.append(f'    <text class="dg-sub" x="{ATT_X0 - 52}" y="{ATT_BASE + 24}" '
             f'text-anchor="end">{t["session"]}</text>')

    # where each run of sessions was held
    for a, b, name in t["venues"]:
        x1 = ATT_X0 + (a - 1) * ATT_STEP - 20
        x2 = ATT_X0 + (b - 1) * ATT_STEP + 20
        p.append(bracket(x1, x2, ATT_BASE + 44, depth=8, below=True))
        p.append(f'    <text class="dg-sub" x="{(x1 + x2) / 2}" y="{ATT_BASE + 72}" '
                 f'text-anchor="middle">{name}</text>')

    return figure("0 0 1080 350", t["aria"], "\n".join(p), t["caption"], t["title"])


# ---------------------------------------------------------------------------
# 13. The road ahead — what is on the record, and what is only planned
# ---------------------------------------------------------------------------

ROAD = {
    "en": dict(
        title="Where this is going",
        caption=("The four filled heads are on the record. The four open ones are not: they are "
                 "the next steps, in the order we intend to take them, and they stay under a "
                 "dashed bracket until each one is done. Nothing here has a date it does not "
                 "have yet."),
        aria=("Eight note-heads rising left to right on a stave. The first four, filled and under "
              "a solid bracket, are done: founded 2024, pilot completed 2026, first public "
              "commission 2026, first community course 2026. The next four, open and under a dashed "
              "bracket, are planned: a company with directors, a second cohort and new counties, "
              "the first educator employed, wellbeing measured and reported."),
        done=[("Jan 2024", ["Founded", "in Dublin"]),
              ("Apr 2026", ["Pilot completed", "seven of seven"]),
              ("Aug 2026", ["First public", "commission"]),
              ("Sep 2026", ["First community", "course opens"])],
        next=[("Next", ["Incorporated,", "with directors"]),
              ("Then", ["A second cohort,", "new counties"]),
              ("Then", ["The first educator", "properly employed"]),
              ("Then", ["Wellbeing measured", "and reported here"])],
        on_record="on the record", planned="planned, not yet done",
        axis_a="one clarinet", axis_b="a community that plays",
    ),
    "ko": dict(
        title="이 일이 가려는 곳",
        caption=("채운 음표 넷은 기록에 있는 일입니다. 빈 음표 넷은 아직 없는 일입니다. 다음 "
                 "걸음을 밟으려는 순서대로 놓았고, 하나씩 마칠 때까지 점선 괄호 아래 둡니다. "
                 "아직 정해지지 않은 날짜는 여기 적지 않았습니다."),
        aria=("오선 위로 왼쪽에서 오른쪽으로 올라가는 음표 여덟 개. 앞의 넷은 채워져 있고 실선 "
              "괄호 아래 있다 — 2024년 창립, 2026년 파일럿 완료, 2026년 첫 공적 위촉, 2026년 첫 "
              "커뮤니티 과정. 뒤의 넷은 비어 있고 점선 괄호 아래 있다 — 이사가 있는 법인, 두 번째 "
              "기수와 새 카운티, 첫 교육가 고용, 측정하고 보고하는 웰빙."),
        done=[("2024년 1월", ["더블린에서", "창립"]),
              ("2026년 4월", ["파일럿 완료", "7명 중 7명"]),
              ("2026년 8월", ["첫 공적", "위촉"]),
              ("2026년 9월", ["첫 커뮤니티", "과정 개강"])],
        next=[("다음", ["이사진을 갖춘", "비영리 법인"]),
              ("그다음", ["두 번째 기수와", "위클로·미스·라우스"]),
              ("그다음", ["첫 음악 교육가를", "정식으로 고용"]),
              ("그다음", ["웰빙을 재어", "이 자리에 보고"])],
        on_record="기록에 있는 일", planned="계획, 아직 안 한 일",
        axis_a="클라리넷 하나", axis_b="연주하는 공동체",
    ),
}

ROAD_X = [96, 226, 356, 486, 616, 746, 876, 1006]
ROAD_Y = [232, 214, 196, 178, 160, 142, 124, 106]


def roadmap(lang):
    t = ROAD[lang]
    p = []
    p += stave(40, 1000, 106, gap=22, n=7)
    steps = [(w, l, False) for w, l in t["done"]] + [(w, l, True) for w, l in t["next"]]

    # the line of the road, threaded through the heads
    d = f"M{ROAD_X[0]} {ROAD_Y[0]}"
    for (x0, y0), (x1, y1) in zip(zip(ROAD_X, ROAD_Y), zip(ROAD_X[1:], ROAD_Y[1:])):
        d += f" C {x0 + 60} {y0}, {x1 - 60} {y1}, {x1} {y1}"
    p.append(draw(d, width=2.25))

    for (when, what, open_), x, y in zip(steps, ROAD_X, ROAD_Y):
        p.append(note(x, y, open_=open_))
        p.append(f'    <line class="dg-stroke" x1="{x}" y1="{y + 11}" x2="{x}" y2="268"/>')
        p.append(f'    <text class="dg-edge" x="{x}" y="292" text-anchor="middle">{when}</text>')
        p += lines(x, 314, what, cls="dg-sub", step=18, anchor="middle")

    p.append(bracket(ROAD_X[0] - 30, ROAD_X[3] + 30, 62, depth=10))
    p.append(f'    <text class="dg-sub" x="{(ROAD_X[0] + ROAD_X[3]) / 2}" y="44" '
             f'text-anchor="middle">{t["on_record"]}</text>')
    p.append(bracket(ROAD_X[4] - 30, ROAD_X[7] + 30, 62, depth=10, dashed=True))
    p.append(f'    <text class="dg-sub" x="{(ROAD_X[4] + ROAD_X[7]) / 2}" y="44" '
             f'text-anchor="middle">{t["planned"]}</text>')

    # the crescendo, as in the term figure: the one mark that means "grows"
    p.append('    <path class="dg-note" opacity=".28" d="M40 366 L1040 352 L1040 384 L40 370 Z"/>')
    p.append(f'    <text class="dg-sub" x="40" y="402">{t["axis_a"]}</text>')
    p.append(f'    <text class="dg-sub" x="1040" y="402" text-anchor="end">{t["axis_b"]}</text>')

    return figure("0 0 1080 414", t["aria"], "\n".join(p), t["caption"], t["title"])


# ---------------------------------------------------------------------------
# 14. Partnership — three ways in, and what every one of them comes with
# ---------------------------------------------------------------------------

PARTNER = {
    "en": dict(
        title="Three ways to partner, one set of promises",
        caption=("Whichever route an organisation takes, the right-hand panel is the same: a "
                 "named person to write to, a dated account of what the money did, and an open "
                 "invitation to come and see it. The three on the left are not tiers. They are "
                 "the three shapes support usually arrives in."),
        aria=("Three panels of equal size — fund a season, fund a place, bring your people — run "
              "to a single gold rule, and one arrow leaves it for a panel listing what every "
              "partnership comes with: a named contact, a dated report and an open invitation."),
        rows=[(["Fund a season"], ["a set number of concerts, in named settings"]),
              (["Fund a place"], ["free places for people cost would otherwise exclude"]),
              (["Bring your people"], ["staff volunteering, a workplace talk, seats at a concert"])],
        hub="Every partnership comes with",
        hub_rows=["a named contact", "a dated report of what it did", "an open invitation to attend"],
        edge="whichever fits",
    ),
    "ko": dict(
        title="파트너가 되는 세 가지 길, 약속은 하나",
        caption=("어느 길로 오시든 오른쪽 판은 같습니다. 편지를 보낼 담당자의 이름, 그 돈이 "
                 "무엇을 했는지 날짜를 적은 보고, 그리고 직접 와서 보시라는 초대. 왼쪽의 셋은 "
                 "등급이 아닙니다. 후원이 대개 찾아오는 세 가지 모양입니다."),
        aria=("같은 크기의 판 셋 — 시즌 후원, 자리 후원, 사람을 데려오기 — 이 금색 세로선 하나에서 "
              "만나고, 거기서 화살표 하나가 모든 파트너십에 따라오는 것을 적은 판으로 간다: 담당자 "
              "이름, 날짜 있는 보고, 언제든 오라는 초대."),
        rows=[(["시즌을 후원합니다"], ["정해진 횟수의 음악회를, 이름을 밝힌 곳에서"]),
              (["자리를 후원합니다"], ["비용 때문에 못 올 사람의 무료 자리를"]),
              (["사람을 데려옵니다"], ["직원 자원봉사, 직장 강연, 음악회 좌석"])],
        hub="모든 파트너십에 따라오는 것",
        hub_rows=["담당자 한 사람의 이름", "그 돈이 한 일을 날짜와 함께 보고", "언제든 와서 보시라는 초대"],
        edge="맞는 쪽으로",
    ),
}

PT_X, PT_W, PT_H = 24, 400, 76
PT_Y = [40, 140, 240]
PT_COLLECT = 496
PT_HUB = (620, 436)


def partnership(lang):
    t = PARTNER[lang]
    x, w, h = PT_X, PT_W, PT_H
    cx, (hx, hw) = PT_COLLECT, PT_HUB
    mids = [y + h / 2 for y in PT_Y]
    hy = (mids[0] + mids[-1]) / 2
    p = []

    for (head, sub), y, my in zip(t["rows"], PT_Y, mids):
        p.append(f'    <rect class="dg-fill-soft" x="{x}" y="{y}" width="{w}" height="{h}" rx="12"/>')
        p.append(note(x + 34, my - 4))
        p += lines(x + 64, my, head, cls="dg-h")
        p += lines(x + 64, my + 25, sub, cls="dg-sub", step=18)
        p.append(f'    <line class="dg-stroke" x1="{x + w}" y1="{my}" x2="{cx}" y2="{my}"/>')

    p.append(f'    <line class="dg-stroke-accent" x1="{cx}" y1="{mids[0]}" x2="{cx}" y2="{mids[-1]}" '
             f'stroke-width="2.5"/>')
    p.append(draw(f"M{cx} {hy} H{hx - 34}", width=2.5))
    p.append(tri(hx - 22, hy))
    p.append(f'    <text class="dg-edge dg-late" x="{(cx + hx - 34) / 2}" y="{hy - 16}" '
             f'text-anchor="middle">{t["edge"]}</text>')

    p.append(f'    <rect class="dg-fill-accent dg-box" x="{hx}" y="{hy - 78}" width="{hw}" '
             f'height="156" rx="12" stroke-width="1.6"/>')
    p.append(f'    <text class="dg-h" x="{hx + 32}" y="{hy - 40}">{t["hub"]}</text>')
    for i, row in enumerate(t["hub_rows"]):
        yy = hy - 8 + i * 28
        p.append(note(hx + 42, yy - 4, open_=True))
        p.append(f'    <text class="dg-label" x="{hx + 64}" y="{yy + 1}">{row}</text>')

    return figure("0 0 1080 356", t["aria"], "\n".join(p), t["caption"], t["title"])
