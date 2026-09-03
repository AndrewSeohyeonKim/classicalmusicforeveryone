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
    <div class="stat"><b>40+</b><span>세션·공연</span></div>
    <div class="stat"><b>4</b><span>연주한 국가</span></div>
    <div class="stat"><b>20+</b><span>기관·공간</span></div>
    <div class="stat"><b>143</b><span>강의 누적 참석</span></div>
    <div class="stat"><b>7 / 7</b><span>파일럿 전원 수료</span></div>
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
  <div class="wrap narrow reveal" style="text-align:center;margin-inline:auto">
    <h2 style="font-size:clamp(26px,3.4vw,40px)">당신을 위한 자리가 있습니다.</h2>
    <p class="lead" style="margin-top:18px;color:var(--fg-inverse-muted)">
      처음 악기를 배우든, 들으러 오든, 함께 연주하든, 공간을 열어 주든 —
      한 줄이면 시작됩니다.</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn btn-accent" href="get-involved.html">참여하기 <span class="arrow">→</span></a>
      <a class="btn btn-on-dark" href="support.html">후원하기</a>
    </div>
  </div>
</section>"""


# ---------------------------------------------------------------------------

INDEX = f"""<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow lift lift-1">커뮤니티 음악 · 아일랜드 더블린</p>
      <h1><span class="line lift lift-1">클래식 음악을,</span><span class="line lift lift-2"><em>모두에게.</em></span></h1>
      <p class="lead lift lift-3">듣는 데서 그치지 않고 직접 연주하도록 가르칩니다.
         그리고 클래식 음악이 좀처럼 닿지 않는 곳으로 찾아갑니다.</p>
      <div class="btn-row lift lift-4">
        <a class="btn btn-primary" href="get-involved.html">수업 참여하기 <span class="arrow">→</span></a>
        <a class="btn btn-quiet" href="programmes.html">하는 일 보기</a>
      </div>
    </div>
    <figure class="lift lift-3">
      <div class="photo photo-3x2">
        <img src="../images/hero-outreach.jpg" width="1800" height="1350"
             alt="커뮤니티 홀에서 성 파트리치오 축일 음악회를 여는 연주자들">
      </div>
      <figcaption>한 수도 공동체를 위한 성 파트리치오 축일 음악회 — Letters Ensemble.</figcaption>
    </figure>
  </div>
</section>

{STATS}

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">지금</p>
      <h2>진행 중인 일.</h2>
    </div>
{WHATS_ON}
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">작동 방식</p>
      <h2>연주하기와 듣기가 서로를 먹여 살립니다.</h2>
      <p>찾아가서 연주합니다. 누군가 자기도 해 볼 수 있겠느냐고 묻습니다. 그 질문이 수업이 되고,
         그 수업이 다음 방에서 연주할 사람을 만듭니다.</p>
    </div>
    <div class="reveal">{dg.loop(L)}</div>
  </div>
</section>

<section class="band-photo">
  <img src="../images/church-concert.jpg" alt="" width="1400" height="1050">
  <div class="wrap narrow reveal">
    <p class="eyebrow">우리가 존재하는 이유</p>
    <h2 style="font-size:clamp(26px,3.6vw,42px)">존엄을 되찾아 주는 것은
       듣기가 아니라 연주하기입니다.</h2>
    <p class="lead" style="margin-top:20px;color:var(--fg-inverse-body)">
      클래식 음악은 풍요롭지만 여전히 많은 사람에게 닿지 않습니다 — 나이, 거동, 소득, 지역,
      그리고 그저 낯설다는 이유로. 요양시설도, 병원도, 쉼터도, 시골 본당도 관객이 없는 곳이
      아닙니다. 가장 오래 기다려 온 관객이 이미 그곳에 있습니다.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">하는 일</p>
      <h2>다섯 개의 프로그램, 하나의 믿음.</h2>
    </div>
    <div class="grid grid-3 stagger">
      <a class="card card-media" href="programmes.html">
        <div class="photo photo-3x2"><img src="../images/community-room.jpg" width="1400" height="1050"
             alt="커뮤니티 공간에서 클라리넷을 연주하는 모습"></div>
        <div class="card-body">
          <span class="kicker">대표 프로그램</span>
          <h3>리코더 앙상블</h3>
          <p>완전 초보를 위한 한 학기. 첫 주에 첫 소리, 마지막 주에 음악회.</p>
          <div class="meta">주 1회 · 커뮤니티 센터와 본당</div>
        </div>
      </a>
      <a class="card card-media" href="programmes.html">
        <div class="photo photo-3x2"><img src="../images/care-christmas.jpg" width="1400" height="1050"
             alt="성탄 시기 돌봄시설에서 연주하는 사중주"></div>
        <div class="card-body">
          <span class="kicker">찾아가는 음악회</span>
          <h3>음악이 찾아갑니다</h3>
          <p>요양시설·본당·병원·쉼터·커뮤니티 공간으로 실연을 가져갑니다.</p>
          <div class="meta">20회 · 4개국 · 15곳 이상</div>
        </div>
      </a>
      <a class="card card-media" href="programmes.html">
        <div class="photo photo-3x2"><img src="../images/lecture-recital.jpg" width="1400" height="1050"
             alt="강의·연주가 진행되는 모습"></div>
        <div class="card-body">
          <span class="kicker">배움</span>
          <h3>클래식 음악과 친해지기</h3>
          <p>사전 지식이 필요 없는 무료 강의·연주, 대략 월 1회.</p>
          <div class="meta">17회 · 누적 참석 143명</div>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap split split-center reveal">
    <div class="quote">
      <p>&ldquo;음악을 통해 그는 달리 고립감을 느낄 수 있는 이들에게 격려와 존엄,
         그리고 영적 동행을 건넵니다.&rdquo;</p>
      <cite>더블린 보좌주교 도날 로치 · 2026년 2월 16일</cite>
    </div>
    <div>
      <p class="eyebrow">기록으로 남은 것</p>
      <h3 style="font-size:25px">우리 아닌 누군가가 비용을 댔습니다.</h3>
      <p style="margin-top:14px">2026년 South Dublin County Council 예술과가 이 프로젝트를
         <strong>South Dublin Live 2026</strong>에 선정했습니다. 처음으로 공적 자금이 들어온
         일입니다. Rua Red, The Civic, Tallaght University Hospital의 지지 서한을 보유하고
         있습니다.</p>
      <div class="btn-row"><a class="btn btn-quiet" href="support.html">지금까지의 후원 <span class="arrow">→</span></a></div>
    </div>
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
      <p class="eyebrow" style="margin-top:38px">비전</p>
      <p class="lead">도시와 농촌, 돌봄 시설과 장애가 있는 삶 어디에서든 함께 음악을 만드는
         환대하는 통로가 있는 아일랜드. 그리고 그 일을 안정된 정규 고용 상태의 교육자들이
         수행하는 것.</p>
    </div>
    <figure class="reveal">
      <div class="photo photo-4x5">
        <img src="../images/clarinet.jpg" width="1400" height="1400"
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
  <img src="../images/organ.jpg" alt="" width="1400" height="1050">
  <div class="wrap split split-center">
    <div class="reveal">
      <p class="eyebrow">창립자</p>
      <h2 style="font-size:clamp(26px,3.2vw,38px)">Andrew Seohyeon Kim · 김서현</h2>
      <p class="lead" style="margin-top:18px;color:var(--fg-inverse-body)">
        클라리네티스트이자 오르가니스트, 커뮤니티 음악 실천가. TU Dublin Conservatoire 연주 전공
        음악학사(우등). 졸업 연구는 은퇴 프레젠테이션 수녀 일곱 분을 위해 직접 설계하고 이끈
        10주 리코더 앙상블이었습니다.</p>
      <p style="margin-top:14px;color:var(--fg-inverse-muted)">
        2022년부터 Dolphin&rsquo;s Barn 성모 통고 성당 음악감독, 2023년부터 Rathgar 삼주보 성당
        오르가니스트. 2024년에 Classical Music for Everyone과 Letters Ensemble을 창립했습니다.</p>
    </div>
    <div>
      <ul class="plainlist reveal" style="color:var(--fg-inverse-muted)">
        <li><strong style="color:var(--fg-inverse)">클라리넷</strong> — Dr Paul Roe, TU Dublin Conservatoire</li>
        <li><strong style="color:var(--fg-inverse)">오르간</strong> — Simon Harden</li>
        <li><strong style="color:var(--fg-inverse)">지휘</strong> — IAYO · London Conducting Workshop</li>
        <li><strong style="color:var(--fg-inverse)">사회적기업</strong> — TU Dublin Venture Lab</li>
        <li><strong style="color:var(--fg-inverse)">장학</strong> — 한국 천주교 주교회의
            평신도사도직위원회 명도회</li>
      </ul>
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
        <h4>아일랜드</h4>
        <ul class="plainlist" style="margin-top:14px">
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
        <h4>국외</h4>
        <ul class="plainlist" style="margin-top:14px">
          <li>루르드 성모 성지, 프랑스</li>
          <li>파리 외방 전교회 · Palais Brongniart, 파리</li>
          <li>런던 한인 천주교회, 영국</li>
          <li>관덕정 순교자 기념관, 대구, 한국</li>
        </ul>
        <div class="callout" style="margin-top:26px">
          <h4>주장하지 않는 것</h4>
          <p class="small" style="margin-top:10px">지금까지의 근거는 참여·지속·증언이지 측정된
             성과가 아닙니다. 검증된 도구로 웰빙을 측정한 적이 없고, 찾아가는 음악회의 관객 수도
             기록되지 않았습니다. 2026년 가을 기수부터 간단한 사전·사후 측정과 동의 절차를
             도입합니다.</p>
        </div>
      </div>
    </div>
  </div>
</section>

{CTA}"""


# ---------------------------------------------------------------------------

PROGRAMMES = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">프로그램</p>
    <h1>실제로 무엇을 하는가.</h1>
    <p>두 축 아래 다섯 갈래, 그리고 하나의 신앙 기반 하위 갈래. 리코더 앙상블 과정이 대표
       프로그램이고, 나머지는 그리로 이어지거나 거기서 자라났습니다.</p>
  </div>
</section>

<section class="tight">
  <div class="wrap reveal">
    <div class="table-scroll">
      <table>
        <thead><tr>
          <th scope="col">프로그램</th><th scope="col">축</th>
          <th scope="col">상태</th><th scope="col">지금까지</th>
        </tr></thead>
        <tbody>
          <tr><td><strong>리코더 앙상블 과정</strong></td><td>배움</td>
              <td>대표 · 진행 중</td><td>파일럿 완료, 2026년 9월 첫 커뮤니티 기수</td></tr>
          <tr><td><strong>클래식 음악과 친해지기</strong></td><td>배움</td>
              <td>진행 중 · 무료</td><td>강의·연주 17회 · 누적 참석 143명</td></tr>
          <tr><td><strong>함께하는 음악여행</strong></td><td>배움</td>
              <td>진행 중</td><td>기록된 동행 10회 (BBC Proms 2년 연속 포함)</td></tr>
          <tr><td><strong>찾아가는 음악회</strong></td><td>나눔</td>
              <td>진행 중</td><td>20회 · 4개국 · 15곳 이상</td></tr>
          <tr><td style="padding-inline-start:34px">↳ Bringing Music to Sacred Places</td><td>나눔</td>
              <td>하위 갈래</td><td>20회 중 약 16회</td></tr>
          <tr><td><strong>Letters Ensemble</strong></td><td>나눔</td>
              <td>진행 중</td><td>정식 음악회 4회 · 2024년 1월부터 주 1회 합주</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">대표 프로그램</p>
      <h2>한 학기, 아무것도 없는 데서 음악회까지.</h2>
      <p>리코더는 손과 호흡에 부담이 적고, 만족스러운 첫 소리가 빨리 나오고, 값이 싸고, 무엇보다
         함께 연주하기 위해 만들어진 악기입니다. 완전 초보에게 통하는 이유가 그것입니다.</p>
    </div>
    <div class="reveal">{dg.term(L)}</div>

    <div class="split" style="margin-top:52px">
      <div class="reveal">
        <h3>어떻게 진행되나</h3>
        <div class="table-scroll" style="margin-top:16px">
          <table><tbody>
            <tr><td><strong>기간</strong></td><td>한 학기, 주 1회</td></tr>
            <tr><td><strong>수업 시간</strong></td><td>60–90분</td></tr>
            <tr><td><strong>규모</strong></td><td>작고 편안한 그룹</td></tr>
            <tr><td><strong>악기</strong></td><td>소프라노 리코더 — 구입 안내, 원가 공급,
                대여 모두 가능</td></tr>
            <tr><td><strong>교재</strong></td><td>악보와 유인물을 직접 인쇄합니다.
                참가자 부담 없음</td></tr>
            <tr><td><strong>마무리</strong></td><td>가족·친구를 초대한 짧은 음악회</td></tr>
          </tbody></table>
        </div>
      </div>
      <div class="reveal">
        <h3>무엇이 남는가</h3>
        <ul class="checklist" style="margin-top:16px">
          <li><strong>연결</strong> — 매주 모일 따뜻한 이유.</li>
          <li><strong>존엄과 성취</strong> — &ldquo;나도 음악을 만들 수 있다&rdquo;는 조용한 자부심.</li>
          <li><strong>부드러운 자극</strong> — 기억력, 협응, 호흡, 집중.</li>
          <li><strong>우정</strong> — 학기가 끝난 뒤에도 남는 관계.</li>
        </ul>
        <div class="callout" style="margin-top:24px">
          <span class="tag tag-live">현재 진행</span>
          <p style="margin-top:12px"><strong>Mulhuddart Community Centre, Dublin 15.</strong>
             2026년 9월 9일부터 수요일 저녁 7:00–8:00, 12주, 무료 — 성탄 전 음악회로 마칩니다.</p>
          <div class="btn-row"><a class="btn btn-accent" href="get-involved.html">수업 참여하기 <span class="arrow">→</span></a></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split split-wide split-center">
    <div class="reveal">
      <p class="eyebrow">파일럿</p>
      <h2 style="font-size:clamp(24px,3vw,36px)">이 모델은 어디서 왔는가.</h2>
      <p class="lead" style="margin-top:18px">은퇴 프레젠테이션 수녀 일곱 분. Dublin 8
         Warrenmount에서 주 1회 한 시간씩 10주. Clondalkin Lodge에서 아홉 곡의 부활 음악회.
         TU Dublin Conservatoire 음악학사 연구로 수행되었습니다.</p>
      <p style="margin-top:16px">그 전에 석 달의 준비가 있었습니다 — 필요 조사, 허가, 신원조회,
         개별 레슨, 파트 배정. 소프라노·알토·테너·베이스 리코더에 멜로디카, 실로폰, 작은 타악기를
         더하고 악보는 크게 확대해 썼습니다. 일곱 분 전원이 수료하고 공개 연주까지 했습니다.</p>
    </div>
    <figure class="reveal">
      <div class="photo photo-4x3">
        <img src="../images/conducting.jpg" width="1400" height="1050"
             alt="커뮤니티 공간에서 작은 앙상블을 지휘하는 모습">
      </div>
      <figcaption>모든 과정은 같은 방식으로 끝납니다 — 작더라도 음악회로.</figcaption>
    </figure>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">나머지 프로그램</p>
      <h2>들어오는 네 가지 길.</h2>
    </div>
    <div class="grid grid-2 stagger">
      <article class="card"><span class="kicker">배움</span>
        <h3>클래식 음악과 친해지기</h3>
        <p>대략 월 1회 열리는 무료 강의·연주. 녹음과 실연을 함께 씁니다. 커리큘럼은
           <em>가까워지기</em>, <em>함께 경험하기</em>, <em>내 취향 찾기</em> 세 단계이고,
           유럽 여름 페스티벌·BBC Proms·웩스포드 오페라·성탄 특강이 계절마다 붙습니다.</p>
        <div class="meta">17회 · 보통 6–14명 · 무료</div>
      </article>
      <article class="card"><span class="kicker">배움</span>
        <h3>함께하는 음악여행</h3>
        <p>혼자서는 가지 않을 공연에 소그룹으로 동행합니다 — 국립교향악단, 아일랜드 국립 오페라,
           RTÉ 콘서트 오케스트라, 국립 콘서트홀 국제 시리즈, 2년 연속 BBC Proms. 사전 준비,
           현장 안내, 사후 나눔의 3단계.</p>
        <div class="meta">5명 내외 · 티켓이 £8인 공연도 있습니다</div>
      </article>
      <article class="card"><span class="kicker">나눔</span>
        <h3>찾아가는 음악회</h3>
        <p>요양시설·본당·병원·쉼터·커뮤니티 공간으로 실연을 가져갑니다 — 더블린 7구역의 노숙인
           쉼터에서 대구의 순교 성지까지. 확장 우선 지역은 위클로·미스·라우스입니다.</p>
        <div class="meta">2023년부터 · 연 10회 이상 목표</div>
      </article>
      <article class="card"><span class="kicker">나눔</span>
        <h3>Letters Ensemble</h3>
        <p>2024년 1월 더블린에 사는 아마추어 연주자들이 만들었습니다. 매주 토요일 연습.
           아일랜드 전통음악, 한국 전통음악, 성음악, 접근하기 쉬운 편곡 — 어떤 방에서든 절반쯤
           마주 나와 줄 수 있는 곡들로 고릅니다.</p>
        <div class="meta">정식 음악회 4회 · 아마추어 연주자에게 열려 있습니다</div>
      </article>
    </div>
    <div class="callout reveal" style="margin-top:26px">
      <span class="kicker" style="color:var(--accent);font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase">하위 갈래</span>
      <h3 style="margin-top:8px">Bringing Music to Sacred Places</h3>
      <p style="margin-top:10px">본당·성지·수도원·전례·은퇴 수도 공동체를 향한 신앙 기반 갈래로,
         스무 번의 찾아가는 음악회 가운데 약 열여섯 번이 여기 해당합니다. 교회 안에서는 음악을
         통한 평신도 사도직 — 연주 시리즈가 아니라 현존의 봉사로 설명합니다.</p>
    </div>
  </div>
</section>

{CTA}"""


# ---------------------------------------------------------------------------

GET_INVOLVED = """<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">참여하기</p>
    <h1>네 가지 길. 나에게 맞는 것을 고르면 됩니다.</h1>
    <p>오디션도, 사전 경험도, 준비할 것도 없습니다. 어디에 해당하는지 모르겠다면 그렇게 적어
       주세요. 아주 평범한 문의입니다.</p>
  </div>
</section>

<section>
  <div class="wrap">
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
           공공배상책임보험을 보유하고 있고, 필요한 경우 Garda 신원조회를 완료합니다.</p>
        <div class="meta">더블린·위클로·미스·라우스, 그 밖 지역도 협의</div>
      </article>
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
        <ul class="checklist" style="margin-top:16px">
          <li>열 명에서 열두 명이 둥글게 앉을 따뜻한 방, 학기 동안 주 1회</li>
          <li>지역에 알리는 일에 조금의 도움</li>
          <li>담당자 한 분</li>
          <li>그 밖에는 없습니다 — 장비도, 행정도, 피아노도</li>
        </ul>
      </div>
      <div>
        <h3>저희가 준비하는 것</h3>
        <ul class="checklist" style="margin-top:16px">
          <li>강사와 전체 커리큘럼</li>
          <li>모든 악보와 주간 교재 (저희 비용으로 인쇄)</li>
          <li>저렴한 악기 안내, 필요하면 대여</li>
          <li>학기 말 음악회</li>
          <li>보험·신원조회 서류</li>
        </ul>
      </div>
    </div>
    <div class="callout reveal" style="margin-top:30px">
      <p><strong>비용에 관하여.</strong> 모든 프로그램에 무료·할인 자리를 둡니다. 공간이 자체
         예산에서 진행비를 지불할 수 있으면 그 방에 있는 모든 분의 참여가 무료가 되고, 그 기여가
         다른 곳의 문을 열어 둡니다. 그럴 수 없더라도 우선 이야기부터 나눕니다.</p>
    </div>
  </div>
</section>

<section class="band-photo">
  <img src="../images/quartet-hall.jpg" alt="" width="1400" height="788">
  <div class="wrap narrow reveal" style="text-align:center;margin-inline:auto">
    <p class="eyebrow" style="justify-content:center">다음 단계</p>
    <h2 style="font-size:clamp(26px,3.4vw,40px)">한 줄만 적어 주세요.</h2>
    <p class="lead" style="margin-top:18px;color:var(--fg-inverse-body)">네 가지 중 어디에
       해당하는지, 그리고 대략 어디에 계신지. 구체적인 안내를 답장으로 보내 드립니다.</p>
    <div class="btn-row" style="justify-content:center">
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
    <div class="callout reveal" style="margin-top:26px">
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
        <div class="photo photo-3x2"><img src="../images/quartet-hall.jpg" width="1400" height="788"
             alt="밝은 홀에서 연주하는 앙상블"></div>
        <div class="card-body">
          <span class="tag tag-live">첫 공적 지원</span>
          <h3 style="margin-top:12px">South Dublin Live 2026</h3>
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
          <h4>시작 이전</h4>
          <p>루르드의 영어 미사에서 클라리넷 독주. 이름이 붙기 2년 전의 찾아가는 음악회.</p></div>
        <div class="tl-item"><div class="tl-date">2024년 1월</div>
          <h4>시작</h4>
          <p>더블린에서 CMFE가, 그리고 Letters Ensemble이 함께 만들어집니다. 첫 강의·연주는
             Dublin 18에서 여섯 명과 함께.</p></div>
        <div class="tl-item"><div class="tl-date">2024년</div>
          <h4>음악이 나갑니다</h4>
          <p>Dalgan Park와 성 골롬반 외방 선교 수녀회에서 음악회, 런던·파리·대구에서 연주.
             강의 시리즈는 TU Dublin으로 옮겨 갑니다.</p></div>
        <div class="tl-item"><div class="tl-date">2024–2025년</div>
          <h4>함께 갑니다</h4>
          <p>동행 관람이 독립된 갈래가 됩니다 — 국립교향악단, 아일랜드 국립 오페라, 2년 연속
             BBC Proms.</p></div>
        <div class="tl-item"><div class="tl-date">2025년 10월</div>
          <h4>관객이 연주자가 됩니다</h4>
          <p>은퇴 프레젠테이션 수녀 일곱 분과의 리코더 앙상블 준비 — 조사, 허가, 신원조회,
             개별 레슨.</p></div>
        <div class="tl-item"><div class="tl-date">2025년 12월</div>
          <h4>국립 콘서트홀에서</h4>
          <p>열다섯 번째 배움의 자리는 아일랜드 국립 콘서트홀에서 함께 본 공연이었습니다.</p></div>
        <div class="tl-item"><div class="tl-date">2026년 1–4월</div>
          <h4>파일럿, 그리고 그 음악회</h4>
          <p>Warrenmount에서 10주 합주, 이어 Clondalkin Lodge에서 아홉 곡의 부활 음악회.
             일곱 분 전원 수료.</p></div>
        <div class="tl-item"><div class="tl-date">2026년 8월</div>
          <h4>첫 공적 위촉</h4>
          <p>South Dublin Live 2026을 위한 두 번의 연주 — Tallaght University Hospital과
             Rua Red.</p></div>
        <div class="tl-item"><div class="tl-date">2026년 9월</div>
          <h4>모델이 일반에 열립니다</h4>
          <p>첫 커뮤니티 리코더 앙상블 과정이 Dublin 15 Mulhuddart Community Centre에서
             시작됩니다 — 12주, 무료.</p></div>
      </div>
      <div>
        <figure class="reveal">
          <div class="photo photo-4x3">
            <img src="../images/letters-ensemble.jpg" width="1400" height="1050"
                 alt="악기를 든 Letters Ensemble 단원들">
          </div>
          <figcaption>2024년 1월에 만들어진 Letters Ensemble.</figcaption>
        </figure>
        <div class="callout reveal" style="margin-top:26px">
          <h4>기사와 기고</h4>
          <ul class="plainlist" style="margin-top:12px">
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
    <div class="split split-center reveal" style="margin-top:48px">
      <div class="quote">
        <p>&ldquo;그는 넉넉한 형편에서 이 일을 하는 것이 아닙니다. 개인적으로 제한된 재정 여건
           안에서도 시간과 에너지와 재능을 아낌없이 내어 주고 있습니다.&rdquo;</p>
        <cite>더블린 보좌주교 도날 로치 · 2026년 2월 16일</cite>
      </div>
      <div>
        <h4>지지 서한</h4>
        <ul class="plainlist" style="margin-top:14px">
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
    <div class="btn-row reveal" style="justify-content:center;margin-top:36px">
      <a class="btn btn-accent" href="mailto:sby05034@gmail.com?subject=CMFE%20후원%20문의">후원 문의 <span class="arrow">→</span></a>
      <a class="btn btn-quiet" href="mailto:sby05034@gmail.com?subject=CMFE%20파트너십·펀딩%20문의">제안서 요청</a>
    </div>
    <div class="callout reveal" style="margin-top:34px">
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
      <div class="table-scroll" style="margin-top:24px">
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
      <p class="small" style="margin-top:22px">공공배상책임보험을 보유하고 있으며, 활동이
         요구하는 경우 Garda 신원조회를 완료합니다. 파트너 공간에는 요청 시 서류를 보내
         드립니다.</p>
    </div>
    <div class="reveal">
      <h2>어떤 문의를 어떻게</h2>
      <ul class="checklist" style="margin-top:24px">
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
  <div class="wrap narrow reveal" style="text-align:center;margin-inline:auto">
    <p class="eyebrow" style="justify-content:center">단체 정보</p>
    <h2>Classical Music for Everyone</h2>
    <p class="lead" style="margin-top:22px">2024년 1월 더블린에서 시작한 커뮤니티 음악
       사회적기업이며, 현재 비영리 보증유한책임회사(CLG) 설립을 준비하고 있습니다.
       자원봉사로 운영합니다. 커뮤니티 음악 · 사회적기업 · 예술과 건강.</p>
  </div>
</section>"""
