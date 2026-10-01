# -*- coding: utf-8 -*-
"""Line icons, drawn once. 24-unit grid, 1.6px stroke, no fill: the same thin
gold line the diagrams use, so an icon reads as part of the same vocabulary
rather than as a sticker. Each is a single glyph for one noun the cards
already name; none is decorative. Rendered inside a .ico disc, aria-hidden,
because the card's own heading carries the meaning."""

import re

_P = {
    "recorder": '<path d="M12 2.5v19"/><path d="M9.5 2.5h5"/><circle cx="12" cy="8" r="1"/>'
                '<circle cx="12" cy="12" r="1"/><circle cx="12" cy="16" r="1"/>',
    "score":    '<rect x="5" y="3" width="14" height="18" rx="1.5"/><path d="M8.5 8h7M8.5 12h7M8.5 16h4"/>',
    "room":     '<path d="M4.5 21V10.5a7.5 7.5 0 0 1 15 0V21"/><path d="M3 21h18"/><path d="M9.5 21v-5h5v5"/>',
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
    # a ticket with notched ends and its perforation: going to a concert
    "ticket":   '<path d="M3 7.5A1.5 1.5 0 0 1 4.5 6h15A1.5 1.5 0 0 1 21 7.5v2a2.5 2.5 0 0 0 0 5v2a1.5 1.5 0 0 1-1.5 1.5'
                'h-15A1.5 1.5 0 0 1 3 16.5v-2a2.5 2.5 0 0 0 0-5z"/><path d="M15.5 6.5v2M15.5 11v2M15.5 15.5v2"/>',
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
