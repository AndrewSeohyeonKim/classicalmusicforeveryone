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
]
N_PLACES = sum(len(rows) for _, rows in PLACES)

PROGRAMMES_DATA = [
    dict(slug="getting-to-know", pillar="learn", name="Getting to Know Classical Music",
         short="Getting to Know",
         icon="score", vocab="Getting closer · Together · My taste",
         img=("lecture-recital.jpg", 1050, 1400, "A talk in progress, with live playing"),
         line="Talks with <mark>live music</mark>, for anyone curious about Classical Music.",
         page=dict(
             lead="We give talks on Classical Music, with <mark>live playing</mark>. They are for anyone curious to "
                  "hear more.",
             cap=None,
             glance=[("For", "Anyone curious about Classical Music"),
                     ("Where", "Dublin"),
                     ("When", "On request"),
                     ("What you need", "No knowledge of music")],
             now=("On request", "Write to us. We will plan a talk with your group."),
             # 02 §4: three stages, in this order; 08 §1 for what each covers
             how_h2="Three stages, from first listening to your own taste.",
             steps=[("Getting Closer",
                     "What Classical Music is, by period and by instrument, with recordings and live "
                     "playing."),
                    ("Together",
                     "Orchestras and performers, including Ireland&rsquo;s own. How to book a ticket and "
                     "choose a seat."),
                    ("My Taste",
                     "<mark>Finding what you like</mark>, for example by hearing one piece played by five pianists.")],
             expect_h2="Before your first talk.",
             faq=[("Do I need to know anything first?",
                   "<strong>No.</strong> We start from &lsquo;what is Classical Music?&rsquo; and explain "
                   "every piece we play."),
                  ("How many people come?",
                   "Six to fourteen people came to each talk we counted. The chart below shows those counts."),
                  ("Can our group ask for a talk?",
                   "<strong>Yes.</strong> That is how talks are arranged now.")],
             record_h2="Talks so far.",
             record_lead="Every talk on the record, with its date, topic and place.",
             join_h2="Ask for a talk.",
             join_text="Write even if you are on your own.",
             join_btn="Ask about a talk",
             mail_subject="Getting to Know Classical Music",
             mail_fields=["Your name", "Your group or organisation (if any)", "Where you could meet",
                          "Roughly how many people", "Dates or times that suit"],
         )),
    dict(slug="outreach-concerts", pillar="share", name="Outreach Concerts",
         short="Outreach Concerts",
         icon="room", vocab="Day room · Chapel · Atrium",
         img=("care-christmas.jpg", 1400, 1050, CARE_ALT),
         line="Live Classical Music in <mark>care homes, hospitals</mark>, parishes and community centres.",
         page=dict(
             # each lead sentence fits its column on a laptop (typeset_check:
             # the longer first sentences folded into half lines)
             lead="We play in the rooms <mark>where people already are</mark>. We explain the music as we go.",
             cap=("Outreach concert", "Christmas 2025"),
             glance=[("For", "Care homes, hospitals, parishes and community groups"),
                     ("Where", "Your own room, in Dublin and further by arrangement"),
                     ("When", "By arrangement"),
                     ("What you need", "A room, a date and a contact person")],
             now=("Taking invitations", "Write with your room and a few dates that suit."),
             how_h2="Three steps to a concert in your room.",
             steps=[("You tell us", "Write with the room, a date and who will be listening."),
                    ("We plan the music",
                     "We choose pieces people can <mark>enjoy on first hearing</mark>, for your listeners."),
                    ("We come and play",
                     "Musicians, instruments and stands come with us, and we play in your room.")],
             expect_h2="Before you invite us.",
             faq=[("Who plays?",
                   "Andrew Seohyeon Kim, our founder, plays clarinet and organ, alone or with musicians he "
                   "invites. Our Letters Ensemble gives some concerts."),
                  ("Who can listen?",
                   "<mark>Everyone in the room</mark>: residents or patients, family and staff. There is no dress code."),
                  ("Where have you played?",
                   "A hospital, a care home, religious communities and parishes, in four countries. See <a "
                   f'class="link" href="about.html#places">all {N_PLACES} places where we have played and '
                   "taught</a>.")],
             record_h2="Concerts so far.",
             record_lead="Every outreach concert on the record, with its date, place and music.",
             join_h2="Invite us to play.",
             join_text="",
             join_btn="Invite us",
             mail=MAIL_INVITE,
             mail_fields=INVITE_FIELDS,
         )),
    dict(slug="recorder-ensemble", pillar="learn", name="Community Recorder Ensemble Class",
         short="Recorder Ensemble Class",
         icon="recorder", vocab="First notes · Reading · Your own part",
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
                     ("Where", "Mulhuddart Community Centre, Dublin 15"),
                     ("When", "Wednesday evenings, 7pm to 8pm, autumn 2026"),
                     ("What you need", "No instrument and no music reading")],
             now=("Running now", "<strong>Wednesday evenings, 7pm to 8pm</strong>, Mulhuddart Community Centre, "
                                 "Dublin 15."),
             live=True,
             how_h2="From a first note to your own part.",
             steps=[("Your first notes", "Hold the recorder, breathe and play."),
                    ("Reading from zero",
                     "Notes and fingering, one at a time, with music we prepare for the class."),
                    ("Your own part",
                     "The group plays in harmony. The term ends with <mark>a small concert</mark> of our own.")],
             expect_h2="Before your first class.",
             faq=[("Do I need my own recorder?", "<strong>No.</strong> We can lend you one."),
                  ("Do I need to read music?",
                   "<strong>No.</strong> You learn to read a few notes at a time, as you play."),
                  ("Where did the class come from?",
                   "From a ten-week pilot with seven retired Presentation Sisters, shown in the video "
                   "below.")],
             record_h2="The story so far.",
             record_lead="How the class came about, step by step.",
             join_h2="Join the class.",
             join_text="",
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
         icon="people", vocab="Irish · Korean · Sacred",
         img=("letters-ensemble.jpg", 1400, 1050, "The Letters Ensemble with their instruments"),
         line="<mark>Amateur musicians</mark> in Dublin playing Irish, Korean and sacred music.",
         page=dict(
             lead="<mark>Amateur musicians</mark> in Dublin, together since 2024. We play Irish, Korean and sacred music.",
             cap=("Letters Ensemble", "with their instruments"),
             glance=[("For", "Amateur players of any background"),
                     ("Where", "Dublin"),
                     ("When", "Ask us for rehearsal times"),
                     ("What you need", "An instrument you play")],
             now=("All players welcome", "Write with your instrument, and we will send rehearsal times."),
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
                   "Pieces such as Mozart&rsquo;s Ave verum corpus, Down by the Sally Gardens and Arirang."),
                  ("I stopped playing years ago. Can I join?",
                   "<strong>Yes.</strong> One member joined after a talk reminded them of the viola they "
                   "played at school."),
                  ("How many concerts has it given?",
                   "Four formal concerts, from Dalgan Park in March 2024 to Christmas 2025.")],
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
         line="<mark>Small groups</mark> go to concerts together, prepared beforehand.",
         page=dict(
             lead="For people who would rather not go to a concert alone. We prepare, <mark>go together</mark>, then "
                  "talk it over.",
             # the founder's own photograph from the audience at the BBC Proms; no group trip to the
             # Proms is on the record, so the caption says whose view it is. The month is the
             # recording date of the source video (Andrew, 1 Oct 2026)
             cap=("BBC Proms, Royal Albert Hall", "London · September 2023 · seen from the audience by our founder"),
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
                   "In December 2025, six people went together to the National Concert Hall."),
                  ("New to Ireland. Is this for me?",
                   "<strong>Yes.</strong> People new to Ireland are welcome, and we work in English and Korean.")],
             record_h2="Concerts suggested so far.",
             record_lead="Concerts we introduced to participants, and the one we attended together.",
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

HOME = dict(
    hero=dict(
        eyebrow="Community music · Dublin, Ireland",
        title=["Classical Music,", '<span class="for">for </span><em>Everyone.</em>'],
        # under the title comes the master line (Andrew, 2 Oct 2026, evening), taken from
        # layout.STR, the same string the footer sets, so the two cannot drift
        cta=("#programmes", "See the programmes"),
        more=("programmes/outreach-concerts.html", "Invite us to play"),
        img=("hero-outreach.jpg", 1800, 1350,
             "The Letters Ensemble and their conductor playing a St Patrick&rsquo;s Day concert in a hall"),
        cap=("Letters Ensemble", "St Patrick&rsquo;s Day concert"),
    ),
    # the ways in, as the contents line of a programme (no boxes, no tint):
    # taking part comes first, because most visitors come to join something
    progs=dict(
        label="What we do",
        h2="Five programmes.",
        lead="Three help you listen and play; two take live music out to people.",
        others='Musicians and artists can <a class="link" href="get-involved.html#play">register '
               'interest</a> any time. Volunteers can <a class="link" '
               'href="get-involved.html#board">join the founding board</a>.',
        # kit 27, message 3: a plan, said as a plan, with the one thing open now
    ),
    # kit 27 ①, the opening of the one-page case, set in three parts so the
    # answer stands out; Ireland rather than Dublin (Andrew, 1 Oct 2026). It
    # describes the need, not our reach: never "across Ireland".
    why=dict(
        label="Why we exist",
        premise="Many people in Ireland miss going to concerts, and still need the music.",
        reasons=["Some live in a nursing home.",
                 "Some rarely leave the house.",
                 "Some are new to the country and don&rsquo;t know where to begin."],
        resolve="So we go to <em>them.</em>",
        link="About us",
    ),
    numbers=dict(
        label="On the record",
        sr="In numbers",
        figs=[(40, "talks and performances", "since 2024", True),
              (4, "countries: Ireland, France, the UK and Korea", "since 2024", False)],
        forty=dict(aria="The {n} talks and performances on the record to September 2026, one square each: "
                        "{talks} talks and {perf} performances.",
                   talks="Talk ({n})", perf="Performance ({n})",
                   period="On the record to September 2026, one square each"),
        # kit 27: a selection of the founder, said as such
        note='Our founder was selected for South Dublin Live 2026. <a class="link" '
             'href="news.html#record">See the record, month by month</a>',
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
        cap=("Missionary Sisters of St Columban, Co. Wicklow", "November 2024"),
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
              "By September 2026 there were forty talks and performances on the record. A pilot with seven "
              "retired Presentation Sisters led to our recorder class in Mulhuddart."],
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
        line="Andrew is a clarinettist, organist and community musician in Dublin.",
        facts=[("Training", "BMus (Hons) in Performance, TU Dublin Conservatoire"),
               ("Parish", "Music Director, Our Lady of Dolours, Dolphin&rsquo;s Barn"),
               ("Research",
                "Recorder pilot with seven retired Presentation Sisters; all seven played in public")],
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
                "We are not asking for or accepting gifts yet. We will never ask you to pay into a "
                "personal account."),
               ("Photographs.",
                "We show performers, instruments and empty rooms. Anyone else who can be recognised "
                "appears only with their written consent.")],
    ),
    places=dict(
        label="Places",
        h2="Where we have played and taught.",
        # 08 §2: concerts introduced to participants, with group attendance organised
        lead=f"{N_PLACES} places in four countries, grouped by kind of place.",
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
        h2="Why <em>Everyone</em> is in gold",
        # the meaning is in the proportion (CLAUDE.md §1), so "for" stays in the sentence
        text="Our logo sets &ldquo;for&rdquo; small and &ldquo;Everyone&rdquo; large. We have to live up to "
             "<mark>that word</mark>.",
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
        text='From any field, <a class="link" href="get-involved.html#play">register interest</a> any '
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
    ways=[("programmes.html", "Anyone", "Join a programme", "The programmes"),
          # the approved action (R8), as in the footer and on the home page: one line, like the others
          ("#invite", "Venues", "Invite us to play", "What it takes"),
          ("#play", "Artists", "Perform with us", "Example programmes"),
          ("#board", "Volunteers", "Join the founding board", "The roles")],
    # the address and phone under each mail button
    alt=dict(or_write="Or write to", email=EMAIL, tel="+353 83 078 0635", tel_href="+353830780635"),
    invite=dict(
        label="Partner venues",
        h2="Bring a concert to your place.",
        lead="Care homes, hospitals, parishes and community centres <mark>can invite us</mark>.",
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
               ("Planned for 2027", "CMFE Artists: paid, mentored performances for emerging musicians")],
        examples_label="Example programmes",
        # each one is on the record (ledger.py, public labels): the kind of
        # place, never a liturgy or a private occasion; newest first
        examples=[("An autumn concert in a church", "Soprano, haegeum, clarinet and piano", "September 2026"),
                  ("Christmas in a care home", "Clarinet and string trio", "December 2025"),
                  ("A homeless hostel", "Organ and clarinet", "July 2025"),
                  ("St Patrick&rsquo;s Day in a religious community", "Korean traditional ensemble and clarinet",
                   "March 2025")],
        note='Amateur players of any background can also join the <a class="link" '
             'href="programmes/letters-ensemble.html">Letters Ensemble</a> now.',
        href=_MAIL_EOI, btn="Register your interest",
    ),
    support=dict(
        label="Help us build it",
        board=dict(
            h2="Join the founding board.",
            lead="We are looking for the first members of <mark>an independent volunteer board</mark>.",
            facts=[("Roles", "Chair, treasurer, secretary, safeguarding and care lead, community lead"),
                   ("Conditions", "Unpaid, with reasonable expenses")],
            # the same roles, one a seat at the drawn table (parts.table); no number of seats is said
            roles=["Chair", "Treasurer", "Secretary", "Safeguarding and care lead", "Community lead"],
            href=_MAIL_BOARD, btn="Enquire about a role",
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
               learn="Learning", share="Sharing", note="A dot is one session; a bar spans several months."),
    earlier="Earlier: {n} more",
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
        lead="The latest news, every talk and performance since 2024, and photographs.",
    ),
    latest_sr="Latest",
    latest=[("Autumn 2026",
             "Forming a founding board",
             "We are looking for volunteers for the founding board.",
             "get-involved.html#board",
             "The roles"),
            ("Autumn 2026",
             "Community Recorder Ensemble Class",
             "Running at Mulhuddart Community Centre on Wednesday evenings.",
             "programmes/recorder-ensemble.html",
             "About the class"),
            ("19 September 2026",
             "An autumn concert",
             "Soprano, haegeum, clarinet and piano at Methodist Centenary Church, Ranelagh.",
             "programmes/outreach-concerts.html#record",
             "All outreach concerts")],
    chart=dict(
        label="The record",
        h2="Forty, one square each.",
        lead="Every talk and performance on the record, month by month.",
        figs=[(17, "talks"),
              (20, "outreach performances"),
              (1, "pilot concert"),
              (2, "South Dublin Live 2026 concerts")],
        period="January 2024 &ndash; September 2026",
        aria=("A calendar from 2024 to 2026 with one square for each of the {n} talks and performances on "
              "the record: {talks} talks and {perf} performances."),
        scroll="The record, month by month",
        key_talk="Talk ({n})",
        key_perf="Performance ({n})",
        # the ledger's own note on talk 15 (5 Dec 2025)
        key_note="The December 2025 talk was a concert, attended together.",
    ),
    timeline=dict(
        label="Timeline",
        h2="How it grew.",
        rows=[("January 2024",
               "It starts",
               "Founded in Dublin, with the Letters Ensemble. Six people come to the first talk."),
              ("2024",
               "Music goes out",
               "Concerts in Co. Meath, Co. Wicklow, London, Paris and Daegu."),
              ("Autumn 2025",
               "Introducing concerts",
               "We start introducing concerts to participants and organising group attendance."),
              ("October 2025",
               "An audience becomes players",
               "Preparation begins for a recorder ensemble with seven retired Presentation Sisters."),
              ("December 2025",
               "A concert, attended together",
               "For the fifteenth talk, we go to a concert at the National Concert Hall."),
              ("January&ndash;April 2026",
               "All seven, to the end",
               "Ten weekly rehearsals at Warrenmount, then an Easter concert at Clondalkin Lodge."),
              ("August 2026",
               "South Dublin Live 2026",
               "Our founder was selected for South Dublin Live 2026: two concerts in Tallaght."),
              ("September 2026",
               "An autumn concert",
               "We held it at Methodist Centenary Church, Ranelagh, Dublin 6."),
              ("Autumn 2026",
               "The public class begins",
               "The class born from the pilot opens to the public in Mulhuddart.")],
    ),
    gallery=dict(
        label="Photographs",
        h2="In the room.",
        lead="From our concerts and rehearsals, newest first.",
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
        h2="Write to us",
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
        general="Choose a topic, or simply write.",
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
        intro="How we use the details you send, and your rights. Last updated 2 October 2026.",
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
                 ["We use what you send only to reply and to do what you asked.",
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
                  "You can ask for any of these at any time."],
                 'If you are not happy with our answer, you can complain to the <a class="link" '
                 'href="https://www.dataprotection.ie/">Data Protection Commission</a>.')],
    ),
)

CONTACT = P.contact(CONTACT_T)
