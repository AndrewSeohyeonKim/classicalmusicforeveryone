# -*- coding: utf-8 -*-
"""The activity ledger — every session and performance, 2023 to date. The
site counts from the founding, January 2024 (counted(), below); the two 2023
rows are kept as history.

One list, read by the chart on the News page (one square per talk or
performance) and the counts beside it. Facts follow 03 — Track Record §3 and
08 — Programme Records; nothing is here that is not in a canonical row. Where
the canonical set leaves a day or a venue "to confirm", the row keeps only
what is known (the month) and says so in its flag; nothing is guessed.

Each row:
    (year, month, day, kind, en_title, ko_title, en_venue, ko_venue, note)

    day     0 when only the month is known; a tuple (d1, d2) marks a span of
            days inside one month, and a span across months is given as
            ("span", m2, d2) in the note field of the first row
    kind    lecture · companion · outreach · ensemble · concert · course
            — lecture / companion / course are the Learning pillar and draw
            as filled note-heads; the other three are Sharing and draw open
    note    a dict: bmsp (faith strand), le (Letters Ensemble concert no.),
            att (attendance where recorded), flag (a short qualifier),
            until (m, d) for a course that runs across months,
            progs / not_in (slugs added to or taken out of a programme's
            record, see for_programme), pub (the qualifier printed on a
            programme page when flag is an internal note; None prints none)
"""

LEARN = ("lecture", "companion", "course")

ROWS = [
    # ---- 2023 ---------------------------------------------------------------
    (2023, 2, 11, "outreach",
     "Lourdes English Mass", "루르드 영어 미사",
     "Sanctuary of Our Lady of Lourdes, France", "루르드 성모 성지, 프랑스",
     dict(bmsp=True, pre=True, flag=("clarinet solo · before the founding", "클라리넷 독주 · 창립 이전"))),
    (2023, 7, 0, "companion",
     "BBC Proms", "BBC 프롬스",
     "Royal Albert Hall, London", "로열 앨버트 홀, 런던",
     dict(pre=True, not_in=("concert-companion",), flag=("attended · the first summer", "첫 번째 여름"))),

    # ---- 2024 ---------------------------------------------------------------
    (2024, 1, 28, "lecture",
     "Getting Closer", "친해지기",
     "Sandyford, Dublin 18", "더블린 18구 Sandyford",
     dict(att=6, flag=("the first talk", "첫 강의"))),
    (2024, 2, 25, "lecture",
     "Together (1)", "함께하기 (1)",
     "Our Lady of Dolours Church, Dolphin&rsquo;s Barn", "Our Lady of Dolours 성당",
     dict(att=6)),
    (2024, 3, 16, "ensemble",
     "St Patrick&rsquo;s Day Concert", "성 파트리치오 축일 음악회",
     "Dalgan Park, Co. Meath", "Dalgan Park, 미스 주",
     dict(bmsp=True, le=1, flag=("string quartet and clarinet · retired missionaries",
                                 "현악 4중주와 클라리넷 · 은퇴 선교사들"))),
    (2024, 3, 23, "lecture",
     "Together (2)", "함께하기 (2)",
     "Our Lady of Dolours Church", "Our Lady of Dolours 성당",
     dict(att=8)),
    (2024, 4, 14, "lecture",
     "My Taste (1)", "내 취향 찾기 (1)",
     "Our Lady of Dolours Church", "Our Lady of Dolours 성당",
     dict(att=7)),
    (2024, 4, 27, "lecture",
     "My Taste (2)", "내 취향 찾기 (2)",
     "Our Lady of Dolours Church", "Our Lady of Dolours 성당",
     dict(att=7)),
    (2024, 5, 5, "ensemble",
     "Rathgar Parish Concert", "Rathgar 본당 음악회",
     "Church of the Three Patrons, Rathgar", "Church of the Three Patrons, 더블린 Rathgar",
     dict(bmsp=True, le=2, flag=("string trio and organ", "현악 3중주와 오르간"))),
    (2024, 6, 22, "lecture",
     "Summer Festivals", "유럽의 여름 축제",
     "Our Lady of Dolours Church", "Our Lady of Dolours 성당",
     dict(att=10)),
    (2024, 8, 4, "outreach",
     "Concert in London", "런던 음악회",
     "London Korean Catholic Church, United Kingdom", "런던 한인 천주교회, 영국",
     dict(bmsp=True, flag=("clarinet and organ", "클라리넷과 오르간"))),
    (2024, 10, 27, "outreach",
     "Rendre Hommage &agrave; Leur Mission par la Musique", "선교의 노고에 음악으로 드리는 경의",
     "Missions &Eacute;trang&egrave;res de Paris, France", "파리 외방전교회, 프랑스",
     dict(bmsp=True, flag=("clarinet solo · retired missionaries", "클라리넷 독주 · 은퇴 선교사들"))),
    (2024, 10, 28, "outreach",
     "K-Expo Paris", "K-엑스포 파리",
     "Palais Brongniart, Paris", "Palais Brongniart, 파리",
     dict(flag=("clarinet solo", "클라리넷 독주"))),
    (2024, 11, 8, "lecture",
     "Getting Closer + Together (1)", "친해지기 + 함께하기 (1)",
     "TU Dublin, Grangegorman", "TU Dublin",
     dict(att=12, flag=("the series moves to TU Dublin", "강의가 TU 더블린으로"))),
    (2024, 11, 15, "lecture",
     "Getting Closer + Together (2)", "친해지기 + 함께하기 (2)",
     "TU Dublin", "TU Dublin",
     dict(att=12)),
    (2024, 11, 23, "ensemble",
     "St Columban&rsquo;s Day Concert", "성 골롬반 축일 음악회",
     "Missionary Sisters of St Columban, Co. Wicklow", "성 골롬반 외방선교 수녀회, 위클로 주",
     dict(bmsp=True, le=3, progs=("recorder-ensemble",),
          flag=("where the recorder ensemble began: a sister asked to play again",
                "리코더 앙상블이 시작된 자리. 한 수녀가 다시 연주하고 싶다고 물었다"),
          pub=("where the recorder ensemble began: a sister asked to play again",
               "리코더 앙상블이 시작된 자리 · 다시 연주하고 싶다는 수녀님의 질문"))),
    (2024, 12, 28, "outreach",
     "Christmas Concert", "성탄 축하 음악회",
     "Gwandukjeong Martyrs Memorial Centre, Daegu, Korea", "관덕정 순교기념관, 대구",
     dict(bmsp=True, flag=("clarinet and piano", "클라리넷과 피아노"))),

    # ---- 2025 ---------------------------------------------------------------
    (2025, 2, 21, "lecture",
     "Getting Closer + Together (1)", "친해지기 + 함께하기 (1)",
     "TU Dublin", "TU Dublin",
     dict(att=10)),
    (2025, 3, 7, "lecture",
     "Getting Closer + Together (2)", "친해지기 + 함께하기 (2)",
     "TU Dublin", "TU Dublin",
     dict(att=10)),
    (2025, 3, 16, "outreach",
     "St Patrick&rsquo;s Day Concert", "성 파트리치오 축일 음악회",
     "Dalgan Park, Co. Meath", "Dalgan Park, 미스 주",
     dict(bmsp=True, flag=("Korean traditional ensemble and clarinet", "국악 앙상블과 클라리넷"))),
    (2025, 4, 11, "lecture",
     "My Taste", "내 취향 찾기",
     "TU Dublin", "TU Dublin",
     dict(att=14, flag=("the largest attendance to date", "지금까지 가장 많은 참석"))),
    (2025, 4, 17, "outreach",
     "Goirtin Hub Concert", "Goirtin Hub 음악회",
     "HSE EVE Goirtin Hub, Dublin 7", "HSE EVE Goirtin Hub, 더블린 7구",
     dict(flag=("clarinet solo · a day service", "클라리넷 독주 · 주간 돌봄 서비스"))),
    (2025, 4, 17, "outreach",
     "Holy Thursday liturgy", "성목요일 전례",
     "Blessed Sacrament Chapel, Dublin 1", "Blessed Sacrament Chapel, 더블린 1구",
     dict(bmsp=True, flag=("organ and clarinet", "오르간과 클라리넷"))),
    (2025, 4, 18, "outreach",
     "Good Friday liturgy", "성금요일 전례",
     "Dysart Parish, Co. Westmeath", "Dysart 본당, 웨스트미스 주",
     dict(bmsp=True, flag=("clarinet solo", "클라리넷 독주"))),
    (2025, 5, 27, "outreach",
     "School Mass", "학교 미사",
     "Kilmessan Church, Co. Meath", "Kilmessan 성당, 미스 주",
     dict(bmsp=True, flag=("organ and clarinet", "오르간과 클라리넷"))),
    (2025, 6, 4, "outreach",
     "Beautiful Farewell", "아름다운 작별",
     "Dalgan Park, Co. Meath", "Dalgan Park, 미스 주",
     dict(bmsp=True, flag=("a funeral and remembrance", "장례와 추모"), pub=None)),
    (2025, 7, 21, "lecture",
     "BBC Proms", "BBC 프롬스",
     "Carmelite Community Centre, Dublin", "Carmelite Community Centre, 더블린",
     dict(att=13)),
    (2025, 7, 21, "outreach",
     "Music in place of the Legion of Mary", "레지오 마리애를 대신한 음악",
     "Morning Star Hostel, Dublin 7", "Morning Star Hostel, 더블린 7구",
     dict(bmsp=True, flag=("organ and clarinet · a homeless hostel", "오르간과 클라리넷 · 노숙인 쉼터"))),
    (2025, 8, 0, "companion",
     "BBC Proms", "BBC 프롬스",
     "Royal Albert Hall, London", "로열 앨버트 홀, 런던",
     dict(not_in=("concert-companion",),
          flag=("the second summer · an itinerary of 24 concerts shared with participants",
                "두 번째 여름 · 24개 연주회 안내를 참가자와 공유"))),
    (2025, 9, 26, "lecture",
     "Getting Closer + Together (1)", "친해지기 + 함께하기 (1)",
     "TU Dublin", "TU Dublin",
     dict(att=11)),
    (2025, 9, 30, "companion",
     "NCH International Series: Chineke! Orchestra", "NCH 인터내셔널 시리즈. 치네케! 오케스트라",
     "National Concert Hall, Dublin", "국립 콘서트홀, 더블린",
     dict(flag=("introduced to participants, group attendance organised", "참가자에게 안내, 단체 관람 준비"))),
    (2025, 10, 7, "companion",
     "NCH International Series: Stephen Hough and Viano Quartet",
     "NCH 인터내셔널 시리즈. 스티븐 허프와 비아노 4중주단",
     "National Concert Hall, Dublin", "국립 콘서트홀, 더블린",
     dict(flag=("introduced to participants, group attendance organised", "참가자에게 안내, 단체 관람 준비"))),
    (2025, 10, 11, "companion",
     "TU Dublin Philharmonic", "TU Dublin 필하모닉",
     "TU Dublin Concert Hall", "TU Dublin 콘서트홀",
     dict(flag=("introduced to participants, group attendance organised", "참가자에게 안내, 단체 관람 준비"))),
    (2025, 10, 0, "course",
     "Ensemble for retired religious: preparation", "은퇴 수도자 앙상블. 준비",
     "With the Presentation Sisters, Dublin", "Presentation 수녀회와 함께, 더블린",
     dict(until=(12, 0), flag=("needs survey, permissions, vetting, individual lessons, part allocation",
                                "필요 조사, 허가, 신원조회, 개별 레슨, 파트 배정"),
          pub=("a needs survey, individual lessons and parts for each player",
               "필요 조사, 개별 레슨, 한 사람마다 성부 배정"))),
    (2025, 10, 17, "lecture",
     "Getting Closer + Together (2)", "친해지기 + 함께하기 (2)",
     "TU Dublin", "TU Dublin",
     dict(att=11)),
    (2025, 11, 20, "outreach",
     "Remembrance Mass", "위령 미사",
     "TU Dublin, Dublin 7", "TU Dublin, 더블린 7구",
     dict(bmsp=True, flag=("organ and clarinet", "오르간과 클라리넷"))),
    (2025, 11, 22, "outreach",
     "Remembrance Gathering", "추모 모임",
     "TU Dublin, Dublin 7", "TU Dublin, 더블린 7구",
     dict(flag=("clarinet, piano and harp", "클라리넷, 피아노, 하프"))),
    (2025, 11, 23, "outreach",
     "St Columban&rsquo;s Day Concert", "성 골롬반 축일 음악회",
     "Missionary Sisters of St Columban, Co. Wicklow", "성 골롬반 외방선교 수녀회, 위클로 주",
     dict(bmsp=True, flag=("clarinet solo", "클라리넷 독주"))),
    (2025, 11, 30, "outreach",
     "FMM House Concert", "FMM 하우스 콘서트",
     "Franciscan Missionaries of Mary, Dublin 5", "마리아의 프란치스코 선교 수녀회, 더블린 5구",
     dict(bmsp=True, flag=("clarinet solo", "클라리넷 독주"))),
    (2025, 12, 5, "lecture",
     "Together (1): a concert, attended together", "함께하기 (1): 함께 간 연주회",
     "National Concert Hall, Dublin", "국립 콘서트홀, 더블린",
     dict(att=6, progs=("concert-companion",),
          flag=("the fifteenth session was an outing, not a lecture",
                "열다섯 번째 회차는 강의 대신 동행 관람"),
          pub=("the fifteenth session, at a concert", "열다섯 번째 모임, 공연장에서"))),
    (2025, 12, 20, "ensemble",
     "Christmas Concert", "성탄 음악회",
     "Clondalkin Lodge, Dublin", "Clondalkin Lodge, 더블린",
     dict(bmsp=True, le=4, flag=("clarinet quartet and clarinet · residential care",
                                 "클라리넷 4중주와 클라리넷 · 요양 시설"),
          pub=("clarinet and string trio · residential care", "클라리넷과 현악 3중주 · 요양 시설"))),

    # ---- 2026 ---------------------------------------------------------------
    (2026, 1, 15, "course",
     "Ensemble for retired religious: ten weekly rehearsals", "은퇴 수도자 앙상블. 10주 연습",
     "Warrenmount, Dublin 8", "Warrenmount, 더블린 8구",
     dict(until=(3, 17), att=7, flag=("Thursdays, one hour · seven retired Presentation Sisters · all seven completed",
                                      "목요일 1시간 · 프레젠테이션 수녀회 은퇴 수녀 7명 · 7명 전원 수료"),
          pub=("Thursdays, one hour · seven retired Presentation Sisters · all seven stayed to the end",
               "목요일 1시간 · 은퇴한 Presentation 수녀님 일곱 분 · 일곱 분 모두 끝까지"))),
    (2026, 1, 23, "lecture",
     "My Taste (1)", "내 취향 찾기 (1)",
     "East Quad, TU Dublin Grangegorman", "East Quad, TU Dublin Grangegorman",
     dict(flag=("more than five people · exact number not recorded", "다섯 명 넘게 · 정확한 인원은 기록되지 않음"),
          pub=("more than five people", "다섯 명 넘게"))),
    (2026, 1, 0, "companion",
     "National Symphony Orchestra, RIAM piano series, RT&Eacute; Concert Orchestra",
     "국립 교향악단, RIAM 피아노 시리즈, RT&Eacute; 콘서트 오케스트라",
     "National Concert Hall and RIAM, Dublin", "국립 콘서트홀과 RIAM, 더블린",
     dict(until=(2, 0), flag=("four concerts introduced to participants, January–February",
                              "1–2월, 참가자에게 안내한 연주회 넷"),
          pub=("concerts introduced to participants, group attendance organised",
               "참가자에게 안내, 단체 관람 준비"))),
    (2026, 2, 0, "lecture",
     "My Taste (2)", "내 취향 찾기 (2)",
     "East Quad, TU Dublin Grangegorman", "East Quad, TU Dublin Grangegorman",
     dict(flag=("day not recorded · more than five people", "날짜 미기록 · 다섯 명 넘게"),
          pub=("more than five people", "다섯 명 넘게"))),
    (2026, 4, 0, "concert",
     "Easter Concert: Presentation Sisters Recorder Ensemble", "부활 음악회: Presentation 수녀회 리코더 앙상블",
     "Clondalkin Lodge, Dublin", "Clondalkin Lodge, 더블린",
     dict(bmsp=True, progs=("recorder-ensemble",),
          flag=("the ensemble&rsquo;s first public sharing · nine pieces",
                "앙상블의 첫 공개 연주 · 아홉 곡"))),
    (2026, 4, 0, "course",
     "Ensemble for retired religious: continuation", "은퇴 수도자 앙상블. 이어진 모임",
     "Warrenmount, Dublin 8", "Warrenmount, 더블린 8구",
     dict(until=(8, 29), flag=("weekly until the community chose to conclude in August: a completed pilot",
                               "8월에 공동체가 마무리를 택할 때까지 매주. 완료된 파일럿"))),
    (2026, 8, 20, "concert",
     "Shared Voices of Care", "Shared Voices of Care",
     "Tallaght University Hospital", "Tallaght University Hospital",
     dict(progs=("outreach-concerts",),
          flag=("South Dublin Live 2026 · acoustic, drop-in · atrium and chapel · guest haegeum artist",
                "South Dublin Live 2026 · 어쿠스틱 · 아트리움과 경당 · 해금 객원"),
          pub=("our founder was selected for South Dublin Live 2026 · atrium and chapel · with a guest haegeum player",
               "창립자가 South Dublin Live 2026에 선정 · 아트리움과 경당 · 해금 객원"))),
    (2026, 8, 29, "concert",
     "Shared Voices of Classical Tradition", "Shared Voices of Classical Tradition",
     "Rua Red Performance Space, Tallaght", "Rua Red, 더블린 Tallaght",
     dict(progs=("outreach-concerts",),
          flag=("South Dublin Live 2026 · clarinet, piano and soprano",
                "South Dublin Live 2026 · 클라리넷·피아노·소프라노"),
          pub=("our founder was selected for South Dublin Live 2026 · clarinet, piano and soprano",
               "창립자가 South Dublin Live 2026에 선정 · 클라리넷·피아노·소프라노"))),
    (2026, 9, 0, "course",
     "Community Recorder Ensemble Class begins", "커뮤니티 리코더 앙상블 클래스 시작",
     "Mulhuddart Community Centre, Dublin 15", "Mulhuddart Community Centre, 더블린 15구",
     dict(season=("Autumn 2026", "2026년 가을"), flag=("Wednesday evenings", "매주 수요일 저녁"))),
    (2026, 9, 19, "outreach",
     "An Autumn Concert", "가을 음악회",
     "Methodist Centenary Church, Ranelagh, Dublin 6", "Methodist Centenary Church, 더블린 6구 Ranelagh",
     dict(flag=("soprano, haegeum, clarinet and piano", "소프라노·해금·클라리넷·피아노"))),
]

KIND = {
    "en": {"lecture": "Lecture-recital", "companion": "Concert Guide &amp; Companion",
           "outreach": "Outreach concert", "ensemble": "Letters Ensemble concert",
           "concert": "Concert", "course": "Course"},
    "ko": {"lecture": "강의·연주", "companion": "함께하는 음악여행",
           "outreach": "찾아가는 음악회", "ensemble": "Letters Ensemble 음악회",
           "concert": "음악회", "course": "과정"},
}

MONTH = {
    "en": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "ko": ["1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"],
}


def when(row, lang):
    """A short date string for a row, in either language."""
    y, m, d, *_ = row
    note = row[8]
    if "season" in note:
        # a row whose month is not published prints its season (the class's
        # start: facts.md gives "autumn 2026" and no date)
        return note["season"][0 if lang == "en" else 1]
    mon = MONTH[lang][m - 1]
    if "until" in note:
        m2, d2 = note["until"]
        mon2 = MONTH[lang][m2 - 1]
        if lang == "en":
            a = f"{d} {mon}" if d else mon
            b = f"{d2} {mon2}" if d2 else mon2
            return f"{a}&ndash;{b} {y}"
        a = f"{mon} {d}일" if d else mon
        b = f"{mon2} {d2}일" if d2 else mon2
        return f"{y}년 {a}&ndash;{b}"
    if lang == "en":
        return f"{d} {mon} {y}" if d else f"{mon} {y}"
    return f"{y}년 {mon} {d}일" if d else f"{y}년 {mon}"


def by_year():
    out = {}
    for r in ROWS:
        out.setdefault(r[0], []).append(r)
    return out


def counts():
    """The headline counts, derived rather than typed, so they cannot drift
    from the rows above. Counted rows only: from January 2024 to September
    2026 the outreach rows and the ensemble's four come to twenty (03 §1,
    request 05)."""
    c = dict(lecture=0, outreach=0, ensemble=0, concert=0, companion=0, course=0)
    for r in ROWS:
        c[r[3]] += 1
    return c


# ---------------------------------------------------------------------------
# A programme's own record, for its page (programmes/<slug>.html)
#
# By kind first: talks are Getting to Know; outreach rows and the Letters
# Ensemble's concerts are both outreach performances (the twenty of 03 §1
# include the ensemble's four), and the ensemble's concerts are also its own
# record; courses are the recorder class and the pilot before it; outings
# are Concert Guide & Companion. Then a row's note can add a programme
# (progs) or take one away (not_in). The South Dublin Live concerts, a
# selection of the founder (kit 25, 27), are on the Outreach Concerts record
# and say so in their own line (Andrew, 1 Oct 2026). A row marked scheduled,
# or from before the founding, is never shown.
# ---------------------------------------------------------------------------

BY_KIND = {
    "lecture": ("getting-to-know",),
    "outreach": ("outreach-concerts",),
    "ensemble": ("letters-ensemble", "outreach-concerts"),
    "course": ("recorder-ensemble",),
    "companion": ("concert-companion",),
    "concert": (),
}


def scheduled(row):
    return "scheduled" in (row[8].get("flag") or ("", ""))[0]


def counted(row):
    """On the public record: not still to come, and not from before the
    founding in January 2024 (pre). The two 2023 rows stay in the ledger as
    history; the site counts from 2024 (Andrew, 1 Oct 2026)."""
    return not scheduled(row) and not row[8].get("pre")


def for_programme(slug):
    """Every row on the record for one programme, in date order."""
    out = []
    for r in ROWS:
        note = r[8]
        progs = set(BY_KIND[r[3]]) | set(note.get("progs", ()))
        progs -= set(note.get("not_in", ()))
        if slug in progs and counted(r):
            out.append(r)
    return out


# Which programmes print a row's own title on their page. Talks have stage
# names (Getting Closer, Together, My Taste), the Letters Ensemble and the
# outings have concert names, the class has its stages. An outreach row is
# listed by its place and what was played: its title is often a liturgy or a
# private occasion, which is the host's to name, not ours.
TITLED = ("getting-to-know", "recorder-ensemble", "letters-ensemble", "concert-companion")


def qualifier(row, lang):
    """The short line printed under a row on a programme page."""
    note = row[8]
    i = 0 if lang == "en" else 1
    if "pub" in note:
        return note["pub"][i] if note["pub"] else ""
    return (note.get("flag") or ("", ""))[i]


def public_label(row, lang):
    """A row as one line for a tooltip or a list: the date, then the title and
    place, except an outreach row, which is its place and what was played
    (TITLED, above, says why)."""
    i = 0 if lang == "en" else 1
    title, venue = row[4 + i], row[6 + i]
    if row[3] == "outreach" or "outreach-concerts" in row[8].get("progs", ()):
        q = qualifier(row, lang)
        return f"{when(row, lang)} · {venue}" + (f" · {q}" if q else "")
    return f"{when(row, lang)} · {title} · {venue}"
