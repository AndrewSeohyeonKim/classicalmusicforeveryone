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
from layout import (ROOT, SITE_URL, breadcrumb, page, write)   # noqa: E402

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
     "News & record — Classical Music for Everyone",
     "Upcoming concerts and classes, what happened in 2026, and the milestones since 2023.",
     "소식과 기록 — Classical Music for Everyone",
     "다가오는 연주와 수업, 2026년에 있었던 일, 그리고 2023년부터의 기록.",
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
        "요양시설·본당·병원·쉼터로 실연이 찾아갑니다. 2023년 이후 4개국에서 20회를 "
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
    "programmes/recorder-ensemble.html": "conducting.jpg",
    "programmes/getting-to-know.html": "lecture-recital.jpg",
    "programmes/concert-companion.html": "quartet-hall.jpg",
    "programmes/outreach-concerts.html": "care-christmas.jpg",
    "programmes/letters-ensemble.html": "letters-ensemble.jpg",
}

CRUMB_ROOT = {"en": "Home", "ko": "홈"}
CRUMB_PROG = {"en": "Programmes", "ko": "프로그램"}


def extra_nodes(lang, slug, title):
    """The per-page JSON-LD nodes that hang off the shared graph."""
    nodes = []
    if slug in EVENT_PAGES:
        nodes += [e % {"site": SITE_URL} for e in EVENTS[lang]]
    if slug.startswith("programmes/"):
        nodes.append(breadcrumb(SITE_URL, lang, slug, [
            ("", CRUMB_ROOT[lang]),
            ("programmes.html", CRUMB_PROG[lang]),
            (slug, title.split(" — ")[0]),
        ]))
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
        fh.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")


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
    written += ["404.html", "sitemap.xml", "robots.txt"]
    for path in written:
        print("wrote", path)
    print(f"\n{len(written)} files.")


if __name__ == "__main__":
    main()
