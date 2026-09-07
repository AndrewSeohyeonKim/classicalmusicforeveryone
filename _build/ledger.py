# -*- coding: utf-8 -*-
"""The activity ledger — every session and performance, 2023 to date.

One list, read by three things: the Archive page (the table), the chronicle
diagram (the note-heads), and the counts quoted on the Impact page. Facts
follow 03 — Track Record §3 and 08 — Programme Records; nothing is here that
is not in a canonical row. Rows the canonical set marks "to confirm" are
left out rather than guessed at.

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
            until (m, d) for a course that runs across months
"""

LEARN = ("lecture", "companion", "course")

ROWS = [
    # ---- 2023 ---------------------------------------------------------------
    (2023, 2, 11, "outreach",
     "Lourdes English Mass", "루르드 영어 미사",
     "Sanctuary of Our Lady of Lourdes, France", "루르드 성모 성지, 프랑스",
     dict(bmsp=True, flag=("clarinet solo · before the founding", "클라리넷 독주 · 창립 이전"))),
    (2023, 7, 0, "companion",
     "BBC Proms", "BBC 프롬스",
     "Royal Albert Hall, London", "로열 앨버트 홀, 런던",
     dict(flag=("attended · the first summer", "첫 번째 여름"))),

    # ---- 2024 ---------------------------------------------------------------
    (2024, 1, 28, "lecture",
     "Getting Closer", "친해지기",
     "4 Sandyford Hall Places, Dublin 18", "샌디포드, 더블린 18",
     dict(att=6, flag=("the first lecture-recital", "첫 강의·연주"))),
    (2024, 2, 25, "lecture",
     "Together (1)", "함께하기 (1)",
     "Our Lady of Dolours Church, Dolphin&rsquo;s Barn", "Our Lady of Dolours 성당",
     dict(att=6)),
    (2024, 3, 16, "ensemble",
     "St Patrick&rsquo;s Day Concert", "성 파트리치오 축일 음악회",
     "Dalgan Park, Co. Meath", "달간 파크, 미스 주",
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
     "Rathgar Parish Concert", "라스가 본당 음악회",
     "Church of the Three Patrons, Rathgar", "Three Patrons 성당, 라스가",
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
     "Palais Brongniart, Paris", "팔레 브로냐르, 파리",
     dict(flag=("clarinet solo", "클라리넷 독주"))),
    (2024, 11, 8, "lecture",
     "Getting Closer + Together (1)", "친해지기 + 함께하기 (1)",
     "TU Dublin, Grangegorman", "TU 더블린",
     dict(att=12, flag=("the series moves to TU Dublin", "강의가 TU 더블린으로"))),
    (2024, 11, 15, "lecture",
     "Getting Closer + Together (2)", "친해지기 + 함께하기 (2)",
     "TU Dublin", "TU 더블린",
     dict(att=12)),
    (2024, 11, 23, "ensemble",
     "St Columban&rsquo;s Day Concert", "성 골롬반 축일 음악회",
     "Missionary Sisters of St Columban, Co. Wicklow", "성 골롬반 선교 수녀회, 위클로 주",
     dict(bmsp=True, le=3, flag=("where the recorder ensemble began — a sister asked to play again",
                                 "리코더 앙상블이 시작된 자리 — 한 수녀가 다시 연주하고 싶다고 물었다"))),
    (2024, 12, 28, "outreach",
     "Christmas Concert", "성탄 축하 음악회",
     "Gwandukjeong Martyrs Memorial Centre, Daegu, Korea", "관덕정 순교기념관, 대구",
     dict(bmsp=True, flag=("clarinet and piano", "클라리넷과 피아노"))),

    # ---- 2025 ---------------------------------------------------------------
    (2025, 2, 21, "lecture",
     "Getting Closer + Together (1)", "친해지기 + 함께하기 (1)",
     "TU Dublin", "TU 더블린",
     dict(att=10)),
    (2025, 3, 7, "lecture",
     "Getting Closer + Together (2)", "친해지기 + 함께하기 (2)",
     "TU Dublin", "TU 더블린",
     dict(att=10)),
    (2025, 3, 16, "outreach",
     "St Patrick&rsquo;s Day Concert", "성 파트리치오 축일 음악회",
     "Dalgan Park, Co. Meath", "달간 파크, 미스 주",
     dict(bmsp=True, flag=("Korean traditional ensemble and clarinet", "국악 앙상블과 클라리넷"))),
    (2025, 4, 11, "lecture",
     "My Taste", "내 취향 찾기",
     "TU Dublin", "TU 더블린",
     dict(att=14, flag=("the largest attendance to date", "지금까지 가장 많은 참석"))),
    (2025, 4, 17, "outreach",
     "Goirtin Hub Concert", "고르틴 허브 음악회",
     "HSE EVE Goirtin Hub, Dublin 7", "HSE EVE 고르틴 허브, 더블린 7",
     dict(flag=("clarinet solo · a day service", "클라리넷 독주 · 주간 돌봄 서비스"))),
    (2025, 4, 17, "outreach",
     "Holy Thursday liturgy", "성목요일 전례",
     "Blessed Sacrament Chapel, Dublin 1", "성체 성당, 더블린 1",
     dict(bmsp=True, flag=("organ and clarinet", "오르간과 클라리넷"))),
    (2025, 4, 18, "outreach",
     "Good Friday liturgy", "성금요일 전례",
     "Dysart Parish, Co. Westmeath", "다이사트 본당, 웨스트미스 주",
     dict(bmsp=True, flag=("clarinet solo", "클라리넷 독주"))),
    (2025, 5, 27, "outreach",
     "School Mass", "학교 미사",
     "Kilmessan Church, Co. Meath", "킬메산 성당, 미스 주",
     dict(bmsp=True, flag=("organ and clarinet", "오르간과 클라리넷"))),
    (2025, 6, 4, "outreach",
     "Beautiful Farewell", "아름다운 작별",
     "Dalgan Park, Co. Meath", "달간 파크, 미스 주",
     dict(bmsp=True, flag=("a funeral and remembrance", "장례와 추모"))),
    (2025, 7, 21, "lecture",
     "BBC Proms", "BBC 프롬스",
     "Carmelite Community Centre, Dublin", "가르멜 커뮤니티 센터, 더블린",
     dict(att=13)),
    (2025, 7, 21, "outreach",
     "Music in place of the Legion of Mary", "레지오 마리애를 대신한 음악",
     "Morning Star Hostel, Dublin 7", "모닝 스타 쉼터, 더블린 7",
     dict(bmsp=True, flag=("organ and clarinet · a homeless hostel", "오르간과 클라리넷 · 노숙인 쉼터"))),
    (2025, 8, 0, "companion",
     "BBC Proms", "BBC 프롬스",
     "Royal Albert Hall, London", "로열 앨버트 홀, 런던",
     dict(flag=("the second summer · an itinerary of 24 concerts shared with participants",
                "두 번째 여름 · 24개 연주회 안내를 참가자와 공유"))),
    (2025, 9, 26, "lecture",
     "Getting Closer + Together (1)", "친해지기 + 함께하기 (1)",
     "TU Dublin", "TU 더블린",
     dict(att=11)),
    (2025, 9, 30, "companion",
     "NCH International Series — Chineke! Orchestra", "NCH 인터내셔널 시리즈 — 치네케! 오케스트라",
     "National Concert Hall, Dublin", "국립 콘서트홀, 더블린",
     dict(flag=("introduced to participants, group attendance organised", "참가자에게 안내, 단체 관람 준비"))),
    (2025, 10, 7, "companion",
     "NCH International Series — Stephen Hough and Viano Quartet",
     "NCH 인터내셔널 시리즈 — 스티븐 허프와 비아노 4중주단",
     "National Concert Hall, Dublin", "국립 콘서트홀, 더블린",
     dict(flag=("introduced to participants, group attendance organised", "참가자에게 안내, 단체 관람 준비"))),
    (2025, 10, 11, "companion",
     "TU Dublin Philharmonic", "TU 더블린 필하모닉",
     "TU Dublin Concert Hall", "TU 더블린 콘서트홀",
     dict(flag=("introduced to participants, group attendance organised", "참가자에게 안내, 단체 관람 준비"))),
    (2025, 10, 0, "course",
     "Ensemble for retired religious — preparation", "은퇴 수도자 앙상블 — 준비",
     "With the Presentation Sisters, Dublin", "프레젠테이션 수녀회와 함께, 더블린",
     dict(until=(12, 0), flag=("needs survey, permissions, vetting, individual lessons, part allocation",
                                "필요 조사, 허가, 신원조회, 개별 레슨, 파트 배정"))),
    (2025, 10, 17, "lecture",
     "Getting Closer + Together (2)", "친해지기 + 함께하기 (2)",
     "TU Dublin", "TU 더블린",
     dict(att=11)),
    (2025, 11, 20, "outreach",
     "Remembrance Mass", "위령 미사",
     "TU Dublin, Dublin 7", "TU 더블린",
     dict(bmsp=True, flag=("organ and clarinet", "오르간과 클라리넷"))),
    (2025, 11, 22, "outreach",
     "Remembrance Gathering", "추모 모임",
     "TU Dublin, Dublin 7", "TU 더블린",
     dict(flag=("clarinet, piano and harp", "클라리넷, 피아노, 하프"))),
    (2025, 11, 23, "outreach",
     "St Columban&rsquo;s Day Concert", "성 골롬반 축일 음악회",
     "Missionary Sisters of St Columban, Co. Wicklow", "성 골롬반 선교 수녀회, 위클로 주",
     dict(bmsp=True, flag=("clarinet solo", "클라리넷 독주"))),
    (2025, 11, 30, "outreach",
     "FMM House Concert", "FMM 하우스 콘서트",
     "Franciscan Missionaries of Mary, Dublin 5", "마리아의 프란치스코 선교 수녀회, 더블린 5",
     dict(bmsp=True, flag=("clarinet solo", "클라리넷 독주"))),
    (2025, 12, 5, "lecture",
     "Together (1) — a concert, attended together", "함께하기 (1) — 함께 간 연주회",
     "National Concert Hall, Dublin", "국립 콘서트홀, 더블린",
     dict(att=6, flag=("the fifteenth session was an outing, not a lecture",
                       "열다섯 번째 회차는 강의 대신 동행 관람"))),
    (2025, 12, 20, "ensemble",
     "Christmas Concert", "성탄 음악회",
     "Clondalkin Lodge, Dublin", "클론달킨 로지, 더블린",
     dict(bmsp=True, le=4, flag=("clarinet quartet and clarinet · residential care",
                                 "클라리넷 4중주와 클라리넷 · 요양 시설"))),

    # ---- 2026 ---------------------------------------------------------------
    (2026, 1, 15, "course",
     "Ensemble for retired religious — ten weekly rehearsals", "은퇴 수도자 앙상블 — 10주 연습",
     "Warrenmount, Dublin 8", "워렌마운트, 더블린 8",
     dict(until=(3, 17), att=7, flag=("Thursdays, one hour · seven retired Presentation Sisters · all seven completed",
                                      "목요일 1시간 · 프레젠테이션 수녀회 은퇴 수녀 7명 · 7명 전원 수료"))),
    (2026, 1, 23, "lecture",
     "My Taste", "내 취향 찾기",
     "Dublin", "더블린",
     dict(flag=("venue and attendance not recorded", "장소와 참석 인원은 기록되지 않음"))),
    (2026, 1, 0, "companion",
     "National Symphony Orchestra, RIAM piano series, RT&Eacute; Concert Orchestra",
     "국립 교향악단, RIAM 피아노 시리즈, RT&Eacute; 콘서트 오케스트라",
     "National Concert Hall and RIAM, Dublin", "국립 콘서트홀과 RIAM, 더블린",
     dict(until=(2, 0), flag=("four concerts introduced to participants, January–February",
                              "1–2월, 참가자에게 안내한 연주회 넷"))),
    (2026, 2, 0, "lecture",
     "My Taste (2)", "내 취향 찾기 (2)",
     "Dublin", "더블린",
     dict(flag=("date and venue to confirm", "날짜와 장소 확인 중"))),
    (2026, 4, 0, "concert",
     "Easter Concert — Presentation Sisters Recorder Ensemble", "부활 음악회 — 프레젠테이션 수녀회 리코더 앙상블",
     "Clondalkin Lodge, Dublin", "클론달킨 로지, 더블린",
     dict(bmsp=True, flag=("the ensemble&rsquo;s first public sharing · nine pieces",
                           "앙상블의 첫 공개 연주 · 아홉 곡"))),
    (2026, 4, 0, "course",
     "Ensemble for retired religious — continuation", "은퇴 수도자 앙상블 — 이어진 모임",
     "Warrenmount, Dublin 8", "워렌마운트, 더블린 8",
     dict(until=(8, 29), flag=("weekly until the community chose to conclude in August — a completed pilot",
                               "8월에 공동체가 마무리를 택할 때까지 매주 — 완료된 파일럿"))),
    (2026, 8, 20, "concert",
     "Shared Voices of Care", "Shared Voices of Care",
     "Tallaght University Hospital, Atrium", "탈라 대학병원 아트리움",
     dict(flag=("South Dublin Live 2026 · 30 minutes, acoustic, drop-in · guest haegeum artist Jaewon Kim",
                "South Dublin Live 2026 · 30분 · 어쿠스틱 · 해금 객원 김재원"))),
    (2026, 8, 29, "concert",
     "Shared Voices of Classical Tradition", "Shared Voices of Classical Tradition",
     "Rua Red Performance Space, Tallaght", "루아 레드 퍼포먼스 스페이스, 탈라",
     dict(flag=("South Dublin Live 2026 · clarinet, piano and soprano · free",
                "South Dublin Live 2026 · 클라리넷·피아노·소프라노 · 무료"))),
    (2026, 9, 9, "course",
     "Recorder Ensemble course — the first community class", "리코더 앙상블 과정 — 첫 커뮤니티 수업",
     "Mulhuddart Community Centre, Dublin 15", "멀허다트 커뮤니티 센터, 더블린 15",
     dict(until=(12, 0), flag=("twelve weeks, Wednesdays, free", "12주 · 수요일 · 무료"))),
    (2026, 9, 19, "outreach",
     "An Autumn Concert", "가을 음악회",
     "Methodist Centenary Church, Ranelagh, Dublin 6", "메소디스트 센테너리 교회, 라넬라, 더블린 6",
     dict(flag=("soprano, haegeum, clarinet and piano · scheduled", "소프라노·해금·클라리넷·피아노 · 예정"))),
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
    mon = MONTH[lang][m - 1]
    if "until" in note:
        m2, d2 = note["until"]
        mon2 = MONTH[lang][m2 - 1]
        if lang == "en":
            a = f"{d} {mon}" if d else mon
            b = f"{d2} {mon2}" if d2 else mon2
            return f"{a} &ndash; {b} {y}"
        a = f"{mon} {d}일" if d else mon
        b = f"{mon2} {d2}일" if d2 else mon2
        return f"{y}년 {a} &ndash; {b}"
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
    from the rows above. 2023–2025 outreach must come to twenty (03 §1)."""
    c = dict(lecture=0, outreach=0, ensemble=0, concert=0, companion=0, course=0)
    for r in ROWS:
        c[r[3]] += 1
    return c
