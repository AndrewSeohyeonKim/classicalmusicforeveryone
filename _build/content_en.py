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
from layout import OPEN_GIVING, PROG_MENU

L = "en"
EMAIL = "sby05034@gmail.com"

# The status sentence, word for word wherever the site says what we are (canon v2.0, 0-4 no. 1,
# 2026-10-31; request 20, 2 Nov 2026). The old sentence ("…a not-for-profit community music
# initiative, forming a company limited by guarantee. It is not yet a registered charity.") is retired:
# no "not yet" line about ourselves (Andrew).
STATUS = ('<span class="brandname">Classical Music for Everyone</span> is preparing to run as a '
          "not-for-profit social enterprise from&nbsp;2027, as a company limited by guarantee.")

# The two pillars' own lines (request 19 no. 4 and the Strategy 2027-2030): on each programme page's
# eyebrow and over the lines planned for 2027 on Programmes
PILLAR_LINES = {"learn": "We open the door", "share": "We take the music out"}


def _mail(subject, body=""):
    """A mailto link with a subject and, optionally, a pre-filled body."""
    href = f"mailto:{EMAIL}?subject={quote(subject)}"
    if body:
        href += "&amp;body=" + quote(body)
    return href


def _fields(prompts):
    """A mail body with one line per prompt, for the reader to fill in. A
    prompt that is a question or already has a colon gets no second one, and
    lines end in CRLF (RFC 6068; QA40-17)."""
    return "".join(f"{x}{'' if x.endswith(('?', ':')) or ': ' in x else ':'} \r\n" for x in prompts)


# One invitation, the same wherever it is offered (Outreach Concerts, Get
# involved, Contact), so a venue gets the same questions from every door.
INVITE_FIELDS = ["Organisation and town",
                 "The room (and piano, if any)",
                 "Who will listen, and how many",
                 "Dates or times that suit",
                 "Contact name and phone number"]
MAIL_INVITE = _mail("Concert invitation", _fields(INVITE_FIELDS))
_MAIL_INVITE = MAIL_INVITE
_MAIL_BOARD = _mail("Founding board: Classical Music for Everyone",
                    "The role that interests me (chair, treasurer, secretary, safeguarding and care, "
                    "community): \r\nA few lines about me: \r\n")

# Working with us (22 Oct 2026): a company, practical help, and the host of a recorder class
_MAIL_CO = _mail("Working with a company: Classical Music for Everyone",
                 _fields(["Company and town",
                          "What interests you (a workplace concert, volunteering, a venue, help in kind, advice)",
                          "Contact name and phone number"]))
_MAIL_INTEREST = _mail("Interest: Classical Music for Everyone",
                       _fields(["Your name", "What you would like to hear about"]))
_MAIL_HOST = _mail("Hosting a recorder class", _fields(["Organisation and town", "The room you could use",
                                                        "Contact name and phone number"]))

# CMFE Artist Services (the canon's name for line B since v7; "CMFE Artists" until 1 Nov 2026):
# interest is taken freely (Andrew, 2 Oct 2026). Four prompts in place of the kit 15 form: whoever
# writes can say the rest in their own words.
EOI_FIELDS = ["Your name", "Instrument, voice or art form", "A link to your work (optional)",
              "A few lines about you"]
_MAIL_EOI = _mail("CMFE Artist Services: expression of interest", _fields(EOI_FIELDS))


# ---------------------------------------------------------------------------
# The five programmes. One list, read by the home cards, the Programmes page
# and the structured data, so none of them can drift. Same fields, same
# order, no main one (CLAUDE.md §2.1). Each programme has one photograph and
# uses it everywhere it appears.
# ---------------------------------------------------------------------------

PILLARS = {"learn": ("Learning", "dot"), "share": ("Sharing", "dot dot-open")}

# Photographs that appear in more than one place keep one description.
# Players who have not given consent are shown with their faces softly blurred, and
# the set leans on the founder and on players seen from behind (Andrew, 14 Oct 2026).
# christmas-conducting: the founder conducting two string players (20 Dec 2025).
# goirtin-solo: the founder's clarinet solo at a day service (17 Apr 2025).
# tuh-atrium: despite the file name, the chapel set, with its cross and lectern.
XMAS_ALT = "Our founder, in a Santa hat, conducting two string players in a care home decorated for Christmas"
GOIRTIN_ALT = "A clarinettist playing in a bright room at a day service, before a screen that reads Thank you"
STPAT_ALT = "Four string players, seated and playing, and our founder conducting, in a hall hung with Irish flags and shamrocks"
TUH_CHAPEL_ALT = "Clarinet, haegeum and keyboard in the chapel of Tallaght University Hospital"
RECORDERS_ALT = "Six recorders of different sizes standing in a row"

# The places we have played and taught, grouped by the kind of place, each
# with where it is (About #places). Every name is on the record. The count
# is derived, so a sentence that quotes it cannot go stale (4th pass).
PLACES = [
    ("Hospital and care", [
        ("Tallaght University Hospital", "Tallaght, Dublin"),
        ("Clondalkin Lodge", "Dublin"),
        ("HSE EVE Goirtin Hub", "Dublin 7"),
        ("Morning Star Hostel", "Dublin 7")]),
    ("Parishes and churches", [
        ("Our Lady of Dolours", "Dolphin&rsquo;s Barn, Dublin"),
        ("Church of the Three Patrons", "Rathgar, Dublin 6"),
        ("Methodist Centenary Church", "Ranelagh, Dublin 6"),
        ("Blessed Sacrament Chapel", "Dublin 1"),
        ("Kilmessan Church", "Co. Meath"),
        ("Dysart Parish", "Co. Westmeath")]),
    ("Religious communities", [
        ("Missionary Sisters of St Columban", "Magheramore, Co. Wicklow"),
        ("Dalgan Park", "Co. Meath"),
        ("Warrenmount", "Dublin 8"),
        ("Franciscan Missionaries of Mary", "Dublin 5")]),
    ("Arts and learning", [
        ("Rua Red", "Tallaght, Dublin"),
        ("TU Dublin", "Grangegorman, Dublin 7"),
        ("Carmelite Community Centre", "Dublin"),
        ("Mulhuddart Community Centre", "Dublin 15")]),
    ("Abroad", [
        ("Missions &Eacute;trang&egrave;res de Paris", "Paris, France"),
        ("Palais Brongniart", "Paris, France"),
        ("London Korean Catholic Church", "London, United Kingdom"),
        ("Gwandukjeong Martyrs Memorial Centre", "Daegu, Korea")]),
]
N_PLACES = sum(len(rows) for _, rows in PLACES)

PROGRAMMES_DATA = [
    dict(slug="getting-to-know", pillar="learn", name="Getting to Know Classical Music",
         short="Getting to Know",
         # what the talks cover, in Andrew's words (3 Oct 2026); the stage names stay on the page
         icon="lesson", vocab="Music history · Theory · Stories",
         img=("lecture-recital.jpg", 1050, 1400, "Our founder teaching a Classical Music class, with a slide about the BBC Proms on the screen"),
         line="Talks with <mark>live music</mark>, for anyone curious about Classical Music.",
         page=dict(
             lead="Talks for anyone unsure where to begin. We use stories, recordings and <mark>live playing</mark>.",
             # the search result and share card: where, when, for whom (marketing r9)
             meta="Classical Music talks in Dublin for care settings, libraries, parishes and community groups: music history, theory and stories, with live playing. 45 to 60 minutes.",
             cap=("A Classical Music class on the BBC Proms", "Dublin"),  # Andrew 2026-10-29: this photo is a class
             room_h2="At a talk.",
             room_focus="50% 41%",
             # the Strategy 2027-2030 (p.11) and the Service Catalogue (4 Nov 2026): who, where and how long
             glance=[("For", "Anyone who loves music, especially older people"),
                     ("Where", "Care settings, libraries, parishes and community groups in Dublin"),
                     # the Strategy 2027-2030 (11-05): "A single talk or a six-week block"; the Catalogue's 45 to 60 minutes
                     ("When", "One talk or six weekly talks, 45 to 60 minutes each"),
                     ("What you need", "No knowledge of music")],
             now=("On request", "Write to us, on your own or as a group."),
             # 02 §4: three stages, in this order; 08 §1 for what each covers
             how_h2="From first listening to your own taste.",
             steps=[("Getting Closer",
                     "What Classical Music is, by period and by instrument, with recordings and live "
                     "playing."),
                    ("Together",
                     "Orchestras and performers, including Ireland&rsquo;s&nbsp;own, and how to book and choose a seat."),
                    ("My Taste",
                     "Finding <mark>what you like</mark>, for example by hearing one piece played by five pianists.")],
             expect_h2="Before your first talk.",
             faq=[("Do I need to know anything first?",
                   "<strong>No.</strong> We start from &lsquo;what is Classical Music?&rsquo; and "
                   "<mark>explain every piece</mark> we play."),
                  ("How many people come?",
                   "Between <mark>six and fourteen</mark> people came to each talk we counted."),
                  # Andrew, 6 Oct 2026 (a group asks through the status line and the join section)
                  ("Which language are the talks in?", "English or Korean, depending on the talk.")],
             record_h2="Every talk.",
             record_lead="",
             # the Strategy's 2027 line on each programme card (9 Nov 2026)
             next="Ten talks across the year, for the groups who ask.",
             join_h2="Ask for a talk.",
             join_text="",
             join_btn="Ask about a talk",
             mail_subject="Getting to Know Classical Music",
             mail_fields=["Your name", "Your group or organisation (if any)", "Where you could meet",
                          "Roughly how many people", "Dates or times that suit"],
         )),
    dict(slug="outreach-concerts", pillar="share", name="Outreach Concerts",
         short="Outreach Concerts",
         # the grand piano is the sign of a concert, not a list of what we bring
         # (pianos are on the record: clarinet and piano, the autumn concert)
         icon="piano", vocab="Day room · Chapel · Atrium",
         img=("goirtin-solo.jpg", 1120, 1400, GOIRTIN_ALT),
         line="Live Classical Music in <mark>care homes</mark>, hospitals, parishes and community centres.",
         page=dict(
             # each lead sentence fits its column on a laptop (typeset_check:
             # the longer first sentences folded into half lines)
             lead="We play in the rooms where <mark>people already are</mark>. We explain the music as we go.",
             meta="Live Classical Music in care settings, hospitals, parishes, religious communities, libraries, workplaces and community venues in Dublin, in your own room.",
             cap=("Clarinet solo", "A day service, Dublin 7 · April 2025"),
             room_h2="At a day service.",
             room_focus="50% 62.5%",
             # the Strategy (p.12) adds libraries and workplaces; hospitals and care homes stay until Hope Concerts start
             glance=[("For", "Care settings, hospitals, parishes, religious houses, libraries, workplaces and community venues"),
                     ("Where", "Your own room, in Dublin and further by arrangement"),
                     # the Strategy 2027-2030 (11-05): "Two or more musicians, 45 to 60 minutes" (it replaces the
                     # 6 Oct "one to two hours"); a room with a socket, a piano welcome (Andrew, 6 Oct 2026)
                     ("When", "A date we agree with you, for 45 to 60 minutes"),
                     ("What you need", "A room with a power socket; a piano is welcome")],
             now=("Taking invitations", "Write with your room and a few dates that suit."),
             how_h2="From your email to a concert in your room.",
             steps=[("You tell us", "Write with the room, a date and who will be listening."),
                    ("We plan the music",
                     "We choose pieces your listeners can enjoy <mark>on first hearing</mark>."),
                    ("We come and play",
                     "We bring the musicians, instruments and stands, and play in your room.")],
             expect_h2="Before you invite us.",
             faq=[("Who plays?",
                   "<strong>Two or more musicians</strong>. <mark>Our founder</mark> plays clarinet or organ, with "
                   "musicians he invites or our Letters Ensemble."),
                  ("Are you insured?",
                   "<strong>Yes.</strong> We have <mark>public liability insurance</mark> and show the certificate on request."),
                  ("Where have you played?",
                   "<mark>Tallaght University Hospital</mark>, a care home, religious communities and parishes. See <a "
                   f'class="link" href="about.html#places">all {N_PLACES} places where we have played and '
                   "taught</a>.")],
             record_h2="Every concert.",
             record_lead="",
             next="Four or more concerts, with the Letters Ensemble and other musicians. Hope Concerts begin in "
                  "2027, and Ceol le Chéile from September.",
             next_link=("programmes.html#planned", "The lines planned for 2027"),
             join_h2="Invite us to play.",
             join_text="",
             join_btn="Invite us",
             mail=MAIL_INVITE,
             mail_fields=INVITE_FIELDS,
         )),
    dict(slug="recorder-ensemble", pillar="learn", name="Community Recorder Ensemble Class",
         short="Recorder Ensemble Class",
         icon="recorder", vocab="First notes · Scores · Harmony",
         img=("recorders.jpg", 1343, 1400, RECORDERS_ALT),
         # renamed 1 Oct 2026
         line="A weekly class for adults who have <mark>never played an instrument</mark>.",
         page=dict(
             lead="A weekly recorder class for adults. You play your first notes <mark>in week one</mark>.",
             meta="A recorder class for adults who have never played an instrument. Wednesday evenings, 7pm to 8pm, Mulhuddart Community Centre, Dublin 15. Recorders lent.",
             cap=("Recorders", "November 2025"),
             # the pilot ensemble on the founder's own channel; our still until play is pressed
             video=dict(kind="youtube", id="i7skwGKWSYY", poster="recorders.jpg",
                        cap=("The pilot ensemble", "Retired Presentation Sisters playing the recorder together."),
                        title="Video: the recorder pilot ensemble"),
             room_h2="Where the class began.",
             glance=[("For", "Adults who have never played an instrument"),
                     ("Where", "Mulhuddart, Dublin 15"),
                     ("When", "Wednesday evenings, 7pm to 8pm, ten weeks a term"),
                     ("What you need", "No instrument, and no need to read music")],
             now=("Running now", "<strong>Wednesday evenings, 7pm to 8pm</strong><span class=\"sr-only\">, </span>"
                                 "<span class=\"pp-where\">Mulhuddart Community Centre</span>"
                                 "<span class=\"sr-only\">. </span><span class=\"pp-come\">Just come along.</span>"),
             live=True,
             how_h2="From a first note to your own part.",
             # Andrew, 6 Oct 2026: he leads the class (in the join line it folded into two half lines)
             steps=[("Your first notes", "Our founder shows you how to hold the recorder, breathe and play."),
                    ("Reading from scratch",
                     "Notes and fingering, one at a time, with music we prepare for the class."),
                    ("Your own part",
                     "The group plays in harmony. The term ends with <mark>a small concert</mark> of our own.")],
             expect_h2="Before your first class.",
             # Andrew, 6 Oct 2026: join during the term; step-free; he leads the class (reading music is
             # in the glance and the steps, the pilot in the video and the record)
             faq=[("Do I need my own recorder?", "<strong>No.</strong> We can <mark>lend you one</mark>."),
                  ("Can I join during the term?", "<strong>Yes.</strong> Just come along <mark>any Wednesday</mark> at 7pm."),
                  ("Is the centre step-free?",
                   "<strong>Yes.</strong> Mulhuddart Community Centre has <mark>step-free access</mark>."),
                  # the Strategy's path to performing (G2-02)
                  ("What comes after the class?",
                   "Members who want more can join the <a class=\"link\" href=\"programmes/letters-ensemble.html\">Letters Ensemble</a> and give concerts.")],
             # For hosts (22 Oct 2026): the programme model, from CMFE_Recorder_Ensemble_Model. The class
             # runs 7pm to 8pm; the model's "about 75 minutes" is not repeated. "Nine enrolled, seven
             # completed" is the canonical pilot sentence (canon 2).
             model=dict(
                 label="For hosts",
                 h2="A ten-week term, for your place.",
                 lead="For centres, parishes, day centres, libraries and schools: <mark>what a host agrees to</mark>.",
                 facts=[("Shape", "Ten weekly sessions, then a short presentation"),
                        ("Group", "Up to ten adults"),
                        ("Instruments", "Recorders lent, with large-print music and alternatives"),
                        ("Led by", "A named facilitator, with the host&rsquo;s contact at the first session")],
                 pilot="The model comes from our pilot with retired Presentation Sisters in Dublin 8. Nine sisters "
                       "enrolled and seven completed the study&rsquo;s final questionnaire. The sisters began to practise "
                       "every day, of their own accord.",
                 weeks_summary="The ten weeks", weeks_hide="Hide the ten weeks",
                 weeks=[("Week 1 · First sounds.", "Names, a welcome circle, holding the instrument, breath, a first familiar tune on three notes."),
                        ("Week 2 · Playing together.", "A steady pulse, listening to each other, two more familiar tunes."),
                        ("Week 3 · Widening the range.", "New notes and short phrases. Groups often begin their own practice about now."),
                        ("Week 4 · Accompaniment.", "Playing with a piano, finding the beat in a fuller sound."),
                        ("Week 5 · Two parts.", "A melody and a second line, and a first look at dynamics."),
                        ("Week 6 · Pieces we chose.", "The programme takes shape from the group&rsquo;s request cards."),
                        ("Week 7 · A community piece.", "One piece from the host community&rsquo;s own tradition."),
                        ("Week 8 · Shaping.", "Beginnings, endings, who plays where, the running order."),
                        ("Week 9 · Rehearsal in the room.", "A run-through where the presentation will be, and invitations to guests."),
                        ("Week 10 · Full run.", "The whole programme, with time to talk about what comes next."),
                        ("Presentation.", "A short, relaxed concert for friends, family and neighbours, led by the participants.")],
                 host_summary="What a host provides", host_hide="Hide what a host provides",
                 host=[("A room.", "Warm, accessible, ideally on the ground floor, at the same time each week."),
                       ("A contact.", "A named person who helps invite people. We supply a flyer and a one-page description."),
                       ("Storage.", "Space for the instruments between sessions, or we take them each time."),
                       ("Safeguarding.", "We follow the venue&rsquo;s own arrangements and provide what the host asks for."),
                       ("A proposal.", "A costed proposal is available on request."),
                       ("Numbers.", "Up to ten participants, with a short waiting list if more are interested."),
                       ("How we begin.", "A call, a visit to the room, agreed dates, a written agreement, then the first session.")],
                 href=_MAIL_HOST, btn="Ask about hosting a class",
                 doc=("assets/docs/CMFE_Recorder_Ensemble_Model.pdf", "Programme model (PDF)"),
             ),
             record_h2="How the class came about.",
             record_lead="",
             next="A second class at St Columbanus, Loughlinstown, from January. It ends in June with a concert "
                  "with the parish choir.",
             next_link=("news.html#preparing", "Projects in preparation"),
             join_h2="Join the class.",
             join_text="<strong>Wednesday evenings, 7pm to 8pm</strong>, in Mulhuddart: just come along any week.",
             join_btn="Ask about the class",
             mail_hint="No need to write first. If you do, tell us:",
             mail_subject="Community Recorder Ensemble Class",
             mail_fields=["Your name",
                          "A phone number (optional)",
                          "Have you played an instrument before?",
                          "Do you need a recorder?",
                          "Any access needs (optional)"],
         )),
    dict(slug="letters-ensemble", pillar="share", name="Letters Ensemble",
         short="Letters Ensemble",
         icon="strings", vocab="Irish · Korean · Sacred",
         img=("letters-stpatricks.jpg", 1400, 1050, STPAT_ALT),
         line="<mark>Amateur musicians</mark> in Dublin who play for parishes and religious houses.",
         page=dict(
             lead="<mark>Amateur musicians</mark> in&nbsp;Dublin, together since 2024. We play Irish, Korean and sacred music.",
             meta="An amateur ensemble in Dublin since 2024, open to players of any background. We play Irish, Korean and sacred music for parishes and religious communities.",
             cap=("Letters Ensemble", "St Patrick&rsquo;s Day concert"),
             room_h2="On St Patrick&rsquo;s Day.",
             glance=[("For", "Amateur players of any background, students and early-career musicians"),
                     ("Where", "Dublin"),
                     ("When", "Ask us for rehearsal times"),
                     ("What you need", "An instrument you play")],
             now=("All players welcome", "Write with your instrument; we will send rehearsal times."),
             how_h2="Rehearse in Dublin, then give concerts.",
             steps=[("Tell us your instrument",
                     "Write with what you play. <mark>Any background</mark> is welcome, including our recorder class."),
                    ("Rehearse together",
                     "We rehearse in Dublin, directed by our founder, Andrew Seohyeon Kim."),
                    ("Give a concert",
                     "We give concerts for parishes, religious houses, care homes, venues and councils.")],
             expect_h2="Before you join.",
             faq=[("What does the ensemble play?",
                   "Pieces such as Mozart&rsquo;s &lsquo;Ave verum corpus&rsquo;, &lsquo;Down by the Sally Gardens&rsquo; and &lsquo;Arirang&rsquo;."),
                  ("Can I join if I stopped playing years ago?",
                   "<strong>Yes.</strong> Tell us what you play and <mark>when you last played</mark>."),
                  # the Strategy (p.12): rehearsals planned around about five players, more welcome
                  ("How big is the ensemble?",
                   "We plan rehearsals for <mark>about five players</mark>, and more are welcome."),
                  # the name, in the Strategy's words (p.12); the four concerts are the record below
                  ("Why &lsquo;Letters&rsquo;?",
                   "It is named after <mark>the letters A, B, C, D</mark>.")],
             record_h2="Four concerts.",
             record_lead="",
             next="Four concerts, one each season.",
             join_h2="Play with us.",
             join_text="",
             join_btn="Ask about joining",
             mail_subject="Joining the Letters Ensemble",
             mail_fields=["Your name",
                          "What you play",
                          "How long you have played",
                          "When you last played",
                          "Days and times that suit you"],
         )),
    # the canon's name since v7 (0-4 no. 11; "Concert Guide & Companion" until 1 Nov 2026)
    dict(slug="concert-companion", pillar="learn", name="Concert Companion",
         short="Concert Companion",
         icon="ticket", vocab="Before · During · After",
         img=("proms-hall.jpg", 1400, 933,
              "A full Royal Albert Hall during a BBC Prom, seen from high in the audience: the orchestra on a lit stage, beams of light and the acoustic discs overhead"),
         line="<mark>Small groups</mark> go to concerts together, with a guide.",
         page=dict(
             lead="For people who would rather not go to a concert alone. We prepare, <mark>go together</mark>, then "
                  "talk it over.",
             # the founder's own photograph from the audience at the BBC Proms; no group trip to the
             # Proms is on the record, so the caption says whose view it is. The month is the
             # recording date of the source video (Andrew, 1 Oct 2026)
             meta="Go to concerts in Dublin with a small group and a guide, especially if you have never been. Centres and community groups can ask for an outing.",
             cap=("BBC Proms, Royal Albert Hall", "London · September 2023 · photo: our founder, from the audience"),
             room_h2="The hall, from the seats.",
             # the Strategy (p.11): people who have never been to a concert
             glance=[("For", "Anyone new to concerts, or who would rather not go alone"),
                     ("Where", "Concert halls in Dublin"),
                     ("When", "As outings are planned"),
                     ("What you need", "No knowledge of music")],
             now=("Dates by email", "Write to us. We will tell you about the next outing."),
             how_h2="Before, during and after the concert.",
             steps=[("Prepare",
                     "We choose a concert and book seats with the venue. Then we go through the music."),
                    ("Go as a group", "A guide goes with the group and stays through the concert."),
                    ("Talk it over", "Afterwards we talk about what we heard, and there is <mark>no wrong answer</mark>.")],
             expect_h2="Before your first outing.",
             # who can ask (Strategy p.11, Catalogue); the concerts suggested are the record below
             faq=[("Can a centre or group ask for an outing?",
                   "<strong>Yes.</strong> Community groups and centres, including <mark>children&rsquo;s centres</mark> "
                   "and homeless services, can ask us."),
                  ("How big is a group?",
                   "In December 2025, <mark>six people</mark> went together to the National Concert Hall."),
                  ("I am new to Ireland. Is this for me?",
                   "<strong>Yes.</strong> We work in <mark>English and Korean</mark>.")],
             record_h2="Concerts we suggested.",
             record_lead="",
             next="At least two outings, and more with the help of other organisations.",
             join_h2="Join an outing.",
             join_text="",
             join_btn="Ask about an outing",
             mail_subject="Concert Companion",
             mail_fields=["Your name",
                          "Days and times that suit you",
                          "Music you like (optional)",
                          "Any access needs (optional)",
                          "Language you prefer: English or Korean"],
         )),
]

# The five in the canon's order and numbers (v7, 0-4 no. 11; request 20, 2 Nov 2026): 1 Getting to Know
# Classical Music, 2 Concert Companion, 3 the Community Recorder Ensemble Class, 4 Letters Ensemble,
# 5 Outreach Concerts. The covers' 01 to 05 are these numbers, so the site and the Strategy 2027-2030 and
# At a Glance 2027 number a programme the same way, and the three of Learning come before the two of Sharing.
# The lines planned for 2027 (A, B, C) are not programmes with a page: PROGRAMMES_T["planned"].
ORDER = ("getting-to-know", "concert-companion", "recorder-ensemble", "letters-ensemble", "outreach-concerts")
PROGRAMMES_DATA.sort(key=lambda q: ORDER.index(q["slug"]))


# Each page's email is written from the prompts it lists, so the two cannot
# differ (QA40-02: the class and the outings mailed one line fewer than they
# showed). Outreach Concerts uses MAIL_INVITE.
for _p in PROGRAMMES_DATA:
    _g = _p["page"]
    if "mail_subject" in _g:
        _g["mail"] = _mail(_g["mail_subject"], _fields(_g["mail_fields"]))


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------

# the five, under Programmes in the header (layout.PROG_MENU)
PROG_MENU["en"][:] = [(q["slug"], q["name"], q["page"].get("live", False)) for q in PROGRAMMES_DATA]

HOME = dict(
    hero=dict(
        eyebrow="Community music · Dublin, Ireland",
        title=["Classical Music,", '<span class="for">for </span><em>Everyone.</em>'],
        # under the title comes the master line (Andrew, 2 Oct 2026, evening), taken from
        # layout.STR, the same string the footer sets, so the two cannot drift
        cta=("#programmes", "See the programmes"),
        more=("get-involved.html#invite", "Invite us to play"),
        img=("ruared-duo.jpg", 1800, 1200, "A clarinettist and a pianist performing on the Rua Red stage"),
        cap=("Clarinet and piano", "Rua Red, Tallaght · August 2026 · photo: Ben Ryan / SDCC"),
    ),
    # the ways in, as the contents line of a programme (no boxes, no tint):
    # taking part comes first, because most visitors come to join something
    progs=dict(
        label="What we do",
        h2="Five programmes.",
        lead="Three help you listen and play; two bring music to people.",
        # the two ways in the cards do not cover, as two doors (Andrew, 3 Oct
        # 2026: inside two sentences they did not read as actions): the labels
        # of the doors on Get involved, and the action each leads to. Kit 27,
        # message 3: CMFE Artist Services is a plan, so the one thing open now is to
        # register interest (parts.door_pair)
        others=[("get-involved.html#play", "Artists", "Register your interest",
                 "Musicians and artists from any field, any time."),
                ("get-involved.html#board", "Volunteers", "Join the founding board",
                 "First members of an independent board.")],
    ),
    # kit 27 ①, the opening of the one-page case, set in three parts so the
    # answer stands out; Ireland rather than Dublin (Andrew, 1 Oct 2026). It
    # describes the need, not our reach: never "across Ireland".
    why=dict(
        label="Why we exist",
        premise="Many people in Ireland miss going to concerts, and still need the music.",
        reasons=["Some live <mark>in a nursing home</mark>.",
                 "Some <mark>rarely leave the house</mark>.",
                 "Some are <mark>new to the country</mark> and don&rsquo;t know where to begin."],
        resolve="So we go to <em>them.</em>",
        link=("get-involved.html#invite", "Invite us to play"),
    ),
    # The Strategy 2027-2030's three commitments (its page 2, Andrew 9 Nov 2026), each with the programmes that
    # keep it: (name, pillar, page or None, when it begins if it is still a plan). Artist Services stays "in
    # preparation" on the site (the Strategy calls it running; Cowork question, request 22).
    commitments=dict(
        label="Our promises",
        h2="Three commitments.",
        lead="Each programme keeps one of them.",
        items=[("We bring live music to you.",
                "To care homes, hospitals, parishes and counties, in the room where people already are.",
                [("Outreach Concerts", "share", "programmes/outreach-concerts.html", None),
                 ("Hope Concerts", "share", None, "From 2027"),
                 ("Ceol le Chéile", "share", None, "From September 2027")]),
               ("Anyone can play, at any age.",
                "Classes and talks that start from the very beginning.",
                [("Getting to Know Classical Music", "learn", "programmes/getting-to-know.html", None),
                 ("Community Recorder Ensemble Class", "learn", "programmes/recorder-ensemble.html", None),
                 ("Music for Inclusive Classrooms", "learn", None, "From September 2027")]),
               ("Musicians and communities meet here.",
                "Paid work for musicians, and a stage and a seat for everyone else.",
                [("Letters Ensemble", "share", "programmes/letters-ensemble.html", None),
                 ("Concert Companion", "learn", "programmes/concert-companion.html", None),
                 ("CMFE Artist Services", "share", None, "In preparation")])],
    ),
    # the need in four figures, each with its source (the Strategy's page 3), and the six groups the work is
    # for, folded (its pages 6 to 9). Public research only; no participant's age.
    need=dict(
        label="The need",
        h2="Music is for everyone. Many have no way to reach it.",
        figs=[("3", "Dublin council areas had no project in the national care-settings music scheme.",
               "Creative Ireland, 2024"),
              ("1 in 6", "adults went to no arts event at all in a year.", "Arts Council, Arts Insight 2024"),
              ("1.3%", "of adults aged 50 and over go to a concert, play or film in a typical week.",
               "TILDA, 2021"),
              ("13.6%", "of pupils fall in the borderline range, a group no school support has named since 2017.",
               "Wieland and Zitman, 2016")],
        groups_summary="Six groups we work for", groups_hide="Hide the six groups",
        groups=[("Older people in care homes and hospitals.",
                 "In a care study, 69% of residents responded to live music and 25% to recorded music (Holmes "
                 "2006). Outreach Concerts, Hope Concerts, Getting to Know."),
                ("People who rarely reach a concert hall.",
                 "Cost, time and too little choice nearby keep adults away (Arts Council 2025). Getting to Know, "
                 "Concert Companion, Ceol le Chéile."),
                ("Adults who never learned an instrument.",
                 "Few groups teach an instrument from the very beginning. The Community Recorder Ensemble Class."),
                ("Amateur and student players.",
                 "Belonging, a skilled leader and a concert to aim for keep a group going (Pearce 2015; Lamont "
                 "2018). Letters Ensemble, CMFE Artist Services."),
                ("Pupils with borderline or developmental needs.",
                 "Student-centred lessons and peer contact help inclusion in music (Mommo 2025). Music for "
                 "Inclusive Classrooms."),
                ("Migrants and newcomers.",
                 "12% of people living in Ireland are not Irish citizens (CSO 2022), with few ways into local "
                 "music. Concert Companion, the class, Letters Ensemble.")],
    ),
    numbers=dict(
        label="On the record",
        sr="In numbers",
        # what we did, where, how far (v7: the places are counted from About's list, never typed)
        # canon v2.0 0-4 no. 3 (request 20): "40+ community music programmes since 2024", never
        # "40+ talks and performances"; the dots are one a programme (the canon's own line), and the
        # site's dot grammar stays (R17: filled for the talks of Learning, open for the performances)
        figs=[(40, "community music programmes", "since 2024", True),
              (N_PLACES, "places where we have played and taught", "since 2024", False),
              (4, "countries: Ireland, France, the UK and Korea", "since 2024", False)],
        forty=dict(talks="{n} talks", perf="{n} performances",
                   period="On the record to October 2026, one dot for each programme"),
        # kit 27: a selection of the founder, said as such; the one outside
        # selection on the site, so it is not the quietest line in the band (v7)
        note="Our founder was selected for South Dublin Live 2026.",
        link=("news.html#record", "See the record, year by year"),
    ),
)


# ---------------------------------------------------------------------------
# ABOUT. The anchors #founder #run #places #identity are redirect targets.
# ---------------------------------------------------------------------------

ABOUT_T = dict(
    glance_sr="At a glance",
    head=dict(
        eyebrow="About",
        title=["About us."],
        # who, and how (request 20: "initiative" went with the old status sentence)
        lead="Community music in Dublin since 2024. We play and teach <mark>where music is needed</mark>.",
        img=("christmas-conducting.jpg", 1400, 1050, XMAS_ALT),
        cap=("Christmas concert", "Clondalkin Lodge, Dublin · December 2025"),
    ),
    glance=[("Started", "January 2024", "Dublin, Ireland"),
            ("What we run", "Five programmes", "in Learning and Sharing"),
            ("Where we have played", "Four countries", "Ireland, France, the UK, Korea"),
            # the status sentence in a cell (canon v2.0 0-4 no. 1): what we are preparing to be, and from when;
            # the sentence itself leads "How we are run" below
            ("From 2027", "Social enterprise", "Not-for-profit, a company limited by guarantee")],
    story=dict(
        label="Our story",
        h2="Since 2024.",
        # the site counts from the founding, January 2024 (Andrew, 1 Oct 2026). The canon's activity
        # sentence (0-4 no. 3) without its "more than 25 places": About counts its own list (N_PLACES)
        # the question the class began with (the Strategy 2027-2030, page 2), without the sister's age (§2)
        # and without "an audience became players" (Andrew, 6 Oct 2026, Q14: she was not one of the players)
        text=["We started in Dublin in January 2024, with our Letters Ensemble. Six people came to our "
              "first talk.",
              "Our recorder class began with a question. After a concert, a retired sister asked about the "
              "violin she played in 1950.",
              "Since 2024 we have run more than 40 <mark>community music programmes</mark>."],
        link="The full timeline",
    ),
    founder=dict(
        # the founder playing, not speaking: the lecture photograph showed a
        # projected slide with other recognisable people (art direction, 1 Oct 2026)
        img=("founder-playing.jpg", 1050, 1400,
             "Andrew Seohyeon Kim playing the clarinet in the chapel of Tallaght University Hospital"),
        cap=("Clarinet", "Chapel, Tallaght University Hospital · August 2026 · photo: Tallaght University Hospital"),
        label="The founder",
        name='<span class="nm">Andrew Seohyeon Kim</span>',
        # the canon's contact line: "Founder and Artistic Director" (v2.0 §1)
        role="Founder and Artistic Director",
        line="A clarinettist and organist, in Dublin since 2022.",
        # request 20 (canon v2.0 0-4 no. 5 and the Strategy 2027-2030): his two parishes as Music Director;
        # the pilot as the Strategy cites his dissertation (nine sisters enrolled, so not "all seven")
        facts=[("Degree", "BMus (Hons) in Performance, TU Dublin Conservatoire"),
               # a parish a line (a dot between them was left at a line end at 1440)
               ("Music Director", '<span class="sl">Our Lady of Dolours, Dolphin&rsquo;s Barn<span class="sr-only">;</span></span> '
                                  '<span class="sl">St Columbanus, Loughlinstown</span>'),
               # request 19 (4 Nov 2026): the CHMHE letter; Cowork's standard wording, no prize money, no date
               ("Award", "First Prize, CHMHE Undergraduate Dissertation Competition 2025&ndash;26"),
               # kit 25 / 27: the one outside selection, said as a selection of the founder (d4 r9)
               ("Selected for", "South Dublin Live 2026")],
        # more about him (the Strategy 2027-2030, page 3, 9 Nov 2026), folded as reference so the page keeps
        # its reading budget: the instruments, the parishes, the teaching, the Korean community, the
        # volunteering, the research and the courses (canon v2.0 0-4 no. 5; Venture Lab is "took part", never
        # "completed"). Interpreting and where he lives are left out. One item a line (sl).
        courses=("More about Andrew", "Hide",
                 [("Graduation research", "A ten-week recorder pilot with retired Presentation Sisters, 2026"),
                  ("Instruments", "Clarinet, organ, saxophone, piano and drums"),
                  ("Organist", "Every week since September 2022, in three Dublin parishes"),
                  ("Teaching", "Clarinet, saxophone, piano and theory at Greystones Music Academy"),
                  ("Korea and Ireland",
                   '<span class="sl">Concerts with Korean musicians in Ireland<span class="sr-only">;</span></span> '
                   '<span class="sl">Classical Music Meet Ups in Korean</span>'),
                  ("Volunteering", "With retired Columban missionaries at Dalgan Park, since 2022"),
                  ("Festivals",
                   '<span class="sl">ICA ClarinetFest 2024<span class="sr-only">;</span></span> '
                   '<span class="sl">Veronica Dunne International Singing Competition, 2025<span class="sr-only">;</span></span> '
                   '<span class="sl">Dublin International Piano Competition, 2025<span class="sr-only">;</span></span> '
                   '<span class="sl">Korea Festival in Ireland, 2025</span>'),
                  # a course a line (in one run "Safeguarding / Vulnerable Adults" parted at 1440)
                  ("Completed, 2026",
                   '<span class="sl">Introduction to Children First<span class="sr-only">;</span></span> '
                   '<span class="sl">Safeguarding Vulnerable Adults<span class="sr-only">;</span></span> '
                   '<span class="sl">Creating a Social Enterprise</span>'),
                  ("Took part", "Venture Lab start-up programme, TU Dublin, 2024&ndash;25")]),
    ),
    run=dict(
        label="How we are run",
        h2="Who decides, and what we promise.",
        # kit 27: the status sentence, exactly as written
        lead=STATUS,
        links=[("get-involved.html#board", "Join the founding board"),
               ("contact.html#privacy", "How we handle your details")],
        # canon v2.0 0-4 no. 8: three founding directors (chair, treasurer, secretary), five in 2027
        items=[("Who decides.",
                "An independent, unpaid board: three founding directors, then five in 2027."),
               ("Money.",
                "We do not ask for or accept gifts or pledges. Gifts open only after charity registration. "
                "We will never ask you to pay into <mark>a personal account</mark>."),
               # the consent ledger in one sentence (_build/photos.py: founder, sdcc, blurred, nobody, crowd)
               ("Photographs.", "Anyone you can recognise has agreed, or we blur their face."),
               # facts.md l.59, word for word, where families and partners decide (v7)
               ("Public liability insurance.", "We show the certificate on request.")],
        # the Strategy 2027-2030, pages 21 and 22 (9 Nov 2026), as reference: who is a member, what the
        # founder does, the advisory council (its participant seat is the 2030 goal, page 17), what the board
        # decides, and the year's cycle. The payments rule and the committees are internal and left out.
        more=("How the company will be run", "Hide",
              [("Members and directors.",
                "The members are the directors, one vote each. Directors are unpaid and give two to four hours "
                "a month."),
               ("The founder.",
                "Our Founder and Artistic Director leads the programmes and brings plans and reports to every "
                "board meeting."),
               ("An advisory council.",
                "Six people with music, care and community experience, meeting twice a year. A seat for a "
                "participant is our goal for 2030."),
               ("What the board decides.",
                "The strategy, the annual plan and budget; the mission, values and any new programme; prices "
                "and policies."),
               ("Each year.",
                "We plan in November and December, measure every session, report at every meeting and review "
                "in October.")]),
    ),
    # Our mission (request 20, canon v2.0 0-4 no. 2): the mission in its parts, each under the commitment it
    # serves (the Strategy's own pairing, canon §1); the vision and the five values folded as reference, so
    # the page keeps its reading budget (readability.PAGE_BUDGET)
    mission=dict(
        label="Our mission",
        h2="What we are here to do.",
        items=[("We bring live music to you.",
                "To care settings, schools, parishes and community spaces."),
               ("Anyone can play, at any age.", "People of any ability learn and play together."),
               ("Musicians and communities meet here.", "We pay our musicians fairly.")],
        more_summary="Our vision and five values", more_hide="Hide the vision and values",
        more=[("Vision.", "Live Classical Music is part of ordinary life in every community on the island of "
                          "Ireland, for people of any age, ability or background."),
              ("Dignity.", "Every person is met as a listener and a musician."),
              ("Accessibility.", "Music comes to people, at a time, place and price that work for them."),
              ("Accompaniment.", "We come back, and we go with people to music."),
              ("Community.", "Music is made together, so people meet and belong."),
              ("Hope.", "Regular music gives people something to look forward to.")],
    ),
    # Our plan (request 20, canon v2.0 0-4 nos. 7, 9 and 13; the Strategy 2027-2030's roadmap): the four
    # stages by their names, one station on each line of the page (styles.css .steps-4). The company in
    # November-December 2026, the board three then five (How we are run), charitable status applied for in
    # 2027, a first paid post from September 2027 only if agreements and grants cover it. "Across Ireland"
    # is the 2030 stage's name and is said as a target (readability.PERMITTED). No amounts: the budget
    # totals are in the Strategy, the site keeps the work. The six goals are folded under the stages.
    plan=dict(
        label="Our plan",
        h2="A foundation year, then three years of growth.",
        # one line on a laptop (R10: "Our company is to be formed / in November–December 2026." folded)
        lead="We form the company in November&ndash;December 2026.",
        steps=[("2027 · Foundation",
                "Charitable status applied for. A first paid post from September, if agreements and grants "
                "cover it."),
               ("2028 · Build", "Full care-visit circuits in Dublin, and our first annual report."),
               ("2029 · Widen",
                "All four Dublin council areas and eight counties. A coordinator and our first impact report."),
               ("2030 · Across Ireland",
                "Our target: concerts in twelve or more counties, and an external evaluation.")],
        goals_summary="Six goals for 2027 to 2030", goals_hide="Hide the six goals",
        goals=[("Presence.", "Live Classical Music in care settings, hospitals, parishes and counties, under "
                             "written agreements."),
               ("Participation.", "Groups where adults of any age, and from September 2027 pupils, learn and "
                                  "play together."),
               ("Inclusion and voice.", "Access and participants&rsquo; voices built into every programme."),
               ("Fair work for musicians.", "A paid, trained musician panel, and more performing work for "
                                            "musicians who need it."),
               ("Partnerships and income.", "Written agreements and a balanced mix of income."),
               ("Governance and accountability.", "A skilled independent board, sound policies and public "
                                                  "reporting.")],
        # the Strategy 2027-2030, pages 19 and 20 (9 Nov 2026): 2027 quarter by quarter and the work area by
        # area, folded as reference. One item a line (sl). The paid post and payroll lines are left out (§3),
        # and so are the budget figures.
        folds=[("2027, quarter by quarter", "Hide the quarters",
                [("January to March.",
                  '<span class="sl">First participant meeting</span> '
                  '<span class="sl">Loughlinstown class begins; Mulhuddart spring term</span> '
                  '<span class="sl">Haegeum week, 14&ndash;21 February</span> '
                  '<span class="sl">Hope Concert, Mater Hospital</span> '
                  '<span class="sl">Letters Ensemble spring concert</span>'),
                 ("April to June.",
                  '<span class="sl">Talks through the year</span> '
                  '<span class="sl">Chamber Series; a Mater Hospital visit, May</span> '
                  '<span class="sl">Letters Ensemble summer concert</span> '
                  '<span class="sl">Loughlinstown concert with the parish choir, June</span>'),
                 ("July to September.",
                  '<span class="sl">Inclusive Classrooms: a first term in one or two schools</span> '
                  '<span class="sl">First Ceol le Chéile counties chosen</span> '
                  '<span class="sl">Charitable status applied for</span>'),
                 ("October to December.",
                  '<span class="sl">Ceol le Chéile in its first four counties</span> '
                  '<span class="sl">Recitals by Hyelee Jung and Dr Soo-Jung Ann</span> '
                  '<span class="sl">Letters Ensemble autumn and winter concerts</span> '
                  '<span class="sl">The first year reviewed and the 2028 plan adopted</span>')]),
               ("Where the work grows, area by area", "Hide the areas",
                [("Dublin City.",
                  "In 2027, the haegeum week, the Chamber Series and Hope Concerts. Then care-home circuits, "
                  "school terms and a second recorder class."),
                 ("Fingal and Dublin 15.",
                  "In 2027, the Mulhuddart class and visits to Blanchardstown Library and Connolly Hospital. "
                  "Then school music in Dublin 15 and a second Fingal class."),
                 ("South Dublin.",
                  "In 2027, visits to Tallaght University Hospital after South Dublin Live 2026. Then care "
                  "seasons and a recorder class."),
                 ("Dún Laoghaire-Rathdown.",
                  "In 2027, the Loughlinstown class and its concert with the parish choir. Then care seasons and "
                  "two recorder classes."),
                 ("Beyond Dublin.",
                  "From September 2027, Ceol le Chéile in four counties. Eight by 2029, and twelve or more is "
                  "our target for 2030.")])],
        link=("get-involved.html#support", "How to help now"),
        doc=("assets/docs/CMFE_Business_Plan_Summary_2027.pdf", "Business plan summary (PDF)"),
    ),
    places=dict(
        label="Places",
        h2="Where we have played and taught.",
        # 08 §2: concerts introduced to participants, with group attendance organised
        lead=f"<mark>{N_PLACES} places</mark> in four countries, most of them in Dublin.",
        # every name is on the record (content review, 1 Oct 2026); grouped by
        # the kind of place, each with where it is; counts are derived
        groups=PLACES,
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
        h2="Why <em>Everyone</em> is in gold.",
        # the meaning is in the proportion (CLAUDE.md §1), so "for" stays in the sentence
        text="Our logo sets &lsquo;for&rsquo; small and &lsquo;Everyone&rsquo; large. We have to live up to "
             "that word.",
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
        lead="Most programmes <mark>need no experience</mark>. <a class=\"link\" href=\"contact.html\">Write to us</a>, and we will tell you how to start.",
    ),
    list_sr="The five programmes",
    # The lines planned for 2027 (request 20, canon v2.0 0-4 no. 11 and §5; request 19 no. 4): a section of
    # their own after the five, grouped by pillar under each pillar's line, joined to no running programme
    # (R19). A Music for Inclusive Classrooms, B CMFE Artist Services, C The Channel, the two strands of
    # Outreach Concerts (5a, 5b) and the second recorder class. The old "For artists" note ("CMFE Artists
    # is planned for 2027") lives on in line B, with the one thing open now: registering interest.
    planned=dict(
        # the Strategy's own heading for this page: "Projects in preparation for 2027"
        label="In preparation",
        h2="Planned for 2027.",
        pillar_lines=PILLAR_LINES,
        groups=[("learn", [
                    ("A second recorder class.",
                     "From January 2027, a weekly class for adults at St Columbanus, Loughlinstown. It ends in "
                     "June with a concert with the parish choir."),
                    ("Music for Inclusive Classrooms.",
                     "From September 2027, in one or two mainstream schools: music for pupils who learn "
                     "differently, planned with the class teacher."),
                    ("Three ways to run it.",
                     "A recorder ensemble, an instrumental ensemble, or a hands-on classroom of instruments, "
                     "rhythm and listening.")]),
                ("share", [
                    ("Hope Concerts.",
                     "From 2027, within Outreach Concerts: regular visits to the Mater Hospital and to care homes "
                     "and hospitals that ask, the same musicians returning."),
                    ("Ceol le Chéile (Music Together, in Every County).",
                     "From September 2027, the first four counties, with council arts offices: a school or "
                     "library visit, a care home and an&nbsp;evening&nbsp;concert."),
                    ("CMFE Artist Services.",
                     "Concerts we plan and produce for musicians and groups. First, recitals by soprano Hyelee "
                     'Jung and pianist Dr Soo-Jung Ann. <a class="link" href="get-involved.html#play">Register '
                     "your interest</a> any time."),
                    ("The Channel.",
                     "From January 2027, on Instagram and YouTube: weekly concert listings, a newsletter, a "
                     "monthly magazine and learning videos.")])],
        link=("news.html#preparing", "Projects in preparation for 2027"),
    ),
    # One path, many ways in (the Strategy's page 12, 9 Nov 2026): four stations, each with the programmes
    # that open it (name, page or None, when a plan begins, what you do there); the three ways in from the
    # side under the path. Programme numbers are left out: the cover numbers are the site's (R33).
    path=dict(
        # not the drawing taken off in v7 (one programme's story): every programme, as equals (§2.1)
        label="How it fits together",
        h2="One path, many ways in.",
        lead="Many people first meet us at a concert, then listen, join, play and perform.",
        stations=[("Listen", [
                      ("Getting to Know", "programmes/getting-to-know.html", None, "A talk with live playing."),
                      ("Concert Companion", "programmes/concert-companion.html", None, "Going to a concert together.")]),
                  ("Join", [
                      ("Recorder Class", "programmes/recorder-ensemble.html", None, "Start each week as a beginner."),
                      ("Inclusive Classrooms", None, "From September 2027", "A small group in school.")]),
                  ("Play", [
                      ("Recorder Class", "programmes/recorder-ensemble.html", None, "Play in the ensemble and the term&rsquo;s concert."),
                      ("Letters Ensemble", "programmes/letters-ensemble.html", None, "Rehearse with the ensemble.")]),
                  ("Perform", [
                      ("Letters Ensemble", "programmes/letters-ensemble.html", None, "Concerts for parishes and venues."),
                      ("Inclusive Classrooms", None, "From September 2027", "A shared performance at the end of term.")])],
        notes=[("We come to you.",
                "Care homes, hospitals and parishes often meet us at an Outreach Concert, then book a talk or "
                "host a class."),
               ("Behind the scenes.", "CMFE Artist Services will plan and produce concerts for musicians and groups."),
               ("Staying in touch.", "From January 2027, our channel on Instagram and YouTube points to the next concert.")],
    ),
    # 2027, one dot for each talk, session, concert, visit or day (the Strategy's page 13): (name, pillar,
    # how many dots, what they are). No total: the Strategy's own total counts more than these rows.
    year=dict(
        label="The year ahead",
        h2="2027, one dot each.",
        lead="A dot is a talk, a session, a concert, a visit or a day we plan.",
        rows=[("Getting to Know", "learn", 10, "10 talks"),
              ("Concert Companion", "learn", 2, "2 outings or more"),
              ("Recorder Class", "learn", 20, "20 sessions: two classes of ten a term"),
              ("Inclusive Classrooms", "learn", 2, "Up to 2 schools, from September"),
              ("Letters Ensemble", "share", 4, "4 concerts, one each season"),
              ("Outreach Concerts", "share", 4, "4 concerts or more"),
              ("Hope Concerts", "share", 9, "9 visits"),
              ("Ceol le Chéile", "share", 4, "4 counties, from September"),
              ("CMFE Artist Services", "share", 2, "2 recitals")],
        note="This is our plan for 2027. Plans can change.",
    ),
)


# ---------------------------------------------------------------------------
# GET INVOLVED. Anchors: #invite (old Partner page), #play (CMFE Artist Services),
# #support and #board (old Support page), #join. #friends and #sponsor exist
# only while giving is open (layout.OPEN_GIVING).
# ---------------------------------------------------------------------------

GET_INVOLVED_T = dict(
    head=dict(
        eyebrow="Get involved",
        title=["Ways to get involved."],
        lead="<mark>One line by email</mark> is enough to start.",
    ),
    ways_label="Four ways",
    # four doors (2 Oct 2026 night): who each way is for, then the heading of
    # the section it leads to, then what is there (parts.doors)
    ways=[("programmes.html", "Anyone", "Join a programme", "Five programmes"),
          # the approved action (R8), as in the footer and on the home page: one line, like the others
          ("#invite", "Venues", "Invite us to play", "What it takes"),
          ("#play", "Artists", "Perform with us", "Example programmes"),
          ("#board", "Volunteers", "Join the founding board", "The roles")],
    # the address and phone under each mail button
    alt=dict(or_write="Or write to", email=EMAIL, tel="+353 83 078 0635", tel_href="+353830780635"),
    invite=dict(
        label="Venues",
        h2="Bring a concert to your place.",
        # the Service Catalogue (4 Nov 2026): who hosts or commissions
        lead="Care settings, parishes, libraries, schools, councils and festivals <mark>can invite us</mark>.",
        pair_labels=("You provide", "We bring"),
        pairs=[("A concert",
                ["A room with a power socket", "A date", "A contact person", "Responsibility for audience safety"],
                ["The musicians", "Instruments and stands", "Music chosen for your listeners",
                 "Public liability insurance"]),
               ("A recorder class",
                ["A warm room each week", "A contact person", "Help letting local people know"],
                ["Recorders to lend", "Music and teaching, as funding allows"])],
        # kit 02 §2 and 29: what a host gives, and what we can promise
        # the same three steps as the Outreach Concerts page
        href=MAIL_INVITE, btn="Invite us", more="How a concert works",
        # the Strategy 2027-2030 (9 Nov 2026): 45 to 60 minutes, with two or more musicians (in place of
        # Andrew's "one to two hours" of 6 Oct 2026, Q4: the newer document wins, §00 Cowork rule)
        hub_notes=["45 to 60 minutes", None],
        class_href=_MAIL_HOST,
        class_go="Ask about hosting a class",
    ),
    # Partner with us (22 Oct 2026): the corporate menu, summarised. No amounts: quotations on request.
    # "partner" only where a written agreement exists; gifts and matched giving wait for registration
    # (Charities Act 2009 s.41). Nine options: six open now, three later.
    companies=dict(
        label="Partner with us",
        h2="Work with us as a company.",
        lead="Nine ways to take part, <mark>six open now</mark>, each agreed in writing first.",
        items=[("Workplace concert.",
                "A 45-&#8288;minute lunchtime talk with live playing, under a written service agreement. Quotation on request."),
               ("Staff volunteering.", "Welcome and seat audiences at public concerts and class presentations."),
               ("Promotion.", "Share accurate wording and consented photographs through your own channels.")],
        later="Concert sponsorship and series partnerships follow once our company bank account is open. "
              "Gifts and matched giving wait until after charity registration.",
        menu_summary="All nine options", menu_hide="Hide the nine options",
        menu=[("Workplace concert.", "A lunchtime talk with live playing at your workplace. Open now."),
              ("Concert sponsorship.",
               # request 20: no "not yet" line about ourselves; what it waits for, said forward
               "Your company supports one visit or concert and is named in the programme. Opens once our "
               "bank account and written terms are in place."),
              ("Series partner.",
               "A season of visits at one setting, with recognition agreed in writing. We talk now, so a season "
               "can begin in 2028."),
              ("Staff volunteering.", "Real tasks at public concerts. Open now."),
              ("In kind.", "Instruments, printing, tuning, refreshments or equipment hire. Open now."),
              ("A venue.", "Your space for rehearsals, classes or public concerts. Open now."),
              ("Promotion.", "Your newsletter and notice boards. We do not buy advertising. Open now."),
              ("Pro bono advice.", "Accounting or legal help, with a written brief, one contact and an end date. Open now."),
              ("Matched giving.", "Opens only after charity registration.")],
        how_summary="How we work with companies", how_hide="Hide how we work",
        how=[("The programme is ours and the host&rsquo;s.", "A company does not choose the performers or who takes part."),
             ("No selling.", "Companies do not promote products to the people we play for."),
             ("Writing first.", "Terms are signed for the company by two directors.")],
        href=_MAIL_CO, btn="Ask about working together",
    ),
    # Andrew, 2 Oct 2026: take interest freely, from any field, at any time;
    # vetting depends on the venue; show example programmes (from the record)
    # the canon's name for line B (v7, 0-4 no. 11); what is planned for 2027 is the Strategy's: a paid panel of
    # 15 musicians (G4) and concerts planned and produced for musicians (line B). Still a plan on the site
    # (request 20): the 2026 concerts the Strategy lists under it were the founder's own selection (canon §2)
    play=dict(
        # the margin label in its short form (at 1024 "CMFE Artist Services" ran within 60px of the heading, one
        # phrase in two faces, typeset_check faces); the full name is the plan line's and the mail subject's
        label="Artist Services",
        h2="Perform with us.",
        lead="We are ready to work with musicians and artists <mark>from any field</mark>, at any time.",
        facts=[("For", "Students, emerging, amateur and professional artists"),
               ("How", "A few lines about you, and a link to your work"),
               ("Garda vetting", "May be needed, depending on the venue"),
               ("Planned<span class=\"sr-only\"> for 2027</span>",
                "A paid panel of 15 musicians, and concerts we plan and produce")],
        examples_label="Example programmes",
        # each one is on the record (ledger.py, public labels): the kind of
        # place, never a liturgy or a private occasion; newest first
        examples=[("An autumn concert in a church", "Soprano, haegeum, clarinet and piano", "September 2026"),
                  ("Christmas in a care home", "Clarinet and string trio", "December 2025"),
                  ("A homeless hostel", "Organ and clarinet", "July 2025"),
                  ("St Patrick&rsquo;s Day in a religious community", "Korean traditional ensemble and clarinet",
                   "March 2025")],
        href=_MAIL_EOI, btn="Register your interest",
    ),
    # Support (22 Oct 2026, canon v1.7 0-3 no. 11): before registration only what is not a gift. We call an
    # organisation a partner only once there is a written agreement.
    # Prepared, not shown: layout.OPEN_DOCS is False until Andrew decides which PDFs go public (22 Oct 2026).
    docs=dict(
        label="Read more",
        h2="The plans in full.",
        lead="Short documents for councils, funders, companies and hosts.",
        summary="The six documents", hide="Hide the documents",
        items=[("assets/docs/CMFE_One_Page_Summary.pdf", "One-page summary", "What we do, who we work with, how to take part."),
               ("assets/docs/CMFE_Business_Plan_Summary_2027.pdf", "Business plan summary 2027", "How it runs, how it is governed, how we measure it."),
               ("assets/docs/CMFE_Corporate_Support_Menu.pdf", "Corporate support menu", "Nine ways for a company to take part."),
               ("assets/docs/CMFE_Support_Proposal_2027.pdf", "Support proposal 2027", "What we ask now, and what waits for registration."),
               ("assets/docs/CMFE_Development_Roadmap_2027-2030.pdf", "Development roadmap 2027 to 2030", "Three stages and what each needs."),
               ("assets/docs/CMFE_Recorder_Ensemble_Model.pdf", "Recorder ensemble model", "The ten-week programme, for hosts.")],
    ),
    support=dict(
        label="Support",
        h2="Help now, in practical ways.",
        lead="<mark>Rooms, skills and introductions</mark> help most while we set up.",
        routes=[("Programme partner.", "Host a season of visits or a class, under a written agreement."),
                ("Service agreement.", "Commission music education or visiting concerts. Quotations on request."),
                ("A room.", "Lend a step-free space for a class or a concert."),
                ("In kind.", "Instruments, printing, tuning, storage or volunteer hosts."),
                ("Your skill.", "Pro bono law, accounting, safeguarding, evaluation or translation."),
                ("An introduction.", "To a care setting, a council arts officer or a hospital arts team."),
                ("Register interest.", "Contact only. We ask for nothing more.")],
        note="We call an organisation a partner only once the agreement is written. We do not ask for or accept "
             "gifts or pledges. Gifts open only after charity registration.",
        href=_MAIL_INTEREST, btn="Register your interest",
        board_label="Help us build it",
        # canon v2.0 0-4 no. 8 (request 20): three founding directors (chair, treasurer, secretary) in 2026,
        # five in 2027 with the safeguarding and care seat and the community seat; unpaid; two to four hours a
        # month (the Strategy 2027-2030). The seats are counted now that the canon counts them (R19 kept:
        # the drawing shows the five seats the sentence names). No candidate is ever named.
        board=dict(
            h2="Join the founding board.",
            lead="Three founding directors in 2026, then five in 2027: an <mark>independent, unpaid</mark> board.",
            facts=[("Roles", "Chair, treasurer and secretary; from 2027, safeguarding and care, and community"),
                   # the Founding Board Invitation: "2 to 4 hours a month"; "Reasonable expenses are reimbursed"
                   ("Conditions", "Unpaid, two to four hours a month, with reasonable expenses")],
            # the same roles, one a seat at the drawn table (parts.table): the Strategy's five seats
            roles=["Chair", "Treasurer", "Secretary", "Safeguarding and care", "Community"],
            # what each seat asks, and when it is filled (the Strategy 2027-2030, page 21), folded
            needs=("What each role asks", "Hide",
                   [("Chair, during 2026.", "Experience of leading a board, an arts organisation or a community body."),
                    ("Treasurer, during 2026.", "Finance or accounting: budgets, accounts and controls."),
                    ("Secretary, during 2026.", "Governance and company records: minutes, filings and policies."),
                    ("Safeguarding and care, during 2027.",
                     "Experience in care, health, disability or education settings."),
                    ("Community, during 2027.", "Someone from the communities and parishes we serve.")]),
            href=_MAIL_BOARD, btn="Ask about a role",
        ),
    ),
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
    pillar_lines=PILLAR_LINES,
    crumbs_label="Breadcrumb", crumb="Programmes",
    how_label="How it works", expect_label="What to expect", record_label="On the record",
    join_label="Take part", others_label="The other programmes", all_label="All five programmes",
    room_label="In the room", room_h2="Where it happens.",
    how_join="How to take part",
    # the Strategy's 2027 line under each record (9 Nov 2026)
    next_label="In 2027",
    video_h="Watch", video_label="Video: {name}", play="Play the video", watch="Watch on {service}",
    people="{n} people",
    mail_hint="One line is enough. If it helps, tell us:",
    or_write="Or write to", email=EMAIL, tel="+353 83 078 0635", tel_href="+353830780635",
    strip=dict(aria="{n} entries on the record for this programme, shown month by month from 2024 to 2026.",
               learn="Learning", share="Sharing", bar="A bar spans several months.",
               dot={"getting-to-know": "A dot is one talk.", "outreach-concerts": "A dot is one concert.",
                    "recorder-ensemble": "A dot is one date.", "letters-ensemble": "A dot is one concert.",
                    "concert-companion": "A dot is one concert."}),
    earlier="Show {n} earlier entries", earlier_hide="Hide earlier entries",
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
        title=["News and the record."],
        # 40+ since 2024; the forty-two on the record to October 2026 are 18 + 20 + 1 + 3 (Andrew, 29 Oct 2026)
        lead="<mark>Every talk and performance</mark> since 2024.",
    ),
    latest_sr="Latest",
    # request 19 (4 Nov 2026, Andrew said yes to a news item): the award takes the first panel and the
    # 19 September concert leaves the three (it stays in the record below); Cowork's wording, no money, no date of a talk
    latest=[("Award", "November 2026",
             "Our founder&rsquo;s recorder pilot study",
             "First Prize, CHMHE Undergraduate Dissertation Competition 2025&ndash;26.",
             "about.html#founder",
             "About our founder"),
            ("Board", "Autumn 2026",
             "A founding board",
             "We are looking for volunteers to serve on the first board.",
             "get-involved.html#board",
             "Board roles"),
            ("Class", "Autumn 2026",
             "Community Recorder Ensemble Class",
             "Wednesday evenings, 7pm to 8pm, at Mulhuddart Community Centre.",
             "programmes/recorder-ensemble.html",
             "About the class")],
    # projects in preparation for 2027 (the Strategy 2027-2030, page 14, 9 Nov 2026): each a plan, with the
    # venues and musicians named (Andrew, 9 Nov 2026) and no grant, funder or application named; the line
    # with the two embassies is left out (in discussion). (when, title, line, [(label, parts with " · ")])
    preparing=dict(
        label="Coming in 2027",
        h2="Projects in preparation.",
        lead="Each grows from work we have already done.",
        items=[("14&ndash;21 February 2027", "Two Traditions: A Haegeum Week",
                "Korean haegeum and Irish uilleann pipes on one stage, with two new pieces.",
                [("Where", "TU Dublin Concert Hall, 16 February · Mater Hospital, 17 February · "
                           "St Andrew&rsquo;s, Westland Row, 19 February"),
                 ("With", "Jieun Kim, haegeum · Mark Redmond, uilleann pipes · Dr Soo-Jung Ann, piano · "
                          "Andrew Seohyeon Kim, clarinet")]),
               ("May and September 2027", "Chamber Series",
                "Korean musicians who live in Dublin, playing in their own city.",
                [("Concerts", "&lsquo;One Voice&rsquo;, Church of the Three Patrons, Rathgar · A piano recital by "
                              "Dr Soo-Jung Ann, St Andrew&rsquo;s"),
                 ("Visits", "Mater Hospital · Our Lady of Dolours"),
                 ("With", "Dr Soo-Jung Ann · Hyelee Jung · Andrew Seohyeon Kim")]),
               ("2027&ndash;28", "New music for two traditions",
                "One Irish and one Korean composer each write a piece for haegeum, uilleann pipes, clarinet and "
                "piano.",
                [("Heard", "First in Dublin, then in Korea"),
                 ("With", "Mark Redmond · Jieun Kim")]),
               ("January to June 2027", "Loughlinstown Recorder Ensemble",
                "A weekly class for adults from January, ending before summer in a concert.",
                [("Where", "St Columbanus, Loughlinstown"),
                 ("With", "The parish of St Columbanus · The parish choir and a guest trio, at the concert")]),
               ("2027", "Music in Dublin 15",
                "The Mulhuddart class goes on, with visiting concerts in Dublin 15.",
                [("Where", "Blanchardstown Library, during Bealtaine · Connolly Hospital · A hospice · "
                           "A local venue"),
                 ("Trio", "Dr Soo-Jung Ann · Hyelee Jung · Andrew Seohyeon Kim")]),
               ("2027", "Two recitals",
                "Our first recitals produced by CMFE Artist Services.",
                [("Soprano", "Hyelee Jung, with Landon Ronald&rsquo;s <cite>A Cycle of Life</cite>"),
                 ("Piano", "Dr Soo-Jung Ann")])],
        note="Dates and places are plans, and may change.",
        link=("programmes.html#planned", "The lines planned for 2027"),
    ),
    chart=dict(
        label="The record",
        h2="Forty-two, by year.",
        lead="Every talk and performance, with what it was and where.",
        figs=[(18, "talks", "talk"),
              (20, "outreach performances", "perf"),
              (1, "pilot concert", "perf"),
              (3, "South Dublin Live 2026 concerts", "perf")],
        period="January 2024 &ndash; October 2026",
        year_count="{n} talks and performances",
        year_talks=("{n} talk", "{n} talks"),
        year_perf=("{n} performance", "{n} performances"),
        year_more="Show all {n} from {y}", year_less="Hide {y}",
        row_talk="Talk",
        row_perf="Performance",
    ),
    timeline=dict(
        label="Timeline",
        h2="How it grew.",
        years=[("2024", [("January", "It starts",
                          "We started in Dublin, with the Letters Ensemble. <mark>Six people</mark> came to the first talk."),
                         ("Through the year", "Beyond Dublin",
                          "Concerts in Co. Meath, Co. Wicklow, London, Paris and Daegu.")]),
               ("2025", [("Through the year", "Into care settings",
                          "Concerts at a day service, a homeless hostel and a care home."),
                         ("Autumn", "Introducing concerts",
                          "We started introducing concerts to participants and organising group attendance."),
                         # canon v2.0 0-4 no. 4 and §2: nine enrolled, seven completed the final questionnaire
                         ("October", "Preparing the recorder pilot",
                          # one sentence: "Nine retired" alone made a short first line on a phone (typeset_check steps)
                          "With retired Presentation Sisters: <mark>nine enrolled</mark>, each with individual "
                          "lessons and her own part."),
                         ("December", "At the National Concert Hall",
                          "The fifteenth&nbsp;talk was a concert we heard together.")]),
               ("2026", [("January to&nbsp;April", "The recorder pilot",
                          "Ten weekly rehearsals at Warrenmount, then <mark>an Easter concert</mark> at Clondalkin "
                          "Lodge."),
                         ("August", "South Dublin Live",
                          # one sentence: "Our founder was selected." alone was a short first line on a phone (typeset_check steps)
                          "Our founder was selected to play twice at the hospital, once at Rua Red."),
                         ("September", "An autumn concert",
                          "In Ranelagh, Dublin 6, at Methodist Centenary Church."),
                         ("Autumn", "Open to the public",
                          "The class, based on the pilot, meets <mark>every Wednesday</mark> in Mulhuddart.")])],
    ),
    gallery=dict(
        label="Photographs",
        h2="In the room.",
        lead="From our concerts and rehearsals, newest first.",
        more="Show {n} earlier photographs", less="Hide earlier photographs",
        # newest first, a contact sheet: every frame at its own shape, with a true caption
        rows=[
            (("tuh-trio.jpg", 1236, 787,
              "Soprano, piano and clarinet in the atrium of Tallaght University Hospital"),
             "Atrium · Tallaght University Hospital · August 2026 · photo: Tallaght University Hospital"),
            (("tuh-atrium.jpg", 1400, 1052, TUH_CHAPEL_ALT),
             "Chapel · Tallaght University Hospital · August 2026 · photo: Tallaght University Hospital"),
            (("tuh-haegeum.jpg", 1400, 934, "A haegeum player performing in a hospital atrium"),
             "Haegeum · Tallaght University Hospital · August 2026 · photo: Tallaght University Hospital"),
            (("ruared-trio.jpg", 1400, 933, "A clarinettist, a soprano and a pianist standing together on the Rua Red stage"),
             "Clarinet, soprano and piano · Rua Red, Tallaght · August 2026 · photo: Ben Ryan / SDCC"),
            (("ruared-back.jpg", 1400, 933,
              "A clarinettist, seen from behind, playing towards a soprano on the Rua Red stage"),
             "Clarinet and soprano · Rua Red, Tallaght · August 2026 · photo: Ben Ryan / SDCC"),
            (("christmas-conducting.jpg", 1400, 1050, XMAS_ALT),
             "Conducting · Clondalkin Lodge, Dublin · December 2025"),
            (("rehearsal-stand.jpg", 1050, 1400, "A string trio rehearsing behind a part on a music stand"),
             "Rehearsal · Christmas 2025"),
            (("recorders.jpg", 1343, 1400, RECORDERS_ALT),
             "Recorders · November 2025"),
            (("church-aisle.jpg", 1050, 1400,
              "A clarinet held up before the altar of a parish church in Co. Westmeath"),
             "Clarinet before the altar · Dysart, Co. Westmeath · 2025"),
            (("goirtin-solo.jpg", 1120, 1400, GOIRTIN_ALT),
             "Clarinet solo · a day service, Dublin 7 · April 2025"),
            (("dalgan-hall.jpg", 1400, 1050,
              "A hall set out with chairs and music stands before a concert, with no one there yet"),
             "The hall before the concert · Dalgan Park, Co. Meath · March 2024"),
            (("letters-stpatricks.jpg", 1400, 1050, STPAT_ALT),
             "Letters Ensemble · St Patrick&rsquo;s Day concert"),
            (("two-clarinets.jpg", 1050, 1400, "Two clarinets resting on the lid of a piano"),
             "Two clarinets on a piano"),
        ],
    ),
)

NEWS = P.news(NEWS_T, L, PROGRAMMES_DATA)


# ---------------------------------------------------------------------------
# CONTACT, with the privacy notice (kit 06: a privacy notice on the website)
# ---------------------------------------------------------------------------

CONTACT_T = dict(
    head=dict(
        eyebrow="Contact",
        title=["Write to us."],
        # each sentence fits its column on a laptop (chief designer, typography
        # pass: the old pair folded into four half lines); now as the Korean says
        lead="Choose a topic below, or simply write. We reply <mark>as soon as we can</mark>.",
    ),
    # one form, a topic to choose (Andrew, 2 Oct 2026, evening). It is a mailto form: the
    # visitor's own email app opens with the subject and the message; nothing passes through
    # this site. Each topic shows what helps us answer (the same prompts as the mail buttons).
    # research (2 Oct 2026): radios, not a dropdown (GOV.UK), named "subject" with today's
    # subject lines as values; one textarea named "body"; nothing required; the button says
    # what happens. A mailto URL stays safe under about 2,000 characters.
    form=dict(
        h2="Contact form",
        topic_label="What is it about?",
        topics=[("part", "Taking part", "Taking part in a programme",
                 ["Which programme interests you", "How we can reach you"]),
                ("venue", "Concert invitation", "A venue, school or council: invite us", INVITE_FIELDS),
                ("work", "Working with a company: Classical Music for Everyone", "A company or organisation: work with us",
                 ["Company or organisation and town", "What interests you", "Contact name and phone number"]),
                ("artist", "CMFE Artist Services: expression of interest", "An artist: register interest", EOI_FIELDS),
                ("board", "Founding board: Classical Music for Everyone", "The founding board",
                 ["Which role interests you", "A few lines about you"]),
                ("data", "Personal data request", "Your details: see, correct or delete",
                 ["Whether you want to see, correct or delete your details"]),
                ("other", "Enquiry: Classical Music for Everyone", "Anything else", [])],
        helps="Helpful to include:",
        general="A few lines are enough. Pick a topic to see what to include.",
        message_label="Your message",
        button="Open in my email app",
        # "keep it short" is always in view, beside the button (chief designer v2: a mailto
        # address over about 2,000 characters may not open at all)
        note="Keep it short here: you can finish and send it in your email app. If nothing opens, write to",
    ),
    direct_label="Or phone",
    email=EMAIL,
    email_href=_mail("Enquiry: Classical Music for Everyone"),
    tel="+353 83 078 0635",
    tel_href="+353830780635",
    details_label="Details",
    details_h2="Where we travel, and who answers.",
    # Insurance: the certificate is in hand (1 Oct 2026). Garda vetting is not
    # mentioned until it is complete. We travel to (Andrew, 2 Oct 2026 night): a
    # need, not a territory. The counties on the record stay on About and in
    # areaServed; never "across Ireland".
    details=[("Based in", "Dublin, Ireland"),
             ("We travel to", "Wherever music is needed"),
             ("Languages", 'English · <span lang="ko">한국어</span>'),
             ("Insurance", "Public liability insurance. We show the certificate on request."),
             # a signature: the name on its own line, then the role (R23)
             ("Who answers", '<span class="sl">Andrew Seohyeon Kim</span> '
                             '<span class="sl">Founder and Artistic Director</span>')],
    privacy=dict(
        label="Privacy notice",
        h2="How we look after your details.",
        intro="Last updated 2 November 2026.",
        # what this website does not have, said once and plainly
        # the contact form is a mailto form: it sends nothing itself (2 Oct 2026)
        none=[("Forms", "One, and it only opens your email app"), ("Cookies", "None of ours"),
              ("Analytics", "None"), ("Advertising", "None")],
        blocks=[("Who is responsible",
                 "p",
                 # request 20: the old status wording ("a not-for-profit community music initiative") went
                 '<span class="brandname">Classical Music for Everyone</span>, based in Dublin. For anything '
                 'about your details, write to <a class="link" '
                 'href="mailto:sby05034@gmail.com">sby05034@gmail.com</a>.',
                 ""),
                ("When you email us",
                 "list",
                 ["We use what you send <mark>only to reply</mark> and to do what you asked.",
                  "We <mark>never sell it</mark>, and only the services listed below handle it for us.",
                  "Telling us about access needs is optional."],
                 ""),
                ("Who else handles it",
                 "rows",
                 [("GitHub", "Hosts this site and records IP addresses for security"),
                  ("Google", "Runs our email"),
                  ("YouTube", "If you play the class video, it receives your IP and may set cookies")],
                 "These services may handle data outside the European Economic Area, under safeguards "
                 "approved by the EU."),
                ("Your rights",
                 "list",
                 ["You can ask to see, correct or delete what we hold about you.",
                  "You can ask us to restrict how we use it, or object to it.",
                  "You can ask for a copy.",
                  "You can ask for any of these <mark>at any time</mark>."],
                 'If you are not happy with our answer, you can complain to the <a class="link" '
                 'href="https://www.dataprotection.ie/">Data Protection Commission</a>.')],
    ),
)

CONTACT = P.contact(CONTACT_T)
