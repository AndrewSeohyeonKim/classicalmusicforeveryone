# -*- coding: utf-8 -*-
"""한국어 페이지 내용. 사실관계는 정본 세트(00_최종본, 2026-08-27)를 따릅니다.

이 파일의 원칙: 한 섹션당 두세 문장. 그보다 길어지는 설명은 문단이 아니라
도식·표·캡션으로 옮깁니다.
"""

import diagrams as dg

L = "ko"

# ---------------------------------------------------------------------------

STATS = """<div class="stats">
  <div class="wrap stats-grid">
    <div class="stat"><b>40+</b><span>진행한 세션과 연주</span></div>
    <div class="stat"><b>5</b><span>운영 중인 프로그램</span></div>
    <div class="stat"><b>20+</b><span>닿은 공간과 기관</span></div>
    <div class="stat"><b>4</b><span>연주한 나라</span></div>
    <div class="stat"><b>143</b><span>강의 누적 참석</span></div>
  </div>
</div>"""

WHATS_ON = """<div class="grid grid-2 stagger">
  <div class="notice">
    <span class="tag tag-live">모집 중</span>
    <h3>리코더 앙상블 — Mulhuddart</h3>
    <p class="small">완전 초보를 위한 12주. 경험도, 악보 읽는 능력도 필요하지 않습니다.</p>
    <dl>
      <dt>장소</dt><dd>Mulhuddart Community Centre, Dublin 15</dd>
      <dt>요일</dt><dd>수요일 저녁 7:00–8:00</dd>
      <dt>개강</dt><dd>2026년 9월 9일</dd>
      <dt>수강료</dt><dd>무료</dd>
    </dl>
    <div class="btn-row"><a class="btn btn-primary" href="get-involved.html">참여 방법 <span class="arrow">→</span></a></div>
  </div>
  <div class="notice">
    <span class="tag">다가오는 연주</span>
    <h3>An Autumn Concert · 가을 음악회</h3>
    <p class="small">소프라노·해금·클라리넷·피아노 — 쇼팽, 피에르네, 슈포어, 슈베르트와 한국 가곡.</p>
    <dl>
      <dt>장소</dt><dd>Methodist Centenary Church, Ranelagh, Dublin 6</dd>
      <dt>일시</dt><dd>2026년 9월 19일 토요일 오후 5시</dd>
      <dt>입장</dt><dd>무료 · 후원금은 감사히 받습니다</dd>
    </dl>
    <div class="btn-row"><a class="btn btn-quiet" href="news.html">전체 일정 <span class="arrow">→</span></a></div>
  </div>
</div>"""

CTA = """<section class="band-inverse">
  <div class="wrap narrow center reveal">
    <h2 class="h-lg">당신을 위한 자리가 있습니다.</h2>
    <p class="lead mt-2">
      처음 악기를 배우든, 들으러 오든, 함께 연주하든, 공간을 열어 주든 —
      한 줄이면 시작됩니다.</p>
    <div class="btn-row center-row">
      <a class="btn btn-accent" href="get-involved.html">참여하기 <span class="arrow">→</span></a>
      <a class="btn btn-on-dark" href="support.html">후원하기</a>
    </div>
  </div>
</section>"""


# ---------------------------------------------------------------------------
# 홈
#
# 순서에는 이유가 있습니다. 동종 단체를 따라, 방문자에게 무엇을 부탁하기 전에
# 단체가 무엇을 운영하는지를 먼저 말합니다. 다섯 프로그램은 동등합니다 —
# 더 큰 카드도, 먼저 칠한 색도, '대표'라는 표기도 두지 않습니다.
# ---------------------------------------------------------------------------

INDEX = f"""<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow lift lift-1">커뮤니티 음악 · 아일랜드 더블린</p>
      <h1><span class="line lift lift-1">클래식 음악을,</span><span class="line lift lift-2"><em>모두에게.</em></span></h1>
      <p class="lead lift lift-3">듣는 데서 그치지 않고 직접 연주하도록 가르칩니다.
         그리고 클래식 음악이 좀처럼 닿지 않는 곳으로 찾아갑니다.</p>
      <div class="btn-row lift lift-4">
        <a class="btn btn-primary" href="programmes.html">하는 일 보기 <span class="arrow">→</span></a>
        <a class="btn btn-quiet" href="get-involved.html">참여하기</a>
      </div>
    </div>
    <figure class="lift lift-3">
      <div class="photo photo-3x2">
        <img src="images/hero-outreach.jpg" width="1800" height="1350"
             alt="커뮤니티 홀에서 열린 성 파트리치오 축일 음악회에서 연주하는 연주자들">
      </div>
      <figcaption>수도 공동체를 위한 성 파트리치오 축일 음악회 — Letters Ensemble.</figcaption>
    </figure>
  </div>
</section>

{STATS}

<section>
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">우리가 하는 일</p>
      <h2>다섯 프로그램, 두 축, 하나의 회로.</h2>
      <p>직접 연주하도록 가르치고, 공연장에 오기 어려운 분들을 찾아가 연주합니다.
         어느 한쪽만으로는 돌아가지 않습니다. 찾아간 방에서 다음 수업이 생기고,
         그 수업에서 다음 연주자가 나옵니다.</p>
    </div>
    <div class="legend reveal">
      <b>배움</b><span>한 학기, 한 번의 강의, 옆자리의 동행</span>
      <b class="b2">나눔</b><span>그 방으로 음악을 가져갑니다</span>
    </div>
    <div class="grid grid-5 stagger">
      <a class="prog" href="programmes/recorder-ensemble.html">
        <div class="photo photo-3x2"><img src="images/conducting.jpg" width="1400" height="933" alt="더블린의 한 커뮤니티 공간에서 진행하는 주간 수업"></div>
        <div class="prog-body">
          <span class="kicker">배움</span>
          <h3>리코더 앙상블 과정</h3>
          <p>완전 초보를 위한 한 학기, 마지막은 음악회로 끝납니다.</p>
          <div class="meta">주 1회 · 한 학기</div>
        </div>
      </a>
      <a class="prog" href="programmes/getting-to-know.html">
        <div class="photo photo-3x2"><img src="images/lecture-recital.jpg" width="1400" height="933" alt="진행 중인 강의·연주"></div>
        <div class="prog-body">
          <span class="kicker">배움</span>
          <h3>클래식 음악과 친해지기</h3>
          <p>사전 지식이 없는 분들을 위한 무료 강의·연주.</p>
          <div class="meta">17회 · 누적 143명</div>
        </div>
      </a>
      <a class="prog" href="programmes/concert-companion.html">
        <div class="photo photo-3x2"><img src="images/quartet-hall.jpg" width="1400" height="933" alt="밝은 홀에서 연주하는 앙상블"></div>
        <div class="prog-body">
          <span class="kicker">배움</span>
          <h3>함께하는 음악여행</h3>
          <p>혼자서는 가지 않을 공연에 소그룹으로 동행합니다.</p>
          <div class="meta">10회 동행 · 5명 안팎</div>
        </div>
      </a>
      <a class="prog" href="programmes/outreach-concerts.html">
        <div class="photo photo-3x2"><img src="images/care-christmas.jpg" width="1400" height="933" alt="성탄에 요양시설에서 연주하는 사중주"></div>
        <div class="prog-body">
          <span class="kicker">나눔</span>
          <h3>찾아가는 음악회</h3>
          <p>요양시설·본당·병원·쉼터로 실연을 가져갑니다.</p>
          <div class="meta">20회 · 15곳 이상</div>
        </div>
      </a>
      <a class="prog" href="programmes/letters-ensemble.html">
        <div class="photo photo-3x2"><img src="images/letters-ensemble.jpg" width="1400" height="933" alt="악기를 든 Letters Ensemble"></div>
        <div class="prog-body">
          <span class="kicker">나눔</span>
          <h3>Letters Ensemble</h3>
          <p>더블린에 사는 아마추어 연주자들이 매주 토요일 연습합니다.</p>
          <div class="meta">정식 음악회 4회 · 2024년 1월부터</div>
        </div>
      </a>
    </div>
    <div class="reveal mt-4">{dg.loop(L)}</div>
    <div class="btn-row reveal"><a class="btn btn-quiet" href="programmes.html">다섯 가지 자세히 보기 <span class="arrow">→</span></a></div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">지금 열려 있는 것</p>
      <h2>지금 참여할 수 있습니다.</h2>
      <p>모집 중인 수업 하나와 문이 열려 있는 음악회 하나. 둘 다 무료입니다.</p>
    </div>
{WHATS_ON}
  </div>
</section>

<section class="band-photo">
  <img src="images/church-concert.jpg" alt="" width="1400" height="1050">
  <div class="wrap narrow reveal">
    <p class="eyebrow">왜 이 일을 하는가</p>
    <h2 class="h-lg">존엄을 되돌려 주는 것은 듣는 일이 아니라
       직접 연주하는 일입니다.</h2>
    <p class="lead mt-3">
      클래식 음악은 문화적으로 풍요롭지만 여전히 많은 이에게 닿지 않습니다 —
      나이, 거동, 소득, 사는 곳, 혹은 그저 낯설다는 이유로. 요양시설과 병원, 쉼터,
      시골 본당은 관객이 없는 곳이 아닙니다. 가장 오래 기다려 온 관객이
      이미 있는 곳입니다.</p>
    <div class="btn-row"><a class="btn btn-on-dark" href="about.html">단체 소개 <span class="arrow">→</span></a></div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">신뢰의 근거</p>
      <h2>우리가 아닌 누군가가 값을 치렀습니다.</h2>
      <p>자원봉사로 운영하며 비영리 보증유한책임회사(CLG) 설립을 준비하고 있습니다.
         그 절차가 끝나기 전까지, 자선단체 등록번호 대신 내놓을 수 있는 것은 기록입니다.</p>
    </div>
    <div class="evidence stagger">
      <div><dl>
        <dt>공적 지원</dt>
        <dd>사우스더블린 카운티 의회 예술과가 <strong>South Dublin Live 2026</strong>에
            이 프로젝트를 선정했습니다. 첫 공적 위촉입니다.</dd>
      </dl></div>
      <div><dl>
        <dt>지지 서한</dt>
        <dd><strong>Rua Red</strong>, <strong>The Civic</strong>,
            <strong>Tallaght University Hospital</strong>의 지지 서한을 보유하고 있습니다.</dd>
      </dl></div>
      <div><dl>
        <dt>연주해 온 곳</dt>
        <dd><strong>네 나라</strong>—아일랜드·프랑스·영국·한국—의
            <strong>20곳 이상의 공간과 기관</strong>에서 연주했습니다.</dd>
      </dl></div>
    </div>
    <div class="quote reveal mt-4">
      <p>&ldquo;음악을 통해 그는 달리 고립감을 느낄 수 있는 이들에게 격려와 존엄,
         그리고 영적인 동행을 건넵니다.&rdquo;</p>
      <cite>더블린 보좌주교 도날 로치 · 2026년 2월 16일</cite>
    </div>
    <div class="btn-row reveal"><a class="btn btn-quiet" href="support.html">지금까지의 재원 <span class="arrow">→</span></a></div>
  </div>
</section>

{CTA}"""


# ---------------------------------------------------------------------------

ABOUT = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">단체 소개</p>
    <h1>음악은 일상에서 함께 나누는 경험이어야 합니다.</h1>
    <p>2024년 1월 더블린에서 시작한 커뮤니티 음악 사회적기업입니다. 전문 연주단체가 아니라,
       직접 연주하는 것이 핵심인 참여형 공동체입니다.</p>
  </div>
</section>

<section>
  <div class="wrap split split-wide">
    <div class="reveal">
      <p class="eyebrow">미션</p>
      <p class="lead">나이·배경·거동·소득·음악 지식과 무관하게, 살아있는 클래식 음악을 누구나
         누릴 수 있게 만듭니다 — 사람들에게 연주를 가르치고, 곁에서 함께 연주하고, 음악이 닿지
         않는 곳으로 찾아감으로써.</p>
      <p class="eyebrow mt-4">비전</p>
      <p class="lead">도시와 농촌, 돌봄 시설과 장애가 있는 삶 어디에서든 함께 음악을 만드는
         환대하는 통로가 있는 아일랜드. 그리고 그 일을 안정된 정규 고용 상태의 교육자들이
         수행하는 것.</p>
    </div>
    <figure class="reveal">
      <div class="photo photo-4x5">
        <img src="images/clarinet.jpg" width="1400" height="1400"
             alt="본당 전례에서 클라리넷을 연주하는 김서현">
      </div>
      <figcaption>더블린의 한 본당 전례에서. 커뮤니티 활동과 교회 봉사는 같은 실천입니다.</figcaption>
    </figure>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">변화이론</p>
      <h2>방 하나, 한 시간, 리코더 하나가 무엇이 되어야 하는가.</h2>
    </div>
    <div class="reveal">{dg.theory_of_change(L)}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">가치</p>
      <h2>다섯 가지 — 실제로 무엇을 감수하는가.</h2>
    </div>
    <div class="grid grid-3 stagger">
      <div class="card"><span class="kicker">01</span><h3>존엄</h3>
        <p>나이·건강·처지와 무관하게, 여전히 무언가를 창조할 수 있는 사람으로 대합니다.</p></div>
      <div class="card"><span class="kicker">02</span><h3>접근성</h3>
        <p>가격·거리·낯섦의 장벽을 낮춥니다. 신체적·환경적·심리적 장벽 모두.</p></div>
      <div class="card"><span class="kicker">03</span><h3>동행</h3>
        <p>한 번 방문하고 끝내지 않고 한 학기 내내 곁에 머뭅니다. 의미는 지속에서 자랍니다.</p></div>
      <div class="card"><span class="kicker">04</span><h3>공동체</h3>
        <p>나이와 배경과 언어를 가로질러 사람을 잇는 음악.</p></div>
      <div class="card"><span class="kicker">05</span><h3>희망</h3>
        <p>극적인 변화를 약속하지 않습니다. 작고 진짜인 연결의 순간을 소중히 여깁니다.</p></div>
      <div class="card" style="--card-bg:var(--surface-sunken)"><span class="kicker">그리고</span>
        <h3>교육자의 일자리</h3>
        <p>음악교육자 대부분이 불안정한 프리랜서 조건에서 일합니다. 제대로 고용하는 것이
           두 번째 사회적 목표입니다.</p></div>
    </div>
  </div>
</section>

<section class="band-photo">
  <img src="images/organ.jpg" alt="" width="1400" height="1050">
  <div class="wrap narrow reveal">
    <p class="eyebrow">창립자</p>
    <h2 class="h-lg">Andrew Seohyeon Kim · 김서현</h2>
    <p class="lead mt-3">
      더블린에서 활동하는 클라리네티스트이자 오르가니스트, 커뮤니티 음악 실천가입니다.
      2024년 1월 <span class="brandname">Classical Music for Everyone</span>과
      Letters Ensemble을 창립했고, 이 사이트의 모든 프로그램을 직접 이끌고 있습니다.</p>
  </div>
</section>

<section>
  <div class="wrap split split-wide">
    <div class="reveal">
      <h3 class="h-sub">실제로 하는 일</h3>
      <p class="lead mt-2">전부 같은 방 안에 있습니다. 리코더 수업의 강사, 강의·연주의 진행자,
         동행을 예약하는 사람, 요양시설에서 클라리넷을 부는 연주자, 그 자리에서 앙상블을
         지휘하는 사람이 같은 한 사람입니다.</p>
      <p class="mt-3">이건 설명인 동시에 한계입니다. 주당 50회 세션이 아니라 다섯 개
         프로그램이라고 말하는 이유가 여기 있고, 음악교육자를 제대로 고용하는 것이 좋은
         아이디어가 아니라 두 번째 사회적 목표인 이유도 여기 있습니다. 이 일은 한 사람 위에서
         커지지 않고, 커져서도 안 됩니다.</p>
      <p class="mt-3">2026년 5월 TU Dublin Conservatoire에서 연주 전공 음악학사(우등)를
         졸업했습니다. Dr Paul Roe에게 클라리넷을 배우며 오르간·첼로·피아노를 함께 공부했고,
         졸업 연구는 은퇴 프레젠테이션 수녀 일곱 분을 위해 직접 설계하고 이끈 10주 리코더
         앙상블에 대한 실천 기반 연구였습니다. 지금의 교육 프로그램 전체가 그 위에 서 있습니다.</p>
    </div>
    <div class="reveal">
      <div class="callout">
        <h3 class="h-sub">교회와 커뮤니티는 하나의 실천</h3>
        <p class="small mt-2">2022년 9월부터 Dolphin&rsquo;s Barn 성모 통고 성당 음악감독,
           2023년 9월부터 Rathgar 삼주보 성당의 주일 오르가니스트로 봉사하고 있습니다 —
           성주간 전례, 학교 미사와 위령 미사, 장례, 본당 음악회.</p>
        <p class="small mt-2">본당과 수도 공동체에는 이 일을 &lsquo;음악을 통한 평신도
           사도직&rsquo;으로 설명합니다. 연주 시리즈가 아니라 함께 있어 주는 봉사라는 뜻입니다.
           커뮤니티 활동과 같은 실천을, 그렇게 물어본 분들의 언어로 설명한 것입니다.</p>
      </div>
      <div class="quote mt-4">
        <p>&ldquo;음악을 통해 그는 고립감을 느낄 수 있는 이들에게 격려와 존엄, 그리고 영적
           동행을 건넵니다.&rdquo;</p>
        <cite>더블린 보좌주교 Donal Roche &middot; 2026년 2월 16일</cite>
      </div>
    </div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">배움과 역할</p>
      <h2 class="h-md">이 실천이 어디에서 왔는가.</h2>
    </div>
    <div class="split reveal">
      <div>
        <h3 class="h-sub">학력과 훈련</h3>
        <ul class="plainlist mt-2">
          <li><strong>연주 전공 음악학사(우등)</strong> — TU Dublin Conservatoire, 2022–2026</li>
          <li><strong>클라리넷</strong> — Dr Paul Roe</li>
          <li><strong>오르간</strong> — Simon Harden &middot; <strong>첼로</strong> — Arun Rao
              &middot; <strong>피아노</strong> — Sam Armstrong</li>
          <li><strong>지휘</strong> — 아일랜드 청소년오케스트라협회(IAYO) &middot;
              London Conducting Workshop &middot; TU Dublin 특별 과정</li>
          <li><strong>사회적기업</strong> — TU Dublin Venture Lab, 2024년 9월부터</li>
          <li><strong>장학</strong> — 한국 천주교 주교회의 평신도사도직위원회 명도회,
              2025년 3월부터</li>
        </ul>
      </div>
      <div>
        <h3 class="h-sub">현재 맡고 있는 일</h3>
        <ul class="plainlist mt-2">
          <li><strong>창립자 · 프로젝트 리드</strong> — <span class="brandname">Classical Music
              for Everyone</span>, 2024년 1월부터</li>
          <li><strong>창립자 · 음악감독 · 지휘</strong> — Letters Ensemble, 2024년 1월부터</li>
          <li><strong>음악감독</strong> — 성모 통고 성당(Dolphin&rsquo;s Barn), 2022년 9월부터</li>
          <li><strong>오르가니스트</strong> — 삼주보 성당(Rathgar), 2023년 9월부터</li>
          <li><strong>학생 홍보대사</strong> — TU Dublin, 2024년 8월부터</li>
        </ul>
        <h3 class="h-sub mt-4">그 전에</h3>
        <ul class="plainlist mt-2">
          <li><strong>Baram</strong>, 2023–24 — 한국 전통음악과 클래식 듀오. 대사관 행사와
              문화 전시</li>
          <li><strong>Chorus of Angels</strong>, 2023 — 더블린의 한인·다문화 어린이 합창단</li>
          <li><strong>At Home Ensemble Project</strong>, 2020–21 — 코로나19 기간의 온라인
              관악 앙상블</li>
        </ul>
      </div>
    </div>
    <div class="split reveal mt-4">
      <div>
        <h3 class="h-sub">자원봉사</h3>
        <ul class="plainlist mt-2">
          <li>세계청년대회, 리스본, 2023 — 진행·음악·전례·언어 지원</li>
          <li>ICA ClarinetFest, 더블린, 2024 — 지원과 통역</li>
          <li>제13회 더블린 국제 피아노 콩쿠르, 2025 — Team Harmony</li>
          <li>청년 희년, 로마, 2025 &middot; Korea Festival, Farmleigh House, 2025</li>
        </ul>
        <p class="small mt-2">포르투갈과 이탈리아는 자원봉사지입니다. 저희 기록의 &lsquo;4개국&rsquo;은
           <em>연주한</em> 네 나라입니다.</p>
      </div>
      <div>
        <h3 class="h-sub">함께 연주하는 예술가</h3>
        <ul class="plainlist mt-2">
          <li><strong>안수정</strong>, 피아노 — RIAM 음악박사(2022). 제58회 마리아 카날스
              국제콩쿠르 1위</li>
          <li><strong>정혜리</strong>, 소프라노 — 신라대학교, 로마 산타 체칠리아 국립음악원</li>
          <li><strong>김재원</strong>, 해금 — <em>Shared Voices of Care</em>와
              <em>An Autumn Concert</em>(2026) 객원</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">연주해 온 곳</p>
      <h2>음악이 잘 들어가지 않는 방들.</h2>
      <p>요양·거주 돌봄시설 · 수도 공동체 · 본당 · 대학 · 국립 콘서트홀 · HSE 주간보호센터 ·
         노숙인 쉼터 · 커뮤니티 센터.</p>
    </div>
    <div class="split reveal">
      <div>
        <h3 class="h-sub">아일랜드</h3>
        <ul class="plainlist mt-2">
          <li>National Concert Hall · TU Dublin, Grangegorman</li>
          <li>Tallaght University Hospital · Rua Red, Tallaght</li>
          <li>성모 통고 성당(Dolphin&rsquo;s Barn) · 삼주보 성당(Rathgar)</li>
          <li>Carmelite Community Centre · Blessed Sacrament Chapel</li>
          <li>Clondalkin Lodge · Warrenmount, Dublin 8</li>
          <li>성 골롬반 외방 선교 수녀회, Co. Wicklow</li>
          <li>마리아의 프란치스코 선교 수녀회, Dublin 5</li>
          <li>Dalgan Park · Kilmessan Church, Co. Meath · Dysart, Co. Westmeath</li>
          <li>HSE EVE Goirtin Hub · Morning Star Hostel, Dublin 7</li>
          <li>Methodist Centenary Church, Ranelagh · Mulhuddart Community Centre, D15</li>
        </ul>
      </div>
      <div>
        <h3 class="h-sub">국외</h3>
        <ul class="plainlist mt-2">
          <li>루르드 성모 성지, 프랑스</li>
          <li>파리 외방 전교회 · Palais Brongniart, 파리</li>
          <li>런던 한인 천주교회, 영국</li>
          <li>관덕정 순교자 기념관, 대구, 한국</li>
        </ul>
        <div class="callout mt-3">
          <h3 class="h-sub">주장하지 않는 것</h3>
          <p class="small mt-1">지금까지의 근거는 참여·지속·증언이지 측정된
             성과가 아닙니다. 검증된 도구로 웰빙을 측정한 적이 없고, 찾아가는 음악회의 관객 수도
             기록되지 않았습니다. 2026년 가을 기수부터 간단한 사전·사후 측정과 동의 절차를
             도입합니다.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">우리가 하는 일</p>
      <h2>다섯 개의 프로그램, 각각의 페이지.</h2>
      <p>두 개의 축 — 사람들에게 연주를 가르치는 일과, 콘서트홀까지 오기 어려운 분들을 위해
         찾아가 연주하는 일. 다섯을 같은 분량으로, 같은 항목으로, 같은 순서로 적었습니다.
         그 가운데 주된 것은 없습니다.</p>
    </div>
    <div class="reveal">{dg.loop(L)}</div>
    <div class="btn-row reveal">
      <a class="btn btn-primary" href="programmes.html">다섯 프로그램 전체 <span class="arrow">&rarr;</span></a>
      <a class="btn btn-quiet" href="get-involved.html">참여하는 방법</a>
    </div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">아이덴티티</p>
      <h2>디자인 표준을 공개합니다.</h2>
      <p>작은 단체가 이름을 올리는 모든 것은, 디자인 도구로 만들었든 본당 주보에 타이핑했든
         같은 곳에서 나온 것처럼 보여야 합니다. 저희가 지키는 기준이고, 저희를 대신해
         무언가를 인쇄하는 파트너도 이 기준으로 저희를 붙잡을 수 있도록 공개합니다.</p>
    </div>

    <div class="split split-center reveal">
      <div class="logo-pair">
        <figure class="logo-plate on-light">
          <img src="assets/logo-horizontal.svg" width="341" height="131"
               alt="가로형 로고 — 높은음자리표와 워드마크">
          <figcaption>밝은 바탕 — 기본형</figcaption>
        </figure>
        <figure class="logo-plate on-dark">
          <img src="assets/logo-reversed.svg" width="341" height="131"
               alt="어두운 바탕용 반전 로고">
          <figcaption>네이비 바탕 — 반전형</figcaption>
        </figure>
      </div>
      <div>
        <h3 class="h-sub">마크</h3>
        <p class="mt-2">높은음자리표와 워드마크를 함께 쓰며, 2026년 8월 17일에 확정했습니다.
           워드마크 안의 비례가 의미를 지므로 절대 바뀌지 않습니다 —
           <strong>&lsquo;for&rsquo;는 작게, &lsquo;Everyone&rsquo;은 크고 금색으로.</strong>
           이름은 하나의 모양을 가진 고유명사입니다 — <span class="brandname">Classical Music
           for Everyone</span> — 전부 대문자로 쓰지 않고, 대외 문안에서 CMFE로 줄이지 않으며,
           다른 서체로 다시 조판하지 않습니다.</p>
        <div class="rules mt-3">
          <div class="do">
            <h3 class="h-sub">언제나</h3>
            <ul>
              <li>자리표와 워드마크를 함께</li>
              <li>네 면 모두에 자리표 너비의 절반만큼 여백</li>
              <li>밝은 바탕 → 가로형, 어두운 바탕 → 반전형</li>
              <li>사진 위에 놓을 때는 뒤가 조용한 자리에</li>
            </ul>
          </div>
          <div class="dont">
            <h3 class="h-sub">절대로</h3>
            <ul>
              <li>늘이거나 누르거나 기울이거나 색을 바꾸지 않습니다</li>
              <li>그림자·외곽선·광채를 넣지 않습니다</li>
              <li>&lsquo;for&rsquo;와 &lsquo;Everyone&rsquo;을 같은 크기로 두지 않습니다</li>
              <li>파비콘 크기를 넘어서 자리표만 쓰지 않습니다</li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <div class="section-head reveal mt-4">
      <h3 class="h-sub">색</h3>
      <p>여덟 개의 값을 한 번만 정의합니다. 이 사이트의 모든 색은 그중 하나이거나 거기서
         파생된 톤입니다. 컴포넌트가 자기 색을 새로 만들어 쓰는 일은 없습니다.</p>
    </div>
    <div class="swatches reveal">
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--ink-navy)"></i><b>Ink Navy</b><code>#1D2430</code>
        <span>로고 바탕색, 본문, 어두운 밴드</span></div>
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--gold-bronze)"></i><b>Gold Bronze</b><code>#B8893A</code>
        <span>로고 금색, 괘선, 화살표, 도식 선</span></div>
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--gold-light)"></i><b>Light Gold</b><code>#D9B36A</code>
        <span>반전 로고의 금색, 어두운 면 위 강조</span></div>
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--warm-cream)"></i><b>Warm Cream</b><code>#FAF5EE</code>
        <span>거의 모든 페이지의 배경</span></div>
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--soft-navy)"></i><b>Soft Navy</b><code>#33405C</code>
        <span>인쇄물의 패널과 블록</span></div>
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--antique-gold)"></i><b>Antique Gold</b><code>#B4914F</code>
        <span>인쇄물의 액센트</span></div>
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--dusty-rose)"></i><b>Dusty Rose</b><code>#8C4A56</code>
        <span>강조 — 아껴 쓰고, 본문에는 쓰지 않습니다</span></div>
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--slate)"></i><b>Slate</b><code>#5F6B7D</code>
        <span>보조 텍스트</span></div>
    </div>
    <div class="callout reveal mt-3">
      <p class="small"><strong>더 예쁜 선택지를 포기하게 만드는 규칙 하나.</strong>
         Gold Bronze는 크림 바탕에서 대비가 2.9:1이라 본문 크기에서 떨어집니다. 그래서
         <em>글자</em>로 쓰는 금색은 언제나 어둡게 조정한 <code>#7F5C1C</code>이고, 금색 버튼의
         글자는 흰색이 아니라 잉크 네이비입니다. 이 사이트의 모든 글자·배경 조합은 WCAG AA를
         통과합니다. 예외는 로고 하나뿐인데, 로고는 이미지이고 색을 바꾸지 않기 때문입니다.</p>
    </div>

    <div class="section-head reveal mt-4">
      <h3 class="h-sub">서체</h3>
      <p>세 벌이고, 네 번째는 들이지 않습니다. Fraunces는 옵티컬 사이즈 세리프라 스케일의 각
         단계마다 자간을 따로 잡았고, 한국어는 행간을 더 주고 음수 자간을 덜 조입니다.
         Noto Sans KR에는 둘 다 필요하기 때문입니다.</p>
    </div>
    <div class="specimen reveal">
      <div>
        <dfn>Fraunces — 제목</dfn>
        <div class="sp-display">Bringing classical music where it&rsquo;s needed.</div>
        <p>SemiBold. 제목·헤드라인·디스플레이 크기.</p>
      </div>
      <div>
        <dfn>Plus Jakarta Sans — 영문 본문과 라벨</dfn>
        <div class="sp-body">We teach people to play, not only to listen.</div>
        <p>Regular · SemiBold · Bold. 본문, 표, 캡션, 모든 라벨.</p>
      </div>
      <div>
        <dfn>Noto Sans KR — 한글</dfn>
        <div class="sp-kr">클래식 음악을, 그것이 필요한 곳으로.</div>
        <p>Regular · Medium · Bold. 한국어 페이지의 제목과 본문 모두.</p>
      </div>
      <div>
        <dfn>Cormorant Garamond — 로고 전용</dfn>
        <div class="sp-body">워드마크에만 쓰고, 다른 어디에도 쓰지 않습니다.</div>
        <p>로고의 글자는 외곽선으로 변환돼 있어, 이 사이트는 이 서체를 불러오지 않습니다.</p>
      </div>
    </div>

    <div class="section-head reveal mt-4">
      <h3 class="h-sub">도식</h3>
      <p>설명이 여든 단어를 넘어가면 그것은 문단이기를 그만두고 그림이 됩니다. 이 사이트의
         모든 도식은 같은 네 개의 표시로 그려집니다. 그래서 아홉 개의 도식이 아홉 개의
         순서도가 아니라 하나의 세트로 읽힙니다.</p>
    </div>
    <div class="reveal">{dg.vocabulary(L)}</div>
  </div>
</section>

{CTA}"""


# ---------------------------------------------------------------------------

PROGRAMMES = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">프로그램</p>
    <h1>실제로 하고 있는 일.</h1>
    <p>두 축 아래 다섯 개의 프로그램, 그리고 하나의 신앙 기반 세부 갈래. 그중 주된 것은
       없습니다. 다섯 모두를 같은 분량, 같은 항목, 같은 순서로 적었습니다.</p>
  </div>
</section>

<section class="tight">
  <div class="wrap reveal">
    <div class="table-scroll">
      <table>
        <thead><tr>
          <th scope="col">프로그램</th><th scope="col">축</th>
          <th scope="col">상태</th><th scope="col">현재까지</th>
        </tr></thead>
        <tbody>
          <tr><td><strong><a class="link" href="programmes/recorder-ensemble.html">리코더 앙상블 과정</a></strong></td><td>배움</td>
              <td>운영 중</td><td>파일럿 완료 · 2026년 9월 첫 커뮤니티 수업</td></tr>
          <tr><td><strong><a class="link" href="programmes/getting-to-know.html">클래식 음악과 친해지기</a></strong></td><td>배움</td>
              <td>운영 중 · 무료</td><td>강의·연주 17회 · 누적 참석 143명</td></tr>
          <tr><td><strong><a class="link" href="programmes/concert-companion.html">함께하는 음악여행</a></strong></td><td>배움</td>
              <td>운영 중</td><td>기록된 동행 10회 · 두 해 연속 BBC 프롬스 포함</td></tr>
          <tr><td><strong><a class="link" href="programmes/outreach-concerts.html">찾아가는 음악회</a></strong></td><td>나눔</td>
              <td>운영 중</td><td>20회 · 4개국 · 15곳 이상</td></tr>
          <tr><td style="padding-inline-start:34px">↳ 성지에 음악을</td><td>나눔</td>
              <td>세부 갈래</td><td>찾아가는 음악회 20회 중 약 16회</td></tr>
          <tr><td><strong><a class="link" href="programmes/letters-ensemble.html">Letters Ensemble</a></strong></td><td>나눔</td>
              <td>운영 중</td><td>정식 음악회 4회 · 2024년 1월부터 매주 연습</td></tr>
        </tbody>
      </table>
    </div>
    <div class="mt-4">{dg.loop(L)}</div>
  </div>
</section>

<section>
  <div class="wrap split split-wide split-center">
    <figure class="reveal">
      <div class="photo photo-4x3">
        <img src="images/conducting.jpg" width="1400" height="1050" alt="커뮤니티 공간에서 소규모 앙상블을 지휘하는 모습">
      </div>
      <figcaption>모든 과정은 같은 방식으로 끝납니다 — 아무리 작아도 음악회로.</figcaption>
    </figure>
    <div class="reveal">
      <p class="eyebrow">배움</p>
      <h2 class="h-md">리코더 앙상블 과정</h2>
      <p class="lead mt-2">완전 초보를 위한 한 학기, 마지막은 음악회로 끝납니다.</p>
      <p class="mt-2">리코더는 손과 호흡에 부담이 적고, 만족스러운 첫 소리가 빨리 나오며, 값이 싸고, 함께 부는 악기입니다. 아무 악기도 다뤄 본 적 없는 분에게 맞는 이유입니다. 악보와 유인물은 저희가 인쇄해 드리며 참가자 부담은 없습니다.</p>
      <dl class="facts">
        <dt>기간</dt><dd>한 학기 · 주 1회 · 회당 60–90분</dd>
        <dt>대상</dt><dd>완전 초보 — 악보를 읽을 줄 몰라도 됩니다</dd>
        <dt>악기</dt><dd>소프라노 리코더 — 구입 안내, 원가 공급, 또는 대여</dd>
        <dt>마무리</dt><dd>가족과 친구를 위한 짧은 음악회</dd>
        <dt>현재 진행</dt><dd>Mulhuddart Community Centre, Dublin 15 · 2026년 9월 9일부터 수요일 19:00–20:00 · 무료</dd>
      </dl>
      <div class="btn-row"><a class="btn btn-quiet" href="programmes/recorder-ensemble.html">자세히 보기 <span class="arrow">&rarr;</span></a></div>
    </div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap split split-wide split-center split-flip">
    <figure class="reveal">
      <div class="photo photo-4x3">
        <img src="images/lecture-recital.jpg" width="1400" height="1050" alt="진행 중인 강의·연주">
      </div>
      <figcaption>진행 중인 강의·연주.</figcaption>
    </figure>
    <div class="reveal">
      <p class="eyebrow">배움</p>
      <h2 class="h-md">클래식 음악과 친해지기</h2>
      <p class="lead mt-2">사전 지식이 없는 분들을 위한 무료 강의·연주.</p>
      <p class="mt-2">대략 월 1회, 음원과 실연을 함께 씁니다. 어디서부터 시작해야 할지 몰랐던 분을 위한 자리입니다. 자격 조건도, 미리 준비할 것도 없습니다.</p>
      <dl class="facts">
        <dt>세 단계</dt><dd>가까이 가기 · 함께 겪기 · 내 취향 찾기</dd>
        <dt>계절 특별편</dt><dd>유럽 여름 페스티벌, BBC 프롬스, 웩스퍼드 오페라 페스티벌, 성탄</dd>
        <dt>규모</dt><dd>보통 6–14명</dd>
        <dt>비용</dt><dd>무료</dd>
        <dt>현재까지</dt><dd>17회 · 누적 참석 143명</dd>
      </dl>
      <div class="btn-row"><a class="btn btn-quiet" href="programmes/getting-to-know.html">자세히 보기 <span class="arrow">&rarr;</span></a></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split split-wide split-center">
    <figure class="reveal">
      <div class="photo photo-4x3">
        <img src="images/quartet-hall.jpg" width="1400" height="1050" alt="밝은 홀에서 연주하는 앙상블">
      </div>
      <figcaption>밝은 홀에서 연주하는 앙상블.</figcaption>
    </figure>
    <div class="reveal">
      <p class="eyebrow">배움</p>
      <h2 class="h-md">함께하는 음악여행</h2>
      <p class="lead mt-2">혼자서는 가지 않을 공연에 소그룹으로 동행합니다.</p>
      <p class="mt-2">가기 전에 준비하고, 인터미션에 설명하고, 끝나고 함께 이야기합니다. 걸림돌은 티켓값인 경우가 드뭅니다 — 가서 무슨 일이 벌어지는지 모르는 것, 그리고 같이 갈 사람이 없다는 것입니다.</p>
      <dl class="facts">
        <dt>규모</dt><dd>5명 안팎</dd>
        <dt>다녀온 곳</dt><dd>국립교향악단 · 아일랜드 국립오페라 · RTÉ 콘서트 오케스트라 · NCH 인터내셔널 시리즈</dd>
        <dt>멀리는</dt><dd>두 해 연속 BBC 프롬스</dd>
        <dt>비용</dt><dd>티켓이 £8 정도인 경우도 있습니다</dd>
        <dt>현재까지</dt><dd>기록된 동행 10회</dd>
      </dl>
      <div class="btn-row"><a class="btn btn-quiet" href="programmes/concert-companion.html">자세히 보기 <span class="arrow">&rarr;</span></a></div>
    </div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap split split-wide split-center split-flip">
    <figure class="reveal">
      <div class="photo photo-4x3">
        <img src="images/care-christmas.jpg" width="1400" height="1050" alt="성탄에 요양시설에서 연주하는 사중주">
      </div>
      <figcaption>성탄에 요양시설에서 연주하는 사중주.</figcaption>
    </figure>
    <div class="reveal">
      <p class="eyebrow">나눔</p>
      <h2 class="h-md">찾아가는 음악회</h2>
      <p class="lead mt-2">이미 사람들이 있는 방으로 실연을 가져갑니다.</p>
      <p class="mt-2">요양시설·본당·병원·쉼터·커뮤니티 공간 — 더블린 7구의 노숙인 쉼터부터 대구의 순교 성지까지. 악기와 보면대, 프로그램은 저희가 가져갑니다. 그 공간은 공간만 내어 주시면 됩니다.</p>
      <dl class="facts">
        <dt>장소</dt><dd>요양시설 · 본당 · 병원 · 쉼터 · 커뮤니티 공간</dd>
        <dt>넓혀 가는 지역</dt><dd>위클로 · 미스 · 라우스</dd>
        <dt>목표</dt><dd>연 10회 이상</dd>
        <dt>시작</dt><dd>2023년</dd>
        <dt>현재까지</dt><dd>20회 · 15곳 이상 · 4개국</dd>
      </dl>
      <div class="btn-row"><a class="btn btn-quiet" href="programmes/outreach-concerts.html">자세히 보기 <span class="arrow">&rarr;</span></a></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split split-wide split-center">
    <figure class="reveal">
      <div class="photo photo-4x3">
        <img src="images/letters-ensemble.jpg" width="1400" height="1050" alt="악기를 든 Letters Ensemble">
      </div>
      <figcaption>악기를 든 Letters Ensemble.</figcaption>
    </figure>
    <div class="reveal">
      <p class="eyebrow">나눔</p>
      <h2 class="h-md">Letters Ensemble</h2>
      <p class="lead mt-2">더블린에 사는 아마추어 연주자들이 매주 토요일 연습합니다.</p>
      <p class="mt-2">어떤 방이든 음악을 반쯤 마중 나올 수 있도록 곡을 고릅니다 — 아일랜드 전통음악, 한국 전통음악, 전례 음악, 그리고 편하게 들리는 편곡. 새로운 아마추어 연주자를 환영합니다.</p>
      <dl class="facts">
        <dt>창단</dt><dd>2024년 1월, 더블린에 사는 아마추어 연주자들이</dd>
        <dt>연습</dt><dd>매주 토요일</dd>
        <dt>레퍼토리</dt><dd>아일랜드 전통 · 한국 전통 · 전례 음악 · 편안한 편곡</dd>
        <dt>함께할 수 있는 분</dt><dd>아마추어 연주자</dd>
        <dt>현재까지</dt><dd>정식 음악회 4회</dd>
      </dl>
      <div class="btn-row"><a class="btn btn-quiet" href="programmes/letters-ensemble.html">자세히 보기 <span class="arrow">&rarr;</span></a></div>
    </div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">한 과정을 만드는 방식</p>
      <h2>만족스러운 첫 소리는 1주차에 납니다.</h2>
      <p>악기가 무엇이든 배움 프로그램은 같은 모양으로 만듭니다 — 들을 만한 소리에 일찍
         닿고, 그룹 전체가 함께 움직이고, 사람들 앞에서 끝냅니다.</p>
    </div>
    <div class="reveal">{dg.term(L)}</div>

    <div class="split split-wide split-center mt-4">
      <div class="reveal">
        <p class="eyebrow">이 모델이 나온 곳</p>
        <h3 class="h-md">파일럿.</h3>
        <p class="lead mt-2">은퇴한 프레젠테이션 수녀 일곱 분. 더블린 8구 Warrenmount에서
           주 1회씩 열 시간. Clondalkin Lodge에서 아홉 곡의 부활 음악회. TU Dublin
           음악원 학사 연구로 수행했습니다.</p>
        <p class="mt-2">그에 앞서 석 달의 준비가 있었습니다 — 필요 조사, 허가, 신원 확인,
           개별 레슨, 파트 배정. 소프라노·알토·테너·베이스 리코더에 멜로디카와 실로폰,
           작은 타악기를 더하고 악보를 확대했습니다. 일곱 분 모두 수료하고 사람들 앞에서
           연주했습니다.</p>
      </div>
      <div class="reveal">
        <ul class="checklist">
          <li><strong>관계</strong> — 매주 모일 따뜻한 이유.</li>
          <li><strong>존엄과 성취</strong> — &ldquo;나도 음악을 만들 수 있다&rdquo;는 조용한 자부심.</li>
          <li><strong>부드러운 자극</strong> — 기억, 협응, 호흡, 집중.</li>
          <li><strong>우정</strong> — 학기가 끝나도 남는 관계.</li>
        </ul>
        <div class="callout mt-3">
          <span class="tag tag-live">현재 진행</span>
          <p class="mt-1"><strong>Mulhuddart Community Centre, Dublin 15.</strong>
             2026년 9월 9일부터 수요일 19:00–20:00, 12주, 무료 — 성탄 전 음악회로 마무리합니다.</p>
          <div class="btn-row"><a class="btn btn-accent" href="get-involved.html">수업 참여하기 <span class="arrow">→</span></a></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap narrow reveal">
    <p class="eyebrow">세부 갈래</p>
    <h2 class="h-md">성지에 음악을</h2>
    <p class="mt-2">신앙에 기반한 갈래입니다 — 본당, 성지, 수도원, 전례, 은퇴한 수도
       공동체. 찾아가는 음악회 20회 가운데 약 열여섯 회가 여기에 해당합니다. 신앙 공동체
       앞에서는 음악을 통한 평신도 사도직으로 설명합니다. 연주 시리즈가 아니라
       현존의 봉사입니다.</p>
  </div>
</section>

{CTA}"""


# ---------------------------------------------------------------------------
# 참여하기
# ---------------------------------------------------------------------------

GET_INVOLVED = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">참여하기</p>
    <h1>네 가지 길. 나에게 맞는 것을 고르면 됩니다.</h1>
    <p>오디션도, 사전 경험도, 준비할 것도 없습니다. 어디에 해당하는지 모르겠다면 그렇게 적어
       주세요. 아주 평범한 문의입니다.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <h2 class="sr-only">참여하는 방법</h2>
    <div class="grid grid-2 stagger">
      <article class="card">
        <span class="kicker">완전 초보라면</span>
        <h3>연주를 배웁니다</h3>
        <p>리코더 앙상블 과정에 참여하세요. 첫 주에 첫 소리, 악보는 처음부터, 앙상블에서 내 파트,
           그리고 학기 끝에 짧은 음악회.</p>
        <div class="meta">Mulhuddart Community Centre, D15 · 수요일 19:00–20:00 ·
           2026년 9월 9일 개강 · 무료</div>
      </article>
      <article class="card">
        <span class="kicker">먼저 듣고 싶다면</span>
        <h3>들으러 옵니다</h3>
        <p>무료 강의·연주에 오시거나, 함께 공연을 보러 가는 소그룹에 합류하세요. 미리 준비하고,
           나란히 앉아 듣고, 끝나고 이야기를 나눕니다. 혼자서는 가지 않게 되는 분,
           아일랜드에 막 오신 분을 특히 환영합니다.</p>
        <div class="meta">대략 월 1회 · 5명 내외</div>
      </article>
      <article class="card">
        <span class="kicker">이미 연주한다면</span>
        <h3>함께 연주합니다</h3>
        <p>Letters Ensemble은 더블린에 사는 아마추어 연주자에게 열려 있습니다 — 매주 토요일
           연습과 커뮤니티 공간에서의 연주. 찾아가는 음악회 운영을 돕는 자원봉사자도
           환영합니다.</p>
        <div class="meta">현악·관악 모두 환영</div>
      </article>
      <article class="card">
        <span class="kicker">공간을 운영한다면</span>
        <h3>초대하거나 함께합니다</h3>
        <p>찾아가는 음악회를 초대하시거나, 그 공동체를 위한 과정을 여실 수 있습니다.
           공공배상책임보험을 보유하고 있고, 신원조회가 필요한 일은 시작 전에 Garda 신원조회를 마칩니다.</p>
        <div class="meta">더블린·위클로·미스·라우스, 그 밖 지역도 협의</div>
      </article>
    </div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">네 갈래는 어떻게 이어지는가</p>
      <h2>신청서 네 종류가 아니라, 문장 네 개입니다.</h2>
      <p>어느 쪽이 맞는지 고르실 필요 없습니다. 지금 함께 연주하는 분들 대부분이 처음에는
         들으러 오셨고, 저희가 연주하는 방 중 둘은 음악회에 오셨던 분이 내어 주신 것입니다.</p>
    </div>
    <div class="reveal">{dg.pathways(L)}</div>
  </div>
</section>

<section>
  <div class="wrap split split-wide split-center">
    <div class="reveal">
      <p class="eyebrow">보내신 다음에는</p>
      <h2 class="h-md">서식도, 대기자 명단도, 면접도 없습니다.</h2>
      <p class="mt-3">모든 문의는 창립자에게 바로 갑니다. 답장을 쓰는 사람이 그 방에서 함께
         있을 사람입니다. 작성할 서식도, 첨부할 것도 없습니다.</p>
    </div>
    <div class="reveal">
      <ol class="steps">
        <li><strong>한 줄만 쓰시면 됩니다.</strong> 무엇에 관한 문의인지, 대략 어느 지역인지.
            정말 그걸로 충분합니다.</li>
        <li><strong>실무적인 내용으로 답을 드립니다</strong> — 장소·요일·시간·비용, 그리고
            가져오실 것. 대개 며칠 안에 답장합니다.</li>
        <li><strong>한 번 와서 보시면 됩니다.</strong> 한 회차에 와 보는 것이 한 학기를
            약속하는 일은 아닙니다.</li>
        <li><strong>맞지 않는다면</strong> 그렇다고 말씀드리고, 맞는 곳을 알려 드립니다.
            저희가 하지 않는 일이라도 그렇게 합니다.</li>
      </ol>
    </div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">공간을 여는 분들께</p>
      <h2>방 하나와 담당자 한 분. 나머지는 저희가 합니다.</h2>
    </div>
    <div class="split reveal">
      <div>
        <h3>공간이 준비하는 것</h3>
        <ul class="checklist mt-2">
          <li>열 명에서 열두 명이 둥글게 앉을 따뜻한 방, 학기 동안 주 1회</li>
          <li>지역에 알리는 일에 조금의 도움</li>
          <li>담당자 한 분</li>
          <li>그 밖에는 없습니다 — 장비도, 행정도, 피아노도</li>
        </ul>
      </div>
      <div>
        <h3>저희가 준비하는 것</h3>
        <ul class="checklist mt-2">
          <li>강사와 전체 커리큘럼</li>
          <li>모든 악보와 주간 교재 (저희 비용으로 인쇄)</li>
          <li>저렴한 악기 안내, 필요하면 대여</li>
          <li>학기 말 음악회</li>
          <li>보험·신원조회 서류</li>
        </ul>
      </div>
    </div>
    <div class="callout reveal mt-4">
      <p><strong>비용에 관하여.</strong> 모든 프로그램에 무료·할인 자리를 둡니다. 공간이 자체
         예산에서 진행비를 지불할 수 있으면 그 방에 있는 모든 분의 참여가 무료가 되고, 그 기여가
         다른 곳의 문을 열어 둡니다. 그럴 수 없더라도 우선 이야기부터 나눕니다.</p>
    </div>
  </div>
</section>

<section class="band-photo">
  <img src="images/quartet-hall.jpg" alt="" width="1400" height="788">
  <div class="wrap narrow center reveal">
    <p class="eyebrow center-row">다음 단계</p>
    <h2 class="h-lg">한 줄만 적어 주세요.</h2>
    <p class="lead mt-2">네 가지 중 어디에
       해당하는지, 그리고 대략 어디에 계신지. 구체적인 안내를 답장으로 보내 드립니다.</p>
    <div class="btn-row center-row">
      <a class="btn btn-accent" href="mailto:sby05034@gmail.com?subject=CMFE%20참여%20문의">메일 보내기 <span class="arrow">→</span></a>
      <a class="btn btn-on-dark" href="contact.html">연락처 전체</a>
    </div>
  </div>
</section>"""


# ---------------------------------------------------------------------------

NEWS = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">소식과 기록</p>
    <h1>다가오는 일, 그리고 지나온 일.</h1>
    <p>하이라이트가 아니라 대장(帳)으로 남깁니다. 모든 세션과 연주를 그날 기록해 두기 때문에,
       인용하는 숫자는 어느 것이든 한 줄로 되짚을 수 있습니다.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">다가오는 일정</p>
      <h2>2026년 가을.</h2>
    </div>
{WHATS_ON}
    <div class="callout reveal mt-3">
      <p><strong>2026년 12월 —</strong> 가족과 친구를 초대한 음악회로 Mulhuddart 첫 기수를
         마무리합니다. 자세한 내용은 추후 안내합니다.</p>
    </div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">올해</p>
      <h2>2026년, 여기까지.</h2>
    </div>
    <div class="grid grid-3 stagger">
      <article class="card card-media">
        <div class="photo photo-3x2"><img src="images/quartet-hall.jpg" width="1400" height="788"
             alt="밝은 홀에서 연주하는 앙상블"></div>
        <div class="card-body">
          <span class="tag tag-live">첫 공적 지원</span>
          <h3 class="mt-1">South Dublin Live 2026</h3>
          <p>SDCC 예술과가 이 프로젝트를 2026년 프로그램에 선정했습니다. 우리 아닌 누군가가
             처음으로 비용을 댄 일입니다.</p>
          <div class="meta">2026년 8월 · SDCC 예술과</div>
        </div>
      </article>
      <article class="card">
        <span class="kicker">2026년 8월 20일</span>
        <h3>Shared Voices of Care</h3>
        <p>Tallaght University Hospital 아트리움에서 30분 어쿠스틱 드롭인 공연. 해금 연주자
           김재원과 함께 환자·보호자·방문객·직원을 위해 연주했습니다. 병원의 National Centre
           for Arts &amp; Health가 주최했습니다.</p>
        <div class="meta">Tallaght University Hospital</div>
      </article>
      <article class="card">
        <span class="kicker">2026년 8월 29일</span>
        <h3>Shared Voices of Classical Tradition</h3>
        <p>South Dublin의 현대예술센터 Rua Red 퍼포먼스 스페이스에서 클라리넷·피아노·소프라노
           트리오로 60분 실내악 리사이틀. 무료 입장.</p>
        <div class="meta">Rua Red, Tallaght</div>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">지나온 길</p>
      <h2>클라리넷 하나에서 공동체까지.</h2>
    </div>
    <div class="split split-wide">
      <div class="timeline reveal">
        <div class="tl-item"><div class="tl-date">2023년 2월</div>
          <h3>시작 이전</h3>
          <p>루르드의 영어 미사에서 클라리넷 독주. 이름이 붙기 2년 전의 찾아가는 음악회.</p></div>
        <div class="tl-item"><div class="tl-date">2024년 1월</div>
          <h3>시작</h3>
          <p>더블린에서 CMFE가, 그리고 Letters Ensemble이 함께 만들어집니다. 첫 강의·연주는
             Dublin 18에서 여섯 명과 함께.</p></div>
        <div class="tl-item"><div class="tl-date">2024년</div>
          <h3>음악이 나갑니다</h3>
          <p>Dalgan Park와 성 골롬반 외방 선교 수녀회에서 음악회, 런던·파리·대구에서 연주.
             강의 시리즈는 TU Dublin으로 옮겨 갑니다.</p></div>
        <div class="tl-item"><div class="tl-date">2024–2025년</div>
          <h3>함께 갑니다</h3>
          <p>동행 관람이 독립된 갈래가 됩니다 — 국립교향악단, 아일랜드 국립 오페라, 2년 연속
             BBC Proms.</p></div>
        <div class="tl-item"><div class="tl-date">2025년 10월</div>
          <h3>관객이 연주자가 됩니다</h3>
          <p>은퇴 프레젠테이션 수녀 일곱 분과의 리코더 앙상블 준비 — 조사, 허가, 신원조회,
             개별 레슨.</p></div>
        <div class="tl-item"><div class="tl-date">2025년 12월</div>
          <h3>국립 콘서트홀에서</h3>
          <p>열다섯 번째 배움의 자리는 아일랜드 국립 콘서트홀에서 함께 본 공연이었습니다.</p></div>
        <div class="tl-item"><div class="tl-date">2026년 1–4월</div>
          <h3>파일럿, 그리고 그 음악회</h3>
          <p>Warrenmount에서 10주 합주, 이어 Clondalkin Lodge에서 아홉 곡의 부활 음악회.
             일곱 분 전원 수료.</p></div>
        <div class="tl-item"><div class="tl-date">2026년 8월</div>
          <h3>첫 공적 위촉</h3>
          <p>South Dublin Live 2026을 위한 두 번의 연주 — Tallaght University Hospital과
             Rua Red.</p></div>
        <div class="tl-item"><div class="tl-date">2026년 9월</div>
          <h3>모델이 일반에 열립니다</h3>
          <p>첫 커뮤니티 리코더 앙상블 과정이 Dublin 15 Mulhuddart Community Centre에서
             시작됩니다 — 12주, 무료.</p></div>
      </div>
      <div>
        <figure class="reveal">
          <div class="photo photo-4x3">
            <img src="images/letters-ensemble.jpg" width="1400" height="1050"
                 alt="악기를 든 Letters Ensemble 단원들">
          </div>
          <figcaption>2024년 1월에 만들어진 Letters Ensemble.</figcaption>
        </figure>
        <div class="callout reveal mt-3">
          <h3 class="h-sub">기사와 기고</h3>
          <ul class="plainlist mt-1">
            <li><strong>경향잡지</strong> 2026년 5월호 — 기획 &ldquo;청년, 어떻게 지내니&rdquo;
                청탁 원고</li>
            <li><strong>가톨릭대학교 학보</strong> 2026년 3월 — &ldquo;Fáilte go hÉirinn!&rdquo;</li>
            <li><strong>연주 후기</strong> 2025년 3월 — &ldquo;하느님께서 주신 모두를 위한 선물
                &lsquo;음악&rsquo;&rdquo;</li>
            <li><strong>The Echo</strong> 2026년 8월 — Rua Red·Tallaght 연주 광고</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

{CTA}"""


# ---------------------------------------------------------------------------

SUPPORT = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">후원</p>
    <h1>문이 계속 열려 있도록.</h1>
    <p>자원봉사로 운영합니다. 후원은 리코더와 악보, 공간 대여, 그리고 음악이 닿지 않았을 방까지
       데려다주는 이동에 쓰입니다.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">돈이 도는 방식</p>
      <h2>값을 치른 한 건이 무료 자리를 무료로 지킵니다.</h2>
      <p>우리는 순수 자선단체가 아니라 사회적기업입니다. 형식의 문제가 아닙니다 — 선의가
         잠시 식어도 무료 자리가 살아남게 하는 구조입니다.</p>
    </div>
    <div class="reveal">{dg.subsidy(L)}</div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">지금까지</p>
      <h2>누가 이 일을 받쳐 왔는가.</h2>
      <p>2026년 이전은 전부 자비와 자원봉사였습니다. 후원자의 첫 질문은 늘 &lsquo;앞서 누가
         했는가&rsquo;이기에 기록을 공개합니다.</p>
    </div>
    <div class="table-scroll reveal">
      <table>
        <thead><tr><th scope="col">출처</th><th scope="col">내용</th><th scope="col">상태</th></tr></thead>
        <tbody>
          <tr><td><strong>South Dublin County Council</strong><br><span class="tiny">예술과 ·
              South Dublin Live 2026</span></td>
              <td><em>Shared Voices of South Dublin</em> 시리즈 위촉 — 처음으로 공적 자금이
                  들어온 작업.</td><td>수령 완료</td></tr>
          <tr><td><strong>명도회 장학금</strong><br><span class="tiny">한국 천주교 주교회의
              평신도사도직위원회</span></td>
              <td>2025년 3월부터 학기별 지원, 창립자의 음악 사도직을 위한 것.</td><td>종료</td></tr>
          <tr><td><strong>개인 후원자</strong></td>
              <td>유럽과 한국의 후원자들이 정기적인 찾아가는 음악회가 가능하도록 보내 준
                  도움.</td><td>진행 중</td></tr>
          <tr><td><strong>파트너 공간, 현물</strong></td>
              <td>Tallaght University Hospital — 공간과 운영 시간. Mulhuddart Community Centre —
                  수업 공간. TU Dublin — 연습 공간.</td><td>계속</td></tr>
          <tr><td><strong>TU Dublin Venture Lab</strong></td>
              <td>사회적기업 창업 프로그램, 2024년 9월부터.</td><td>수료</td></tr>
        </tbody>
      </table>
    </div>
    <div class="split split-center reveal mt-4">
      <div class="quote">
        <p>&ldquo;그는 넉넉한 형편에서 이 일을 하는 것이 아닙니다. 개인적으로 제한된 재정 여건
           안에서도 시간과 에너지와 재능을 아낌없이 내어 주고 있습니다.&rdquo;</p>
        <cite>더블린 보좌주교 도날 로치 · 2026년 2월 16일</cite>
      </div>
      <div>
        <h3 class="h-sub">지지 서한</h3>
        <ul class="plainlist mt-2">
          <li><strong>Rua Red</strong> — South Dublin의 현대예술센터</li>
          <li><strong>The Civic Theatre</strong>, Tallaght</li>
          <li><strong>Tallaght University Hospital</strong> — National Centre for Arts &amp; Health</li>
          <li><strong>SDCC 예술과</strong> — South Dublin Live 2026 선정</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">돕는 방법</p>
      <h2>네 가지 후원, 모두 쓸모가 있습니다.</h2>
    </div>
    <div class="grid grid-4 stagger">
      <div class="card"><span class="kicker">01</span><h3>후원금</h3>
        <p>일시든 정기든 악기·교재·공간·이동에 쓰입니다. 메일 주시면 입금 정보와 함께
           무엇을 감당하게 되는지 알려 드립니다.</p></div>
      <div class="card"><span class="kicker">02</span><h3>프로그램 지원</h3>
        <p>재단·기금·지자체·기업 후원자를 위해 전체 제안서와 예산, 활동 기록을 요청 시
           보내 드립니다.</p></div>
      <div class="card"><span class="kicker">03</span><h3>문을 열어 주기</h3>
        <p>요양시설·본당·커뮤니티 센터·병원으로의 소개는 후원금만큼, 때로는 그보다 더
           큰 도움입니다.</p></div>
      <div class="card"><span class="kicker">04</span><h3>공간 내어 주기</h3>
        <p>한 학기 동안 매주 한 번 쓸 따뜻한 방 하나가 가장 값진 현물 후원입니다.
           그대로 무료 자리가 됩니다.</p></div>
    </div>
    <div class="btn-row reveal center-row mt-4">
      <a class="btn btn-accent" href="mailto:sby05034@gmail.com?subject=CMFE%20후원%20문의">후원 문의 <span class="arrow">→</span></a>
      <a class="btn btn-quiet" href="mailto:sby05034@gmail.com?subject=CMFE%20파트너십·펀딩%20문의">제안서 요청</a>
    </div>
    <div class="callout reveal mt-4">
      <p class="small"><strong>안내.</strong> CMFE는 자원봉사로 운영되는 사회적기업이며, 현재
         비영리 보증유한책임회사(CLG) 설립을 준비하고 있습니다. 아직 등록 자선단체가 아니므로
         기부금 세제 혜택은 적용되지 않습니다. 짐작하시게 두기보다 분명히 밝혀 두는 편이
         낫다고 생각합니다.</p>
    </div>
  </div>
</section>"""


# ---------------------------------------------------------------------------

CONTACT = """<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">문의</p>
    <h1>메일 주세요.</h1>
    <p>모든 문의는 창립자에게 바로 갑니다. 한 줄이면 충분합니다 — 무엇에 관한 것인지,
       어디에 계신지.</p>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="reveal">
      <h2>연락처</h2>
      <div class="table-scroll mt-3">
        <table><tbody>
          <tr><td><strong>이메일</strong></td>
              <td><a class="link" href="mailto:sby05034@gmail.com">sby05034@gmail.com</a></td></tr>
          <tr><td><strong>전화</strong></td>
              <td><a class="link" href="tel:+353830780635">+353 83 078 0635</a></td></tr>
          <tr><td><strong>거점</strong></td><td>아일랜드 더블린</td></tr>
          <tr><td><strong>활동 지역</strong></td>
              <td>더블린, Co. Meath, Co. Wicklow, Co. Westmeath — 그 밖도 협의</td></tr>
          <tr><td><strong>창립자</strong></td>
              <td>Andrew Seohyeon Kim (김서현), BMus (Hons), TU Dublin Conservatoire</td></tr>
          <tr><td><strong>언어</strong></td><td>한국어 · English</td></tr>
        </tbody></table>
      </div>
      <p class="small mt-3">공공배상책임보험을 보유하고 있으며, 활동이
         요구하는 경우 Garda 신원조회를 완료합니다. 파트너 공간에는 요청 시 서류를 보내
         드립니다.</p>
    </div>
    <div class="reveal">
      <h2>어떤 문의를 어떻게</h2>
      <ul class="checklist mt-3">
        <li><strong>수업 참여</strong> — 어느 장소인지, 악기를 다뤄 본 적이 있는지.
            &lsquo;전혀 없다&rsquo;도 아주 평범한 답입니다.</li>
        <li><strong>음악회 초대</strong> — 어떤 공간인지, 인원이 대략 얼마인지, 시기가
            언제쯤인지.</li>
        <li><strong>과정 개설</strong> — 방 하나, 요일, 담당자 한 분.</li>
        <li><strong>후원과 파트너십</strong> — 제안서와 예산을 요청해 주세요. 활동 기록과 함께
            보내 드립니다.</li>
        <li><strong>언론·취재</strong> — 약력, 사진, 프로그램 정보를 제공합니다.</li>
      </ul>
      <div class="btn-row">
        <a class="btn btn-accent" href="mailto:sby05034@gmail.com?subject=CMFE%20문의">메일 보내기 <span class="arrow">→</span></a>
        <a class="btn btn-quiet" href="get-involved.html">참여 방법 보기</a>
      </div>
    </div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap narrow center reveal">
    <p class="eyebrow center-row">단체 정보</p>
    <h2>Classical Music for Everyone</h2>
    <p class="lead mt-3">2024년 1월 더블린에서 시작한 커뮤니티 음악
       사회적기업이며, 현재 비영리 보증유한책임회사(CLG) 설립을 준비하고 있습니다.
       자원봉사로 운영합니다. 커뮤니티 음악 · 사회적기업 · 예술과 건강.</p>
  </div>
</section>"""
