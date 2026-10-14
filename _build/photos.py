"""Who is in each published photograph, and why it may be shown (Andrew, 14 October 2026).

Every file in images/ is public by its address, used or not, so the build checks this folder
against the register below (build.check_photos):
  - every photograph in images/ is listed here, with the reason it may be shown;
  - every listed photograph is used by a page (an unused file is still public: retire it);
  - no withdrawn name comes back.

The reasons:
  founder  the founder alone (or the founder's hands and view)
  sdcc     South Dublin Live performers, and the photographs by Ben Ryan for South Dublin County
           Council and by Tallaght University Hospital: consent and permission on record
  blurred  players who have not given consent, their faces softly blurred before publishing
           (_build/face-blur.swift, then _build/add-photo.sh on the blurred file)
  nobody   instruments and empty rooms
  crowd    a distant audience in which no one can be picked out

A new photograph of anyone else needs written consent first, or a blurred face.
"""

PHOTOS = {
    # the founder, and SDCC performers who gave consent
    "ruared-duo": ("sdcc", "clarinet and piano on the Rua Red stage, Aug 2026 (home hero)"),
    "ruared-back": ("sdcc", "the founder from behind, playing towards the soprano, Aug 2026"),
    "ruared-trio": ("sdcc", "the trio taking a bow at Rua Red, Aug 2026"),
    "tuh-trio": ("sdcc", "soprano, piano and clarinet in the TUH atrium, Aug 2026"),
    "tuh-atrium": ("sdcc", "clarinet, haegeum and keyboard in the TUH chapel, Aug 2026"),
    "tuh-haegeum": ("sdcc", "the haegeum player in the TUH atrium, Aug 2026"),
    "founder-playing": ("founder", "clarinet in the TUH chapel, Aug 2026, photo TUH"),
    "goirtin-solo": ("founder", "clarinet solo at a day service, Dublin 7, Apr 2025; the one listener "
                                "at the left edge is cropped out"),
    "lecture-recital": ("founder", "a talk on the BBC Proms; the slide shows a press photograph"),
    "church-aisle": ("founder", "the founder's hand and clarinet before the altar, Dysart, Apr 2025"),
    # players without consent: faces softly blurred
    "christmas-conducting": ("blurred", "the founder conducting; the violinist and violist blurred, "
                                        "Clondalkin Lodge, Dec 2025"),
    "letters-stpatricks": ("blurred", "the founder conducting; the four string players blurred, "
                                      "St Patrick's Day concert"),
    "rehearsal-stand": ("blurred", "the founder's view over the stand; the violist and the violinist "
                                   "at the left edge blurred (the cellist's face is behind a hand)"),
    # no one, or no one who can be picked out
    "recorders": ("nobody", "six recorders, Nov 2025"),
    "dalgan-hall": ("nobody", "the hall before the concert, Dalgan Park, Mar 2024"),
    "two-clarinets": ("nobody", "two clarinets on a piano"),
    "proms-hall": ("crowd", "the Royal Albert Hall from high in the audience, Sep 2023"),
}

# Photographs of Letters Ensemble players, without consent and unblurred, published until
# 14 October 2026. Their names never come back (a new file under an old name would be
# served to anyone who kept the old address).
WITHDRAWN = {"hero-outreach", "columban-ensemble", "letters-ensemble", "care-christmas", "score-stand"}
