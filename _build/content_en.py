# -*- coding: utf-8 -*-
"""English page content. Facts follow the canonical set (00_최종본, 2026-08-27).

House rule for this file: roughly 50–80 words per section. Where an explanation
runs longer than that, it belongs in a diagram, a table or a caption — not in
another paragraph.
"""

import diagrams as dg

L = "en"

# ---------------------------------------------------------------------------
# Reusable blocks
# ---------------------------------------------------------------------------

from layout import SOCIAL as _SOCIAL

_ICONS = {
    "linkedin": ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.36V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45z"/></svg>',
                 "LinkedIn"),
    "instagram": ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 7.3a4.7 4.7 0 1 0 0 9.4 4.7 4.7 0 0 0 0-9.4zm0 7.75a3.05 3.05 0 1 1 0-6.1 3.05 3.05 0 0 1 0 6.1zM17.9 7.1a1.1 1.1 0 1 1-2.2 0 1.1 1.1 0 0 1 2.2 0zM21 12c0-1.24 0-2.47-.07-3.7-.09-1.66-.46-3.14-1.67-4.35S16.5 2.37 14.83 2.28C13.6 2.2 12.36 2.2 11.13 2.2s-2.47 0-3.7.08C5.76 2.37 4.28 2.74 3.07 3.95S1.5 6.64 1.42 8.3C1.35 9.53 1.35 10.77 1.35 12s0 2.47.07 3.7c.09 1.66.46 3.14 1.67 4.35s2.69 1.58 4.35 1.67c1.23.07 2.47.07 3.7.07s2.47 0 3.7-.07c1.66-.09 3.14-.46 4.35-1.67s1.58-2.69 1.67-4.35c.08-1.23.08-2.47.08-3.7zm-2.08 5.3a3.4 3.4 0 0 1-1.92 1.92c-1.33.53-4.48.41-5.95.41s-4.63.12-5.95-.41a3.4 3.4 0 0 1-1.92-1.92c-.53-1.33-.41-4.48-.41-5.95s-.12-4.63.41-5.95A3.4 3.4 0 0 1 5.1 3.48c1.33-.53 4.48-.41 5.95-.41s4.63-.12 5.95.41a3.4 3.4 0 0 1 1.92 1.92c.53 1.33.41 4.48.41 5.95s.12 4.63-.41 5.95z"/></svg>',
                  "Instagram"),
}


def social_links(email_label):
    """The founder's public profiles, rendered only where a URL is set."""
    out = []
    for key, url in _SOCIAL.items():
        if url:
            icon, label = _ICONS[key]
            out.append(f'<li><a href="{url}" rel="me noopener" target="_blank">{icon}{label}</a></li>')
    out.append(f'<li><a href="mailto:sby05034@gmail.com">{email_label}</a></li>')
    return '<ul class="social">' + "".join(out) + "</ul>"


# The home page no longer opens on a band of figures. Counts answer "how much
# of it is there" before the reader has been told what it is, and they made the
# work read as a tally rather than as a programme. The same numbers still sit
# where they are evidence for a claim — on About, on the programme pages, and
# in "Grounds for trust" further down this page.

WHATS_ON = """<div class="grid grid-2 stagger">
  <div class="notice">
    <span class="tag tag-live">Now enrolling</span>
    <h3>Recorder Ensemble — Mulhuddart</h3>
    <p class="small">Twelve weeks for complete beginners. No experience, no music reading.</p>
    <dl>
      <dt>Where</dt><dd>Mulhuddart Community Centre, Dublin 15</dd>
      <dt>When</dt><dd>Wednesdays, 7:00–8:00pm</dd>
      <dt>Starts</dt><dd>9 September 2026</dd>
      <dt>Cost</dt><dd>Free</dd>
    </dl>
    <div class="btn-row"><a class="btn btn-primary" href="get-involved.html">How to join <span class="arrow">→</span></a></div>
  </div>
  <div class="notice">
    <span class="tag">Coming up</span>
    <h3>An Autumn Concert</h3>
    <p class="small">Soprano, haegeum, clarinet and piano — Chopin, Pierné, Spohr, Schubert
       and Korean traditional songs.</p>
    <dl>
      <dt>Where</dt><dd>Methodist Centenary Church, Ranelagh, Dublin 6</dd>
      <dt>When</dt><dd>Saturday 19 September 2026, 5:00pm</dd>
      <dt>Admission</dt><dd>Free · donations welcome</dd>
    </dl>
    <div class="btn-row"><a class="btn btn-quiet" href="news.html">All dates <span class="arrow">→</span></a></div>
  </div>
</div>"""

CTA = """<section class="band-inverse">
  <div class="wrap narrow center reveal">
    <h2 class="h-lg">There is a place for you here.</h2>
    <p class="lead mt-2">
      Learn an instrument for the first time, come and listen, play alongside us,
      or open your venue. Start with one line.</p>
    <div class="btn-row center-row">
      <a class="btn btn-accent" href="get-involved.html">Get involved <span class="arrow">→</span></a>
      <a class="btn btn-on-dark" href="support.html">Support our work</a>
    </div>
  </div>
</section>"""


_MAIL_PARTNER_HOME = ("mailto:sby05034@gmail.com?subject=Partnership%20enquiry"
                      "&body=Organisation%3A%20%0AWhere%3A%20%0AThe%20room%20and%20a%20possible%20date%3A%20%0A"
                      "One%20line%20on%20what%20you%20have%20in%20mind%3A%20")

# ---------------------------------------------------------------------------
# Home
#
# Order is deliberate and follows the sector convention (Music and Health
# Ireland, Live Music Now, Heart to Heart): say what the organisation runs
# before asking anything of the reader. The five programmes carry equal
# weight — no card is larger, first-coloured or labelled as the main one.
# ---------------------------------------------------------------------------

INDEX = f"""<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow lift lift-1">Community music · Dublin, Ireland</p>
      <h1><span class="line lift lift-1">Classical music,</span><span class="line lift lift-2"><em>for Everyone.</em></span></h1>
      <p class="lead lift lift-3">We teach people to play — not only to listen — and we bring
         live classical music to the places it rarely reaches.</p>
      <div class="btn-row lift lift-4">
        <a class="btn btn-primary" href="programmes.html">What we do <span class="arrow">→</span></a>
        <a class="btn btn-quiet" href="get-involved.html">Get involved</a>
      </div>
    </div>
    <figure class="lift lift-3">
      <div class="photo photo-3x2">
        <img src="images/hero-outreach.jpg" width="1800" height="1350"
             alt="Musicians playing a St Patrick&rsquo;s Day concert in a community hall">
      </div>
      <figcaption>A St Patrick&rsquo;s Day concert for a religious community — the Letters Ensemble.</figcaption>
    </figure>
  </div>
</section>


<section>
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">What we do</p>
      <h2>Five programmes, two pillars, one circuit.</h2>
      <p>We teach people to play, and we play for people who cannot easily come to a concert
         hall. Neither half works alone: the rooms we play in are where the next class comes
         from, and the class is where the next players come from.</p>
    </div>
    <div class="pillar-bar reveal" aria-hidden="true">
      <div class="pillar-span">
        <b>Learning</b><span>We teach people to play. Three ways in, all of them
        starting from nothing.</span>
      </div>
      <div class="pillar-span pillar-b">
        <b>Sharing</b><span>We play where the music does not otherwise go.</span>
      </div>
    </div>
    <div class="grid grid-5 stagger">
      <a class="prog" href="programmes/recorder-ensemble.html">
        <div class="photo photo-3x2"><img src="images/conducting.jpg" width="1400" height="933" alt="A weekly class in a community room in Dublin"></div>
        <div class="prog-body">
          <span class="kicker">Learning</span>
          <h3>Free Recorder Ensemble course</h3>
          <p>A term for complete beginners, ending in a concert.</p>
          <div class="meta">weekly · a term</div>
        </div>
      </a>
      <a class="prog" href="programmes/getting-to-know.html">
        <div class="photo photo-3x2"><img src="images/lecture-recital.jpg" width="1400" height="933" alt="A lecture-recital in progress"></div>
        <div class="prog-body">
          <span class="kicker">Learning</span>
          <h3>Getting to Know Classical Music</h3>
          <p>Free lecture-recitals for people with no prior knowledge.</p>
          <div class="meta">17 sessions · 143 attendances</div>
        </div>
      </a>
      <a class="prog" href="programmes/concert-companion.html">
        <div class="photo photo-3x2"><img src="images/quartet-hall.jpg" width="1400" height="933" alt="An ensemble performing in a bright hall"></div>
        <div class="prog-body">
          <span class="kicker">Learning</span>
          <h3>Concert Guide &amp; Companion</h3>
          <p>Small groups accompanied to concerts they would not attend alone.</p>
          <div class="meta">10 outings · groups of about five</div>
        </div>
      </a>
      <a class="prog" href="programmes/outreach-concerts.html">
        <div class="photo photo-3x2"><img src="images/care-christmas.jpg" width="1400" height="933" alt="A quartet performing in a care setting at Christmas"></div>
        <div class="prog-body">
          <span class="kicker">Sharing</span>
          <h3>Outreach Concerts</h3>
          <p>Live performance brought into care homes, parishes, hospitals and hostels.</p>
          <div class="meta">20 performances · 15+ venues</div>
        </div>
      </a>
      <a class="prog" href="programmes/letters-ensemble.html">
        <div class="photo photo-3x2"><img src="images/letters-ensemble.jpg" width="1400" height="933" alt="The Letters Ensemble with their instruments"></div>
        <div class="prog-body">
          <span class="kicker">Sharing</span>
          <h3>Letters Ensemble</h3>
          <p>Amateur musicians living in Dublin, rehearsing every Saturday.</p>
          <div class="meta">4 concerts · since Jan 2024</div>
        </div>
      </a>
    </div>
    <div class="reveal mt-4">{dg.loop(L)}</div>
    <div class="btn-row reveal"><a class="btn btn-quiet" href="programmes.html">All five in detail <span class="arrow">→</span></a></div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">What&rsquo;s on</p>
      <h2>Open right now.</h2>
      <p>One class taking enrolments and one concert with the door open. Both are free.</p>
    </div>
{WHATS_ON}
  </div>
</section>

<section class="band-photo">
  <img src="images/ruared-stage.jpg" alt="" width="1400" height="933">
  <div class="wrap narrow reveal">
    <p class="eyebrow">Why we exist</p>
    <h2 class="h-lg">It is playing, not only listening,
       that restores dignity.</h2>
    <p class="lead mt-3">
      Classical music is culturally rich and still out of reach for many people — because of
      age, mobility, income, geography, or simple unfamiliarity. A care home, a hospital, a
      hostel, a rural parish is not a place without an audience. It is where the audience that
      has waited longest already is.</p>
    <div class="btn-row"><a class="btn btn-on-dark" href="about.html">About us <span class="arrow">→</span></a></div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap split split-wide split-center">
    <div class="reveal">
      <p class="eyebrow">One story</p>
      <h2>A question from the back of the room.</h2>
      <p class="lead mt-3">In November 2024 the Letters Ensemble played for the Missionary
         Sisters of St Columban in Co. Wicklow. Afterwards one of the sisters asked whether she
         might play again. She had played the violin, years ago.</p>
      <p class="mt-3">That question became a recorder ensemble for seven retired Presentation
         Sisters &mdash; ten weekly rehearsals, an Easter concert of nine pieces, all seven
         completing. In September 2026 the same course opened to the public, free, in
         Mulhuddart. One question, one term, one open door: that is the whole model.</p>
      <div class="btn-row"><a class="btn btn-quiet" href="impact.html">What the record supports <span class="arrow">&rarr;</span></a></div>
    </div>
    <figure class="reveal">
      <div class="photo photo-4x3">
        <img src="images/letters-ensemble.jpg" width="1400" height="1050"
             alt="The Letters Ensemble with their instruments">
      </div>
      <figcaption>The Letters Ensemble. Its November 2024 concert in Co. Wicklow is where the
        teaching programme began.</figcaption>
    </figure>
  </div>
</section>

<section class="band-mark">
  <div class="wrap split split-wide split-center">
    <div class="reveal">
      <p class="eyebrow">The name, and what it commits us to</p>
      <h2>The gold falls on <em>Everyone</em>.</h2>
      <p class="lead mt-3">That is not a flourish. In the mark, &ldquo;for&rdquo; is set small
         and &ldquo;Everyone&rdquo; large and gold, because the difficult word in the name is
         the last one.</p>
      <p class="mt-3">Classical music is not short of audiences. What it lacks is a reliable way
         in for people who are older, unwell, far from a city, short of money, or simply never
         told that any of it was theirs. The name is the brief, and the mark says which word we
         are judged on.</p>
      <p class="footer-line mark-line">Bringing classical music where it&rsquo;s needed!</p>
    </div>
    <figure class="reveal mark-plate">
      <img src="assets/logo-horizontal.svg" width="341" height="131"
           alt="The Classical Music for Everyone mark: a treble clef beside the wordmark, with &lsquo;Everyone&rsquo; set large and in gold">
      <figcaption>The horizontal mark, adopted 17 August 2026.
        <a class="link" href="identity.html">The full design standard</a></figcaption>
    </figure>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">What we are working towards</p>
      <h2>Two aims, and we are honest about the second.</h2>
      <p>The first is the one people expect from a music charity. The second is the reason we
         are a social enterprise rather than a pure charity, and it is the harder of the two.</p>
    </div>
    <div class="grid grid-2 stagger">
      <div class="card"><span class="kicker">Aim 01</span>
        <h3>A genuine way in, for anyone</h3>
        <p>Live classical music available regardless of age, background, mobility, income or
           prior knowledge &mdash; by teaching people to play, playing alongside them, and
           bringing music to the places it does not normally reach.</p>
        <div class="meta">Five programmes &middot; free and discounted places always held</div>
      </div>
      <div class="card"><span class="kicker">Aim 02</span>
        <h3>Proper work for music educators</h3>
        <p>Music educators mostly work in precarious freelance conditions. Employing them in
           secure, properly paid posts is the second social aim &mdash; not a benefit we hope
           to afford later, but part of what the organisation is for.</p>
        <div class="meta">Volunteer-led today &middot; formalising as a not-for-profit CLG</div>
      </div>
    </div>
    <div class="next reveal mt-4">
      <p class="eyebrow">Where this is going</p>
      <ol class="next-list">
        <li><b>Done</b><span>Founded 2024 &middot; pilot completed &middot; first public commission &middot; first community course</span></li>
        <li><b>Next</b><span>Incorporated as a company limited by guarantee, with directors</span></li>
        <li><b>Then</b><span>A second cohort, and rooms in Wicklow, Meath and Louth</span></li>
        <li><b>Then</b><span>The first music educator properly employed</span></li>
        <li><b>Then</b><span>Wellbeing measured, and reported on this site</span></li>
      </ol>
      <div class="btn-row">
        <a class="btn btn-quiet" href="impact.html#next">The road, in order <span class="arrow">&rarr;</span></a>
        <a class="btn btn-quiet" href="about.html">Mission, values and the founder</a>
      </div>
    </div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">What support has already done</p>
      <h2>Support bought a vehicle. The vehicle bought distance.</h2>
      <p>We are volunteer-led and formalising as a not-for-profit company limited by guarantee.
         Until that is finished there is no charity number to show you, so here is what has
         actually happened instead.</p>
    </div>
    <div class="evidence stagger">
      <div><dl>
        <dt>A vehicle, given by donors</dt>
        <dd>Donations from individuals put <strong>a vehicle on the road</strong>. Players,
            instruments and stands now travel together, to rooms no bus timetable reaches.</dd>
      </dl></div>
      <div><dl>
        <dt>Where that has taken us</dt>
        <dd>Over <strong>20 venues and institutions</strong> across
            <strong>four countries</strong> — care homes, parishes, hospitals, hostels, day
            services and community centres in Ireland, France, the UK and Korea.</dd>
      </dl></div>
      <div><dl>
        <dt>A publicly funded commission</dt>
        <dd>South Dublin County Council&rsquo;s Arts Office selected the project for
            <strong>South Dublin Live 2026</strong>. Rua Red, The Civic and Tallaght University
            Hospital wrote letters of support for that application.</dd>
      </dl></div>
    </div>
    <div class="quote reveal mt-4">
      <p>&ldquo;Through music, he offers encouragement, dignity, and spiritual accompaniment to
         those who may otherwise feel isolated.&rdquo;</p>
      <cite>Donal Roche, Auxiliary Bishop of Dublin · 16 February 2026</cite>
    </div>
    <p class="lead center mt-4 reveal">Every further contribution turns a room we cannot get
       to into a room we can.</p>
    <div class="btn-row center-row reveal">
      <a class="btn btn-quiet" href="impact.html">Dated figures, and what is not proved <span class="arrow">→</span></a>
      <a class="btn btn-quiet" href="support.html">What support pays for</a>
    </div>
  </div>
  <div class="ticker mt-4" aria-label="Institutions we have worked with">
    <p class="eyebrow center-row">Rooms we have played in</p>
    <div class="ticker-track">
      <ul>
        <li>Tallaght University Hospital</li><li>Rua Red</li><li>The Civic Theatre</li>
        <li>Clondalkin Lodge</li><li>Mulhuddart Community Centre</li><li>Presentation Sisters</li>
        <li>Missionary Sisters of St Columban</li><li>Dalgan Park</li><li>TU Dublin</li>
        <li>National Concert Hall</li><li>Our Lady of Dolours, Dolphin&rsquo;s Barn</li>
        <li>Church of the Three Patrons, Rathgar</li><li>HSE EVE Goirtin Hub</li>
        <li>Morning Star Hostel</li><li>Missions &Eacute;trang&egrave;res de Paris</li>
        <li>Sanctuary of Our Lady of Lourdes</li><li>London Korean Catholic Church</li>
        <li>Gwandukjeong Martyrs Memorial Centre, Daegu</li>
      </ul>
      <ul aria-hidden="true">
        <li>Tallaght University Hospital</li><li>Rua Red</li><li>The Civic Theatre</li>
        <li>Clondalkin Lodge</li><li>Mulhuddart Community Centre</li><li>Presentation Sisters</li>
        <li>Missionary Sisters of St Columban</li><li>Dalgan Park</li><li>TU Dublin</li>
        <li>National Concert Hall</li><li>Our Lady of Dolours, Dolphin&rsquo;s Barn</li>
        <li>Church of the Three Patrons, Rathgar</li><li>HSE EVE Goirtin Hub</li>
        <li>Morning Star Hostel</li><li>Missions &Eacute;trang&egrave;res de Paris</li>
        <li>Sanctuary of Our Lady of Lourdes</li><li>London Korean Catholic Church</li>
        <li>Gwandukjeong Martyrs Memorial Centre, Daegu</li>
      </ul>
    </div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap split split-center">
    <div class="reveal">
      <p class="eyebrow">For organisations</p>
      <h2>Are you a nursing home, hospital or parish?</h2>
      <p class="lead mt-3">Tell us your room and your date. Enquiring takes less than two
         minutes, and everything except the room arrives with us &mdash; players, instruments,
         stands, the programme, the insurance.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="partner.html">Partner with us <span class="arrow">&rarr;</span></a>
        <a class="btn btn-quiet" href="{_MAIL_PARTNER_HOME}">Email, two minutes</a>
      </div>
    </div>
    <div class="reveal">
      <ul class="checklist">
        <li><strong>Care homes and hospitals</strong> &mdash; thirty to sixty minutes in the day
            room or the atrium, acoustic, nothing for the audience to pay.</li>
        <li><strong>Parishes and religious communities</strong> &mdash; liturgical music, or a
            concert after Mass. Roughly sixteen of our twenty outreach performances were in
            sacred places.</li>
        <li><strong>Community centres</strong> &mdash; a term-long beginners&rsquo; course in your
            room; you provide the room and a contact, we provide the rest.</li>
        <li><strong>Councils, trusts and companies</strong> &mdash; fund a season, fund a place,
            or bring your people. Every partnership comes with a named contact and a dated
            report.</li>
      </ul>
    </div>
  </div>
</section>

{CTA}"""

# ---------------------------------------------------------------------------
# About
# ---------------------------------------------------------------------------

ABOUT = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">About us</p>
    <h1>We teach people to play. And we go where the music does not.</h1>
    <p><span class="brandname">Classical Music for Everyone</span> is a Dublin social
       enterprise that brings classical music to the places it reaches least. We play live in
       care homes, hospitals and parishes, run ensembles in which older participants play
       themselves, and hold listening talks anyone can come to. Neither age, health nor income
       decides who gets to hear music.</p>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <dl class="glance reveal">
      <div><dt>Founded</dt><dd>January 2024<small>Dublin, Ireland</small></dd></div>
      <div><dt>What we run</dt><dd>Five programmes<small>two pillars: Learning and Sharing</small></dd></div>
      <div><dt>Where we have played</dt><dd>Four countries<small>Ireland, France, the UK, Korea</small></dd></div>
      <div><dt>Status</dt><dd>Volunteer-led<small>forming a not-for-profit CLG</small></dd></div>
    </dl>
  </div>
</section>

<section>
  <div class="wrap split split-wide split-center">
    <div class="reveal">
      <p class="eyebrow">Mission</p>
      <p class="statement">Live classical music, <em>genuinely available to everyone</em> —
         whatever their age, mobility, income or prior knowledge.</p>
      <p class="mt-3">By teaching people to play, playing alongside them, and bringing music to
         the places it does not normally reach.</p>
      <p class="eyebrow mt-4">Vision</p>
      <p class="statement statement-sm">An Ireland in which every community has a way into
         making music together, <em>led by educators in secure, properly paid work.</em></p>
    </div>
    <figure class="reveal">
      <div class="photo photo-4x5">
        <img src="images/clarinet.jpg" width="1400" height="1400"
             alt="Andrew Seohyeon Kim playing the clarinet during a parish liturgy">
      </div>
      <figcaption>A parish liturgy in Dublin. The community work and the church work are the
        same practice.</figcaption>
    </figure>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Values</p>
      <h2>Five, and each one costs us something.</h2>
    </div>
    <ol class="values reveal">
      <li><i>01</i><b>Dignity</b><span>Everyone is someone who can still create, whatever their age or health.</span></li>
      <li><i>02</i><b>Accessibility</b><span>We lower the barriers of price, distance and unfamiliarity.</span></li>
      <li><i>03</i><b>Accompaniment</b><span>A whole term alongside people, not a one-off visit.</span></li>
      <li><i>04</i><b>Community</b><span>Music that connects people across age, background and language.</span></li>
      <li><i>05</i><b>Hope</b><span>No dramatic transformation promised. Small, real moments, counted.</span></li>
    </ol>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">What we run</p>
      <h2>Five programmes, two pillars, one circuit.</h2>
    </div>
    <div class="reveal">{dg.loop(L)}</div>
    <div class="btn-row reveal">
      <a class="btn btn-primary" href="programmes.html">All five in detail <span class="arrow">&rarr;</span></a>
      <a class="btn btn-quiet" href="get-involved.html">Ways to take part</a>
    </div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Where we have played</p>
      <h2>Rooms music does not usually enter.</h2>
      <p>Care homes, religious communities, parishes, a hospital, a homeless hostel, an HSE day
         service, community centres, a university &mdash; and the National Concert Hall, attended
         together.</p>
    </div>
    <ul class="names reveal">
      <li>Tallaght University Hospital</li><li>Rua Red, Tallaght</li><li>Clondalkin Lodge</li>
      <li>Warrenmount, Dublin 8</li><li>Mulhuddart Community Centre</li>
      <li>Missionary Sisters of St Columban, Co. Wicklow</li><li>Franciscan Missionaries of Mary</li>
      <li>Dalgan Park, Co. Meath</li><li>Kilmessan Church</li><li>Dysart Parish, Co. Westmeath</li>
      <li>HSE EVE Goirtin Hub</li><li>Morning Star Hostel</li><li>TU Dublin</li>
      <li>National Concert Hall</li><li>Our Lady of Dolours, Dolphin&rsquo;s Barn</li>
      <li>Church of the Three Patrons, Rathgar</li><li>Carmelite Community Centre</li>
      <li>Blessed Sacrament Chapel</li><li>Sanctuary of Our Lady of Lourdes</li>
      <li>Missions &Eacute;trang&egrave;res de Paris</li><li>Palais Brongniart, Paris</li>
      <li>London Korean Catholic Church</li><li>Gwandukjeong Martyrs Memorial Centre, Daegu</li>
    </ul>
    <p class="tiny mt-3 reveal">Our evidence is participation, retention and testimony, not
       measured outcome. What has and has not been proved is set out on
       <a class="link" href="impact.html#transparency">the Impact page</a>.</p>
  </div>
</section>

<section class="band-photo" id="founder">
  <img src="images/organ.jpg" alt="" width="1400" height="1050">
  <div class="wrap split split-center">
    <div class="reveal">
      <p class="eyebrow">The founder</p>
      <h2 class="h-lg">Andrew Seohyeon Kim</h2>
      <p class="lead mt-3">Clarinettist, organist and community music practitioner. He is in the
         room for all of it: tutor, speaker, driver, clarinettist and conductor are one person.</p>
      <div class="btn-row"><a class="btn btn-on-dark" href="founder.html">Who he is, and how he works <span class="arrow">&rarr;</span></a></div>
    </div>
    <figure class="reveal">
      <div class="photo photo-4x5" style="max-width:300px">
        <img src="images/ruared-andrew.jpg" width="933" height="1400"
             alt="Andrew Seohyeon Kim playing the clarinet beneath stained-glass windows">
      </div>
    </figure>
  </div>
</section>

<section class="band-raised" id="identity">
  <div class="wrap split split-wide split-center">
    <div class="reveal">
      <p class="eyebrow">Identity</p>
      <h2>The gold falls on <em>Everyone</em>.</h2>
      <p class="lead mt-3">The mark, the colours, the type and the rules for using them are
         published on a page of their own, so that anyone printing our name can hold us to the
         standard.</p>
      <div class="btn-row"><a class="btn btn-quiet" href="identity.html">The mark, and what it commits us to <span class="arrow">&rarr;</span></a></div>
    </div>
    <figure class="reveal mark-plate">
      <img src="assets/logo-horizontal.svg" width="341" height="131"
           alt="The Classical Music for Everyone mark: a treble clef beside the wordmark, with &lsquo;Everyone&rsquo; set large and in gold">
      <figcaption>The horizontal mark, adopted 17 August 2026.</figcaption>
    </figure>
  </div>
</section>

{CTA}"""


# ---------------------------------------------------------------------------
# The founder — an artist's profile, not a CV
#
# Facts follow 04 — Founder Profile. The record is still here, complete, but
# folded into an accordion so the page leads with who he is and how he works.
# ---------------------------------------------------------------------------

FOUNDER = f"""<section class="founder-hero">
  <div class="wrap founder-grid">
    <figure class="lift lift-2">
      <div class="photo photo-4x5">
        <img src="images/founder-portrait.jpg" width="790" height="1400"
             alt="Andrew Seohyeon Kim playing the clarinet beneath stained-glass windows">
      </div>
    </figure>
    <div>
      <p class="eyebrow lift lift-1">The founder</p>
      <h1 class="lift lift-2">Andrew Seohyeon Kim<span class="founder-kr">김서현</span></h1>
      <p class="founder-role lift lift-3">Clarinettist, organist and community music practitioner.
         Founder of <span class="brandname">Classical Music for Everyone</span> and the Letters
         Ensemble. Dublin.</p>
      <p class="statement lift lift-3">&ldquo;Rather than expecting people to come to music,
         <em>we bring music to them.</em>&rdquo;</p>
      <div class="lift lift-4">{social_links("Email")}</div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split split-wide split-center">
    <div class="reveal">
      <p class="eyebrow">How he works</p>
      <h2>He is in the room for all of it.</h2>
      <p class="lead mt-3">The tutor at the recorder class, the speaker at the lecture-recitals,
         the person who books the outing, the clarinettist at the care home and the conductor of
         the ensemble that plays there are the same person.</p>
      <p class="mt-3">That is a limit as much as a description. It is why the organisation says
         five programmes rather than fifty sessions a week, and why employing music educators
         properly is its second social aim. The work does not scale on one person, and it is not
         meant to.</p>
    </div>
    <div class="reveal">
      <dl class="facts">
        <dt>Based</dt><dd>Dublin, Ireland</dd>
        <dt>Trained</dt><dd>BMus (Hons) in Performance, TU Dublin Conservatoire, 2026</dd>
        <dt>Clarinet</dt><dd>Dr Paul Roe &middot; organ with Simon Harden</dd>
        <dt>Posts</dt><dd>Music Director, Our Lady of Dolours, Dolphin&rsquo;s Barn &middot; Organist,
            Church of the Three Patrons, Rathgar</dd>
        <dt>Founded</dt><dd><span class="brandname">Classical Music for Everyone</span> and the
            Letters Ensemble, January 2024</dd>        <dt>Languages</dt><dd>English &middot; Korean</dd>
      </dl>
    </div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">On stage, August 2026</p>
      <h2 class="h-md">South Dublin Live: a hospital atrium and a black-box theatre.</h2>
    </div>
    <div class="gallery stagger">
      <figure><div class="photo photo-3x2"><img src="images/ruared-stage.jpg" width="1400" height="933"
          alt="The trio on the Rua Red stage, seen from the audience"></div>
        <figcaption>Rua Red, 29 August. Photograph: Ben Ryan / South Dublin County Council</figcaption></figure>
      <figure><div class="photo photo-4x5"><img src="images/tuh-andrew.jpg" width="1050" height="1400"
          alt="Andrew Seohyeon Kim playing the clarinet in the hospital Atrium"></div>
        <figcaption>Tallaght University Hospital, 20 August.</figcaption></figure>
      <figure><div class="photo photo-4x5"><img src="images/ruared-andrew.jpg" width="933" height="1400"
          alt="Andrew Seohyeon Kim playing the clarinet under stage light"></div>
        <figcaption>Rua Red. Photograph: Ben Ryan / South Dublin County Council</figcaption></figure>
      <figure><div class="photo photo-3x2"><img src="images/tuh-trio.jpg" width="1400" height="787"
          alt="Soprano, piano and clarinet performing in the hospital Atrium"></div>
        <figcaption>Shared Voices of Care, with Dr Soo-Jung Ann and Hyelee Jung.</figcaption></figure>
    </div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap aside-fig">
    <figure class="reveal">
      <div class="photo photo-4x5" style="max-width:440px">
        <img src="images/founder-speaking.jpg" width="1050" height="1400"
             alt="Andrew Seohyeon Kim speaking at a lecture-recital with a microphone">
      </div>
    </figure>
    <div class="reveal">
      <p class="eyebrow">Where the practice comes from</p>
      <h2 class="h-md">A church organ loft, and a room of retired sisters.</h2>
      <p class="mt-3">Since 2022 he has played weekly in two Dublin parishes: Holy Week
         liturgies, school and remembrance Masses, funerals, parish concerts. For parish and
         religious audiences the work is a lay apostolate through music, a ministry of presence.
         It is the same practice as the community work, described to the people who asked for it.</p>
      <p class="mt-3">His final-year research was a ten-week recorder ensemble he designed and
         led for seven retired Presentation Sisters at Warrenmount. All seven completed and
         performed in public. The whole teaching programme is built on it.</p>
      <div class="quote mt-4">
        <p>&ldquo;Through music, he offers encouragement, dignity, and spiritual accompaniment to
           those who may otherwise feel isolated.&rdquo;</p>
        <cite>Donal Roche, Auxiliary Bishop of Dublin &middot; 16 February 2026</cite>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Collaborating artists</p>
      <h2 class="h-md">The people he plays with.</h2>
    </div>
    <div class="grid grid-3 stagger">
      <article class="card card-media">
        <div class="photo photo-4x3"><img src="images/ruared-pianist.jpg" width="1400" height="933"
             alt="Dr Soo-Jung Ann at the piano on the Rua Red stage"></div>
        <div class="card-body"><span class="kicker">Piano</span><h3>Dr Soo-Jung Ann</h3>
          <p>Doctor of Music, RIAM 2022. First prize, 58th Maria Canals International Competition.</p></div>
      </article>
      <article class="card card-media">
        <div class="photo photo-4x3"><img src="images/ruared-soprano.jpg" width="933" height="1400"
             alt="Soprano Hyelee Jung singing at Rua Red"></div>
        <div class="card-body"><span class="kicker">Soprano</span><h3>Hyelee Jung</h3>
          <p>Silla University; Conservatorio di Santa Cecilia, Rome.</p></div>
      </article>
      <article class="card card-media">
        <div class="photo photo-4x3"><img src="images/tuh-haegeum.jpg" width="1400" height="934"
             alt="Jaewon Kim playing the haegeum at Tallaght University Hospital"></div>
        <div class="card-body"><span class="kicker">Haegeum</span><h3>Jaewon Kim</h3>
          <p>Guest artist for <em>Shared Voices of Care</em> and <em>An Autumn Concert</em>, 2026.</p></div>
      </article>
    </div>
    <p class="tiny mt-3 reveal">Rua Red photographs: Ben Ryan / South Dublin County Council.
       Hospital photographs: Tallaght University Hospital.</p>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap narrow">
    <div class="section-head reveal">
      <p class="eyebrow">The record</p>
      <h2 class="h-md">Training, roles and the rest, if you want it.</h2>
    </div>
    <div class="faq-list record">
      <details class="faq reveal"><summary>Education and training</summary>
        <ul class="plainlist">
          <li><strong>BMus (Hons) in Performance</strong> &mdash; TU Dublin Conservatoire, 2022&ndash;2026</li>
          <li><strong>Clarinet</strong> &mdash; Dr Paul Roe &middot; <strong>Organ</strong> &mdash; Simon Harden
              &middot; <strong>Cello</strong> &mdash; Arun Rao &middot; <strong>Piano</strong> &mdash; Sam Armstrong</li>
          <li><strong>Conducting</strong> &mdash; Irish Association of Youth Orchestras &middot; London
              Conducting Workshop &middot; TU Dublin Special Studies</li>
          <li><strong>Social enterprise</strong> &mdash; TU Dublin Venture Lab, from September 2024</li>
          <li><strong>Scholarship</strong> &mdash; Myongdohoe, Lay Apostolate Committee, Catholic
              Bishops&rsquo; Conference of Korea, from March 2025</li>
        </ul>
      </details>
      <details class="faq reveal"><summary>Current roles</summary>
        <ul class="plainlist">
          <li><strong>Founder &amp; Project Lead</strong> &mdash; <span class="brandname">Classical Music for Everyone</span>, from January 2024</li>
          <li><strong>Founder, Music Director &amp; Conductor</strong> &mdash; Letters Ensemble, from January 2024</li>
          <li><strong>Music Director</strong> &mdash; Our Lady of Dolours Church, Dolphin&rsquo;s Barn, from September 2022</li>
          <li><strong>Organist</strong> &mdash; Church of the Three Patrons, Rathgar, from September 2023</li>
          <li><strong>Student Ambassador</strong> &mdash; TU Dublin, from August 2024</li>
        </ul>
      </details>
      <details class="faq reveal"><summary>Before this</summary>
        <ul class="plainlist">
          <li><strong>Baram</strong>, 2023&ndash;24 &mdash; a Korean traditional and classical duo; embassy events and cultural exhibitions</li>
          <li><strong>Chorus of Angels</strong>, 2023 &mdash; a children&rsquo;s choir for Korean and mixed-heritage children in Dublin</li>
          <li><strong>At Home Ensemble Project</strong>, 2020&ndash;21 &mdash; a virtual wind ensemble during Covid-19</li>
        </ul>
      </details>
      <details class="faq reveal"><summary>Volunteering</summary>
        <ul class="plainlist">
          <li>World Youth Day, Lisbon, 2023 &mdash; logistics, music, liturgy, language assistance</li>
          <li>ICA ClarinetFest, Dublin, 2024 &mdash; support and interpreting</li>
          <li>13th Dublin International Piano Competition, 2025 &mdash; Team Harmony</li>
          <li>Jubilee of Youth, Rome, 2025 &middot; Korea Festival, Farmleigh House, 2025</li>
        </ul>
        <p class="small">Portugal and Italy appear here as volunteering. The four countries in our
           record are the four we have <em>performed</em> in.</p>
      </details>
      <details class="faq reveal"><summary>Writing and press</summary>
        <ul class="plainlist">
          <li><strong>Kyunghyang Magazine</strong>, May 2026 &mdash; commissioned article for &ldquo;Young people, how are you?&rdquo;</li>
          <li><strong>Catholic University student paper</strong>, March 2026 &mdash; &ldquo;F&aacute;ilte go h&Eacute;irinn!&rdquo;</li>
          <li><strong>Concert review</strong>, March 2025 &mdash; &ldquo;Music: a gift God gave to everyone&rdquo;</li>
        </ul>
      </details>
    </div>
  </div>
</section>

<section class="band-photo">
  <img src="images/organ.jpg" alt="" width="1400" height="1050">
  <div class="wrap narrow center reveal">
    <p class="eyebrow center-row">Write to him</p>
    <h2 class="h-lg">Every enquiry reaches him directly.</h2>
    <p class="lead mt-2">One line is enough: what you are asking about, and roughly where you are.</p>
    <div class="btn-row center-row">
      <a class="btn btn-accent" href="mailto:sby05034@gmail.com?subject=Enquiry%20—%20Classical%20Music%20for%20Everyone">Email <span class="arrow">&rarr;</span></a>
      <a class="btn btn-on-dark" href="contact.html">All contact details</a>
    </div>
  </div>
</section>"""


# ---------------------------------------------------------------------------
# Programmes
# ---------------------------------------------------------------------------

PROGRAMMES = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Programmes</p>
    <h1>Five programmes. None of them is the main one.</h1>
    <p>Three teach people to play; two bring the music to the room. Same length, same facts,
       same order for each.</p>
  </div>
</section>

<section class="tight">
  <div class="wrap reveal">
    <div class="table-scroll">
      <table>
        <thead><tr>
          <th scope="col">Programme</th><th scope="col">Pillar</th>
          <th scope="col">Status</th><th scope="col">Delivered to date</th>
        </tr></thead>
        <tbody>
          <tr><td><strong><a class="link" href="programmes/recorder-ensemble.html">Free Recorder Ensemble course</a></strong></td><td>Learning</td>
              <td>Running</td><td>Pilot complete; first community class from Sept 2026</td></tr>
          <tr><td><strong><a class="link" href="programmes/getting-to-know.html">Getting to Know Classical Music</a></strong></td><td>Learning</td>
              <td>Running · free</td><td>17 lecture-recitals · 143 attendances</td></tr>
          <tr><td><strong><a class="link" href="programmes/concert-companion.html">Concert Guide &amp; Companion</a></strong></td><td>Learning</td>
              <td>Running</td><td>10 recorded outings, incl. two summers at the BBC Proms</td></tr>
          <tr><td><strong><a class="link" href="programmes/outreach-concerts.html">Outreach Concerts</a></strong></td><td>Sharing</td>
              <td>Running</td><td>20 performances · 4 countries · 15+ venues</td></tr>
          <tr><td style="padding-inline-start:34px">↳ Bringing Music to Sacred Places</td><td>Sharing</td>
              <td>Sub-strand</td><td>Around 16 of the 20 outreach performances</td></tr>
          <tr><td><strong><a class="link" href="programmes/letters-ensemble.html">Letters Ensemble</a></strong></td><td>Sharing</td>
              <td>Running</td><td>4 formal concerts · weekly rehearsals since Jan 2024</td></tr>
        </tbody>
      </table>
    </div>
    <div class="mt-4">{dg.loop(L)}</div>
  </div>
</section>

<section>
  <div class="wrap split split-wide split-center">
    <figure class="reveal">
      <div class="photo photo-4x3">
        <img src="images/conducting.jpg" width="1400" height="1050" alt="Conducting a small ensemble in a community setting">
      </div>
      <figcaption>Every course ends the same way — a concert, however small.</figcaption>
    </figure>
    <div class="reveal">
      <p class="eyebrow">Learning</p>
      <h2 class="h-md">Free Recorder Ensemble course</h2>
      <p class="lead mt-2">A term for complete beginners, ending in a concert.</p>
      <p class="mt-2">Gentle on the hands, quick to a first sound, made for playing together. Nothing to buy, nothing to read beforehand.</p>
      <dl class="facts">
        <dt>Length</dt><dd>One term, weekly · 60–90 minutes</dd>
        <dt>For</dt><dd>Complete beginners — no music reading assumed</dd>
        <dt>Instrument</dt><dd>Descant recorder — we advise on buying one, supply at cost, or lend you one</dd>
        <dt>Ends with</dt><dd>A short concert for family and friends</dd>
        <dt>Running now</dt><dd>Mulhuddart Community Centre, Dublin 15 · Wednesdays 7:00–8:00pm from 9 September 2026 · free</dd>
      </dl>
      <div class="btn-row"><a class="btn btn-quiet" href="programmes/recorder-ensemble.html">Full detail <span class="arrow">&rarr;</span></a></div>
    </div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap split split-wide split-center split-flip">
    <figure class="reveal">
      <div class="photo photo-4x3">
        <img src="images/lecture-recital.jpg" width="1400" height="1050" alt="A lecture-recital in progress">
      </div>
      <figcaption>A lecture-recital in progress.</figcaption>
    </figure>
    <div class="reveal">
      <p class="eyebrow">Learning</p>
      <h2 class="h-md">Getting to Know Classical Music</h2>
      <p class="lead mt-2">Free lecture-recitals for people with no prior knowledge.</p>
      <p class="mt-2">Roughly monthly, for anyone who never knew where to start. Nothing to prepare.</p>
      <dl class="facts">
        <dt>Three stages</dt><dd>Getting Closer · Experiencing Together · Discovering My Taste</dd>
        <dt>Seasonal specials</dt><dd>European summer festivals, the BBC Proms, Wexford Opera Festival, Christmas</dd>
        <dt>Group size</dt><dd>Typically 6–14</dd>
        <dt>Cost</dt><dd>Free</dd>
        <dt>To date</dt><dd>17 sessions · 143 attendances</dd>
      </dl>
      <div class="btn-row"><a class="btn btn-quiet" href="programmes/getting-to-know.html">Full detail <span class="arrow">&rarr;</span></a></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split split-wide split-center">
    <figure class="reveal">
      <div class="photo photo-4x3">
        <img src="images/quartet-hall.jpg" width="1400" height="1050" alt="An ensemble performing in a bright hall">
      </div>
      <figcaption>An ensemble performing in a bright hall.</figcaption>
    </figure>
    <div class="reveal">
      <p class="eyebrow">Learning</p>
      <h2 class="h-md">Concert Guide &amp; Companion</h2>
      <p class="lead mt-2">Small groups accompanied to concerts they would not attend alone.</p>
      <p class="mt-2">Prepared before, sat with during, talked about after. The barrier is rarely the ticket.</p>
      <dl class="facts">
        <dt>Group size</dt><dd>About five</dd>
        <dt>Been to</dt><dd>National Symphony Orchestra · Irish National Opera · RTÉ Concert Orchestra · the NCH International Series</dd>
        <dt>Further afield</dt><dd>The BBC Proms, in two summers</dd>
        <dt>Cost</dt><dd>Tickets can be as little as £8</dd>
        <dt>To date</dt><dd>10 recorded outings</dd>
      </dl>
      <div class="btn-row"><a class="btn btn-quiet" href="programmes/concert-companion.html">Full detail <span class="arrow">&rarr;</span></a></div>
    </div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap split split-wide split-center split-flip">
    <figure class="reveal">
      <div class="photo photo-4x3">
        <img src="images/care-christmas.jpg" width="1400" height="1050" alt="A quartet performing in a care setting at Christmas">
      </div>
      <figcaption>A quartet performing in a care setting at Christmas.</figcaption>
    </figure>
    <div class="reveal">
      <p class="eyebrow">Sharing</p>
      <h2 class="h-md">Outreach Concerts</h2>
      <p class="lead mt-2">Live performance brought into the rooms people are already in.</p>
      <p class="mt-2">From a hostel in Dublin 7 to a shrine in Daegu. We bring everything but the room.</p>
      <dl class="facts">
        <dt>Where</dt><dd>Care homes, parishes, hospitals, hostels, community spaces</dd>
        <dt>Growing into</dt><dd>Wicklow, Meath and Louth</dd>
        <dt>Aim</dt><dd>Ten or more a year</dd>
        <dt>Since</dt><dd>2023</dd>
        <dt>To date</dt><dd>20 performances · 15+ venues · 4 countries</dd>
      </dl>
      <div class="btn-row"><a class="btn btn-quiet" href="programmes/outreach-concerts.html">Full detail <span class="arrow">&rarr;</span></a></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split split-wide split-center">
    <figure class="reveal">
      <div class="photo photo-4x3">
        <img src="images/letters-ensemble.jpg" width="1400" height="1050" alt="The Letters Ensemble with their instruments">
      </div>
      <figcaption>The Letters Ensemble with their instruments.</figcaption>
    </figure>
    <div class="reveal">
      <p class="eyebrow">Sharing</p>
      <h2 class="h-md">Letters Ensemble</h2>
      <p class="lead mt-2">Amateur musicians living in Dublin, rehearsing every Saturday.</p>
      <p class="mt-2">Irish and Korean traditional, sacred, accessible arrangements. New amateur players welcome.</p>
      <dl class="facts">
        <dt>Founded</dt><dd>January 2024, by amateur musicians living in Dublin</dd>
        <dt>Rehearsals</dt><dd>Every Saturday</dd>
        <dt>Repertoire</dt><dd>Irish traditional · Korean traditional · sacred · accessible arrangements</dd>
        <dt>Open to</dt><dd>Amateur musicians</dd>
        <dt>To date</dt><dd>4 formal concerts</dd>
      </dl>
      <div class="btn-row"><a class="btn btn-quiet" href="programmes/letters-ensemble.html">Full detail <span class="arrow">&rarr;</span></a></div>
    </div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">How a course is built</p>
      <h2>The first satisfying sound arrives in week one.</h2>
      <p>Reach something worth hearing early, move as one group, finish in front of people.</p>
    </div>
    <div class="reveal">{dg.term(L)}</div>

    <div class="split split-wide split-center mt-4">
      <div class="reveal">
        <p class="eyebrow">Where the model came from</p>
        <h3 class="h-md">The pilot.</h3>
        <p class="statement statement-sm mt-2">Seven retired sisters. Ten weekly hours.
           <em>All seven completed</em> and played in public.</p>
        <p class="mt-3">Warrenmount, Dublin 8, then an Easter concert of nine pieces at
           Clondalkin Lodge. Completed as Bachelor of Music research at TU Dublin Conservatoire.</p>
      </div>
      <div class="reveal">
        <ul class="checklist">
          <li><strong>Connection</strong> — a warm, weekly reason to gather.</li>
          <li><strong>Dignity and achievement</strong> — the quiet pride of &ldquo;I can make music.&rdquo;</li>
          <li><strong>Gentle stimulation</strong> — memory, coordination, breath and focus.</li>
          <li><strong>Friendship</strong> — bonds that often outlast the term.</li>
        </ul>
        <div class="callout mt-3">
          <span class="tag tag-live">Running now</span>
          <p class="mt-1"><strong>Mulhuddart Community Centre, Dublin 15.</strong>
             Wednesdays 7:00–8:00pm from 9 September 2026, twelve weeks, free — ending with a
             festive concert before Christmas.</p>
          <div class="btn-row"><a class="btn btn-accent" href="get-involved.html">Join the class <span class="arrow">→</span></a></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap narrow reveal">
    <p class="eyebrow">Sub-strand</p>
    <h2 class="h-md">Bringing Music to Sacred Places</h2>
    <p class="mt-2">Parishes, shrines, convents, liturgies and retired religious communities:
       roughly sixteen of the twenty outreach performances. To religious audiences, a lay
       apostolate through music.</p>
  </div>
</section>

{CTA}"""


# ---------------------------------------------------------------------------
# Get involved
# ---------------------------------------------------------------------------

GET_INVOLVED = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Get involved</p>
    <h1>Four ways in. Pick the one that sounds like you.</h1>
    <p>No audition, no experience assumed, nothing to prepare. If you are not sure which one
       fits, say so — that is a normal enquiry.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <h2 class="sr-only">Ways to take part</h2>
    <div class="grid grid-2 stagger">
      <article class="card card-media">
        <div class="photo photo-3x2"><img src="images/conducting.jpg" width="1400" height="933"
             alt="A weekly class in a community room in Dublin"></div>
        <div class="card-body">
          <span class="kicker">For absolute beginners</span>
          <h3>Learn to play</h3>
          <p>Join the recorder ensemble course. First notes in week one, reading music from
             zero, your own part in the ensemble, and a concert at the end of term.</p>
          <div class="meta">Mulhuddart Community Centre, D15 · Wednesdays 7:00–8:00pm ·
             from 9 September 2026 · free</div>
        </div>
      </article>
      <article class="card card-media">
        <div class="photo photo-3x2"><img src="images/lecture-recital.jpg" width="1400" height="933"
             alt="A lecture-recital in progress"></div>
        <div class="card-body">
          <span class="kicker">If you would rather listen first</span>
          <h3>Come and listen</h3>
          <p>A free lecture-recital, or a small group going to a concert together — prepared
             beforehand, sat through together, talked about after. Especially welcome if you
             would never go alone, or are new to Ireland.</p>
          <div class="meta">Roughly monthly · groups of about five</div>
        </div>
      </article>
      <article class="card card-media">
        <div class="photo photo-3x2"><img src="images/letters-ensemble.jpg" width="1400" height="933"
             alt="The Letters Ensemble with their instruments"></div>
        <div class="card-body">
          <span class="kicker">If you already play</span>
          <h3>Play with us</h3>
          <p>The Letters Ensemble is open to amateur musicians living in Dublin — Saturday
             rehearsals and concerts in community settings. Volunteers also help with outreach
             logistics.</p>
          <div class="meta">Strings, winds and more welcome</div>
        </div>
      </article>
      <article class="card card-media">
        <div class="photo photo-3x2"><img src="images/community-room.jpg" width="1400" height="933"
             alt="A musician playing in a plain community room"></div>
        <div class="card-body">
          <span class="kicker">If you run a venue</span>
          <h3>Host or partner</h3>
          <p>Invite an outreach concert, or host a course for your community. We carry public
             liability insurance and complete Garda vetting where the work requires it.</p>
          <div class="meta">Dublin, Wicklow, Meath, Louth and beyond</div>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">How the four fit together</p>
      <h2>They are four sentences, not four application forms.</h2>
      <p>Nobody has to pick the right one. Most of the people playing with us now started by
         coming to listen, and two of the rooms we play in were offered by someone who had come
         to a concert.</p>
    </div>
    <div class="reveal">{dg.pathways(L)}</div>
  </div>
</section>

<section>
  <div class="wrap split split-wide split-center">
    <div class="reveal">
      <p class="eyebrow">What happens after you write</p>
      <h2 class="h-md">No form, no waiting list, no interview.</h2>
      <p class="mt-3">Every enquiry goes to the founder directly and is answered by a person who
         will be in the room with you. There is nothing to fill in and nothing to attach.</p>
    </div>
    <div class="reveal">
      <ol class="steps">
        <li><strong>You write one line.</strong> What you are asking about, and roughly where
            you are. That is genuinely enough.</li>
        <li><strong>We reply with the practical details</strong> — the venue, the day, the time,
            what it costs, and what to bring. Usually within a few days.</li>
        <li><strong>You come once and see.</strong> Nobody is committing to a term by turning up
            to one session.</li>
        <li><strong>If it is not the right fit,</strong> we will say so and point you at
            something that is, including things we do not run.</li>
      </ol>
    </div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">For venues</p>
      <h2>You provide a room and a name. We provide the rest.</h2>
    </div>
    <div class="exchange reveal">
      <div class="exchange-side">
        <span class="kicker">You provide</span>
        <p class="exchange-count">Four things</p>
        <ul class="checklist mt-2">
          <li>A warm room seating ten to twelve in a circle, weekly for the term</li>
          <li>Help spreading the word locally</li>
          <li>One named contact person</li>
          <li>Nothing else — no equipment, no admin, no piano</li>
        </ul>
      </div>
      <div class="exchange-side exchange-ours">
        <span class="kicker">We provide</span>
        <p class="exchange-count">Everything else</p>
        <ul class="checklist mt-2">
          <li>The tutor and the full curriculum</li>
          <li>All scores and weekly materials, printed at our cost</li>
          <li>Guidance on low-cost instruments, and loans where needed</li>
          <li>The end-of-term concert</li>
          <li>Insurance and vetting documentation</li>
        </ul>
      </div>
    </div>
    <div class="callout reveal mt-4">
      <p><strong>On cost.</strong> Every programme keeps free and discounted places. Where a venue
         can pay a facilitation fee from its own budget, participation is free for everyone in the
         room — and that contribution keeps a door open elsewhere. Where it cannot, we will still
         talk.</p>
    </div>
  </div>
</section>

<section class="band-photo">
  <img src="images/quartet-hall.jpg" alt="" width="1400" height="788">
  <div class="wrap narrow center reveal">
    <p class="eyebrow center-row">Next step</p>
    <h2 class="h-lg">Write one line.</h2>
    <p class="lead mt-2">Tell us which of the
       four sounds like you and roughly where you are. We will answer with the practical
       details.</p>
    <div class="btn-row center-row">
      <a class="btn btn-accent" href="mailto:sby05034@gmail.com?subject=Getting%20involved%20with%20CMFE">Email us <span class="arrow">→</span></a>
      <a class="btn btn-on-dark" href="contact.html">All contact details</a>
    </div>
  </div>
</section>"""


# ---------------------------------------------------------------------------
# News
# ---------------------------------------------------------------------------

NEWS = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">What&rsquo;s on</p>
    <h1>What is coming, and what happened this year.</h1>
    <p>One class enrolling, one concert with the door open. The full ledger since 2023 is on
       <a class="crumb" href="archive.html">the record</a>.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Coming up</p>
      <h2>Autumn 2026.</h2>
    </div>
{WHATS_ON}
    <div class="callout reveal mt-3">
      <p><strong>December 2026 —</strong> a festive concert for family and friends closes the
         first Mulhuddart course. Details to follow.</p>
    </div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">This year</p>
      <h2>2026 so far.</h2>
    </div>
    <div class="grid grid-3 stagger">
      <article class="card card-media">
        <div class="photo photo-3x2"><img src="images/ruared-trio.jpg" width="1400" height="933"
             alt="Clarinet, soprano and piano taking a bow on the Rua Red stage"></div>
        <div class="card-body">
          <span class="tag tag-live">First public funding</span>
          <h3 class="mt-1">South Dublin Live 2026</h3>
          <p>Selected by SDCC&rsquo;s Arts Office: the first work funded by anyone other than
             ourselves.</p>
          <div class="meta">August 2026 · SDCC Arts Office</div>
        </div>
      </article>
      <article class="card card-media">
        <div class="photo photo-3x2"><img src="images/tuh-trio.jpg" width="1400" height="787"
             alt="Soprano, piano and clarinet performing in the Atrium of Tallaght University Hospital"></div>
        <div class="card-body">
          <span class="kicker">20 August 2026</span>
          <h3>Shared Voices of Care</h3>
          <p>Thirty minutes, acoustic, drop-in, in the hospital Atrium, with guest haegeum
             artist Jaewon Kim. For patients, families, visitors and staff.</p>
          <div class="meta">Tallaght University Hospital</div>
        </div>
      </article>
      <article class="card card-media">
        <div class="photo photo-3x2"><img src="images/ruared-stage.jpg" width="1400" height="933"
             alt="The trio on the Rua Red stage, seen from the audience"></div>
        <div class="card-body">
          <span class="kicker">29 August 2026</span>
          <h3>Shared Voices of Classical Tradition</h3>
          <p>Sixty minutes for clarinet, piano and soprano in the Performance Space at Rua Red.
             Free admission.</p>
          <div class="meta">Rua Red, Tallaght &middot; photographs Ben Ryan / SDCC</div>
        </div>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap split split-wide split-center">
    <div class="reveal">
      <p class="eyebrow">The record</p>
      <h2>Every session and performance since 2023, on one page.</h2>
      <p class="lead mt-3">A chronicle drawn as four staves, one a year, and the tables under
         it. The milestones, what was planned and not delivered, and what was never written
         down are all there too.</p>
      <div class="btn-row"><a class="btn btn-primary" href="archive.html">Open the record <span class="arrow">&rarr;</span></a></div>
    </div>
    <div>
        <div class="callout reveal mt-3">
          <h3 class="h-sub">Press &amp; publication</h3>
          <ul class="plainlist mt-1">
            <li><strong>Kyunghyang Magazine</strong>, May 2026 — commissioned article for
                &ldquo;Young people, how are you?&rdquo;</li>
            <li><strong>Catholic University student paper</strong>, March 2026 —
                &ldquo;Fáilte go hÉirinn!&rdquo;</li>
            <li><strong>Concert review</strong>, March 2025 — &ldquo;Music: a gift God gave to
                everyone&rdquo;</li>
            <li><strong>The Echo</strong>, August 2026 — advertisements for the Rua Red and
                Tallaght concerts</li>
          </ul>
        </div>
    </div>
  </div>
</section>

{CTA}"""


# ---------------------------------------------------------------------------
# Support
# ---------------------------------------------------------------------------

SUPPORT = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Support</p>
    <h1>Help keep the door open.</h1>
    <p>We are volunteer-led. Support pays for recorders and scores, room hire, and the travel
       that carries music to rooms it would not otherwise reach. Here is what it has done, what
       it becomes, and how to give it.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">What support has already done</p>
      <h2>Support bought a vehicle. The vehicle bought distance.</h2>
      <p>Gifts from individuals in Europe and Korea put a vehicle on the road. Players,
         instruments and stands now travel together to care homes, parishes and hostels that no
         bus timetable reaches &mdash; Wicklow, Meath, Westmeath, and further by arrangement.</p>
    </div>
    <div class="grid grid-4 stagger">
      <div class="card"><span class="kicker">A gift becomes</span><h3>A recorder in someone&rsquo;s hands</h3>
        <p>A descant recorder costs between &euro;8 and &euro;15. We advise on buying one, supply at
           cost, or lend one for the term.</p></div>
      <div class="card"><span class="kicker">A gift becomes</span><h3>Scores nobody has to pay for</h3>
        <p>Every part, arranged so whoever turned up can play it, printed at our cost with
           enlarged notation where eyes need it.</p></div>
      <div class="card"><span class="kicker">A gift becomes</span><h3>A room for a term</h3>
        <p>Where a venue cannot give the room, support hires it &mdash; and a warm room once a
           week is where a course happens.</p></div>
      <div class="card"><span class="kicker">A gift becomes</span><h3>The drive to the next room</h3>
        <p>Fuel for the vehicle donors bought, so a day room in Co. Wicklow costs a morning, not
           a budget line.</p></div>
    </div>
    <p class="tiny mt-3 reveal">No unit costs are quoted here beyond the price of a recorder,
       because the others vary by room and by term. Ask, and we will show you the current
       figures for the programme you have in mind.</p>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">How the money works</p>
      <h2>A paid booking is what keeps a free seat free.</h2>
      <p>We are a social enterprise rather than a pure charity. That is not a technicality &mdash;
         it is what lets the free places survive a dip in goodwill.</p>
    </div>
    <div class="reveal">{dg.subsidy(L)}</div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">How to help</p>
      <h2>Four kinds of support, all of them useful.</h2>
    </div>
    <div class="grid grid-4 stagger">
      <div class="card"><span class="kicker">01</span><h3>Give</h3>
        <p>A one-off or regular gift goes to instruments, materials, room hire and travel. Write
           and we will send the current payment details and say what it funds.</p></div>
      <div class="card"><span class="kicker">02</span><h3>Fund a programme</h3>
        <p>For trusts, foundations, councils and corporate funders: a full proposal, budget and
           activity record on request. <a class="link" href="partner.html">Partner with us</a>
           says what a partnership comes with.</p></div>
      <div class="card"><span class="kicker">03</span><h3>Open a door</h3>
        <p>An introduction to a care home, parish, community centre or hospital is worth as much
           as a donation &mdash; often more.</p></div>
      <div class="card"><span class="kicker">04</span><h3>Give the room</h3>
        <p>A warm room once a week for a term is the most valuable in-kind gift there is. It
           converts directly into free places.</p></div>
    </div>
    <div class="btn-row reveal center-row mt-4">
      <a class="btn btn-accent" href="mailto:sby05034@gmail.com?subject=I%20would%20like%20to%20support%20Classical%20Music%20for%20Everyone">Offer support <span class="arrow">&rarr;</span></a>
      <a class="btn btn-quiet" href="partner.html">For organisations</a>
      <a class="btn btn-quiet" href="mailto:sby05034@gmail.com?subject=Partnership%20and%20funding%20enquiry">Request the proposal</a>
    </div>
    <div class="callout reveal mt-4">
      <p class="small"><strong>Please note.</strong> <span class="brandname">Classical Music for Everyone</span>
         is a volunteer-led social enterprise
         currently formalising as a not-for-profit company limited by guarantee. We are not yet a
         registered charity, so gifts are not eligible for charitable tax relief. We would rather
         say so plainly than let anyone assume otherwise.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap split split-center">
    <div class="reveal">
      <p class="eyebrow">Track record</p>
      <h2 class="h-md">Who has backed this so far.</h2>
      <p class="mt-3">Everything before 2026 was self-funded and voluntary. The full record of
         funding and support, the letters written for the South Dublin Live application, and
         what has not yet been proved are published together on one page.</p>
      <div class="btn-row"><a class="btn btn-quiet" href="impact.html#transparency">Transparency <span class="arrow">&rarr;</span></a></div>
    </div>    <div class="reveal">
      <figure>
        <div class="photo photo-3x2">
          <img src="images/tuh-haegeum.jpg" width="1400" height="934"
               alt="Haegeum player Jaewon Kim performing in the Atrium of Tallaght University Hospital">
        </div>
        <figcaption>Shared Voices of Care, Tallaght University Hospital, 20 August 2026 &mdash; the
          first publicly funded concert.</figcaption>
      </figure>
      <div class="quote mt-4">
        <p>&ldquo;Andrew does not undertake this work from a position of material abundance. Even
           within limited personal financial circumstances, he continues to give generously of his
           time, energy, and talent.&rdquo;</p>
        <cite>Donal Roche, Auxiliary Bishop of Dublin · 16 February 2026</cite>
      </div>
    </div>
  </div>
</section>"""


# ---------------------------------------------------------------------------
# Contact
# ---------------------------------------------------------------------------

CONTACT = """<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Contact</p>
    <h1>Write to us.</h1>
    <p>Every enquiry reaches the founder directly. One line is enough — what you are asking
       about, and roughly where you are.</p>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="reveal">
      <h2>Details</h2>
      <div class="table-scroll mt-3">
        <table><tbody>
          <tr><td><strong>Email</strong></td>
              <td><a class="link" href="mailto:sby05034@gmail.com">sby05034@gmail.com</a></td></tr>
          <tr><td><strong>Phone</strong></td>
              <td><a class="link" href="tel:+353830780635">+353 83 078 0635</a></td></tr>
          <tr><td><strong>Based in</strong></td><td>Dublin, Ireland</td></tr>
          <tr><td><strong>We travel to</strong></td>
              <td>Dublin, Co. Meath, Co. Wicklow, Co. Westmeath — further by arrangement</td></tr>
          <tr><td><strong>Founder</strong></td>
              <td>Andrew Seohyeon Kim, BMus (Hons), TU Dublin Conservatoire</td></tr>
          <tr><td><strong>Languages</strong></td><td>English · 한국어</td></tr>
        </tbody></table>
      </div>
      <p class="small mt-3">We hold public liability insurance and complete
         Garda vetting where the work requires it. Documentation is available to partner venues on
         request.</p>
    </div>
    <div class="reveal">
      <h2>Who writes about what</h2>
      <ul class="checklist mt-3">
        <li><strong>Joining a class</strong> — which venue, and whether you have played anything
            before. &ldquo;Never&rdquo; is a completely normal answer.</li>
        <li><strong>Inviting a concert</strong> — the setting, roughly how many people, and a
            rough time of year.</li>
        <li><strong>Hosting a course</strong> — a room, a day of the week, and a contact person.</li>
        <li><strong>Funding and partnership</strong> — ask for the proposal and budget; we will
            send the current version with the activity record.</li>
        <li><strong>Press and media</strong> — biographies, photographs and programme details on
            request.</li>
      </ul>
      <div class="btn-row">
        <a class="btn btn-accent" href="mailto:sby05034@gmail.com?subject=Enquiry%20—%20Classical%20Music%20for%20Everyone">Email us <span class="arrow">→</span></a>
        <a class="btn btn-quiet" href="get-involved.html">Ways to take part</a>
      </div>
    </div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap narrow center reveal">
    <p class="eyebrow center-row">Organisation</p>
    <h2>Classical Music for Everyone</h2>
    <p class="lead mt-3">A community music social enterprise founded in Dublin
       in January 2024, currently formalising as a not-for-profit company limited by guarantee.
       Volunteer-led. Community music · social enterprise · arts and health.</p>
  </div>
</section>"""


# ---------------------------------------------------------------------------
# Impact — what has changed, and only what the record supports
#
# The page 12 — Brand & Web Master §8 calls "Our impact": dated figures, one
# story, the road ahead, and a transparency block that says what the
# organisation is, what it has received, and what it has not proved.
# Every figure is a row in 03 — Track Record or 09 — Impact & Support.
# ---------------------------------------------------------------------------

import archive as ar

# a dated figure. --n is read by the CSS counter that counts it up on scroll;
# the visible number is also in the markup, so it is there without CSS.
def _fig(n, label, period, suffix=""):
    return (f'<div class="figure"><b class="count" style="--n:{n}"><span>{n}{suffix}</span></b>'
            f'<span class="figure-label">{label}</span>'
            f'<span class="figure-period">{period}</span></div>')


IMPACT = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Our impact</p>
    <h1>What has changed, and only what the record supports.</h1>
    <p>No claim here about measured wellbeing or reduced isolation, because neither has been
       measured. Every figure below carries the period it covers and traces to a dated row in
       <a class="crumb" href="archive.html">the record</a>.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Dated figures</p>
      <h2>A number without a date is marketing. These have dates.</h2>
    </div>
    <div class="figures stagger">
      {_fig(40, "sessions and performances", "2024 – 2026", "+")}
      {_fig(17, "lecture-recitals", "January 2024 – February 2026")}
      {_fig(143, "attendances at those lectures", "sessions 1–15 · 2024 – 2025")}
      {_fig(20, "outreach performances", "2023 – 2025 · four countries")}
      {_fig(7, "of 7 completed the pilot ensemble", "January – April 2026")}
      {_fig(25, "venues and institutions", "2023 – 2026")}
      {_fig(213, "hours recorded, preparation included", "to 27 August 2026")}
      {_fig(4, "Letters Ensemble concerts", "March 2024 – December 2025")}
    </div>
    <p class="tiny mt-3 reveal">Over 40 is 17 lecture-recitals, 20 outreach performances, one
       pilot concert and two South Dublin Live concerts. The four ensemble concerts sit inside
       the twenty and are not counted twice. Audiences at outreach performances were never
       counted, so no audience figure is given.</p>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">What changed</p>
      <h2>Seven things the record supports.</h2>
      <p>Each one is a claim we can show you the paper for. Where the paper is a letter, a
         programme or an attendance sheet, that is said.</p>
    </div>
    <div class="evidence evidence-2 stagger">
      <div><dl><dt>More people came</dt>
        <dd>Attendance at the free lecture-recitals rose from <strong>6</strong> at the first
            session to <strong>14</strong>, with the same people returning &mdash; 15 sessions
            and 143 attendances over two years, each one counted on the day.</dd></dl></div>
      <div><dl><dt>An audience became players</dt>
        <dd>At a 2024 concert for the Missionary Sisters of St Columban, a sister asked whether
            she might play again. That question became the 2026 recorder ensemble for retired
            religious: <strong>all seven completed</strong> the ten weeks and performed nine
            pieces in public.</dd></dl></div>
      <div><dl><dt>Learning fed sharing</dt>
        <dd>A participant who came to a lecture-recital remembered playing the viola at school
            and joined the Letters Ensemble. The two pillars are a circuit, and this is one turn
            of it.</dd></dl></div>
      <div><dl><dt>Hard-to-reach places were reached</dt>
        <dd>Residential and nursing care, retired religious communities, a homeless hostel, an
            HSE day service, a university hospital, rural parishes, a martyrs&rsquo; shrine
            &mdash; and the National Concert Hall, attended together.</dd></dl></div>
      <div><dl><dt>An external body validated it</dt>
        <dd>South Dublin County Council&rsquo;s Arts Office selected the project for
            <strong>South Dublin Live 2026</strong> and funded it. Everything before that had
            been self-funded and voluntary.</dd></dl></div>
      <div><dl><dt>The Church vouched for it</dt>
        <dd>A letter of recommendation from Donal Roche, Auxiliary Bishop of Dublin, and a
            scholarship from the Lay Apostolate Committee of the Catholic Bishops&rsquo;
            Conference of Korea.</dd></dl></div>
      <div><dl><dt>Institutions left the door open</dt>
        <dd>Letters of support from Rua Red, The Civic and Tallaght University Hospital for the
            South Dublin Live application; the hospital&rsquo;s National Centre for Arts &amp;
            Health met us in the Atrium to plan the concert that then took place there.</dd></dl></div>
      <div><dl><dt>Support bought a vehicle</dt>
        <dd>Gifts from individuals in Europe and Korea put a vehicle on the road, so players,
            instruments and stands travel together to rooms no bus timetable reaches.</dd></dl></div>
    </div>
    <div class="reveal mt-4">{dg.attendance(L)}</div>
  </div>
</section>

<section>
  <div class="wrap split split-wide split-center">
    <figure class="reveal">
      <div class="photo photo-4x3">
        <img src="images/letters-ensemble.jpg" width="1400" height="1050"
             alt="The Letters Ensemble with their instruments">
      </div>
      <figcaption>The Letters Ensemble, whose 2024 concert in Co. Wicklow is where the
        teaching programme began.</figcaption>
    </figure>
    <div class="reveal">
      <p class="eyebrow">One story</p>
      <h2 class="h-md">A question from the back of the room.</h2>
      <p class="lead mt-2">In November 2024 the Letters Ensemble played for the Missionary
         Sisters of St Columban in Co. Wicklow. Afterwards one of the sisters asked whether she
         might play again. She had played the violin, years ago.</p>
      <p class="mt-2">That question became a recorder ensemble for seven retired Presentation
         Sisters: three months of preparation, ten weekly rehearsals at Warrenmount, and an
         Easter concert of nine pieces at Clondalkin Lodge. All seven completed. In September
         2026 the same course opened to the public at Mulhuddart Community Centre, free.</p>
      <p class="mt-2">We do not name the sister, because we have not asked her. That is the
         rule for every story on this site.</p>
      <div class="btn-row"><a class="btn btn-quiet" href="programmes/recorder-ensemble.html">The course that came of it <span class="arrow">&rarr;</span></a></div>
    </div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Theory of change</p>
      <h2>What a room, an hour and a recorder are supposed to add up to.</h2>
    </div>
    <div class="reveal">{dg.theory_of_change(L)}</div>
  </div>
</section>

<section id="next">
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">Where this is going</p>
      <h2>Four things done, four to do, in that order.</h2>
      <p>The second social aim &mdash; music educators in secure, properly paid work &mdash; is
         the reason the list ends where it does. A model that runs on one volunteer is a pilot,
         not a programme.</p>
    </div>
    <div class="reveal">{dg.roadmap(L)}</div>
    <div class="grid grid-2 stagger mt-4">
      <div class="card"><span class="kicker">Measuring</span>
        <h3>A simple pre and post measure, from autumn 2026</h3>
        <p>Every cohort from the Mulhuddart course onward is asked the same short questions
           about connection and confidence at the start and the end of term, with written
           consent for anything quoted. The next report on this page will be able to speak to
           wellbeing with the same confidence as it speaks to attendance.</p></div>
      <div class="card"><span class="kicker">Recording</span>
        <h3>The record, kept on the day</h3>
        <p>Every session and performance is logged when it happens &mdash; date, venue, what
           was done, an estimate of who was there, and what evidence exists. The practice is
           also documented as research, and that continues. What has not been counted is said
           so, in the same table.</p></div>
    </div>
  </div>
</section>

<section class="band-raised" id="transparency">
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">Transparency</p>
      <h2>What we are, what we have received, and what we have not proved.</h2>
      <p>A funder forgives a stage. What a funder does not forgive is vagueness. So here is
         the stage, plainly.</p>
    </div>
    <div class="split reveal">
      <div>
        <h3 class="h-sub">Status</h3>
        <dl class="facts">
          <dt>Operating as</dt><dd>A founder-led community music social enterprise, volunteer-led,
              founded in Dublin in January 2024</dd>
          <dt>Legal form</dt><dd>Formalising as a not-for-profit company limited by guarantee
              (CLG). Not yet a registered charity; gifts are not eligible for tax relief</dd>
          <dt>Directors</dt><dd>Not yet appointed. A board of at least three voluntary directors is
              the next step in the list above</dd>
          <dt>Insurance</dt><dd>Public liability insurance in place, from August 2026</dd>
          <dt>Vetting</dt><dd>Garda vetting completed where the work requires it; documentation
              available to partner venues on request</dd>
          <dt>Founder</dt><dd>Andrew Seohyeon Kim, BMus (Hons), TU Dublin Conservatoire &mdash;
              <a class="link" href="founder.html">profile</a></dd>
        </dl>
      </div>
      <div>
        <h3 class="h-sub">What has not been proved</h3>
        <ul class="checklist mt-2">
          <li><strong>Wellbeing has not been measured.</strong> No validated instrument, no pre
              and post measure yet. Anything about easing isolation rests on what participants
              said.</li>
          <li><strong>Audiences have not been counted.</strong> No audience figure exists for any
              of the twenty outreach performances.</li>
          <li><strong>Nothing has been followed up.</strong> What remained after the ten weeks
              ended is unknown.</li>
          <li><strong>There is no comparison.</strong> No other instrument, cohort or tutor has
              been tried against it.</li>
          <li><strong>The practitioner is the researcher.</strong> A strength for design; a limit
              on claims about outcomes.</li>
        </ul>
      </div>
    </div>

    <div class="section-head reveal mt-4">
      <h3 class="h-sub">Funding and support to date</h3>
      <p>Everything before 2026 was self-funded and voluntary. The record is published because a
         funder&rsquo;s first question is who came before them, however small.</p>
    </div>
    <div class="table-scroll reveal">
      <table>
        <thead><tr><th scope="col">Source</th><th scope="col">Detail</th><th scope="col">Status</th></tr></thead>
        <tbody>
          <tr><td><strong>South Dublin County Council</strong><br><span class="tiny">Arts Office ·
              South Dublin Live 2026</span></td>
              <td>&euro;2,000 for <em>Shared Voices of South Dublin</em> &mdash; two concerts delivered,
                  at Tallaght University Hospital and Rua Red. Our first publicly funded work.</td>
              <td>Received</td></tr>
          <tr><td><strong>Myongdohoe Scholarship</strong><br><span class="tiny">Lay Apostolate
              Committee, Catholic Bishops&rsquo; Conference of Korea</span></td>
              <td>Termly support from March 2025 for the founder&rsquo;s musical apostolate.</td>
              <td>Concluded</td></tr>
          <tr><td><strong>Individual donors</strong></td>
              <td>Gifts from supporters in Europe and Korea that put a vehicle on the road.</td>
              <td>Ongoing</td></tr>
          <tr><td><strong>Partner venues, in kind</strong></td>
              <td>Tallaght University Hospital &mdash; venue and operating time. Mulhuddart Community
                  Centre &mdash; the room. TU Dublin &mdash; rehearsal space.</td><td>Continuing</td></tr>
          <tr><td><strong>TU Dublin Venture Lab</strong></td>
              <td>Social enterprise start-up programme, from September 2024.</td><td>Completed</td></tr>
        </tbody>
      </table>
    </div>
    <div class="split split-center reveal mt-4">
      <div class="quote">
        <p>&ldquo;Andrew does not undertake this work from a position of material abundance. Even
           within limited personal financial circumstances, he continues to give generously of his
           time, energy, and talent.&rdquo;</p>
        <cite>Donal Roche, Auxiliary Bishop of Dublin · 16 February 2026</cite>
      </div>
      <div>
        <h3 class="h-sub">Letters written for the South Dublin Live application</h3>
        <ul class="plainlist mt-2">
          <li><strong>Rua Red</strong> &mdash; South Dublin&rsquo;s contemporary arts centre</li>
          <li><strong>The Civic Theatre</strong>, Tallaght</li>
          <li><strong>Tallaght University Hospital</strong> &mdash; National Centre for Arts &amp; Health</li>
          <li><strong>SDCC Arts Office</strong> &mdash; selection for South Dublin Live 2026</li>
        </ul>
        <p class="tiny mt-2">These letters were written in support of that one application. They
           are not a general endorsement of everything we run, and we do not present them as
           one.</p>
      </div>
    </div>
  </div>
</section>

{CTA}"""


# ---------------------------------------------------------------------------
# Archive — the record, 2023 to date
# ---------------------------------------------------------------------------

ARCHIVE = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">The record</p>
    <h1>Every session and performance, 2023 to date.</h1>
    <p>A ledger, not a highlight reel. Every figure on this site traces to a line here.
       Unconfirmed rows are left out.</p>
  </div>
</section>

<section class="tight">
  <div class="wrap reveal">
    {dg.chronicle(L)}
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Milestones</p>
      <h2>From one clarinet to a community.</h2>
    </div>
    <div class="split split-wide">
      <div class="timeline reveal">
        <div class="tl-item"><div class="tl-date">February 2023</div>
          <h3>Before the beginning</h3>
          <p>A clarinet solo at Mass in Lourdes, a year before the work had a name.</p></div>
        <div class="tl-item"><div class="tl-date">January 2024</div>
          <h3>It starts</h3>
          <p>Founded in Dublin, with the Letters Ensemble. First lecture-recital: six people.</p></div>
        <div class="tl-item"><div class="tl-date">2024</div>
          <h3>Music goes out</h3>
          <p>Dalgan Park, Co. Wicklow, London, Paris, Daegu. The lectures move to TU Dublin.</p></div>
        <div class="tl-item"><div class="tl-date">2024–2025</div>
          <h3>Going together</h3>
          <p>Accompanied concert-going becomes a strand: the NCH, the NSO, the BBC Proms.</p></div>
        <div class="tl-item"><div class="tl-date">October 2025</div>
          <h3>An audience becomes players</h3>
          <p>Preparation begins for a recorder ensemble with seven retired sisters.</p></div>
        <div class="tl-item"><div class="tl-date">December 2025</div>
          <h3>To the National Concert Hall</h3>
          <p>The fifteenth session is a concert at the National Concert Hall, attended together.</p></div>
        <div class="tl-item"><div class="tl-date">Jan–Apr 2026</div>
          <h3>The pilot, and its concert</h3>
          <p>Ten weeks at Warrenmount, an Easter concert at Clondalkin Lodge. All seven completed.</p></div>
        <div class="tl-item"><div class="tl-date">August 2026</div>
          <h3>First public commission</h3>
          <p>South Dublin Live 2026: Tallaght University Hospital and Rua Red.</p></div>
        <div class="tl-item"><div class="tl-date">September 2026</div>
          <h3>The model opens to the public</h3>
          <p>The first community course opens at Mulhuddart: twelve weeks, free.</p></div>
      </div>
      <div>
        <figure class="reveal">
          <div class="photo photo-4x3">
            <img src="images/church-concert.jpg" width="1400" height="1050"
                 alt="An ensemble performing in a church">
          </div>
          <figcaption>An ensemble in a church. Roughly sixteen of the twenty outreach performances
            were in parishes, shrines, convents or liturgies.</figcaption>
        </figure>
        <div class="callout reveal mt-3">
          <h3 class="h-sub">How to read the tables</h3>
          <p class="small mt-1">Newest year first. Attendance is recorded for lecture-recitals
             only. <span class="tag">Sacred Places</span> marks the faith-based strand. Letters
             Ensemble rehearsals were never logged and are not listed.</p>
        </div>
      </div>
    </div>
  </div>
</section>

{ar.tables(L)}

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">Planned, and not delivered</p>
      <h2>2026: we halved the plan and delivered what remained in full.</h2>
      <p>This belongs in the record too. In a year that held graduation, a dissertation and a
         move, four planned events became two, and the two were done properly.</p>
    </div>
    <div class="grid grid-2 stagger">
      <div class="card"><span class="kicker">Not held · March 2026</span>
        <h3>A Lenten concert at Our Lady of Dolours</h3>
        <p>A free parish concert with a voluntary offering, clarinet and piano, then clarinet with
           the Letters Ensemble. The proposal, poster and scores exist; it did not go ahead.</p></div>
      <div class="card"><span class="kicker">In discussion</span>
        <h3>A fifth Letters Ensemble concert</h3>
        <p>St John of God Hospital, Stillorgan, with a draft programme. Named in the 2026 plan
           as the first partnership in discussion; no date yet.</p></div>
      <div class="card"><span class="kicker">Not held · August 2026</span>
        <h3>South Dublin Live — a cross-cultural concert at The Civic</h3>
        <p>Clarinet, piano and haegeum in the main auditorium. Of the four concerts proposed to
           the Arts Office, this and the family concert below did not proceed; the two that did
           are in the 2026 table above.</p></div>
      <div class="card"><span class="kicker">Not held · September 2026</span>
        <h3>South Dublin Live — a family concert outdoors</h3>
        <p>A 45-minute trio concert in a public square, with the county library as a wet-weather
           backup. The format is the cheapest and most public of the four, and the one most
           likely to return.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">Still undocumented</p>
      <h2 class="h-md">What happened, and was not written down.</h2>
      <ul class="checklist mt-3">
        <li>Letters Ensemble rehearsals &mdash; weekly since January 2024, well over a hundred,
            not one recorded. We are counting them from now on.</li>
        <li>Actual attendance on Concert Guide outings &mdash; the invitations survive, the
            participation does not.</li>
        <li>Programmes and repertoire for most of the twenty outreach concerts.</li>
        <li>Audience numbers for every performance.</li>
        <li>Participant testimony &mdash; to be collected with consent from the autumn 2026
            cohort on.</li>
      </ul>
    </div>
    <div class="reveal">
      <p class="eyebrow">How the record is kept</p>
      <h2 class="h-md">On the day, in one row.</h2>
      <ol class="steps mt-3">
        <li><strong>Date, formal venue name, institution type</strong> &mdash; what was done, and
            for whom.</li>
        <li><strong>An estimate of who was there</strong>, written down that evening, even when
            nobody counted.</li>
        <li><strong>Hours, preparation included</strong> &mdash; the part every earlier record
            left out.</li>
        <li><strong>Evidence held</strong>, in the order assessors trust it: a letter on headed
            paper, press coverage, a programme or poster, photographs.</li>
      </ol>
      <div class="btn-row"><a class="btn btn-quiet" href="impact.html">What the record adds up to <span class="arrow">&rarr;</span></a></div>
    </div>
  </div>
</section>

{CTA}"""


# ---------------------------------------------------------------------------
# Partner with us — for organisations
#
# Order after Acumen's page, which 12 — Brand & Web Master §11 found the most
# complete of 28 studied: what you get first, then the ways, then the
# evidence, then the questions, then a short ask. Never the need first.
# ---------------------------------------------------------------------------

_MAIL_PARTNER = ("mailto:sby05034@gmail.com?subject=Partnership%20enquiry"
                 "&body=Organisation%3A%20%0AWhere%3A%20%0AThe%20room%20and%20a%20possible%20date%3A%20%0A"
                 "One%20line%20on%20what%20you%20have%20in%20mind%3A%20")

_FAQ_EN = "\n".join(
    f'      <details class="faq reveal"><summary>{q}</summary><p>{a}</p></details>'
    for q, a in [
        ("Can we fund one programme rather than the organisation?",
         "Yes. Name the programme, or the kind of setting, and the support is ring-fenced for it "
         "and reported against it."),
        ("Is a gift tax-deductible?",
         "Not yet. We are formalising as a not-for-profit company limited by guarantee and are not "
         "a registered charity, so gifts are not eligible for charitable tax relief. We say so "
         "plainly rather than let anyone assume otherwise."),
        ("Where would our name appear?",
         "On the printed programme of what you funded, on the Support page of this site, and in "
         "the dated report you receive &mdash; with your agreement, and nowhere else."),
        ("What does a venue need to provide for a concert?",
         "A room, the people who live or work there, and one named contact. Players, instruments, "
         "stands, the programme and insurance arrive with us. There is no stage, no piano and "
         "nothing for the audience to pay."),
    ])

PARTNER = f"""<section class="page-hero page-hero-lead">
  <div class="wrap">
    <p class="eyebrow lift lift-1">Partner with us</p>
    <h1 class="lift lift-2">Tell us your room and your date.</h1>
    <p class="lift lift-3">For care homes, hospitals, parishes and community centres; for councils,
       trusts, foundations and companies. Enquiring takes less than two minutes, and everything
       except the room arrives with us.</p>
    <div class="btn-row lift lift-4">
      <a class="btn btn-accent" href="{_MAIL_PARTNER}">Enquire in two minutes <span class="arrow">&rarr;</span></a>
      <a class="btn btn-on-dark" href="#faq">The questions we are asked</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">What you get</p>
      <h2>Live music in rooms where it changes the day, and something your people can see.</h2>
      <p>Your support puts musicians into a ward, a day room or a parish hall, and gives your
         team something they can visit and take part in. Every partnership comes with a named
         contact, a dated report of what the money did, and an open invitation to attend.</p>
    </div>
    <div class="reveal">{dg.partnership(L)}</div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head wide reveal">
      <p class="eyebrow">If you run a room</p>
      <h2>Everything above the stave arrives in a car.</h2>
      <p>A day room with no piano, no stage and no budget can host a concert. Thirty to sixty
         minutes, acoustic, introduced from the floor in plain language, with nothing for the
         audience to pay. We carry public liability insurance and complete Garda vetting where
         the work requires it; the paperwork is available before we arrive.</p>
    </div>
    <div class="reveal">{dg.visit(L)}</div>
    <div class="grid grid-3 stagger mt-4">
      <div class="card"><span class="kicker">Care homes and hospitals</span>
        <h3>A concert in the day room, or a drop-in in the atrium</h3>
        <p>Residents, patients, families and staff, in the room they are already in. The
           Tallaght University Hospital concert in August 2026 was thirty minutes, acoustic and
           drop-in; a care-home concert is usually the same shape.</p></div>
      <div class="card"><span class="kicker">Parishes and religious communities</span>
        <h3>Liturgical music, or a concert after Mass</h3>
        <p>Roughly sixteen of our twenty outreach performances were in parishes, shrines,
           convents and liturgies. The founder is Music Director at one Dublin parish and
           organist at another; we know what a sacristy needs to hear first.</p></div>
      <div class="card"><span class="kicker">Community centres</span>
        <h3>A term-long course, in your room</h3>
        <p>A warm room seating ten to twelve in a circle, once a week for a term, and one named
           contact. We bring the tutor, the curriculum, the scores and the end-of-term concert.
           <a class="link" href="get-involved.html">What you provide, and what we do</a>.</p></div>
    </div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Evidence</p>
      <h2>Who has already worked with us.</h2>
      <p>Named, because borrowed trust should be checkable. Each of these is a row in
         <a class="link" href="archive.html">the record</a>.</p>
    </div>
    <ul class="names reveal">
      <li>South Dublin County Council Arts Office</li>
      <li>Tallaght University Hospital</li>
      <li>Rua Red</li>
      <li>The Civic Theatre</li>
      <li>Clondalkin Lodge</li>
      <li>Mulhuddart Community Centre</li>
      <li>Presentation Sisters</li>
      <li>Missionary Sisters of St Columban</li>
      <li>Dalgan Park</li>
      <li>TU Dublin</li>
      <li>Our Lady of Dolours, Dolphin&rsquo;s Barn</li>
      <li>Church of the Three Patrons, Rathgar</li>
      <li>HSE EVE Goirtin Hub</li>
      <li>Morning Star Hostel</li>
      <li>Missions &Eacute;trang&egrave;res de Paris</li>
    </ul>
    <div class="figures figures-4 stagger mt-4">
      {_fig(20, "outreach performances", "2023 – 2025 · four countries")}
      {_fig(25, "venues and institutions", "2023 – 2026")}
      {_fig(7, "of 7 completed the pilot", "January – April 2026")}
      {_fig(2, "concerts for South Dublin Live", "August 2026 · first public commission")}
    </div>
    <div class="quote reveal mt-4">
      <p>&ldquo;Through music, he offers encouragement, dignity, and spiritual accompaniment to
         those who may otherwise feel isolated.&rdquo;</p>
      <cite>Donal Roche, Auxiliary Bishop of Dublin · 16 February 2026</cite>
    </div>
  </div>
</section>

<section id="faq">
  <div class="wrap narrow">
    <div class="section-head reveal">
      <p class="eyebrow">The questions we are asked</p>
      <h2 class="h-md">Four, honestly answered.</h2>
    </div>
    <div class="faq-list">
{_FAQ_EN}
    </div>
  </div>
</section>

<section class="band-photo">
  <img src="images/tuh-atrium.jpg" alt="" width="1400" height="1052">
  <div class="wrap narrow center reveal">
    <p class="eyebrow center-row">Next step</p>
    <h2 class="h-lg">One email, four lines.</h2>
    <p class="lead mt-2">Your organisation, where you are, the room and a possible date, and a
       line on what you have in mind. The email opens with those four lines already in it.
       You will hear back from the person who will be in the room.</p>
    <div class="btn-row center-row">
      <a class="btn btn-accent" href="{_MAIL_PARTNER}">Become a partner <span class="arrow">&rarr;</span></a>
      <a class="btn btn-on-dark" href="contact.html">All contact details</a>
    </div>
  </div>
</section>"""


# ---------------------------------------------------------------------------
# Identity — the mark, and what it commits us to
# ---------------------------------------------------------------------------

IDENTITY = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">The mark</p>
    <h1>The gold falls on <em>Everyone</em>.</h1>
    <p>That is not a flourish. In the mark, &ldquo;for&rdquo; is set small and
       &ldquo;Everyone&rdquo; large and gold, because the difficult word in the name is the
       last one. This page is the design standard, published so that anyone printing our name
       can hold us to it.</p>
  </div>
</section>

<section class="band-mark">
  <div class="wrap split split-wide split-center">
    <div class="reveal">
      <p class="eyebrow">The name, and what it commits us to</p>
      <h2 class="h-md">The name is the brief.</h2>
      <p class="lead mt-3">Classical music is not short of audiences. What it lacks is a reliable
         way in for people who are older, unwell, far from a city, short of money, or simply
         never told that any of it was theirs. The mark says which word we are judged on.</p>
      <p class="mt-3">A treble clef with the wordmark, adopted on 17 August 2026. The proportion
         inside the wordmark carries the meaning and never changes. The name is a proper noun
         with one shape &mdash; <span class="brandname">Classical Music for Everyone</span>
         &mdash; and is never set in capitals, never abbreviated in public copy, and never reset
         in another typeface.</p>
      <p class="footer-line mark-line">Bringing classical music where it&rsquo;s needed!</p>
    </div>
    <figure class="reveal mark-plate">
      <img src="assets/logo-horizontal.svg" width="341" height="131"
           alt="The Classical Music for Everyone mark: a treble clef beside the wordmark, with &lsquo;Everyone&rsquo; set large and in gold">
      <figcaption>The horizontal mark, adopted 17 August 2026.</figcaption>
    </figure>
  </div>
</section>

<section id="identity">
  <div class="wrap">
    <div class="split split-center reveal">
      <div class="logo-pair">
        <figure class="logo-plate on-light">
          <img src="assets/logo-horizontal.svg" width="341" height="131"
               alt="The horizontal logo: a treble clef beside the wordmark">
          <figcaption>On light &mdash; the default</figcaption>
        </figure>
        <figure class="logo-plate on-dark">
          <img src="assets/logo-reversed.svg" width="341" height="131"
               alt="The reversed logo, for dark backgrounds">
          <figcaption>On navy &mdash; reversed</figcaption>
        </figure>
        <figure class="logo-plate on-light">
          <img src="assets/logo-signature.png" width="600" height="210"
               alt="The signature lock-up, used at the foot of an email">
          <figcaption>Email signature &mdash; the same lock-up at mail size. A white-background
            version is kept alongside it for clients that strip transparency.</figcaption>
        </figure>
      </div>
      <div>
        <h3 class="h-sub">Using the mark</h3>
        <p class="mt-2">Light ground, horizontal; dark ground, reversed. The clef alone is for
           favicons and profile pictures only. On a photograph, place it where the area behind it
           is quiet, or give it a plain panel.</p>
        <div class="rules mt-3">
          <div class="do">
            <h3 class="h-sub">Always</h3>
            <ul>
              <li>Clef and wordmark together</li>
              <li>Clear space of half the clef&rsquo;s width, on all four sides</li>
              <li>Light ground &rarr; horizontal; dark ground &rarr; reversed</li>
              <li>At least 140px wide on screen, 28mm in print</li>
            </ul>
          </div>
          <div class="dont">
            <h3 class="h-sub">Never</h3>
            <ul>
              <li>Stretch, squash, skew or recolour it</li>
              <li>Add a shadow, outline or glow</li>
              <li>Make &ldquo;for&rdquo; and &ldquo;Everyone&rdquo; the same size</li>
              <li>Use the clef alone above favicon size</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Colour</p>
      <h2 class="h-md">Eight values, defined once.</h2>
      <p>Every colour on this site resolves to one of them or to a tint derived from one. A
         component never invents a colour of its own.</p>
    </div>
    <div class="swatches reveal">
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--ink-navy)"></i><b>Ink Navy</b><code>#1D2430</code>
        <span>Logo base, body text, dark bands</span></div>
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--gold-bronze)"></i><b>Gold Bronze</b><code>#B8893A</code>
        <span>Logo gold, rules, arrows, diagram strokes</span></div>
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--gold-light)"></i><b>Light Gold</b><code>#D9B36A</code>
        <span>The gold of the reversed logo, and on dark grounds</span></div>
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--warm-cream)"></i><b>Warm Cream</b><code>#FAF5EE</code>
        <span>The background of nearly every page</span></div>
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--soft-navy)"></i><b>Soft Navy</b><code>#33405C</code>
        <span>Panels and blocks in print material</span></div>
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--antique-gold)"></i><b>Antique Gold</b><code>#B4914F</code>
        <span>Accents in print material</span></div>
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--dusty-rose)"></i><b>Dusty Rose</b><code>#8C4A56</code>
        <span>Highlight &mdash; used sparingly, never for body text</span></div>
      <div class="swatch"><i aria-hidden="true" style="--sw:var(--slate)"></i><b>Slate</b><code>#5F6B7D</code>
        <span>Secondary text</span></div>
    </div>
    <div class="callout reveal mt-3">
      <p class="small"><strong>One rule that costs us the prettier option.</strong> Gold Bronze
         is a 2.9:1 contrast against cream, which fails at body size. So gold as <em>text</em> is
         always the darkened <code>#7F5C1C</code>, and the gold buttons carry ink navy lettering
         rather than white. Every text and background pair on this site meets WCAG AA. The logo
         is the one thing exempt, because a logo is an image and is never recoloured.</p>
    </div>

    <div class="section-head reveal mt-4">
      <p class="eyebrow">Type</p>
      <h2 class="h-md">Three faces and no fourth.</h2>
      <p>EB Garamond is an old-style serif in the same lineage as the Cormorant Garamond of the
         wordmark, so the headings rhyme with the logo rather than argue with it. Korean gets
         more leading and less negative tracking, because Noto Sans KR needs both.</p>
    </div>
    <div class="specimen reveal">
      <div>
        <dfn>EB Garamond &mdash; headings</dfn>
        <div class="sp-display">Bringing classical music where it&rsquo;s needed!</div>
        <p>SemiBold. Titles, headlines and display sizes.</p>
      </div>
      <div>
        <dfn>Plus Jakarta Sans &mdash; body and labels</dfn>
        <div class="sp-body">We teach people to play, not only to listen.</div>
        <p>Regular, SemiBold, Bold. Body text, tables, captions, every label.</p>
      </div>
      <div>
        <dfn>Noto Sans KR &mdash; Korean</dfn>
        <div class="sp-kr">클래식 음악을, 그것이 필요한 곳으로!</div>
        <p>Regular, Medium, Bold. Headings and body alike on the Korean pages.</p>
      </div>
      <div>
        <dfn>Cormorant Garamond &mdash; logo only</dfn>
        <div class="sp-body">Used for the wordmark and nowhere else.</div>
        <p>The lettering in the logo is outlined, so the face is never loaded on this site.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Diagrams</p>
      <h2 class="h-md">Fourteen figures, four marks.</h2>
      <p>Where an explanation runs past about eighty words, it stops being a paragraph and
         becomes a figure. Every figure on this site is drawn from the same four marks, borrowed
         from notation, so fourteen diagrams read as one set rather than fourteen flowcharts.</p>
    </div>
    <div class="reveal">{dg.vocabulary(L)}</div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">Words</p>
      <h2 class="h-md">How the name is written.</h2>
      <ul class="checklist mt-3">
        <li><strong>In full, always</strong> &mdash; <span class="brandname">Classical Music for
            Everyone</span>. Never in capitals, never shortened in public copy.</li>
        <li><strong>Participants</strong>, not clients, students or the elderly. Older people,
            not seniors.</li>
        <li><strong>Social enterprise</strong>, not charity and not business.</li>
        <li><strong>Irish English</strong> &mdash; programme, organisation, centre.</li>
        <li><strong>No superlatives</strong>, no unverifiable claims, and no number without a
            date.</li>
      </ul>
    </div>
    <div class="reveal">
      <p class="eyebrow">The line</p>
      <h2 class="h-md">One sentence for the whole organisation.</h2>
      <p class="footer-line mark-line">Bringing classical music where it&rsquo;s needed!</p>
      <p class="mt-3">The master line ends in an exclamation mark, and sits at the foot of every
         page. The Korean working equivalent is <span lang="ko">클래식 음악을, 그것이 필요한
         곳으로!</span></p>
      <div class="btn-row"><a class="btn btn-quiet" href="about.html">Mission, values and the founder <span class="arrow">&rarr;</span></a></div>
    </div>
  </div>
</section>

{CTA}"""
