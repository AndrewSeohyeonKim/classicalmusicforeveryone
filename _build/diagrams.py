# -*- coding: utf-8 -*-
"""The diagrams — fourteen figures, one small vocabulary.

Rewritten 2026-09-07. The earlier set drew every figure as a musical stave
with note-heads; Andrew's verdict was that it read as clutter, not music.
This set uses four plain marks instead, and most figures are HTML, not SVG,
so their text wraps, scales with the reader's font size and reflows on a
phone without a scrolling canvas:

    the panel      a rounded box with a hairline — one thing, named
    the dot        filled = on the record / Learning; open = planned / Sharing
    the connector  a thin gold line with a small head — what feeds what
    the wedge      a gold gradient that widens — the one mark meaning "grows"

A panel drawn with a dashed edge is a claim, not a count. Only two figures
are SVG — the chronicle and the attendance chart — because those plot data.

Every function takes a language code and returns a `<figure class="diagram">`.
Labels are pre-wrapped per language, so the English and Korean pages draw the
same figure.
"""

import ledger as _ledger


# ---------------------------------------------------------------------------
# Shared pieces
# ---------------------------------------------------------------------------

def figure(aria, body, caption, title=None, cls=""):
    head = f'  <p class="diagram-title">{title}</p>\n' if title else ""
    return (f'<figure class="diagram {cls}" role="group" aria-label="{aria}">\n'
            f'{head}{body}\n  <figcaption>{caption}</figcaption>\n</figure>')


def _li(rows):
    return "".join(f"<li>{r}</li>" for r in rows)


def step(title, rows=(), *, n=None, kicker=None, edge=None, claim=False, key=False,
         open_=False, sub=None):
    """One panel in a .flow: number, kicker, title, lines. `edge` labels the
    connector that leaves it. `claim` draws it dashed; `key` draws it gold."""
    cls = "fs" + (" is-claim" if claim else "") + (" is-key" if key else "")
    parts = [f'<div class="{cls}">']
    if n is not None:
        parts.append(f'<span class="fs-n">{n:02d}</span>')
    if kicker:
        parts.append(f'<span class="fs-k">{kicker}</span>')
    parts.append(f'<b class="fs-t"><i class="dot{" dot-open" if open_ else ""}"></i>{title}</b>')
    if sub:
        parts.append(f'<span class="fs-s">{sub}</span>')
    if rows:
        parts.append(f'<ul class="fs-l">{_li(rows)}</ul>')
    parts.append("</div>")
    if edge:
        # the connector is its own grid track (.fs-join), so the gap grows to
        # fit the label instead of the label spilling onto the next panel
        parts.append(f'<div class="fs-join"><i class="fs-edge">{edge}</i></div>')
    return "".join(parts)


def _tracks(cols):
    """panel, join, panel, join … panel — the join tracks are `auto` so a
    labelled connector widens to its label; an unlabelled one stays 44px."""
    return " auto ".join(["minmax(0,1fr)"] * cols)


def flow(steps, cols, foot=None):
    """A row of panels with a connector between each pair. `foot` is an
    optional row of bracketed labels underneath, each (text, span, claim);
    they live in the same grid so they line up with the panels above."""
    cells = []
    for i, st in enumerate(steps):
        cells.append(st)
        if i < len(steps) - 1 and 'class="fs-join"' not in st:
            cells.append('<div class="fs-join"></div>')
    if foot:
        col = 1
        for text, span, claim in foot:
            start, end = 2 * col - 1, 2 * (col + span) - 2
            cells.append(f'<span class="ff{" is-claim" if claim else ""}" '
                         f'style="--gc:{start} / {end}">{text}</span>')
            col += span
    return (f'  <div class="flow" style="--flow-tracks:{_tracks(cols)}">\n    '
            + "\n    ".join(cells) + "\n  </div>")


def item(title, sub=None, open_=False):
    """One panel in a .cv (converge) list."""
    s = f'<span class="cv-s">{sub}</span>' if sub else ""
    return f'<div class="cv-item"><i class="dot{" dot-open" if open_ else ""}"></i><b>{title}</b>{s}</div>'


def wedge(a, b):
    return (f'  <div class="wedge"><i></i><span class="wedge-a">{a}</span>'
            f'<span class="wedge-b">{b}</span></div>')


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
        aria=("Two panels of equal width. Learning lists three programmes; Sharing lists two. "
              "An arc from Learning to Sharing is labelled 'a player, ready for the room'; a "
              "mirrored arc back is labelled 'could I do that?'."),
        pillar_a="Learning", pillar_a_sub="we teach people to play",
        pillar_b="Sharing", pillar_b_sub="we bring the music to the room",
        top="a player, ready for the room",
        bottom="&ldquo;could I do that?&rdquo;",
        progs=[("Free Recorder Ensemble course", "a term, weekly"),
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
        aria=("같은 너비의 패널 둘. ‘배움’에는 세 프로그램, ‘나눔’에는 두 프로그램. 배움에서 "
              "나눔으로 가는 곡선은 ‘그 방에 설 준비가 된 연주자’, 돌아오는 곡선은 ‘나도 해 볼 수 "
              "있을까?’."),
        pillar_a="배움", pillar_a_sub="악기를 직접 잡도록 가르칩니다",
        pillar_b="나눔", pillar_b_sub="그 방으로 음악을 들고 갑니다",
        top="그 방에 설 준비가 된 연주자",
        bottom="&ldquo;나도 해 볼 수 있을까?&rdquo;",
        progs=[("무료 리코더 앙상블 과정", "한 학기 · 주 1회"),
               ("클래식 음악과 친해지기", "대략 월 1회"),
               ("함께하는 음악여행", "소그룹 동행"),
               ("찾아가는 음악회", "요양시설 · 본당"),
               ("Letters Ensemble", "주 1회 정기연습")],
    ),
}


def programme_map(lang):
    t = MAP[lang]

    def panel(head, sub, rows, open_):
        lis = "".join(
            f'<li><i class="dot{" dot-open" if open_ else ""}"></i><span>{n}</span><em>{m}</em></li>'
            for n, m in rows)
        return (f'<div class="loop-panel"><b class="fs-t">{head}</b>'
                f'<span class="fs-s">{sub}</span><ul>{lis}</ul></div>')

    body = (f'  <div class="loop">\n'
            f'    <div class="loop-arc loop-top"><span>{t["top"]}</span></div>\n'
            f'    {panel(t["pillar_a"], t["pillar_a_sub"], t["progs"][:3], False)}\n'
            f'    {panel(t["pillar_b"], t["pillar_b_sub"], t["progs"][3:], True)}\n'
            f'    <div class="loop-arc loop-bottom"><span>{t["bottom"]}</span></div>\n'
            f'  </div>')
    return figure(t["aria"], body, t["caption"], t["title"])


def loop(lang):
    return programme_map(lang)


# ---------------------------------------------------------------------------
# 2. Theory of change
# ---------------------------------------------------------------------------

TOC = {
    "en": dict(
        title="From what goes in to what changes",
        caption=("Read left to right. The first three panels are what we count and can show "
                 "you; the dashed fourth is what participants and hosts tell us, which we have "
                 "not yet measured. We would rather mark the join than blur it."),
        aria=("Four stages left to right: inputs buy activities, activities produce outputs, "
              "outputs point to change. The first three are marked counted and recorded; the "
              "fourth, drawn dashed, is reported but not yet measured."),
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
        caption=("왼쪽에서 오른쪽으로 읽습니다. 앞의 세 칸은 저희가 세어서 보여 드릴 수 있는 "
                 "것이고, 점선으로 그린 넷째 칸은 참가자와 공간이 해 준 말입니다. 아직 재 보지 "
                 "않았습니다. 그 경계는 흐리지 않고 그어 둡니다."),
        aria=("왼쪽에서 오른쪽으로 네 단계 — 투입이 활동을 사고, 활동이 산출을 만들고, 산출이 "
              "변화를 가리킨다. 앞의 셋은 ‘세어서 기록함’, 점선의 넷째는 ‘증언에 근거, 아직 측정 "
              "안 됨’."),
        cols=[("투입", ["교육가와 연주자", "리코더와 악보", "주 1회 쓸 방", "보조금과 참가비"]),
              ("활동", ["한 학기 수업", "함께 연주하기", "그 방에서의 음악회", "공연에 함께 가기"]),
              ("산출", ["진행한 세션", "수료한 사람", "닿은 공간", "치른 음악회"]),
              ("변화", ["줄어든 고립", "존엄과 성취", "세대를 잇는 관계", "교육가의 일자리"])],
        edges=["산다", "만든다", "가리킨다"],
        evidenced="세어서 기록함",
        claimed="증언에 근거 · 아직 측정 안 됨",
    ),
}


def theory_of_change(lang):
    t = TOC[lang]
    steps = []
    for i, (title, rows) in enumerate(t["cols"]):
        steps.append(step(title, rows, n=i + 1,
                          edge=t["edges"][i] if i < 3 else None, claim=(i == 3)))
    body = flow(steps, 4, foot=[(t["evidenced"], 3, False), (t["claimed"], 1, True)])
    return figure(t["aria"], body, t["caption"], t["title"])


# ---------------------------------------------------------------------------
# 3. A term — four steps and a crescendo underneath
# ---------------------------------------------------------------------------

TERM = {
    "en": dict(
        title="How one course is built",
        caption=("A course is designed so the first satisfying sound arrives in week one, not "
                 "in week six. Nothing assumes prior music reading, every step is reached by "
                 "the whole group together, and it ends the only way it can end — in front of "
                 "people."),
        aria=("Four steps across a term: first notes in week one, reading music in weeks two "
              "to five, playing your own part in weeks six to eleven, and a concert in the "
              "final week. A widening wedge underneath marks the growth from no experience to "
              "playing in public."),
        steps=[("Week 1", "Play your first notes", "Hold it, breathe, play."),
               ("Weeks 2–5", "Read music from zero", "Small steps, every week."),
               ("Weeks 6–11", "Play your own part", "The moment it clicks."),
               ("Final week", "Perform a concert", "For family and friends.")],
        axis_a="no experience assumed",
        axis_b="playing in public",
    ),
    "ko": dict(
        title="한 과정은 이렇게 만듭니다",
        caption=("만족스러운 첫 소리가 6주차가 아니라 1주차에 나오도록 짜여 있습니다. "
                 "악보를 읽을 줄 안다고 전제하지 않고, 모든 단계를 그룹 전체가 함께 넘습니다. "
                 "끝나는 방식은 하나뿐입니다. 사람들 앞에서."),
        aria=("한 학기의 네 단계 — 1주차 첫 소리, 2–5주차 악보 읽기, 6–11주차 자기 파트 연주, "
              "마지막 주 음악회. 아래의 넓어지는 쐐기는 경험 없음에서 사람들 앞에서 연주하기까지의 "
              "성장을 나타낸다."),
        steps=[("1주차", "첫 소리를 냅니다", "잡고, 숨을 넣고, 붑니다."),
               ("2–5주차", "악보를 처음부터", "매주 조금씩."),
               ("6–11주차", "내 파트를 맡습니다", "맞아떨어지는 순간."),
               ("마지막 주", "음악회를 엽니다", "가족과 친구 앞에서.")],
        axis_a="경험이 없어도 됩니다",
        axis_b="사람들 앞에서 연주합니다",
    ),
}


def term(lang):
    t = TERM[lang]
    steps = [step(what, kicker=when, sub=note) for when, what, note in t["steps"]]
    body = flow(steps, 4) + "\n" + wedge(t["axis_a"], t["axis_b"])
    return figure(t["aria"], body, t["caption"], t["title"])


# ---------------------------------------------------------------------------
# 4. Cross-subsidy — money in, money out
# ---------------------------------------------------------------------------

SUBSIDY = {
    "en": dict(
        title="How a paid booking keeps a free seat free",
        caption=("Money enters from three directions and leaves as places nobody paid for. "
                 "Remove the paid side and the free side does not shrink gracefully — it is "
                 "the first thing that goes. Any surplus goes back in."),
        aria=("Institutions, contributing participants, and grants pay into Classical Music for "
              "Everyone. It pays out free places and more rooms, and any surplus loops back in."),
        in_title="Money in", out_title="What it buys",
        in_rows=[("Institutions", "care homes, parishes, councils and schools — from their own budget"),
                 ("Participants who can", "a small termly contribution"),
                 ("Grants and gifts", "commissions, donations, rooms given in kind")],
        hub="Classical Music for Everyone",
        hub_note="volunteer-led · no private profit",
        out_rows=[("Free places", "older people, people with disabilities, anyone for whom cost decides"),
                  ("More rooms", "surplus goes back into sessions, venues and lower fees")],
        edge_in="pays a rate", edge_out="funds", loop="surplus reinvested",
    ),
    "ko": dict(
        title="유료 예약 하나가 무료 자리를 지키는 방식",
        caption=("돈은 세 방향에서 들어와, 아무도 값을 치르지 않은 자리로 나갑니다. 유료 쪽을 "
                 "걷어내면 무료 쪽이 가장 먼저 사라집니다. 남는 돈은 다시 안으로 돌아옵니다."),
        aria=("기관과 낼 수 있는 참가자, 보조금이 Classical Music for Everyone에 지불하고, 그 돈이 "
              "무료 자리와 더 많은 방으로 나가며, 잉여는 다시 안으로 돌아온다."),
        in_title="들어오는 돈", out_title="그 돈이 사는 것",
        in_rows=[("기관", "요양시설 · 본당 · 지자체 · 학교 — 자체 예산에서"),
                 ("낼 수 있는 참가자", "학기당 소액 기여"),
                 ("보조금과 후원", "위촉, 기부, 현물로 내어 주는 공간")],
        hub="Classical Music for Everyone",
        hub_note="자원봉사 운영 · 사적 이익 배분 없음",
        out_rows=[("무료 자리", "어르신, 장애가 있는 분, 비용이 참여를 가르는 모든 사람"),
                  ("더 많은 방", "잉여는 세션 · 공간 · 더 낮은 수강료로")],
        edge_in="비용을 지불", edge_out="자리를 만듦", loop="잉여 재투자",
    ),
}


def subsidy(lang):
    t = SUBSIDY[lang]
    ins = "".join(item(a, b) for a, b in t["in_rows"])
    outs = "".join(item(a, b, open_=True) for a, b in t["out_rows"])
    body = (f'  <div class="cv cv-through">\n'
            f'    <div class="cv-in"><b class="cv-gt">{t["in_title"]}</b>{ins}</div>\n'
            f'    <div class="cv-join"><i class="cv-edge">{t["edge_in"]}</i></div>\n'
            f'    <div class="cv-hub"><b class="fs-t brandname">{t["hub"]}</b>'
            f'<span class="fs-s">{t["hub_note"]}</span></div>\n'
            f'    <div class="cv-join cv-join-out"><i class="cv-edge">{t["edge_out"]}</i></div>\n'
            f'    <div class="cv-out"><b class="cv-gt">{t["out_title"]}</b>{outs}</div>\n'
            f'    <div class="cv-loop"><span>&#8634; {t["loop"]}</span></div>\n'
            f'  </div>')
    return figure(t["aria"], body, t["caption"], t["title"])


# ---------------------------------------------------------------------------
# 5. The lecture series — what changes in the listener
# ---------------------------------------------------------------------------

ARC = {
    "en": dict(
        title="What the three stages actually move",
        caption=("The three stages are not three difficulty levels. They move ownership: "
                 "the music starts as somebody else&rsquo;s, becomes something shared in the "
                 "room, and ends up yours. Each session also stands on its own, so nobody "
                 "arrives having missed the beginning."),
        aria=("An entry point marked 'no prior knowledge' leads to three stages: Getting Closer, "
              "Experiencing Together and Discovering My Taste, with connectors labelled 'listen "
              "without being tested' and 'say what you heard'. A note says every session stands "
              "alone."),
        entry="No prior knowledge", start="Start",
        steps=[("Getting Closer", "the music is somebody else&rsquo;s"),
               ("Experiencing Together", "the music is the room&rsquo;s"),
               ("Discovering My Taste", "the music is yours")],
        edges=["listen without being tested", "say what you heard"],
        loopback="Every session stands alone — start at any one.",
    ),
    "ko": dict(
        title="세 단계가 실제로 옮기는 것",
        caption=("세 단계가 옮기는 것은 난이도가 아니라 소유입니다. 음악은 처음에 남의 "
                 "것이었다가, 그 방이 함께 가진 것이 되고, 끝에는 내 것이 됩니다. 각 회차는 "
                 "그 자체로 완결돼 있어서, 늦게 온 사람이 앞부분을 놓친 채 앉아 있을 일이 "
                 "없습니다."),
        aria=("‘사전 지식 없이’라는 입구에서 세 단계로 이어진다 — 친해지기, 함께 경험하기, 내 취향 "
              "찾기. 연결선에는 ‘평가받지 않고 듣기’와 ‘들은 것을 말해 보기’. 각 회차는 그 자체로 "
              "완결된다는 메모."),
        entry="사전 지식 없이", start="출발",
        steps=[("친해지기", "음악은 아직 남의 것입니다"),
               ("함께 경험하기", "음악은 이 방이 함께 가진 것입니다"),
               ("내 취향 찾기", "음악은 이제 내 것입니다")],
        edges=["평가받지 않고 듣기", "들은 것을 말해 보기"],
        loopback="각 회차는 그 자체로 완결됩니다. 아무 회차나 첫 회차입니다.",
    ),
}


def lecture_arc(lang):
    t = ARC[lang]
    steps = [step(t["entry"], open_=True, kicker=t["start"])]
    for i, (head, sub) in enumerate(t["steps"]):
        steps.append(step(head, sub=sub, n=i + 1, edge=t["edges"][i] if i < 2 else None))
    body = flow(steps, 4) + f'\n  <p class="flow-note">{t["loopback"]}</p>'
    return figure(t["aria"], body, t["caption"], t["title"])


# ---------------------------------------------------------------------------
# 6. An accompanied outing — the concert is only the middle third
# ---------------------------------------------------------------------------

OUTING = {
    "en": dict(
        title="Why an outing is three parts, not one",
        caption=("The ticket is rarely what stops someone. Not knowing what happens when you "
                 "get there, and having nobody to go with, is. So the concert sits in the "
                 "middle: the two parts either side are the ones that make it possible."),
        aria=("Three panels in a row: before, during and after an outing. The middle one, the "
              "concert itself, is highlighted; the two either side are marked as the parts that "
              "make the middle possible."),
        parts=[("Before", "what the piece is, what the room will do"),
               ("During", "we sit together; questions at the interval"),
               ("After", "say what you heard — there is no wrong answer")],
        mid_note="the concert itself",
        side_note="what makes the middle possible",
        edges=["prepare", "sit together"],
    ),
    "ko": dict(
        title="한 번의 동행이 왜 세 부분인가",
        caption=("발목을 잡는 것은 대개 티켓 값이 아닙니다. 가서 뭘 어떻게 해야 하는지 "
                 "모른다는 것, 같이 갈 사람이 없다는 것입니다. 그래서 음악회를 가운데 "
                 "두었습니다. 양옆의 두 부분이 가운데를 가능하게 합니다."),
        aria=("나란한 패널 셋 — 가기 전, 가서, 다녀와서. 가운데 ‘음악회 그 자체’가 강조돼 있고, "
              "양옆은 가운데를 가능하게 하는 부분으로 표시돼 있다."),
        parts=[("가기 전", "어떤 곡인지, 그 자리에서 무슨 일이 있는지"),
               ("가서", "옆자리에 함께 앉고, 쉬는 시간에 궁금한 것을"),
               ("다녀와서", "들은 것을 말해 봅니다. 틀린 답은 없습니다")],
        mid_note="음악회 그 자체",
        side_note="가운데를 가능하게 하는 부분",
        edges=["준비하고", "함께 앉고"],
    ),
}


def outing(lang):
    t = OUTING[lang]
    steps = [step(h, sub=s, key=(i == 1), edge=t["edges"][i] if i < 2 else None)
             for i, (h, s) in enumerate(t["parts"])]
    body = flow(steps, 3, foot=[(t["side_note"], 1, False), (t["mid_note"], 1, False),
                                (t["side_note"], 1, False)])
    return figure(t["aria"], body, t["caption"], t["title"])


# ---------------------------------------------------------------------------
# 7. An outreach visit — what has to be true for a concert to happen in a room
# ---------------------------------------------------------------------------

VISIT = {
    "en": dict(
        title="What a room has to provide",
        caption=("Everything in the first group arrives in a car. Everything in the second is "
                 "already in the building. That is the whole arrangement, and it is why a day "
                 "room with no piano, no stage and no budget can still host a concert."),
        aria=("Two groups of panels converge on one panel marked 'the concert'. The first, 'we "
              "carry in', lists players, instruments, stands, the programme and insurance. The "
              "second, 'already in the building', lists the room, the people and one named contact."),
        in_title="We carry in",
        in_rows=["players and instruments", "stands, scores, programme",
                 "a programme built for the room", "insurance and paperwork"],
        room_title="Already in the building",
        room_rows=["a room, any room", "the people who live or work there", "one named contact"],
        hub="The concert",
        hub_note="30–60 minutes · no stage, no piano, nothing for the audience to pay",
    ),
    "ko": dict(
        title="그 방이 준비해야 하는 것",
        caption=("첫 묶음은 전부 차에 실려 옵니다. 둘째 묶음은 이미 그 건물 안에 있습니다. "
                 "준비물은 그게 전부입니다. 그래서 피아노도 무대도 예산도 없는 휴게실이 "
                 "음악회를 열 수 있습니다."),
        aria=("두 묶음의 패널이 ‘음악회’ 패널 하나로 모인다. ‘우리가 싣고 가는 것’은 연주자·악기·"
              "보면대·프로그램·보험, ‘이미 그 건물에 있는 것’은 방과 사람과 담당자 한 사람."),
        in_title="우리가 싣고 가는 것",
        in_rows=["연주자와 악기", "보면대 · 악보 · 프로그램", "그 방에 맞춰 짠 곡목", "보험과 서류"],
        room_title="이미 그 건물에 있는 것",
        room_rows=["방 하나, 어떤 방이든", "거기 살거나 일하는 사람들", "담당자 한 사람"],
        hub="음악회",
        hub_note="30–60분 · 무대도 피아노도 없이, 관객이 낼 돈도 없이",
    ),
}


def visit(lang):
    t = VISIT[lang]
    g1 = "".join(item(r) for r in t["in_rows"])
    g2 = "".join(item(r, open_=True) for r in t["room_rows"])
    body = (f'  <div class="cv">\n'
            f'    <div class="cv-in">'
            f'<div class="cv-group"><b class="cv-gt">{t["in_title"]}</b>{g1}</div>'
            f'<div class="cv-group"><b class="cv-gt">{t["room_title"]}</b>{g2}</div></div>\n'
            f'    <div class="cv-join"></div>\n'
            f'    <div class="cv-hub is-key"><b class="fs-t">{t["hub"]}</b>'
            f'<span class="fs-s">{t["hub_note"]}</span></div>\n'
            f'  </div>')
    return figure(t["aria"], body, t["caption"], t["title"])


# ---------------------------------------------------------------------------
# 8. Letters Ensemble — what four concerts are resting on
# ---------------------------------------------------------------------------

REHEARSE = {
    "en": dict(
        title="What four concerts are resting on",
        caption=("Four concerts are the part of this that got written down. Underneath them is "
                 "weekly rehearsal since January 2024 — well over a hundred afternoons, none of "
                 "which we recorded. We are counting them from now on, because the rehearsal is "
                 "the programme and the concert is the receipt."),
        aria=("Two panels compared: over one hundred Saturday rehearsals since January 2024, none "
              "recorded, shown as a field of small dots; and four formal concerts, documented, "
              "shown as four large dots."),
        many="100+", many_t="Saturday rehearsals since January 2024",
        many_sub="none of them recorded",
        edge="what gets written down",
        few="4", few_t="formal concerts",
        few_sub="programmes, photographs, dates",
        foot="amateur musicians living in Dublin · about two hours · open to new players",
    ),
    "ko": dict(
        title="네 번의 음악회가 딛고 선 것",
        caption=("네 번의 음악회는 기록으로 남은 부분입니다. 그 아래에 2024년 1월부터의 주간 "
                 "연습이 있습니다. 백 번이 훨씬 넘는 토요일이고, 그중 어느 것도 기록해 두지 "
                 "않았습니다. 이제부터는 셉니다. 연습이 프로그램이고 음악회는 영수증입니다."),
        aria=("두 패널의 비교 — 2024년 1월부터 백 회가 넘는 토요일 연습(기록 없음)을 작은 점의 "
              "무리로, 정식 음악회 네 번(기록됨)을 큰 점 넷으로."),
        many="100+", many_t="2024년 1월부터의 토요일 연습",
        many_sub="기록해 둔 것은 없습니다",
        edge="기록으로 남는 것",
        few="4", few_t="정식 음악회",
        few_sub="프로그램 · 사진 · 날짜",
        foot="더블린에 사는 아마추어 연주자들 · 약 2시간 · 새 연주자를 환영합니다",
    ),
}


def rehearsals(lang):
    t = REHEARSE[lang]
    body = (f'  <div class="cmp">\n'
            f'    <div class="cmp-side"><b class="cmp-num">{t["many"]}</b>'
            f'<span class="cmp-t">{t["many_t"]}</span><div class="dots-many" aria-hidden="true"></div>'
            f'<span class="cmp-s">{t["many_sub"]}</span></div>\n'
            f'    <div class="cmp-join"><i class="cv-edge">{t["edge"]}</i></div>\n'
            f'    <div class="cmp-side is-key"><b class="cmp-num">{t["few"]}</b>'
            f'<span class="cmp-t">{t["few_t"]}</span>'
            f'<div class="dots-few" aria-hidden="true"><i></i><i></i><i></i><i></i></div>'
            f'<span class="cmp-s">{t["few_sub"]}</span></div>\n'
            f'  </div>\n  <p class="flow-note">{t["foot"]}</p>')
    return figure(t["aria"], body, t["caption"], t["title"])


# ---------------------------------------------------------------------------
# 9. Four ways in — one door
# ---------------------------------------------------------------------------

WAYS = {
    "en": dict(
        title="Four ways in, one door",
        caption=("The four routes are not four application processes. They are four sentences "
                 "you might write in the same email, and people move between them all the time "
                 "— most of the players started as listeners, and two of the rooms we play in "
                 "were offered by someone who came to a concert."),
        aria=("Four panels — learn to play, come and listen, play with us, host or partner — "
              "converge on one panel marked 'one email, one line'."),
        rows=[("Learn to play", "you have never played anything"),
              ("Come and listen", "you would rather start by listening"),
              ("Play with us", "you already play something"),
              ("Host or partner", "you have a room, or you know one")],
        hub="One email, one line",
        hub_note="we answer with the practical details",
        move="people move between these",
        edge="whichever fits",
    ),
    "ko": dict(
        title="네 가지 길, 하나의 문",
        caption=("네 갈래는 네 개의 신청 절차가 아닙니다. 같은 이메일에 쓸 수 있는 네 개의 "
                 "문장이고, 사람들은 그 사이를 늘 오갑니다. 지금 연주하는 사람 대부분이 "
                 "처음에는 듣는 사람이었고, 저희가 연주하는 방 중 둘은 음악회에 왔던 분이 "
                 "내어 준 것입니다."),
        aria=("패널 넷 — 배우러 오기, 들으러 오기, 함께 연주하기, 공간 열기 — 이 ‘이메일 한 통, "
              "한 줄’ 패널 하나로 모인다."),
        rows=[("배우러 옵니다", "악기를 잡아 본 적이 없어도"),
              ("들으러 옵니다", "듣는 것부터 시작하고 싶다면"),
              ("함께 연주합니다", "이미 다루는 악기가 있다면"),
              ("공간을 엽니다", "방이 있거나, 아는 방이 있다면")],
        hub="이메일 한 통, 한 줄",
        hub_note="실무적인 내용으로 답을 드립니다",
        move="사람들은 이 사이를 오갑니다",
        edge="당신에게 맞는 쪽으로",
    ),
}


def pathways(lang):
    t = WAYS[lang]
    ins = "".join(item(a, b) for a, b in t["rows"])
    body = (f'  <div class="cv">\n'
            f'    <div class="cv-in cv-linked">{ins}<span class="cv-move">{t["move"]}</span></div>\n'
            f'    <div class="cv-join"><i class="cv-edge">{t["edge"]}</i></div>\n'
            f'    <div class="cv-hub is-key"><b class="fs-t">{t["hub"]}</b>'
            f'<span class="fs-s">{t["hub_note"]}</span></div>\n'
            f'  </div>')
    return figure(t["aria"], body, t["caption"], t["title"])


# ---------------------------------------------------------------------------
# 10. The legend — the four marks, and what each one means
# ---------------------------------------------------------------------------

VOCAB = {
    "en": dict(
        title="How to read every diagram on this site",
        caption=("Four marks, used the same way in every figure. The dot is the load-bearing "
                 "one: every item gets the same dot, so nothing in a figure can be quietly "
                 "ranked above anything else. That is a decision about the organisation, not "
                 "about the drawing."),
        aria=("A key to four drawing marks: the panel, the dot, the connector and the wedge, each "
              "with the meaning it carries in the diagrams on this site."),
        items=[("The panel", "one thing, named. Dashed means a claim, not a count"),
               ("The dot", "filled: on the record, or Learning. Open: planned, or Sharing"),
               ("The connector", "what feeds what, with a word on it"),
               ("The wedge", "the only mark here that means &lsquo;this grows&rsquo;")],
    ),
    "ko": dict(
        title="이 사이트의 도식을 읽는 법",
        caption=("네 개의 표시를 모든 도식에서 같은 뜻으로 씁니다. 무게를 지는 것은 점입니다. "
                 "모든 항목에 같은 점이 붙어서, 어떤 것도 다른 것보다 슬그머니 높아질 수 "
                 "없습니다. 그림 때문에 정한 규칙이 아니라 단체 때문에 정한 규칙입니다."),
        aria=("네 가지 표시의 범례 — 패널, 점, 연결선, 쐐기. 각각이 이 사이트의 도식에서 갖는 뜻이 "
              "함께 적혀 있다."),
        items=[("패널", "하나의 것, 이름을 붙여서. 점선이면 셈이 아니라 주장"),
               ("점", "채움: 기록에 있음, 또는 배움. 빔: 계획, 또는 나눔"),
               ("연결선", "무엇이 무엇을 먹이는지, 한 낱말과 함께"),
               ("쐐기", "이 세트에서 ‘자란다’를 뜻하는 유일한 표시")],
    ),
}


def vocabulary(lang):
    t = VOCAB[lang]
    marks = ['<span class="lg-mark"><i class="lg-panel"></i><i class="lg-panel is-claim"></i></span>',
             '<span class="lg-mark"><i class="dot"></i><i class="dot dot-open"></i></span>',
             '<span class="lg-mark"><i class="lg-conn"></i></span>',
             '<span class="lg-mark"><i class="lg-wedge"></i></span>']
    cells = "".join(
        f'<div class="lg">{m}<b class="fs-t">{h}</b><span class="fs-s">{s}</span></div>'
        for m, (h, s) in zip(marks, t["items"]))
    return figure(t["aria"], f'  <div class="legend">{cells}</div>', t["caption"], t["title"])


# ---------------------------------------------------------------------------
# 11. The chronicle — four years, one row each, a dot per activity  (SVG)
# ---------------------------------------------------------------------------

CHRON = {
    "en": dict(
        title="Every session and performance, 2023 to date",
        caption=("One line a year, one dot an activity, placed on the day it happened. Filled "
                 "dots are Learning — a lecture, an outing, a class; open dots are Sharing — a "
                 "concert in somebody else&rsquo;s room. A gold bar under the line is a course "
                 "that met weekly. Dots stacked on one day mean two things happened. Hover a dot "
                 "for the name. The tables below are the same record in words."),
        aria=("Four timelines, one for each year from 2023 to 2026, with months across the top. "
              "Dots are placed on the day of each activity: filled for learning, open for "
              "sharing. Bars under the lines mark weekly courses. The density rises year by year."),
        legend=[("learning — a lecture, an outing, a class", False),
                ("sharing — a concert in someone&rsquo;s room", True)],
        tie="a course, weekly",
    ),
    "ko": dict(
        title="2023년부터 지금까지, 모든 회차와 연주",
        caption=("한 해에 선 하나, 활동 하나에 점 하나를 그날 자리에 놓았습니다. 채운 점은 "
                 "배움 — 강의, 동행, 수업 — 이고, 빈 점은 나눔 — 누군가의 방에서 연 음악회 — "
                 "입니다. 선 아래 금색 막대는 매주 모인 과정입니다. 같은 날 점이 겹쳐 있으면 "
                 "그날 두 가지가 있었다는 뜻입니다. 점에 마우스를 올리면 이름이 보입니다. "
                 "아래 표는 같은 기록을 글로 적은 것입니다."),
        aria=("2023년부터 2026년까지 해마다 선 하나, 위쪽에 열두 달. 활동이 있던 날에 점을 "
              "놓았고, 배움은 채운 점, 나눔은 빈 점이다. 선 아래 막대는 주간 과정. 해가 갈수록 "
              "점이 촘촘해진다."),
        legend=[("배움 — 강의, 동행, 수업", False),
                ("나눔 — 누군가의 방에서 연 음악회", True)],
        tie="매주 모인 과정",
    ),
}

CH_X0, CH_W = 96, 960
CH_MONTH = CH_W / 12
CH_TOP, CH_STEP = 74, 88     # first baseline, pitch between years
CH_R, CH_STACK = 6.5, 17     # dot radius, lift per stacked dot


def _ch_x(m, d):
    return CH_X0 + ((m - 1) + ((d - 1) / 31 if d else 0.5)) * CH_MONTH


def _dot(x, y, open_):
    k = "dg-dot-open" if open_ else "dg-dot"
    return f'<circle class="{k}" cx="{x:.1f}" cy="{y:.1f}" r="{CH_R}"/>'


def chronicle(lang):
    t = CHRON[lang]
    p = []
    years = sorted(_ledger.by_year())

    for i, mon in enumerate(_ledger.MONTH[lang]):
        x = CH_X0 + (i + 0.5) * CH_MONTH
        p.append(f'    <text class="dg-sub" x="{x:.1f}" y="40" text-anchor="middle">{mon}</text>')

    for yi, year in enumerate(years):
        y = CH_TOP + yi * CH_STEP
        p.append(f'    <line class="dg-line" x1="{CH_X0}" y1="{y}" x2="{CH_X0 + CH_W}" y2="{y}"/>')
        for i in range(13):
            x = CH_X0 + i * CH_MONTH
            p.append(f'    <line class="dg-line" x1="{x:.1f}" y1="{y - 3}" x2="{x:.1f}" y2="{y + 3}"/>')
        p.append(f'    <text class="dg-h" x="24" y="{y + 7}">{year}</text>')

        placed = []
        for r in _ledger.by_year()[year]:
            _, m, d, kind, en_t, ko_t, en_v, ko_v, note_ = r
            title = en_t if lang == "en" else ko_t
            venue = en_v if lang == "en" else ko_v
            x = _ch_x(m, d)
            lift = 0
            while any(lv == lift and abs(px - x) < 2 * CH_R + 2 for px, lv in placed):
                lift += 1
            placed.append((x, lift))
            cy = y - lift * CH_STACK
            open_ = kind not in _ledger.LEARN
            label = f"{_ledger.when(r, lang)} &middot; {title} &middot; {venue}"
            p.append(f'    <g class="dg-ev"><title>{label}</title>{_dot(x, cy, open_)}</g>')
            if "until" in note_ and kind == "course":
                m2, d2 = note_["until"]
                x2 = _ch_x(m2, d2)
                p.append(f'    <rect class="dg-span" x="{x:.1f}" y="{y + 12}" '
                         f'width="{x2 - x:.1f}" height="4" rx="2"/>')

    ly = CH_TOP + len(years) * CH_STEP - 10
    lx = CH_X0
    for text, open_ in t["legend"]:
        p.append("    " + _dot(lx + 7, ly - 4, open_))
        p.append(f'    <text class="dg-sub" x="{lx + 24}" y="{ly}">{text}</text>')
        lx += 400 if lang == "en" else 300
    p.append(f'    <rect class="dg-span" x="{lx}" y="{ly - 6}" width="36" height="4" rx="2"/>')
    p.append(f'    <text class="dg-sub" x="{lx + 48}" y="{ly}">{t["tie"]}</text>')

    svg = (f'  <div class="diagram-canvas">\n  <svg viewBox="0 0 1080 {ly + 24}" role="img" '
           f'aria-label="{t["aria"]}">\n' + "\n".join(p) + "\n  </svg>\n  </div>")
    return figure(t["aria"], svg, t["caption"], t["title"], cls="diagram-svg")


# ---------------------------------------------------------------------------
# 12. Lecture attendance — fifteen sessions  (SVG)
# ---------------------------------------------------------------------------

ATT = {
    "en": dict(
        title="Who came to the lecture-recitals, session by session",
        caption=("Six people came to the first session in January 2024; fourteen came to the "
                 "eleventh. The fifteenth, drawn open, was not a lecture but a concert at the "
                 "National Concert Hall attended together, and six came. Sessions sixteen and "
                 "seventeen were held in 2026 but their attendance was not recorded, so they "
                 "are not drawn."),
        aria=("A bar chart of fifteen sessions from January 2024 to December 2025; attendance "
              "rises from six to fourteen and dips to six at the fifteenth, a concert outing."),
        venues=[(1, 1, "Dublin 18"), (2, 6, "Dolphin&rsquo;s Barn"),
                (7, 14, "TU Dublin &middot; once at the Carmelite centre"), (15, 15, "NCH")],
        axis="people", session="session",
    ),
    "ko": dict(
        title="강의·연주에 온 사람, 회차별로",
        caption=("2024년 1월 첫 회차에 여섯 명이 왔고, 열한 번째 회차에는 열네 명이 왔습니다. "
                 "빈 막대로 그린 열다섯 번째 회차는 강의 대신 국립 콘서트홀에 함께 간 날이고, "
                 "여섯 명이 왔습니다. 2026년의 열여섯·열일곱 번째 회차는 참석 인원이 기록되지 "
                 "않아 그리지 않았습니다."),
        aria=("2024년 1월부터 2025년 12월까지 열다섯 회차의 막대 그래프. 참석이 6명에서 14명으로 "
              "늘고, 동행 관람이었던 열다섯 번째에서 6명으로 내려간다."),
        venues=[(1, 1, "더블린 18"), (2, 6, "돌핀스 반"),
                (7, 14, "TU 더블린 · 한 번은 가르멜 센터"), (15, 15, "NCH")],
        axis="명", session="회차",
    ),
}

ATT_X0, ATT_STEP, ATT_BW = 132, 64, 26
ATT_BASE, ATT_UNIT = 250, 10


def attendance(lang):
    t = ATT[lang]
    rows = [r for r in _ledger.ROWS if r[3] == "lecture" and "att" in r[8]]
    p = []
    x_end = ATT_X0 + (len(rows) - 1) * ATT_STEP + 40
    for k in (4, 8, 12, 16):
        y = ATT_BASE - k * ATT_UNIT
        p.append(f'    <line class="dg-line" x1="{ATT_X0 - 40}" y1="{y}" x2="{x_end}" y2="{y}"/>')
        p.append(f'    <text class="dg-sub" x="{ATT_X0 - 52}" y="{y + 4}" text-anchor="end">{k}</text>')
    p.append(f'    <line class="dg-base" x1="{ATT_X0 - 40}" y1="{ATT_BASE}" x2="{x_end}" y2="{ATT_BASE}"/>')
    p.append(f'    <text class="dg-sub" x="{ATT_X0 - 52}" y="{ATT_BASE - 16 * ATT_UNIT - 22}" '
             f'text-anchor="end">{t["axis"]}</text>')

    for i, r in enumerate(rows):
        x = ATT_X0 + i * ATT_STEP
        v = r[8]["att"]
        y = ATT_BASE - v * ATT_UNIT
        outing_ = "outing" in (r[8].get("flag", ("", ""))[0])
        cls = "dg-bar-open" if outing_ else "dg-bar"
        p.append(f'    <rect class="{cls}" x="{x - ATT_BW / 2}" y="{y}" width="{ATT_BW}" '
                 f'height="{ATT_BASE - y}" rx="4"/>')
        p.append(f'    <text class="dg-num" x="{x}" y="{y - 10}" text-anchor="middle">{v}</text>')
        p.append(f'    <text class="dg-sub" x="{x}" y="{ATT_BASE + 24}" text-anchor="middle">{i + 1}</text>')
    p.append(f'    <text class="dg-sub" x="{ATT_X0 - 52}" y="{ATT_BASE + 24}" '
             f'text-anchor="end">{t["session"]}</text>')

    for a, b, name in t["venues"]:
        x1 = ATT_X0 + (a - 1) * ATT_STEP - 22
        x2 = ATT_X0 + (b - 1) * ATT_STEP + 22
        p.append(f'    <line class="dg-base" x1="{x1}" y1="{ATT_BASE + 44}" x2="{x2}" y2="{ATT_BASE + 44}"/>')
        p.append(f'    <text class="dg-sub" x="{(x1 + x2) / 2}" y="{ATT_BASE + 66}" '
                 f'text-anchor="middle">{name}</text>')

    svg = (f'  <div class="diagram-canvas">\n  <svg viewBox="0 0 1080 340" role="img" '
           f'aria-label="{t["aria"]}">\n' + "\n".join(p) + "\n  </svg>\n  </div>")
    return figure(t["aria"], svg, t["caption"], t["title"], cls="diagram-svg")


# ---------------------------------------------------------------------------
# 13. The road ahead — on the record, and planned
# ---------------------------------------------------------------------------

ROAD = {
    "en": dict(
        title="Where this is going",
        caption=("The four filled steps are on the record. The four dashed ones are not: they "
                 "are the next steps, in the order we intend to take them, and they stay dashed "
                 "until each one is done. Nothing here has a date it does not have yet."),
        aria=("Two rows of four steps. The first row, on the record: founded 2024, pilot "
              "completed 2026, first public commission 2026, first community course 2026. The "
              "second row, dashed and planned: incorporated with directors, a second cohort and "
              "new counties, the first educator employed, wellbeing measured and reported."),
        done=[("Jan 2024", "Founded in Dublin"),
              ("Apr 2026", "Pilot completed, seven of seven"),
              ("Aug 2026", "First public commission"),
              ("Sep 2026", "First community course opens")],
        next=[("Next", "Incorporated, with directors"),
              ("Then", "A second cohort, and new counties"),
              ("Then", "The first educator properly employed"),
              ("Then", "Wellbeing measured, and reported here")],
        on_record="on the record", planned="planned, not yet done",
        axis_a="one clarinet", axis_b="a community that plays",
    ),
    "ko": dict(
        title="이 일이 가려는 곳",
        caption=("채운 네 칸은 기록에 있는 일입니다. 점선 네 칸은 아직 없는 일입니다. 다음 "
                 "걸음을 밟으려는 순서대로 놓았고, 하나씩 마칠 때까지 점선으로 둡니다. "
                 "아직 정해지지 않은 날짜는 여기 적지 않았습니다."),
        aria=("네 칸씩 두 줄. 첫 줄은 기록에 있는 일 — 2024년 창립, 2026년 파일럿 완료, 2026년 "
              "첫 공적 위촉, 2026년 첫 커뮤니티 과정. 둘째 줄은 점선의 계획 — 이사가 있는 법인, "
              "두 번째 기수와 새 카운티, 첫 교육가 고용, 측정하고 보고하는 웰빙."),
        done=[("2024년 1월", "더블린에서 창립"),
              ("2026년 4월", "파일럿 완료, 7명 중 7명"),
              ("2026년 8월", "첫 공적 위촉"),
              ("2026년 9월", "첫 커뮤니티 과정 개강")],
        next=[("다음", "이사진을 갖춘 비영리 법인"),
              ("그다음", "두 번째 기수와 새 카운티"),
              ("그다음", "첫 음악 교육가를 정식으로 고용"),
              ("그다음", "웰빙을 재어 이 자리에 보고")],
        on_record="기록에 있는 일", planned="계획, 아직 안 한 일",
        axis_a="클라리넷 하나", axis_b="연주하는 공동체",
    ),
}


def roadmap(lang):
    t = ROAD[lang]
    done = [step(w, kicker=k) for k, w in t["done"]]
    nxt = [step(w, kicker=k, claim=True, open_=True) for k, w in t["next"]]
    body = (f'  <p class="flow-group-t">{t["on_record"]}</p>\n' + flow(done, 4) +
            f'\n  <p class="flow-group-t is-claim">{t["planned"]}</p>\n' + flow(nxt, 4) +
            "\n" + wedge(t["axis_a"], t["axis_b"]))
    return figure(t["aria"], body, t["caption"], t["title"])


# ---------------------------------------------------------------------------
# 14. Partnership — three ways in, one set of promises
# ---------------------------------------------------------------------------

PARTNER = {
    "en": dict(
        title="Three ways to partner, one set of promises",
        caption=("Whichever route an organisation takes, the right-hand panel is the same: a "
                 "named person to write to, a dated account of what the money did, and an open "
                 "invitation to come and see it. The three on the left are not tiers. They are "
                 "the three shapes support usually arrives in."),
        aria=("Three panels — fund a season, fund a place, bring your people — converge on one "
              "panel listing what every partnership comes with: a named contact, a dated report "
              "and an open invitation."),
        rows=[("Fund a season", "a set number of concerts, in named settings"),
              ("Fund a place", "free places for people cost would otherwise exclude"),
              ("Bring your people", "staff volunteering, a workplace talk, seats at a concert")],
        hub="Every partnership comes with",
        hub_rows=["a named contact", "a dated report of what it did", "an open invitation to attend"],
        edge="whichever fits",
    ),
    "ko": dict(
        title="파트너가 되는 세 가지 길, 약속은 하나",
        caption=("어느 길로 오시든 오른쪽 판은 같습니다. 편지를 보낼 담당자의 이름, 그 돈이 "
                 "무엇을 했는지 날짜를 적은 보고, 그리고 직접 와서 보시라는 초대. 왼쪽의 셋은 "
                 "등급이 아닙니다. 후원이 대개 찾아오는 세 가지 모양입니다."),
        aria=("패널 셋 — 시즌 후원, 자리 후원, 사람을 데려오기 — 이 모든 파트너십에 따라오는 것을 "
              "적은 패널 하나로 모인다: 담당자 이름, 날짜 있는 보고, 언제든 오라는 초대."),
        rows=[("시즌을 후원합니다", "정해진 횟수의 음악회를, 이름을 밝힌 곳에서"),
              ("자리를 후원합니다", "비용 때문에 못 올 사람의 무료 자리를"),
              ("사람을 데려옵니다", "직원 자원봉사, 직장 강연, 음악회 좌석")],
        hub="모든 파트너십에 따라오는 것",
        hub_rows=["담당자 한 사람의 이름", "그 돈이 한 일을 날짜와 함께 보고", "언제든 와서 보시라는 초대"],
        edge="맞는 쪽으로",
    ),
}


def partnership(lang):
    t = PARTNER[lang]
    ins = "".join(item(a, b) for a, b in t["rows"])
    hub_rows = "".join(f'<li><i class="dot dot-open"></i>{r}</li>' for r in t["hub_rows"])
    body = (f'  <div class="cv">\n'
            f'    <div class="cv-in">{ins}</div>\n'
            f'    <div class="cv-join"><i class="cv-edge">{t["edge"]}</i></div>\n'
            f'    <div class="cv-hub is-key"><b class="fs-t">{t["hub"]}</b><ul class="fs-l">{hub_rows}</ul></div>\n'
            f'  </div>')
    return figure(t["aria"], body, t["caption"], t["title"])
