# -*- coding: utf-8 -*-
"""한국어 문안. 여섯 쪽의 마크업은 parts.py가 영문과 함께 그린다.

2026-10-01부터 이 파일은 문안만 갖는다. 영문 덱(content_en.py)과 같은 열쇠를
같은 순서로 채우므로 두 언어의 구조가 어긋날 수 없다. 영문의 번역이 아니라
같은 사실을 한국어로 쓴 것이다.

넣는 것과 넣지 않는 것(2026-10-01): 공개 사이트는 지금 하는 일, 지금 함께하는
방법, 믿을 수 있는 근거만 말한다. 아직 실행되지 않은 계획과 내부의 일은 넣지
않는다. 사실은 정본(00_최종본)과 통합 마스터 키트(11_CMFE_통합마스터)를 따른다.
"""

from urllib.parse import quote

import parts as P
from icons import icon as _ico
from layout import OPEN_GIVING

L = "ko"
EMAIL = "sby05034@gmail.com"

# 지위 문장(키트 27). 단체가 무엇인지 말하는 곳에서는 이 문장을 그대로 쓴다.
STATUS = ('<span class="brandname">Classical Music for Everyone</span>은 보증유한회사(CLG) 설립을 '
          "준비하고 있는 비영리 공동체 음악 단체입니다. 아직 등록된 자선단체는 아닙니다.")


def _mail(subject, body=""):
    href = f"mailto:{EMAIL}?subject={quote(subject)}"
    if body:
        href += "&amp;body=" + quote(body)
    return href


_MAIL_INVITE = _mail("음악회 초청 문의", "기관: \n장소: \n방과 가능한 날짜: \n")
_MAIL_BOARD = _mail("창립 이사회 문의",
                    "관심 있는 자리 (의장 / 재무 / 사무 / 세이프가딩·돌봄 / 지역사회): \n"
                    "저에 대해 몇 줄: \n")

# CMFE Artists 참여 신청 항목(키트 15). 서명 줄과 근로 자격 줄은 뺐다. 메일에는
# 서명이 필요 없고, 근로 자격은 연주를 맡길 때 확인한다(키트 06 I).
EOI_FIELDS = [
    "이름",
    "악기 또는 성악",
    "단계: 전문 연주자 / 학생 (학교, 학년) / 신진 / 아마추어 앙상블",
    "사는 곳 (카운티)",
    "보통 가능한 요일과 시간",
    "어르신 청중을 위한 45분 프로그램으로 연주할 수 있는 곡",
    "요양시설·병원·도서관·지역 공간에서 연주한 경험 (있다면)",
    "최근 연주 녹음·영상 링크 (YouTube, Vimeo, SoundCloud)",
    "Garda 신원조회: 있음 (어느 기관을 통해) / 필요함",
    "저희가 알아야 할 접근성 필요 (선택)",
    "CMFE Artists에서 얻고 싶은 것 (한두 줄)",
]
_MAIL_EOI = _mail("CMFE Artists 참여 신청",
                  "".join(f"{f}: \n" for f in EOI_FIELDS)
                  + "\n연주 기회를 받기 위해 이 내용을 최대 2년 보관하는 데 동의합니다.\n")


# 다섯 프로그램. 홈 카드, 프로그램 쪽, 구조화 데이터가 이 목록 하나를 읽는다.
# 항목·순서가 모두 같고 대표는 없다(CLAUDE.md §2.1). 프로그램마다 사진은 하나다.
PILLARS = {"learn": ("배움", "dot"), "share": ("나눔", "dot dot-open")}

# 여러 곳에 쓰는 사진은 설명을 하나로 둔다. care-christmas는 클라리넷 1명과 현악 3명
# (08 §3, 2025-12-20). tuh-atrium은 파일 이름과 달리 십자가와 독서대가 있는 경당이다.
CARE_ALT = "성탄절 요양시설에서 연주하는 클라리넷과 현악 연주자 세 명"
TUH_CHAPEL_ALT = "Tallaght University Hospital 경당에서 연주하는 클라리넷·해금·키보드"
RECORDERS_ALT = "나란히 세워 둔 크기가 다른 리코더 여섯 대"

PROGRAMMES_DATA = [
    dict(slug="getting-to-know", pillar="learn", name="클래식 음악과 친해지기",
         short="클래식 음악과 친해지기",
         img=("lecture-recital.jpg", 1050, 1400, "진행 중인 강의·연주"),
         line="어른과 어르신을 위한 클래식 음악 강의.",
         who="클래식 음악 소리가 좋은데 어디서부터 들어야 할지 몰랐던 어른과 어르신. 아무것도 "
             "몰라도 됩니다.",
         what="이야기하고, 녹음을 듣고, 눈앞에서 연주합니다. 강의는 친해지기, 함께하기, 내 취향 "
              "찾기의 세 단계로 이어집니다. 보통 여섯에서 열네 명이 모입니다.",
         # 정해진 날짜가 없다(Andrew, 2026-10-01). 강의는 요청을 받아 연다
         where="더블린 &middot; 무료 &middot; 요청하시면 엽니다",
         how="강의를 원하시면 메일 주세요. 도서관과 본당, 모임에서도 요청하실 수 있습니다.",
         btn="강의 문의", mail=_mail("클래식 음악과 친해지기")),
    dict(slug="outreach-concerts", pillar="share", name="찾아가는 음악회",
         short="찾아가는 음악회",
         img=("care-christmas.jpg", 1400, 1050, CARE_ALT),
         line="요양시설과 병원, 수도회, 지역 공간으로 연주를 들고 갑니다.",
         who="공연장까지 오기 어려운 분들, 그리고 그분들을 돌보는 곳.",
         what="휴게실이나 경당, 로비에서 30분에서 60분 동안 어쿠스틱으로 연주합니다. 관객이 낼 돈은 "
              "없습니다.",
         where="더블린, Co. Meath, Co. Wicklow, Co. Westmeath, 그 밖은 협의",
         how="방과 날짜를 알려 주세요. 연주자와 악기, 보면대는 저희가 챙겨 갑니다.",
         btn="음악회 초청하기", mail=_mail("찾아가는 음악회 초청")),
    dict(slug="recorder-ensemble", pillar="learn", name="무료 리코더 앙상블 과정",
         short="무료 리코더 앙상블 과정",
         img=("recorders.jpg", 1343, 1400, RECORDERS_ALT),
         line="악기를 처음 잡는 어른을 위한 무료 과정. 끝은 음악회입니다.",
         who="악기를 한 번도 다뤄 본 적 없는 어른. 악보를 몰라도 됩니다.",
         what="작은 모임이 둥글게 앉습니다. 첫 주에 첫 소리를 내고, 각자 자기 성부를 맡고, 가족과 "
              "친구 앞에서 짧은 음악회를 엽니다.",
         where="Mulhuddart Community Centre, Dublin 15 &middot; 매주 수요일 저녁 19:00&ndash;20:00 "
               "&middot; 무료",
         how="메일을 주시면 함께하는 방법을 알려 드립니다. 리코더는 빌려 드립니다.",
         btn="과정 문의하기", mail=_mail("리코더 앙상블 과정")),
    dict(slug="letters-ensemble", pillar="share", name="Letters Ensemble",
         short="Letters Ensemble",
         img=("letters-ensemble.jpg", 1400, 1050, "악기를 든 Letters Ensemble 단원들"),
         line="더블린에 사는 연주자들의 앙상블. 2024년 1월에 만들었습니다.",
         who="현악기, 관악기 등을 연주하는 아마추어 연주자.",
         what="아일랜드와 한국의 전통 음악, 성가, 편하게 들을 수 있는 편곡을 연습해서 공동체 "
              "공간에서 연주합니다.",
         where="더블린 &middot; 2024년 1월부터",
         # 단원 모집 중(Andrew, 2026-10-01)
         how="새 단원을 받고 있습니다. 다루시는 악기를 적어 메일을 주세요.",
         btn="단원 문의", mail=_mail("Letters Ensemble 참여")),
    dict(slug="concert-companion", pillar="learn", name="함께하는 음악여행",
         short="함께하는 음악여행",
         img=("dalgan-hall.jpg", 1400, 1050, "음악회를 앞두고 의자와 보면대를 놓아 둔, 아직 아무도 없는 홀"),
         line="소그룹으로 함께 공연을 보러 갑니다.",
         who="혼자서는 공연장에 가지 않을 분. 아일랜드에 온 지 얼마 안 된 분도 반깁니다.",
         what="다섯 명 안팎이 함께 갑니다. 미리 준비하고, 옆자리에 나란히 앉고, 다녀와서 이야기를 "
              "나눕니다.",
         where="더블린 &middot; 국립교향악단, RT&Eacute; 콘서트 오케스트라, NCH 인터내셔널 시리즈 "
               "같은 공연",
         how="메일을 주시면 함께 갈 공연이 생길 때 알려 드립니다.",
         btn="동행 문의", mail=_mail("함께하는 음악여행")),
]


# ---------------------------------------------------------------------------
# 홈
# ---------------------------------------------------------------------------

HOME = dict(
    hero=dict(
        eyebrow="공동체 음악 · 아일랜드 더블린",
        title=["클래식 음악을,", "<em>모두에게.</em>"],
        # 마스터 태그라인은 번역하지 않는다. 한국어 대역은 내부용이다(06 §5, 키트 27)
        master='<span lang="en">Bringing classical music where it&rsquo;s needed!</span>',
        # 키트 27 한국어 짧은 판과 일하는 방식
        lead='<span class="brandname">Classical Music for Everyone</span>은 더블린의 어르신, 이주민 '
             "공동체, 돌봄 시설에 클래식 음악회와 해설 강의, 무료 리코더 앙상블을 가져갑니다. 곡을 "
             "설명하며 연주하고, 듣는 분들을 직접 연주하도록 초대합니다.",
        cta=("get-involved.html", "함께하기"),
        more=("#programmes", "하는 일 보기"),
        img=("hero-outreach.jpg", 1800, 1350,
             "성 파트리치오 축일 음악회에서 연주하는 Letters Ensemble과 지휘자"),
        cap=("Letters Ensemble", "성 파트리치오 축일 음악회"),
    ),
    strip_label="함께하는 세 가지 길",
    strip=[
        ("get-involved.html#invite", "공간", "우리 공간으로 음악회를",
         "요양시설, 병원, 도서관, 본당. 방과 날짜만 알려 주세요.", "초청하기", False),
        ("get-involved.html#play", "연주자", "함께 연주하기",
         "2027년부터 사례와 멘토가 있는 연주를 열 계획입니다. 참여 신청은 지금 받습니다.",
         "CMFE Artists", False),
        ("get-involved.html#board", "자원봉사", "함께 세워 주세요",
         "첫 이사회를 꾸리고 있습니다. 자원봉사 자리 다섯입니다.", "이사회 자리", True),
    ],
    progs=dict(
        label="우리가 하는 일",
        h2="프로그램 다섯 가지.",
        lead="셋은 듣고 연주하는 법을 함께 배우는 자리이고, 둘은 실황 연주를 사람들이 있는 곳으로 "
             "들고 갑니다.",
        artists='2027년부터는 신진 연주자가 사례를 받고 멘토와 함께 연주하는 CMFE Artists를 열 '
                '계획입니다. <a class="link" href="get-involved.html#play">참여 신청은 지금 받습니다</a>.',
    ),
    why=dict(
        label="이 일을 하는 이유",
        text="더블린에는 음악회에 가기 어려운 분이 많습니다. 요양원에 계시거나 집 밖에 잘 나가지 "
             "못하는 분도 있고, 아일랜드에 온 지 얼마 안 되어 어디서 시작할지 모르는 분도 있습니다. "
             "그래서 저희가 찾아갑니다.",
        link="단체 소개",
    ),
    numbers=dict(
        label="기록",
        sr="숫자로 보기",
        figs=[(40, "회의 강의와 연주", "2023년부터", True),
              (5, "개의 프로그램, 배움과 나눔", "2026년 10월 현재", False),
              (4, "개국에서 연주: 아일랜드 · 프랑스 · 영국 · 한국", "2023 – 2025년", False)],
        note="2026년 South Dublin County Council 예술과가 창립자를 South Dublin Live에 "
             '선정했습니다. <a class="link" href="news.html#record">달마다 본 기록 보기</a>',
    ),
    bleed=dict(
        img=("tuh-atrium.jpg", 1400, 1052, TUH_CHAPEL_ALT),
        cap=("Tallaght University Hospital", "2026년 8월 · 사진: Tallaght University Hospital"),
    ),
    now=dict(
        img=("recorders.jpg", 1343, 1400, RECORDERS_ALT),
        label="지금 진행 중",
        tag="매주 수요일 저녁",
        h2="무료 리코더 앙상블 과정",
        facts=[("장소", "Mulhuddart Community Centre, Dublin 15"),
               ("시간", "매주 수요일 저녁 19:00&ndash;20:00"),
               ("비용", "무료. 리코더는 빌려 드립니다")],
        href="programmes.html#recorder-ensemble",
        btn="과정 안내",
    ),
)


# ---------------------------------------------------------------------------
# 소개. #founder #run #places #identity는 옛 주소가 가리키는 앵커다.
# ---------------------------------------------------------------------------

ABOUT_T = dict(
    head=dict(
        eyebrow="단체 소개",
        title=["이 일을 하는 이유."],
        lead="클래식 음악을 가까이 듣기 어려운 분들에게 실황 연주를 가져갑니다. 더블린의 어르신과 "
             "이주민 공동체, 돌봄 시설에 계신 분들입니다. 그분들이 이미 계신 방으로 찾아갑니다.",
        img=("columban-ensemble.jpg", 1400, 1050,
             "노란 방에서 악기를 든 Letters Ensemble 현악 연주자 네 명과 지휘자"),
        cap=("성 골롬반 선교 수녀회, 위클로", "2024년 11월"),
    ),
    glance=[("창립", "2024년 1월", "아일랜드 더블린"),
            ("운영하는 것", "프로그램 다섯", "배움과 나눔"),
            ("연주한 곳", "4개국", "아일랜드 · 프랑스 · 영국 · 한국"),
            ("지위", "비영리 활동", "보증유한회사(CLG) 설립 준비 중. 아직 등록된 자선단체는 "
                                   "아닙니다.")],
    story=dict(
        label="지나온 길",
        h2="2023년부터.",
        text=["시작은 2023년입니다. 루르드에서 클라리넷을 독주했고, 여름에는 런던 BBC 프롬스 객석에 "
              '앉았습니다. 2024년 1월 김서현이 더블린에서 <span class="brandname">Classical Music for '
              "Everyone</span>과 Letters Ensemble을 만들었고, 첫 강의에는 여섯 명이 왔습니다.",
              "2026년 8월까지 요양시설과 수도 공동체, 본당, 병원, 노숙인 쉼터, 공동체 센터에서 마흔 "
              "번의 강의와 연주를 했습니다. 2026년에는 은퇴한 Presentation 수녀님 일곱 분과 함께한 "
              "파일럿 리코더 앙상블에서 Mulhuddart의 무료 과정이 나왔고, South Dublin County Council "
              "예술과가 창립자를 South Dublin Live 2026에 선정했습니다."],
        link="전체 연표 보기",
    ),
    founder=dict(
        img=("founder-speaking.jpg", 1050, 1400, "마이크를 들고 강의·연주를 진행하는 김서현"),
        label="창립자",
        name="Andrew Seohyeon Kim (김서현)",
        role="창립자·예술감독",
        text="더블린에서 활동하는 클라리네티스트이자 오르가니스트, 공동체 음악가입니다. TU Dublin "
             "Conservatoire에서 연주 전공 학사(BMus Hons) 학위를 받았고, Dolphin&rsquo;s Barn "
             "성모 통고 성당의 음악감독입니다. 졸업 연구로 더블린 8구 Warrenmount에서 은퇴한 "
             "Presentation 수녀님 일곱 분과 10주 동안 리코더 앙상블을 했습니다. 일곱 분 모두 끝까지 "
             "함께해 사람들 앞에서 연주했습니다.",
    ),
    run=dict(
        label="운영 방식",
        h2="비영리 활동입니다.",
        # 키트 27의 지위 문장 그대로
        lead=STATUS,
        cols=[("누가 정하나", "법인이 등록되면 독립된 자원봉사 이사회가 운영을 맡습니다. 지금 첫 "
                            "이사를 모집하고 있습니다. 의장, 재무, 사무, 세이프가딩·돌봄, 지역사회 "
                            "자리입니다."),
              ("돈", "아직은 후원을 요청하거나 받지 않습니다. 저희를 대신해 개인 계좌로 돈을 보내 "
                    "달라고 하는 사람은 없습니다."),
              ("사진과 이야기", "연주자와 악기, 빈 공간을 싣습니다. 그 밖에 알아볼 수 있는 분은 서면 "
                             "동의가 있을 때만 싣습니다. 이 방식은 Dóchas 윤리적 소통 지침(2023)⁠을 "
                             "참고했습니다.")],
        links=[("get-involved.html#board", "창립 이사회 알아보기"),
               ("contact.html#privacy", "개인정보를 다루는 방식")],
    ),
    places=dict(
        label="장소",
        h2="연주하고 가르쳐 온 곳.",
        # 08 §2: 참가자에게 공연을 안내하고 단체 관람을 준비했다
        lead="국립 콘서트홀(National Concert Hall) 공연은 참가자에게 안내하고 단체 관람을 "
             "준비했습니다.",
        names=["Tallaght University Hospital", "Rua Red, Tallaght", "Clondalkin Lodge",
               "Warrenmount, Dublin 8", "Mulhuddart Community Centre",
               "성 골롬반 선교 수녀회, 위클로", "Dalgan Park, 미스", "Dysart 본당, 웨스트미스",
               "HSE EVE Goirtin Hub", "Morning Star Hostel", "TU Dublin",
               "Our Lady of Dolours, Dolphin&rsquo;s Barn", "Church of the Three Patrons, Rathgar",
               "파리 외방전교회", "런던 한인 천주교회", "관덕정 순교기념관, 대구"],
    ),
    identity=dict(
        label="이름",
        h2="<em>Everyone</em>이 금색인 이유",
        text="로고에서 &lsquo;for&rsquo;는 작게, &lsquo;Everyone&rsquo;은 크고 금색으로 놓습니다. "
             "이름의 마지막 낱말이 저희가 지켜야 할 약속이기 때문입니다.",
        alt="Classical Music for Everyone 로고: 높은음자리표 옆 워드마크, &lsquo;Everyone&rsquo;이 "
            "크고 금색으로 놓여 있다",
    ),
)


# ---------------------------------------------------------------------------
# 프로그램
# ---------------------------------------------------------------------------

PROGRAMMES_T = dict(
    head=dict(
        eyebrow="프로그램",
        title=["프로그램."],
        lead="강의, 사람들이 사는 곳으로 가는 음악회, 무료 수업, 앙상블, 그리고 공연장에 함께 가기.",
        img=("tuh-trio.jpg", 1400, 787,
             "Tallaght University Hospital 아트리움의 소프라노·피아노·클라리넷"),
        cap=("Tallaght University Hospital", "2026년 8월 · 사진: Tallaght University Hospital"),
    ),
    toc_label="다섯 프로그램",
    fact_labels=("대상", "하는 일", "장소와 때", "참여 방법"),
    artists=dict(
        img=("ruared-trio.jpg", 1400, 933, "Rua Red 무대에서 인사하는 클라리넷·소프라노·피아노"),
        cap=("Rua Red, Tallaght", "South Dublin Live 2026 · 사진: Ben Ryan / SDCC"),
        label="2027년부터",
        lead="신진 연주자가 사례를 받고 멘토와 함께 요양시설, 병원, 도서관, 공동체 공간에서 연주하는 "
             "자리를 열 계획입니다.",
        facts=[("대상", "학생, 신진, 아마추어, 한국 연주자. 전문 연주자도 함께합니다."),
               ("하는 방식", "전문·학생·신진 연주자는 예술위원회의 「Paying the Artist」 원칙에 맞춰 "
                          "사례를 받고, 아마추어 연주자는 실비를 받게 됩니다. 학생·신진 연주자의 첫 "
                          "방문은 멘토와 함께 갑니다."),
               ("지금", "참여 신청을 받고 있습니다. 첫 공모와 선발 기준은 2027년에 공개할 "
                        "계획입니다.")],
        btn="참여 신청하기",
    ),
)


# ---------------------------------------------------------------------------
# 함께하기
# ---------------------------------------------------------------------------

GET_INVOLVED_T = dict(
    head=dict(
        eyebrow="함께하기",
        title=["함께하는 방법."],
        lead="우리 공간으로 음악회를 부르거나, 함께 연주하고 싶다고 알려 주시거나, 창립 이사회에 "
             "함께해 주세요. 시작은 메일 한 줄이면 됩니다.",
        img=("church-aisle.jpg", 1050, 1400, "웨스트미스 주 본당 제대 앞에 든 클라리넷"),
        cap=("Dysart, 웨스트미스", "2025년"),
    ),
    ways=[("invite", "우리 공간으로 음악회를", "요양시설, 병원, 본당, 공동체 센터"),
          ("play", "함께 연주하기", "연주자를 위한 CMFE Artists, 2027년 계획"),
          ("board", "창립 이사회", "자원봉사 자리 다섯")],
    invite=dict(
        label="파트너 공간",
        h2="우리 공간으로 음악회를.",
        text="요양시설, 병원, 도서관, 본당, 공동체 센터. 방과 날짜를 알려 주시면 연주자와 악기, "
             "보면대, 프로그램은 저희가 챙겨 갑니다. 공동체 센터라면 무료 초보자 과정도 열 수 있습니다. "
             "매주 따뜻한 방 하나와 담당자 한 분, 동네에 알리는 일을 맡아 주시면 나머지는 재원이 "
             "마련되는 대로 저희가 준비합니다.",
        href=_MAIL_INVITE, btn="초청 문의하기",
        img=("care-christmas.jpg", 1400, 1050, CARE_ALT),
        cap=("찾아가는 음악회", "성탄"),
    ),
    play=dict(
        label="CMFE Artists",
        h2="함께 연주하기.",
        lead="학생, 신진, 아마추어, 한국 연주자, 그리고 음악이 필요한 곳에서 연주하고 싶은 전문 "
             "연주자를 위한 자리입니다. CMFE Artists는 2027년에 시작할 계획입니다. 지금 알려 주시면 "
             "첫 공모가 열릴 때 연락드리겠습니다. 아마추어 연주자라면 지금 "
             '<a class="link" href="programmes.html#letters-ensemble">Letters Ensemble</a>에 함께하실 '
             "수 있습니다.",
        sub="보내 주실 것",
        fields=EOI_FIELDS,
        note="전문·학생·신진 연주자는 사례를, 아마추어 연주자는 실비를 받게 됩니다. 보내 주신 내용은 "
             "연주 기회를 드리기 위해 최대 2년 동안 보관하고, 요청하시면 언제든 지웁니다.",
        href=_MAIL_EOI, btn="참여 신청 보내기",
    ),
    support=dict(
        label="함께 세우기",
        board=dict(
            h2="창립 이사회에 함께해 주세요.",
            lead="독립된 자원봉사 이사회의 첫 이사를 모집하고 있습니다.",
            facts=[("자리", "의장, 재무, 사무, 세이프가딩·돌봄, 지역사회 이사"),
                   ("시간", "1년에 여섯 번쯤 회의하고, 한 달에 서너 시간이 듭니다"),
                   ("조건", "무보수이며 합당한 실비는 드립니다. Garda 신원조회와 짧은 입문 안내가 있습니다")],
            href=_MAIL_BOARD, btn="자리 문의하기",
        ),
        gifts="아직은 후원을 요청하거나 받지 않습니다. 받을 수 있게 되면 이 쪽에 알리겠습니다.",
    ),
    join=dict(tag="직접 참여",
              text="직접 참여하고 싶으신가요? 모든 프로그램이 처음인 분을 반기고, 한 번 와 보셨다고 "
                   '계속 나와야 하는 것도 아닙니다. <a class="link" href="programmes.html">프로그램 보기</a>'),
)


# 후원(Friends, 음악회 후원, 후원자에게 드리는 약속)은 닫혀 있다. 문안은 공개 저장소
# 밖의 giving_ko.py에 있고, layout.OPEN_GIVING이 True일 때만 읽는다.
if OPEN_GIVING:
    import giving_ko
    giving_ko.apply(globals())

INDEX = P.home(HOME, PROGRAMMES_DATA, PILLARS)
ABOUT = P.about(ABOUT_T)
PROGRAMMES = P.programmes(PROGRAMMES_T, PROGRAMMES_DATA, PILLARS)
GET_INVOLVED = P.get_involved(GET_INVOLVED_T, _ico)


# ---------------------------------------------------------------------------
# 소식·기록
# ---------------------------------------------------------------------------

NEWS_T = dict(
    head=dict(
        eyebrow="소식·기록",
        title=["새 소식과 지나온 기록."],
        # 2023년부터 40+ · 2026년 8월까지 기록된 40 = 17 + 20 + 1 + 2 (03 §1)
        lead="2023년부터 마흔 번이 넘는 강의와 연주를 했습니다. 2026년 8월까지 기록된 것은 강의 "
             "17회, 찾아가는 음악회 20회, 파일럿 음악회 1회, South Dublin Live 2026 음악회 "
             "2회입니다.",
        img=("quartet-hall.jpg", 1400, 791, "성 파트리치오 축일 장식이 걸린 홀에서 연주하는 현악 4중주와 지휘자"),
        cap=("Letters Ensemble", "성 파트리치오 축일 음악회"),
    ),
    latest_sr="새 소식",
    latest=[
        ("2026년 가을", "창립 이사회를 꾸립니다",
         "보증유한회사(CLG) 설립을 준비하며 자원봉사 이사를 찾고 있습니다.",
         "get-involved.html#board", "이사 자리 보기"),
        ("2026년 가을", "무료 리코더 앙상블 과정",
         "매주 수요일 저녁 Mulhuddart Community Centre에서 열립니다.",
         "programmes.html#recorder-ensemble", "과정 안내"),
        ("2026년 8월", "South Dublin Live 2026",
         "South Dublin County Council 예술과가 창립자를 선정했습니다. Tallaght University Hospital과 "
         "Tallaght의 Rua Red에서 두 번 연주했습니다.",
         "#gallery", "사진 보기"),
    ],
    chart=dict(
        label="기록",
        h2="마흔 번, 한 칸에 하나씩.",
        lead="2023년 2월부터 2026년 8월까지 기록된 강의와 연주를 달마다 놓았습니다. 채운 칸은 강의, "
             "빈 칸은 음악회와 연주입니다.",
        aria=("2023년부터 2026년까지의 달력. 기록된 {n}회를 한 칸씩 표시했다: 강의 {talks}회, "
              "연주 {perf}회."),
        scroll="달마다 본 기록",
        key_talk="강의 ({n})",
        key_perf="음악회·연주 ({n})",
        # 활동대장의 강의 15 메모(2025-12-05)
        key_note="열다섯 번째 강의(2025년 12월)는 함께 들은 음악회였습니다. 그 밖의 함께 관람, "
                 "연습, 수업은 넣지 않았습니다.",
    ),
    timeline=dict(
        label="연표",
        h2="클라리넷 하나에서 공동체까지.",
        rows=[
            ("2023년 2월", "시작 이전",
             "프랑스 루르드에서 클라리넷을 독주했습니다. 이름이 붙기 한 해 전입니다."),
            ("2024년 1월", "시작",
             "더블린에서 Letters Ensemble과 함께 창립했습니다. 첫 강의에 여섯 명이 왔습니다."),
            ("2024년", "음악이 나갑니다",
             "미스 주 Dalgan Park, 위클로, 런던, 파리, 대구. 강의는 TU Dublin으로 옮겼습니다."),
            # 08 §2: 안내하고, 단체 관람을 준비했다
            ("2025년 가을", "공연을 안내합니다",
             "참가자에게 공연을 안내하고 단체 관람을 준비하기 시작합니다. NCH 인터내셔널 시리즈, "
             "TU Dublin 필하모닉, 2026년 초에는 국립교향악단."),
            ("2025년 10월", "관객이 연주자가 됩니다",
             "은퇴한 Presentation 수녀님 일곱 분과 리코더 앙상블 준비를 시작합니다."),
            ("2025년 12월", "함께 본 음악회",
             "열다섯 번째 모임은 국립 콘서트홀에서 함께 들은 음악회였습니다."),
            ("2026년 1&ndash;4월", "파일럿, 그리고 그 음악회",
             "더블린 8구 Warrenmount에서 10주 동안 연습하고, Clondalkin Lodge에서 부활 음악회를 "
             "열었습니다. 일곱 분 모두 끝까지 함께했습니다."),
            ("2026년 8월", "South Dublin Live 2026",
             "South Dublin County Council 예술과가 창립자를 South Dublin Live 2026에 선정해 Tallaght "
             "University Hospital과 Rua Red에서 두 번 연주했습니다. 같은 달 파일럿 모임이 "
             "마무리됩니다."),
            ("2026년 가을", "일반에 열린 과정",
             "무료 리코더 앙상블 과정이 매주 수요일 저녁 Mulhuddart Community Centre에서 열립니다."),
        ],
    ),
    gallery=dict(
        label="사진",
        h2="그 자리에서.",
        lead="연주자와 악기, 빈 공간을 싣습니다. 그 밖에 알아볼 수 있는 분은 서면 동의가 있을 때만 "
             "싣습니다.",
        rows=[
            (("hero-outreach.jpg", 1800, 1350,
              "성 파트리치오 축일 음악회에서 연주하는 Letters Ensemble과 지휘자"),
             "Letters Ensemble · 성 파트리치오 축일 음악회"),
            (("care-christmas.jpg", 1400, 1050, CARE_ALT),
             "찾아가는 음악회 · 성탄"),
            (("columban-ensemble.jpg", 1400, 1050,
              "노란 방에서 악기를 든 Letters Ensemble 현악 연주자 네 명과 지휘자"),
             "성 골롬반 선교 수녀회, 위클로 · 2024년 11월"),
            (("dalgan-hall.jpg", 1400, 1050, "음악회를 앞두고 의자와 보면대를 놓아 둔, 아직 아무도 없는 홀"),
             "Dalgan Park, 미스 · 2024년 3월"),
            (("church-aisle.jpg", 1050, 1400, "웨스트미스 주 본당 제대 앞에 든 클라리넷"),
             "Dysart, 웨스트미스 · 2025년"),
            (("score-stand.jpg", 1050, 1400, "보면대 위 파트 악보 너머로 연습하는 현악 3중주"),
             "성탄 음악회를 앞두고 · 2025년 12월"),
            (("recorders.jpg", 1343, 1400, RECORDERS_ALT),
             "리코더 · 2025년 11월"),
            (("tuh-trio.jpg", 1400, 787,
              "Tallaght University Hospital 아트리움의 소프라노·피아노·클라리넷"),
             "Tallaght University Hospital · 2026년 8월 · 사진: Tallaght University Hospital"),
            (("ruared-trio.jpg", 1400, 933, "Rua Red 무대에서 인사하는 클라리넷·소프라노·피아노"),
             "Rua Red, Tallaght · 2026년 8월 · 사진: Ben Ryan / SDCC"),
            (("letters-ensemble.jpg", 1400, 1050, "악기를 든 Letters Ensemble 단원들"), "Letters Ensemble"),
            (("two-clarinets.jpg", 1050, 1400, "피아노 뚜껑 위에 놓인 클라리넷 두 대"), None),
            (("tuh-haegeum.jpg", 1400, 934, "병원 아트리움에서 해금을 연주하는 연주자"),
             "Tallaght University Hospital · 2026년 8월 · 사진: Tallaght University Hospital"),
        ],
    ),
)

NEWS = P.news(NEWS_T, L)


# ---------------------------------------------------------------------------
# 문의, 개인정보 고지와 함께(키트 06: 웹사이트의 개인정보 고지)
# ---------------------------------------------------------------------------

CONTACT_T = dict(
    head=dict(
        eyebrow="문의",
        title=["메일 주세요."],
        lead="보내 주신 메일에는 모두 답장합니다. 한 줄이면 충분합니다.",
    ),
    email_label="이메일",
    email=EMAIL,
    email_href=_mail("Classical Music for Everyone 문의"),
    btn="메일 보내기",
    tel="+353 83 078 0635",
    tel_href="tel:+353830780635",
    details_label="연락처",
    details_h2="저희가 있는 곳.",
    # 보험: 증서 보유(2026-10-01 확인). Garda 신원조회는 마친 뒤에 쓴다.
    details=[("거점", "아일랜드 더블린"),
             ("활동 지역", "더블린, Co. Meath, Co. Wicklow, Co. Westmeath, 그 밖은 협의"),
             ("언어", '한국어 · <span lang="en">English</span>'),
             ("보험", "공공배상책임보험에 들어 있습니다. 요청하시는 기관에 증서를 보여 드립니다."),
             ("답하는 사람", "창립자·예술감독 Andrew Seohyeon Kim(김서현)")],
    privacy=dict(
        label="개인정보",
        h2="보내 주신 정보.",
        intro="이 웹사이트에는 입력 양식도, 쿠키도, 방문 분석이나 광고 도구도 없습니다. 2026년 10월 1일 "
              "갱신.",
        blocks=[
            ("정보를 책임지는 곳", '<span class="brandname">Classical Music for Everyone</span>, 더블린의 '
                                "비영리 공동체 음악 단체입니다. 개인정보에 관한 문의는 "
                                f'<a class="link" href="mailto:{EMAIL}">{EMAIL}</a>로 보내 주세요.'),
            ("메일을 보내 주시면", "보내 주신 내용은 답장하고 요청하신 일을 하는 데만 씁니다. 음악회 문의, "
                                "이사회 문의, 연주자 참여 신청이 그렇습니다. 팔거나 넘기지 않습니다. 연주자 "
                                "정보는 연주 기회를 드리기 위해 최대 2년 동안 보관하고, 접근성 필요는 적지 "
                                "않으셔도 됩니다."),
            ("함께 다루는 곳", "이 사이트는 GitHub에 있고, GitHub는 보안을 위해 방문자의 IP 주소를 "
                             "기록합니다. 글꼴은 Google Fonts에서 불러와 Google도 IP 주소를 받고, 이메일은 "
                             "Google 서비스를 씁니다. 이 업체들은 EU가 승인한 보호 장치에 따라 유럽경제지역 "
                             "밖에서 정보를 다룰 수 있습니다."),
            ("요청하실 수 있는 것", "저희가 가진 정보를 보거나 고치거나 지우도록, 사용을 멈추거나 사본을 "
                                 "주도록 언제든 요청하실 수 있습니다. 답에 만족하지 못하시면 아일랜드 "
                                 '<a class="link" href="https://www.dataprotection.ie/">개인정보보호위원회(Data '
                                 "Protection Commission)</a>에 민원을 내실 수 있습니다."),
        ],
    ),
)

CONTACT = P.contact(CONTACT_T)
