# -*- coding: utf-8 -*-
"""English copy for the six pages.

Since 2026-10-01 this file is a copy deck and nothing else: the markup lives
in parts.py, shared with the Korean deck, so the two languages cannot drift
apart in structure.

What goes in, and what does not (2026-10-01): the public site says what
Classical Music for Everyone does now, how to take part now, and what a
visitor needs to trust it. Plans that are not yet happening, and internal
matters, stay out. Facts follow the canonical set (00_최종본) and the
integrated master kit (11_CMFE_통합마스터); a sentence taken from the kit
says which document it comes from.
"""

from urllib.parse import quote

import parts as P
from icons import icon as _ico
from layout import OPEN_GIVING

L = "en"
EMAIL = "sby05034@gmail.com"

# The status sentence (kit 27), word for word wherever the site says what we are.
STATUS = ('<span class="brandname">Classical Music for Everyone</span> is a not-for-profit community '
          "music initiative, forming a company limited by guarantee. It is not yet a registered "
          "charity.")


def _mail(subject, body=""):
    """A mailto link with a subject and, optionally, a pre-filled body."""
    href = f"mailto:{EMAIL}?subject={quote(subject)}"
    if body:
        href += "&amp;body=" + quote(body)
    return href


_MAIL_INVITE = _mail("Inviting Classical Music for Everyone",
                     "Organisation: \nWhere: \nThe room and a possible date: \n")
_MAIL_BOARD = _mail("Founding board: Classical Music for Everyone",
                    "The role that interests me (Chair / Treasurer / Secretary / "
                    "Safeguarding and care / Community): \nA few lines about me: \n")

# CMFE Artists expression of interest (kit 15). The fields are the kit's,
# less the signature line and the right-to-work line: an email needs no
# signature, and the right to work is confirmed at engagement (kit 06 I).
EOI_FIELDS = [
    "Name",
    "Instrument(s) or voice",
    "Stage: professional / student (institution, year) / emerging / amateur ensemble",
    "County you are based in",
    "Days and times usually available",
    "Repertoire you could play in a 45-minute programme for older listeners",
    "Experience in care homes, hospitals, libraries or community settings (if any)",
    "Link to a recent recording (YouTube, Vimeo or SoundCloud)",
    "Garda vetting: current (through which organisation) / I would need vetting",
    "Access needs we should know about (optional)",
    "What you would like to get from CMFE Artists (one or two lines)",
]
_MAIL_EOI = _mail("CMFE Artists: expression of interest",
                  "".join(f"{f}: \n" for f in EOI_FIELDS)
                  + "\nI agree that you may keep these details for up to two years to offer me "
                    "engagements.\n")


# ---------------------------------------------------------------------------
# The five programmes. One list, read by the home cards, the Programmes page
# and the structured data, so none of them can drift. Same fields, same
# order, no main one (CLAUDE.md §2.1). Each programme has one photograph and
# uses it everywhere it appears.
# ---------------------------------------------------------------------------

PILLARS = {"learn": ("Learning", "dot"), "share": ("Sharing", "dot dot-open")}

# Photographs that appear in more than one place keep one description.
# care-christmas: one clarinettist and three string players (08 §3, 20 Dec 2025).
# tuh-atrium: despite the file name, the chapel set, with its cross and lectern.
CARE_ALT = "A clarinettist and three string players performing in a care setting at Christmas"
TUH_CHAPEL_ALT = "Clarinet, haegeum and keyboard in the chapel of Tallaght University Hospital"
RECORDERS_ALT = "Six recorders of different sizes standing in a row"

PROGRAMMES_DATA = [
    dict(slug="getting-to-know", pillar="learn", name="Getting to Know Classical Music",
         short="Getting to Know",
         img=("lecture-recital.jpg", 1050, 1400, "A lecture-recital in progress"),
         line="Classical music talks for adults and older people.",
         who="Adults and older people who like the sound of classical music and never knew where "
             "to start. No prior knowledge needed.",
         # kit 02 §4: a three-stage curriculum, not a talk per composer
         what="Talk, recordings and live playing, in three stages: getting closer, experiencing "
              "together and finding your own taste. Usually six to fourteen people.",
         # no date is fixed (Andrew, 1 Oct 2026), so a talk is offered on request
         where="Dublin &middot; free &middot; on request",
         how="Email us to ask about a talk. Libraries, parishes and groups can book one.",
         btn="Ask about a talk", mail=_mail("Getting to Know Classical Music")),
    dict(slug="outreach-concerts", pillar="share", name="Outreach Concerts",
         short="Outreach Concerts",
         img=("care-christmas.jpg", 1400, 1050, CARE_ALT),
         line="Live music in care homes, hospitals, religious houses and community settings.",
         who="People who cannot easily get to a concert hall, and the places that care for them.",
         what="Thirty to sixty minutes of acoustic music in the day room, chapel or atrium. Nothing "
              "for the audience to pay.",
         where="Dublin, Co. Meath, Co. Wicklow, Co. Westmeath, and further by arrangement",
         how="Tell us your room and a date. We bring the players, instruments and stands.",
         btn="Invite a concert", mail=_mail("Inviting an outreach concert")),
    dict(slug="recorder-ensemble", pillar="learn", name="Free Recorder Ensemble course",
         short="Recorder Ensemble",
         img=("recorders.jpg", 1343, 1400, RECORDERS_ALT),
         line="A free course for adults who have never played, ending in a concert.",
         who="Adults who have never played an instrument. No music reading needed.",
         # no class size and no instrument price in public copy (06 §6, 02 §2)
         what="A small group in a circle: a first sound in week one, your own part in the "
              "ensemble, and a short concert for family and friends.",
         where="Mulhuddart Community Centre, Dublin 15 &middot; Wednesday evenings, 7:00&ndash;8:00pm "
               "&middot; free",
         how="Email us and we will tell you how to join. We can lend you a recorder.",
         btn="Ask about the course", mail=_mail("Recorder Ensemble course")),
    dict(slug="letters-ensemble", pillar="share", name="Letters Ensemble",
         short="Letters Ensemble",
         img=("letters-ensemble.jpg", 1400, 1050, "The Letters Ensemble with their instruments"),
         line="Our ensemble of Dublin-based musicians, formed in January 2024.",
         who="Amateur players of strings, winds and more.",
         what="Irish and Korean traditional music, sacred music and accessible arrangements, played "
              "in community settings.",
         where="Dublin &middot; since January 2024",
         # still recruiting (Andrew, 1 Oct 2026)
         how="New players are welcome. Email us with your instrument.",
         btn="Ask about joining", mail=_mail("Joining the Letters Ensemble")),
    dict(slug="concert-companion", pillar="learn", name="Concert Guide &amp; Companion",
         short="Concert Guide &amp; Companion",
         img=("dalgan-hall.jpg", 1400, 1050,
              "A hall set out with chairs and music stands before a concert, with no one there yet"),
         line="Going to concerts together, in small groups.",
         who="People who would not go to a concert on their own, including people new to Ireland.",
         what="Groups of about five. We prepare beforehand, sit together during, and talk it over "
              "after.",
         # 08 §2 and the ledger: the outings on record are in Dublin
         where="Dublin &middot; concerts such as the National Symphony Orchestra, the RT&Eacute; "
               "Concert Orchestra and the NCH International Series",
         how="Email us and we will tell you when there is an outing to join.",
         btn="Ask about an outing", mail=_mail("Concert Guide & Companion")),
]


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------

HOME = dict(
    hero=dict(
        eyebrow="Community music · Dublin, Ireland",
        title=["Classical music,", '<span class="for">for </span><em>Everyone.</em>'],
        master="Bringing classical music where it&rsquo;s needed!",
        # kit 27: the 25-word version, then how we work
        lead='<span class="brandname">Classical Music for Everyone</span> brings live classical music, '
             "talks and a free recorder ensemble to older people, migrant communities and care "
             "settings in Dublin. We explain the music as we go, and we invite people to play as "
             "well as listen.",
        # one action on the first screen; the three ways in follow under it
        cta=("get-involved.html", "Get involved"),
        more=("#programmes", "See what we do"),
        img=("hero-outreach.jpg", 1800, 1350,
             "The Letters Ensemble and their conductor playing a St Patrick&rsquo;s Day concert in a hall"),
        cap=("Letters Ensemble", "St Patrick&rsquo;s Day concert"),
    ),
    strip_label="Three ways in",
    strip=[
        ("get-involved.html#invite", "Venues", "Bring a concert to your place",
         "Care homes, hospitals, libraries and parishes: tell us your room and a date.",
         "Invite us", False),
        ("get-involved.html#play", "Musicians", "Perform with us",
         "From 2027 we plan paid, mentored performances. Expressions of interest are open now.",
         "CMFE Artists", False),
        ("get-involved.html#board", "Volunteers", "Help us build it",
         "We are forming our first board: five volunteer roles.", "The roles", True),
    ],
    progs=dict(
        label="What we do",
        h2="Five programmes.",
        lead="Three help people listen and play. Two take live music out to the places where "
             "people already are.",
        # kit 27, message 3: a plan, said as a plan, with the one thing open now
        artists='From 2027 we plan paid, mentored performances for emerging musicians, as CMFE '
                'Artists. <a class="link" href="get-involved.html#play">Expressions of interest are '
                "open now</a>.",
    ),
    why=dict(
        label="Why we exist",
        # kit 27 ①, the opening of the one-page case
        text="Many people in Dublin never get to a concert. Some live in a nursing home or rarely "
             "leave the house. Some are new to Ireland and don&rsquo;t know where to begin. So we "
             "go to them.",
        link="About us",
    ),
    numbers=dict(
        label="On the record",
        sr="In numbers",
        figs=[(40, "sessions and performances", "since 2023", True),
              (5, "programmes, in Learning and Sharing", "as of October 2026", False),
              (4, "countries: Ireland, France, the UK and Korea", "2023 – 2025", False)],
        # kit 27: a selection of the founder, said as such
        note="In 2026 South Dublin County Council&rsquo;s Arts Office selected our founder for South "
             'Dublin Live. <a class="link" href="news.html#record">See the record, month by month</a>',
    ),
    bleed=dict(
        img=("tuh-atrium.jpg", 1400, 1052, TUH_CHAPEL_ALT),
        cap=("Tallaght University Hospital", "August 2026 · photo: Tallaght University Hospital"),
    ),
    now=dict(
        img=("recorders.jpg", 1343, 1400, RECORDERS_ALT),
        label="Now running",
        tag="Wednesday evenings",
        h2="Free Recorder Ensemble course",
        facts=[("Where", "Mulhuddart Community Centre, Dublin 15"),
               ("When", "Wednesday evenings, 7:00&ndash;8:00pm"),
               ("Cost", "Free. We can lend you a recorder")],
        href="programmes.html#recorder-ensemble",
        btn="About the course",
    ),
)


# ---------------------------------------------------------------------------
# ABOUT. The anchors #founder #run #places #identity are redirect targets.
# ---------------------------------------------------------------------------

ABOUT_T = dict(
    head=dict(
        eyebrow="About us",
        title=["Why we exist."],
        # kit 27, positioning: who, and how
        lead="We bring live classical music to people who rarely get to hear it: older people, "
             "migrant communities and people in care settings around Dublin. We go to the rooms "
             "where they already are.",
        img=("columban-ensemble.jpg", 1400, 1050,
             "Four string players of the Letters Ensemble and their conductor in a bright yellow room"),
        cap=("Missionary Sisters of St Columban, Co. Wicklow", "November 2024"),
    ),
    glance=[("Founded", "January 2024", "Dublin, Ireland"),
            ("What we run", "Five programmes", "in Learning and Sharing"),
            ("Where we have played", "Four countries", "Ireland, France, the UK, Korea"),
            ("Status", "Not-for-profit", "Forming a company limited by guarantee. Not yet a "
                                         "registered charity.")],
    story=dict(
        label="Our story",
        h2="Since 2023.",
        # 08 §2: no group trip to the Proms is on the record
        text=["It began in 2023, with a clarinet solo in Lourdes and a summer in the audience at the "
              "BBC Proms in London. In January 2024 Andrew Seohyeon Kim founded "
              '<span class="brandname">Classical Music for Everyone</span> and the Letters Ensemble '
              "in Dublin; six people came to the first talk.",
              "By August 2026 there were forty recorded talks and performances, in care homes, "
              "religious communities, parishes, a hospital, a homeless hostel and community centres. "
              "In 2026 a pilot recorder ensemble with seven retired Presentation Sisters led to a free "
              "course at Mulhuddart, and South Dublin County Council&rsquo;s Arts Office selected our "
              "founder for South Dublin Live 2026."],
        link="The full timeline",
    ),
    founder=dict(
        img=("founder-speaking.jpg", 1050, 1400,
             "Andrew Seohyeon Kim speaking at a lecture-recital with a microphone"),
        label="The founder",
        name="Andrew Seohyeon Kim",
        role="Founder &amp; Artistic Director",
        text="Andrew is a clarinettist, organist and community musician in Dublin. He holds a BMus "
             "(Hons) in Performance from TU Dublin Conservatoire and is Music Director at Our Lady of "
             "Dolours, Dolphin&rsquo;s Barn. His final-year research was a ten-week recorder ensemble "
             "with seven retired Presentation Sisters at Warrenmount, Dublin 8. All seven completed "
             "and played in public.",
    ),
    run=dict(
        label="How we are run",
        h2="A not-for-profit initiative.",
        # kit 27: the status sentence, exactly as written
        lead=STATUS,
        cols=[("Who decides", "Once the company is registered, an independent volunteer board will "
                              "govern it. We are recruiting its first members now: a chair, a "
                              "treasurer, a secretary, and leads for safeguarding and care, and for "
                              "the community."),
              ("Money", "We are not asking for or accepting gifts yet. No one acting for us will ask "
                        "you to pay into a personal account."),
              ("Photographs and stories", "We show performers, instruments and empty rooms. Anyone "
                                          "else who can be recognised appears only with their written "
                                          "consent. Our approach draws on the D&oacute;chas Guide to "
                                          "Ethical Communications (2023).")],
        links=[("get-involved.html#board", "Join the founding board"),
               ("contact.html#privacy", "How we handle your details")],
    ),
    places=dict(
        label="Places",
        h2="Where we have played and taught.",
        # 08 §2: concerts introduced to participants, with group attendance organised
        lead="We have also introduced participants to concerts at the National Concert Hall and "
             "organised group attendance.",
        names=["Tallaght University Hospital", "Rua Red, Tallaght", "Clondalkin Lodge",
               "Warrenmount, Dublin 8", "Mulhuddart Community Centre",
               "Missionary Sisters of St Columban, Co. Wicklow", "Dalgan Park, Co. Meath",
               "Dysart Parish, Co. Westmeath", "HSE EVE Goirtin Hub", "Morning Star Hostel",
               "TU Dublin", "Our Lady of Dolours, Dolphin&rsquo;s Barn",
               "Church of the Three Patrons, Rathgar", "Missions &Eacute;trang&egrave;res de Paris",
               "London Korean Catholic Church", "Gwandukjeong Martyrs Memorial Centre, Daegu"],
    ),
    identity=dict(
        label="The name",
        h2="Why <em>Everyone</em> is in gold",
        text="In the mark, &ldquo;for&rdquo; is small and &ldquo;Everyone&rdquo; is large and gold. "
             "The last word of the name is the one we have to live up to.",
        alt="The Classical Music for Everyone mark: a treble clef beside the wordmark, with "
            "&lsquo;Everyone&rsquo; set large and in gold",
    ),
)


# ---------------------------------------------------------------------------
# PROGRAMMES
# ---------------------------------------------------------------------------

PROGRAMMES_T = dict(
    head=dict(
        eyebrow="Programmes",
        title=["Our programmes."],
        lead="Talks, concerts where people live, a free class, an ensemble, and company at the "
             "concert hall.",
        img=("tuh-trio.jpg", 1400, 787,
             "Soprano, piano and clarinet in the atrium of Tallaght University Hospital"),
        cap=("Tallaght University Hospital", "August 2026 · photo: Tallaght University Hospital"),
    ),
    toc_label="The five programmes",
    fact_labels=("For", "What happens", "Where and when", "How to join"),
    artists=dict(
        img=("ruared-trio.jpg", 1400, 933, "Clarinet, soprano and piano taking a bow on the Rua Red stage"),
        cap=("Rua Red, Tallaght", "South Dublin Live 2026 · photo: Ben Ryan / SDCC"),
        label="From 2027",
        lead="We plan paid, mentored performances for emerging musicians, in care homes, hospitals, "
             "libraries and community settings.",
        facts=[("For", "Student, emerging, amateur and Korean musicians, alongside professional "
                       "players."),
               ("How it will work", "Professional, student and emerging players will be paid, in "
                                    "line with the Arts Council&rsquo;s Paying the Artist policy; "
                                    "amateur players will receive expenses. Student and emerging "
                                    "players will go with a mentor on their first visits."),
               ("Now", "Expressions of interest are open. We plan to open the first call, with "
                       "its selection criteria, in 2027.")],
        btn="Tell us about yourself",
    ),
)


# ---------------------------------------------------------------------------
# GET INVOLVED. Anchors: #invite (old Partner page), #play (CMFE Artists),
# #support and #board (old Support page), #join. #friends and #sponsor exist
# only while giving is open (layout.OPEN_GIVING).
# ---------------------------------------------------------------------------

GET_INVOLVED_T = dict(
    head=dict(
        eyebrow="Get involved",
        title=["Ways to get involved."],
        lead="Bring a concert to your place, tell us you would like to perform, or join the "
             "founding board. One line by email is enough to start.",
        img=("church-aisle.jpg", 1050, 1400,
             "A clarinet held up before the altar of a parish church in Co. Westmeath"),
        cap=("Dysart, Co. Westmeath", "2025"),
    ),
    ways=[("invite", "Bring a concert to your place", "Care homes, hospitals, parishes, community centres"),
          ("play", "Perform with us", "CMFE Artists, for musicians, planned for 2027"),
          ("board", "Join the founding board", "Five volunteer roles")],
    invite=dict(
        label="Partner venues",
        h2="Bring a concert to your place.",
        # kit 02 §2 and 29: what a host gives, and what we can promise
        text="Care homes, hospitals, libraries, parishes and community centres. Tell us your room "
             "and a date, and we bring the players, instruments, stands and programme. A community "
             "centre can also host a free beginners&rsquo; course: you give a warm room once a week, "
             "a contact and help letting local people know, and we bring the rest as funding allows.",
        href=_MAIL_INVITE, btn="Invite us",
        img=("care-christmas.jpg", 1400, 1050, CARE_ALT),
        cap=("Outreach concert", "Christmas"),
    ),
    play=dict(
        label="CMFE Artists",
        h2="Perform with us.",
        lead="For student, emerging, amateur and Korean musicians, and professional players who "
             "want to play where music is needed. We plan to begin CMFE Artists in 2027; tell us "
             "about yourself now and we will write when the first call opens. Amateur players can "
             'join the <a class="link" href="programmes.html#letters-ensemble">Letters Ensemble</a> now.',
        sub="What to send us",
        fields=EOI_FIELDS,
        note="Professional, student and emerging players will be paid; amateur players will receive "
             "expenses. We keep your details for up to two years to offer you engagements, and delete "
             "them whenever you ask.",
        href=_MAIL_EOI, btn="Send an expression of interest",
    ),
    support=dict(
        label="Help us build it",
        board=dict(
            h2="Join the founding board.",
            lead="We are recruiting the first members of an independent volunteer board.",
            facts=[("Roles", "Chair, treasurer, secretary, safeguarding and care lead, community "
                             "director"),
                   ("Time", "About six meetings a year, and three to four hours a month"),
                   ("Conditions", "Unpaid, with reasonable expenses; Garda vetting and a short induction")],
            href=_MAIL_BOARD, btn="Enquire about a role",
        ),
        gifts="We are not asking for or accepting gifts yet. When we can, we will say so on this page.",
    ),
    join=dict(tag="Taking part",
              text="Want to take part yourself? Every programme welcomes beginners, and coming once "
                   'commits you to nothing. <a class="link" href="programmes.html">See the programmes</a>'),
)


# Giving (Friends, sponsored concerts, the promise to supporters) is closed.
# Its copy lives in giving_en.py, outside the public repository, and is read
# only when layout.OPEN_GIVING is True.
if OPEN_GIVING:
    import giving_en
    giving_en.apply(globals())

INDEX = P.home(HOME, PROGRAMMES_DATA, PILLARS)
ABOUT = P.about(ABOUT_T)
PROGRAMMES = P.programmes(PROGRAMMES_T, PROGRAMMES_DATA, PILLARS)
GET_INVOLVED = P.get_involved(GET_INVOLVED_T, _ico)


# ---------------------------------------------------------------------------
# NEWS & ARCHIVE
# ---------------------------------------------------------------------------

NEWS_T = dict(
    head=dict(
        eyebrow="News &amp; archive",
        title=["What is new, and what we have done."],
        # 40+ since 2023; the forty on the record to August 2026 are 17 + 20 + 1 + 2 (03 §1)
        lead="40+ sessions and performances since 2023. On the record to August 2026: seventeen "
             "talks, twenty outreach performances, one pilot concert and two concerts for South "
             "Dublin Live 2026.",
        img=("quartet-hall.jpg", 1400, 791,
             "A string quartet and its conductor playing in a hall decorated for St Patrick&rsquo;s Day"),
        cap=("Letters Ensemble", "St Patrick&rsquo;s Day concert"),
    ),
    latest_sr="Latest",
    latest=[
        ("Autumn 2026", "Forming a founding board",
         "We are forming a company limited by guarantee and looking for volunteer directors.",
         "get-involved.html#board", "The roles"),
        ("Autumn 2026", "Free Recorder Ensemble course",
         "Running at Mulhuddart Community Centre on Wednesday evenings.",
         "programmes.html#recorder-ensemble", "About the course"),
        ("August 2026", "South Dublin Live 2026",
         "Our founder was selected by South Dublin County Council&rsquo;s Arts Office: two concerts, "
         "at Tallaght University Hospital and at Rua Red, Tallaght.",
         "#gallery", "Photographs"),
    ],
    chart=dict(
        label="The record",
        h2="Forty, one square each.",
        lead="Every talk and performance on the record, month by month, from February 2023 to August "
             "2026. Filled squares are talks; open squares are concerts and performances.",
        aria=("A calendar from 2023 to 2026 with one square for each of {n} sessions on the record: "
              "{talks} talks and {perf} performances."),
        scroll="The record, month by month",
        key_talk="Talk ({n})",
        key_perf="Concert or performance ({n})",
        # the ledger's own note on talk 15 (5 Dec 2025)
        key_note="The fifteenth talk session, in December 2025, was a concert attended together. "
                 "Other outings, rehearsals and classes are not counted.",
    ),
    timeline=dict(
        label="Timeline",
        h2="From one clarinet to a community.",
        rows=[
            ("February 2023", "Before the beginning",
             "A clarinet solo in Lourdes, France, a year before the work had a name."),
            ("January 2024", "It starts",
             "Founded in Dublin, with the Letters Ensemble. Six people come to the first talk."),
            ("2024", "Music goes out",
             "Dalgan Park, Co. Meath; Co. Wicklow; London; Paris; Daegu. The talks move to TU Dublin."),
            # 08 §2: introduced, with group attendance organised
            ("Autumn 2025", "Introducing concerts",
             "We start introducing concerts to participants and organising group attendance: the "
             "NCH International Series, the TU Dublin Philharmonic and, early in 2026, the National "
             "Symphony Orchestra."),
            ("October 2025", "An audience becomes players",
             "Preparation begins for a recorder ensemble with seven retired Presentation Sisters."),
            ("December 2025", "A concert, attended together",
             "For the fifteenth session we go together to a concert at the National Concert Hall."),
            ("January&ndash;April 2026", "The pilot, and its concert",
             "Ten weekly rehearsals at Warrenmount, Dublin 8, and an Easter concert at Clondalkin "
             "Lodge. All seven completed."),
            ("August 2026", "South Dublin Live 2026",
             "Our founder was selected for South Dublin Live 2026 by South Dublin County "
             "Council&rsquo;s Arts Office: two concerts, at Tallaght University Hospital and Rua Red. "
             "The pilot group concludes the same month."),
            ("Autumn 2026", "The course opens to the public",
             "The Free Recorder Ensemble course runs at Mulhuddart Community Centre on Wednesday "
             "evenings, free."),
        ],
    ),
    gallery=dict(
        label="Photographs",
        h2="In the room.",
        lead="We show performers, instruments and empty rooms. Anyone else who can be recognised "
             "appears only with their written consent.",
        rows=[
            (("hero-outreach.jpg", 1800, 1350,
              "The Letters Ensemble and their conductor playing a St Patrick&rsquo;s Day concert in a hall"),
             "Letters Ensemble · St Patrick&rsquo;s Day concert"),
            (("care-christmas.jpg", 1400, 1050, CARE_ALT),
             "Outreach concert · Christmas"),
            (("columban-ensemble.jpg", 1400, 1050,
              "Four string players of the Letters Ensemble and their conductor in a bright yellow room"),
             "Missionary Sisters of St Columban, Co. Wicklow · November 2024"),
            (("dalgan-hall.jpg", 1400, 1050,
              "A hall set out with chairs and music stands before a concert, with no one there yet"),
             "Dalgan Park, Co. Meath · March 2024"),
            (("church-aisle.jpg", 1050, 1400,
              "A clarinet held up before the altar of a parish church in Co. Westmeath"),
             "Dysart, Co. Westmeath · 2025"),
            (("score-stand.jpg", 1050, 1400, "A string trio rehearsing behind a part on a music stand"),
             "Before the Christmas concert · December 2025"),
            (("recorders.jpg", 1343, 1400, RECORDERS_ALT),
             "Recorders · November 2025"),
            (("tuh-trio.jpg", 1400, 787,
              "Soprano, piano and clarinet in the atrium of Tallaght University Hospital"),
             "Tallaght University Hospital · August 2026 · photo: Tallaght University Hospital"),
            (("ruared-trio.jpg", 1400, 933, "Clarinet, soprano and piano taking a bow on the Rua Red stage"),
             "Rua Red, Tallaght · August 2026 · photo: Ben Ryan / SDCC"),
            (("letters-ensemble.jpg", 1400, 1050, "The Letters Ensemble with their instruments"),
             "Letters Ensemble"),
            (("two-clarinets.jpg", 1050, 1400, "Two clarinets resting on the lid of a piano"), None),
            (("tuh-haegeum.jpg", 1400, 934, "A haegeum player performing in a hospital atrium"),
             "Tallaght University Hospital · August 2026 · photo: Tallaght University Hospital"),
        ],
    ),
)

NEWS = P.news(NEWS_T, L)


# ---------------------------------------------------------------------------
# CONTACT, with the privacy notice (kit 06: a privacy notice on the website)
# ---------------------------------------------------------------------------

CONTACT_T = dict(
    head=dict(
        eyebrow="Contact",
        title=["Write to us."],
        lead="We answer every message. One line is enough.",
    ),
    email_label="Email",
    email=EMAIL,
    email_href=_mail("Enquiry: Classical Music for Everyone"),
    btn="Email us",
    tel="+353 83 078 0635",
    tel_href="tel:+353830780635",
    details_label="Details",
    details_h2="Where we are.",
    # Insurance: the certificate is in hand (1 Oct 2026). Garda vetting is not
    # mentioned until it is complete.
    details=[("Based in", "Dublin, Ireland"),
             ("We travel to", "Dublin, Co. Meath, Co. Wicklow, Co. Westmeath, and further by arrangement"),
             ("Languages", 'English · <span lang="ko">한국어</span>'),
             ("Insurance", "Public liability insurance. We show the certificate to a venue on request."),
             ("Who answers", "Andrew Seohyeon Kim, Founder &amp; Artistic Director")],
    privacy=dict(
        label="Privacy",
        h2="Your details.",
        intro="This website has no forms, no cookies, no analytics and no advertising. Last updated "
              "1 October 2026.",
        blocks=[
            ("Who is responsible", '<span class="brandname">Classical Music for Everyone</span>, a '
                                   "not-for-profit community music initiative in Dublin. For anything "
                                   f'about your details, write to <a class="link" href="mailto:{EMAIL}">{EMAIL}</a>.'),
            ("When you email us", "We use what you send only to answer you and to do what you asked: a "
                                  "concert enquiry, a board enquiry or an expression of interest from a "
                                  "musician. We never sell or share it. Musicians&rsquo; details are kept "
                                  "for up to two years to offer engagements; telling us about access needs "
                                  "is optional."),
            ("Who else handles it", "This site is hosted by GitHub, which records visitors&rsquo; IP "
                                    "addresses for security. Its typefaces come from Google Fonts, which "
                                    "also receives your IP address, and our email runs on Google. These "
                                    "services may handle data outside the European Economic Area under "
                                    "safeguards approved by the EU."),
            ("Your rights", "You can ask to see, correct or delete what we hold about you, to restrict "
                            "or object to its use, or for a copy, at any time. If you are not satisfied "
                            'with our answer, you can complain to the <a class="link" '
                            'href="https://www.dataprotection.ie/">Data Protection Commission</a>.'),
        ],
    ),
)

CONTACT = P.contact(CONTACT_T)
