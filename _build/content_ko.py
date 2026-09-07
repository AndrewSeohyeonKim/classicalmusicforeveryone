# -*- coding: utf-8 -*-
"""한국어 페이지 내용. 사실관계는 정본 세트(00_최종본, 2026-08-27)를 따릅니다.

이 파일의 원칙: 한 섹션당 두세 문장. 그보다 길어지는 설명은 문단이 아니라
도식·표·캡션으로 옮깁니다.
"""

import diagrams as dg
from content_en import social_links

L = "ko"

# ---------------------------------------------------------------------------

# 홈은 더 이상 숫자 띠로 시작하지 않습니다. 무엇을 하는 곳인지 말하기도 전에
# 몇 번 했는지부터 세면, 하는 일이 아니라 실적표처럼 읽힙니다. 같은 숫자는
# 그것이 근거로 쓰이는 자리에 그대로 있습니다 — 소개 페이지, 프로그램 페이지,
# 그리고 이 페이지 아래쪽 "신뢰의 근거".

WHATS_ON = """<div class="grid grid-2 stagger">
  <div class="notice">
    <span class="tag tag-live">모집 중</span>
    <h3>리코더 앙상블 — Mulhuddart</h3>
    <p class="small">12주 과정입니다. 악기를 한 번도 잡아 본 적 없어도, 악보를 못 읽어도 됩니다.</p>
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
    <h2 class="h-lg">여기 당신 자리가 있습니다.</h2>
    <p class="lead mt-2">
      악기를 처음 배우든, 들으러 오든, 같이 연주하든, 방을 하나 내어 주시든.
      메일 한 줄이면 시작됩니다.</p>
    <div class="btn-row center-row">
      <a class="btn btn-accent" href="get-involved.html">참여하기 <span class="arrow">→</span></a>
      <a class="btn btn-on-dark" href="support.html">후원하기</a>
    </div>
  </div>
</section>"""


_MAIL_PARTNER_HOME = ("mailto:sby05034@gmail.com?subject=%ED%8C%8C%ED%8A%B8%EB%84%88%EC%8B%AD%20%EB%AC%B8%EC%9D%98"
                      "&body=%EA%B8%B0%EA%B4%80%3A%20%0A%EC%9C%84%EC%B9%98%3A%20%0A%EA%B3%B5%EA%B0%84%EA%B3%BC%20%EA%B0%80%EB%8A%A5%ED%95%9C%20%EB%82%A0%EC%A7%9C%3A%20%0A"
                      "%EC%83%9D%EA%B0%81%ED%95%98%EC%8B%9C%EB%8A%94%20%EA%B2%83%20%ED%95%9C%20%EC%A4%84%3A%20")

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
      <p class="lead lift lift-3">악기를 직접 잡고 소리를 내도록 가르칩니다.
         그리고 클래식 음악이 좀처럼 가지 않는 곳으로 저희가 갑니다.</p>
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


<section>
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">우리가 하는 일</p>
      <h2>가르치는 일 셋, 찾아가는 일 둘.</h2>
      <p>악기를 가르치는 프로그램이 셋, 공연장까지 오기 어려운 분들을 찾아가 연주하는
         프로그램이 둘입니다. 이 둘은 붙어 있습니다. 찾아간 방에서 다음 수업이 생기고,
         그 수업에서 다음 연주자가 나옵니다.</p>
    </div>
    <div class="pillar-bar reveal" aria-hidden="true">
      <div class="pillar-span">
        <b>배움</b><span>악기를 직접 잡도록 가르칩니다. 셋 다 아무것도 모르는
        자리에서 시작합니다.</span>
      </div>
      <div class="pillar-span pillar-b">
        <b>나눔</b><span>음악이 좀처럼 가지 않는 곳으로 저희가 갑니다.</span>
      </div>
    </div>
    <div class="grid grid-5 stagger">
      <a class="prog" href="programmes/recorder-ensemble.html">
        <div class="photo photo-3x2"><img src="images/conducting.jpg" width="1400" height="933" alt="더블린의 한 커뮤니티 공간에서 진행하는 주간 수업"></div>
        <div class="prog-body">
          <span class="kicker">배움</span>
          <h3>무료 리코더 앙상블 과정</h3>
          <p>악기를 처음 잡는 분들과 한 학기. 끝은 음악회입니다.</p>
          <div class="meta">주 1회 · 한 학기</div>
        </div>
      </a>
      <a class="prog" href="programmes/getting-to-know.html">
        <div class="photo photo-3x2"><img src="images/lecture-recital.jpg" width="1400" height="933" alt="진행 중인 강의·연주"></div>
        <div class="prog-body">
          <span class="kicker">배움</span>
          <h3>클래식 음악과 친해지기</h3>
          <p>아무것도 몰라도 되는 무료 강의·연주.</p>
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
          <p>요양시설과 본당, 병원과 쉼터로 연주를 들고 갑니다.</p>
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
  <img src="images/ruared-stage.jpg" alt="" width="1400" height="933">
  <div class="wrap narrow reveal">
    <p class="eyebrow">왜 이 일을 하는가</p>
    <h2 class="h-lg">그 방에도 관객은
       이미 앉아 있습니다.</h2>
    <p class="lead mt-3">
      클래식 음악은 풍요롭습니다. 그런데 여전히 많은 사람에게 닿지 않습니다.
      나이가 많아서, 몸이 아파서, 형편이 빠듯해서, 사는 곳이 멀어서, 그저 낯설어서.
      요양시설과 병원, 쉼터와 시골 본당에는 가장 오래 기다린 관객이 앉아 있습니다.
      아무도 찾아가지 않았을 뿐입니다.</p>
    <div class="btn-row"><a class="btn btn-on-dark" href="about.html">단체 소개 <span class="arrow">→</span></a></div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap split split-wide split-center">
    <div class="reveal">
      <p class="eyebrow">이야기 하나</p>
      <h2>뒷줄에서 나온 질문.</h2>
      <p class="lead mt-3">2024년 11월, Letters Ensemble이 위클로 주의 성 골롬반 선교
         수녀회에서 연주했습니다. 연주가 끝나고 한 수녀님이 물었습니다. 다시 연주할 수
         있을까요. 오래전에 바이올린을 켰다고 했습니다.</p>
      <p class="mt-3">그 질문이 은퇴 프레젠테이션 수녀 일곱 분의 리코더 앙상블이 됐습니다.
         10주의 연습, 아홉 곡의 부활 음악회, 일곱 분 전원 수료. 2026년 9월, 같은 과정이
         멀허다트에서 누구에게나 무료로 열렸습니다. 질문 하나, 한 학기, 열린 문 하나.
         이 모델의 전부입니다.</p>
      <div class="btn-row"><a class="btn btn-quiet" href="impact.html">기록이 뒷받침하는 것 <span class="arrow">&rarr;</span></a></div>
    </div>
    <figure class="reveal">
      <div class="photo photo-4x3">
        <img src="images/letters-ensemble.jpg" width="1400" height="1050"
             alt="악기를 든 Letters Ensemble 단원들">
      </div>
      <figcaption>Letters Ensemble. 2024년 11월 위클로 주 음악회가 가르치는 프로그램의
        출발점이 됐습니다.</figcaption>
    </figure>
  </div>
</section>

<section class="band-mark">
  <div class="wrap split split-wide split-center">
    <div class="reveal">
      <p class="eyebrow">이름이 곧 숙제입니다</p>
      <h2>금색은 <em>Everyone</em> 위에 놓입니다.</h2>
      <p class="lead mt-3">로고에서 &lsquo;for&rsquo;는 작게, &lsquo;Everyone&rsquo;은 크고
         금색으로 놓습니다. 이 이름에서 지키기 어려운 낱말이 마지막 낱말이라서 그렇습니다.</p>
      <p class="mt-3">이 음악에 부족한 건 관객이 아니라 길입니다. 나이가 많거나, 몸이
         아프거나, 도시에서 멀거나, 형편이 빠듯하거나, 이 음악이 자기 것이라는 말을 한 번도
         못 들어 본 사람이 걸어 들어올 길. 저희가 무엇으로 평가받아야 하는지는 로고에 이미
         적혀 있습니다.</p>
      <p class="footer-line mark-line">클래식 음악을, 그것이 필요한 곳으로!</p>
    </div>
    <figure class="reveal mark-plate">
      <img src="assets/logo-horizontal.svg" width="341" height="131"
           alt="Classical Music for Everyone 로고 — 높은음자리표와 워드마크. &lsquo;Everyone&rsquo;이 크고 금색으로 놓여 있다">
      <figcaption>가로형 로고, 2026년 8월 17일 확정.
        <a class="link" href="identity.html">디자인 표준 전체 보기</a></figcaption>
    </figure>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">무엇을 향해 가는가</p>
      <h2>목표는 둘입니다. 두 번째가 훨씬 어렵습니다.</h2>
      <p>첫 번째는 음악 단체라면 으레 기대하실 만한 것입니다. 두 번째 때문에 저희는
         자선단체 대신 사회적기업을 택했습니다.</p>
    </div>
    <div class="grid grid-2 stagger">
      <div class="card"><span class="kicker">목표 01</span>
        <h3>누구든 들어설 수 있는 길</h3>
        <p>나이가 몇이든, 어디서 왔든, 몸이 어떻든, 형편이 어떻든, 음악을 알든 모르든
           실황 연주를 만날 수 있게 합니다. 악기를 가르치고, 옆에 앉아 함께 연주하고,
           음악이 평소에 가지 않는 곳까지 찾아갑니다.</p>
        <div class="meta">다섯 개 프로그램 &middot; 무료·감면 자리는 언제나 확보</div>
      </div>
      <div class="card"><span class="kicker">목표 02</span>
        <h3>음악교육자의 제대로 된 일자리</h3>
        <p>음악교육자는 대부분 불안정한 프리랜서로 일합니다. 이들을 제대로 된 급여의
           정규직으로 채용하는 것이 저희의 두 번째 사회적 목표입니다. 형편이 나아지면
           그때 하겠다는 약속이 아닙니다. 이 단체가 있는 이유의 절반입니다.</p>
        <div class="meta">현재는 자원봉사 운영 &middot; 비영리 CLG 설립 준비 중</div>
      </div>
    </div>
    <div class="next reveal mt-4">
      <p class="eyebrow">가려는 곳</p>
      <ol class="next-list">
        <li><b>마침</b><span>2024년 창립 &middot; 파일럿 완료 &middot; 첫 공적 위촉 &middot; 첫 커뮤니티 과정</span></li>
        <li><b>다음</b><span>이사진을 갖춘 비영리 보증유한책임회사로 법인 설립</span></li>
        <li><b>그다음</b><span>두 번째 기수, 그리고 위클로·미스·라우스의 방들</span></li>
        <li><b>그다음</b><span>첫 음악 교육가를 정식으로 고용</span></li>
        <li><b>그다음</b><span>웰빙을 재어 이 사이트에 보고</span></li>
      </ol>
      <div class="btn-row">
        <a class="btn btn-quiet" href="impact.html#next">가는 길, 순서대로 <span class="arrow">&rarr;</span></a>
        <a class="btn btn-quiet" href="about.html">미션과 가치, 그리고 창립자</a>
      </div>
    </div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">후원이 이미 바꾼 것</p>
      <h2>차가 생겼고, 그만큼 멀리 갑니다.</h2>
      <p>지금은 자원봉사로 운영하고 있고, 비영리 보증유한책임회사(CLG) 설립을 준비하는
         중입니다. 그 절차가 끝나기 전까지 보여 드릴 자선단체 등록번호가 없으니,
         대신 실제로 있었던 일을 적습니다.</p>
    </div>
    <div class="evidence stagger">
      <div><dl>
        <dt>후원으로 마련한 차량</dt>
        <dd>개인 후원이 모여 <strong>차량 한 대</strong>가 생겼습니다. 연주자와 악기와
            보면대를 한 번에 싣고, 버스로는 갈 수 없던 곳까지 갑니다.</dd>
      </dl></div>
      <div><dl>
        <dt>그래서 닿은 곳</dt>
        <dd>아일랜드·프랑스·영국·한국 <strong>네 나라</strong>의 <strong>20곳 이상</strong>.
            요양시설, 본당, 병원, 쉼터, 주간보호센터, 커뮤니티 센터.</dd>
      </dl></div>
      <div><dl>
        <dt>공적 위촉 한 건</dt>
        <dd>사우스더블린 카운티 의회 예술과가 <strong>South Dublin Live 2026</strong>에 이
            프로젝트를 선정했습니다. Rua Red, The Civic, Tallaght University Hospital은
            그 신청을 위해 지지 서한을 써 주었습니다.</dd>
      </dl></div>
    </div>
    <div class="quote reveal mt-4">
      <p>&ldquo;음악으로, 그는 홀로 남았을 이들에게 격려와 존엄과
         영적인 동행을 건넵니다.&rdquo;</p>
      <cite>더블린 보좌주교 도날 로치 · 2026년 2월 16일</cite>
    </div>
    <p class="lead center mt-4 reveal">다음 후원도 마찬가지입니다.
       못 가던 방 하나가 갈 수 있는 방이 됩니다.</p>
    <div class="btn-row center-row reveal">
      <a class="btn btn-quiet" href="impact.html">날짜가 있는 숫자, 그리고 증명되지 않은 것 <span class="arrow">→</span></a>
      <a class="btn btn-quiet" href="support.html">후원이 쓰이는 곳</a>
    </div>
  </div>
  <div class="ticker mt-4" aria-label="함께한 기관">
    <p class="eyebrow center-row">저희가 연주한 방들</p>
    <div class="ticker-track">
      <ul>
        <li>Tallaght University Hospital</li><li>Rua Red</li><li>The Civic Theatre</li>
        <li>Clondalkin Lodge</li><li>Mulhuddart Community Centre</li><li>프레젠테이션 수녀회</li>
        <li>성 골롬반 선교 수녀회</li><li>Dalgan Park</li><li>TU Dublin</li>
        <li>국립 콘서트홀</li><li>Our Lady of Dolours, Dolphin&rsquo;s Barn</li>
        <li>Church of the Three Patrons, Rathgar</li><li>HSE EVE Goirtin Hub</li>
        <li>Morning Star Hostel</li><li>파리 외방전교회</li>
        <li>루르드 성모 성지</li><li>런던 한인 천주교회</li>
        <li>관덕정 순교기념관, 대구</li>
      </ul>
      <ul aria-hidden="true">
        <li>Tallaght University Hospital</li><li>Rua Red</li><li>The Civic Theatre</li>
        <li>Clondalkin Lodge</li><li>Mulhuddart Community Centre</li><li>프레젠테이션 수녀회</li>
        <li>성 골롬반 선교 수녀회</li><li>Dalgan Park</li><li>TU Dublin</li>
        <li>국립 콘서트홀</li><li>Our Lady of Dolours, Dolphin&rsquo;s Barn</li>
        <li>Church of the Three Patrons, Rathgar</li><li>HSE EVE Goirtin Hub</li>
        <li>Morning Star Hostel</li><li>파리 외방전교회</li>
        <li>루르드 성모 성지</li><li>런던 한인 천주교회</li>
        <li>관덕정 순교기념관, 대구</li>
      </ul>
    </div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap split split-center">
    <div class="reveal">
      <p class="eyebrow">기관을 위한 안내</p>
      <h2>요양시설이나 병원, 본당이신가요?</h2>
      <p class="lead mt-3">방과 날짜만 알려 주세요. 문의는 2분이면 되고, 방을 뺀 나머지는
         전부 저희가 가져갑니다. 연주자, 악기, 보면대, 프로그램, 보험까지.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="partner.html">기관 파트너십 <span class="arrow">&rarr;</span></a>
        <a class="btn btn-quiet" href="{_MAIL_PARTNER_HOME}">2분이면 되는 메일</a>
      </div>
    </div>
    <div class="reveal">
      <ul class="checklist">
        <li><strong>요양시설과 병원</strong> &mdash; 휴게실이나 아트리움에서 30분에서 60분,
            어쿠스틱으로, 관객이 낼 돈 없이.</li>
        <li><strong>본당과 수도 공동체</strong> &mdash; 전례 음악, 또는 미사 뒤의 음악회.
            스무 번의 찾아가는 음악회 가운데 열여섯 번쯤이 성지와 본당이었습니다.</li>
        <li><strong>커뮤니티 센터</strong> &mdash; 여러분의 방에서 여는 한 학기 초보 과정.
            방과 담당자만 주시면 나머지는 저희가 합니다.</li>
        <li><strong>지자체, 재단, 기업</strong> &mdash; 시즌을 후원하거나, 자리를 후원하거나,
            사람을 데려오거나. 모든 파트너십에 담당자의 이름과 날짜 있는 보고가 따라옵니다.</li>
      </ul>
    </div>
  </div>
</section>

{CTA}"""


# ---------------------------------------------------------------------------

ABOUT = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">단체 소개</p>
    <h1>악기를 가르칩니다. 그리고 음악이 가지 않는 곳으로 갑니다.</h1>
    <p><span class="brandname">Classical Music for Everyone</span>은 클래식 음악이 가장 닿지
       않는 곳으로 클래식 음악을 가져가는 더블린의 사회적기업입니다. 요양시설과 병원과
       본당에서 실황으로 연주하고, 나이 든 참가자들이 직접 연주하는 앙상블을 운영하며,
       누구나 올 수 있는 감상 강의를 엽니다. 나이도, 건강도, 소득도 음악을 들을 자격을
       정하지 않는다고 믿기 때문입니다.</p>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <dl class="glance reveal">
      <div><dt>창립</dt><dd>2024년 1월<small>아일랜드 더블린</small></dd></div>
      <div><dt>하는 일</dt><dd>프로그램 다섯<small>두 축: 배움과 나눔</small></dd></div>
      <div><dt>연주한 나라</dt><dd>네 나라<small>아일랜드 · 프랑스 · 영국 · 한국</small></dd></div>
      <div><dt>지위</dt><dd>자원봉사 운영<small>비영리 CLG 설립 준비 중</small></dd></div>
    </dl>
  </div>
</section>

<section>
  <div class="wrap split split-wide split-center">
    <div class="reveal">
      <p class="eyebrow">미션</p>
      <p class="statement">실황 클래식 음악을 <em>누구나 만날 수 있게.</em> 나이가 몇이든,
         몸이 어떻든, 형편이 어떻든, 음악을 알든 모르든.</p>
      <p class="mt-3">악기를 가르치고, 옆에 앉아 함께 연주하고, 음악이 평소에 가지 않는
         곳까지 찾아갑니다.</p>
      <p class="eyebrow mt-4">비전</p>
      <p class="statement statement-sm">모든 공동체에 함께 음악을 만드는 길이 있는 아일랜드.
         <em>그 안에서 일하는 교육자는 안정된 자리에서 일합니다.</em></p>
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
      <p class="eyebrow">가치</p>
      <h2>다섯 가지. 하나하나 무언가를 치릅니다.</h2>
    </div>
    <ol class="values reveal">
      <li><i>01</i><b>존엄</b><span>나이와 건강이 어떻든, 여전히 무언가를 만들 수 있는 사람으로 대합니다.</span></li>
      <li><i>02</i><b>접근성</b><span>값, 거리, 낯섦의 문턱을 낮춥니다.</span></li>
      <li><i>03</i><b>동행</b><span>한 번 다녀오고 마는 대신 한 학기를 함께 머뭅니다.</span></li>
      <li><i>04</i><b>공동체</b><span>나이도 출신도 언어도 다른 사람들을 한 방에 앉히는 음악.</span></li>
      <li><i>05</i><b>희망</b><span>인생이 바뀐다고 약속하지 않습니다. 작지만 진짜인 순간을 셉니다.</span></li>
    </ol>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">하는 일</p>
      <h2>프로그램 다섯, 축 둘, 한 바퀴.</h2>
    </div>
    <div class="reveal">{dg.loop(L)}</div>
    <div class="btn-row reveal">
      <a class="btn btn-primary" href="programmes.html">다섯 프로그램 전체 <span class="arrow">&rarr;</span></a>
      <a class="btn btn-quiet" href="get-involved.html">참여하는 방법</a>
    </div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">연주해 온 곳</p>
      <h2>음악이 잘 들어가지 않는 방들.</h2>
      <p>요양시설, 수도 공동체, 본당, 병원, 노숙인 쉼터, HSE 주간 돌봄 서비스, 커뮤니티 센터,
         대학교. 그리고 국립 콘서트홀에는 함께 갔습니다.</p>
    </div>
    <ul class="names reveal">
      <li>Tallaght University Hospital</li><li>Rua Red, Tallaght</li><li>Clondalkin Lodge</li>
      <li>Warrenmount, Dublin 8</li><li>Mulhuddart Community Centre</li>
      <li>성 골롬반 선교 수녀회, 위클로</li><li>마리아의 프란치스코 선교 수녀회</li>
      <li>Dalgan Park, 미스</li><li>Kilmessan 성당</li><li>Dysart 본당, 웨스트미스</li>
      <li>HSE EVE Goirtin Hub</li><li>Morning Star Hostel</li><li>TU Dublin</li>
      <li>국립 콘서트홀</li><li>Our Lady of Dolours, Dolphin&rsquo;s Barn</li>
      <li>Church of the Three Patrons, Rathgar</li><li>가르멜 커뮤니티 센터</li>
      <li>Blessed Sacrament Chapel</li><li>루르드 성모 성지</li>
      <li>파리 외방전교회</li><li>팔레 브로냐르, 파리</li>
      <li>런던 한인 천주교회</li><li>관덕정 순교기념관, 대구</li>
    </ul>
    <p class="tiny mt-3 reveal">지금 내놓을 수 있는 근거는 사람들이 왔고, 계속 왔고, 이런 말을 해
       주었다는 것까지입니다. 증명한 것과 못 한 것은
       <a class="link" href="impact.html#transparency">성과 페이지</a>에 적어 두었습니다.</p>
  </div>
</section>

<section class="band-photo" id="founder">
  <img src="images/organ.jpg" alt="" width="1400" height="1050">
  <div class="wrap split split-center">
    <div class="reveal">
      <p class="eyebrow">창립자</p>
      <h2 class="h-lg">김서현 · Andrew Seohyeon Kim</h2>
      <p class="lead mt-3">클라리네티스트, 오르가니스트, 커뮤니티 음악 실천가. 전부 같은 방 안에
         있습니다. 강사, 진행자, 운전자, 연주자, 지휘자가 한 사람입니다.</p>
      <div class="btn-row"><a class="btn btn-on-dark" href="founder.html">누구인지, 어떻게 일하는지 <span class="arrow">&rarr;</span></a></div>
    </div>
    <figure class="reveal">
      <div class="photo photo-4x5" style="max-width:300px">
        <img src="images/ruared-andrew.jpg" width="933" height="1400"
             alt="스테인드글라스 아래에서 클라리넷을 연주하는 김서현">
      </div>
    </figure>
  </div>
</section>

<section class="band-raised" id="identity">
  <div class="wrap split split-wide split-center">
    <div class="reveal">
      <p class="eyebrow">아이덴티티</p>
      <h2>금색은 <em>Everyone</em> 위에 놓입니다.</h2>
      <p class="lead mt-3">로고와 색과 서체, 그리고 그것을 쓰는 규칙은 따로 한 페이지에
         공개해 두었습니다. 저희 이름을 인쇄하는 누구든 그 기준으로 저희를 붙들어 두실 수
         있도록.</p>
      <div class="btn-row"><a class="btn btn-quiet" href="identity.html">상징과 표준 <span class="arrow">&rarr;</span></a></div>
    </div>
    <figure class="reveal mark-plate">
      <img src="assets/logo-horizontal.svg" width="341" height="131"
           alt="Classical Music for Everyone 로고 — 높은음자리표와 워드마크. &lsquo;Everyone&rsquo;이 크고 금색으로 놓여 있다">
      <figcaption>가로형 로고, 2026년 8월 17일 확정.</figcaption>
    </figure>
  </div>
</section>

{CTA}"""


# ---------------------------------------------------------------------------
# 창립자 — 이력서 대신 아티스트 프로필로
# ---------------------------------------------------------------------------

FOUNDER = f"""<section class="founder-hero">
  <div class="wrap founder-grid">
    <figure class="lift lift-2">
      <div class="photo photo-4x5">
        <img src="images/founder-portrait.jpg" width="790" height="1400"
             alt="스테인드글라스 아래에서 클라리넷을 연주하는 김서현">
      </div>
    </figure>
    <div>
      <p class="eyebrow lift lift-1">창립자</p>
      <h1 class="lift lift-2">김서현<span class="founder-kr">Andrew Seohyeon Kim</span></h1>
      <p class="founder-role lift lift-3">클라리네티스트, 오르가니스트, 커뮤니티 음악 실천가.
         <span class="brandname">Classical Music for Everyone</span>과 Letters Ensemble의 창립자.
         더블린.</p>
      <p class="statement lift lift-3">&ldquo;사람들이 음악에 오기를 기다리는 대신,
         <em>음악이 사람들에게 갑니다.</em>&rdquo;</p>
      <div class="lift lift-4">{social_links("이메일")}</div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split split-wide split-center">
    <div class="reveal">
      <p class="eyebrow">일하는 방식</p>
      <h2>전부 같은 방 안에 있습니다.</h2>
      <p class="lead mt-3">리코더 수업의 강사, 강의·연주의 진행자, 동행을 예약하는 사람,
         요양시설에서 클라리넷을 부는 연주자, 그 자리에서 앙상블을 지휘하는 사람이 같은 한
         사람입니다.</p>
      <p class="mt-3">이건 설명인 동시에 한계입니다. 주당 50회 대신 다섯 개 프로그램인 이유가
         여기 있고, 음악교육자를 제대로 고용하는 일을 두 번째 사회적 목표로 못 박아 둔 이유도
         같습니다. 이 일은 한 사람 위에서 커지지 않고, 커져서도 안 됩니다.</p>
    </div>
    <div class="reveal">
      <dl class="facts">
        <dt>활동</dt><dd>아일랜드 더블린</dd>
        <dt>학업</dt><dd>연주 전공 음악학사(우등), TU Dublin Conservatoire, 2026</dd>
        <dt>클라리넷</dt><dd>Dr Paul Roe &middot; 오르간은 Simon Harden</dd>
        <dt>맡은 자리</dt><dd>Dolphin&rsquo;s Barn 성모 통고 성당 음악감독 &middot; Rathgar 삼주보 성당 오르가니스트</dd>
        <dt>창립</dt><dd><span class="brandname">Classical Music for Everyone</span>과 Letters Ensemble, 2024년 1월</dd>        <dt>언어</dt><dd>한국어 &middot; 영어</dd>
      </dl>
    </div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">무대 위, 2026년 8월</p>
      <h2 class="h-md">South Dublin Live: 병원 아트리움과 블랙박스 극장.</h2>
    </div>
    <div class="gallery stagger">
      <figure><div class="photo photo-3x2"><img src="images/ruared-stage.jpg" width="1400" height="933"
          alt="객석에서 본 Rua Red 무대의 트리오"></div>
        <figcaption>Rua Red, 8월 29일. 사진: Ben Ryan / South Dublin County Council</figcaption></figure>
      <figure><div class="photo photo-4x5"><img src="images/tuh-andrew.jpg" width="1050" height="1400"
          alt="병원 아트리움에서 클라리넷을 연주하는 김서현"></div>
        <figcaption>Tallaght University Hospital, 8월 20일.</figcaption></figure>
      <figure><div class="photo photo-4x5"><img src="images/ruared-andrew.jpg" width="933" height="1400"
          alt="무대 조명 아래에서 클라리넷을 연주하는 김서현"></div>
        <figcaption>Rua Red. 사진: Ben Ryan / South Dublin County Council</figcaption></figure>
      <figure><div class="photo photo-3x2"><img src="images/tuh-trio.jpg" width="1400" height="787"
          alt="병원 아트리움에서 연주하는 소프라노·피아노·클라리넷"></div>
        <figcaption>Shared Voices of Care, 안수정·정혜리와 함께.</figcaption></figure>
    </div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap aside-fig">
    <figure class="reveal">
      <div class="photo photo-4x5" style="max-width:440px">
        <img src="images/founder-speaking.jpg" width="1050" height="1400"
             alt="강의·연주에서 마이크를 들고 이야기하는 김서현">
      </div>
    </figure>
    <div class="reveal">
      <p class="eyebrow">이 실천이 나온 곳</p>
      <h2 class="h-md">성당의 오르간 자리, 그리고 은퇴 수녀들의 방.</h2>
      <p class="mt-3">2022년부터 더블린의 두 본당에서 매주 연주해 왔습니다. 성주간 전례, 학교
         미사와 위령 미사, 장례, 본당 음악회. 본당과 수도 공동체에는 이 일을 음악을 통한
         평신도 사도직으로 설명합니다. 그 자리에 함께 있어 주는 봉사라는 뜻입니다. 커뮤니티
         활동과 같은 일을, 물어보신 분들의 말로 옮긴 것입니다.</p>
      <p class="mt-3">졸업 연구는 워렌마운트의 은퇴 프레젠테이션 수녀 일곱 분을 위해 직접
         설계하고 이끈 10주 리코더 앙상블이었습니다. 일곱 분 모두 마치고 사람들 앞에서
         연주했습니다. 지금의 교육 프로그램 전체가 그 위에 서 있습니다.</p>
      <div class="quote mt-4">
        <p>&ldquo;음악으로, 그는 홀로 남았을 이들에게 격려와 존엄과
           영적인 동행을 건넵니다.&rdquo;</p>
        <cite>더블린 보좌주교 도날 로치 &middot; 2026년 2월 16일</cite>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">함께 연주하는 예술가</p>
      <h2 class="h-md">같이 무대에 서는 사람들.</h2>
    </div>
    <div class="grid grid-3 stagger">
      <article class="card card-media">
        <div class="photo photo-4x3"><img src="images/ruared-pianist.jpg" width="1400" height="933"
             alt="Rua Red 무대에서 피아노를 연주하는 안수정"></div>
        <div class="card-body"><span class="kicker">피아노</span><h3>안수정</h3>
          <p>RIAM 음악박사(2022). 제58회 마리아 카날스 국제콩쿠르 1위.</p></div>
      </article>
      <article class="card card-media">
        <div class="photo photo-4x3"><img src="images/ruared-soprano.jpg" width="933" height="1400"
             alt="Rua Red에서 노래하는 소프라노 정혜리"></div>
        <div class="card-body"><span class="kicker">소프라노</span><h3>정혜리</h3>
          <p>신라대학교, 로마 산타 체칠리아 국립음악원.</p></div>
      </article>
      <article class="card card-media">
        <div class="photo photo-4x3"><img src="images/tuh-haegeum.jpg" width="1400" height="934"
             alt="Tallaght University Hospital에서 해금을 연주하는 김재원"></div>
        <div class="card-body"><span class="kicker">해금</span><h3>김재원</h3>
          <p><em>Shared Voices of Care</em>와 <em>An Autumn Concert</em>(2026) 객원.</p></div>
      </article>
    </div>
    <p class="tiny mt-3 reveal">Rua Red 사진: Ben Ryan / South Dublin County Council. 병원 사진:
       Tallaght University Hospital.</p>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap narrow">
    <div class="section-head reveal">
      <p class="eyebrow">기록</p>
      <h2 class="h-md">학력과 역할, 그 밖의 것. 필요하신 만큼만.</h2>
    </div>
    <div class="faq-list record">
      <details class="faq reveal"><summary>학력과 훈련</summary>
        <ul class="plainlist">
          <li><strong>연주 전공 음악학사(우등)</strong> &mdash; TU Dublin Conservatoire, 2022&ndash;2026</li>
          <li><strong>클라리넷</strong> &mdash; Dr Paul Roe &middot; <strong>오르간</strong> &mdash; Simon Harden
              &middot; <strong>첼로</strong> &mdash; Arun Rao &middot; <strong>피아노</strong> &mdash; Sam Armstrong</li>
          <li><strong>지휘</strong> &mdash; 아일랜드 청소년오케스트라협회(IAYO) &middot; London Conducting
              Workshop &middot; TU Dublin 특별 과정</li>
          <li><strong>사회적기업</strong> &mdash; TU Dublin Venture Lab, 2024년 9월부터</li>
          <li><strong>장학</strong> &mdash; 한국 천주교 주교회의 평신도사도직위원회 명도회, 2025년 3월부터</li>
        </ul>
      </details>
      <details class="faq reveal"><summary>현재 맡고 있는 일</summary>
        <ul class="plainlist">
          <li><strong>창립자 · 프로젝트 리드</strong> &mdash; <span class="brandname">Classical Music for Everyone</span>, 2024년 1월부터</li>
          <li><strong>창립자 · 음악감독 · 지휘</strong> &mdash; Letters Ensemble, 2024년 1월부터</li>
          <li><strong>음악감독</strong> &mdash; 성모 통고 성당(Dolphin&rsquo;s Barn), 2022년 9월부터</li>
          <li><strong>오르가니스트</strong> &mdash; 삼주보 성당(Rathgar), 2023년 9월부터</li>
          <li><strong>학생 홍보대사</strong> &mdash; TU Dublin, 2024년 8월부터</li>
        </ul>
      </details>
      <details class="faq reveal"><summary>그 전에</summary>
        <ul class="plainlist">
          <li><strong>Baram</strong>, 2023&ndash;24 &mdash; 한국 전통음악과 클래식 듀오. 대사관 행사와 문화 전시</li>
          <li><strong>Chorus of Angels</strong>, 2023 &mdash; 더블린의 한인·다문화 어린이 합창단</li>
          <li><strong>At Home Ensemble Project</strong>, 2020&ndash;21 &mdash; 코로나19 기간의 온라인 관악 앙상블</li>
        </ul>
      </details>
      <details class="faq reveal"><summary>자원봉사</summary>
        <ul class="plainlist">
          <li>세계청년대회, 리스본, 2023 &mdash; 진행·음악·전례·언어 지원</li>
          <li>ICA ClarinetFest, 더블린, 2024 &mdash; 지원과 통역</li>
          <li>제13회 더블린 국제 피아노 콩쿠르, 2025 &mdash; Team Harmony</li>
          <li>청년 희년, 로마, 2025 &middot; Korea Festival, Farmleigh House, 2025</li>
        </ul>
        <p class="small">포르투갈과 이탈리아는 자원봉사를 간 곳입니다. 저희가 적는 &lsquo;4개국&rsquo;은
           <em>연주한</em> 나라만 셉니다.</p>
      </details>
      <details class="faq reveal"><summary>글과 기사</summary>
        <ul class="plainlist">
          <li><strong>경향잡지</strong> 2026년 5월호 &mdash; 기획 &ldquo;청년, 어떻게 지내니&rdquo; 청탁 원고</li>
          <li><strong>가톨릭대학교 학보</strong> 2026년 3월 &mdash; &ldquo;F&aacute;ilte go h&Eacute;irinn!&rdquo;</li>
          <li><strong>연주 후기</strong> 2025년 3월 &mdash; &ldquo;하느님께서 주신 모두를 위한 선물 &lsquo;음악&rsquo;&rdquo;</li>
        </ul>
      </details>
    </div>
  </div>
</section>

<section class="band-photo">
  <img src="images/organ.jpg" alt="" width="1400" height="1050">
  <div class="wrap narrow center reveal">
    <p class="eyebrow center-row">편지하기</p>
    <h2 class="h-lg">모든 문의는 본인에게 바로 갑니다.</h2>
    <p class="lead mt-2">한 줄이면 충분합니다. 무엇에 관한 것인지, 대략 어디 계신지.</p>
    <div class="btn-row center-row">
      <a class="btn btn-accent" href="mailto:sby05034@gmail.com?subject=%EB%AC%B8%EC%9D%98">이메일 <span class="arrow">&rarr;</span></a>
      <a class="btn btn-on-dark" href="contact.html">연락처 전체</a>
    </div>
  </div>
</section>"""


# ---------------------------------------------------------------------------

PROGRAMMES = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">프로그램</p>
    <h1>프로그램 다섯. 대표는 없습니다.</h1>
    <p>셋은 악기를 가르치고, 둘은 방으로 음악을 들고 갑니다. 같은 분량, 같은 항목, 같은
       순서로.</p>
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
          <tr><td><strong><a class="link" href="programmes/recorder-ensemble.html">무료 리코더 앙상블 과정</a></strong></td><td>배움</td>
              <td>운영 중</td><td>파일럿 완료 · 2026년 9월 첫 커뮤니티 수업</td></tr>
          <tr><td><strong><a class="link" href="programmes/getting-to-know.html">클래식 음악과 친해지기</a></strong></td><td>배움</td>
              <td>운영 중 · 무료</td><td>강의·연주 17회 · 누적 참석 143명</td></tr>
          <tr><td><strong><a class="link" href="programmes/concert-companion.html">함께하는 음악여행</a></strong></td><td>배움</td>
              <td>운영 중</td><td>기록된 동행 10회 · 두 번의 여름에 BBC 프롬스 포함</td></tr>
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
      <h2 class="h-md">무료 리코더 앙상블 과정</h2>
      <p class="lead mt-2">악기를 처음 잡는 분들과 한 학기. 끝은 음악회입니다.</p>
      <p class="mt-2">손에 부담이 없고, 첫 소리가 금방 나고, 여럿이 함께 붑니다. 살 것도, 미리 읽을 것도 없습니다.</p>
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
      <p class="lead mt-2">아무것도 몰라도 되는 무료 강의·연주.</p>
      <p class="mt-2">대략 월 1회. 어디서부터 시작해야 할지 몰랐던 분을 위한 자리입니다. 준비할 것은 없습니다.</p>
      <dl class="facts">
        <dt>세 단계</dt><dd>친해지기 · 함께 경험하기 · 내 취향 찾기</dd>
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
      <p class="mt-2">가기 전에 준비하고, 옆자리에 앉고, 다녀와서 이야기합니다. 발목을 잡는 건 대개 티켓값이 아닙니다.</p>
      <dl class="facts">
        <dt>규모</dt><dd>5명 안팎</dd>
        <dt>다녀온 곳</dt><dd>국립교향악단 · 아일랜드 국립오페라 · RTÉ 콘서트 오케스트라 · NCH 인터내셔널 시리즈</dd>
        <dt>멀리는</dt><dd>두 번의 여름, BBC 프롬스</dd>
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
      <p class="lead mt-2">사람들이 이미 있는 방으로 연주를 들고 갑니다.</p>
      <p class="mt-2">더블린 7구의 쉼터부터 대구의 순교 성지까지. 방만 빼고 전부 저희가 가져갑니다.</p>
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
      <p class="mt-2">아일랜드와 한국의 전통음악, 전례 음악, 편하게 들리는 편곡. 새 아마추어 연주자를 환영합니다.</p>
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
      <p>들을 만한 소리가 일찍 나오고, 그룹 전체가 같이 움직이고, 사람들 앞에서 끝납니다.</p>
    </div>
    <div class="reveal">{dg.term(L)}</div>

    <div class="split split-wide split-center mt-4">
      <div class="reveal">
        <p class="eyebrow">이 모델이 나온 곳</p>
        <h3 class="h-md">파일럿.</h3>
        <p class="statement statement-sm mt-2">은퇴 수녀 일곱 분. 매주 한 시간, 열 주.
           <em>일곱 분 모두 마치고</em> 사람들 앞에서 연주했습니다.</p>
        <p class="mt-3">더블린 8구 Warrenmount에서 연습하고, Clondalkin Lodge에서 아홉 곡의 부활
           음악회를 열었습니다. TU Dublin 음악원 학사 연구로 진행했습니다.</p>
      </div>
      <div class="reveal">
        <ul class="checklist">
          <li><strong>관계</strong> — 매주 모일 따뜻한 이유.</li>
          <li><strong>존엄과 성취</strong> — &ldquo;나도 음악을 만들 수 있다&rdquo;는 조용한 자부심.</li>
          <li><strong>가벼운 자극</strong> — 기억, 손발 맞추기, 호흡, 집중.</li>
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
    <p class="mt-2">본당, 성지, 수도원, 전례, 은퇴 수도 공동체. 찾아가는 음악회 20회 가운데 열여섯
       회쯤입니다. 신앙 공동체에는 음악을 통한 평신도 사도직이라고 설명합니다.</p>
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
      <article class="card card-media">
        <div class="photo photo-3x2"><img src="images/conducting.jpg" width="1400" height="933"
             alt="더블린의 한 커뮤니티 공간에서 진행하는 주간 수업"></div>
        <div class="card-body">
          <span class="kicker">완전 초보라면</span>
          <h3>연주를 배웁니다</h3>
          <p>무료 리코더 앙상블 과정에 오세요. 첫 주에 첫 소리를 내고, 악보는 처음부터 배우고,
             앙상블에서 내 파트를 맡고, 학기 끝에는 음악회를 엽니다.</p>
          <div class="meta">Mulhuddart Community Centre, D15 · 수요일 19:00–20:00 ·
             2026년 9월 9일 개강 · 무료</div>
        </div>
      </article>
      <article class="card card-media">
        <div class="photo photo-3x2"><img src="images/lecture-recital.jpg" width="1400" height="933"
             alt="진행 중인 강의·연주"></div>
        <div class="card-body">
          <span class="kicker">먼저 듣고 싶다면</span>
          <h3>들으러 옵니다</h3>
          <p>무료 강의·연주에 오시거나, 공연을 보러 가는 소그룹에 끼세요. 미리 준비하고,
             나란히 앉아 듣고, 끝나고 이야기를 나눕니다. 혼자서는 잘 안 가게 되는 분,
             아일랜드에 막 오신 분을 특히 환영합니다.</p>
          <div class="meta">대략 월 1회 · 5명 내외</div>
        </div>
      </article>
      <article class="card card-media">
        <div class="photo photo-3x2"><img src="images/letters-ensemble.jpg" width="1400" height="933"
             alt="악기를 든 Letters Ensemble"></div>
        <div class="card-body">
          <span class="kicker">이미 연주한다면</span>
          <h3>함께 연주합니다</h3>
          <p>Letters Ensemble은 더블린에 사는 아마추어 연주자에게 열려 있습니다. 토요일마다
             모여 연습하고, 커뮤니티 공간에서 연주합니다. 찾아가는 음악회 준비를 돕는
             자원봉사자도 환영합니다.</p>
          <div class="meta">현악·관악 모두 환영</div>
        </div>
      </article>
      <article class="card card-media">
        <div class="photo photo-3x2"><img src="images/community-room.jpg" width="1400" height="933"
             alt="꾸밈없는 커뮤니티 공간에서 연주하는 모습"></div>
        <div class="card-body">
          <span class="kicker">공간을 운영한다면</span>
          <h3>초대하거나 함께합니다</h3>
          <p>찾아가는 음악회를 부르시거나, 그 공동체를 위한 과정을 여실 수 있습니다.
             공공배상책임보험을 들어 두었고, 신원조회가 필요한 일은 시작 전에 Garda
             신원조회를 마칩니다.</p>
          <div class="meta">더블린·위클로·미스·라우스, 그 밖 지역도 협의</div>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">네 갈래는 어떻게 이어지는가</p>
      <h2>신청서 네 종류가 아니라, 문장 네 개입니다.</h2>
      <p>어느 쪽인지 고르지 않으셔도 됩니다. 지금 함께 연주하는 분들 대부분이 처음에는
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
    <div class="exchange reveal">
      <div class="exchange-side">
        <span class="kicker">공간이 준비하는 것</span>
        <p class="exchange-count">네 가지</p>
        <ul class="checklist mt-2">
          <li>열 명에서 열두 명이 둥글게 앉을 따뜻한 방, 학기 동안 주 1회</li>
          <li>지역에 알리는 일에 조금의 도움</li>
          <li>담당자 한 분</li>
          <li>그 밖에는 없습니다 — 장비도, 행정도, 피아노도</li>
        </ul>
      </div>
      <div class="exchange-side exchange-ours">
        <span class="kicker">저희가 준비하는 것</span>
        <p class="exchange-count">나머지 전부</p>
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
      <p><strong>비용 이야기.</strong> 모든 프로그램에 무료·할인 자리를 둡니다. 공간이 자체
         예산으로 진행비를 내주시면 그 방에 계신 분들은 전원 무료가 되고, 그 돈이 다른 방의
         무료 자리까지 지킵니다. 그럴 형편이 아니어도 우선 이야기부터 나눕니다.</p>
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
    <p class="eyebrow">일정과 소식</p>
    <h1>다가오는 일, 그리고 올해 있었던 일.</h1>
    <p>모집 중인 수업 하나, 열려 있는 음악회 하나. 2023년부터의 전체 기록은
       <a class="crumb" href="archive.html">기록</a> 페이지에 있습니다.</p>
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
        <div class="photo photo-3x2"><img src="images/ruared-trio.jpg" width="1400" height="933"
             alt="Rua Red 무대에서 인사하는 클라리넷·소프라노·피아노"></div>
        <div class="card-body">
          <span class="tag tag-live">첫 공적 지원</span>
          <h3 class="mt-1">South Dublin Live 2026</h3>
          <p>SDCC 예술과가 선정했습니다. 저희 주머니 밖에서 처음으로 돈이 나온 일입니다.</p>
          <div class="meta">2026년 8월 · SDCC 예술과</div>
        </div>
      </article>
      <article class="card card-media">
        <div class="photo photo-3x2"><img src="images/tuh-trio.jpg" width="1400" height="787"
             alt="Tallaght University Hospital 아트리움에서 연주하는 소프라노·피아노·클라리넷"></div>
        <div class="card-body">
          <span class="kicker">2026년 8월 20일</span>
          <h3>Shared Voices of Care</h3>
          <p>병원 아트리움에서 30분, 어쿠스틱, 오가며 듣는 형식. 해금 김재원과 함께, 환자와
             가족과 직원을 위해.</p>
          <div class="meta">Tallaght University Hospital</div>
        </div>
      </article>
      <article class="card card-media">
        <div class="photo photo-3x2"><img src="images/ruared-stage.jpg" width="1400" height="933"
             alt="객석에서 본 Rua Red 무대의 트리오"></div>
        <div class="card-body">
          <span class="kicker">2026년 8월 29일</span>
          <h3>Shared Voices of Classical Tradition</h3>
          <p>Rua Red 퍼포먼스 스페이스에서 클라리넷·피아노·소프라노로 60분. 무료 입장.</p>
          <div class="meta">Rua Red, Tallaght &middot; 사진 Ben Ryan / SDCC</div>
        </div>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap split split-wide split-center">
    <div class="reveal">
      <p class="eyebrow">기록</p>
      <h2>2023년부터의 모든 회차와 연주, 한 페이지에.</h2>
      <p class="lead mt-3">한 해에 오선 하나로 그린 연대기와 그 아래의 표. 지나온 길, 계획했지만
         하지 못한 것, 적어 두지 못한 것까지 거기 있습니다.</p>
      <div class="btn-row"><a class="btn btn-primary" href="archive.html">기록 열기 <span class="arrow">&rarr;</span></a></div>
    </div>
    <div>
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
</section>

{CTA}"""


# ---------------------------------------------------------------------------

SUPPORT = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">후원</p>
    <h1>문이 계속 열려 있도록.</h1>
    <p>자원봉사로 운영합니다. 후원금은 리코더와 악보, 공간 대여, 그리고 그 방까지 가는
       이동에 쓰입니다. 후원이 이미 한 일, 후원이 되는 것, 후원하는 방법을 차례로 적었습니다.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">후원이 이미 바꾼 것</p>
      <h2>차가 생겼고, 그만큼 멀리 갑니다.</h2>
      <p>유럽과 한국의 개인 후원이 모여 차량 한 대가 생겼습니다. 연주자와 악기와 보면대가
         한 번에 실려, 버스 시간표에 없는 요양시설과 본당과 쉼터까지 갑니다. 위클로, 미스,
         웨스트미스, 그리고 상의하면 더 멀리.</p>
    </div>
    <div class="grid grid-4 stagger">
      <div class="card"><span class="kicker">후원금은 이렇게 됩니다</span><h3>누군가의 손에 들린 리코더</h3>
        <p>소프라노 리코더 한 대는 8유로에서 15유로입니다. 사는 법을 알려 드리거나, 원가로
           드리거나, 한 학기 빌려 드립니다.</p></div>
      <div class="card"><span class="kicker">후원금은 이렇게 됩니다</span><h3>아무도 값을 치르지 않는 악보</h3>
        <p>그날 온 사람 누구든 불 수 있게 편곡한 파트를, 눈이 필요로 하면 크게 확대해서,
           저희 비용으로 인쇄합니다.</p></div>
      <div class="card"><span class="kicker">후원금은 이렇게 됩니다</span><h3>한 학기 동안 쓸 방</h3>
        <p>공간이 방을 내어 줄 수 없을 때 후원금으로 빌립니다. 매주 한 번 쓸 따뜻한 방이
           있어야 과정이 열립니다.</p></div>
      <div class="card"><span class="kicker">후원금은 이렇게 됩니다</span><h3>다음 방까지 가는 길</h3>
        <p>후원자들이 사 준 차의 기름값입니다. 그래서 위클로 주의 휴게실 하나가 예산 항목
           대신 오전 한나절이 됩니다.</p></div>
    </div>
    <p class="tiny mt-3 reveal">리코더 값 말고는 단가를 적지 않았습니다. 나머지는 방과 학기에
       따라 달라지기 때문입니다. 물어보시면 생각하시는 프로그램의 지금 수치를 보여 드립니다.</p>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">돈이 도는 방식</p>
      <h2>돈을 받은 일 하나가 무료 자리 하나를 지킵니다.</h2>
      <p>저희는 사회적기업입니다. 기부가 줄어드는 해에도 무료 자리가 남아 있으려면 이
         구조여야 합니다.</p>
    </div>
    <div class="reveal">{dg.subsidy(L)}</div>
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
        <p>일시든 정기든 악기와 교재, 공간과 이동에 쓰입니다. 메일 주시면 입금 정보와,
           그 금액이 무엇을 감당하는지 함께 알려 드립니다.</p></div>
      <div class="card"><span class="kicker">02</span><h3>프로그램 지원</h3>
        <p>재단·기금·지자체·기업 후원자를 위해 전체 제안서와 예산, 활동 기록을 요청 시
           보내 드립니다. <a class="link" href="partner.html">기관 파트너십</a> 페이지에
           파트너십에 따라오는 것을 적어 두었습니다.</p></div>
      <div class="card"><span class="kicker">03</span><h3>문을 열어 주기</h3>
        <p>요양시설이나 본당, 커뮤니티 센터나 병원에 저희를 소개해 주시는 일은
           후원금만큼, 때로는 그보다 더 큰 도움이 됩니다.</p></div>
      <div class="card"><span class="kicker">04</span><h3>공간 내어 주기</h3>
        <p>한 학기 동안 매주 한 번 쓸 따뜻한 방 하나가 가장 값진 현물 후원입니다.
           그대로 무료 자리가 됩니다.</p></div>
    </div>
    <div class="btn-row reveal center-row mt-4">
      <a class="btn btn-accent" href="mailto:sby05034@gmail.com?subject=CMFE%20후원%20문의">후원 문의 <span class="arrow">→</span></a>
      <a class="btn btn-quiet" href="partner.html">기관을 위한 안내</a>
      <a class="btn btn-quiet" href="mailto:sby05034@gmail.com?subject=CMFE%20파트너십·펀딩%20문의">제안서 요청</a>
    </div>
    <div class="callout reveal mt-4">
      <p class="small"><strong>안내.</strong> <span class="brandname">Classical Music for Everyone</span>은
         자원봉사로 운영되는 사회적기업이며, 현재
         비영리 보증유한책임회사(CLG) 설립을 준비하고 있습니다. 아직 등록 자선단체가 아니므로
         기부금 세제 혜택은 적용되지 않습니다. 헷갈리실 수 있어 미리 밝혀 둡니다.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap split split-center">
    <div class="reveal">
      <p class="eyebrow">지금까지</p>
      <h2 class="h-md">누가 이 일을 받쳐 왔는가.</h2>
      <p class="mt-3">2026년 이전은 전부 자비와 자원봉사였습니다. 지금까지의 지원 전체, South
         Dublin Live 신청을 위해 받은 서한, 그리고 아직 증명하지 못한 것을 한 페이지에 함께
         적어 두었습니다.</p>
      <div class="btn-row"><a class="btn btn-quiet" href="impact.html#transparency">투명성 <span class="arrow">&rarr;</span></a></div>
    </div>    <div class="reveal">
      <figure>
        <div class="photo photo-3x2">
          <img src="images/tuh-haegeum.jpg" width="1400" height="934"
               alt="Tallaght University Hospital 아트리움에서 해금을 연주하는 김재원">
        </div>
        <figcaption>Shared Voices of Care, Tallaght University Hospital, 2026년 8월 20일. 처음으로
          공적 자금이 들어온 음악회.</figcaption>
      </figure>
      <div class="quote mt-4">
        <p>&ldquo;넉넉한 형편에서 하는 일이 아닙니다. 본인의 재정 형편이 빠듯한
           가운데서도 시간과 에너지와 재능을 아낌없이 내어 주고 있습니다.&rdquo;</p>
        <cite>더블린 보좌주교 도날 로치 · 2026년 2월 16일</cite>
      </div>
    </div>
  </div>
</section>"""


# ---------------------------------------------------------------------------

CONTACT = """<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">문의</p>
    <h1>메일 주세요.</h1>
    <p>모든 문의는 창립자에게 바로 갑니다. 한 줄이면 충분합니다. 무엇에 관한 것인지,
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
      <p class="small mt-3">공공배상책임보험을 들어 두었고, 신원조회가 필요한 활동은
         시작 전에 Garda 신원조회를 마칩니다. 파트너 공간에는 요청하시면 서류를 보내
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


# ---------------------------------------------------------------------------
# 성과 — 무엇이 달라졌는지, 기록이 뒷받침하는 것만
# ---------------------------------------------------------------------------

import archive as ar


def _fig(n, label, period, suffix=""):
    return (f'<div class="figure"><b class="count" style="--n:{n}"><span>{n}{suffix}</span></b>'
            f'<span class="figure-label">{label}</span>'
            f'<span class="figure-period">{period}</span></div>')


IMPACT = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">성과와 근거</p>
    <h1>무엇이 달라졌는지, 기록이 뒷받침하는 것만 적었습니다.</h1>
    <p>웰빙이 좋아졌다거나 고립이 줄었다는 말은 여기 없습니다. 아직 재 보지 않았기
       때문입니다. 아래 숫자에는 전부 기간이 붙어 있고, 하나하나
       <a class="crumb" href="archive.html">기록</a>의 한 줄로 되짚을 수 있습니다.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">날짜가 있는 숫자</p>
      <h2>기간이 없는 숫자는 광고입니다. 이 숫자에는 기간이 있습니다.</h2>
    </div>
    <div class="figures stagger">
      {_fig(40, "회의 세션과 연주", "2024 – 2026년", "+")}
      {_fig(17, "회의 강의·연주", "2024년 1월 – 2026년 2월")}
      {_fig(143, "명이 그 강의에 왔습니다", "1–15회차 · 2024 – 2025년")}
      {_fig(20, "회의 찾아가는 음악회", "2023 – 2025년 · 4개국")}
      {_fig(7, "명 중 7명이 파일럿을 마쳤습니다", "2026년 1 – 4월")}
      {_fig(25, "곳의 공간과 기관", "2023 – 2026년")}
      {_fig(213, "시간, 준비 시간까지 기록", "2026년 8월 27일 기준")}
      {_fig(4, "회의 Letters Ensemble 음악회", "2024년 3월 – 2025년 12월")}
    </div>
    <p class="tiny mt-3 reveal">40회는 강의·연주 17회, 찾아가는 음악회 20회, 파일럿 음악회 1회,
       South Dublin Live 음악회 2회를 더한 것입니다. 앙상블 음악회 4회는 20회 안에 들어 있어
       두 번 세지 않았습니다. 찾아가는 음악회의 관객 수는 세어 둔 적이 없어 적지 않습니다.</p>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">달라진 것</p>
      <h2>기록이 뒷받침하는 일곱 가지.</h2>
      <p>하나하나 종이로 보여 드릴 수 있는 것들입니다. 그 종이가 편지인지, 프로그램인지,
         출석부인지도 함께 적었습니다.</p>
    </div>
    <div class="evidence evidence-2 stagger">
      <div><dl><dt>더 많은 사람이 왔습니다</dt>
        <dd>무료 강의·연주의 참석은 첫 회 <strong>6명</strong>에서 <strong>14명</strong>까지
            늘었고, 같은 분들이 다시 왔습니다. 두 해 동안 15회, 연 143명. 매회 그날
            세었습니다.</dd></dl></div>
      <div><dl><dt>관객이 연주자가 됐습니다</dt>
        <dd>2024년 성 골롬반 선교 수녀회 음악회가 끝난 뒤, 한 수녀님이 다시 연주할 수 있을지
            물었습니다. 그 질문이 2026년 은퇴 수도자 리코더 앙상블이 됐고, <strong>7명
            전원</strong>이 10주를 마치고 아홉 곡을 사람들 앞에서 연주했습니다.</dd></dl></div>
      <div><dl><dt>배움이 나눔을 먹였습니다</dt>
        <dd>강의·연주에 왔던 한 분이 학교 다닐 때 비올라를 켰던 것을 떠올리고 Letters
            Ensemble에 들어왔습니다. 두 축이 한 바퀴를 돈다는 말은 이런 뜻입니다.</dd></dl></div>
      <div><dl><dt>닿기 어려운 곳에 닿았습니다</dt>
        <dd>요양시설, 은퇴 수도 공동체, 노숙인 쉼터, HSE 주간 돌봄 서비스, 대학병원, 시골
            본당, 순교 성지. 그리고 국립 콘서트홀에는 함께 갔습니다.</dd></dl></div>
      <div><dl><dt>외부 기관이 인정했습니다</dt>
        <dd>사우스더블린 카운티 의회 예술과가 <strong>South Dublin Live 2026</strong>에 이
            프로젝트를 선정하고 비용을 지원했습니다. 그전까지는 전부 자비와 자원봉사였습니다.</dd></dl></div>
      <div><dl><dt>교회가 보증했습니다</dt>
        <dd>더블린 보좌주교 도날 로치의 추천서, 그리고 한국 천주교 주교회의
            평신도사도직위원회의 장학금.</dd></dl></div>
      <div><dl><dt>기관이 문을 열어 두었습니다</dt>
        <dd>South Dublin Live 신청을 위해 Rua Red, The Civic, Tallaght University Hospital이
            지지 서한을 썼습니다. 병원의 National Centre for Arts &amp; Health는 아트리움에서
            저희를 만나 음악회를 함께 준비했고, 그 자리에서 음악회가 열렸습니다.</dd></dl></div>
      <div><dl><dt>후원이 차를 샀습니다</dt>
        <dd>유럽과 한국의 개인 후원이 모여 차량 한 대가 생겼습니다. 연주자와 악기와 보면대가
            한 번에 실려, 버스 시간표에 없는 방까지 갑니다.</dd></dl></div>
    </div>
    <div class="reveal mt-4">{dg.attendance(L)}</div>
  </div>
</section>

<section>
  <div class="wrap split split-wide split-center">
    <figure class="reveal">
      <div class="photo photo-4x3">
        <img src="images/letters-ensemble.jpg" width="1400" height="1050"
             alt="악기를 든 Letters Ensemble 단원들">
      </div>
      <figcaption>Letters Ensemble. 2024년 위클로 주 음악회가 가르치는 프로그램의 출발점이
        됐습니다.</figcaption>
    </figure>
    <div class="reveal">
      <p class="eyebrow">이야기 하나</p>
      <h2 class="h-md">뒷줄에서 나온 질문.</h2>
      <p class="lead mt-2">2024년 11월, Letters Ensemble이 위클로 주의 성 골롬반 선교 수녀회에서
         연주했습니다. 연주가 끝나고 한 수녀님이 물었습니다. 다시 연주할 수 있을까요.
         오래전에 바이올린을 켰다고 했습니다.</p>
      <p class="mt-2">그 질문이 은퇴 프레젠테이션 수녀 일곱 분의 리코더 앙상블이 됐습니다.
         석 달의 준비, 워렌마운트에서의 10주 연습, 클론달킨 로지에서의 아홉 곡 부활 음악회.
         일곱 분 모두 끝까지 함께했습니다. 2026년 9월, 같은 과정이 멀허다트 커뮤니티 센터에서
         누구에게나 무료로 열렸습니다.</p>
      <p class="mt-2">그 수녀님의 이름은 적지 않습니다. 아직 여쭙지 않았기 때문입니다. 이
         사이트의 모든 이야기가 같은 규칙을 따릅니다.</p>
      <div class="btn-row"><a class="btn btn-quiet" href="programmes/recorder-ensemble.html">그 질문에서 나온 과정 <span class="arrow">&rarr;</span></a></div>
    </div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">변화 이론</p>
      <h2>방 하나, 한 시간, 리코더 하나가 무엇이 되어야 하는가.</h2>
    </div>
    <div class="reveal">{dg.theory_of_change(L)}</div>
  </div>
</section>

<section id="next">
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">가려는 곳</p>
      <h2>마친 일 넷, 할 일 넷. 이 순서대로 갑니다.</h2>
      <p>목록이 교육가 고용에서 끝나는 이유가 두 번째 사회적 목표입니다. 자원봉사자 한
         사람으로 굴러가는 모델은 파일럿입니다. 프로그램이 되려면 사람을 고용해야 합니다.</p>
    </div>
    <div class="reveal">{dg.roadmap(L)}</div>
    <div class="grid grid-2 stagger mt-4">
      <div class="card"><span class="kicker">재기</span>
        <h3>2026년 가을부터, 간단한 사전·사후 조사</h3>
        <p>멀허다트 과정부터 모든 기수에게 학기 처음과 끝에 관계와 자신감에 관한 짧은
           질문을 같은 방식으로 묻습니다. 인용할 말은 서면 동의를 받습니다. 다음 보고에서는
           출석만큼 자신 있게 웰빙을 말할 수 있게 됩니다.</p></div>
      <div class="card"><span class="kicker">적기</span>
        <h3>기록은 그날 남깁니다</h3>
        <p>모든 회차와 연주를 그날 적습니다. 날짜, 장소, 한 일, 대략 몇 명이 있었는지, 어떤
           증거가 남았는지. 이 실천은 연구로도 기록되고 있고, 앞으로도 그렇습니다. 세지
           못한 것은 같은 표에 세지 못했다고 적습니다.</p></div>
    </div>
  </div>
</section>

<section class="band-raised" id="transparency">
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">투명성</p>
      <h2>저희가 무엇이고, 무엇을 받았고, 무엇을 아직 증명하지 못했는가.</h2>
      <p>후원자는 초기 단계를 이해합니다. 이해하지 못하는 것은 얼버무림입니다. 그래서 지금
         단계를 그대로 적습니다.</p>
    </div>
    <div class="split reveal">
      <div>
        <h3 class="h-sub">현재 지위</h3>
        <dl class="facts">
          <dt>운영 형태</dt><dd>창립자가 이끄는 커뮤니티 음악 사회적기업. 자원봉사 운영.
              2024년 1월 더블린에서 창립</dd>
          <dt>법적 형태</dt><dd>비영리 보증유한책임회사(CLG) 설립 준비 중. 아직 등록 자선단체가
              아니며, 기부금 세제 혜택은 적용되지 않습니다</dd>
          <dt>이사진</dt><dd>아직 없습니다. 자원봉사 이사 세 명 이상의 이사회가 위 목록의 다음
              걸음입니다</dd>
          <dt>보험</dt><dd>공공배상책임보험 가입 완료, 2026년 8월부터</dd>
          <dt>신원조회</dt><dd>일에 필요한 경우 Garda 신원조회를 마칩니다. 관련 서류는 파트너
              공간에 요청 시 제공합니다</dd>
          <dt>창립자</dt><dd>김서현 Andrew Seohyeon Kim, BMus (Hons), TU 더블린 음악원 &mdash;
              <a class="link" href="founder.html">프로필</a></dd>
        </dl>
      </div>
      <div>
        <h3 class="h-sub">아직 증명하지 못한 것</h3>
        <ul class="checklist mt-2">
          <li><strong>웰빙을 재지 않았습니다.</strong> 검증된 도구도, 사전·사후 조사도 아직
              없습니다. 고립이 줄었다는 말은 참가자가 해 준 말에 기대고 있습니다.</li>
          <li><strong>관객을 세지 않았습니다.</strong> 스무 번의 찾아가는 음악회 어느 것에도
              관객 수 기록이 없습니다.</li>
          <li><strong>뒤를 좇지 않았습니다.</strong> 10주가 끝난 뒤 무엇이 남았는지
              모릅니다.</li>
          <li><strong>비교가 없습니다.</strong> 다른 악기, 다른 기수, 다른 교사를 견주어 본
              적이 없습니다.</li>
          <li><strong>실천한 사람이 곧 연구한 사람입니다.</strong> 설계에는 강점이고, 결과를
              주장하는 데는 한계입니다.</li>
        </ul>
      </div>
    </div>

    <div class="section-head reveal mt-4">
      <h3 class="h-sub">지금까지의 지원</h3>
      <p>2026년 이전은 전부 자비와 자원봉사였습니다. 후원을 검토하는 분이 가장 먼저 묻는
         것이 &lsquo;지금까지 누가 냈는가&rsquo;여서, 아무리 작아도 그대로 적어 둡니다.</p>
    </div>
    <div class="table-scroll reveal">
      <table>
        <thead><tr><th scope="col">출처</th><th scope="col">내용</th><th scope="col">상태</th></tr></thead>
        <tbody>
          <tr><td><strong>South Dublin County Council</strong><br><span class="tiny">예술과 ·
              South Dublin Live 2026</span></td>
              <td><em>Shared Voices of South Dublin</em>에 &euro;2,000. Tallaght University Hospital과
                  Rua Red에서 음악회 두 번을 열었습니다. 처음으로 공적 자금이 들어온 작업.</td>
              <td>수령 완료</td></tr>
          <tr><td><strong>명도회 장학금</strong><br><span class="tiny">한국 천주교 주교회의
              평신도사도직위원회</span></td>
              <td>2025년 3월부터 학기별 지원. 창립자의 음악 사도직을 위한 것.</td><td>종료</td></tr>
          <tr><td><strong>개인 후원자</strong></td>
              <td>유럽과 한국의 후원자들이 보내 준 도움으로 차량 한 대가 생겼습니다.</td>
              <td>진행 중</td></tr>
          <tr><td><strong>파트너 공간, 현물</strong></td>
              <td>Tallaght University Hospital &mdash; 공간과 운영 시간. Mulhuddart Community Centre
                  &mdash; 수업 공간. TU Dublin &mdash; 연습 공간.</td><td>계속</td></tr>
          <tr><td><strong>TU Dublin Venture Lab</strong></td>
              <td>사회적기업 창업 프로그램, 2024년 9월부터.</td><td>수료</td></tr>
        </tbody>
      </table>
    </div>
    <div class="split split-center reveal mt-4">
      <div class="quote">
        <p>&ldquo;넉넉한 형편에서 하는 일이 아닙니다. 본인의 재정 형편이 빠듯한
           가운데서도 시간과 에너지와 재능을 아낌없이 내어 주고 있습니다.&rdquo;</p>
        <cite>더블린 보좌주교 도날 로치 · 2026년 2월 16일</cite>
      </div>
      <div>
        <h3 class="h-sub">South Dublin Live 신청을 위해 받은 서한</h3>
        <ul class="plainlist mt-2">
          <li><strong>Rua Red</strong> &mdash; South Dublin의 현대예술센터</li>
          <li><strong>The Civic Theatre</strong>, Tallaght</li>
          <li><strong>Tallaght University Hospital</strong> &mdash; National Centre for Arts &amp; Health</li>
          <li><strong>SDCC 예술과</strong> &mdash; South Dublin Live 2026 선정</li>
        </ul>
        <p class="tiny mt-2">이 서한들은 그 한 건의 신청을 위해 써 주신 것입니다. 저희가 하는
           모든 일에 대한 포괄적인 보증이 아니며, 그렇게 내세우지 않습니다.</p>
      </div>
    </div>
  </div>
</section>

{CTA}"""


# ---------------------------------------------------------------------------
# 기록 — 2023년부터 지금까지
# ---------------------------------------------------------------------------

ARCHIVE = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">기록</p>
    <h1>2023년부터 지금까지, 모든 회차와 연주.</h1>
    <p>잘된 것만 고르지 않고 있었던 일을 그대로 적습니다. 이 사이트의 모든 숫자는 여기 한
       줄로 되짚을 수 있습니다. 확인되지 않은 행은 뺐습니다.</p>
  </div>
</section>

<section class="tight">
  <div class="wrap reveal">
    {dg.chronicle(L)}
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">지나온 길</p>
      <h2>클라리넷 하나에서 공동체까지.</h2>
    </div>
    <div class="split split-wide">
      <div class="timeline reveal">
        <div class="tl-item"><div class="tl-date">2023년 2월</div>
          <h3>시작 이전</h3>
          <p>루르드 미사에서 클라리넷 독주. 이름이 붙기 한 해 전.</p></div>
        <div class="tl-item"><div class="tl-date">2024년 1월</div>
          <h3>시작</h3>
          <p>더블린에서 창립, Letters Ensemble과 함께. 첫 강의·연주에 여섯 명.</p></div>
        <div class="tl-item"><div class="tl-date">2024년</div>
          <h3>음악이 나갑니다</h3>
          <p>달간 파크, 위클로, 런던, 파리, 대구. 강의는 TU Dublin으로.</p></div>
        <div class="tl-item"><div class="tl-date">2024–2025년</div>
          <h3>함께 갑니다</h3>
          <p>동행 관람이 독립된 갈래가 됩니다. NCH, 국립교향악단, BBC 프롬스.</p></div>
        <div class="tl-item"><div class="tl-date">2025년 10월</div>
          <h3>관객이 연주자가 됩니다</h3>
          <p>은퇴 수녀 일곱 분과의 리코더 앙상블 준비가 시작됩니다.</p></div>
        <div class="tl-item"><div class="tl-date">2025년 12월</div>
          <h3>국립 콘서트홀에서</h3>
          <p>열다섯 번째 회차는 국립 콘서트홀에서 함께 본 공연.</p></div>
        <div class="tl-item"><div class="tl-date">2026년 1–4월</div>
          <h3>파일럿, 그리고 그 음악회</h3>
          <p>Warrenmount에서 10주, Clondalkin Lodge에서 부활 음악회. 일곱 분 전원 수료.</p></div>
        <div class="tl-item"><div class="tl-date">2026년 8월</div>
          <h3>첫 공적 위촉</h3>
          <p>South Dublin Live 2026: Tallaght University Hospital과 Rua Red.</p></div>
        <div class="tl-item"><div class="tl-date">2026년 9월</div>
          <h3>이 모델이 처음으로 일반에 열립니다</h3>
          <p>첫 커뮤니티 과정이 Mulhuddart에서 열립니다. 12주, 무료.</p></div>
      </div>
      <div>
        <figure class="reveal">
          <div class="photo photo-4x3">
            <img src="images/church-concert.jpg" width="1400" height="1050"
                 alt="성당에서 연주하는 앙상블">
          </div>
          <figcaption>성당에서의 앙상블. 스무 번의 찾아가는 음악회 가운데 열여섯 번쯤이
            본당, 성지, 수도원, 전례였습니다.</figcaption>
        </figure>
        <div class="callout reveal mt-3">
          <h3 class="h-sub">표 읽는 법</h3>
          <p class="small mt-1">최근 해가 먼저 옵니다. 참석 인원은 강의·연주만 기록했습니다.
             <span class="tag">성지·본당 강</span>은 신앙 공동체를 찾아가는 갈래입니다. Letters
             Ensemble 연습은 기록해 두지 않아 싣지 않았습니다.</p>
        </div>
      </div>
    </div>
  </div>
</section>

{ar.tables(L)}

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">계획했지만 하지 못한 것</p>
      <h2>2026년: 계획을 반으로 줄이고, 남은 것은 끝까지 했습니다.</h2>
      <p>이것도 기록에 넣습니다. 졸업과 논문과 이사가 한 해에 겹치면서 계획한 넷이 둘이
         됐고, 그 둘은 제대로 치렀습니다.</p>
    </div>
    <div class="grid grid-2 stagger">
      <div class="card"><span class="kicker">열리지 않음 · 2026년 3월</span>
        <h3>Our Lady of Dolours 사순 음악회</h3>
        <p>자유 봉헌으로 여는 무료 본당 음악회. 클라리넷과 피아노, 이어 클라리넷과 Letters
           Ensemble. 제안서와 포스터와 악보는 있었고, 열리지 못했습니다.</p></div>
      <div class="card"><span class="kicker">논의 중</span>
        <h3>Letters Ensemble 다섯 번째 음악회</h3>
        <p>St John of God Hospital, Stillorgan. 프로그램 초안이 있습니다. 2026년 계획에서 첫
           번째로 논의 중인 파트너십으로 적었고, 날짜는 아직 없습니다.</p></div>
      <div class="card"><span class="kicker">열리지 않음 · 2026년 8월</span>
        <h3>South Dublin Live — The Civic의 한국·아일랜드 음악회</h3>
        <p>대극장에서 클라리넷과 피아노와 해금. 예술과에 제안한 네 음악회 가운데 이것과 아래
           가족 음악회는 열리지 못했고, 열린 둘은 위 2026년 표에 있습니다.</p></div>
      <div class="card"><span class="kicker">열리지 않음 · 2026년 9월</span>
        <h3>South Dublin Live — 야외 가족 음악회</h3>
        <p>광장에서 여는 45분 트리오 음악회. 비가 오면 카운티 도서관으로 옮길 계획까지
           있었습니다. 넷 가운데 가장 값싸고 가장 열린 형식이라, 가장 먼저 다시 살아날
           것입니다.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">아직 기록되지 않은 것</p>
      <h2 class="h-md">있었지만 적어 두지 않은 일.</h2>
      <ul class="checklist mt-3">
        <li>Letters Ensemble 연습. 2024년 1월부터 매주, 백 번이 훨씬 넘는데 하나도 적지
            않았습니다. 이제부터 셉니다.</li>
        <li>함께하는 음악여행의 실제 참석. 안내한 기록은 남았고, 몇 명이 갔는지는 남지
            않았습니다.</li>
        <li>스무 번의 찾아가는 음악회 대부분의 프로그램과 곡목.</li>
        <li>모든 연주의 관객 수.</li>
        <li>참가자의 증언. 2026년 가을 기수부터 동의를 받고 모읍니다.</li>
      </ul>
    </div>
    <div class="reveal">
      <p class="eyebrow">기록을 남기는 법</p>
      <h2 class="h-md">그날, 한 줄로.</h2>
      <ol class="steps mt-3">
        <li><strong>날짜, 정식 장소 이름, 기관 종류.</strong> 무엇을 했고, 누구를 위한
            것이었는지.</li>
        <li><strong>몇 명이 있었는지의 어림.</strong> 아무도 세지 않았어도 그날 저녁에
            적습니다.</li>
        <li><strong>준비 시간까지 넣은 시간.</strong> 예전 기록마다 빠져 있던 부분입니다.</li>
        <li><strong>남은 증거.</strong> 심사자가 믿는 순서대로: 기관 레터헤드의 편지, 언론
            보도, 프로그램이나 포스터, 사진.</li>
      </ol>
      <div class="btn-row"><a class="btn btn-quiet" href="impact.html">이 기록이 무엇이 되는가 <span class="arrow">&rarr;</span></a></div>
    </div>
  </div>
</section>

{CTA}"""


# ---------------------------------------------------------------------------
# 기관 파트너십
# ---------------------------------------------------------------------------

_MAIL_PARTNER = ("mailto:sby05034@gmail.com?subject=%ED%8C%8C%ED%8A%B8%EB%84%88%EC%8B%AD%20%EB%AC%B8%EC%9D%98"
                 "&body=%EA%B8%B0%EA%B4%80%3A%20%0A%EC%9C%84%EC%B9%98%3A%20%0A%EA%B3%B5%EA%B0%84%EA%B3%BC%20%EA%B0%80%EB%8A%A5%ED%95%9C%20%EB%82%A0%EC%A7%9C%3A%20%0A"
                 "%EC%83%9D%EA%B0%81%ED%95%98%EC%8B%9C%EB%8A%94%20%EA%B2%83%20%ED%95%9C%20%EC%A4%84%3A%20")

_FAQ_KO = "\n".join(
    f'      <details class="faq reveal"><summary>{q}</summary><p>{a}</p></details>'
    for q, a in [
        ("단체 전체가 아니라 프로그램 하나만 후원할 수 있나요?",
         "네. 프로그램이나 공간의 종류를 지정해 주시면 그 후원은 거기에만 쓰고, 거기에 맞춰 "
         "보고합니다."),
        ("기부금 세제 혜택이 있나요?",
         "아직 없습니다. 비영리 보증유한책임회사로 설립을 준비 중이고 등록 자선단체가 아니어서, "
         "기부금은 세제 혜택 대상이 아닙니다. 오해가 생기기 전에 분명히 적어 둡니다."),
        ("후원사 이름은 어디에 실리나요?",
         "후원하신 연주의 인쇄 프로그램, 이 사이트의 후원 페이지, 그리고 받으시는 보고서에 "
         "실립니다. 동의를 받은 뒤에만, 그 밖의 자리에는 싣지 않습니다."),
        ("음악회를 열려면 공간이 무엇을 준비해야 하나요?",
         "방 하나, 거기 살거나 일하는 사람들, 담당자 한 사람입니다. 연주자와 악기, 보면대, "
         "프로그램, 보험은 저희가 가져갑니다. 무대도 피아노도 필요 없고, 관객이 낼 돈도 "
         "없습니다."),
    ])

PARTNER = f"""<section class="page-hero page-hero-lead">
  <div class="wrap">
    <p class="eyebrow lift lift-1">기관 파트너십</p>
    <h1 class="lift lift-2">방과 날짜만 알려 주세요.</h1>
    <p class="lift lift-3">요양시설·병원·본당·커뮤니티 센터를 위한 안내이고, 지자체·재단·기금·기업을
       위한 안내이기도 합니다. 문의는 2분이면 되고, 방을 뺀 나머지는 전부 저희가 가져갑니다.</p>
    <div class="btn-row lift lift-4">
      <a class="btn btn-accent" href="{_MAIL_PARTNER}">2분이면 되는 문의 <span class="arrow">&rarr;</span></a>
      <a class="btn btn-on-dark" href="#faq">자주 받는 질문</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">받으시는 것</p>
      <h2>하루가 달라지는 방에 실황 연주가 들어갑니다. 직접 와서 보실 수 있습니다.</h2>
      <p>후원은 병동과 휴게실과 본당 홀에 연주자를 세웁니다. 그리고 여러분의 팀에게 가서
         볼 수 있고 함께할 수 있는 무언가를 줍니다. 모든 파트너십에는 담당자의 이름, 그 돈이
         한 일을 날짜와 함께 적은 보고, 언제든 와서 보시라는 초대가 따라옵니다.</p>
    </div>
    <div class="reveal">{dg.partnership(L)}</div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">방을 맡고 계시다면</p>
      <h2>오선 위쪽은 전부 차에 실려 옵니다.</h2>
      <p>피아노도 무대도 예산도 없는 휴게실이 음악회를 열 수 있습니다. 30분에서 60분,
         어쿠스틱으로, 곡마다 쉬운 말로 소개하고, 관객이 낼 돈은 없습니다. 공공배상책임보험에
         들어 있고 일에 필요하면 Garda 신원조회를 마칩니다. 서류는 가기 전에 보내 드립니다.</p>
    </div>
    <div class="reveal">{dg.visit(L)}</div>
    <div class="grid grid-3 stagger mt-4">
      <div class="card"><span class="kicker">요양시설과 병원</span>
        <h3>휴게실 음악회, 또는 아트리움 드롭인</h3>
        <p>입소자와 환자, 가족과 직원이 이미 있는 그 방에서. 2026년 8월 Tallaght University
           Hospital 음악회는 30분, 어쿠스틱, 오가며 듣는 형식이었습니다. 요양시설 음악회도
           대개 같은 모양입니다.</p></div>
      <div class="card"><span class="kicker">본당과 수도 공동체</span>
        <h3>전례 음악, 또는 미사 뒤의 음악회</h3>
        <p>스무 번의 찾아가는 음악회 가운데 열여섯 번쯤이 본당과 성지, 수도원과 전례였습니다.
           창립자는 더블린의 한 본당에서 음악 감독을, 다른 본당에서 오르가니스트를 맡고
           있습니다. 제의실에서 먼저 듣고 싶어 하는 말이 무엇인지 압니다.</p></div>
      <div class="card"><span class="kicker">커뮤니티 센터</span>
        <h3>여러분의 방에서 여는 한 학기 과정</h3>
        <p>열 명에서 열두 명이 둥글게 앉을 따뜻한 방, 한 학기 동안 매주 한 번, 담당자 한
           사람. 교사와 교육과정, 악보, 학기 말 음악회는 저희가 가져갑니다.
           <a class="link" href="get-involved.html">공간이 준비할 것과 저희가 할 것</a>.</p></div>
    </div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">근거</p>
      <h2>이미 함께한 곳.</h2>
      <p>빌려온 신뢰는 확인할 수 있어야 하므로 이름을 그대로 적습니다. 하나하나
         <a class="link" href="archive.html">기록</a>의 한 줄입니다.</p>
    </div>
    <ul class="names reveal">
      <li>South Dublin County Council 예술과</li>
      <li>Tallaght University Hospital</li>
      <li>Rua Red</li>
      <li>The Civic Theatre</li>
      <li>Clondalkin Lodge</li>
      <li>Mulhuddart Community Centre</li>
      <li>프레젠테이션 수녀회</li>
      <li>성 골롬반 선교 수녀회</li>
      <li>Dalgan Park</li>
      <li>TU Dublin</li>
      <li>Our Lady of Dolours, Dolphin&rsquo;s Barn</li>
      <li>Church of the Three Patrons, Rathgar</li>
      <li>HSE EVE Goirtin Hub</li>
      <li>Morning Star Hostel</li>
      <li>파리 외방전교회</li>
    </ul>
    <div class="figures figures-4 stagger mt-4">
      {_fig(20, "회의 찾아가는 음악회", "2023 – 2025년 · 4개국")}
      {_fig(25, "곳의 공간과 기관", "2023 – 2026년")}
      {_fig(7, "명 중 7명이 파일럿을 마쳤습니다", "2026년 1 – 4월")}
      {_fig(2, "회의 South Dublin Live 음악회", "2026년 8월 · 첫 공적 위촉")}
    </div>
    <div class="quote reveal mt-4">
      <p>&ldquo;음악으로, 그는 홀로 남았을 이들에게 격려와 존엄과
         영적인 동행을 건넵니다.&rdquo;</p>
      <cite>더블린 보좌주교 도날 로치 · 2026년 2월 16일</cite>
    </div>
  </div>
</section>

<section id="faq">
  <div class="wrap narrow">
    <div class="section-head reveal">
      <p class="eyebrow">자주 받는 질문</p>
      <h2 class="h-md">네 가지, 있는 그대로 답합니다.</h2>
    </div>
    <div class="faq-list">
{_FAQ_KO}
    </div>
  </div>
</section>

<section class="band-photo">
  <img src="images/tuh-atrium.jpg" alt="" width="1400" height="1052">
  <div class="wrap narrow center reveal">
    <p class="eyebrow center-row">다음 걸음</p>
    <h2 class="h-lg">이메일 한 통, 네 줄.</h2>
    <p class="lead mt-2">기관, 위치, 공간과 가능한 날짜, 그리고 생각하시는 것 한 줄. 메일을
       열면 그 네 줄이 미리 적혀 있습니다. 답장은 그 방에 직접 갈 사람이 보냅니다.</p>
    <div class="btn-row center-row">
      <a class="btn btn-accent" href="{_MAIL_PARTNER}">파트너 되기 <span class="arrow">&rarr;</span></a>
      <a class="btn btn-on-dark" href="contact.html">연락처 전체</a>
    </div>
  </div>
</section>"""


# ---------------------------------------------------------------------------
# 상징과 표준
# ---------------------------------------------------------------------------

IDENTITY = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">상징과 표준</p>
    <h1>금색은 <em>Everyone</em> 위에 놓입니다.</h1>
    <p>장식이 아닙니다. 로고에서 &lsquo;for&rsquo;는 작게, &lsquo;Everyone&rsquo;은 크고
       금색으로 놓습니다. 이 이름에서 지키기 어려운 낱말이 마지막 낱말이라서 그렇습니다.
       이 페이지가 디자인 표준입니다. 저희 이름을 인쇄하는 누구든 이 기준으로 저희를
       붙들어 두실 수 있도록 공개합니다.</p>
  </div>
</section>

<section class="band-mark">
  <div class="wrap split split-wide split-center">
    <div class="reveal">
      <p class="eyebrow">이름이 곧 숙제입니다</p>
      <h2 class="h-md">이름에 해야 할 일이 적혀 있습니다.</h2>
      <p class="lead mt-3">이 음악에 부족한 건 관객이 아니라 길입니다. 나이가 많거나, 몸이
         아프거나, 도시에서 멀거나, 형편이 빠듯하거나, 이 음악이 자기 것이라는 말을 한 번도
         못 들어 본 사람이 걸어 들어올 길. 저희가 무엇으로 평가받아야 하는지는 로고에 이미
         적혀 있습니다.</p>
      <p class="mt-3">높은음자리표와 워드마크, 2026년 8월 17일 확정. 워드마크 안의 비례가 뜻을
         담고 있고, 바뀌지 않습니다. 이름은 한 가지 모양의 고유명사입니다 &mdash;
         <span class="brandname">Classical Music for Everyone</span>. 전부 대문자로 쓰지 않고,
         대외 문안에서 줄이지 않으며, 다른 서체로 다시 짜지 않습니다.</p>
      <p class="footer-line mark-line">클래식 음악을, 그것이 필요한 곳으로!</p>
    </div>
    <figure class="reveal mark-plate">
      <img src="assets/logo-horizontal.svg" width="341" height="131"
           alt="Classical Music for Everyone 로고 — 높은음자리표와 워드마크. &lsquo;Everyone&rsquo;이 크고 금색으로 놓여 있다">
      <figcaption>가로형 로고, 2026년 8월 17일 확정.</figcaption>
    </figure>
  </div>
</section>

<section id="identity">
  <div class="wrap">
    <div class="split split-center reveal">
      <div class="logo-pair">
        <figure class="logo-plate on-light">
          <img src="assets/logo-horizontal.svg" width="341" height="131"
               alt="가로형 로고 — 높은음자리표와 워드마크">
          <figcaption>밝은 바탕 &mdash; 기본</figcaption>
        </figure>
        <figure class="logo-plate on-dark">
          <img src="assets/logo-reversed.svg" width="341" height="131"
               alt="어두운 바탕용 반전 로고">
          <figcaption>네이비 바탕 &mdash; 반전</figcaption>
        </figure>
        <figure class="logo-plate on-light">
          <img src="assets/logo-signature.png" width="600" height="210"
               alt="이메일 끝에 쓰는 서명용 로고">
          <figcaption>이메일 서명 &mdash; 같은 조합을 메일 크기로. 투명도를 지우는 메일
            클라이언트를 위해 흰 바탕 판본을 함께 둡니다.</figcaption>
        </figure>
      </div>
      <div>
        <h3 class="h-sub">로고 쓰는 법</h3>
        <p class="mt-2">밝은 바탕에는 가로형, 어두운 바탕에는 반전형. 높은음자리표만 따로 쓰는
           것은 파비콘과 프로필 사진뿐입니다. 사진 위에 놓을 때는 뒤가 조용한 자리를 고르거나
           단색 판을 깝니다.</p>
        <div class="rules mt-3">
          <div class="do">
            <h3 class="h-sub">언제나</h3>
            <ul>
              <li>높은음자리표와 워드마크를 함께</li>
              <li>사방에 높은음자리표 폭의 절반만큼 여백</li>
              <li>밝은 바탕 &rarr; 가로형, 어두운 바탕 &rarr; 반전형</li>
              <li>화면 140px, 인쇄 28mm 이상</li>
            </ul>
          </div>
          <div class="dont">
            <h3 class="h-sub">절대로</h3>
            <ul>
              <li>늘리거나, 찌그러뜨리거나, 기울이거나, 색을 바꾸지 않기</li>
              <li>그림자·외곽선·광채를 넣지 않기</li>
              <li>&lsquo;for&rsquo;와 &lsquo;Everyone&rsquo;을 같은 크기로 만들지 않기</li>
              <li>파비콘보다 큰 자리에 높은음자리표만 쓰지 않기</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">색</p>
      <h2 class="h-md">여덟 가지 값, 한 번만 정의합니다.</h2>
      <p>이 사이트의 모든 색은 이 여덟 가운데 하나이거나 거기서 파생한 톤입니다. 어떤
         구성요소도 자기 색을 새로 만들지 않습니다.</p>
    </div>
    <div class="swatches reveal">
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--ink-navy)"></i><b>Ink Navy</b><code>#1D2430</code>
        <span>로고 바탕, 본문, 어두운 띠</span></div>
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--gold-bronze)"></i><b>Gold Bronze</b><code>#B8893A</code>
        <span>로고의 금색, 규칙선, 화살표, 도식의 선</span></div>
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--gold-light)"></i><b>Light Gold</b><code>#D9B36A</code>
        <span>반전 로고의 금색, 어두운 바탕 위의 강조</span></div>
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--warm-cream)"></i><b>Warm Cream</b><code>#FAF5EE</code>
        <span>거의 모든 페이지의 바탕</span></div>
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--soft-navy)"></i><b>Soft Navy</b><code>#33405C</code>
        <span>인쇄물의 패널과 블록</span></div>
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--antique-gold)"></i><b>Antique Gold</b><code>#B4914F</code>
        <span>인쇄물의 액센트</span></div>
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--dusty-rose)"></i><b>Dusty Rose</b><code>#8C4A56</code>
        <span>강조 &mdash; 드물게, 본문에는 쓰지 않음</span></div>
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--slate)"></i><b>Slate</b><code>#5F6B7D</code>
        <span>보조 텍스트</span></div>
    </div>
    <div class="callout reveal mt-3">
      <p class="small"><strong>더 예쁜 쪽을 포기하게 만드는 규칙 하나.</strong> Gold Bronze는
         크림 위에서 대비가 2.9:1이라 본문 크기에서 읽히지 않습니다. 그래서 글자로 쓰는 금색은
         언제나 어둡게 한 <code>#7F5C1C</code>이고, 금색 버튼의 글자는 흰색 대신 잉크
         네이비입니다. 이 사이트의 모든 글자와 바탕 조합은 WCAG AA를 넘깁니다. 예외는 로고
         하나뿐입니다. 로고는 이미지이고, 색을 바꾸지 않기 때문입니다.</p>
    </div>

    <div class="section-head reveal mt-4">
      <p class="eyebrow">서체</p>
      <h2 class="h-md">세 서체, 네 번째는 없습니다.</h2>
      <p>EB Garamond은 워드마크의 Cormorant Garamond과 같은 올드스타일 계보라서, 제목이 로고와
         다투지 않고 어울립니다. 한글은 행간을 더 주고 자간을 덜 조입니다. Noto Sans KR에는 둘
         다 필요합니다.</p>
    </div>
    <div class="specimen reveal">
      <div>
        <dfn>EB Garamond &mdash; 제목</dfn>
        <div class="sp-display">Bringing classical music where it&rsquo;s needed!</div>
        <p>SemiBold. 제목, 헤드라인, 디스플레이 크기.</p>
      </div>
      <div>
        <dfn>Plus Jakarta Sans &mdash; 본문과 라벨</dfn>
        <div class="sp-body">We teach people to play, not only to listen.</div>
        <p>Regular, SemiBold, Bold. 본문, 표, 캡션, 모든 라벨.</p>
      </div>
      <div>
        <dfn>Noto Sans KR &mdash; 한글</dfn>
        <div class="sp-kr">클래식 음악을, 그것이 필요한 곳으로!</div>
        <p>Regular, Medium, Bold. 한국어 페이지에서는 제목과 본문 모두.</p>
      </div>
      <div>
        <dfn>Cormorant Garamond &mdash; 로고 전용</dfn>
        <div class="sp-body">워드마크에만 쓰고, 다른 어디에도 쓰지 않습니다.</div>
        <p>로고의 글자는 외곽선으로 변환돼 있어, 이 사이트는 이 서체를 불러오지 않습니다.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">도식</p>
      <h2 class="h-md">열네 개의 도식, 네 가지 표시.</h2>
      <p>설명이 여든 낱말을 넘어가면 문단 대신 그림으로 옮깁니다. 이 사이트의 도식은 전부
         악보에서 빌려 온 같은 네 가지 표시로만 그려서, 열네 개가 순서도 열네 장 대신 한
         세트로 읽힙니다.</p>
    </div>
    <div class="reveal">{dg.vocabulary(L)}</div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">말</p>
      <h2 class="h-md">이름을 적는 법.</h2>
      <ul class="checklist mt-3">
        <li><strong>언제나 전체 이름으로</strong> &mdash; <span class="brandname">Classical Music
            for Everyone</span>. 대문자로만 쓰지 않고, 대외 문안에서 줄이지 않습니다.</li>
        <li><strong>참가자</strong>라고 부릅니다. 고객이나 학생, 노인이라고 하지 않습니다.
            어르신 대신 나이 많은 분.</li>
        <li><strong>사회적기업</strong>입니다. 자선단체도, 사업체도 아닙니다.</li>
        <li><strong>영문은 아일랜드식 철자</strong> &mdash; programme, organisation, centre.</li>
        <li><strong>최상급 표현을 쓰지 않고</strong>, 확인할 수 없는 주장을 하지 않으며,
            날짜 없는 숫자를 내놓지 않습니다.</li>
      </ul>
    </div>
    <div class="reveal">
      <p class="eyebrow">한 문장</p>
      <h2 class="h-md">단체 전체를 한 문장으로.</h2>
      <p class="footer-line mark-line">Bringing classical music where it&rsquo;s needed!</p>
      <p class="mt-3">마스터 태그라인은 느낌표로 끝나고, 모든 페이지 맨 아래에 있습니다.
         한국어 내부 대역은 &lsquo;클래식 음악을, 그것이 필요한 곳으로!&rsquo;입니다.</p>
      <div class="btn-row"><a class="btn btn-quiet" href="about.html">미션과 가치, 그리고 창립자 <span class="arrow">&rarr;</span></a></div>
    </div>
  </div>
</section>

{CTA}"""
