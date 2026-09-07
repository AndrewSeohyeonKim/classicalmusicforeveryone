#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the Classical Music for Everyone site.

    python3 _build/build.py

Writes the seven English pages to the repository root, the seven Korean pages
to ko/, and regenerates sitemap.xml and robots.txt. Nothing else is touched —
styles.css, assets/ and images/ are hand-maintained.
"""

import os
import re
import sys
from datetime import date
from urllib.parse import urlparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import content_en as en          # noqa: E402
import content_ko as ko          # noqa: E402
import notfound                  # noqa: E402
import prog_en                   # noqa: E402
import prog_ko                   # noqa: E402
import programmes_sub as sub     # noqa: E402
from layout import (ROOT, SITE_URL, EMAIL, SUBNAV, breadcrumb, page, write)   # noqa: E402

PAGES = [
    # slug,               en title,                     en description,
    #                     ko title,                     ko description,
    #                     en body,        ko body
    ("index.html",
     "Classical Music for Everyone — community music in Dublin, Ireland",
     "A Dublin community music social enterprise. We teach people to play, not just listen, "
     "and bring live classical music to care homes, parishes, hospitals and community centres.",
     "Classical Music for Everyone — 아일랜드 더블린의 커뮤니티 음악",
     "더블린의 커뮤니티 음악 사회적기업. 듣는 데서 그치지 않고 직접 연주하도록 가르치고, "
     "요양시설·본당·병원·커뮤니티 센터로 클래식 음악이 찾아갑니다.",
     en.INDEX, ko.INDEX),

    ("about.html",
     "About — Classical Music for Everyone",
     "Our mission, vision and five values; the founder Andrew Seohyeon Kim; and the venues and "
     "institutions we have played in since 2024.",
     "단체 소개 — Classical Music for Everyone",
     "미션과 비전, 다섯 가지 가치, 창립자 김서현, 그리고 2024년 이후 연주해 온 공간과 기관.",
     en.ABOUT, ko.ABOUT),

    ("programmes.html",
     "Programmes — Classical Music for Everyone",
     "Five programmes under two pillars: the Recorder Ensemble course, lecture-recitals, "
     "accompanied concert-going, outreach concerts and the Letters Ensemble.",
     "프로그램 — Classical Music for Everyone",
     "두 축 아래 다섯 개의 프로그램: 리코더 앙상블 과정, 강의·연주, 함께하는 음악여행, "
     "찾아가는 음악회, Letters Ensemble.",
     en.PROGRAMMES, ko.PROGRAMMES),

    ("get-involved.html",
     "Get involved — Classical Music for Everyone",
     "Learn to play, come and listen, play with us, or host a course. Beginners welcome — "
     "no experience assumed and nothing to prepare.",
     "참여하기 — Classical Music for Everyone",
     "연주를 배우거나, 들으러 오거나, 함께 연주하거나, 공간을 여는 네 가지 길. "
     "완전 초보를 환영합니다.",
     en.GET_INVOLVED, ko.GET_INVOLVED),

    ("news.html",
     "What's on — Classical Music for Everyone",
     "A class enrolling, a concert with the door open, what happened in 2026, and press "
     "coverage. The full record since 2023 is on its own page.",
     "일정과 소식 — Classical Music for Everyone",
     "모집 중인 수업, 열려 있는 음악회, 2026년에 있었던 일, 그리고 기사와 기고. "
     "2023년부터의 전체 기록은 별도 페이지에 있습니다.",
     en.NEWS, ko.NEWS),

    ("support.html",
     "Support — Classical Music for Everyone",
     "What support pays for, who has backed the work so far, and four ways to help — "
     "including giving a room or opening a door.",
     "후원 — Classical Music for Everyone",
     "후원이 실제로 쓰이는 곳, 지금까지 이 일을 받쳐 온 이들, 그리고 도울 수 있는 네 가지 방법.",
     en.SUPPORT, ko.SUPPORT),

    ("contact.html",
     "Contact — Classical Music for Everyone",
     "Email, phone and where we travel to. Every enquiry reaches the founder directly.",
     "문의 — Classical Music for Everyone",
     "이메일, 전화, 활동 지역. 모든 문의는 창립자에게 바로 전달됩니다.",
     en.CONTACT, ko.CONTACT),

    ("impact.html",
     "Our impact — Classical Music for Everyone",
     "What has changed because of the work, backed only by the record: dated figures, one "
     "story, where it is going next, and what has not been proved.",
     "성과와 근거 — Classical Music for Everyone",
     "기록이 뒷받침하는 것만 적었습니다. 날짜가 있는 숫자, 이야기 하나, 다음 걸음, "
     "그리고 아직 증명되지 않은 것.",
     en.IMPACT, ko.IMPACT),

    ("archive.html",
     "The record, 2023 to date — Classical Music for Everyone",
     "Every session and performance since February 2023, year by year: lecture-recitals, "
     "outreach concerts, ensemble concerts, courses and outings, with venues and dates.",
     "기록, 2023년부터 — Classical Music for Everyone",
     "2023년 2월 이후의 모든 회차와 연주를 해마다 정리했습니다. 강의·연주, 찾아가는 음악회, "
     "앙상블 음악회, 과정과 동행, 장소와 날짜.",
     en.ARCHIVE, ko.ARCHIVE),

    ("partner.html",
     "Partner with us — Classical Music for Everyone",
     "For care homes, hospitals, parishes, councils, trusts and companies: what a partnership "
     "brings, three ways to partner, what a visit needs, and the questions we are asked most.",
     "기관 파트너십 — Classical Music for Everyone",
     "요양시설·병원·본당·지자체·재단·기업을 위한 안내. 파트너십이 가져다주는 것, 세 가지 "
     "방식, 방문에 필요한 것, 가장 자주 받는 질문.",
     en.PARTNER, ko.PARTNER),

    ("identity.html",
     "The mark — Classical Music for Everyone",
     "The logo and what it commits us to: why the gold falls on Everyone, the colours, the "
     "type, the rules for using the mark, and how to read the diagrams on this site.",
     "상징과 표준 — Classical Music for Everyone",
     "로고와 그것이 약속하는 것. 금색이 Everyone 위에 놓이는 이유, 색, 서체, 로고 사용 규칙, "
     "그리고 이 사이트의 도식을 읽는 법.",
     en.IDENTITY, ko.IDENTITY),
]

# One detail page per programme, under programmes/. The five share a renderer
# (programmes_sub.py) so no one of them can drift into looking like the main
# one; only the prose differs, and it is written natively in each language.
SUB_META = {
    "recorder-ensemble": (
        "Recorder Ensemble course — Classical Music for Everyone",
        "A term of weekly recorder sessions for complete beginners in Dublin, ending in a "
        "concert. Free at Mulhuddart Community Centre from September 2026.",
        "리코더 앙상블 과정 — Classical Music for Everyone",
        "완전 초보를 위한 더블린의 리코더 주간 수업. 마지막은 음악회. "
        "2026년 9월부터 Mulhuddart Community Centre에서 무료로 진행합니다."),
    "getting-to-know": (
        "Getting to Know Classical Music — Classical Music for Everyone",
        "Free lecture-recitals in Dublin for people with no prior knowledge — three stages, "
        "seasonal specials, 17 sessions and 143 attendances so far.",
        "클래식 음악과 친해지기 — Classical Music for Everyone",
        "사전 지식이 없는 분들을 위한 더블린의 무료 강의·연주. 세 단계와 계절 특집, "
        "지금까지 17회에 연 143명이 참석했습니다."),
    "concert-companion": (
        "Concert Guide & Companion — Classical Music for Everyone",
        "Small groups accompanied to live concerts in Dublin and beyond — prepared "
        "beforehand, sat with during, and talked about afterwards.",
        "함께하는 음악여행 — Classical Music for Everyone",
        "혼자서는 가지 않았을 공연에 소그룹으로 함께 갑니다. 미리 준비하고, 옆자리에 앉고, "
        "다녀와서 이야기를 나눕니다."),
    "outreach-concerts": (
        "Outreach Concerts — Classical Music for Everyone",
        "Live classical music brought into care homes, parishes, hospitals and hostels — "
        "20 performances across four countries since 2023.",
        "찾아가는 음악회 — Classical Music for Everyone",
        "요양시설·본당·병원·쉼터로 실황 연주가 찾아갑니다. 2023년 이후 4개국에서 20회를 "
        "연주했습니다."),
    "letters-ensemble": (
        "Letters Ensemble — Classical Music for Everyone",
        "An amateur ensemble in Dublin rehearsing every Saturday since January 2024, "
        "playing in community settings. New amateur players welcome.",
        "Letters Ensemble — Classical Music for Everyone",
        "2024년 1월부터 매주 토요일 연습해 온 더블린의 아마추어 앙상블. 커뮤니티 공간에서 "
        "연주합니다. 새 연주자를 환영합니다."),
}

for _slug in sub.ORDER:
    _en_t, _en_d, _ko_t, _ko_d = SUB_META[_slug]
    PAGES.append((f"programmes/{_slug}.html", _en_t, _en_d, _ko_t, _ko_d,
                  sub.render("en", _slug, prog_en.DATA),
                  sub.render("ko", _slug, prog_ko.DATA)))


# --- structured data beyond the shared graph -------------------------------
#
# Two things are worth declaring per page. Events, because a free class and a
# free concert are exactly what a search engine can surface for someone in
# Dublin who did not know we exist; and breadcrumbs, because the five
# programme pages sit a level down and should say so. Facts here must match
# the page — WHATS_ON in the content files is the same two events.
EVENTS = {
    "en": ["""    {
      "@type": "EducationEvent",
      "@id": "%(site)s/programmes/recorder-ensemble.html#mulhuddart-2026",
      "name": "Recorder Ensemble course — Mulhuddart",
      "description": "A term of weekly recorder sessions for complete beginners. No experience and no music reading assumed.",
      "startDate": "2026-09-09T19:00:00+01:00",
      "endDate": "2026-09-09T20:00:00+01:00",
      "eventSchedule": {
        "@type": "Schedule", "byDay": "https://schema.org/Wednesday",
        "startTime": "19:00", "endTime": "20:00", "repeatFrequency": "P1W",
        "scheduleTimezone": "Europe/Dublin"
      },
      "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
      "eventStatus": "https://schema.org/EventScheduled",
      "location": {
        "@type": "Place", "name": "Mulhuddart Community Centre",
        "address": {"@type": "PostalAddress", "addressLocality": "Dublin 15",
                    "addressCountry": "IE"}
      },
      "organizer": {"@id": "%(site)s/#organisation"},
      "isAccessibleForFree": true,
      "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR",
                 "availability": "https://schema.org/InStock",
                 "url": "%(site)s/get-involved.html"},
      "inLanguage": "en-IE"
    }""",
           """    {
      "@type": "MusicEvent",
      "@id": "%(site)s/news.html#autumn-concert-2026",
      "name": "An Autumn Concert",
      "description": "Soprano, haegeum, clarinet and piano — Chopin, Pierne, Spohr, Schubert and Korean traditional songs.",
      "startDate": "2026-09-19T17:00:00+01:00",
      "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
      "eventStatus": "https://schema.org/EventScheduled",
      "location": {
        "@type": "Place", "name": "Methodist Centenary Church, Ranelagh",
        "address": {"@type": "PostalAddress", "addressLocality": "Dublin 6",
                    "addressCountry": "IE"}
      },
      "organizer": {"@id": "%(site)s/#organisation"},
      "performer": {"@id": "%(site)s/#organisation"},
      "isAccessibleForFree": true,
      "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR",
                 "availability": "https://schema.org/InStock",
                 "url": "%(site)s/news.html"},
      "inLanguage": "en-IE"
    }"""],
}
EVENTS["ko"] = [e.replace('"inLanguage": "en-IE"', '"inLanguage": "ko"') for e in EVENTS["en"]]
EVENT_PAGES = ("index.html", "news.html")

# which photograph each page hands to a social card
OG = {
    "index.html": "hero-outreach.jpg",
    "about.html": "clarinet.jpg",
    "programmes.html": "conducting.jpg",
    "get-involved.html": "community-room.jpg",
    "news.html": "quartet-hall.jpg",
    "support.html": "church-concert.jpg",
    "contact.html": "letters-ensemble.jpg",
    "impact.html": "care-christmas.jpg",
    "archive.html": "church-concert.jpg",
    "partner.html": "quartet-hall.jpg",
    "identity.html": "hero-outreach.jpg",
    "programmes/recorder-ensemble.html": "conducting.jpg",
    "programmes/getting-to-know.html": "lecture-recital.jpg",
    "programmes/concert-companion.html": "quartet-hall.jpg",
    "programmes/outreach-concerts.html": "care-christmas.jpg",
    "programmes/letters-ensemble.html": "letters-ensemble.jpg",
}

CRUMB_ROOT = {"en": "Home", "ko": "홈"}
CRUMB_PROG = {"en": "Programmes", "ko": "프로그램"}
# second-level pages that hang off a first-level one, as the nav says they do
PARENT = {"archive.html": ("news.html", {"en": "What&rsquo;s on", "ko": "일정과 소식"}),
          "partner.html": ("support.html", {"en": "Support", "ko": "후원"}),
          "identity.html": ("about.html", {"en": "About", "ko": "소개"})}

# The questions organisations actually ask (12 §11), answered the same way
# on the page and in the graph so a search engine can show them.
FAQ = {
    "en": [("Can we fund one programme rather than the organisation?",
            "Yes. Name the programme, or the kind of setting, and the support is ring-fenced for it and reported against it."),
           ("Is a gift tax-deductible?",
            "Not yet. Classical Music for Everyone is formalising as a not-for-profit company limited by guarantee and is not a registered charity, so gifts are not eligible for charitable tax relief. We say so plainly rather than let anyone assume otherwise."),
           ("Where would our name appear?",
            "On the printed programme of what you funded, on the Support page of this site, and in the dated report you receive — with your agreement, and nowhere else."),
           ("What does a venue need to provide for a concert?",
            "A room, the people who live or work there, and one named contact. Players, instruments, stands, the programme and insurance arrive with us. There is no stage, no piano and nothing for the audience to pay.")],
    "ko": [("단체 전체가 아니라 프로그램 하나만 후원할 수 있나요?",
            "네. 프로그램이나 공간의 종류를 지정해 주시면 그 후원은 거기에만 쓰고, 거기에 맞춰 보고합니다."),
           ("기부금 세제 혜택이 있나요?",
            "아직 없습니다. Classical Music for Everyone은 비영리 보증유한책임회사로 설립을 준비 중이고 등록 자선단체가 아니어서, 기부금은 세제 혜택 대상이 아닙니다. 오해가 생기기 전에 분명히 적어 둡니다."),
           ("후원사 이름은 어디에 실리나요?",
            "후원하신 연주의 인쇄 프로그램, 이 사이트의 후원 페이지, 그리고 받으시는 보고서에 실립니다. 동의를 받은 뒤에만, 그 밖의 자리에는 싣지 않습니다."),
           ("음악회를 열려면 공간이 무엇을 준비해야 하나요?",
            "방 하나, 거기 살거나 일하는 사람들, 담당자 한 사람입니다. 연주자와 악기, 보면대, 프로그램, 보험은 저희가 가져갑니다. 무대도 피아노도 필요 없고, 관객이 낼 돈도 없습니다.")],
}


def _faq_node(lang):
    items = ",\n".join(
        '        {"@type": "Question", "name": "%s", "acceptedAnswer": {"@type": "Answer", "text": "%s"}}'
        % (q.replace('"', "'").replace("&rsquo;", "’"), a.replace('"', "'"))
        for q, a in FAQ[lang])
    return ('    {\n      "@type": "FAQPage",\n      "@id": "%s/partner.html#faq",\n'
            '      "mainEntity": [\n%s\n      ]\n    }' % (SITE_URL, items))


def _programme_list(lang):
    """The five programmes as one ItemList, in the order they appear everywhere."""
    base = SITE_URL + "/" + ("" if lang == "en" else "ko/")
    items = ",\n".join(
        '        {"@type": "ListItem", "position": %d, "name": "%s", "url": "%s%s"}'
        % (i, t.replace("&amp;", "&"), base, h)
        for i, (h, t, _) in enumerate(SUBNAV["programmes.html"][lang], start=1))
    return ('    {\n      "@type": "ItemList",\n      "@id": "%s/programmes.html#list",\n'
            '      "name": "Programmes",\n      "itemListOrder": "https://schema.org/ItemListUnordered",\n'
            '      "numberOfItems": 5,\n      "itemListElement": [\n%s\n      ]\n    }' % (SITE_URL, items))


def extra_nodes(lang, slug, title):
    """The per-page JSON-LD nodes that hang off the shared graph."""
    nodes = []
    if slug in EVENT_PAGES:
        nodes += [e % {"site": SITE_URL} for e in EVENTS[lang]]
    if slug == "partner.html":
        nodes.append(_faq_node(lang))
    if slug == "programmes.html":
        nodes.append(_programme_list(lang))
    # every interior page says where it sits; the search result shows the trail
    if slug.startswith("programmes/"):
        nodes.append(breadcrumb(SITE_URL, lang, slug, [
            ("", CRUMB_ROOT[lang]),
            ("programmes.html", CRUMB_PROG[lang]),
            (slug, title.split(" — ")[0]),
        ]))
    elif slug in PARENT:
        parent, label = PARENT[slug]
        nodes.append(breadcrumb(SITE_URL, lang, slug, [
            ("", CRUMB_ROOT[lang]), (parent, label[lang]), (slug, title.split(" — ")[0])]))
    elif slug != "index.html":
        nodes.append(breadcrumb(SITE_URL, lang, slug, [
            ("", CRUMB_ROOT[lang]), (slug, title.split(" — ")[0])]))
    return nodes


def build_404():
    """GitHub Pages serves this for any unknown path, at any depth.

    A 404 for /ko/foo/bar is rendered by this file but the browser's base URL is
    still /ko/foo/, so every relative path in it would resolve wrongly. All links
    and assets are therefore rewritten absolute, using the path from SITE_URL —
    which is why previewing 404.html locally needs the same path (see README).
    """
    base = urlparse(SITE_URL).path.rstrip("/") + "/"      # "/classicalmusicforeveryone/"
    html = page("en", "404.html", notfound.TITLE, notfound.DESC, notfound.BODY)
    # every path in the shell and body is relative and correct for a page at
    # the root; rewrite all of them absolute so the file also works when the
    # browser thinks it is at /ko/whatever/ — which is the whole point of a 404
    html = re.sub(r'\b(href|src)="(?!https?:|mailto:|tel:|data:|#|/)',
                  lambda m: f'{m.group(1)}="{base}', html)
    # there is no Korean 404 — send the language switch to the Korean home
    html = html.replace(f'href="{base}ko/404.html"', f'href="{base}ko/"')
    # a 404 is not a page to index, and it has no language twin
    html = re.sub(r'<link rel="(canonical|alternate)"[^>]*>\n', "", html)
    html = html.replace("<title>", '<meta name="robots" content="noindex">\n<title>')
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as fh:
        fh.write(html)


def build_sitemap():
    today = date.today().isoformat()
    urls = []
    for slug, *_ in PAGES:
        for lang in ("en", "ko"):
            loc = f"{SITE_URL}/" + ("" if lang == "en" else "ko/")
            loc += "" if slug == "index.html" else slug
            alt_en = f"{SITE_URL}/" + ("" if slug == "index.html" else slug)
            alt_ko = f"{SITE_URL}/ko/" + ("" if slug == "index.html" else slug)
            priority = "1.0" if slug == "index.html" else "0.8"
            urls.append(
                "  <url>\n"
                f"    <loc>{loc}</loc>\n"
                f"    <lastmod>{today}</lastmod>\n"
                f"    <priority>{priority}</priority>\n"
                f'    <xhtml:link rel="alternate" hreflang="en" href="{alt_en}"/>\n'
                f'    <xhtml:link rel="alternate" hreflang="ko" href="{alt_ko}"/>\n'
                "  </url>"
            )
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + "\n".join(urls) + "\n</urlset>\n")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write(xml)

    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write(f"User-agent: *\nAllow: /\nDisallow: /_build/\n\nSitemap: {SITE_URL}/sitemap.xml\n")


def build_llms():
    """A plain-text summary at /llms.txt for AI assistants and answer engines —
    the same canonical one-line and short descriptions (01 §2), plus a map
    of the pages. Facts only; nothing here that is not on the site."""
    lines = ["# Classical Music for Everyone", "",
             "> Classical Music for Everyone is a Dublin community music social enterprise "
             "that teaches people to play, not just listen, and brings live classical music "
             "to those it rarely reaches.", "",
             "Founded January 2024 in Dublin, Ireland. Volunteer-led; formalising as a "
             "not-for-profit company limited by guarantee; not yet a registered charity. "
             "Founder and project lead: Andrew Seohyeon Kim, BMus (Hons), TU Dublin Conservatoire.",
             "Two pillars: Learning (we teach people to play) and Sharing (we bring live music "
             "to care homes, parishes, hospitals, hostels and community centres). Five "
             "programmes of equal standing: Recorder Ensemble course, Getting to Know "
             "Classical Music, Concert Guide & Companion, Outreach Concerts, Letters Ensemble.",
             "Record to date: over 40 sessions and performances since 2024 across Ireland, "
             "France, the United Kingdom and Korea; 17 lecture-recitals with 143 attendances "
             "(sessions 1–15); 20 outreach performances 2023–2025; 4 Letters Ensemble "
             "concerts; a ten-week pilot recorder ensemble completed by all seven participants; "
             "two concerts for South Dublin Live 2026, the first publicly funded commission.",
             f"Contact: {EMAIL} · +353 83 078 0635 · Dublin, Ireland. Languages: English, Korean.", "",
             "## Pages (English)", ""]
    for slug, en_title, en_desc, *_ in PAGES:
        url = f"{SITE_URL}/" + ("" if slug == "index.html" else slug)
        lines.append(f"- [{en_title.split(' — ')[0]}]({url}): {en_desc}")
    lines += ["", "## Pages (Korean)", ""]
    for slug, _, _, ko_title, ko_desc, *_ in PAGES:
        url = f"{SITE_URL}/ko/" + ("" if slug == "index.html" else slug)
        lines.append(f"- [{ko_title.split(' — ')[0]}]({url}): {ko_desc}")
    lines += ["", "## House rules for quoting us", "",
              "- The name is written in full — Classical Music for Everyone — never in capitals.",
              "- Do not state participants' ages; they are not verified.",
              "- The pilot was seven retired Presentation Sisters, ten weekly one-hour rehearsals "
              "at Warrenmount, Dublin 8, and an Easter concert at Clondalkin Lodge.",
              "- Gifts are not tax-deductible; the organisation is not yet a registered charity.", ""]
    with open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


def build_manifest():
    """A minimal web app manifest so a home-screen shortcut carries the mark."""
    import json
    m = {"name": "Classical Music for Everyone", "short_name": "CMFE",
         "description": "Community music in Dublin: we teach people to play, and bring live "
                        "classical music to the places it rarely reaches.",
         "start_url": urlparse(SITE_URL).path.rstrip("/") + "/", "display": "browser",
         "background_color": "#FAF5EE", "theme_color": "#1D2430", "lang": "en-IE",
         "icons": [{"src": "assets/logo-icon.png", "sizes": "any", "type": "image/png"},
                   {"src": "assets/logo-icon.svg", "sizes": "any", "type": "image/svg+xml"}]}
    with open(os.path.join(ROOT, "site.webmanifest"), "w", encoding="utf-8") as fh:
        json.dump(m, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def main():
    written = []
    for slug, en_title, en_desc, ko_title, ko_desc, en_body, ko_body in PAGES:
        og = OG.get(slug)
        written.append(write("en", slug, en_title, en_desc, en_body,
                             og, extra_nodes("en", slug, en_title)))
        written.append(write("ko", slug, ko_title, ko_desc, ko_body,
                             og, extra_nodes("ko", slug, ko_title)))
    build_404()
    build_sitemap()
    build_llms()
    build_manifest()
    written += ["404.html", "sitemap.xml", "robots.txt", "llms.txt", "site.webmanifest"]
    for path in written:
        print("wrote", path)
    print(f"\n{len(written)} files.")


if __name__ == "__main__":
    main()
