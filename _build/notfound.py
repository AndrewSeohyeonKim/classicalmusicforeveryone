# -*- coding: utf-8 -*-
"""The 404 page.

GitHub Pages serves /404.html for any unknown path at any depth, so every link
on it must be absolute from the site root rather than relative.
"""

BODY = """<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">404</p>
    <h1>That page has moved, or never existed.</h1>
    <p>Nothing is broken on your side. Pick up the thread from one of these.
       <span lang="ko">찾으시는 페이지가 없습니다. 아래에서 이어 가세요.</span></p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="grid grid-3 stagger">
      <a class="card" href="/classicalmusicforeveryone/">
        <span class="kicker">English</span>
        <h2>Home</h2>
        <p>What we do, what is on, and how the two pillars feed each other.</p>
      </a>
      <a class="card" href="/classicalmusicforeveryone/get-involved.html">
        <span class="kicker">English</span>
        <h2>Get involved</h2>
        <p>Learn to play, come and listen, play with us, or host a course.</p>
      </a>
      <a class="card" href="/classicalmusicforeveryone/contact.html">
        <span class="kicker">English</span>
        <h2>Contact</h2>
        <p>Every enquiry reaches the founder directly.</p>
      </a>
      <a class="card" href="/classicalmusicforeveryone/ko/" lang="ko">
        <span class="kicker">한국어</span>
        <h2>홈</h2>
        <p>하는 일, 진행 중인 일, 그리고 두 축이 서로를 먹여 살리는 방식.</p>
      </a>
      <a class="card" href="/classicalmusicforeveryone/ko/get-involved.html" lang="ko">
        <span class="kicker">한국어</span>
        <h2>참여하기</h2>
        <p>연주를 배우거나, 들으러 오거나, 함께 연주하거나, 공간을 여는 네 가지 길.</p>
      </a>
      <a class="card" href="/classicalmusicforeveryone/ko/contact.html" lang="ko">
        <span class="kicker">한국어</span>
        <h2>문의</h2>
        <p>모든 문의는 창립자에게 바로 전달됩니다.</p>
      </a>
    </div>
  </div>
</section>"""

TITLE = "Page not found — Classical Music for Everyone"
DESC = ("The page you asked for is not here. Links back to the English and Korean "
        "home, get-involved and contact pages.")
