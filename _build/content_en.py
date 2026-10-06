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
                    "The role that interests me (chair, treasurer, secretary, safeguarding and care "
                    "lead, community lead): \r\nA few lines about me: \r\n")

# CMFE Artists: interest is taken freely (Andrew, 2 Oct 2026). Four prompts
# in place of the kit 15 form: whoever writes can say the rest in their own words.
EOI_FIELDS = ["Your name", "Instrument, voice or art form", "A link to your work (optional)",
              "A few lines about you"]
_MAIL_EOI = _mail("CMFE Artists: expression of interest", _fields(EOI_FIELDS))


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
         img=("lecture-recital.jpg", 1050, 1400, "Our founder giving a talk, with a slide about the BBC Proms on the screen"),
         line="Talks with <mark>live music</mark>, for anyone curious about Classical Music.",
         page=dict(
             lead="We give talks on Classical Music, with <mark>live playing</mark>. They are for anyone curious to "
                  "hear more.",
             cap=("A talk on the BBC Proms", "Dublin"),
             glance=[("For", "Anyone curious about Classical Music"),
                     ("Where", "Dublin"),
                     ("When", "A date we agree with you"),
                     ("What you need", "No knowledge of music")],
             now=("On request", "Write to us, on your own or as a group."),
             # 02 §4: three stages, in this order; 08 §1 for what each covers
             how_h2="Three stages, from first listening to your own taste.",
             steps=[("Getting Closer",
                     "What Classical Music is, by period and by instrument, with recordings and live "
                     "playing."),
                    ("Together",
                     "Orchestras and performers, including Ireland&rsquo;s own. How to book a ticket and "
                     "choose a seat."),
                    ("My Taste",
                     "Finding <mark>what you like</mark>, for example by hearing one piece played by five pianists.")],
             expect_h2="Before your first talk.",
             faq=[("Do I need to know anything first?",
                   "<strong>No.</strong> We start from &lsquo;what is Classical Music?&rsquo; and "
                   "<mark>explain every piece</mark> we play."),
                  ("How many people come?",
                   "Between <mark>six and fourteen</mark> people came to each talk we counted. The chart below shows those counts."),
                  ("Can our group ask for a talk?",
                   "<strong>Yes.</strong> Tell us your group, roughly how many people and where you could meet.")],
             record_h2="Talks so far.",
             record_lead="Every talk on the record, with its date, topic and place.",
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
         img=("care-christmas.jpg", 1400, 1050, CARE_ALT),
         line="Live Classical Music in <mark>care homes</mark>, hospitals, parishes and community centres.",
         page=dict(
             # each lead sentence fits its column on a laptop (typeset_check:
             # the longer first sentences folded into half lines)
             lead="We play in the rooms where <mark>people already are</mark>. We explain the music as we go.",
             cap=("Clarinet and string trio", "Christmas 2025"),
             glance=[("For", "Care homes, hospitals, religious communities, parishes and community centres"),
                     ("Where", "Your own room, in Dublin and further by arrangement"),
                     ("When", "A date we agree with you"),
                     ("What you need", "A room, a date and a contact person")],
             now=("Taking invitations", "Write with your room and a few dates that suit."),
             how_h2="Three steps to a concert in your room.",
             steps=[("You tell us", "Write with the room, a date and who will be listening."),
                    ("We plan the music",
                     "We choose pieces people can enjoy <mark>on first hearing</mark>, for your listeners."),
                    ("We come and play",
                     "Musicians, instruments and stands come with us, and we play in your room.")],
             expect_h2="Before you invite us.",
             faq=[("Who plays?",
                   "Andrew Seohyeon Kim, <mark>our founder</mark>, plays clarinet and organ, alone or with musicians he "
                   "invites. Our Letters Ensemble gives some concerts."),
                  ("Who can listen?",
                   "<mark>Everyone in the room</mark>: residents or patients, family and staff. There is no dress code."),
                  ("Where have you played?",
                   "A hospital, a care home, religious communities and parishes, <mark>in four countries</mark>. See <a "
                   f'class="link" href="about.html#places">all {N_PLACES} places where we have played and '
                   "taught</a>.")],
             record_h2="Concerts so far.",
             record_lead="Every outreach concert, with its date, place and music.",
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
             lead="For adults who have never played an instrument. You play your first notes <mark>in week one</mark>.",
             cap=("Recorders", "November 2025"),
             # the pilot ensemble on the founder's own channel; our still until play is pressed
             video=dict(kind="youtube", id="i7skwGKWSYY", poster="recorders.jpg",
                        cap=("The pilot ensemble", "Retired Presentation Sisters playing the recorder together.")),
             room_h2="Where the class began.",
             glance=[("For", "Adults who have never played an instrument"),
                     ("Where", "Mulhuddart, Dublin 15"),
                     ("When", "Wednesday evenings, 7pm to 8pm, autumn 2026"),
                     ("What you need", "No instrument, and no need to read music")],
             now=("Running now", "<strong>Wednesday evenings, 7pm to 8pm</strong><span class=\"sr-only\">, </span>"
                                 "<span class=\"pp-where\">Mulhuddart Community Centre</span>"),
             live=True,
             how_h2="From a first note to your own part.",
             steps=[("Your first notes", "Hold the recorder, breathe and play."),
                    ("Reading from scratch",
                     "Notes and fingering, one at a time, with music we prepare for the class."),
                    ("Your own part",
                     "The group plays in harmony. The term ends with <mark>a small concert</mark> of our own.")],
             expect_h2="Before your first class.",
             faq=[("Do I need my own recorder?", "<strong>No.</strong> We can <mark>lend you one</mark>."),
                  ("Do I need to read music?",
                   "<strong>No.</strong> You learn to read a few notes at a time, <mark>as you play</mark>."),
                  ("Where did the class come from?",
                   "From <mark>a ten-week pilot</mark> with seven retired Presentation Sisters, shown in the video "
                   "below.")],
             record_h2="The story so far.",
             record_lead="It began with one question, asked at a concert.",
             join_h2="Join the class.",
             join_text="<strong>Wednesday evenings, 7pm to 8pm</strong>, in Mulhuddart.",
             join_btn="Ask about the class",
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
         img=("letters-ensemble.jpg", 1400, 1050, "Four string players and their conductor standing with their instruments in a hall hung with Irish flags and shamrocks"),
         line="<mark>Amateur musicians</mark> in Dublin who play for communities.",
         page=dict(
             lead="<mark>Amateur musicians</mark> in&nbsp;Dublin, together since 2024. We play Irish, Korean and sacred music.",
             cap=("Letters Ensemble", "Four string players and their conductor"),
             glance=[("For", "Amateur players of any background"),
                     ("Where", "Dublin"),
                     ("When", "Ask us for rehearsal times"),
                     ("What you need", "An instrument you play")],
             now=("All players welcome", "Write with your instrument; we will send rehearsal times."),
             how_h2="Rehearse in Dublin, then play for communities.",
             steps=[("Tell us your instrument",
                     "Write with what you play. Players of <mark>any background</mark> are welcome."),
                    ("Rehearse together",
                     "We rehearse in Dublin, directed by our founder, Andrew Seohyeon Kim."),
                    ("Play for a community",
                     "Concerts go to religious communities, parishes and care settings, often around a "
                     "feast day.")],
             expect_h2="Before you join.",
             faq=[("What does the ensemble play?",
                   "Pieces such as Mozart&rsquo;s &lsquo;Ave verum corpus&rsquo;, &lsquo;Down by the Sally Gardens&rsquo; and &lsquo;Arirang&rsquo;."),
                  ("Can I join if I stopped playing years ago?",
                   "<strong>Yes.</strong> One member joined after a talk reminded them of the viola they "
                   "played at school."),
                  ("How many concerts has it given?",
                   "<mark>Four formal concerts</mark>, from Dalgan Park in March 2024 to Christmas 2025.")],
             record_h2="Concerts so far.",
             record_lead="The ensemble&rsquo;s four formal concerts, with date, occasion and place.",
             join_h2="Play with us.",
             join_text="",
             join_btn="Ask about joining",
             mail_subject="Joining the Letters Ensemble",
             mail_fields=["Your name",
                          "Your instrument(s)",
                          "How long you have played",
                          "When you last played",
                          "Days and times that suit you"],
         )),
    dict(slug="concert-companion", pillar="learn", name="Concert Guide &amp; Companion",
         short="Concert Guide &amp; Companion",
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
             cap=("BBC Proms, Royal Albert Hall", "London · September 2023 · photo: our founder, from the audience"),
             room_h2="The hall, from the seats.",
             glance=[("For", "Anyone who would rather not go alone"),
                     ("Where", "Concert halls in Dublin"),
                     ("When", "As outings are planned"),
                     ("What you need", "No knowledge of music")],
             now=("Dates by email", "Write to us. We will tell you about the next outing."),
             how_h2="Before, during and after the concert.",
             steps=[("Prepare beforehand",
                     "We choose a concert. Then we go through the music and what happens in the hall."),
                    ("Go as a group", "The group goes together, with a guide during the concert."),
                    ("Talk it over", "Afterwards we talk about what we heard. There is <mark>no wrong answer</mark>.")],
             expect_h2="Before your first outing.",
             faq=[("Which concerts have you suggested?",
                   "The National Symphony Orchestra, the TU Dublin Philharmonic and a National Concert "
                   "Hall series, among others."),
                  ("How big is a group?",
                   "In December 2025, <mark>six people</mark> went together to the National Concert Hall."),
                  ("New to Ireland. Is this for me?",
                   "<strong>Yes.</strong> People new to Ireland are welcome, and we work in <mark>English and Korean</mark>.")],
             record_h2="Concerts suggested so far.",
             record_lead="Concerts we introduced, and one we attended together.",
             join_h2="Join an outing.",
             join_text="",
             join_btn="Ask about an outing",
             mail_subject="Concert Guide & Companion",
             mail_fields=["Your name",
                          "Days and times that suit you",
                          "Music you like (optional)",
                          "Any access needs (optional)",
                          "Language you prefer: English or Korean"],
         )),
]


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
        img=("hero-outreach.jpg", 1800, 1350,
             "Four string players, seated and playing, and their conductor in a hall hung with Irish flags and shamrocks"),
        cap=("Letters Ensemble", "St Patrick&rsquo;s Day concert"),
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
        # message 3: CMFE Artists is a plan, so the one thing open now is to
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
        link="About us",
    ),
    numbers=dict(
        label="On the record",
        sr="In numbers",
        # what we did, where, how far (v7: the places are counted from About's list, never typed)
        figs=[(40, "talks and performances", "since 2024", True),
              (N_PLACES, "places where we have played and taught", "since 2024", False),
              (4, "countries: Ireland, France, the UK and Korea", "since 2024", False)],
        forty=dict(talks="{n} talks", perf="{n} performances",
                   period="On the record to September 2026, one dot each"),
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
        # kit 27, positioning: who, and how
        lead="A community music initiative in Dublin. We play and teach <mark>where music is needed</mark>.",
        img=("columban-ensemble.jpg", 1400, 1050,
             "Four string players of the Letters Ensemble and their conductor in a bright yellow room"),
        cap=("Letters Ensemble", "Missionary Sisters of St Columban, Co. Wicklow · November 2024"),
    ),
    glance=[("Founded", "January 2024", "Dublin, Ireland"),
            ("What we run", "Five programmes", "in Learning and Sharing"),
            ("Where we have played", "Four countries", "Ireland, France, the UK, Korea"),
            ("Status", "Not-for-profit", "Forming a company limited by guarantee")],
    story=dict(
        label="Our story",
        h2="Since 2024.",
        # the site counts from the founding, January 2024 (Andrew, 1 Oct 2026)
        text=["We started in Dublin in January 2024, with our Letters Ensemble. Six people came to our "
              "first talk.",
              "By September 2026 there were <mark>forty talks and performances</mark> on the record. A pilot with seven "
              "retired Presentation Sisters led to our recorder class in Mulhuddart."],
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
        role="Founder &amp; Artistic Director",
        line="Andrew is a clarinettist, organist and community musician in Dublin.",
        facts=[("Training", "BMus (Hons) in Performance, TU Dublin Conservatoire"),
               ("Parish", "Music Director, Our Lady of Dolours, Dolphin&rsquo;s Barn"),
               ("Recorder pilot",
                "Seven retired Presentation Sisters, ten weeks; all seven stayed to the end")],
    ),
    run=dict(
        label="How we are run",
        h2="A not&#8209;for&#8209;profit initiative.",
        # kit 27: the status sentence, exactly as written
        lead=STATUS,
        links=[("get-involved.html#board", "Join the founding board"),
               ("contact.html#privacy", "How we handle your details")],
        items=[("Who decides.",
                "Once the company is registered, an independent volunteer board will run it. We are "
                "looking for its first members now."),
               ("Money.",
                "We are not asking for or accepting gifts yet. We will never ask you to pay into "
                "<mark>a personal account</mark>."),
               ("Photographs.",
                "We show performers, instruments and empty rooms. Anyone else who can be recognised "
                "appears only with their written consent."),
               # facts.md l.59, word for word, where families and partners decide (v7)
               ("Public liability insurance.", "We show the certificate on request.")],
    ),
    places=dict(
        label="Places",
        h2="Where we have played and taught.",
        # 08 §2: concerts introduced to participants, with group attendance organised
        lead=f"<mark>{N_PLACES} places</mark> in four countries, grouped by kind of place.",
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
        lead="Most programmes <mark>need no experience</mark>. Write to us, and we will tell you how to start.",
    ),
    list_sr="The five programmes",
    # kit 27, message 3: a plan, said as a plan, with the one thing open now
    artists=dict(
        label="For artists",
        text='From any field, <a class="link" href="get-involved.html#play">register&nbsp;interest</a> any '
             "time. CMFE Artists is planned for 2027.",
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
        label="Partner venues",
        h2="Bring a concert to your place.",
        lead="Care homes, hospitals, religious communities, parishes and community centres <mark>can invite us</mark>.",
        pair_labels=("You provide", "We bring"),
        pairs=[("A concert",
                ["A room", "A date", "A contact person"],
                ["The musicians", "Instruments and stands", "Music chosen for your listeners"]),
               ("A recorder class",
                ["A warm room each week", "A contact person", "Help letting local people know"],
                ["Recorders to lend", "Music and teaching, as funding allows"])],
        # kit 02 §2 and 29: what a host gives, and what we can promise
        # the same three steps as the Outreach Concerts page
        href=MAIL_INVITE, btn="Invite us", more="How a concert works",
    ),
    # Andrew, 2 Oct 2026: take interest freely, from any field, at any time;
    # vetting depends on the venue; show example programmes (from the record)
    play=dict(
        label="CMFE Artists",
        h2="Perform with us.",
        lead="We are ready to work with musicians and artists <mark>from any field</mark>, at any time.",
        facts=[("For", "Students, emerging, amateur and professional artists"),
               ("How", "A few lines about you, and a link to your work"),
               ("Garda vetting", "May be needed, depending on the venue"),
               ("Planned<span class=\"sr-only\"> for 2027</span>", "CMFE Artists: paid, mentored performances for emerging musicians")],
        examples_label="Example programmes",
        # each one is on the record (ledger.py, public labels): the kind of
        # place, never a liturgy or a private occasion; newest first
        examples=[("An autumn concert in a church", "Soprano, haegeum, clarinet and piano", "September 2026"),
                  ("Christmas in a care home", "Clarinet and string trio", "December 2025"),
                  ("A homeless hostel", "Organ and clarinet", "July 2025"),
                  ("St Patrick&rsquo;s Day in a religious community", "Korean traditional ensemble and clarinet",
                   "March 2025")],
        note='Players of <mark>any background</mark> can also join the <a class="link" '
             'href="programmes/letters-ensemble.html">Letters Ensemble</a>.',
        href=_MAIL_EOI, btn="Register your interest",
    ),
    support=dict(
        label="Help us build it",
        board=dict(
            h2="Join the founding board.",
            lead="Once our company is registered, this <mark>independent volunteer</mark> board will run it.",
            facts=[("Roles", "Chair, treasurer, secretary, safeguarding and care lead, community lead"),
                   ("Conditions", "Unpaid, with reasonable expenses")],
            # the same roles, one a seat at the drawn table (parts.table); no number of seats is said
            roles=["Chair", "Treasurer", "Secretary", "Safeguarding and care lead", "Community lead"],
            href=_MAIL_BOARD, btn="Ask about a role",
        ),
        gifts="We are not asking for or accepting gifts yet.",
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
    crumbs_label="Breadcrumb", crumb="Programmes",
    how_label="How it works", expect_label="What to expect", record_label="On the record",
    join_label="Take part", others_label="The other programmes", all_label="All five programmes",
    room_label="In the room", room_h2="Where it happens.",
    how_join="How to take part",
    video_h="Watch", video_label="Video: {name}", play="Play the video", watch="Watch on {service}",
    people="{n} people",
    mail_hint="One line is enough. If it helps, tell us:",
    or_write="Or write to", email=EMAIL, tel="+353 83 078 0635", tel_href="+353830780635",
    strip=dict(aria="{n} entries on the record for this programme, shown month by month from 2024 to 2026.",
               learn="Learning", share="Sharing", bar="A bar spans several months.",
               dot={"getting-to-know": "A dot is one talk.", "outreach-concerts": "A dot is one concert.",
                    "recorder-ensemble": "A dot is one date.", "letters-ensemble": "A dot is one concert.",
                    "concert-companion": "A dot is one concert."}),
    earlier="Show {n} earlier",
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
        lead="The latest news, <mark>every talk and performance</mark> since 2024, and photographs.",
    ),
    latest_sr="Latest",
    latest=[("Board", "Autumn 2026",
             "Forming a founding board",
             "As we form the company, we are looking for volunteer board members.",
             "get-involved.html#board",
             "The roles"),
            ("Class", "Autumn 2026",
             "Community Recorder Ensemble Class",
             "Wednesday evenings, 7pm to 8pm, at Mulhuddart Community Centre.",
             "programmes/recorder-ensemble.html",
             "About the class"),
            ("Concert", "19 September 2026",
             "An autumn concert",
             "At Methodist Centenary Church, Ranelagh, with soprano, haegeum, clarinet and piano.",
             "programmes/outreach-concerts.html#record",
             "All outreach concerts")],
    chart=dict(
        label="The record",
        h2="Forty, by year.",
        lead="Every talk and performance, with what it was and where.",
        figs=[(17, "talks", "talk"),
              (20, "outreach performances", "perf"),
              (1, "pilot concert", "perf"),
              (2, "South Dublin Live 2026 concerts", "perf")],
        period="January 2024 &ndash; September 2026",
        year_count="{n} talks and performances",
        year_talks=("{n} talk", "{n} talks"),
        year_perf=("{n} performance", "{n} performances"),
        year_more="Show all {n} from {y}",
        row_talk="Talk",
        row_perf="Performance",
    ),
    timeline=dict(
        label="Timeline",
        h2="How it grew.",
        years=[("2024", [("January", "It starts",
                          "Founded in Dublin, with the Letters Ensemble. <mark>Six people</mark> came to the first talk."),
                         ("Through the year", "Music goes out",
                          "Concerts in Co. Meath, Co. Wicklow, London, Paris and Daegu.")]),
               ("2025", [("Through the year", "Into care settings",
                          "Concerts at a day service, a homeless hostel and a care home."),
                         ("Autumn", "Introducing concerts",
                          "We started introducing concerts to participants and organising group attendance."),
                         ("October", "Preparing the recorder pilot",
                          "Preparation began for a recorder ensemble with <mark>seven retired Presentation "
                          "Sisters</mark>."),
                         ("December", "At the National Concert Hall",
                          "The fifteenth&nbsp;talk was a concert we heard together.")]),
               ("2026", [("January to&nbsp;April", "All seven, to the end",
                          "Ten weekly rehearsals at Warrenmount, then <mark>an Easter concert</mark> at Clondalkin "
                          "Lodge."),
                         ("August", "South Dublin Live",
                          "Our founder was selected. We played twice in Tallaght."),
                         ("September", "An autumn concert",
                          "In Ranelagh, Dublin 6, at Methodist Centenary Church."),
                         ("Autumn", "The public class begins",
                          "The class <mark>born from the pilot</mark> opens to the public in Mulhuddart.")])],
    ),
    gallery=dict(
        label="Photographs",
        h2="In the room.",
        lead="From our concerts and rehearsals, newest first.",
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
            (("care-christmas.jpg", 1400, 1050, CARE_ALT),
             "Clarinet and string trio · Christmas 2025"),
            (("score-stand.jpg", 1050, 1400, "A string trio rehearsing behind a part on a music stand"),
             "Before the concert · Christmas 2025"),
            (("recorders.jpg", 1343, 1400, RECORDERS_ALT),
             "Recorders · November 2025"),
            (("church-aisle.jpg", 1050, 1400,
              "A clarinet held up before the altar of a parish church in Co. Westmeath"),
             "Clarinet before the altar · Dysart, Co. Westmeath · 2025"),
            (("columban-ensemble.jpg", 1400, 1050,
              "Four string players of the Letters Ensemble and their conductor in a bright yellow room"),
             "Letters Ensemble · Missionary Sisters of St Columban, Co. Wicklow · November 2024"),
            (("dalgan-hall.jpg", 1400, 1050,
              "A hall set out with chairs and music stands before a concert, with no one there yet"),
             "The hall before the concert · Dalgan Park, Co. Meath · March 2024"),
            (("hero-outreach.jpg", 1800, 1350,
              "Four string players, seated and playing, and their conductor in a hall hung with Irish flags and shamrocks"),
             "Letters Ensemble · St Patrick&rsquo;s Day concert"),
            (("letters-ensemble.jpg", 1400, 1050, "Four string players and their conductor standing with their instruments in a hall hung with Irish flags and shamrocks"),
             "Letters Ensemble · four string players and their conductor"),
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
        lead="Choose a topic below, or simply write. We answer <mark>every message</mark>.",
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
                ("venue", "Concert invitation", "A venue: invite us to play", INVITE_FIELDS),
                ("artist", "CMFE Artists: expression of interest", "An artist: register interest", EOI_FIELDS),
                ("board", "Founding board: Classical Music for Everyone", "The founding board",
                 ["Which role interests you", "A few lines about you"]),
                ("data", "Personal data request", "Your details: see, correct or delete",
                 ["What you would like: to see, correct or delete it"]),
                ("other", "Enquiry: Classical Music for Everyone", "Anything else", [])],
        helps="Helpful to include:",
        general="A few lines are enough. Choosing a topic shows what helps us answer.",
        message_label="Your message",
        button="Open in my email app",
        # "keep it short" is always in view, beside the button (chief designer v2: a mailto
        # address over about 2,000 characters may not open at all)
        note="Keep it short here: you can finish and send it in your email app. If nothing opens, write to",
    ),
    direct_label="Or write directly",
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
                             '<span class="sl">Founder &amp; Artistic Director</span>')],
    privacy=dict(
        label="Privacy notice",
        h2="How we look after your details.",
        intro="How we use the details you send, and your rights. Last updated 5 October 2026.",
        # what this website does not have, said once and plainly
        # the contact form is a mailto form: it sends nothing itself (2 Oct 2026)
        none=[("Forms", "One, and it only opens your email app"), ("Cookies", "None of ours"),
              ("Analytics", "None"), ("Advertising", "None")],
        blocks=[("Who is responsible",
                 "p",
                 '<span class="brandname">Classical Music for Everyone</span>, a not-for-profit community '
                 'music initiative in Dublin. For anything about your details, write to <a class="link" '
                 'href="mailto:sby05034@gmail.com">sby05034@gmail.com</a>.',
                 ""),
                ("When you email us",
                 "list",
                 ["We use what you send <mark>only to reply</mark> and to do what you asked.",
                  "We <mark>never sell it</mark>, and only the services listed below handle it for us.",
                  "We keep artists&rsquo; details for up to two years, to offer them concerts.",
                  "Telling us about access needs is optional."],
                 ""),
                ("Who else handles it",
                 "rows",
                 [("GitHub", "Hosts this site and records IP addresses for security"),
                  ("Google Fonts", "Supplies our typefaces and receives your IP address"),
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
