"""Shared page shell for the CMFE site.

Emits plain static HTML — there is no runtime dependency. Run `_build/build.py`
after editing content, or edit the generated .html files directly.
Directories beginning with an underscore are not published by GitHub Pages.
"""

import os
import re

SITE_URL = "https://andrewseohyeonkim.github.io/classicalmusicforeveryone"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EMAIL = "sby05034@gmail.com"
PHONE_INTL = "+353 83 078 0635"
PHONE_TEL = "+353830780635"

FONTS = ("https://fonts.googleapis.com/css2?"
         "family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700"
         ";1,9..144,400;1,9..144,600"
         "&family=Plus+Jakarta+Sans:wght@400;500;600;700"
         "&family=Noto+Sans+KR:wght@400;500;700&display=swap")

NAV = {
    "en": [("about.html", "About"), ("programmes.html", "Programmes"),
           ("get-involved.html", "Get Involved"), ("news.html", "News"),
           ("support.html", "Support")],
    "ko": [("about.html", "소개"), ("programmes.html", "프로그램"),
           ("get-involved.html", "참여하기"), ("news.html", "소식"),
           ("support.html", "후원")],
}

# The five programme pages hang off the Programmes item. Without this they were
# reachable only from a card on another page — the menu said the section existed
# but gave no way to choose within it. Order matches the five cards everywhere
# else; no entry is marked out as the main one.
SUBNAV = {
    "programmes.html": {
        "en": [("programmes/recorder-ensemble.html", "Recorder Ensemble course",
                "A term for complete beginners"),
               ("programmes/getting-to-know.html", "Getting to Know Classical Music",
                "Free lecture-recitals"),
               ("programmes/concert-companion.html", "Concert Guide &amp; Companion",
                "Accompanied concert-going"),
               ("programmes/outreach-concerts.html", "Outreach Concerts",
                "Care homes, parishes, hospitals"),
               ("programmes/letters-ensemble.html", "Letters Ensemble",
                "Amateur players, weekly")],
        "ko": [("programmes/recorder-ensemble.html", "리코더 앙상블 과정",
                "완전 초보를 위한 한 학기"),
               ("programmes/getting-to-know.html", "클래식 음악과 친해지기",
                "무료 강의·연주"),
               ("programmes/concert-companion.html", "함께하는 음악여행",
                "공연에 함께 갑니다"),
               ("programmes/outreach-concerts.html", "찾아가는 음악회",
                "요양시설 · 본당 · 병원"),
               ("programmes/letters-ensemble.html", "Letters Ensemble",
                "아마추어 연주자, 주 1회")],
    },
}

SUBNAV_LABEL = {"en": "Programmes", "ko": "프로그램"}

STR = {
    "en": {
        "skip": "Skip to main content",
        "contact": "Contact",
        "menu": "Menu",
        "lang_label": "Language",
        "logo_alt": "Classical Music for Everyone",
        "this_lang": "EN", "other_lang": "한국어",
        "tagline": "Bringing classical music where it&rsquo;s needed.",
        "footer_about": ("We teach people to play — not only to listen — and bring live "
                         "classical music to the places it rarely reaches."),
        "f_explore": "Explore",
        "f_connect": "Connect",
        "f_legal": "© 2026 Classical Music for Everyone · Dublin, Ireland",
        "f_status": "Volunteer-led · formalising as a not-for-profit company limited by guarantee",
        "f_links": [("about.html", "About us"), ("programmes.html", "Programmes"),
                    ("get-involved.html", "Get involved"), ("news.html", "News &amp; record"),
                    ("support.html", "Support our work")],
    },
    "ko": {
        "skip": "본문으로 건너뛰기",
        "contact": "문의",
        "menu": "메뉴",
        "lang_label": "언어",
        "logo_alt": "Classical Music for Everyone",
        "this_lang": "한국어", "other_lang": "EN",
        "tagline": "클래식 음악을, 그것이 필요한 곳으로.",
        "footer_about": ("듣는 데서 그치지 않고 직접 연주하도록 가르치고, "
                         "클래식 음악이 잘 닿지 않는 곳으로 찾아갑니다."),
        "f_explore": "둘러보기",
        "f_connect": "연락",
        "f_legal": "© 2026 Classical Music for Everyone · 아일랜드 더블린",
        "f_status": "자원봉사로 운영 · 비영리 보증유한책임회사(CLG) 설립 준비 중",
        "f_links": [("about.html", "단체 소개"), ("programmes.html", "프로그램"),
                    ("get-involved.html", "참여하기"), ("news.html", "소식과 기록"),
                    ("support.html", "후원하기")],
    },
}

MENU_JS = ("var n=document.getElementById('nav');"
           "var o=n.getAttribute('data-open')!==&quot;true&quot;;"
           "n.setAttribute('data-open',o);this.setAttribute('aria-expanded',o)")


JSONLD = """<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "{site}/#organisation",
  "name": "Classical Music for Everyone",
  "alternateName": "CMFE",
  "url": "{site}/",
  "logo": "{site}/assets/logo-horizontal.png",
  "image": "{site}/images/hero-outreach.jpg",
  "description": "{desc}",
  "foundingDate": "2024-01",
  "founder": {{"@type": "Person", "name": "Andrew Seohyeon Kim"}},
  "email": "{email}",
  "telephone": "{phone}",
  "address": {{"@type": "PostalAddress", "addressLocality": "Dublin", "addressCountry": "IE"}},
  "areaServed": "Ireland",
  "knowsLanguage": ["en", "ko"],
  "inLanguage": "{lang}"
}}
</script>"""


def _images(body, eager_first):
    """Lazy-load every image; the hero, if there is one, loads eagerly."""
    out, first = [], True
    for chunk in re.split(r"(<img\b)", body):
        if chunk == "<img":
            if first and eager_first:
                out.append('<img fetchpriority="high" decoding="async"')
                first = False
            else:
                out.append('<img loading="lazy" decoding="async"')
                first = False
        else:
            out.append(chunk)
    return "".join(out)


# ---------------------------------------------------------------------------
# Paths
#
# A page may live one level down — programmes/recorder-ensemble.html — and the
# Korean twin of that is two levels down, in ko/programmes/. Two different
# prefixes fall out of that, and confusing them is exactly how the Korean nav
# once pointed at the English pages:
#
#   _here  … back to the top of THIS language's tree. Page-to-page links use
#            it, because ko/about.html is the Korean about page.
#   _root  … back to the site root. Shared files — assets/, images/,
#            styles.css — use it, because there is only one copy of them.
#
# Content files write every path root-relative (`href="programmes.html"`,
# `src="images/x.jpg"`); the right prefix is bolted on here, in one place, so
# a new sub-page cannot end up with a broken path in one language only.
# ---------------------------------------------------------------------------

SHARED = ("images/", "assets/", "styles.css")


def _here(slug):
    """Prefix from this page back to the top of its own language tree."""
    return "../" * slug.count("/")


def _root(lang, slug):
    """Prefix from this page back to the site root."""
    return "../" * (slug.count("/") + (0 if lang == "en" else 1))


def _switch(lang, slug):
    r = _root(lang, slug)
    return (r + "ko/" + slug) if lang == "en" else (r + slug)


# a path that is already resolved, and must be left exactly as written
_LINK = re.compile(r'\b(href|src)="(?!https?:|mailto:|tel:|data:|#|/|\.\.?/)([^"]*)"')


def _relink(markup, here, root):
    """Give every root-relative href/src in a body the prefix it needs."""
    def sub(m):
        attr, path = m.group(1), m.group(2)
        pre = root if path.startswith(SHARED) else here
        return f'{attr}="{pre}{path}"'
    return _LINK.sub(sub, markup)


def header(lang, slug):
    p, r, s = _here(slug), _root(lang, slug), STR[lang]
    rows = []
    for href, label in NAV[lang]:
        sub = SUBNAV.get(href)
        # a page under programmes/ should light up the Programmes item too
        here = href == slug or (sub and slug.startswith(href[:-5] + "/"))
        current = ' aria-current="page"' if here else ""
        if not sub:
            rows.append(f'      <a class="nav-link" href="{p}{href}"{current}>{label}</a>')
            continue
        # CSS-only disclosure: hover, and :focus-within for the keyboard. No
        # script — the whole site still runs on the one menu-toggle line.
        items = "\n".join(
            f'          <a href="{p}{h}"'
            + (' aria-current="page"' if h == slug else "")
            + f'><b>{t}</b><span>{d}</span></a>'
            for h, t, d in sub[lang])
        rows.append(
            f'      <div class="nav-item has-sub">\n'
            f'        <a class="nav-link" href="{p}{href}"{current}>{label}'
            f'<svg class="nav-chev" width="9" height="6" viewBox="0 0 9 6" aria-hidden="true">'
            f'<path d="M1 1l3.5 3.5L8 1" fill="none" stroke="currentColor" stroke-width="1.6" '
            f'stroke-linecap="round"/></svg></a>\n'
            f'        <div class="subnav">\n{items}\n        </div>\n'
            f'      </div>')
    links = "\n".join(rows)
    other = "ko" if lang == "en" else "en"
    return f"""<div class="progress" aria-hidden="true"></div>
<a class="skip" href="#main">{s['skip']}</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{p}index.html" aria-label="{s['logo_alt']}">
      <img src="{r}assets/logo-horizontal.svg" alt="{s['logo_alt']}"
           width="120" height="46" fetchpriority="high" decoding="async">
    </a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav"
            aria-label="{s['menu']}" onclick="{MENU_JS}">☰</button>
    <nav class="nav" id="nav" data-open="false" aria-label="{s['menu']}">
{links}
      <div class="lang-switch" role="group" aria-label="{s['lang_label']}">
        <span aria-current="true">{s['this_lang']}</span>
        <a href="{_switch(lang, slug)}" hreflang="{other}" lang="{other}">{s['other_lang']}</a>
      </div>
      <a class="btn btn-accent btn-nav" href="{p}contact.html">{s['contact']}</a>
    </nav>
  </div>
</header>"""


def footer(lang, slug="index.html"):
    p, r, s = _here(slug), _root(lang, slug), STR[lang]
    # the footer language link always goes to the other language's home page,
    # not to this page's twin — that is what the header switcher is for
    home_other = r + ("ko/index.html" if lang == "en" else "index.html")
    links = "\n".join(f'        <a href="{p}{h}">{t}</a>' for h, t in s["f_links"])
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <img src="{r}assets/logo-reversed.svg" alt="{s['logo_alt']}"
             width="109" height="42" loading="lazy" decoding="async">
        <p class="footer-line">{s['tagline']}</p>
        <p class="footer-tagline">{s['footer_about']}</p>
      </div>
      <div>
        <h3>{s['f_explore']}</h3>
{links}
      </div>
      <div>
        <h3>{s['f_connect']}</h3>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <a href="tel:{PHONE_TEL}">{PHONE_INTL}</a>
        <a href="{p}contact.html">{s['contact']}</a>
        <a href="{home_other}">{s['other_lang']}</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>{s['f_legal']}</span>
      <span>{s['f_status']}</span>
    </div>
  </div>
</footer>"""


def page(lang, slug, title, description, body):
    p, r = _here(slug), _root(lang, slug)
    sub = "" if slug == "index.html" else slug
    body = _images(body, eager_first='<section class="hero">' in body)
    body = _relink(body, p, r)
    jsonld = JSONLD.format(site=SITE_URL, desc=description.replace('"', "'"),
                           email=EMAIL, phone=PHONE_INTL,
                           lang="en-IE" if lang == "en" else "ko")
    canonical = f"{SITE_URL}/" + ("" if lang == "en" else "ko/") + sub
    return f"""<!DOCTYPE html>
<html lang="{'en-IE' if lang == 'en' else 'ko'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#1D2430">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{SITE_URL}/{sub}">
<link rel="alternate" hreflang="ko" href="{SITE_URL}/ko/{sub}">
<link rel="alternate" hreflang="x-default" href="{SITE_URL}/{sub}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Classical Music for Everyone">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/images/hero-outreach.jpg">
<meta property="og:locale" content="{'en_IE' if lang == 'en' else 'ko_KR'}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{r}assets/logo-icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{r}assets/logo-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{r}styles.css">
{jsonld}
</head>
<body>
{header(lang, slug)}
<main id="main">
{body}
</main>
{footer(lang, slug)}
</body>
</html>
"""


def write(lang, slug, title, description, body):
    out = os.path.join(ROOT, "" if lang == "en" else "ko", slug)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(page(lang, slug, title, description, body))
    return os.path.relpath(out, ROOT)
