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


def _fields(prompts):
    """A mail body with one line per prompt, for the reader to fill in."""
    return "".join(f"{x}: \n" for x in prompts)


# One invitation, the same wherever it is offered (Outreach Concerts, Get
# involved, Contact), so a venue gets the same questions from every door.
INVITE_FIELDS = ["Organisation and town",
                 "The room (day room, chapel, hall) and whether it has a piano",
                 "Who will be listening, and roughly how many",
                 "Dates or times that suit",
                 "A contact name and phone number"]
MAIL_INVITE = _mail("Inviting an outreach concert", _fields(INVITE_FIELDS))
_MAIL_INVITE = MAIL_INVITE
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
         icon="score", vocab="Getting closer · Together · My taste",
         img=("lecture-recital.jpg", 1050, 1400, "A lecture-recital in progress"),
         line="Talks with live music for people who like classical music and never knew where to start.",
         page=dict(
             lead="Talks with live music for people who like the sound of classical music and never "
                  "knew where to start. You do not need to know anything beforehand.",
             cap=None,
             glance=[("For", "Anyone curious about classical music"),
                     ("Where", "Dublin"),
                     ("When", "On request"),
                     ("What you need", "No knowledge of music")],
             now=("On request", "No talk is scheduled at the moment. Write to us and we will plan one "
                                "with your group."),
             # 02 §4: three stages, in this order; 08 §1 for what each covers
             how_h2="Three stages, from first listening to your own taste.",
             steps=[("Getting Closer",
                     "What classical music is, by period and by instrument, with recordings and live "
                     "playing."),
                    ("Experiencing Together",
                     "Orchestras and performers, including Ireland&rsquo;s own, and the practical side: "
                     "booking a ticket, choosing a seat."),
                    ("Discovering My Taste",
                     "Finding what you like, for example by hearing one piece played by five different "
                     "pianists.")],
             expect_h2="Before your first talk.",
             faq=[("Do I need to know anything first?",
                   "<strong>No.</strong> The first stage starts from the question &lsquo;what is classical music?&rsquo;, "
                   "and each talk explains the music it plays."),
                  ("How many people come?",
                   "Usually six to fourteen. Six came to the first talk in January 2024; fourteen came "
                   "in April 2025."),
                  ("Can our group ask for a talk?",
                   "<strong>Yes.</strong> Talks are arranged on request. Tell us who the group is, roughly how many "
                   "people, and where you could meet.")],
             record_h2="Talks so far.",
             record_lead="Every talk on the record, with its date, topic and place. In December 2025 "
                         "the group went to a concert together instead.",
             join_h2="Ask for a talk.",
             join_text="Write with the group, the place and dates that suit. On your own? Write anyway, "
                       "and we will tell you when a talk is arranged.",
             join_btn="Ask about a talk",
             mail=_mail("Getting to Know Classical Music",
                        _fields(["Your name", "Your group or organisation (if any)",
                                 "Where you could meet", "Roughly how many people",
                                 "Dates or times that suit"])),
             mail_fields=["Your name", "Your group or organisation (if any)", "Where you could meet",
                          "Roughly how many people", "Dates or times that suit"],
         )),
    dict(slug="outreach-concerts", pillar="share", name="Outreach Concerts",
         short="Outreach Concerts",
         icon="room", vocab="Day room · Chapel · Atrium",
         img=("care-christmas.jpg", 1400, 1050, CARE_ALT),
         line="Live classical music in the rooms where people already are: care homes, hospitals, "
              "parishes and community centres.",
         page=dict(
             lead="We bring live classical music to the rooms where people already are: care homes, "
                  "hospitals, religious communities, parishes and community centres. We explain the "
                  "music as we go.",
             cap=("Outreach concert", "Christmas 2025"),
             glance=[("For", "Care homes, hospitals, parishes and community groups"),
                     ("Where", "Your own room: Dublin, Co. Meath, Co. Wicklow, Co. Westmeath, or further "
                               "by arrangement"),
                     ("When", "By arrangement"),
                     ("What you need", "A room, a date and a contact person")],
             now=("Taking invitations", "No concert is fixed at the moment. Write with your room and a "
                                        "few dates that suit."),
             how_h2="From one email to music in your room.",
             steps=[("You tell us",
                     "Write with the room, the date you have in mind and who will be listening."),
                    ("We plan the music",
                     "We choose pieces people can enjoy on first hearing, for that room and those "
                     "listeners."),
                    ("We come and play",
                     "Musicians and instruments come with us. We play for thirty to sixty minutes and "
                     "introduce each piece.")],
             expect_h2="Before you invite us.",
             faq=[("Who plays?",
                   "Our founder, Andrew Seohyeon Kim, clarinettist and organist, alone or with "
                   "musicians he invites. Some concerts are given by our Letters Ensemble."),
                  ("Who can listen?",
                   "Whoever is in the room: residents or patients, family and staff. No one needs to "
                   "know the music, and there is no dress code."),
                  ("Where have you played?",
                   "Care homes, religious communities, parishes and churches, a hospital, an arts centre, a "
                   "university, an HSE day service and a homeless hostel, in Ireland, France, the UK "
                   "and Korea.")],
             record_h2="Concerts so far.",
             record_lead="Every outreach concert on the record, with its date, its place and the music "
                         "we brought. The Letters Ensemble gave four of them; two were for South Dublin "
                         "Live 2026, for which our founder was selected.",
             join_h2="Invite a concert.",
             join_text="Write with your organisation, the room, who will be listening and some dates "
                       "that suit. We will reply to talk it through.",
             join_btn="Invite a concert",
             mail=MAIL_INVITE,
             mail_fields=INVITE_FIELDS,
         )),
    dict(slug="recorder-ensemble", pillar="learn", name="Community Recorder Ensemble Class",
         short="Recorder Ensemble Class",
         icon="recorder", vocab="First notes · Reading · Your own part",
         img=("recorders.jpg", 1343, 1400, RECORDERS_ALT),
         # renamed 1 Oct 2026
         line="A weekly class for adults who have never played: first notes, then your own part in an "
              "ensemble.",
         page=dict(
             lead="A weekly class for adults who have never played. You make a first sound in week one "
                  "and, week by week, learn to play your own part in an ensemble.",
             cap=("Recorders", "November 2025"),
             # the pilot ensemble on the founder's own channel; our still until play is pressed
             video=dict(kind="youtube", id="i7skwGKWSYY", poster="recorders.jpg",
                        cap=("The pilot ensemble", "Retired Presentation Sisters playing the recorder "
                                                   "together. The class grew from this group.")),
             room_h2="Where the class began.",
             glance=[("For", "Adults who have never played an instrument"),
                     ("Where", "Mulhuddart Community Centre, Dublin 15"),
                     ("When", "Wednesday evenings, 7:00&#8288;&ndash;&#8288;8:00pm, autumn 2026"),
                     ("What you need", "No instrument and no music reading; we can lend you a recorder")],
             now=("Running now", "<strong>Wednesday evenings, 7:00&#8288;&ndash;&#8288;8:00pm</strong>, at Mulhuddart "
                                 "Community Centre, Dublin 15."),
             live=True,
             how_h2="From a first note to your own part.",
             steps=[("Your first notes",
                     "Hold the recorder, breathe and play. You make a real sound in the first week."),
                    ("Reading from zero",
                     "Small steps every week: notes and fingering one at a time, with scores we make "
                     "for the class."),
                    ("Your own part",
                     "The group plays in harmony, and each player has their own line. The term "
                     "ends with a small concert of our own.")],
             expect_h2="Before your first class.",
             faq=[("Do I need my own recorder?",
                   "<strong>No.</strong> We can lend you one."),
                  ("Do I need to read music?",
                   "<strong>No.</strong> Reading starts from zero, a few notes at a time, alongside playing."),
                  ("Where did the class come from?",
                   "From a ten-week pilot with seven retired Presentation Sisters, who rehearsed at "
                   "Warrenmount, Dublin 8, and gave an Easter concert at Clondalkin Lodge.")],
             record_h2="The story so far.",
             record_lead="How the class came about: a question at a concert in 2024, the pilot with "
                         "seven retired Presentation Sisters, and the class in Mulhuddart.",
             join_h2="Join the class.",
             join_text="Never played anything? That is who the class is for. Write with your name and we "
                       "will tell you how to join.",
             join_btn="Ask about the class",
             mail=_mail("Community Recorder Ensemble Class",
                        _fields(["Your name", "A phone number (optional)",
                                 "Have you played an instrument before?",
                                 "Would you like to borrow a recorder?"])),
             mail_fields=["Your name", "A phone number (optional)",
                          "Have you played an instrument before?",
                          "Would you like to borrow a recorder?",
                          "Anything that would make it easier to take part (optional)"],
         )),
    dict(slug="letters-ensemble", pillar="share", name="Letters Ensemble",
         short="Letters Ensemble",
         icon="people", vocab="Irish · Korean · Sacred",
         img=("letters-ensemble.jpg", 1400, 1050, "The Letters Ensemble with their instruments"),
         line="Amateur musicians in Dublin playing Irish, Korean and sacred music in community settings "
              "since January 2024.",
         page=dict(
             lead="An ensemble of amateur musicians living in Dublin, formed in January 2024. We play "
                  "Irish and Korean traditional music, sacred music and accessible arrangements in "
                  "community settings.",
             cap=("Letters Ensemble", "with their instruments"),
             glance=[("For", "Amateur players of any background, on strings, winds and more"),
                     ("Where", "Dublin"),
                     ("When", "Ask us for rehearsal times"),
                     ("What you need", "An instrument you play")],
             now=("All players welcome", "No concert date is fixed yet. Write with your instrument and "
                                         "we will tell you when we rehearse."),
             how_h2="Rehearse in Dublin, play where people are.",
             steps=[("Tell us your instrument",
                     "Write with what you play. Players of any background are welcome."),
                    ("Rehearse together",
                     "We rehearse in Dublin, directed by our founder, Andrew Seohyeon Kim."),
                    ("Play for a community",
                     "Concerts go to religious communities, parishes and care settings, often around a "
                     "feast day or Christmas.")],
             expect_h2="Before you join.",
             faq=[("What does the ensemble play?",
                   "Pieces such as Mozart&rsquo;s Ave verum corpus, Down by the Sally Gardens, Arirang "
                   "and When You Wish Upon a Star."),
                  ("I stopped playing years ago. Can I join?",
                   "Write to us. One member joined after a talk reminded them of the viola they had "
                   "played at school."),
                  ("How many concerts has it given?",
                   "Four formal concerts so far, from Dalgan Park, Co. Meath, in March 2024 to "
                   "Clondalkin Lodge at Christmas 2025.")],
             record_h2="Concerts so far.",
             record_lead="The ensemble&rsquo;s formal concerts on the record, with the date, occasion "
                         "and place of each.",
             join_h2="Play with us.",
             join_text="Write with your instrument, roughly how long you have played and when you last "
                       "played. We will reply with rehearsal details.",
             join_btn="Ask about joining",
             mail=_mail("Joining the Letters Ensemble",
                        _fields(["Your name", "Your instrument(s)",
                                 "How long you have played, and when you last played",
                                 "Days and times that usually suit you"])),
             mail_fields=["Your name", "Your instrument(s)",
                          "How long you have played, and when you last played",
                          "Days and times that usually suit you"],
         )),
    dict(slug="concert-companion", pillar="learn", name="Concert Guide &amp; Companion",
         short="Concert Guide &amp; Companion",
         icon="ticket", vocab="Before · During · After",
         img=("proms-hall.jpg", 1400, 933,
              "A full Royal Albert Hall during a BBC Prom, seen from high in the audience: the orchestra on a lit stage, beams of light and the acoustic discs overhead"),
         line="Going to concerts in small groups, with preparation before and a conversation after.",
         page=dict(
             lead="For people who would rather not go to a concert alone. A small group prepares "
                  "beforehand, goes together and talks it over afterwards.",
             # the founder's own photograph from the audience at the BBC Proms; no group trip to the
             # Proms is on the record, so the caption says whose view it is. The month is the
             # recording date of the source video (Andrew, 1 Oct 2026)
             cap=("BBC Proms, Royal Albert Hall", "London · September 2023 · seen from the audience by our founder"),
             room_h2="The hall, from the seats.",
             glance=[("For", "Anyone who would rather not go to a concert alone"),
                     ("Where", "Concert halls in Dublin"),
                     ("When", "When there is an outing; we will email you"),
                     ("What you need", "No knowledge of music; we prepare together first")],
             now=("Next outing by email", "No outing is planned at the moment. Write to us and we will "
                                          "tell you when there is one."),
             how_h2="Before, during and after the concert.",
             steps=[("Prepare beforehand",
                     "We choose a concert in Dublin and prepare together: what the music is, and what "
                     "happens in the hall."),
                    ("Go as a group",
                     "A group of about five goes together, with guidance during the concert."),
                    ("Talk it over",
                     "Afterwards we talk about what we heard. There is no wrong answer.")],
             expect_h2="Before your first outing.",
             faq=[("Which concerts have you suggested?",
                   "The NCH International Series, the TU Dublin Philharmonic, the RT&Eacute; Concert "
                   "Orchestra, the RIAM piano series and the National Symphony Orchestra."),
                  ("How big is a group?",
                   "About five. In December 2025 a group of six went together to a concert at the "
                   "National Concert Hall."),
                  ("New to Ireland. Is this for me?",
                   "<strong>Yes.</strong> The programme is for anyone who would not go alone, including people new to "
                   "Ireland. We work in English and Korean.")],
             record_h2="Concerts suggested so far.",
             record_lead="Concerts we introduced to participants, with group attendance organised, and "
                         "the December 2025 concert we went to together.",
             join_h2="Join an outing.",
             join_text="Write with your name and the days and times that suit you. We will tell you when "
                       "there is an outing to join.",
             join_btn="Ask about an outing",
             mail=_mail("Concert Guide & Companion",
                        _fields(["Your name", "Days and times that suit you",
                                 "Music you like, or would like to try (optional)",
                                 "Language you prefer: English or Korean"])),
             mail_fields=["Your name", "Days and times that suit you",
                          "Music you like, or would like to try (optional)",
                          "Anything we should check about access (optional)",
                          "Language you prefer: English or Korean"],
         )),
]


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------

HOME = dict(
    hero=dict(
        eyebrow="Community music · Dublin, Ireland",
        title=["Classical music,", '<span class="for">for </span><em>Everyone.</em>'],
        master="Bringing classical music where it&rsquo;s needed!",
        # kit 27: the 25-word version (with the class's new name), then how we work
        lead='<span class="brandname">Classical Music for Everyone</span> brings live classical music, '
             "talks and a community recorder ensemble to older people, migrant communities and care "
             "settings in Dublin. We explain the music as we go, and we invite people to play as "
             "well as listen.",
        cta=("get-involved.html", "Get involved"),
        more=("#programmes", "See what we do"),
        img=("hero-outreach.jpg", 1800, 1350,
             "The Letters Ensemble and their conductor playing a St Patrick&rsquo;s Day concert in a hall"),
        cap=("Letters Ensemble", "St Patrick&rsquo;s Day concert"),
    ),
    # the ways in, as the contents line of a programme (no boxes, no tint):
    # taking part comes first, because most visitors come to join something
    ways_label="Ways in",
    ways=[("programmes.html", "Take part", "Join a talk, the class, the ensemble or an outing",
           "The programmes"),
          ("get-involved.html#invite", "Venues", "Bring a concert to your place", "Invite us"),
          ("get-involved.html#play", "Musicians", "Perform with us, from 2027", "Tell us about you"),
          ("get-involved.html#board", "Volunteers", "Join the founding board", "The five roles")],
    progs=dict(
        label="What we do",
        h2="Five programmes.",
        lead="Three help people listen and play. Two take live music out to the places where people "
             "already are.",
        # kit 27, message 3: a plan, said as a plan, with the one thing open now
        artists='From 2027 we plan paid, mentored performances for emerging musicians, as CMFE '
                'Artists. <a class="link" href="get-involved.html#play">Expressions of interest are '
                "open now</a>.",
    ),
    # kit 27 ①, the opening of the one-page case, set in three parts so the
    # answer stands out; Ireland rather than Dublin (Andrew, 1 Oct 2026). It
    # describes the need, not our reach: never "across Ireland".
    why=dict(
        label="Why we exist",
        premise="Many people in Ireland never get to a concert.",
        reasons=["Some live in a nursing home.",
                 "Some rarely leave the house.",
                 "Some are new to the country and don&rsquo;t know where to begin."],
        resolve="So we go to <em>them.</em>",
        link="About us",
    ),
    numbers=dict(
        label="On the record",
        sr="In numbers",
        figs=[(40, "sessions and performances", "since 2024", True),
              (5, "programmes, in Learning and Sharing", "as of October 2026", False),
              (4, "countries: Ireland, France, the UK and Korea", "2024–2025", False)],
        forty=dict(aria="The {n} talks and performances on the record to September 2026, one square each: "
                        "{talks} talks and {perf} performances.",
                   talks="Talk ({n})", perf="Performance ({n})",
                   period="On the record to September 2026, one square each"),
        # kit 27: a selection of the founder, said as such
        note="In 2026 South Dublin County Council&rsquo;s Arts Office selected our founder for South "
             'Dublin Live. <a class="link" href="news.html#record">See the record, month by month</a>',
    ),
    now=dict(
        img=("recorders.jpg", 1343, 1400, RECORDERS_ALT),
        label="Now running",
        tag="Running now",
        facts=[("When", "Wednesday evenings, 7:00&#8288;&ndash;&#8288;8:00pm"),
               ("Where", "Mulhuddart Community Centre, Dublin 15"),
               ("For", "Adults who have never played. We can lend you a recorder.")],
        btn="About the class",
    ),
)


# ---------------------------------------------------------------------------
# ABOUT. The anchors #founder #run #places #identity are redirect targets.
# ---------------------------------------------------------------------------

ABOUT_T = dict(
    glance_sr="At a glance",
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
        h2="Since 2024.",
        # the site counts from the founding, January 2024 (Andrew, 1 Oct 2026)
        text=["In January 2024 Andrew Seohyeon Kim founded "
              '<span class="brandname">Classical Music for Everyone</span> and the Letters Ensemble '
              "in Dublin; six people came to the first talk.",
              "By September 2026 there were forty recorded talks and performances, in care homes, "
              "religious communities, parishes, a hospital, a homeless hostel and community centres. "
              "In 2026 a pilot recorder ensemble with seven retired Presentation Sisters led to a community "
              "class at Mulhuddart, and South Dublin County Council&rsquo;s Arts Office selected our "
              "founder for South Dublin Live 2026."],
        link="The full timeline",
    ),
    founder=dict(
        # the founder playing, not speaking: the lecture photograph showed a
        # projected slide with other recognisable people (art direction, 1 Oct 2026)
        img=("founder-playing.jpg", 1050, 1400,
             "Andrew Seohyeon Kim playing the clarinet in the chapel of Tallaght University Hospital"),
        cap=("Tallaght University Hospital", "August 2026 · photo: Tallaght University Hospital"),
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
        h2="A not&#8209;for&#8209;profit initiative.",
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
        # every name is on the record (content review, 1 Oct 2026); grouped by
        # the kind of place, each with where it is; counts are derived
        groups=[
            ("Hospital and care", [
                ("Tallaght University Hospital", "Tallaght, Dublin"),
                ("Clondalkin Lodge", "Dublin"),
                ("HSE EVE Goirtin Hub", "Dublin 7"),
                ("Morning Star Hostel", "Dublin 7")]),
            ("Religious communities", [
                ("Missionary Sisters of St Columban", "Magheramore, Co. Wicklow"),
                ("Dalgan Park", "Co. Meath"),
                ("Warrenmount", "Dublin 8"),
                ("Franciscan Missionaries of Mary", "Dublin 5")]),
            ("Parishes and churches", [
                ("Our Lady of Dolours", "Dolphin&rsquo;s Barn, Dublin"),
                ("Church of the Three Patrons", "Rathgar, Dublin 6"),
                ("Methodist Centenary Church", "Ranelagh, Dublin 6"),
                ("Blessed Sacrament Chapel", "Dublin 1"),
                ("Kilmessan Church", "Co. Meath"),
                ("Dysart Parish", "Co. Westmeath")]),
            ("Arts, education and community", [
                ("Rua Red", "Tallaght, Dublin"),
                ("TU Dublin", "Grangegorman, Dublin 7"),
                ("Carmelite Community Centre", "Dublin"),
                ("Mulhuddart Community Centre", "Dublin 15")]),
            ("Abroad", [
                ("Missions &Eacute;trang&egrave;res de Paris", "Paris, France"),
                ("Palais Brongniart", "Paris, France"),
                ("London Korean Catholic Church", "London, United Kingdom"),
                ("Gwandukjeong Martyrs Memorial Centre", "Daegu, Korea")]),
        ],
        map=dict(
            labels={"dublin": ("Dublin", None), "meath": ("Co. Meath", None),
                    "wicklow": ("Co. Wicklow", "Magheramore"), "westmeath": ("Co. Westmeath", "Dysart")},
            count="{n} places",
            aria="A map of the island of Ireland with the places in Ireland where we have played and "
                 "taught: fourteen in Dublin, two in Co. Meath, and one each in Co. Wicklow and "
                 "Co. Westmeath.",
            caption="In Ireland: Dublin and three counties. Abroad: France, the United Kingdom and Korea.",
        ),
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
        lead="Three help people listen and play. Two take live music out to the places where people "
             "already are. Each has its own page: how it works, what is on now and what it has done.",
    ),
    list_sr="The five programmes",
    # kit 27, message 3: a plan, said as a plan, with the one thing open now
    artists=dict(
        label="For musicians",
        text='CMFE Artists, planned for 2027: paid, mentored performances for emerging musicians. '
             '<a class="link" href="get-involved.html#play">Expressions of interest are open now</a>.',
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
        lead="Take part in a programme, bring a concert to your place, tell us you would like to "
             "perform, or join the founding board. One line by email is enough to start.",
    ),
    ways_label="Four ways",
    ways=[("programmes.html", "Take part", "Join a talk, the class, the ensemble or an outing",
           "The programmes"),
          ("#invite", "Venues", "Bring a concert to your place", "How it works"),
          ("#play", "Musicians", "Perform with us, from 2027", "What to send"),
          ("#board", "Volunteers", "Join the founding board", "The five roles")],
    # the address and phone under each mail button
    alt=dict(or_write="Or write to", email=EMAIL, tel="+353 83 078 0635", tel_href="+353830780635"),
    invite=dict(
        label="Partner venues",
        h2="Bring a concert to your place.",
        # kit 02 §2 and 29: what a host gives, and what we can promise
        text="Care homes, hospitals, libraries, parishes and community centres. Tell us your room "
             "and a date, and we bring the players, instruments, stands and programme. A community "
             "centre can also host a beginners&rsquo; recorder class: you give a warm room once a "
             "week, a contact and help letting local people know, and we bring the rest as funding "
             "allows.",
        # the same three steps as the Outreach Concerts page
        steps=[s for s in PROGRAMMES_DATA[1]["page"]["steps"]],
        href=MAIL_INVITE, btn="Invite us", more="About outreach concerts",
    ),
    play=dict(
        label="CMFE Artists",
        h2="Perform with us.",
        lead="For student, emerging, amateur and Korean musicians, and professional players who "
             "want to play where music is needed. We plan to begin CMFE Artists in 2027; tell us "
             "about yourself now and we will write when the first call opens. Amateur players of any "
             'background can join the <a class="link" href="programmes/letters-ensemble.html">Letters '
             'Ensemble</a> now.',
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
              text="Want to take part yourself? Most programmes need no experience, and coming once "
                   'commits you to nothing. <a class="link" href="programmes.html">See the programmes</a>'),
)


# Giving (Friends, sponsored concerts, the promise to supporters) is closed.
# Its copy lives in giving_en.py, outside the public repository, and is read
# only when layout.OPEN_GIVING is True.
if OPEN_GIVING:
    import giving_en
    giving_en.apply(globals())

# ---------------------------------------------------------------------------
# PROGRAMME PAGES (programmes/<slug>.html), from 1 October 2026. The copy for
# each page is the `page` dict of its programme above; these are the labels
# the five pages share. The record on each page comes from ledger.py.
# ---------------------------------------------------------------------------

PROGRAMME_T = dict(
    crumbs_label="Breadcrumb", crumb="Programmes",
    how_label="How it works", expect_label="What to expect", record_label="On the record",
    join_label="Take part", others_label="The other programmes", all_label="All five programmes",
    room_label="In the room", room_h2="Where it happens.",
    how_join="How to take part",
    video_h="Watch", video_label="Video: {name}", play="Play the video", watch="Watch on {service}",
    people="{n} people",
    mail_hint="One line is enough. If it helps, tell us:",
    or_write="Or write to", email=EMAIL, tel="+353 83 078 0635", tel_href="+353830780635",
    strip=dict(aria="{n} sessions on the record for this programme, shown month by month from 2024 to 2026.",
               learn="Learning", share="Sharing", note="Each mark is one session; a bar spans several months."),
    att=dict(h3="How many came", lead="Attendance at each talk where it was recorded.",
             aria="Attendance at {n} talks where it was recorded: from {lo} to {hi} people.",
             people="{n} people"),
)

PROGRAMME_PAGES = {_p["slug"]: P.programme_page(PROGRAMME_T, _i, _p, PROGRAMMES_DATA, PILLARS, L)
                   for _i, _p in enumerate(PROGRAMMES_DATA)}

INDEX = P.home(HOME, PROGRAMMES_DATA, PILLARS, L)
ABOUT = P.about(ABOUT_T, L)
PROGRAMMES = P.programmes(PROGRAMMES_T, PROGRAMMES_DATA, PILLARS)
GET_INVOLVED = P.get_involved(GET_INVOLVED_T, _ico)


# ---------------------------------------------------------------------------
# NEWS & ARCHIVE
# ---------------------------------------------------------------------------

NEWS_T = dict(
    head=dict(
        eyebrow="News &amp; archive",
        title=["What is new, and what we have done."],
        # 40+ since 2024; the forty on the record to September 2026 are 17 + 20 + 1 + 2 (03 §1)
        lead="40+ sessions and performances since 2024. On the record to September 2026: seventeen "
             "talks, twenty outreach performances, one pilot concert and two concerts for South "
             "Dublin Live 2026.",
    ),
    latest_sr="Latest",
    latest=[
        ("Autumn 2026", "Forming a founding board",
         "We are forming a company limited by guarantee and looking for volunteer directors.",
         "get-involved.html#board", "The roles"),
        ("Autumn 2026", "Community Recorder Ensemble Class",
         "Running at Mulhuddart Community Centre on Wednesday evenings.",
         "programmes/recorder-ensemble.html", "About the class"),
        ("August 2026", "South Dublin Live 2026",
         "Our founder was selected by South Dublin County Council&rsquo;s Arts Office: two concerts, "
         "at Tallaght University Hospital and at Rua Red, Tallaght.",
         "#gallery", "Photographs"),
    ],
    chart=dict(
        label="The record",
        h2="Forty, one square each.",
        lead="Every talk and performance on the record, month by month, from January 2024 to September "
             "2026. Filled squares are talks; open squares are concerts and performances.",
        aria=("A calendar from 2024 to 2026 with one square for each of {n} sessions on the record: "
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
        h2="From a first talk to a community.",
        rows=[
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
            ("September 2026", "An autumn concert",
             "Soprano, haegeum, clarinet and piano at Methodist Centenary Church, Ranelagh, Dublin 6."),
            ("Autumn 2026", "The class opens to the public",
             "The Community Recorder Ensemble Class runs at Mulhuddart Community Centre on "
             "Wednesday evenings."),
        ],
    ),
    gallery=dict(
        label="Photographs",
        h2="In the room.",
        lead="We show performers, instruments and empty rooms. Anyone else who can be recognised "
             "appears only with their written consent.",
        # newest first, a contact sheet: every frame at its own shape, with a true caption
        rows=[
            (("tuh-trio.jpg", 1236, 787,
              "Soprano, piano and clarinet in the atrium of Tallaght University Hospital"),
             "Tallaght University Hospital · August 2026 · photo: Tallaght University Hospital"),
            (("tuh-atrium.jpg", 1400, 1052, TUH_CHAPEL_ALT),
             "Tallaght University Hospital · August 2026 · photo: Tallaght University Hospital"),
            (("tuh-haegeum.jpg", 1400, 934, "A haegeum player performing in a hospital atrium"),
             "Tallaght University Hospital · August 2026 · photo: Tallaght University Hospital"),
            (("ruared-trio.jpg", 1400, 933, "Clarinet, soprano and piano taking a bow on the Rua Red stage"),
             "Rua Red, Tallaght · August 2026 · photo: Ben Ryan / SDCC"),
            (("care-christmas.jpg", 1400, 1050, CARE_ALT),
             "Outreach concert · Christmas 2025"),
            (("score-stand.jpg", 1050, 1400, "A string trio rehearsing behind a part on a music stand"),
             "Before the Christmas concert · December 2025"),
            (("recorders.jpg", 1343, 1400, RECORDERS_ALT),
             "Recorders · November 2025"),
            (("church-aisle.jpg", 1050, 1400,
              "A clarinet held up before the altar of a parish church in Co. Westmeath"),
             "Dysart, Co. Westmeath · 2025"),
            (("columban-ensemble.jpg", 1400, 1050,
              "Four string players of the Letters Ensemble and their conductor in a bright yellow room"),
             "Missionary Sisters of St Columban, Co. Wicklow · November 2024"),
            (("dalgan-hall.jpg", 1400, 1050,
              "A hall set out with chairs and music stands before a concert, with no one there yet"),
             "Dalgan Park, Co. Meath · March 2024"),
            (("hero-outreach.jpg", 1800, 1350,
              "The Letters Ensemble and their conductor playing a St Patrick&rsquo;s Day concert in a hall"),
             "Letters Ensemble · St Patrick&rsquo;s Day concert"),
            (("letters-ensemble.jpg", 1400, 1050, "The Letters Ensemble with their instruments"),
             "Letters Ensemble"),
            (("two-clarinets.jpg", 1050, 1400, "Two clarinets resting on the lid of a piano"),
             "Instruments · two clarinets"),
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
        lead="Choose what your message is about, or simply write. One line is enough, and we answer "
             "every message.",
    ),
    # what is it about? each row opens an email with its subject (and, for an
    # invitation, the same questions as everywhere else); the address itself
    # is quiet, underneath
    topics_h2="What is it about?",
    topics=[(_mail("Taking part"), "Taking part", "A talk, the class, the Letters Ensemble or an outing",
             "Write"),
            (MAIL_INVITE, "Venues", "Inviting a concert to your place", "Write"),
            (_MAIL_EOI, "Musicians", "Performing with us, from 2027", "Write"),
            (_MAIL_BOARD, "Founding board", "One of the five volunteer roles", "Write"),
            (_mail("Personal data request"), "Your details", "Seeing, correcting or deleting what we hold",
             "Write"),
            (_mail("Enquiry: Classical Music for Everyone"), "Anything else",
             "Questions, ideas, press or anything not on this list", "Write")],
    direct_label="Or write directly",
    email=EMAIL,
    email_href=_mail("Enquiry: Classical Music for Everyone"),
    tel="+353 83 078 0635",
    tel_href="+353830780635",
    details_label="Details",
    details_h2="Email, phone and where we travel.",
    # Insurance: the certificate is in hand (1 Oct 2026). Garda vetting is not
    # mentioned until it is complete.
    details=[("Email", f'<a class="link" href="mailto:{EMAIL}">{EMAIL}</a>'),
             ("Phone", '<a class="link" href="tel:+353830780635">+353 83 078 0635</a>'),
             ("Based in", "Dublin, Ireland"),
             ("We travel to", "Dublin, Co. Meath, Co. Wicklow, Co. Westmeath, and further by arrangement"),
             ("Languages", 'English · <span lang="ko">한국어</span>'),
             ("Insurance", "Public liability insurance. We show the certificate to a venue on request."),
             ("Who answers", "Andrew Seohyeon Kim, Founder &amp; Artistic Director")],
    privacy=dict(
        label="Privacy notice",
        h2="How we look after your details.",
        intro="What we do with the details you send us, and your rights. Last updated 1 October 2026.",
        # what this website does not have, said once and plainly
        none=[("Forms", "None"), ("Cookies", "None of ours"), ("Analytics", "None"), ("Advertising", "None")],
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
                                    "also receives your IP address, and our email runs on Google. The class "
                                    "page has a video from YouTube: nothing loads from YouTube until you "
                                    "press play, and then YouTube (Google) receives your IP address and may "
                                    "set its own cookies. These services may handle data outside the "
                                    "European Economic Area under safeguards approved by the EU."),
            ("Your rights", "You can ask to see, correct or delete what we hold about you, to restrict "
                            "or object to its use, or for a copy, at any time. If you are not satisfied "
                            'with our answer, you can complain to the <a class="link" '
                            'href="https://www.dataprotection.ie/">Data Protection Commission</a>.'),
        ],
    ),
)

CONTACT = P.contact(CONTACT_T)
