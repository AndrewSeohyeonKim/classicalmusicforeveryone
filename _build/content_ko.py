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
from layout import OPEN_GIVING, PROG_MENU

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


def _fields(prompts):
    """메일 본문: 한 줄에 하나씩, 읽는 분이 채워 넣을 항목. 물음이나 콜론으로 끝나는 항목에는
    콜론을 또 붙이지 않고, 줄은 CRLF로 끝낸다(RFC 6068, QA40-17)."""
    return "".join(f"{x}{'' if x.endswith(('?', ':')) or ': ' in x else ':'} \r\n" for x in prompts)


# 초청 메일은 어디서 보내든 같다(찾아가는 음악회, 함께하기, 문의).
INVITE_FIELDS = ["기관 이름과 지역",
                 "연주할 방, 피아노가 있는지",
                 "들으실 분들과 대략의 인원",
                 "가능한 날짜나 시간",
                 "담당자 이름과 전화번호"]
MAIL_INVITE = _mail("찾아가는 음악회 초청", _fields(INVITE_FIELDS))
_MAIL_INVITE = MAIL_INVITE
_MAIL_BOARD = _mail("창립 이사회 문의",
                    "관심 있는 역할 (의장 / 재무 / 사무 / 세이프가딩·돌봄 / 지역사회): \r\n"
                    "저에 대해 몇 줄: \r\n")

# CMFE Artists: 관심은 자유롭게 받는다(Andrew, 2026-10-02). 키트 15의 신청서 대신 네 줄,
# 나머지는 쓰는 분이 자기 말로 적는다.
EOI_FIELDS = ["이름", "악기·성악·분야", "연주나 작업 링크 (있다면)", "자기소개 몇 줄"]
_MAIL_EOI = _mail("CMFE Artists 참여 신청", _fields(EOI_FIELDS))


# 다섯 프로그램. 홈 카드, 프로그램 쪽, 구조화 데이터가 이 목록 하나를 읽는다.
# 항목·순서가 모두 같고 대표는 없다(CLAUDE.md §2.1). 프로그램마다 사진은 하나다.
PILLARS = {"learn": ("배움", "dot"), "share": ("나눔", "dot dot-open")}

# 여러 곳에 쓰는 사진은 설명을 하나로 둔다. care-christmas는 클라리넷 1명과 현악 3명
# (08 §3, 2025-12-20). tuh-atrium은 파일 이름과 달리 십자가와 독서대가 있는 경당이다.
CARE_ALT = "성탄절 요양시설에서 연주하는 클라리넷과 현악 연주자 세 명"
TUH_CHAPEL_ALT = "Tallaght University Hospital 경당에서 연주하는 클라리넷·해금·키보드"
RECORDERS_ALT = "나란히 세워 둔 크기가 다른 리코더 여섯 대"

# 연주하고 가르쳐 온 곳(소개 #places). 곳의 성격으로 묶고 지역을 붙였다. 모두 기록에 있는 곳이다.
# 수는 계산하므로, 그 수를 인용하는 문장이 낡지 않는다(4차 개편).
PLACES = [
    ("병원과 돌봄", [
        ("Tallaght University Hospital", "더블린 Tallaght"),
        ("Clondalkin Lodge", "더블린"),
        ("HSE EVE Goirtin Hub", "더블린 7구"),
        ("Morning Star Hostel", "더블린 7구")]),
    ("본당과 교회", [
        ("Our Lady of Dolours 성당", "더블린 Dolphin&rsquo;s Barn"),
        ("Church of the Three Patrons", "더블린 6구 Rathgar"),
        ("Methodist Centenary Church", "더블린 6구 Ranelagh"),
        ("Blessed Sacrament Chapel", "더블린 1구"),
        ("Kilmessan 성당", "미스 주"),
        ("Dysart 본당", "웨스트미스 주")]),
    ("수도 공동체", [
        ("성 골롬반 외방선교 수녀회", "위클로 주 Magheramore"),
        ("Dalgan Park", "미스 주"),
        ("Warrenmount", "더블린 8구"),
        ("마리아의 프란치스코 선교 수녀회", "더블린 5구")]),
    ("예술과 배움", [
        ("Rua Red", "더블린 Tallaght"),
        ("TU Dublin", "더블린 7구 Grangegorman"),
        ("Carmelite Community Centre", "더블린"),
        ("Mulhuddart Community Centre", "더블린 15구")]),
    ("해외", [
        ("파리 외방전교회", "프랑스 파리"),
        ("Palais Brongniart", "프랑스 파리"),
        ("런던 한인 천주교회", "영국 런던"),
        ("관덕정 순교기념관", "한국 대구")]),
]
N_PLACES = sum(len(rows) for _, rows in PLACES)

PROGRAMMES_DATA = [
    dict(slug="getting-to-know", pillar="learn", name="클래식 음악과 친해지기",
         short="클래식 음악과 친해지기",
         # 강의가 다루는 것, Andrew의 말(2026-10-03, 「야화」는 「밤 강의」로도 읽혀 「뒷이야기」로). 단계 이름은 쪽에 남는다
         icon="lesson", vocab="음악사 · 이론 · 뒷이야기",
         img=("lecture-recital.jpg", 1050, 1400, "BBC 프롬스 슬라이드를 띄워 놓고 강의하는 창립자"),
         line="<mark>연주를 눈앞에서</mark> 들으며 처음부터 알아 가는 강의입니다.",
         page=dict(
             lead="어디서부터 들어야 할지 모르는 분을 위한 강의입니다. 이야기와 녹음, <mark>실황 연주로</mark> 클래식과 "
                  "친해집니다.",
             cap=("BBC 프롬스를 다룬 강의", "더블린"),
             glance=[("대상", "클래식 음악이 궁금한 분 누구나"),
                     ("장소", "더블린"),
                     ("언제", "함께 정하는 날"),
                     ("준비물", "음악 지식이 없어도 됩니다")],
             now=("요청하시면 엽니다", "혼자이시든 모임이시든 메일을 주세요."),
             how_h2="처음 듣는 데서 내 취향까지, 세 단계.",
             steps=[("친해지기", "클래식 음악이 무엇인지 시대와 악기로 나눠 들어 봅니다."),
                    ("함께하기",
                     "아일랜드의 오케스트라와 연주자를 소개합니다. 표 예매와 좌석 고르기도 알려 드립니다."),
                    ("내 취향 찾기",
                     "한 곡을 피아니스트 다섯 명의 연주로 견주어 들으며 <mark>내 취향을</mark> 찾아봅니다.")],
             expect_h2="첫 강의 전에.",
             faq=[("미리 알아야 할 것이 있나요?",
                   "<strong>아니요.</strong> 첫 단계는 「클래식 음악이란 무엇인가」에서 시작하고, "
                   "<mark>곡마다 설명을</mark> 곁들입니다."),
                  ("몇 명쯤 모이나요?",
                   "인원을 센 강의에는 <mark>여섯에서 열네 명이</mark> 왔습니다. 강의별 인원은 아래 "
                   "도표에 있습니다."),
                  ("우리 모임에서도 요청할 수 있나요?",
                   "<strong>네.</strong> 모임 이름과 인원, 모일 곳을 메일로 알려 주세요.")],
             record_h2="지금까지의 강의.",
             record_lead="기록에 남은 강의를 날짜, 주제, 장소와 함께 모았습니다.",
             join_h2="강의를 요청해 주세요.",
             join_text="",
             join_btn="강의 문의하기",
             mail_subject="클래식 음악과 친해지기",
             mail_fields=["이름", "모임이나 기관 (있다면)", "모일 수 있는 곳", "대략의 인원",
                          "좋은 날짜나 시간"],
         )),
    dict(slug="outreach-concerts", pillar="share", name="찾아가는 음악회",
         short="찾아가는 음악회",
         icon="piano", vocab="휴게실 · 경당 · 아트리움",
         img=("care-christmas.jpg", 1400, 1050, CARE_ALT),
         line="<mark>요양시설과 병원</mark>, 본당과 커뮤니티 센터로 갑니다.",
         page=dict(
             lead="사람들이 <mark>이미 계신 방으로</mark> 찾아가 연주합니다. 곡마다 이야기를 곁들입니다.",
             cap=("클라리넷과 현악 3중주", "2025년 성탄"),
             glance=[("대상", "요양시설, 병원, 수도 공동체, 본당, 커뮤니티 센터"),
                     ("장소", "초청하신 방, 더블린과 그 밖은 협의"),
                     ("언제", "함께 정하는 날"),
                     ("준비물", "방 하나와 날짜, 연락할 담당자 한 분")],
             now=("초청받는 중", "방과 가능한 날짜를 적어 메일을 주세요."),
             how_h2="세 단계면 방에서 음악회가 열립니다.",
             steps=[("알려 주세요", "어느 방에서, 언제쯤, 어떤 분들이 들으실지 메일로 알려 주세요."),
                    ("곡을 고릅니다", "<mark>처음 들어도</mark> 즐길 수 있는 곡을 그 방과 듣는 분들에 맞춰 고릅니다."),
                    ("찾아가 연주합니다", "연주자와 악기, 보면대까지 저희가 챙겨 갑니다.")],
             expect_h2="초청하시기 전에.",
             faq=[("누가 연주하나요?",
                   "<mark>창립자 김서현이</mark> 클라리넷과 오르간으로 혼자, 또는 연주자를 불러 함께 "
                   "연주합니다. Letters Ensemble이 맡는 음악회도 있습니다."),
                  ("누가 들을 수 있나요?",
                   "입주자나 환자, 가족, 직원까지 그 방에 계신 분 <mark>누구나</mark> 들으실 수 "
                   "있습니다. 복장 규정은 없습니다."),
                  ("어디에서 연주해 왔나요?",
                   f"가르친 곳까지 <mark>4개국</mark> {N_PLACES}곳입니다. 요양시설과 수도 공동체, 본당, 병원 등 "
                   '모든 곳이 <a class="link" href="about.html#places">단체 소개</a>에 있습니다.')],
             record_h2="지금까지의 음악회.",
             record_lead="기록에 남은 음악회를 날짜와 장소, 편성과 함께 모았습니다.",
             join_h2="음악회를 초청해 주세요.",
             join_text="",
             join_btn="음악회 초청하기",
             mail=MAIL_INVITE,
             mail_fields=INVITE_FIELDS,
         )),
    dict(slug="recorder-ensemble", pillar="learn", name="커뮤니티 리코더 앙상블 클래스",
         short="리코더 앙상블 클래스",
         icon="recorder", vocab="첫 소리 · 악보 읽기 · 화음",
         img=("recorders.jpg", 1343, 1400, RECORDERS_ALT),
         # 2026-10-01 이름을 바꿨다
         line="<mark>악기를 처음 잡는</mark> 어른이 함께 배우는 클래스입니다.",
         page=dict(
             lead="악기를 한 번도 다뤄 보지 않은 어른이 매주 함께 배웁니다. <mark>첫 주에</mark> 첫 소리를 냅니다.",
             cap=("리코더", "2025년 11월"),
             # 창립자 채널의 파일럿 앙상블 영상. 재생을 누르기 전에는 저희 사진만 보인다
             video=dict(kind="youtube", id="i7skwGKWSYY", poster="recorders.jpg",
                        cap=("파일럿 앙상블", "은퇴한 Presentation 수녀님들의 리코더 합주입니다.")),
             room_h2="클래스가 시작된 곳.",
             glance=[("대상", "악기를 처음 잡는 어른"),
                     ("장소", "Mulhuddart, 더블린 15구"),
                     ("언제", "2026년 가을, 매주 수요일 저녁 7시~8시"),
                     ("준비물", "악기도, 악보 지식도 없어도 됩니다")],
             now=("진행 중", "<strong>매주 수요일 저녁 7시~8시</strong><span class=\"sr-only\">, </span>"
                         "<span class=\"pp-where\">Mulhuddart Community Centre</span>"),
             live=True,
             how_h2="첫 소리에서 나만의 성부까지.",
             steps=[("첫 소리", "리코더를 잡고, 숨을&nbsp;쉬고, 불어 봅니다."),
                    ("악보는 처음부터",
                     "음과 손가락 짚는 법을 하나씩 익힙니다. 악보는 저희가 클래스에 맞춰 만듭니다."),
                    ("나만의 성부",
                     "한 사람이 한 성부씩 맡아 화음을 냅니다. 학기 끝에는 우리들의 <mark>작은 음악회를</mark> 엽니다.")],
             expect_h2="첫 수업 전에.",
             faq=[("리코더가 없어도 되나요?", "<strong>네.</strong> 리코더는 <mark>빌려 드립니다</mark>."),
                  ("악보를 읽을 줄 알아야 하나요?",
                   "<strong>아니요.</strong> <mark>연주하면서</mark> 악보 읽기도 처음부터 조금씩 배웁니다."),
                  ("이 클래스는 어떻게 시작됐나요?",
                   "<mark>10주 파일럿에서</mark> 시작했습니다. 은퇴한 Presentation 수녀님 일곱 분이 "
                   "함께했고, 아래 영상이 그 모임입니다.")],
             record_h2="이 클래스가 생겨나기까지.",
             record_lead="음악회에서 나온 질문 하나에서 시작합니다.",
             join_h2="클래스에 함께하세요.",
             join_text="<strong>매주 수요일 저녁 7시~8시</strong>, Mulhuddart에서 열립니다.",
             join_btn="클래스 문의하기",
             mail_subject="커뮤니티 리코더 앙상블 클래스",
             mail_fields=["이름",
                          "전화번호 (선택)",
                          "악기를 배워 본 적이 있는지",
                          "리코더를 빌리고 싶은지",
                          "참여에 도움이 필요한 점 (선택)"],
         )),
    dict(slug="letters-ensemble", pillar="share", name="Letters Ensemble",
         short="Letters Ensemble",
         icon="strings", vocab="아일랜드 · 한국 · 성가",
         img=("letters-ensemble.jpg", 1400, 1050, "아일랜드 국기와 클로버로 꾸민 홀에서 악기를 들고 선 현악 연주자 네 명과 지휘자"),
         line="더블린의 <mark>아마추어</mark> 연주자들이 공동체를&nbsp;위해 연주합니다.",
         page=dict(
             lead="2024년 1월 더블린에서 생긴 <mark>아마추어</mark> 앙상블입니다. 아일랜드와 한국의 전통 음악, 성가를 "
                  "연주합니다.",
             cap=("Letters Ensemble", "현악 연주자 네 명과 지휘자"),
             glance=[("대상", "악기를 연주하는 아마추어 누구나"),
                     ("장소", "더블린"),
                     ("언제", "연습 시간은 문의해 주세요"),
                     ("준비물", "직접 연주하는 악기")],
             now=("누구나 환영", "메일을 주시면 연습 일정을 알려 드립니다."),
             how_h2="더블린에서 연습하고, 사람들이 있는 곳에서 연주합니다.",
             steps=[("악기를 알려 주세요", "다루시는 악기를 적어 메일을 주세요. <mark>누구나</mark> 함께할 수 있습니다."),
                    ("함께 연습합니다", "더블린에서 창립자 김서현의 지휘로 연습합니다."),
                    ("공동체에서 연주합니다",
                     "수도 공동체와 본당, 돌봄&nbsp;시설에서 연주합니다. 축일이나 성탄 음악회가 많았습니다.")],
             expect_h2="함께하시기 전에.",
             faq=[("어떤 곡을 연주하나요?",
                   "모차르트 「아베 베룸 코르푸스」, 「아리랑」 등입니다. 「Down by the Sally Gardens」 같은 "
                   "아일랜드 노래도 연주합니다."),
                  ("오래 쉬었는데 함께할 수 있을까요?",
                   "<strong>네.</strong> 강의에 왔다가 학창 시절의 비올라를 다시 잡고 단원이 된 분도 "
                   "있습니다."),
                  ("음악회는 몇 번 했나요?",
                   "정식 음악회는 <mark>네 번입니다</mark>. 첫 음악회는 2024년 3월 Dalgan Park, 가장 "
                   "최근은 2025년 성탄입니다.")],
             record_h2="지금까지의 음악회.",
             record_lead="정식 음악회 네 번을 날짜, 행사, 장소와 함께 모았습니다.",
             join_h2="함께 연주해 주세요.",
             join_text="",
             join_btn="참여 문의하기",
             mail_subject="Letters Ensemble 참여",
             mail_fields=["이름", "악기", "연주해 온 기간", "마지막으로 연주한 때", "편한 요일과 시간"],
         )),
    dict(slug="concert-companion", pillar="learn", name="함께하는 음악여행",
         short="함께하는 음악여행",
         icon="ticket", vocab="공연 전 · 공연 중 · 공연 뒤",
         img=("proms-hall.jpg", 1400, 933, "BBC 프롬스 공연 중 객석 높은 곳에서 본 로열 앨버트 홀. 불 밝힌 무대의 오케스트라와 가득 찬 객석, 빛줄기, 천장의 음향 반사판"),
         line="혼자 가기 어려운 공연장에 <mark>소그룹으로</mark> 함께 갑니다.",
         page=dict(
             lead="혼자 공연장에 가기 망설여지는 분을 위한 프로그램입니다. 미리 준비하고, <mark>함께 가고</mark>, "
                  "다녀와서 이야기합니다.",
             # 창립자가 BBC 프롬스 객석에서 찍은 사진. 프롬스 단체 관람 기록은 없으므로 누구의 시선인지
             # 밝힌다. 연월은 원본 영상의 촬영일(Andrew, 2026-10-01)
             cap=("BBC 프롬스, 로열 앨버트 홀", "런던 · 2023년 9월 · 사진: 창립자, 객석에서"),
             room_h2="객석에서 본 공연장.",
             glance=[("대상", "혼자서는 공연장에 가기 어려운 분"),
                     ("장소", "더블린의 공연장"),
                     ("언제", "함께 갈 공연이 생기면"),
                     ("준비물", "음악 지식이 없어도 됩니다")],
             now=("메일로 안내", "메일을 주시면 다음 음악여행을 알려 드립니다."),
             how_h2="공연 전과 공연 중, 그리고 공연 뒤.",
             steps=[("미리 준비하기",
                     "더블린의 공연을 고릅니다. 어떤 곡인지, 공연장에서는 어떻게 하는지 미리 알아봅니다."),
                    ("함께 가기", "소그룹으로 함께 가고, 공연 중에도 곁에서 안내합니다."),
                    ("다녀와서 나누기", "들은 것을 함께 이야기합니다. <mark>정답은&nbsp;없습니다</mark>.")],
             expect_h2="첫 음악여행 전에.",
             faq=[("어떤 공연을 안내했나요?",
                   "국립 콘서트홀 인터내셔널 시리즈와 국립 교향악단, TU Dublin 필하모닉 같은 공연입니다."),
                  ("몇 명이 함께 가나요?",
                   "2025년 12월에는 <mark>여섯 명이</mark> 국립 콘서트홀 음악회에 함께 갔습니다."),
                  ("아일랜드에 온 지 얼마 안 됐어요. 괜찮을까요?",
                   "<strong>네.</strong> 아일랜드에 처음 온 분도 반기고, <mark>영어와 한국어로</mark> 진행합니다.")],
             record_h2="지금까지 안내한 공연.",
             record_lead="안내한 공연과 함께 간 음악회를 날짜순으로 모았습니다.",
             join_h2="음악여행에 함께하세요.",
             join_text="",
             join_btn="음악여행 문의하기",
             mail_subject="함께하는 음악여행",
             mail_fields=["이름",
                          "편한 요일과 시간",
                          "듣고 싶은 음악 (선택)",
                          "참여에 도움이 필요한 점 (선택)",
                          "편한 언어: 영어 또는 한국어"],
         )),
]


# 쪽마다 메일은 화면에 적은 항목 그대로 만든다(QA40-02: 클래스와 음악여행의 메일에 한 줄이 빠져
# 있었다). 찾아가는 음악회는 MAIL_INVITE를 쓴다.
for _p in PROGRAMMES_DATA:
    _g = _p["page"]
    if "mail_subject" in _g:
        _g["mail"] = _mail(_g["mail_subject"], _fields(_g["mail_fields"]))


# ---------------------------------------------------------------------------
# 홈
# ---------------------------------------------------------------------------

# the five, under Programmes in the header (layout.PROG_MENU)
PROG_MENU["ko"][:] = [(q["slug"], q["name"], q["page"].get("live", False)) for q in PROGRAMMES_DATA]

HOME = dict(
    hero=dict(
        eyebrow="공동체 음악 · 아일랜드 더블린",
        title=["클래식 음악을,", "<em>모두에게.</em>"],
        # 제목 아래는 마스터 태그라인(Andrew, 2026-10-02 저녁). 바닥글과 같은 layout.STR에서 가져온다.
        # 태그라인은 번역하지 않는다(06 §5, 키트 27)
        cta=("#programmes", "프로그램 보기"),
        more=("get-involved.html#invite", "음악회 초청"),
        img=("hero-outreach.jpg", 1800, 1350,
             "아일랜드 국기와 클로버로 꾸민 홀에서 앉아 연주하는 현악 연주자 네 명과 지휘자"),
        cap=("Letters Ensemble", "성 파트리치오 축일 음악회"),
    ),
    # 함께하는 길을 연주회 프로그램의 차례처럼(상자도 색도 없이). 대부분은 무언가에
    # 참여하러 오므로 참여가 맨 앞이다
    progs=dict(
        label="우리가 하는 일",
        h2="프로그램 다섯 가지.",
        lead="셋은 함께 배우는 자리, 둘은 찾아가 연주하는 자리입니다.",
        # 카드가 다루지 않는 두 길을 문 두 개로(Andrew, 2026-10-03: 문장 속 링크는 동작으로 읽히지
        # 않았다). 라벨은 함께하기의 문과 같고, 제목은 그 길 끝의 동작이다. CMFE Artists는 계획이라
        # 지금 열린 것은 참여 신청뿐(키트 27 메시지 3, parts.door_pair)
        others=[("get-involved.html#play", "예술가", "참여 신청 보내기",
                 "분야를 가리지 않고 언제든 받습니다."),
                ("get-involved.html#board", "자원봉사자", "창립 이사회에 참여하기",
                 "독립된 이사회의 첫 이사를 찾습니다.")],
    ),
    # 키트 27 ①을 세 부분으로 나눠 답이 드러나게. 더블린 대신 아일랜드(Andrew,
    # 2026-10-01). 필요를 말하는 문장이지 활동 범위가 아니다(「아일랜드 전역」 금지)
    why=dict(
        label="이 일을 하는 이유",
        premise="아일랜드에는 음악회를 그리워하고, 지금도 음악이 필요한 분이 많습니다.",
        reasons=["<mark>요양원에</mark> 계신 분이 있습니다.",
                 "집 밖에 <mark>잘 나가지 못하는</mark> 분도 있습니다.",
                 "이 나라에 <mark>온 지 얼마 되지 않아</mark> 어디서 시작할지 모르는 분도 있습니다."],
        resolve="그래서 <em>저희가 찾아갑니다.</em>",
        link="단체 소개",
    ),
    numbers=dict(
        label="기록",
        sr="숫자로 보기",
        figs=[(40, "강의와 연주", "2024년부터", True),
              (N_PLACES, "연주하고 가르쳐 온 곳", "2024년부터", False),
              (4, "연주한 나라: 아일랜드·프랑스·영국·한국", "2024년부터", False)],
        forty=dict(talks="강의 {n}회", perf="연주 {n}회",
                   period="2026년 9월까지의 기록, 점 하나에 하나씩"),
        note="창립자가 South Dublin Live 2026에 선정됐습니다.",
        link=("news.html#record", "연도별 기록 보기"),
    ),
)


# ---------------------------------------------------------------------------
# 소개. #founder #run #places #identity는 옛 주소가 가리키는 앵커다.
# ---------------------------------------------------------------------------

ABOUT_T = dict(
    glance_sr="한눈에",
    head=dict(
        eyebrow="소개",
        title=["단체 소개."],
        lead="더블린에서 활동하는 공동체 음악 단체입니다. <mark>음악이 필요한 곳을</mark> 찾아가 연주하고 가르칩니다.",
        img=("columban-ensemble.jpg", 1400, 1050,
             "노란 방에서 악기를 든 Letters Ensemble 현악 연주자 네 명과 지휘자"),
        cap=("Letters Ensemble", "성 골롬반 외방선교 수녀회, 위클로 주 · 2024년 11월"),
    ),
    glance=[("창립", "2024년 1월", "아일랜드 더블린"),
            ("운영하는 것", "프로그램 다섯", "배움과 나눔"),
            ("연주한 곳", "4개국", "아일랜드·프랑스·영국·한국"),
            ("지위", "비영리 공동체 음악 단체", "보증유한회사(CLG) 설립 준비 중")],
    story=dict(
        label="지나온 길",
        h2="2024년부터.",
        text=["2024년 1월 더블린에서 Letters Ensemble과 함께 시작했습니다. 첫 강의에는 여섯 명이 왔습니다.",
              "2026년 9월까지 기록된 강의와 연주는 <mark>마흔 번입니다</mark>. 은퇴한 Presentation 수녀님 일곱 분과 "
              "함께한 파일럿에서 Mulhuddart의 리코더&nbsp;클래스가 나왔습니다."],
        link="전체 연표 보기",
    ),
    founder=dict(
        # 강의 사진의 화면에 알아볼 수 있는 다른 분들이 있어, 연주하는 사진으로 바꿨다(2026-10-01)
        img=("founder-playing.jpg", 1050, 1400, "Tallaght University Hospital 경당에서 클라리넷을 연주하는 김서현"),
        cap=("클라리넷", "Tallaght University Hospital 경당 · 2026년 8월 · 사진: Tallaght University Hospital"),
        label="창립자",
        name='<span class="nm">Andrew Seohyeon Kim</span><span class="sr-only">, </span><span class="founder-ko">김서현</span>',
        role="창립자·예술감독",
        line="더블린의 클라리넷·오르간 연주자이자 공동체 음악가입니다.",
        facts=[("학력", "TU Dublin Conservatoire 연주 전공 학사(BMus Hons)"),
               ("맡은 일", "Our Lady of Dolours 성당 음악감독, 더블린 Dolphin&rsquo;s Barn"),
               ("리코더 파일럿", "은퇴한 Presentation 수녀님 일곱 분과 10주, 일곱 분 모두 끝까지")],
    ),
    run=dict(
        label="운영 방식",
        h2="비영리 공동체 음악 단체입니다.",
        # 키트 27의 지위 문장 그대로
        lead=STATUS,
        links=[("get-involved.html#board", "창립 이사회 알아보기"),
               ("contact.html#privacy", "개인정보를 다루는 방식")],
        items=[("운영:",
                "법인이 등록되면 독립된 자원봉사 이사회가 맡습니다. 지금 첫 이사를 모집하고 있습니다."),
               ("돈:",
                "아직은 후원을 요청하거나 받지 않습니다. 저희는 절대 <mark>개인 계좌로</mark> 돈을 보내 달라고 하지 "
                "않습니다."),
               ("사진:",
                "연주자와 악기, 빈 공간을 싣습니다. 그 밖에 알아볼 수 있는 분은 서면 동의가 있을 때만 "
                "싣습니다."),
               ("보험:", "공공배상책임보험에 들어 있습니다. 증서는 요청 시 보여 드립니다.")],
    ),
    places=dict(
        label="장소",
        h2="연주하고 가르쳐 온 곳.",
        # 08 §2: 참가자에게 공연을 안내하고 단체 관람을 준비했다
        lead=f"4개국 <mark>{N_PLACES}곳을</mark> 종류별로 모았습니다.",
        # 모두 기록에 있는 곳(2026-10-01 검토). 곳의 성격으로 묶고 지역을 붙였다. 개수는 계산한다
        groups=PLACES,
        map=dict(
            labels={"dublin": ("더블린", None), "meath": ("미스 주", None),
                    "wicklow": ("위클로 주", "Magheramore"), "westmeath": ("웨스트미스 주", "Dysart")},
            count="{n}곳",
            aria="아일랜드 섬 지도에 연주하고 가르쳐 온 아일랜드 안의 곳을 표시했습니다: 더블린 열네 곳, 미스 주 "
                 "두 곳, 위클로·웨스트미스 주에 한 곳씩.",
            caption="아일랜드 안: 더블린과 세 주. 해외: 프랑스, 영국, 한국.",
        ),
    ),
    identity=dict(
        label="이름",
        h2="<em>Everyone</em>이 금색인 이유.",
        text="로고의 &lsquo;for&rsquo;는 작고, &lsquo;Everyone&rsquo;은 크고 금색입니다. "
             "그 낱말이 저희가 지켜야 할 약속입니다.",
        alt="Classical Music for Everyone 로고: 높은음자리표 옆 워드마크, &lsquo;Everyone&rsquo;이 "
            "크고 금색으로 놓여 있습니다",
    ),
)


# ---------------------------------------------------------------------------
# 프로그램
# ---------------------------------------------------------------------------

PROGRAMMES_T = dict(
    head=dict(
        eyebrow="프로그램",
        title=["프로그램."],
        lead="대부분 <mark>경험 없이</mark> 오셔도 됩니다. 메일을 주시면 시작하는 방법을 알려 드립니다.",
    ),
    list_sr="다섯 프로그램",
    # 키트 27 메시지 3: 계획은 계획으로, 지금 열린 것 하나와 함께
    artists=dict(
        label="예술가라면",
        text='분야와 상관없이 <a class="link" href="get-involved.html#play">언제든 신청</a>하세요. '
             "CMFE Artists는 2027년 계획입니다.",
    ),
)


# ---------------------------------------------------------------------------
# 함께하기
# ---------------------------------------------------------------------------

GET_INVOLVED_T = dict(
    head=dict(
        eyebrow="함께하기",
        title=["함께하는 방법."],
        lead="어느 길이든 <mark>메일 한 줄로</mark> 시작하시면 됩니다.",
    ),
    ways_label="네 가지 길",
    # 네 개의 문(2026-10-02 밤): 누구의 길인지, 그 길이 닿는 섹션의 제목, 거기 있는 것(parts.doors)
    ways=[("programmes.html", "누구나", "프로그램에 참여하기", "다섯 프로그램"),
          ("#invite", "공간", "음악회 초청하기", "준비할 것"),
          ("#play", "예술가", "함께 연주하기", "예시 프로그램"),
          ("#board", "자원봉사자", "창립 이사회에 참여하기", "이사회 역할")],
    alt=dict(or_write="또는", email=EMAIL, tel="+353 83 078 0635", tel_href="+353830780635"),
    invite=dict(
        label="파트너 공간",
        h2="음악회를 초청해 주세요.",
        lead="요양시설과 병원, 수도 공동체와 본당, 커뮤니티 센터에서 저희를 <mark>초청하실</mark> 수 있습니다.",
        pair_labels=("준비해 주실 것", "저희가 챙겨 갈 것"),
        pairs=[("음악회",
                ["연주할 방 하나", "가능한 날짜", "연락할 담당자 한 분"],
                ["연주자와 악기", "보면대", "듣는 분들께 맞춘 곡"]),
               # 그림의 고리 안에 들어가는 이름: 영문처럼 곳은 빼고(클래스 쪽과 히어로가 곳을 말한다)
               ("리코더 클래스",
                ["매주 쓸 따뜻한 방 하나", "담당자 한 분", "동네에 알리는 일"],
                ["빌려 드릴 리코더", "악보와 수업, 재원에 따라"])],
        href=MAIL_INVITE, btn="음악회 초청하기", more="진행 방식 보기",
    ),
    # Andrew, 2026-10-02: 분야를 가리지 않고 언제든 자유롭게 관심만 받는다. 신원조회는 공연장에 따라,
    # 예시 프로그램은 기록(ledger.py)에서
    play=dict(
        label="CMFE Artists",
        h2="함께 연주하기.",
        lead="<mark>분야를 가리지 않고</mark> 연주자·예술가와 언제든 함께할 준비가 되어 있습니다.",
        facts=[("대상", "학생·신진·아마추어·전문 예술가"),
               ("방법", "자기소개 몇 줄과 연주나 작업 링크"),
               ("Garda 신원조회", "공연장에 따라 필요할 수 있습니다"),
               ("<span class=\"sr-only\">2027년 </span>계획", "CMFE Artists: 신진 연주자가 사례를 받고 멘토와 함께하는 연주")],
        examples_label="예시 프로그램",
        examples=[("교회의 가을 음악회", "소프라노·해금·클라리넷·피아노", "2026년 9월"),
                  ("요양시설의 성탄", "클라리넷과 현악 3중주", "2025년 12월"),
                  ("노숙인 쉼터", "오르간과 클라리넷", "2025년 7월"),
                  ("수도 공동체의 성 파트리치오 축일", "국악 앙상블과 클라리넷", "2025년 3월")],
        note='연주자라면 <mark>누구나</mark> <a class="link" href="programmes/letters-ensemble.html">Letters '
             "Ensemble</a>에도 함께하실 수 있습니다.",
        href=_MAIL_EOI, btn="참여 신청 보내기",
    ),
    support=dict(
        label="함께 세우기",
        board=dict(
            h2="창립 이사회에 함께해 주세요.",
            lead="법인이 등록되면 이 <mark>독립된 자원봉사</mark> 이사회가 단체를 운영합니다.",
            # 그림의 칸 이름은 「역할」(영문 Roles): 「자리」는 의자 수로 읽힐 수 있다(총괄 디자이너 v2, R19)
            facts=[("역할", "의장, 재무, 사무, 세이프가딩·돌봄, 지역사회"),
                   ("조건", "무보수, 합당한&nbsp;실비&nbsp;지급")],
            # 같은 역할을 그림의 탁자 둘레에 하나씩(parts.table). 자리 수는 말하지 않는다
            roles=["의장", "재무", "사무", "세이프가딩·돌봄 담당", "지역사회 담당"],
            href=_MAIL_BOARD, btn="이사회 문의하기",
        ),
        gifts="아직은 후원을 요청하거나 받지 않습니다.",
    ),
)


# 후원(Friends, 음악회 후원, 후원자에게 드리는 약속)은 닫혀 있다. 문안은 공개 저장소
# 밖의 giving_ko.py에 있고, layout.OPEN_GIVING이 True일 때만 읽는다.
if OPEN_GIVING:
    import giving_ko
    giving_ko.apply(globals())

# ---------------------------------------------------------------------------
# 프로그램 쪽 (programmes/<slug>.html), 2026-10-01부터. 쪽마다의 문안은 위 프로그램의
# `page`에 있고, 여기는 다섯 쪽이 함께 쓰는 이름표다. 쪽의 기록은 ledger.py에서 온다.
# ---------------------------------------------------------------------------

PROGRAMME_T = dict(
    crumbs_label="현재 위치", crumb="프로그램",
    how_label="진행 방식", expect_label="미리 알아 두실 것", record_label="기록",
    join_label="함께하기", others_label="다른 프로그램", all_label="프로그램 다섯 가지 모두 보기",
    room_label="그 자리에서", room_h2="음악이 있는 곳.",
    how_join="참여하는 방법",
    video_h="영상", video_label="영상: {name}", play="영상 재생", watch="{service}에서 보기",
    people="{n}명",
    mail_hint="한 줄이면 됩니다. 이런 것을 적어 주시면 도움이 됩니다:",
    or_write="또는", email=EMAIL, tel="+353 83 078 0635", tel_href="+353830780635",
    strip=dict(aria="이 프로그램의 기록 {n}건을 2024년부터 2026년까지 달마다 표시했습니다.",
               learn="배움", share="나눔", bar="막대는 여러 달에 걸친 것입니다.",
               dot={"getting-to-know": "점 하나가 강의 하나입니다.", "outreach-concerts": "점 하나가 음악회 하나입니다.",
                    "recorder-ensemble": "점 하나가 하루입니다.", "letters-ensemble": "점 하나가 음악회 하나입니다.",
                    "concert-companion": "점 하나가 공연 하나입니다."}),
    earlier="이전 기록 {n}건 보기",
    att=dict(h3="참석 인원", lead="참석 인원이 기록된 강의마다 몇 분이 오셨는지 보여 줍니다.",
             aria="참석 인원이 기록된 강의 {n}회: 적게는 {lo}명, 많게는 {hi}명.",
             people="{n}명"),
)

PROGRAMME_PAGES = {_p["slug"]: P.programme_page(PROGRAMME_T, _i, _p, PROGRAMMES_DATA, PILLARS, L)
                   for _i, _p in enumerate(PROGRAMMES_DATA)}

INDEX = P.home(HOME, PROGRAMMES_DATA, PILLARS, L)
ABOUT = P.about(ABOUT_T, L)
PROGRAMMES = P.programmes(PROGRAMMES_T, PROGRAMMES_DATA, PILLARS)
GET_INVOLVED = P.get_involved(GET_INVOLVED_T, _ico)


# ---------------------------------------------------------------------------
# 소식·기록
# ---------------------------------------------------------------------------

NEWS_T = dict(
    head=dict(
        eyebrow="소식·기록",
        title=["새 소식과 지나온 기록."],
        # 2024년부터 40+ · 2026년 9월까지 기록된 40 = 17 + 20 + 1 + 2 (03 §1)
        lead="새 소식과 2024년부터 <mark>해 온 강의와 연주</mark>, 사진을 모았습니다.",
    ),
    latest_sr="새 소식",
    latest=[("이사회", "2026년 가을",
             "창립 이사회를 꾸립니다",
             "보증유한회사 설립을 준비하며 자원봉사 이사를 찾습니다.",
             "get-involved.html#board",
             "이사회 역할 보기"),
            ("클래스", "2026년 가을",
             "커뮤니티 리코더 앙상블 클래스",
             "매주 수요일 저녁 7시~8시, Mulhuddart에서 열립니다.",
             "programmes/recorder-ensemble.html",
             "클래스 안내"),
            ("음악회", "2026년 9월 19일",
             "가을 음악회",
             "Ranelagh에서 소프라노, 해금, 클라리넷, 피아노로 열었습니다.",
             "programmes/outreach-concerts.html#record",
             "음악회 기록 보기")],
    chart=dict(
        label="기록",
        h2="마흔 번, 연도별로.",
        lead="기록된 강의와 연주마다 무엇을 어디서 했는지 적었습니다.",
        figs=[(17, "강의", "talk"),
              (20, "찾아가는 음악회", "perf"),
              (1, "파일럿 음악회", "perf"),
              (2, "South Dublin Live 2026 음악회", "perf")],
        period="2024년 1월~2026년 9월",
        year_count="강의와 연주 {n}회",
        year_talks=("강의 {n}회", "강의 {n}회"),
        year_perf=("연주 {n}회", "연주 {n}회"),
        year_more="{y}년 {n}건 모두 보기",
        row_talk="강의",
        row_perf="연주",
    ),
    timeline=dict(
        label="연표",
        h2="자라 온 길.",
        years=[("2024", [("1월", "시작",
                          "더블린에서 Letters Ensemble과 함께 창립했습니다. 첫 강의에 <mark>여섯 명이</mark> 왔습니다."),
                         ("한 해 동안", "더블린 밖으로",
                          "미스·위클로 주와 런던, 파리, 대구에서 연주했습니다.")]),
               ("2025", [("한 해 동안", "돌봄의 자리로",
                          "주간 돌봄 서비스와 노숙인 쉼터, 요양시설에서 연주했습니다."),
                         ("가을", "공연을 안내합니다",
                          "참가자에게 공연을 안내하고 단체 관람을 준비하기 시작했습니다."),
                         ("10월", "리코더 파일럿을 준비합니다",
                          "은퇴한 Presentation 수녀님 <mark>일곱 분과</mark> 리코더 앙상블 준비를 시작했습니다."),
                         ("12월", "국립 콘서트홀에서",
                          "강의 열다섯 번째 모임은 함께 들은 음악회였습니다.")]),
               ("2026", [("1월~4월", "일곱 분 모두 끝까지",
                          "Warrenmount에서 10주 동안 연습했습니다. <mark>부활 음악회는</mark> Clondalkin "
                          "Lodge에서 무대에 올랐습니다."),
                         ("8월", "Tallaght에서 두 번",
                          "창립자가 South Dublin Live에 선정됐습니다. 병원과 Rua Red에서 연주했습니다."),
                         ("9월", "Ranelagh의 가을 음악회", "Methodist Centenary Church에서 열었습니다."),
                         ("가을", "일반에 열린 클래스",
                          "<mark>파일럿에서 나온</mark> 클래스를 Mulhuddart에서 엽니다.")])],
    ),
    gallery=dict(
        label="사진",
        h2="그 자리에서.",
        lead="최근 사진부터 실었습니다.",
        # 새것부터, 한 장의 밀착 인화처럼: 사진마다 제 비율로, 참인 설명과 함께
        rows=[
            (("tuh-trio.jpg", 1236, 787,
              "Tallaght University Hospital 아트리움의 소프라노·피아노·클라리넷"),
             "아트리움 · Tallaght University Hospital · 2026년 8월 · 사진: Tallaght University Hospital"),
            (("tuh-atrium.jpg", 1400, 1052, TUH_CHAPEL_ALT),
             "경당 · Tallaght University Hospital · 2026년 8월 · 사진: Tallaght University Hospital"),
            (("tuh-haegeum.jpg", 1400, 934, "병원 아트리움에서 해금을 연주하는 연주자"),
             "해금 · Tallaght University Hospital · 2026년 8월 · 사진: Tallaght University Hospital"),
            (("ruared-trio.jpg", 1400, 933, "Rua Red 무대에 함께 선 클라리넷 연주자, 소프라노, 피아니스트"),
             "클라리넷·소프라노·피아노 · Rua Red · 2026년 8월 · 사진: Ben Ryan / SDCC"),
            (("care-christmas.jpg", 1400, 1050, CARE_ALT),
             "클라리넷과 현악 3중주 · 2025년 성탄"),
            (("score-stand.jpg", 1050, 1400, "보면대 위 파트 악보 너머로 연습하는 현악 3중주"),
             "음악회를 앞두고 · 2025년 성탄"),
            (("recorders.jpg", 1343, 1400, RECORDERS_ALT),
             "리코더 · 2025년 11월"),
            (("church-aisle.jpg", 1050, 1400, "웨스트미스 주 본당 제대 앞에서 들어 보인 클라리넷"),
             "제대 앞의 클라리넷 · Dysart, 웨스트미스 주 · 2025년"),
            (("columban-ensemble.jpg", 1400, 1050,
              "노란 방에서 악기를 든 Letters Ensemble 현악 연주자 네 명과 지휘자"),
             "Letters Ensemble · 성 골롬반 외방선교 수녀회, 위클로 주 · 2024년 11월"),
            (("dalgan-hall.jpg", 1400, 1050, "음악회를 앞두고 의자와 보면대를 놓아 둔, 아직 아무도 없는 홀"),
             "음악회를 앞둔 홀 · Dalgan Park, 미스 주 · 2024년 3월"),
            (("hero-outreach.jpg", 1800, 1350,
              "아일랜드 국기와 클로버로 꾸민 홀에서 앉아 연주하는 현악 연주자 네 명과 지휘자"),
             "Letters Ensemble · 성 파트리치오 축일 음악회"),
            (("letters-ensemble.jpg", 1400, 1050, "아일랜드 국기와 클로버로 꾸민 홀에서 악기를 들고 선 현악 연주자 네 명과 지휘자"),
             "Letters Ensemble · 현악 연주자 네 명과 지휘자"),
            (("two-clarinets.jpg", 1050, 1400, "피아노 뚜껑 위에 놓인 클라리넷 두 대"), "피아노 위의 클라리넷 두 대"),
        ],
    ),
)

NEWS = P.news(NEWS_T, L, PROGRAMMES_DATA)


# ---------------------------------------------------------------------------
# 문의, 개인정보 고지와 함께(키트 06: 웹사이트의 개인정보 고지)
# ---------------------------------------------------------------------------

CONTACT_T = dict(
    head=dict(
        eyebrow="문의",
        title=["메일 주세요."],
        lead="주제를 고르시거나, 바로 메일을 쓰셔도 됩니다. <mark>모든 메일에</mark> 답장합니다.",
    ),
    # 연락 양식 하나, 주제를 고른다(Andrew, 2026-10-02 저녁). 메일 양식이라 보내는 분의 메일 앱이
    # 제목과 내용을 채운 채 열리고, 이 사이트로는 아무것도 지나가지 않는다.
    # 리서치(2026-10-02): 고르기 목록이 아니라 라디오(GOV.UK), 이름은 subject(값은 지금의 메일 제목),
    # 내용은 body 하나, 필수 칸 없음, 버튼은 무슨 일이 일어나는지 말한다. 한글 한 음절이 주소에서 9자가
    # 되므로 짧게(약 200음절).
    form=dict(
        h2="문의 양식",
        topic_label="어떤 일로 연락하시나요?",
        topics=[("part", "프로그램 참여 문의", "프로그램 참여", ["관심 있는 프로그램", "연락받을 방법"]),
                ("venue", "찾아가는 음악회 초청", "공간: 음악회 초청", INVITE_FIELDS),
                ("artist", "CMFE Artists 참여 신청", "예술가: 참여 신청", EOI_FIELDS),
                ("board", "창립 이사회 문의", "창립 이사회", ["관심 있는 역할", "자기소개 몇 줄"]),
                ("data", "개인정보 요청", "내 정보 보기·고치기·지우기", ["보기, 고치기, 지우기 중 원하시는 것"]),
                ("other", "Classical Music for Everyone 문의", "그 밖의 일", [])],
        helps="이런 것을 적어 주시면 도움이 됩니다:",
        general="몇 줄이면 됩니다. 주제를 고르시면 무엇을 적으면 좋을지 보여 드립니다.",
        message_label="보내실 내용",
        button="이메일 앱에서 열기",
        # 「짧게」는 늘 버튼 옆에(총괄 디자이너 v2: 한글 한 음절이 주소에서 9자, 약 2,000자를 넘으면 안 열릴 수 있다)
        note="메일 앱에서 마저 쓰고 보내실 수 있으니, 여기에는 짧게 적어 주세요. 메일 앱이 열리지 않으면 이 주소로 보내 주세요:",
    ),
    direct_label="바로 연락하기",
    email=EMAIL,
    email_href=_mail("Classical Music for Everyone 문의"),
    tel="+353 83 078 0635",
    tel_href="+353830780635",
    details_label="기본 정보",
    details_h2="어디에 있고, 누가 답하나요?",
    # 보험: 증서 보유(2026-10-01 확인). Garda 신원조회는 마친 뒤에 쓴다.
    # 찾아가는 곳(Andrew, 2026-10-02 밤): 범위가 아니라 필요를 말한다. 연주해 온 주는 소개 쪽 기록과
    # areaServed에 남는다. 「아일랜드 전역」 금지. 라벨이 「활동 지역」이면 범위를 주장하는 말로 읽힌다
    details=[("거점", "아일랜드 더블린"),
             ("찾아가는 곳", "음악이 필요한&nbsp;곳 어디든지"),
             ("언어", '한국어 · <span lang="en">English</span>'),
             ("보험", "공공배상책임보험에 들어 있습니다. 증서는 요청 시 보여 드립니다."),
             # 서명처럼 이름 줄, 그다음 역할 줄(R23: 노트북 폭에서 이름이 「Andrew / Seohyeon Kim」으로 갈렸다)
             ("답하는 사람", '<span class="sl">Andrew Seohyeon Kim(김서현)</span> '
                           '<span class="sl">창립자·예술감독</span>')],
    privacy=dict(
        label="개인정보 처리방침",
        h2="보내 주신 정보는 이렇게 다룹니다.",
        intro="어떤 정보를 받고 어떻게 쓰는지 적었습니다. 2026년 10월 5일 갱신.",
        # 연락 양식은 메일 양식이라 스스로 보내지 않는다(2026-10-02)
        none=[("입력 양식", "하나, 메일&nbsp;앱을 열기만 함"), ("쿠키", "저희 것은 없음"), ("방문 분석", "없음"),
              ("광고", "없음")],
        blocks=[("정보를 책임지는 곳",
                 "p",
                 '<span class="brandname">Classical Music for Everyone</span>, 더블린의 비영리 공동체 음악 '
                 '단체입니다. 개인정보에 관한 문의는 <a class="link" '
                 'href="mailto:sby05034@gmail.com">sby05034@gmail.com</a>으로 보내 주세요.',
                 ""),
                ("메일을 보내 주시면",
                 "list",
                 ["답장하고 요청하신 일을 <mark>하는 데만 씁니다</mark>.",
                  "<mark>팔지 않으며</mark>, 아래 업체만 저희를 대신해 다룹니다.",
                  "연주자·예술가 정보는 연주 기회를 드리려고 최대 2년 보관합니다.",
                  "도움이 필요한 점은 원하실 때만 적어 주세요."],
                 ""),
                ("함께 다루는 곳",
                 "rows",
                 [("GitHub", "이 사이트가 있는 곳. 보안을 위해 IP 주소를 기록합니다."),
                  ("Google Fonts", "글꼴. 불러올 때 IP 주소를 받습니다."),
                  ("Google", "저희 이메일."),
                  ("YouTube", "클래스 영상. 재생을 누르면 IP 주소를 받고 쿠키를 둘 수 있습니다.")],
                 "이 업체들은 EU가 승인한 보호 장치에 따라 유럽경제지역 밖에서 정보를 다룰 수 있습니다."),
                ("요청하실 수 있는 것",
                 "list",
                 ["저희가 가진 정보를 보거나 고치거나 지우기",
                  "사용을 멈추게 하거나 사용에 반대하기",
                  "사본 받기"],
                 '<mark>언제든</mark> 메일로 요청하실 수 있습니다. 답에 만족하지 못하시면 아일랜드 <a class="link" '
                 'href="https://www.dataprotection.ie/">개인정보보호위원회(Data Protection '
                 "Commission)</a>에 민원을 내실 수 있습니다.")],
    ),
)

CONTACT = P.contact(CONTACT_T)
