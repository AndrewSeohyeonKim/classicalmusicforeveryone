"""Shared page shell for the CMFE site.

Emits plain static HTML — there is no runtime dependency. Run `_build/build.py`
after editing content, or edit the generated .html files directly.
Directories beginning with an underscore are not published by GitHub Pages.
"""

import os

SITE_URL = "https://andrewseohyeonkim.github.io/classicalmusicforeveryone"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EMAIL = "sby05034@gmail.com"
PHONE_INTL = "+353 83 078 0635"
PHONE_TEL = "+353830780635"

FONTS = ("https://fonts.googleapis.com/css2?"
         "family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400"
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

STR = {
    "en": {
        "skip": "Skip to main content",
        "contact": "Contact",
        "menu": "Menu",
        "logo_alt": "Classical Music for Everyone",
        "other_lang": "한국어",
        "tagline": "Making live classical music a shared, everyday experience.",
        "footer_about": ("A community music social enterprise based in Dublin, founded in 2024. "
                         "We teach people to play — not only to listen — and bring live classical "
                         "music to the places it rarely reaches."),
        "f_explore": "Explore",
        "f_connect": "Connect",
        "f_legal": ("© 2026 Classical Music for Everyone · Founded by Andrew Seohyeon Kim · Dublin, Ireland"),
        "f_status": "Volunteer-led · Formalising as a not-for-profit company limited by guarantee",
        "f_links": [("about.html", "About us"), ("programmes.html", "Programmes"),
                    ("get-involved.html", "Get involved"), ("news.html", "News & record"),
                    ("support.html", "Support our work")],
    },
    "ko": {
        "skip": "본문으로 건너뛰기",
        "contact": "문의",
        "menu": "메뉴",
        "logo_alt": "Classical Music for Everyone",
        "other_lang": "English",
        "tagline": "살아있는 클래식 음악을 일상에서 함께 나누는 경험으로.",
        "footer_about": ("2024년 더블린에서 시작한 커뮤니티 음악 사회적기업입니다. "
                         "듣는 데서 그치지 않고 직접 연주하도록 가르치고, "
                         "클래식 음악이 잘 닿지 않는 곳으로 찾아갑니다."),
        "f_explore": "둘러보기",
        "f_connect": "연락",
        "f_legal": "© 2026 Classical Music for Everyone · 창립자 Andrew Seohyeon Kim (김서현) · 아일랜드 더블린",
        "f_status": "자원봉사로 운영 · 비영리 보증유한책임회사(CLG) 설립 준비 중",
        "f_links": [("about.html", "단체 소개"), ("programmes.html", "프로그램"),
                    ("get-involved.html", "참여하기"), ("news.html", "소식과 기록"),
                    ("support.html", "후원하기")],
    },
}


def _prefix(lang):
    """Relative path back to the site root from a page in this language."""
    return "" if lang == "en" else "../"


def _lang_switch_href(lang, slug):
    return ("ko/" + slug) if lang == "en" else ("../" + slug)


def header(lang, slug):
    p, s = _prefix(lang), STR[lang]
    items = []
    for href, label in NAV[lang]:
        current = ' aria-current="page"' if href == slug else ""
        items.append(f'      <a href="{href}"{current}>{label}</a>')
    items.append(f'      <a class="lang" href="{_lang_switch_href(lang, slug)}" '
                 f'hreflang="{"ko" if lang == "en" else "en"}">{s["other_lang"]}</a>')
    items.append(f'      <a class="btn btn-gold" href="contact.html">{s["contact"]}</a>')
    nav = "\n".join(items)
    return f"""<a class="skip" href="#main">{s['skip']}</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="logo" href="index.html">
      <img src="{p}assets/logo-horizontal.svg" alt="{s['logo_alt']}" width="120" height="46">
    </a>
    <nav class="nav" id="nav" aria-label="{s['menu']}">
{nav}
    </nav>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav"
            aria-label="{s['menu']}" onclick="var n=document.getElementById('nav');
            var o=n.classList.toggle('open');this.setAttribute('aria-expanded',o)">☰</button>
  </div>
</header>"""


def footer(lang):
    p, s = _prefix(lang), STR[lang]
    links = "\n".join(f'        <a href="{h}">{t}</a>' for h, t in s["f_links"])
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <img src="{p}assets/logo-reversed.svg" alt="{s['logo_alt']}" width="109" height="42">
        <p class="footer-tagline">{s['footer_about']}</p>
      </div>
      <div>
        <h4>{s['f_explore']}</h4>
{links}
      </div>
      <div>
        <h4>{s['f_connect']}</h4>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <a href="tel:{PHONE_TEL}">{PHONE_INTL}</a>
        <a href="contact.html">{s['contact']}</a>
        <a href="{_lang_switch_href(lang, 'index.html')}">{s['other_lang']}</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>{s['f_legal']}</span>
      <span>{s['f_status']}</span>
    </div>
  </div>
</footer>"""


def page(lang, slug, title, description, body):
    p = _prefix(lang)
    canonical = f"{SITE_URL}/" + ("" if lang == "en" else "ko/") + ("" if slug == "index.html" else slug)
    alt_en = f"{SITE_URL}/" + ("" if slug == "index.html" else slug)
    alt_ko = f"{SITE_URL}/ko/" + ("" if slug == "index.html" else slug)
    return f"""<!DOCTYPE html>
<html lang="{'en-IE' if lang == 'en' else 'ko'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{alt_en}">
<link rel="alternate" hreflang="ko" href="{alt_ko}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Classical Music for Everyone">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/images/hero-outreach.jpg">
<meta property="og:locale" content="{'en_IE' if lang == 'en' else 'ko_KR'}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{p}assets/logo-icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{p}assets/logo-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{p}styles.css">
</head>
<body>
{header(lang, slug)}
<main id="main">
{body}
</main>
{footer(lang)}
</body>
</html>
"""


def write(lang, slug, title, description, body):
    out = os.path.join(ROOT, "" if lang == "en" else "ko", slug)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(page(lang, slug, title, description, body))
    return os.path.relpath(out, ROOT)
