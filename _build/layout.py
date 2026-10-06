"""Shared page shell for the CMFE site.

Emits plain static HTML — there is no runtime dependency. Run `_build/build.py`
after editing content, or edit the generated .html files directly.
Directories beginning with an underscore are not published by GitHub Pages.
"""

import html
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
         "&family=Noto+Sans+KR:wght@400;700&display=swap")
# An English page carries two Korean words (the language switch) and no
# Korean text, so it does not wait for the Korean family: those two words
# take the system's Korean face. The 404 page is in both languages.
FONTS_EN = FONTS.replace("&family=Noto+Sans+KR:wght@400;700", "")
# Korean is set in two weights only, 400 and 700 (QA, 1 Oct 2026: three
# weights meant 15-19 font files and a slow first paint on a phone).

# The date the copy was last checked against the canonical set and the kit,
# printed in every footer (24: the website is a trust document, and a reader
# should see when it was last looked at). Change it by hand when the content
# is reviewed, not on every rebuild.
UPDATED = {"en": "5 October 2026", "ko": "2026년 10월 5일"}
UPDATED_ISO = "2026-10-05"

# Six pages and the language switch (2026-09-30: five pages, then News &
# archive added back when the organisation was restructured). Five plain
# links; Contact is the one filled button, so the header still has a single
# clear action. Programmes opens a panel of the five programme pages on hover
# and keyboard focus (Andrew, 3 Oct 2026 evening: "from the menu I want to
# see each programme and choose it"); in the phone menu they are listed
# under it. The names come from each deck's PROGRAMMES_DATA (PROG_MENU).
NAV = {
    "en": [("index.html", "Home"), ("about.html", "About"),
           ("programmes.html", "Programmes"), ("get-involved.html", "Get involved"),
           ("news.html", "News &amp; archive")],
    "ko": [("index.html", "홈"), ("about.html", "소개"),
           ("programmes.html", "프로그램"), ("get-involved.html", "함께하기"),
           ("news.html", "소식·기록")],
}

PROG_MENU = {"en": [], "ko": []}

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
        "running": ", running now",
        "lang_label": "Language",
        "logo_alt": "Classical Music for Everyone",
        "this_lang": "EN", "other_lang": "한국어",
        # "Classical Music" is one unit (R23): balance once split it, "Bringing Classical / Music"
        "tagline": 'Bringing <span class="cm">Classical Music</span> <em>where it&rsquo;s needed!</em>',
        "tagline_plain": "Bringing Classical Music where it&rsquo;s needed!",
        # the footer's line about what we do went on 2 Oct 2026: it was the third
        # telling of the hero lead on every page (content review); "" omits it
        "footer_about": "",
        "f_explore": "Explore",
        "f_record": "Get involved",
        "f_connect": "Connect",
        "f_legal": "© 2026 Classical Music for Everyone · Dublin, Ireland",
        "f_status": ("Classical Music for Everyone is a not-for-profit community music initiative, "
                     "forming\u00a0a\u00a0company limited by guarantee. It is not yet a registered charity."),
        "f_updated": "Updated",
        "f_privacy": "Privacy notice",
        "nav_label": "Main",
        "f_links": [("index.html", "Home"), ("about.html", "About"),
                    ("programmes.html", "Programmes"), ("get-involved.html", "Get involved"),
                    ("news.html", "News &amp; archive")],
        "f_links2": [("get-involved.html#invite", "Invite us to play"), ("get-involved.html#play", "Perform with us"),
                     ("get-involved.html#board", "Founding board")]
                    + ([("get-involved.html#friends", "Friends"), ("get-involved.html#sponsor", "Sponsor a concert")]
                       if OPEN_GIVING else []),
    },
    "ko": {
        "skip": "본문으로 건너뛰기",
        "cta": "문의",
        "contact": "문의",
        "menu": "메뉴",
        "running": ", 진행 중",
        "lang_label": "언어",
        "logo_alt": "Classical Music for Everyone",
        "this_lang": "한국어", "other_lang": "English",
        "tagline": '<span lang="en">Bringing <span class="cm">Classical Music</span> '
                   '<em>where it&rsquo;s needed!</em></span>',
        "tagline_plain": '<span lang="en">Bringing Classical Music where it&rsquo;s needed!</span>',
        "footer_about": "",
        "f_explore": "둘러보기",
        "f_record": "함께하기",
        "f_connect": "연락",
        "f_legal": "© 2026 Classical Music for Everyone · 아일랜드 더블린",
        "f_status": ("Classical Music for Everyone은 보증유한회사(CLG) 설립을 준비하고 있는 "
                     "비영리\u00a0공동체\u00a0음악\u00a0단체입니다. 아직 등록된 자선단체는 아닙니다."),
        "f_updated": "갱신",
        "f_privacy": "개인정보 처리방침",
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
ESC_JS = ("if(event.key==='Escape'){var n=document.getElementById('nav'),b=document.querySelector('.menu-toggle'),"
          "a=document.activeElement,f=a&amp;&amp;a.closest('.has-sub'),h=f||document.querySelector('.has-sub:hover');"
          "if(n&amp;&amp;n.getAttribute('data-open')==='true'){n.setAttribute('data-open','false');"
          "b.setAttribute('aria-expanded','false');b.focus()}"
          "else if(h){h.setAttribute('data-shut','');if(f)h.querySelector('.nav-link').focus()}}")
# the programmes panel, shut with Escape, opens again once the pointer or
# the focus has left it
SUB_JS = ("onmouseleave=\"this.removeAttribute('data-shut')\" "
          "onfocusout=\"if(!this.contains(event.relatedTarget))this.removeAttribute('data-shut')\"")
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
ORG_DESC = ("Classical Music for Everyone brings live Classical Music, talks and a recorder class to "
            "people in Dublin who find it hard to get to concerts. Classical Music for Everyone is a "
            "not-for-profit community music initiative, forming a company limited by guarantee. It is "
            "not yet a registered charity.")

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
      "inLanguage": ["en-IE", "ko"],
      "publisher": {{"@id": "{site}/#organisation"}}
    }}"""



def _jtext(text):
    """Text for a JSON-LD string: entities decoded (a <script> block does not
    decode them, so "&amp;" would reach a search engine as five characters),
    then made safe inside double quotes."""
    return html.unescape(text).replace("\\", "\\\\").replace('"', '\\"')

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
    # a programme page (programmes/<slug>.html) sits under Programmes: the
    # parent link is marked as the current section, not as the current page
    section = "programmes.html" if slug.startswith("programmes/") else None
    for i, (href, label) in enumerate(NAV[lang], start=1):
        current = (' aria-current="page"' if href == slug else
                   ' aria-current="true"' if href == section else "")
        mark = '<span class="nav-mark" aria-hidden="true"></span>' if current else ""
        link = (f'<a class="nav-link" href="{p}{href}"{current}>'
                f'<span class="nav-n" aria-hidden="true">{i:02d}</span>{label}{mark}</a>')
        if href == "programmes.html" and PROG_MENU[lang]:
            subs = "".join(
                f'<li><a href="{p}programmes/{s_}.html"{" aria-current=\"page\"" if slug == f"programmes/{s_}.html" else ""}>'
                f'<span class="ns-n" aria-hidden="true">{k:02d}</span><span class="ns-name">{name}'
                + (f'<span class="ns-live" aria-hidden="true"></span><span class="sr-only">{s["running"]}</span>' if live else "")
                + '</span></a></li>'
                for k, (s_, name, live) in enumerate(PROG_MENU[lang], start=1))
            rows.append(f'        <li class="has-sub" {SUB_JS}>{link}\n'
                        f'          <ul class="nav-sub">{subs}</ul></li>')
        else:
            rows.append(f'        <li>{link}</li>')
    links = "\n".join(rows)
    cta_current = ' aria-current="page"' if slug == "contact.html" else ""
    other = "ko" if lang == "en" else "en"
    rel = "" if slug == "404.html" else ' rel="alternate"'
    tongue = (f'href="{_switch(lang, slug)}" hreflang="{other}" lang="{other}"{rel} '
              f'translate="no">{s["other_lang"]}</a>')
    return f"""<div class="progress" aria-hidden="true"></div>
<a class="skip" href="#main">{s['skip']}</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{p}index.html">
      <img src="{r}assets/logo-horizontal.svg" alt="{s['logo_alt']}"
           width="120" height="46" decoding="async">
    </a>
    <a class="lang lang-bar" {tongue}
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav"
            aria-label="{s['menu']}" onclick="{MENU_JS}"><i></i><i></i></button>
    <nav class="nav" id="nav" data-open="false" aria-label="{s['nav_label']}">
      <ul class="nav-list">
{links}
      </ul>
      <a class="btn btn-nav" href="{p}contact.html"{cta_current}>{s['cta']}</a>
    </nav>
    <a class="lang lang-wide" {tongue}
  </div>
</header>"""


def footer(lang, slug="index.html"):
    p, r, s = _here(slug), _root(lang, slug), STR[lang]
    # the footer's language link goes to this page in the other language, as
    # the header's does (v7: it went to the other home page)
    other = "ko" if lang == "en" else "en"
    links = "\n".join(f'          <li><a href="{p}{h}">{t}</a></li>' for h, t in s["f_links"])
    links2 = "\n".join(f'          <li><a href="{p}{h}">{t}</a></li>' for h, t in s["f_links2"])
    return f"""<footer class="site-footer">
  <div class="wrap">
    <p class="footer-line">{s['tagline']}</p>
    <div class="footer-grid">
      <div>
        <img class="logo-screen" src="{r}assets/logo-reversed.svg" alt="{s['logo_alt']}"
             width="229" height="88" loading="lazy" decoding="async">
        <img class="logo-print" src="{r}assets/logo-horizontal.svg" alt="" aria-hidden="true"
             width="229" height="88" loading="lazy" decoding="async">
        {f'<p class="footer-about">{s["footer_about"]}</p>' if s['footer_about'] else ''}
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
          <li><a href="{_switch(lang, slug)}" hreflang="{other}" lang="{other}" rel="alternate" translate="no">{s['other_lang']}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>{s['f_legal']}</span>
      <span class="footer-status">{s['f_status']}</span>
      <span>{s['f_updated']} {UPDATED[lang]} · <a href="{p}contact.html#privacy">{s['f_privacy']}</a></span>
    </div>
  </div>
</footer>"""


# ---------------------------------------------------------------------------
# A lead says one sentence a line (Andrew, 2 Oct 2026: "the sentences do not
# break at the sentence, so readability and proportion look odd"). Each
# sentence of a lead-type block is wrapped in <span class="sl">, which
# styles.css sets as its own balanced block. Running text (answers, steps,
# paragraphs, clauses) is left to flow. Done here, once, for every page, so a
# new lead cannot slip through unsplit.
# ---------------------------------------------------------------------------
# and a value of two sentences on Contact (the insurance line), a line each,
# and the status sentence in the footer ("…guarantee. It / is not yet…")
SENTENCE_BLOCKS = ("lead", "ph-lead", "sh-lead", "figs-note", "pi-text", "wa-v", "footer-status", "tl-text",
                   # v7, chief designer: the answers on About and the programme pages
                   # ("gifts yet. We / will never ask"), and the privacy notice's intro
                   "qa-a", "pv-intro",
                   # v7, chief designer round 3: "concert. Then / we go", "Dublin. For"
                   # (the privacy clauses flow again: legal sentences longer than their line
                   # stepped short, long, short, long, a fresh reviewer, v7)
                   "step-t", "ct-how", "map-cap")
# split too, but the sentences sit side by side where the block fits one line
# (styles.css .sl-n, a line each only under 48em): the programme status
# ("Write to us. We will plan a talk with your group.") and the join hint
# ("One line is enough. If it helps, tell us:") wrap only on a phone, and as
# blocks on every screen they read as two separate notes (audit, after).
SENTENCE_NARROW = ("pp-say", "join-hint", "ct-hint", "ct-help")
_SB_OPEN = re.compile(r'<(p|span|div|dd|figcaption)\b[^>]*?\bclass="([^"]*)"[^>]*>')
_SB_TAG = re.compile(r"<(/?)([a-zA-Z][a-zA-Z0-9]*)\b[^>]*?(/?)>")
_SB_VOID = {"br", "img", "wbr", "input", "meta", "link", "hr", "source", "path", "circle", "rect", "line"}
# the end of a sentence: . ! or ? (and a closing quote), then a space and the
# start of the next one; English sentences start with a capital, a figure,
# an opening quote or a tag
_SB_END = {
    "en": re.compile(r"[.!?](?:&rdquo;|&rsquo;|[”’)])?(?=\s+(?:&[lr]dquo;|&lsquo;|<|[“‘(A-Z0-9]))"),
    "ko": re.compile(r"[.!?](?:&rdquo;|&rsquo;|[”’)])?(?=\s+\S)"),
}
# a full stop after these does not end a sentence (readability.py agrees)
_SB_ABBR = re.compile(r"\b(?:Co|St|Dr|Mr|Mrs|Ms|Fr|Sr|Rev|No|approx|e\.g|i\.e|etc|vs)\.$")


def _sentences(inner, lang):
    """Split a block's inner HTML into sentences, only where the break falls
    outside any inline element (a link or a strong that holds two sentences
    stays whole)."""
    depth, top = 0, []          # spans of inner that sit at depth 0
    pos = 0
    for m in _SB_TAG.finditer(inner):
        if m.start() > pos and depth == 0:
            top.append((pos, m.start()))
        closing, name, selfclose = m.group(1), m.group(2).lower(), m.group(3)
        if not selfclose and name not in _SB_VOID:
            depth += -1 if closing else 1
        pos = m.end()
    if pos < len(inner) and depth == 0:
        top.append((pos, len(inner)))
    cuts = []
    for m in _SB_END[lang].finditer(inner):
        end = m.end()
        if not any(a < end <= b for a, b in top):
            continue
        if _SB_ABBR.search(inner[max(0, m.start() - 8):m.start() + 1]):
            continue
        cuts.append(end)
    parts, last = [], 0
    for c in cuts:
        parts.append(inner[last:c].strip())
        last = c
    parts.append(inner[last:].strip())
    return [x for x in parts if x]


def _close(markup, start, name):
    """Index of the end tag that closes the element whose start tag ends at
    start."""
    depth = 1
    for m in _SB_TAG.finditer(markup, start):
        closing, tag, selfclose = m.group(1), m.group(2).lower(), m.group(3)
        if selfclose or tag in _SB_VOID:
            continue
        depth += -1 if closing else 1
        if depth == 0:
            return m.start()
    return -1


def _text_sub(markup, pattern, repl):
    """Apply a substitution to the text of markup, never inside a tag."""
    parts = re.split(r"(<[^>]+>)", markup)
    for i in range(0, len(parts), 2):
        parts[i] = pattern.sub(repl, parts[i])
    return "".join(parts)


# English leads: "and" and "or" go to the next line with their word, never
# hang at a line end ("Care homes, hospitals, parishes and / community"),
# unless that word is already part of a tied name
_LEAD_CONJ = re.compile(r"\b(and|or) (?=[^\s\u00a0<]+(?:[ \n.,;:!?]|$))")


def _ko_tail(sentence):
    """Korean leads: the last two words of a sentence stay on one line when
    they hold ten syllables or fewer. Chrome's text-wrap:pretty does this;
    Firefox and Safari before 26 do not, and left "연주합니다." alone."""
    i, inside = len(sentence) - 1, False
    while i >= 0:
        ch = sentence[i]
        if ch == ">":
            inside = True
        elif ch == "<":
            inside = False
        elif ch == " " and not inside:
            break
        i -= 1
    if i <= 0:
        return sentence
    head, tail = sentence[:i], sentence[i + 1:]
    last = re.sub(r"<[^>]+>", "", tail)
    before = re.sub(r"<[^>]+>", "", head).split()[-1:] or [""]
    if len(re.sub(r"[^가-힣A-Za-z0-9]", "", before[0] + last)) <= 10:
        return head + NBSP + tail
    return sentence


def sentence_lines(body, lang):
    out, pos = [], 0
    for m in _SB_OPEN.finditer(body):
        classes = set(m.group(2).split())
        if m.start() < pos or not classes & set(SENTENCE_BLOCKS + SENTENCE_NARROW):
            continue
        cls = "sl" if classes & set(SENTENCE_BLOCKS) else "sl sl-n"
        end = _close(body, m.end(), m.group(1))
        if end == -1:
            continue
        inner = body[m.end():end]
        # a block may carry its own language (the bilingual 404 page)
        own = re.search(r'\blang="(en|ko)', m.group(0))
        block_lang = own.group(1) if own else lang
        parts = _sentences(inner, block_lang)
        if block_lang == "ko":
            parts = [_ko_tail(x) for x in parts]
        else:
            parts = [_text_sub(x, _LEAD_CONJ, lambda k: k.group(1) + NBSP) for x in parts]
        out.append(body[pos:m.end()])
        out.append(" ".join(f'<span class="{cls}">{x}</span>' for x in parts) if len(parts) > 1 else parts[0])
        pos = end
    out.append(body[pos:])
    return "".join(out)


# a compound that must not break at its own hyphen: at 390px the status
# sentence read "is a not- / for-profit community" (typography audit, 2 Oct
# 2026). A non-breaking hyphen would depend on the font having the glyph.
KEEP_WHOLE = ("not-for-profit",)


# Safari breaks a quoted word from the Korean particle after it ('Everyone'/은,
# research department, 2 Oct 2026); neither keep-all nor a word joiner stops
# it, only a no-wrap span does
_QUOTE_PARTICLE = re.compile(r"((?:&lsquo;|‘)[^&<’]{1,24}(?:&rsquo;|’)[가-힣]{1,2})")


def keep_whole(markup, lang="en"):
    parts = re.split(r"(<[^>]+>)", markup)
    for i in range(0, len(parts), 2):
        for w in KEEP_WHOLE:
            parts[i] = parts[i].replace(w, f'<span class="nowrap">{w}</span>')
        if lang == "ko":
            parts[i] = _QUOTE_PARTICLE.sub(r'<span class="nowrap">\1</span>', parts[i])
    return "".join(parts)


# Words that belong together never part at the end of a line (typography
# pass, 2 Oct 2026; R6): a number and its counter (여섯 명, which split
# "여섯 / 명이" on a phone), a district and its number (Dublin 15, 더블린 15구),
# a day and its month, a month and its year, a time range (7pm to 8pm,
# 저녁 7시). The space becomes a no-break space; nothing else changes.
NBSP = "\u00a0"
_MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
_TIME = r"\d{1,2}(?::\d{2})?(?:am|pm)"
_KO_NUM = (r"(?:(?:열|스물|서른|마흔|쉰)?(?:한|두|세|네|다섯|여섯|일곱|여덟|아홉)|열|스무|스물|서른|마흔|쉰|몇"
           r"|\d+)")
_KO_COUNT = r"(?:번째|째|명|분|곳|번|가지|줄|해|달|주|시간|곡|대|개|쪽|사람|회|개국|주년|살|군데)"
_KO_PART = r"[이가을를은는의도에과와만께로입]"
_TIES = {
    "en": [
        re.compile(r"\b(Dublin) (?=\d)"),
        re.compile(r"\b(Co\.|St|No\.) (?=[0-9A-Z])"),
        # (articles are tied in tie(), which can see the next tag and the
        # length of a tied name after them)
        re.compile(rf"\b(\d{{1,2}}) (?=(?:{_MONTHS})\b)"),
        # a number stays with what it counts: "Six / people" parted at a line
        # end on About (v7); a word of three letters or more, so "one at a
        # time" is left free
        re.compile(r"\b((?:[Oo]ne|[Tt]wo|[Tt]hree|[Ff]our|[Ff]ive|[Ss]ix|[Ss]even|[Ee]ight|[Nn]ine|[Tt]en|"
                   r"[Ee]leven|[Tt]welve|[Ff]ifteen|[Tt]wenty|\d{1,3})) (?=[a-z]{3,9}\b)"),
        re.compile(rf"\b((?:{_MONTHS})) (?=\d{{4}}\b)"),
        re.compile(rf"\b({_TIME}) (?=to {_TIME})"),
        re.compile(rf"\b({_TIME}[ \u00a0]to) (?={_TIME})"),
        # a year stays with "since" (chief designer v7 round 5: "since / 2024" at 390)
        re.compile(r"\b([Ss]ince) (?=\d{4}\b)"),
    ],
    "ko": [
        re.compile(rf"(?<![가-힣])({_KO_NUM}) (?={_KO_COUNT}(?![가-힣])|{_KO_COUNT}{_KO_PART})"),
        # (determiners such as 그 방 · 첫 주 are tied in tie(), which can see
        # across a tag)
        # a noun stays with the dependent noun after it (병원 등, 공연 중에도, 10주 동안)
        re.compile(rf"([가-힣0-9]+) (?=(?:등|중|동안)(?:{_KO_PART}|[\s.,:]|$))"),
        re.compile(r"(국립) (?=콘서트홀)"),
        re.compile(r"(\S+에) (?=관한|대한)"),
        re.compile(r"(더블린) (?=\d+구)"),
        # a city stays with its district, also a district named in English
        # (「더블린 / Dolphin's Barn」, chief designer v7 round 5)
        re.compile(r"(더블린|\d+구) (?=[A-Z])"),
        # and a county with its 주 (「위클로 / 주」 in the phone record, v7 round 5)
        re.compile(r"(위클로|미스|웨스트미스|킬데어|코크|골웨이) (?=주(?![가-힣]))"),
        # an auxiliary verb stays with the verb it follows (「알아 / 가는」, 「알려 / 드립니다」):
        # a verb's -아/-어 form (not the particle 와) and the helper after it
        re.compile(r"(?<![가-힣])([가-힣]*[아어여려워해겨져쳐]) (?=(?:가|갑|간|오|온|왔|보|봐|주|줘|줍|드리|드립|드려|두|놓)[가-힣]{0,4}(?![가-힣]))"),
        re.compile(r"(\d{4}년) (?=\d{1,2}월)"),
        re.compile(r"(\d{1,2}월) (?=\d{1,2}일)"),
        re.compile(r"(오전|오후|아침|낮|저녁|밤) (?=\d)"),
    ],
}


# A Korean dependent noun stays with the word that governs it (할 수 있습니다,
# 준비할 것, 읽을 줄, 있을 때): the governing word ends in a syllable with a
# final ㄹ or ㄴ, which needs the syllable's final consonant, hence a function.
_KO_DEP = re.compile(r"([가-힣]+) (?=(?:것|줄|때|데|뿐|분들|분)(?:[이가을를은는도에만의로와과입]|[\s.,:]|$)|수 (?:있|없))")
_KO_SU = re.compile("(?<=[가-힣][ \u00a0])(수) (?=있|없)")


def _ko_dependent(text):
    def bind(m):
        last = m.group(1)[-1]
        final = (ord(last) - 0xAC00) % 28
        return m.group(1) + (NBSP if final in (4, 8) else " ")
    text = _KO_DEP.sub(bind, text)
    return _KO_SU.sub(lambda m: m.group(1) + NBSP, text)


# two-word names balance used to split ("Presentation / Sisters", "South /
# Dublin Live"); UKAAF: keep a name, a date or a number on one line
# the Korean places are blocks at any length: a district or county after them moves
# down whole instead ("마리아의 프란치스코 선교 / 수녀회", chief designer v7)
KO_PLACES = ("마리아의 프란치스코 선교 수녀회", "성 골롬반 외방선교 수녀회", "관덕정 순교기념관",
             # v7 round 5: 「은퇴한 Presentation / 수녀님…」 in the phone timeline
             "Presentation 수녀회", "Presentation 수녀님")
# on Korean pages the two long English venues are blocks too (chief designer v7 round 5:
# 「Tallaght University / Hospital」 and 「Methodist / Centenary Church에서」 in the phone record and
# timeline, where a Korean sentence cannot simply end or begin on them); English pages keep the v6
# rule (their sentences end or begin on the name)
KO_BLOCKS = ("Tallaght University Hospital", "Methodist Centenary Church")
_NAMES_KO = re.compile("(" + "|".join(re.escape(n) for n in KO_BLOCKS) + ")")
NAMES = ("Presentation Sisters", "Letters Ensemble", "Community Centre", "Concert Hall", "TU Dublin",
         "Dublin Live", "Royal Albert Hall", "Clondalkin Lodge", "Dalgan Park", "BBC Proms", "Rua Red",
         # the scheme's name ("South / Dublin Live 2026" broke in the timeline, CD v6); with
         # its year, 22 letters, it was longer than a figure's label and broke inside
         "South Dublin Live",
         # the founder's name: "Andrew / Seohyeon Kim" may break, never "Seohyeon / Kim"
         # (the whole name, 19 letters, did not fit a 320px column and broke inside)
         "Seohyeon Kim",
         # the base, in the footer's copyright line and on Contact ("Dublin, / Ireland")
         "Dublin, Ireland",
         # v7: names the desks saw split at a line end ("성 / 파트리치오" at 1440, "Carmelite /
         # Community Centre" in the talks record, "Dolphin's / Barn", "the Sally / Gardens")
         # (the long venues, 26 and 27 letters, are not tied: R12 keeps a tie near 20, and tied they
         # broke inside a word on phones; their sentences end or begin on them instead, v6)
         "성 파트리치오", "성 골롬반", "Dolphin&rsquo;s Barn", "Sally Gardens", "아일랜드 더블린",
         # the name of what we do, in running text too ("talks on Classical / Music" on a phone,
         # v7); the master line's own span (.cm) keeps its 200% release, so it is left alone
         "Classical Music",
         # v7, chief designer: "a National / Concert Hall series", "RTÉ / Concert Orchestra",
         # "European / Economic Area", 「커뮤니티 / 센터를」, 「국립 / 교향악단」, 「복장 / 규정」,
         # 「요청 / 시」, 「단체 / 소개」 (a link), 「Down by / the Sally Gardens」 (a song's title)
         "National Concert Hall", "RT&Eacute; Concert Orchestra", "European Economic Area",
         "커뮤니티 센터", "국립 교향악단", "RT&Eacute; 콘서트 오케스트라", "복장 규정", "요청 시", "단체 소개",
         "Down by the Sally Gardens", "가장 최근",
         # v7, chief designer round 3: the record's long places ("Missionary Sisters of / St
         # Columban" at 1440), the card's title ("Getting to / Know Classical Music"), the
         # orchestra's whole name ("the TU Dublin / Philharmonic")
         "Franciscan Missionaries of Mary", "Missionary Sisters of St Columban",
         "Gwandukjeong Martyrs Memorial Centre", "Blessed Sacrament Chapel", "Rua Red Performance Space",
         "TU Dublin Philharmonic", "Getting to Know") + KO_PLACES
# a name and the article before it ("the Presentation Sisters"): the article
# stays with the name (v7, kinsoku: "the / Letters Ensemble" at 320px, where
# the article rule counted the comma after the name and let it go)
_NAMES = re.compile("(?:\\b((?:[Aa]n?|[Tt]he) ))?(" + "|".join(re.escape(n) for n in sorted(NAMES, key=len, reverse=True)) + ")")
# A name longer than a tie should be (R12: about 20 letters) is kept whole by
# an inline block instead of no-break spaces: it moves to the next line whole
# when it fits there, and only in a column narrower than itself wraps, between
# its words (v7: tied with no-break spaces, "National Concert Hall." was wider
# than the 320px timeline column and broke inside "Hall"). The build marks it
# while the other ties run, so they see it as one word, then writes the span.
_TN_OPEN, _TN_CLOSE, _TN_SP = "\ue011", "\ue012", "\ue010"   # not the highlight's \ue000 \ue001


# what may not part from a long name: before it an article and an opening
# quote or bracket; after it a closing quote or bracket, a joined Korean
# particle or ending (after a word joiner) or "'s", and punctuation
_TN_BEFORE = re.compile("((?:\\b(?:[Aa]n?|[Tt]he)[ \u00a0])?(?:&lsquo;|&ldquo;|[\u2018\u201c\u300c\u300e(])?)" + _TN_OPEN)
_TN_AFTER = re.compile(_TN_CLOSE + "((?:&rsquo;|&rdquo;|[\u2019\u201d\u300d\u300f)])?\u2060?"
                       "(?:&rsquo;s|\u2019s|[\uac00-\ud7a3]+)?(?:[,.;:!?](?:&rsquo;|&rdquo;|[\u2019\u201d)])?)?)")


def _name_tie(m):
    """A name over 20 letters, or a name with its article, becomes a block (it
    keeps whole where it fits and wraps only between its words where the
    column is narrower: "the Letters Ensemble." tied with no-break spaces was
    wider than the 320px timeline column and broke inside "Ensemble"); a short
    bare name is tied with no-break spaces (a link's underline does not run
    under a block)."""
    art, name = m.group(1) or "", m.group(2)
    if art or name in KO_PLACES or len(re.sub(r"&[a-zA-Z]+;", "x", name)) > 20:
        return _TN_OPEN + (art + name).replace(" ", _TN_SP) + _TN_CLOSE
    return name.replace(" ", NBSP)


def _name_heading(m):
    """In a title: a short bare name tied, a long one or one with its article
    left to the title's balanced wrap."""
    art, name = m.group(1) or "", m.group(2)
    if not art and len(re.sub(r"&[a-zA-Z]+;", "x", name)) <= 20:
        return name.replace(" ", NBSP)
    return m.group(0)


def _name_nbsp(m):
    """Inside a drawing (an SVG title) there are no blocks: no-break spaces."""
    return (m.group(1) or "") + m.group(2).replace(" ", NBSP)
# phrases that read as one (chief designer v7 round 5: "for / example", "one / at a time",
# "access / needs", "Our Lady / of Dolours" and the quoted question at 390; "care homes" was
# tied and let go: on the home card it could not make three lines and pushed every card's
# status down, a fresh reviewer);
# a name's own tie may already have joined part of one, hence the [ \u00a0]
_PHRASES = re.compile("|".join(
    p.replace(" ", "[ \u00a0]") for p in (
        r"\bfor example\b", r"\bone at a time\b", r"\baccess needs\b",
        r"\breligious communities\b", r"\ball seven\b",
        r"\bOur Lady of Dolours\b", r"&lsquo;what is Classical Music\?&rsquo;")))


def _phrase_tie(m):
    return re.sub("[ \u00a0]", NBSP, m.group(0))


# a Korean list dot never starts a line ("세이프가딩 / ·돌봄"): a word joiner
# before it forbids that break and leaves the break after it
_KO_DOT = re.compile("(?<=[^\\s\u00a0\u2060])·")


# a Korean determiner stays with its noun (그 방, 첫 주, 각 프로그램) -- but
# 이 right after a word, a tag or a Latin name is the subject particle
# ("Letters Ensemble이 맡는", "<strong>김서현</strong>이"), not "this"
_KO_DET = re.compile(r"(그|이|저|첫|각|몇|모든) (?=[가-힣])")
_WORDLIKE = re.compile(r"[가-힣A-Za-z0-9’”)\]]")


def _ko_determiners(text, prev):
    def bind(m):
        before = text[m.start() - 1] if m.start() else prev
        return m.group(0) if before and _WORDLIKE.match(before) else m.group(1) + NBSP
    return _KO_DET.sub(bind, text)


# An English article goes with the word after it ("the / Data Protection
# Commission" ended a line), also when that word opens a link, and with a
# tied name as long as the whole run stays within 20 characters (R12).
# (and "this"/"these" and a sentence's "We", which ended a line the same way: "Once our company
# is registered, this / independent volunteer board", "Public liability insurance. We / show the
# certificate", a fresh reviewer, v7)
_ARTICLE = re.compile(r"\b(a|an|the|A|An|The|this|This|these|These|We) (?=\S)")
_ARTICLE_END = re.compile(r"\b(a|an|the|A|An|The|this|This|these|These|We) $")
_INLINE_OPEN = re.compile(r"<(a|strong|em|b|i|span)\b")


def _articles(text, before_tag):
    def bind(m):
        run = re.match(r"[^ \t\n\r<]+", text[m.end():])
        if len(m.group(1)) + 1 + len(run.group(0) if run else "") <= 20:
            return m.group(1) + NBSP
        return m.group(0)
    text = _ARTICLE.sub(bind, text)
    if before_tag:
        text = _ARTICLE_END.sub(lambda m: m.group(1) + NBSP, text)
    return text


# Korean: a sentence does not end on one short word alone on a line; its last
# two words stay together when they hold eight syllables or fewer (the leads
# allow ten, _ko_tail; here for every block: answers, steps, values, headings)
# the last word may already be a tied run (「수\u00a0있습니다.」): it is still one word
_KO_LAST = re.compile(r"([^\s<]+) ((?:[^\s<]+\u00a0)*[^\s<]+?[.!?](?:[”’」』)])?)(?=\s|$)")
# nor does a particle start a line after a closing bracket or quote
# (「Down by the Sally Gardens」 / 도)
_KO_CLOSE = re.compile("([」』’”)\\]])(?=[가-힣])")


# the last syllables that close a phrase (a particle or a connecting ending): a
# word ending otherwise is taken for a bare noun
_KO_PHRASE_END = set("이가를의에서와과도만로고며면게지야요께랑나")


def _ko_sentence_ends(text, limit=8, attached=False):
    def bind(m):
        n = len(re.sub(r"[^가-힣A-Za-z0-9]", "", m.group(1) + m.group(2)))
        # the word before may already be tied to the words before it (a
        # highlight kept whole): the whole run must still fit a phone's line
        # (「해 온 강의와 연주, 사진을 모았습니다.」 broke inside at 320px)
        k = m.start(1)
        while k > 0 and m.string[k - 1] not in " \t\n>":
            k -= 1
        run = len(re.sub(r"[^가-힣A-Za-z0-9]", "", m.string[k:m.start(1)]))
        if n + run > limit + 2:
            return m.group(0)
        # nor when the first word is a particle glued to the element before it
        # (「<a>sby05034@gmail.com</a>으로 보내 주세요.」): the tie would hold the
        # whole address with it, wider than a phone's line (v7, 320 and 360px)
        if attached and k == 0:
            return m.group(0)
        # a third word joins a tail of two only if the word before it is neither
        # a modifier (-는 -은 -을 -던) nor a bare noun: the tie would part a noun
        # from its modifier at the line end (「짚는 / 법을 하나씩 익힙니다」,
        # 「좌석 / 고르기도 알려 드립니다」, chief designer v7)
        if "\u00a0" in m.group(2):
            prev = re.split(r"[\s\u00a0>]", m.string[:m.start(1)].rstrip())[-1:] or [""]
            last = prev[0][-1:]
            if last and "\uac00" <= last <= "\ud7a3" and (last in "는은을던" or last not in _KO_PHRASE_END):
                return m.group(0)
        # eight syllables in a heading: one set large on a 320px phone cannot
        # hold a longer tied run; ten in running text, as in the leads (v6:
        # 「공동체 음악가입니다.」 and 「준비를 시작했습니다.」 left one word on a
        # last line once a highlight widened the line before)
        return m.group(1) + (NBSP if n <= limit and re.search("[가-힣]", m.group(2)) else " ") + m.group(2)
    return _KO_LAST.sub(bind, text)


# A highlight (<mark>) sits inside a sentence: tie() must see the words on
# both sides of it as one run, so the tags are masked while it works
_MARK_OPEN, _MARK_CLOSE = "\ue000", "\ue001"


# a highlight short enough to be one tied run (R12: about twenty letters,
# ten Korean syllables) is never split by a line end: the band broken in two
# read as two highlights (v6: 「부활 / 음악회는」)
def _mark_whole(m):
    inner = m.group(2)
    if "<" in inner or " " not in inner:
        return m.group(0)
    text = inner.replace(NBSP, " ")
    ko = len(re.findall("[가-힣]", text))
    short = (ko + len(re.findall("[A-Za-z0-9]", text)) <= 10) if ko else len(text) <= 20
    return m.group(1) + (inner.replace(" ", NBSP) if short else inner) + m.group(3)


_MARK_RUN = re.compile("(<mark>)(.*?)(</mark>)", re.S)


def tie(markup, lang):
    markup = _MARK_RUN.sub(_mark_whole, markup)
    markup = markup.replace("<mark>", _MARK_OPEN).replace("</mark>", _MARK_CLOSE)
    out = _tie(markup, lang)
    return out.replace(_MARK_OPEN, "<mark>").replace(_MARK_CLOSE, "</mark>")


_HEAD_OPEN = re.compile(r"<h[1-6][\s>]")
_HEAD_CLOSE = re.compile(r"</h[1-6]>")


def _tie(markup, lang):
    parts = re.split(r"(<[^>]+>)", markup)
    prev, heading, in_svg = "", False, False
    for i in range(0, len(parts), 2):
        if i:
            tag = parts[i - 1]
            heading = True if _HEAD_OPEN.match(tag) else False if _HEAD_CLOSE.match(tag) else heading
        if i:
            tag = parts[i - 1]
            in_svg = True if tag.startswith("<svg") else False if tag.startswith("</svg") else in_svg
        if not (i and parts[i - 1].startswith('<span class="cm"')):
            parts[i] = _NAMES.sub(_name_nbsp if in_svg else _name_heading if heading else _name_tie, parts[i])
        if lang == "ko" and not (heading or in_svg):
            parts[i] = _NAMES_KO.sub(lambda m: _TN_OPEN + m.group(1).replace(" ", _TN_SP) + _TN_CLOSE, parts[i])
        parts[i] = _PHRASES.sub(_phrase_tie, parts[i])
        before_tag = i + 1 < len(parts) and bool(_INLINE_OPEN.match(parts[i + 1]))
        parts[i] = _articles(parts[i], before_tag)
        for pat in _TIES["en"] + (_TIES["ko"] if lang == "ko" else []):
            parts[i] = pat.sub(lambda m: m.group(1) + NBSP, parts[i])
        if lang == "ko":
            parts[i] = _ko_determiners(parts[i], prev)
            # the dependent noun first (할 수 있습니다), so the sentence's last
            # word is that whole run and the word before can join it
            parts[i] = _ko_dependent(parts[i])
            glued = bool(i and parts[i - 1].startswith("</") and parts[i][:1] not in ("", " ", "\n", "\t"))
            parts[i] = _ko_sentence_ends(parts[i], 8 if heading else 10, glued)
            parts[i] = _KO_CLOSE.sub("\\1\u2060", parts[i])
            parts[i] = _KO_DOT.sub("\u2060·", parts[i])
            # nor does a range part at its tilde (7시 / ~8시, 7시~ / 8시)
            parts[i] = re.sub("(?<=\\S)~(?=\\d)", "\u2060~\u2060", parts[i])
        if _TN_OPEN in parts[i]:
            parts[i] = _TN_BEFORE.sub(lambda m: _TN_OPEN + m.group(1), parts[i])
            parts[i] = _TN_AFTER.sub(lambda m: m.group(1) + _TN_CLOSE, parts[i])
            parts[i] = (parts[i].replace(_TN_OPEN, '<span class="tn">').replace(_TN_CLOSE, "</span>")
                        .replace(_TN_SP, " "))
        text = re.sub(r"<[^>]+>", "", parts[i]).rstrip()
        if text:
            prev = text[-1]
    return "".join(parts)


def page(lang, slug, title, description, body, og_image=None, extra_nodes=(), og_alt=None, og_size=(1800, 1350)):
    """extra_nodes: already-rendered JSON-LD nodes to add to this page's graph
    (a breadcrumb, an event) — see build.py."""
    p, r = _here(slug), _root(lang, slug)
    sub = "" if slug == "index.html" else slug
    # the first photograph is above the fold only when it opens the page:
    # parts.py marks that figure with data-first (the home hero, a page head)
    first = body.find("<img")
    eager = first != -1 and "data-first" in body[:first]
    body = _images(body, eager_first=eager)
    body = _relink(body, p, r)
    # a separator never starts a line: the space before it does not break
    # (QA40-11: Korean keep-all lines began with "·" or "/")
    body = body.replace(" · ", "\u00a0· ").replace(" / ", "\u00a0/ ")
    body = sentence_lines(body, lang)
    body = keep_whole(body, lang)
    body = tie(body, lang)
    canonical = f"{SITE_URL}/" + ("" if lang == "en" else "ko/") + sub
    desc = description.replace('"', "'")
    ld_lang = "en-IE" if lang == "en" else "ko"
    # a page shares its own photograph, not the site-wide hero, so a link to
    # a programme page previews that programme
    image = f"{SITE_URL}/images/{og_image}" if og_image else f"{SITE_URL}/images/hero-outreach.jpg"
    jsonld = _graph([
        ORG_NODE.format(site=SITE_URL, org_desc=ORG_DESC, email=EMAIL, phone=PHONE_INTL),
        SITE_NODE.format(site=SITE_URL),
        PERSON_NODE.format(site=SITE_URL, email=EMAIL,
                           same_as=", ".join(f'"{u}"' for u in SOCIAL.values() if u)),
        *([] if slug == "404.html" else
          [PAGE_NODE.format(site=SITE_URL, canonical=canonical, title=_jtext(title),
                            desc=_jtext(desc), lang=ld_lang, image=image)]),
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
<link rel="icon" href="{r}assets/app-icon-512.png" type="image/png" sizes="512x512">
<link rel="apple-touch-icon" href="{r}assets/apple-touch-icon.png">
<link rel="manifest" href="{r}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS_EN if lang == 'en' and slug != '404.html' else FONTS}">
<link rel="stylesheet" href="{r}styles.css">
<link rel="expect" href="#main" blocking="render">
{jsonld}
</head>
<body onpageshow="{RESET_JS}" onkeydown="{ESC_JS}">
{header(lang, slug)}
<main id="main">
{body}
</main>
{tie(keep_whole(sentence_lines(footer(lang, slug), lang), lang), lang)}
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
