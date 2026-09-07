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
         "family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600"
         "&family=Plus+Jakarta+Sans:wght@400;500;600;700"
         "&family=Noto+Sans+KR:wght@400;500;700&display=swap")

NAV = {
    "en": [("about.html", "About"), ("programmes.html", "Programmes"),
           ("get-involved.html", "Get Involved"), ("news.html", "What&rsquo;s On"),
           ("impact.html", "Impact"), ("support.html", "Support")],
    "ko": [("about.html", "소개"), ("programmes.html", "프로그램"),
           ("get-involved.html", "참여하기"), ("news.html", "일정과 소식"),
           ("impact.html", "성과"), ("support.html", "후원")],
}

# Six items plus Contact, which is the ceiling the sector settles on
# (12 — Brand & Web Master §8: organisations under five staff use five or
# six). Four of the six open a small panel. The panel is CSS-only — hover
# and :focus-within — and on a narrow screen it is an indented list inside
# the drawer. Order inside the Programmes panel matches the five cards
# everywhere else; no entry is marked out as the main one.
SUBNAV = {
    "about.html": {
        "en": [("about.html", "About us", "What we are, in three sentences"),
               ("founder.html", "The founder", "Andrew Seohyeon Kim"),
               ("identity.html", "The mark", "Why the gold falls on Everyone")],
        "ko": [("about.html", "단체 소개", "세 문장으로 말하는 우리"),
               ("founder.html", "창립자", "김서현"),
               ("identity.html", "상징과 표준", "금색이 Everyone 위에 놓이는 이유")],
    },
    "programmes.html": {
        "en": [("programmes/recorder-ensemble.html", "Free Recorder Ensemble course",
                "A term for complete beginners"),
               ("programmes/getting-to-know.html", "Getting to Know Classical Music",
                "Free lecture-recitals"),
               ("programmes/concert-companion.html", "Concert Guide &amp; Companion",
                "Accompanied concert-going"),
               ("programmes/outreach-concerts.html", "Outreach Concerts",
                "Care homes, parishes, hospitals"),
               ("programmes/letters-ensemble.html", "Letters Ensemble",
                "Amateur players, weekly")],
        "ko": [("programmes/recorder-ensemble.html", "무료 리코더 앙상블 과정",
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
    "news.html": {
        "en": [("news.html", "Coming up", "Classes enrolling, concerts with the door open"),
               ("archive.html", "The record, 2023 to date", "Every session and performance")],
        "ko": [("news.html", "다가오는 일정", "모집 중인 수업, 열려 있는 음악회"),
               ("archive.html", "기록, 2023년부터", "모든 회차와 연주")],
    },
    "impact.html": {
        "en": [("impact.html", "What has changed", "Only what the record supports"),
               ("impact.html#next", "Where this is going", "The next steps, in order"),
               ("impact.html#transparency", "Transparency", "Status, money, what is not proved")],
        "ko": [("impact.html", "무엇이 달라졌나", "기록이 뒷받침하는 것만"),
               ("impact.html#next", "가려는 곳", "다음 걸음, 순서대로"),
               ("impact.html#transparency", "투명성", "지위, 돈, 증명되지 않은 것")],
    },
    "support.html": {
        "en": [("support.html", "Support us", "Give, open a door, give a room"),
               ("partner.html", "Partner with us", "For organisations and funders")],
        "ko": [("support.html", "후원하기", "기부, 문 열기, 방 내어 주기"),
               ("partner.html", "기관 파트너십", "기관과 재단을 위한 안내")],
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
        "tagline": "Bringing classical music where it&rsquo;s needed!",
        "footer_about": ("We teach people to play — not only to listen — and bring live "
                         "classical music to the places it rarely reaches."),
        "f_explore": "Explore",
        "f_record": "Record &amp; support",
        "f_connect": "Connect",
        "f_legal": "© 2026 Classical Music for Everyone · Dublin, Ireland",
        "f_status": "Volunteer-led · formalising as a not-for-profit company limited by guarantee",
        "f_links": [("about.html", "About us"), ("founder.html", "The founder"), ("identity.html", "The mark"),
                    ("programmes.html", "Programmes"), ("get-involved.html", "Get involved"),
                    ("news.html", "What&rsquo;s on")],
        "f_links2": [("impact.html", "Our impact"), ("archive.html", "The record, 2023 to date"),
                     ("support.html", "Support our work"), ("partner.html", "Partner with us"),
                     ("impact.html#transparency", "Transparency")],
    },
    "ko": {
        "skip": "본문으로 건너뛰기",
        "contact": "문의",
        "menu": "메뉴",
        "lang_label": "언어",
        "logo_alt": "Classical Music for Everyone",
        "this_lang": "한국어", "other_lang": "EN",
        "tagline": "클래식 음악을, 그것이 필요한 곳으로!",
        "footer_about": ("듣는 데서 그치지 않고 직접 연주하도록 가르치고, "
                         "클래식 음악이 잘 닿지 않는 곳으로 찾아갑니다."),
        "f_explore": "둘러보기",
        "f_record": "기록과 후원",
        "f_connect": "연락",
        "f_legal": "© 2026 Classical Music for Everyone · 아일랜드 더블린",
        "f_status": "자원봉사로 운영 · 비영리 보증유한책임회사(CLG) 설립 준비 중",
        "f_links": [("about.html", "단체 소개"), ("founder.html", "창립자"), ("identity.html", "상징과 표준"),
                    ("programmes.html", "프로그램"), ("get-involved.html", "참여하기"),
                    ("news.html", "일정과 소식")],
        "f_links2": [("impact.html", "성과와 근거"), ("archive.html", "기록, 2023년부터"),
                     ("support.html", "후원하기"), ("partner.html", "기관 파트너십"),
                     ("impact.html#transparency", "투명성")],
    },
}

MENU_JS = ("var n=document.getElementById('nav');"
           "var o=n.getAttribute('data-open')!==&quot;true&quot;;"
           "n.setAttribute('data-open',o);this.setAttribute('aria-expanded',o)")


# Structured data is emitted as one @graph per page rather than a lone
# Organization block repeated on all 25 pages. The organisation is declared
# once with an @id; every other node — the page itself, a breadcrumb, an
# event — points at that @id instead of restating it. That is what lets a
# search engine treat the whole site as one entity, and it is why the
# programme pages can carry a breadcrumb without a second Organization.
ORG_NODE = """    {{
      "@type": ["Organization", "NGO"],
      "@id": "{site}/#organisation",
      "name": "Classical Music for Everyone",
      "alternateName": "CMFE",
      "url": "{site}/",
      "logo": {{"@type": "ImageObject", "url": "{site}/assets/logo-horizontal.png"}},
      "image": "{site}/images/hero-outreach.jpg",
      "description": "{desc}",
      "foundingDate": "2024-01",
      "founder": {{"@type": "Person", "@id": "{site}/founder.html#person",
                  "name": "Andrew Seohyeon Kim"}},
      "email": "{email}",
      "telephone": "{phone}",
      "address": {{"@type": "PostalAddress", "addressLocality": "Dublin",
                  "addressCountry": "IE"}},
      "areaServed": {{"@type": "Country", "name": "Ireland"}},
      "knowsLanguage": ["en", "ko"]
    }}"""

# The founder as a node of his own. Only what the founder profile publishes
# as public (04 §1–2): name, role, qualification, the LinkedIn profile.
PERSON_NODE = """    {{
      "@type": "Person",
      "@id": "{site}/founder.html#person",
      "name": "Andrew Seohyeon Kim",
      "alternateName": "김서현",
      "jobTitle": "Founder and Project Lead",
      "description": "Clarinettist, organist and community music practitioner based in Dublin; founder of Classical Music for Everyone and the Letters Ensemble.",
      "alumniOf": {{"@type": "CollegeOrUniversity", "name": "TU Dublin Conservatoire"}},
      "worksFor": {{"@id": "{site}/#organisation"}},
      "sameAs": [{same_as}],
      "email": "{email}",
      "url": "{site}/founder.html"
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
        # a page under programmes/, or one listed in this item's panel
        # (identity under About, archive under What's on, partner under
        # Support), lights the parent item too
        here = href == slug or (sub and (
            slug.startswith(href[:-5] + "/")
            or any(h.split("#")[0] == slug for h, *_ in sub[lang])))
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
        # no chevron: it sat below the word and broke the nav baseline. The
        # panel opens on hover and on keyboard focus, which is the affordance.
        rows.append(
            f'      <div class="nav-item has-sub">\n'
            f'        <a class="nav-link" href="{p}{href}"{current}>{label}</a>\n'
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
      <a class="btn btn-accent btn-nav" href="{p}contact.html">{s['contact']}</a>
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
    # not to this page's twin — that is what the header switcher is for
    home_other = r + ("ko/index.html" if lang == "en" else "index.html")
    links = "\n".join(f'        <a href="{p}{h}">{t}</a>' for h, t in s["f_links"])
    links2 = "\n".join(f'        <a href="{p}{h}">{t}</a>' for h, t in s["f_links2"])
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
        <h3>{s['f_record']}</h3>
{links2}
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


def page(lang, slug, title, description, body, og_image=None, extra_nodes=()):
    """extra_nodes: already-rendered JSON-LD nodes to add to this page's graph
    (a breadcrumb, an event) — see build.py."""
    p, r = _here(slug), _root(lang, slug)
    sub = "" if slug == "index.html" else slug
    body = _images(body, eager_first='<section class="hero">' in body)
    body = _relink(body, p, r)
    canonical = f"{SITE_URL}/" + ("" if lang == "en" else "ko/") + sub
    desc = description.replace('"', "'")
    ld_lang = "en-IE" if lang == "en" else "ko"
    # a page shares its own photograph, not the site-wide hero, so a link to
    # a programme page previews that programme
    image = f"{SITE_URL}/images/{og_image}" if og_image else f"{SITE_URL}/images/hero-outreach.jpg"
    jsonld = _graph([
        ORG_NODE.format(site=SITE_URL, desc=desc, email=EMAIL, phone=PHONE_INTL),
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
<meta property="og:image" content="{image}">
<meta property="og:image:width" content="1400">
<meta property="og:image:height" content="933">
<meta property="og:image:alt" content="{title}">
<meta property="og:locale" content="{'en_IE' if lang == 'en' else 'ko_KR'}">
<meta property="og:locale:alternate" content="{'ko_KR' if lang == 'en' else 'en_IE'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{image}">
<meta name="author" content="Classical Music for Everyone">
<link rel="icon" href="{r}assets/logo-icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{r}assets/logo-icon.png">
<link rel="manifest" href="{r}site.webmanifest">
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


def write(lang, slug, title, description, body, og_image=None, extra_nodes=()):
    out = os.path.join(ROOT, "" if lang == "en" else "ko", slug)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(page(lang, slug, title, description, body, og_image, extra_nodes))
    return os.path.relpath(out, ROOT)
