# -*- coding: utf-8 -*-
"""Line icons, drawn once. 24-unit grid, 1.6px stroke, no fill: the same thin
gold line the diagrams use, so an icon reads as part of the same vocabulary
rather than as a sticker. Each is a single glyph for one noun the cards
already name; none is decorative. Rendered inside a .ico disc, aria-hidden,
because the card's own heading carries the meaning."""

import re

_P = {
    # a descant recorder held at an angle: the head narrowing to the beak, its
    # window, the joint, a body tapering to the foot, four finger holes as dots
    # (dots, not rings: rings at the cover's stroke merge into a bead chain)
    # (drawn long, corner to corner, so it carries the same weight as the
    # other emblems on a small cover; the joint is the body's width)
    "recorder": '<g transform="rotate(-45 12 12)"><path d="M10.2 6.54V1.6l.75-3.64h2.1l.75 3.64v4.94"/>'
                '<path d="M11.7 2.12h.6"/><path d="M10.1 6.54h3.8"/><path d="M10.4 6.54l.2 13.26h2.8l.2-13.26"/>'
                '<path d="M10.6 19.8l-1 4.55h4.8l-1-4.55"/>'
                '<path d="M12 9.53h.01M12 12h.01M12 14.47h.01M12 16.94h.01"/></g>',
    # a sheet of music: one quaver on the page (three ruled lines read as a letter)
    "score":    '<rect x="5" y="3" width="14" height="18" rx="1.5"/><circle cx="10.4" cy="15.3" r="1.8"/>'
                '<path d="M12.2 15.3V6.9c1.7.4 2.6 1.4 2.6 3"/>',
    # an arched window: the day room, the chapel, the atrium
    "room":     '<path d="M4.5 21V10.5a7.5 7.5 0 0 1 15 0V21"/><path d="M3 21h18"/><path d="M12 3v18M4.5 13.5h15"/>',
    "road":     '<path d="M4 20.5c1-6 6-7 10-8s6-3 6-8"/><path d="M17 6.5l3-2 .5 3.5"/>',
    "gift":     '<path d="M20 12v8.5H4V12"/><path d="M2.5 7.5h19v4.5h-19z"/><path d="M12 7.5v13"/>'
                '<path d="M12 7.5c-2.5 0-4.5-1.5-4.5-3S9.5 2 12 7.5c2.5-5.5 4.5-3 4.5-1.5s-2 1.5-4.5 1.5"/>',
    "building": '<path d="M3 21h18"/><path d="M5 21V9l7-5 7 5v12"/><path d="M10 21v-6h4v6"/><path d="M9 12h2M13 12h2"/>',
    "door":     '<path d="M5 21V3h9v18"/><path d="M14 5.5l5 1.5v12l-5 1.5"/><circle cx="11.5" cy="12" r=".8"/>',
    "way":      '<path d="M4 12h13"/><path d="M13 7l5 5-5 5"/><path d="M20 4v16"/>',
    "work":     '<rect x="3" y="7.5" width="18" height="12" rx="2"/><path d="M9 7.5V5.5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"/>'
                '<path d="M3 12.5h18"/>',
    "people":   '<circle cx="9" cy="8" r="3"/><path d="M3.5 20a5.5 5.5 0 0 1 11 0"/><circle cx="17" cy="9.5" r="2.5"/>'
                '<path d="M14.5 20a4.5 4.5 0 0 1 6-4.2"/>',
    "mail":     '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 7.5l8.5 6 8.5-6"/>',
    # the programme covers redrawn (illustration desk, 3 Oct 2026; Andrew: 01 a Classical Music class,
    # a teacher teaching; 02 a classical concert in a venue; 04 a string quartet; 05 the ticket one of
    # the set). Drawn in the recorder's hand: one 1.2 stroke on the cover, round caps, no fill; a note
    # head is a small tilted oval the stroke closes into a solid head. "score", "room" and "people"
    # stay for Get involved, each with its one meaning there (R17).
    # 01 a teacher at a board, pointing to two beamed quavers on it: a talk about the music
    "lesson": '<rect x="9.4" y="3" width="12.4" height="10.8" rx="1.2"/>'
              '<path d="M12.89 11.42a.78 .4-24 0 1 1.42-.64 .78 .4-24 0 1-1.42 .64z"/>'
              '<path d="M17.49 10.42a.78 .4-24 0 1 1.42-.64 .78 .4-24 0 1-1.42 .64z"/>'
              '<path d="M14.48 10.9v-4.7l4.6-1v4.7"/><circle cx="5" cy="11" r="2.2"/>'
              '<path d="M1.3 21.8v-1.4a3.8 3.8 0 0 1 7.6 0v1.4"/><path d="M7.9 17l4.6-4.9"/>',
    # 02 a grand piano, lid up on its stick, on the stage boards: a concert (an arch round it read as a bell jar)
    "piano": '<path d="M1.8 19.1h20.4"/><path d="M4.6 10.9h15.5a.9 .9 0 0 1 .9 .9v.4a.9 .9 0 0 1-.9 .9h-15.5z"/>'
             '<path d="M7.4 10.9l13.6-8.2"/><path d="M16.33 10.9l-.5-4.88"/><path d="M5.5 10.9l.7-2.4"/>'
             '<path d="M4.6 12h-1.4"/><path d="M5.8 13.1v6M19.6 13.1v6M9 13.1v3.8"/>',
    # 04 two violins and a cello, scrolls and the cello's spike: the ensemble's strings (f-holes closed up at 1.2)
    "strings": '<path d="M12 6.6c1.86 0 3.04 .74 3.04 2.36c0 1.11-.13 1.73-.25 2.17c-.81 .06-1.24 .55-1.24 1.3'
               'c0 .74 .43 1.3 1.36 1.36c.5 .25 .81 1.37 .81 2.61c0 1.86-1.61 2.6-3.72 2.6'
               'c-2.11 0-3.72-.74-3.72-2.6c0-1.24 .31-2.36 .81-2.61c.93-.06 1.36-.62 1.36-1.36'
               'c0-.75-.43-1.24-1.24-1.3c-.12-.44-.25-1.06-.25-2.17c0-1.62 1.18-2.36 3.04-2.36z"/>'
               '<path d="M12 6.6v-3.75a.85 .85 0 1 1 .85-.85"/><path d="M12 19v1.6"/>'
               '<path d="M3.6 10.2c1.32 0 2.16 .53 2.16 1.67c0 .79-.09 1.23-.18 1.54c-.57 .05-.88 .4-.88 .93'
               'c0 .52 .31 .92 .97 .96c.35 .18 .57 .97 .57 1.85c0 1.32-1.14 1.85-2.64 1.85'
               'c-1.5 0-2.64-.53-2.64-1.85c0-.88 .22-1.67 .57-1.85c.66-.04 .97-.44 .97-.96c0-.53-.31-.88-.88-.93'
               'c-.09-.31-.18-.75-.18-1.54c0-1.14 .84-1.67 2.16-1.67z"/>'
               '<path d="M3.6 10.2v-3.35a.85 .85 0 1 1 .85-.85"/>'
               '<path d="M20.4 10.2c1.32 0 2.16 .53 2.16 1.67c0 .79-.09 1.23-.18 1.54c-.57 .05-.88 .4-.88 .93'
               'c0 .52 .31 .92 .97 .96c.35 .18 .57 .97 .57 1.85c0 1.32-1.14 1.85-2.64 1.85'
               'c-1.5 0-2.64-.53-2.64-1.85c0-.88 .22-1.67 .57-1.85c.66-.04 .97-.44 .97-.96c0-.53-.31-.88-.88-.93'
               'c-.09-.31-.18-.75-.18-1.54c0-1.14 .84-1.67 2.16-1.67z"/>'
               '<path d="M20.4 10.2v-3.35a.85 .85 0 1 1 .85-.85"/>',
    # 05 a ticket, tilted in the hand: notched ends, perforation as holes, the covers' quaver: going to a concert
    "ticket": '<g transform="rotate(-14 12 12)">'
              '<path d="M2.6 7.4a1.6 1.6 0 0 1 1.6-1.6h15.6a1.6 1.6 0 0 1 1.6 1.6v2.1a2.5 2.5 0 0 0 0 5v2.1'
              'a1.6 1.6 0 0 1-1.6 1.6h-15.6a1.6 1.6 0 0 1-1.6-1.6v-2.1a2.5 2.5 0 0 0 0-5z"/>'
              '<path d="M15.6 8.5h.01M15.6 10.83h.01M15.6 13.17h.01M15.6 15.5h.01"/>'
              '<path d="M7.49 14.92a.78 .4-24 0 1 1.42-.64 .78 .4-24 0 1-1.42 .64z"/>'
              '<path d="M9.08 14.4v-5.8c1.5 .35 2.4 1.3 2.4 2.8"/></g>',
    # the drawings on Get involved (art direction, 2 Oct 2026 evening): what a
    # host provides and what we bring, one icon a line
    # a page of a calendar with its two rings and one day marked: a date
    "calendar": '<rect x="3.5" y="5" width="17" height="15.5" rx="2"/><path d="M3.5 9.5h17M8 3v4M16 3v4"/>'
                '<rect x="13" y="13" width="3.5" height="3.5" rx=".6"/>',
    # one person, head and shoulders, drawn like "people": a contact person
    "person":   '<circle cx="12" cy="8" r="3.5"/><path d="M5 20.5a7 7 0 0 1 14 0"/>',
    # a music stand: the desk with its lip, the pole, three feet
    "stand":    '<path d="M4.5 4.5h15l-1 6h-13z"/><path d="M4.5 10.5h15"/><path d="M12 10.5v6.5"/>'
                '<path d="M12 17l-4.5 4M12 17l4.5 4M12 17v4"/>',
    # Contact and Get involved (art direction v3, 2 Oct 2026 night)
    # two speech bubbles, one behind the other: the two languages we answer in
    "speech":   '<path d="M4.2 4.5h9.6a1.7 1.7 0 0 1 1.7 1.7v5.6a1.7 1.7 0 0 1-1.7 1.7H9.2L5.6 16.6v-3.1H4.2'
                'a1.7 1.7 0 0 1-1.7-1.7V6.2a1.7 1.7 0 0 1 1.7-1.7z"/>'
                '<path d="M18.5 9h1.3a1.7 1.7 0 0 1 1.7 1.7v5.6a1.7 1.7 0 0 1-1.7 1.7h-1.4v3l-3.5-3h-4.2'
                'a1.7 1.7 0 0 1-1.7-1.7v-.6"/>',
    # a certificate with its seal: the insurance certificate we show on
    # request (not a shield or a tick, which read as a safety check passed)
    "certificate": '<path d="M13 21H6.5A1.5 1.5 0 0 1 5 19.5v-15A1.5 1.5 0 0 1 6.5 3h11A1.5 1.5 0 0 1 19 4.5V11"/>'
                   '<path d="M8.5 7.5h7M8.5 10.5h4.5"/><circle cx="16.5" cy="15" r="2.7"/>'
                   '<path d="M14.9 17.2 14 21.5l2.5-1.3 2.5 1.3-.9-4.3"/>',
    # a raised open hand: putting a hand up to help (the founding board)
    "hand":     '<path d="M8.6 12.4V5.6a1.4 1.4 0 0 1 2.8 0v5.6"/><path d="M11.4 11.2V4.2a1.4 1.4 0 0 1 2.8 0v7"/>'
                '<path d="M14.2 11.2V5.4a1.4 1.4 0 0 1 2.8 0v6.4"/>'
                '<path d="M17 11.8V8.6a1.4 1.4 0 0 1 2.8 0v5.2c0 4.3-2.9 7.4-6.9 7.4-2.4 0-4.1-1-5.4-2.9l-3.2-4.8'
                'a1.5 1.5 0 0 1 2.4-1.8l1.9 2.3"/>',
    # a megaphone with two arcs of sound: letting local people know
    "announce": '<path d="M3.5 10.5v3a1 1 0 0 0 1 1H7l8 4.5v-15L7 9.5H4.5a1 1 0 0 0-1 1z"/>'
                '<path d="M8 14.5l1.2 4.5h2.2l-1-3.6"/><path d="M18.5 9.8a3.2 3.2 0 0 1 0 4.4M20.6 7.6a6.3 6.3 0 0 1 0 8.8"/>',
}


def glyph(name, cls="cover-mark"):
    """The bare drawing, sized by its container (the programme covers). Each
    stroke is given a path length of 1, so styles.css can draw it in as the
    cover arrives, whatever the stroke's real length."""
    body = re.sub(r"<(path|circle|rect)\b", r'<\1 pathLength="1"', _P[name])
    return (f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
            f'{body}</svg>')


def icon(name):
    return (f'<span class="ico" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false">'
            f'{_P[name]}</svg></span>')
