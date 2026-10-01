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
# Public profiles of the founder (04 — Founder Profile §2). Leave a value
# empty and its link is simply not rendered — never invent a handle.
SOCIAL = {
    "linkedin": "https://www.linkedin.com/in/andrewseohyeonkim",
    "instagram": "https://www.instagram.com/sh.andrew_ryan",
}
PHONE_INTL = "+353 83 078 0635"
PHONE_TEL = "+353830780635"

# Headings are EB Garamond, not Fraunces (changed 2026-09-04 on Andrew's call).
# Fraunces' wedge serifs and its wonky italic read as busy at display size; a
# Garamond is calm at any size and is the same lineage as the wordmark's
# Cormorant Garamond, so the headings now rhyme with the logo instead of
# arguing with it.
FONTS = ("https://fonts.googleapis.com/css2?"
         "family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500"
         "&family=Plus+Jakarta+Sans:wght@400;500;600;700"
         "&family=Noto+Sans+KR:wght@400;500;700&display=swap")
# An English page carries two Korean words (the language switch) and no
# Korean text, so it does not wait for the Korean family: those two words
# take the system's Korean face. The 404 page is in both languages.
FONTS_EN = FONTS.replace("&family=Noto+Sans+KR:wght@400;500;700", "")

# The date the copy was last checked against the canonical set and the kit,
# printed in every footer (24: the website is a trust document, and a reader
# should see when it was last looked at). Change it by hand when the content
# is reviewed, not on every rebuild.
UPDATED = {"en": "1 October 2026", "ko": "2026년 10월 1일"}

# Six pages and the language switch, nothing else (2026-09-30: five pages,
# then News & archive added back when the organisation was restructured).
# Five plain links; Contact is the one filled button, so the header still has
# a single clear action. No dropdown panels: every page is one click away.
NAV = {
    "en": [("index.html", "Home"), ("about.html", "About"),
           ("programmes.html", "Programmes"), ("get-involved.html", "Get involved"),
           ("news.html", "News &amp; archive")],
    "ko": [("index.html", "홈"), ("about.html", "소개"),
           ("programmes.html", "프로그램"), ("get-involved.html", "함께하기"),
           ("news.html", "소식·기록")],
}

# GIVING is closed: no payment link, no donation button and no ask for money.
# The giving sections are not in this repository; True needs giving_en.py and
# giving_ko.py beside this file, and a decision to open them.
OPEN_GIVING = False

STR = {
    "en": {
        "skip": "Skip to main content",
        "cta": "Contact",
        "contact": "Contact",
        "menu": "Menu",
        "lang_label": "Language",
        "logo_alt": "Classical Music for Everyone",
        "this_lang": "EN", "other_lang": "한국어",
        "tagline": "Bringing classical music <em>where it&rsquo;s needed!</em>",
        "tagline_plain": "Bringing classical music where it&rsquo;s needed!",
        "footer_about": ("We bring live classical music to the places it rarely reaches, and we "
                         "invite people to play as well as listen."),
        "f_explore": "Explore",
        "f_record": "Take part",
        "f_connect": "Connect",
        "f_legal": "© 2026 Classical Music for Everyone · Dublin, Ireland",
        "f_status": ("A not-for-profit community music initiative, forming a company limited by "
                     "guarantee. Not yet a registered charity."),
        "f_updated": "Updated",
        "f_privacy": "Privacy",
        "nav_label": "Main",
        "f_links": [("index.html", "Home"), ("about.html", "About"),
                    ("programmes.html", "Programmes"), ("get-involved.html", "Get involved"),
                    ("news.html", "News &amp; archive")],
        "f_links2": [("get-involved.html#invite", "Bring a concert"), ("get-involved.html#play", "Perform with us"),
                     ("get-involved.html#board", "Founding board")]
                    + ([("get-involved.html#friends", "Friends"), ("get-involved.html#sponsor", "Sponsor a concert")]
                       if OPEN_GIVING else []),
    },
    "ko": {
        "skip": "본문으로 건너뛰기",
        "cta": "문의",
        "contact": "문의",
        "menu": "메뉴",
        "lang_label": "언어",
        "logo_alt": "Classical Music for Everyone",
        "this_lang": "한국어", "other_lang": "EN",
        "tagline": '<span lang="en">Bringing classical music <em>where it&rsquo;s needed!</em></span>',
        "tagline_plain": '<span lang="en">Bringing classical music where it&rsquo;s needed!</span>',
        "footer_about": ("클래식 음악이 잘 닿지 않는 곳으로 찾아가, 듣는 분들을 직접 연주하도록 "
                         "초대합니다."),
        "f_explore": "둘러보기",
        "f_record": "함께하기",
        "f_connect": "연락",
        "f_legal": "© 2026 Classical Music for Everyone · 아일랜드 더블린",
        "f_status": "보증유한회사(CLG) 설립을 준비하는 비영리 공동체 음악 단체입니다. 아직 등록된 자선단체는 아닙니다.",
        "f_updated": "갱신",
        "f_privacy": "개인정보",
        "nav_label": "주 메뉴",
        "f_links": [("index.html", "홈"), ("about.html", "소개"),
                    ("programmes.html", "프로그램"), ("get-involved.html", "함께하기"),
                    ("news.html", "소식·기록")],
        "f_links2": [("get-involved.html#invite", "음악회 초청"), ("get-involved.html#play", "함께 연주하기"),
                     ("get-involved.html#board", "창립 이사회")]
                    + ([("get-involved.html#friends", "Friends"), ("get-involved.html#sponsor", "음악회 후원")]
                       if OPEN_GIVING else []),
    },
}

# The only script on the site is the menu's: the button opens and closes it,
# Escape closes it and gives focus back to the button, and a page brought
# back by the Back button (from the browser's cache, as it was left) opens
# with the menu shut, not frozen open over a page that cannot scroll.
MENU_JS = ("var n=document.getElementById('nav');"
           "var o=n.getAttribute('data-open')!==&quot;true&quot;;"
           "n.setAttribute('data-open',o);this.setAttribute('aria-expanded',o)")
ESC_JS = ("if(event.key==='Escape'){var n=document.getElementById('nav'),b=this.querySelector('.menu-toggle');"
          "if(n&amp;&amp;n.getAttribute('data-open')==='true'){n.setAttribute('data-open','false');"
          "b.setAttribute('aria-expanded','false');b.focus()}}")
RESET_JS = ("var n=document.getElementById('nav'),b=document.querySelector('.menu-toggle');"
            "if(n){n.setAttribute('data-open','false')}if(b){b.setAttribute('aria-expanded','false')}")


# Structured data is emitted as one @graph per page rather than a lone
# Organization block repeated on all 25 pages. The organisation is declared
# once with an @id; every other node — the page itself, a breadcrumb, an
# event — points at that @id instead of restating it. That is what lets a
# search engine treat the whole site as one entity, and it is why the
# programme pages can carry a breadcrumb without a second Organization.
# The organisation is described the same way on every page: the 25-word
# version from the messaging guide (kit 27), then its status sentence. It used
# to take each page's own description, so the contact page described the
# organisation as "email, phone and where we travel to".
ORG_DESC = ("Classical Music for Everyone brings live classical music, talks and a free recorder "
            "ensemble to older people, migrant communities and care settings in Dublin. It is a "
            "not-for-profit community music initiative, forming a company limited by guarantee. It "
            "is not yet a registered charity.")

ORG_NODE = """    {{
      "@type": "Organization",
      "@id": "{site}/#organisation",
      "name": "Classical Music for Everyone",
      "alternateName": "CMFE",
      "url": "{site}/",
      "logo": {{"@type": "ImageObject", "url": "{site}/assets/logo-horizontal.png"}},
      "image": "{site}/images/hero-outreach.jpg",
      "description": "{org_desc}",
      "foundingDate": "2024-01",
      "founder": {{"@type": "Person", "@id": "{site}/about.html#founder",
                  "name": "Andrew Seohyeon Kim"}},
      "email": "{email}",
      "telephone": "{phone}",
      "address": {{"@type": "PostalAddress", "addressLocality": "Dublin",
                  "addressCountry": "IE"}},
      "areaServed": [{{"@type": "City", "name": "Dublin"}},
                     {{"@type": "AdministrativeArea", "name": "County Meath"}},
                     {{"@type": "AdministrativeArea", "name": "County Wicklow"}},
                     {{"@type": "AdministrativeArea", "name": "County Westmeath"}}],
      "knowsLanguage": ["en", "ko"]
    }}"""

# The founder as a node of his own (on About, #founder, since 2026-09-30). Only what the founder profile publishes
# as public (04 §1–2): name, role, where he trained, the public profiles.
PERSON_NODE = """    {{
      "@type": "Person",
      "@id": "{site}/about.html#founder",
      "name": "Andrew Seohyeon Kim",
      "alternateName": "김서현",
      "description": "Clarinettist, organist and community musician in Dublin; founder of Classical Music for Everyone and the Letters Ensemble.",
      "alumniOf": {{"@type": "CollegeOrUniversity", "name": "TU Dublin Conservatoire"}},
      "sameAs": [{same_as}],
      "email": "{email}",
      "url": "{site}/about.html#founder"
    }}"""

PAGE_NODE = """    {{
      "@type": "WebPage",
      "@id": "{canonical}#page",
      "url": "{canonical}",
      "name": "{title}",
      "description": "{desc}",
      "inLanguage": "{lang}",
      "isPartOf": {{"@id": "{site}/#website"}},
      "about": {{"@id": "{site}/#organisation"}},
      "publisher": {{"@id": "{site}/#organisation"}},
      "primaryImageOfPage": {{"@type": "ImageObject", "url": "{image}"}}
    }}"""

SITE_NODE = """    {{
      "@type": "WebSite",
      "@id": "{site}/#website",
      "url": "{site}/",
      "name": "Classical Music for Everyone",
      "inLanguage": "{lang}",
      "publisher": {{"@id": "{site}/#organisation"}}
    }}"""


def _graph(nodes):
    return ('<script type="application/ld+json">\n'
            '{\n  "@context": "https://schema.org",\n  "@graph": [\n'
            + ",\n".join(nodes) + "\n  ]\n}\n</script>")


def breadcrumb(site, lang, slug, trail):
    """trail is [(path or None, label), ...]; the last item is this page."""
    items = []
    for i, (path, label) in enumerate(trail, start=1):
        loc = site + "/" + ("" if lang == "en" else "ko/") + (path or "")
        items.append('        {"@type": "ListItem", "position": %d, "name": "%s",'
                     ' "item": "%s"}' % (i, label, loc))
        
    return ('    {\n      "@type": "BreadcrumbList",\n      "itemListElement": [\n'
            + ",\n".join(items) + "\n      ]\n    }")


def _images(body, eager_first):
    """Lazy-load every image; the page's opening photograph, if it has one,
    loads eagerly and first."""
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


_SRCSET = re.compile(r'\bsrcset="([^"]*)"')


def _relink(markup, here, root):
    """Give every root-relative href/src in a body the prefix it needs, and
    every URL in a srcset the prefix of the shared images folder."""
    def sub(m):
        attr, path = m.group(1), m.group(2)
        pre = root if path.startswith(SHARED) else here
        return f'{attr}="{pre}{path}"'

    def subset(m):
        return 'srcset="' + ", ".join(root + c.strip() for c in m.group(1).split(",")) + '"'
    return _SRCSET.sub(subset, _LINK.sub(sub, markup))


def header(lang, slug):
    p, r, s = _here(slug), _root(lang, slug), STR[lang]
    rows = []
    for i, (href, label) in enumerate(NAV[lang], start=1):
        current = ' aria-current="page"' if href == slug else ""
        mark = '<span class="nav-mark" aria-hidden="true"></span>' if href == slug else ""
        rows.append(f'        <li><a class="nav-link" href="{p}{href}"{current}>'
                    f'<span class="nav-n" aria-hidden="true">{i:02d}</span>{label}{mark}</a></li>')
    links = "\n".join(rows)
    cta_current = ' aria-current="page"' if slug == "contact.html" else ""
    other = "ko" if lang == "en" else "en"
    return f"""<div class="progress" aria-hidden="true"></div>
<a class="skip" href="#main">{s['skip']}</a>
<header class="site-header" onkeydown="{ESC_JS}">
  <div class="wrap header-inner">
    <a class="brand" href="{p}index.html">
      <img src="{r}assets/logo-horizontal.svg" alt="{s['logo_alt']}"
           width="120" height="46" decoding="async">
    </a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav"
            aria-label="{s['menu']}" onclick="{MENU_JS}"><i></i><i></i></button>
    <nav class="nav" id="nav" data-open="false" aria-label="{s['nav_label']}">
      <ul class="nav-list">
{links}
      </ul>
      <a class="btn btn-primary btn-nav" href="{p}contact.html"{cta_current}>{s['cta']}</a>
      <div class="lang-switch" role="group" aria-label="{s['lang_label']}">
        <span aria-current="true">{s['this_lang']}</span>
        <a href="{_switch(lang, slug)}" hreflang="{other}" lang="{other}">{s['other_lang']}</a>
      </div>
    </nav>
  </div>
</header>"""


def footer(lang, slug="index.html"):
    p, r, s = _here(slug), _root(lang, slug), STR[lang]
    # the footer language link always goes to the other language's home page,
    # not to this page's twin: that is what the header switcher is for
    home_other = r + ("ko/index.html" if lang == "en" else "index.html")
    other = "ko" if lang == "en" else "en"
    links = "\n".join(f'          <li><a href="{p}{h}">{t}</a></li>' for h, t in s["f_links"])
    links2 = "\n".join(f'          <li><a href="{p}{h}">{t}</a></li>' for h, t in s["f_links2"])
    return f"""<footer class="site-footer">
  <div class="wrap">
    <p class="footer-line">{s['tagline']}</p>
    <div class="footer-grid">
      <div>
        <img src="{r}assets/logo-reversed.svg" alt="{s['logo_alt']}"
             width="109" height="42" loading="lazy" decoding="async">
        <p class="footer-about">{s['footer_about']}</p>
      </div>
      <nav aria-label="{s['f_explore']}">
        <h2>{s['f_explore']}</h2>
        <ul>
{links}
        </ul>
      </nav>
      <nav aria-label="{s['f_record']}">
        <h2>{s['f_record']}</h2>
        <ul>
{links2}
        </ul>
      </nav>
      <div>
        <h2>{s['f_connect']}</h2>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="tel:{PHONE_TEL}">{PHONE_INTL}</a></li>
          <li><a href="{p}contact.html">{s['contact']}</a></li>
          <li><a href="{home_other}" hreflang="{other}" lang="{other}">{s['other_lang']}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>{s['f_legal']}</span>
      <span>{s['f_status']}</span>
      <span>{s['f_updated']} {UPDATED[lang]} · <a href="{p}contact.html#privacy">{s['f_privacy']}</a></span>
    </div>
  </div>
</footer>"""


def page(lang, slug, title, description, body, og_image=None, extra_nodes=(), og_alt=None, og_size=(1800, 1350)):
    """extra_nodes: already-rendered JSON-LD nodes to add to this page's graph
    (a breadcrumb, an event) — see build.py."""
    p, r = _here(slug), _root(lang, slug)
    sub = "" if slug == "index.html" else slug
    # the first photograph is above the fold only when it opens the page:
    # the home hero, or the plate under an interior page's title
    first = body.find("<img")
    eager = first != -1 and ("hero-figure open" in body[:first] or "ph-figure wrap open" in body[:first])
    body = _images(body, eager_first=eager)
    body = _relink(body, p, r)
    canonical = f"{SITE_URL}/" + ("" if lang == "en" else "ko/") + sub
    desc = description.replace('"', "'")
    ld_lang = "en-IE" if lang == "en" else "ko"
    # a page shares its own photograph, not the site-wide hero, so a link to
    # a programme page previews that programme
    image = f"{SITE_URL}/images/{og_image}" if og_image else f"{SITE_URL}/images/hero-outreach.jpg"
    jsonld = _graph([
        ORG_NODE.format(site=SITE_URL, org_desc=ORG_DESC, email=EMAIL, phone=PHONE_INTL),
        SITE_NODE.format(site=SITE_URL, lang=ld_lang),
        PERSON_NODE.format(site=SITE_URL, email=EMAIL,
                           same_as=", ".join(f'"{u}"' for u in SOCIAL.values() if u)),
        PAGE_NODE.format(site=SITE_URL, canonical=canonical, title=title.replace('"', "'"),
                         desc=desc, lang=ld_lang, image=image),
        *extra_nodes,
    ])
    return f"""<!DOCTYPE html>
<html lang="{'en-IE' if lang == 'en' else 'ko'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#FAF5EE">
<meta name="color-scheme" content="light">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{SITE_URL}/{sub}">
<link rel="alternate" hreflang="ko" href="{SITE_URL}/ko/{sub}">
<link rel="alternate" hreflang="x-default" href="{SITE_URL}/{sub}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Classical Music for Everyone">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{image}">
<meta property="og:image:width" content="{og_size[0]}">
<meta property="og:image:height" content="{og_size[1]}">
<meta property="og:image:alt" content="{og_alt or title}">
<meta property="og:locale" content="{'en_IE' if lang == 'en' else 'ko_KR'}">
<meta property="og:locale:alternate" content="{'ko_KR' if lang == 'en' else 'en_IE'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{image}">
<meta name="author" content="Classical Music for Everyone">
<link rel="icon" href="{r}assets/logo-icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{r}assets/apple-touch-icon.png">
<link rel="manifest" href="{r}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS_EN if lang == 'en' and slug != '404.html' else FONTS}">
<link rel="stylesheet" href="{r}styles.css">
<link rel="expect" href="#main" blocking="render">
{jsonld}
</head>
<body onpageshow="{RESET_JS}">
{header(lang, slug)}
<main id="main">
{body}
</main>
{footer(lang, slug)}
</body>
</html>
"""


def jpeg_size(path):
    """(width, height) from a JPEG's frame header, without an image library."""
    with open(path, "rb") as fh:
        data = fh.read()
    i = 2
    while i < len(data):
        marker, length = data[i + 1], int.from_bytes(data[i + 2:i + 4], "big")
        if marker in (0xC0, 0xC1, 0xC2):
            return (int.from_bytes(data[i + 7:i + 9], "big"), int.from_bytes(data[i + 5:i + 7], "big"))
        i += 2 + length
    return (1400, 933)


def write(lang, slug, title, description, body, og_image=None, extra_nodes=(), og_alt=None):
    out = os.path.join(ROOT, "" if lang == "en" else "ko", slug)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    size = jpeg_size(os.path.join(ROOT, "images", og_image)) if og_image else (1800, 1350)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(page(lang, slug, title, description, body, og_image, extra_nodes, og_alt, size))
    return os.path.relpath(out, ROOT)
