#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the Classical Music for Everyone site.

    python3 _build/build.py

Writes the seven English pages to the repository root, the seven Korean pages
to ko/, and regenerates sitemap.xml and robots.txt. Nothing else is touched —
styles.css, assets/ and images/ are hand-maintained.
"""

import os
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import content_en as en          # noqa: E402
import content_ko as ko          # noqa: E402
from layout import ROOT, SITE_URL, write   # noqa: E402

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
        written.append(write("en", slug, en_title, en_desc, en_body))
        written.append(write("ko", slug, ko_title, ko_desc, ko_body))
    build_sitemap()
    written += ["sitemap.xml", "robots.txt"]
    for path in written:
        print("wrote", path)
    print(f"\n{len(written)} files.")


if __name__ == "__main__":
    main()
