# -*- coding: utf-8 -*-
"""The 404 page.

GitHub Pages serves /404.html for any unknown path at any depth, so every link
on it must be absolute from the site root rather than relative. build.py
rewrites the shell's paths; the links below are written absolute already.
"""

BODY = """<section class="ph ph-plain">
  <div class="wrap">
    <p class="eyebrow lift">404</p>
    <div class="ph-head">
      <h1 class="ph-title"><span class="ln"><span>That page has moved, or never existed.</span></span></h1>
      <p class="ph-lead lift lift-3">Nothing is broken on your side. Pick up the thread from one of these.
         <span lang="ko">찾으시는 페이지가 없습니다. 아래에서 이어 가세요.</span></p>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <h2 class="sr-only">Where to go next</h2>
    <ul class="nf-list rv">
      <li><a href="/classicalmusicforeveryone/"><span class="kicker">English</span><b>Home</b>
        <span>Who we are, the five programmes, and four ways in.</span></a></li>
      <li><a href="/classicalmusicforeveryone/get-involved.html"><span class="kicker">English</span><b>Get involved</b>
        <span>Take part in a programme, bring a concert to your place, tell us you would like to perform, or join the founding board.</span></a></li>
      <li><a href="/classicalmusicforeveryone/contact.html"><span class="kicker">English</span><b>Contact</b>
        <span>We answer every message.</span></a></li>
      <li lang="ko"><a href="/classicalmusicforeveryone/ko/"><span class="kicker">한국어</span><b>홈</b>
        <span>누구인지, 다섯 프로그램, 그리고 함께하는 네 가지 길.</span></a></li>
      <li lang="ko"><a href="/classicalmusicforeveryone/ko/get-involved.html"><span class="kicker">한국어</span><b>함께하기</b>
        <span>프로그램 참여, 음악회 초청, 함께 연주하기, 창립 이사회.</span></a></li>
      <li lang="ko"><a href="/classicalmusicforeveryone/ko/contact.html"><span class="kicker">한국어</span><b>문의</b>
        <span>보내 주신 메일에는 모두 답장합니다.</span></a></li>
    </ul>
  </div>
</section>"""

TITLE = "Page not found · Classical Music for Everyone"
DESC = ("The page you asked for is not here. Links back to the English and Korean "
        "home, get-involved and contact pages.")
