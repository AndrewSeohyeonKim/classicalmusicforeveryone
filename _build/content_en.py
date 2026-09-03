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

STATS = """<div class="stats">
  <div class="wrap stats-grid">
    <div class="stat"><b>40+</b><span>Sessions &amp; performances</span></div>
    <div class="stat"><b>4</b><span>Countries</span></div>
    <div class="stat"><b>20+</b><span>Venues &amp; institutions</span></div>
    <div class="stat"><b>143</b><span>Lecture attendances</span></div>
    <div class="stat"><b>7 / 7</b><span>Pilot participants completed</span></div>
  </div>
</div>"""

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
  <div class="wrap narrow reveal" style="text-align:center;margin-inline:auto">
    <h2 style="font-size:clamp(28px,3.6vw,42px)">There is a place for you here.</h2>
    <p class="lead" style="margin-top:18px;color:var(--fg-inverse-muted)">
      Learn an instrument for the first time, come and listen, play alongside us,
      or open your venue. Start with one line.</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn btn-accent" href="get-involved.html">Get involved <span class="arrow">→</span></a>
      <a class="btn btn-on-dark" href="support.html">Support our work</a>
    </div>
  </div>
</section>"""


# ---------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------

INDEX = f"""<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow lift lift-1">Community music · Dublin, Ireland</p>
      <h1><span class="line lift lift-1">Classical music,</span><span class="line lift lift-2"><em>for everyone.</em></span></h1>
      <p class="lead lift lift-3">We teach people to play — not only to listen — and we bring
         live classical music to the places it rarely reaches.</p>
      <div class="btn-row lift lift-4">
        <a class="btn btn-primary" href="get-involved.html">Join a class <span class="arrow">→</span></a>
        <a class="btn btn-quiet" href="programmes.html">What we do</a>
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

{STATS}

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">What&rsquo;s on</p>
      <h2>Happening now.</h2>
    </div>
{WHATS_ON}
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">How it works</p>
      <h2>Playing and listening feed each other.</h2>
      <p>We go to a room and play. Someone asks whether they could do that. That question
         becomes a class — and the class produces people who can play in the next room.</p>
    </div>
    <div class="reveal">{dg.loop(L)}</div>
  </div>
</section>

<section class="band-photo">
  <img src="images/church-concert.jpg" alt="" width="1400" height="1050">
  <div class="wrap narrow reveal">
    <p class="eyebrow">Why we exist</p>
    <h2 style="font-size:clamp(28px,3.8vw,44px)">It is playing, not only listening,
       that restores dignity.</h2>
    <p class="lead" style="margin-top:20px;color:var(--fg-inverse-body)">
      Classical music is culturally rich and still out of reach for many people — because of
      age, mobility, income, geography, or simple unfamiliarity. A care home, a hospital, a
      hostel, a rural parish is not a place without an audience. It is where the audience that
      has waited longest already is.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">What we run</p>
      <h2>Five programmes, one belief.</h2>
    </div>
    <div class="grid grid-3 stagger">
      <a class="card card-media" href="programmes.html">
        <div class="photo photo-3x2"><img src="images/community-room.jpg" width="1400" height="1050"
             alt="Playing the clarinet in a community room"></div>
        <div class="card-body">
          <span class="kicker">Flagship</span>
          <h3>Recorder Ensemble</h3>
          <p>A term for complete beginners: first notes in week one, a concert in the last.</p>
          <div class="meta">Weekly · community centres &amp; parishes</div>
        </div>
      </a>
      <a class="card card-media" href="programmes.html">
        <div class="photo photo-3x2"><img src="images/care-christmas.jpg" width="1400" height="1050"
             alt="A quartet performing in a care setting at Christmas"></div>
        <div class="card-body">
          <span class="kicker">Outreach</span>
          <h3>Music that comes to you</h3>
          <p>Live performance in care homes, parishes, hospitals, hostels and community spaces.</p>
          <div class="meta">20 performances · 4 countries · 15+ venues</div>
        </div>
      </a>
      <a class="card card-media" href="programmes.html">
        <div class="photo photo-3x2"><img src="images/lecture-recital.jpg" width="1400" height="1050"
             alt="A lecture-recital in progress"></div>
        <div class="card-body">
          <span class="kicker">Learning</span>
          <h3>Getting to Know Classical Music</h3>
          <p>Free lecture-recitals, roughly monthly, for people with no prior knowledge.</p>
          <div class="meta">17 sessions · 143 attendances</div>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap split split-center reveal">
    <div class="quote">
      <p>&ldquo;Through music, he offers encouragement, dignity, and spiritual accompaniment to
         those who may otherwise feel isolated.&rdquo;</p>
      <cite>Donal Roche, Auxiliary Bishop of Dublin · 16 February 2026</cite>
    </div>
    <div>
      <p class="eyebrow">Backed by the record</p>
      <h3 style="font-size:26px">Someone other than us paid for it.</h3>
      <p style="margin-top:14px">In 2026 South Dublin County Council&rsquo;s Arts Office selected
         the project for <strong>South Dublin Live 2026</strong> — our first publicly funded
         commission. Letters of support are held from Rua Red, The Civic and Tallaght University
         Hospital.</p>
      <div class="btn-row"><a class="btn btn-quiet" href="support.html">Funding to date <span class="arrow">→</span></a></div>
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
    <h1>Music should be a shared, everyday experience.</h1>
    <p>A community music social enterprise founded in Dublin in January 2024. Not a performance
       company — a participatory community, where playing is the point.</p>
  </div>
</section>

<section>
  <div class="wrap split split-wide">
    <div class="reveal">
      <p class="eyebrow">Mission</p>
      <p class="lead">To make live classical music genuinely available to everyone — regardless
         of age, background, mobility, income or prior musical knowledge — by teaching people to
         play, playing alongside them, and bringing music to the places it does not normally
         reach.</p>
      <p class="eyebrow" style="margin-top:38px">Vision</p>
      <p class="lead">An Ireland in which every community — urban, rural, in care, and living
         with disability — has a welcoming pathway into making music together, delivered by
         educators in secure, properly paid employment.</p>
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
      <p class="eyebrow">Theory of change</p>
      <h2>What a room, an hour and a recorder are supposed to add up to.</h2>
    </div>
    <div class="reveal">{dg.theory_of_change(L)}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Values</p>
      <h2>Five, described by what they cost us.</h2>
    </div>
    <div class="grid grid-3 stagger">
      <div class="card"><span class="kicker">01</span><h3>Dignity</h3>
        <p>Everyone is treated as someone who can still create — regardless of age, health or
           circumstance.</p></div>
      <div class="card"><span class="kicker">02</span><h3>Accessibility</h3>
        <p>We lower the barriers of price, distance and unfamiliarity — physical, environmental
           and psychological alike.</p></div>
      <div class="card"><span class="kicker">03</span><h3>Accompaniment</h3>
        <p>We stay alongside people for a whole term, not for a one-off visit. Meaning grows
           through continuity.</p></div>
      <div class="card"><span class="kicker">04</span><h3>Community</h3>
        <p>Music that connects people across age, background and language.</p></div>
      <div class="card"><span class="kicker">05</span><h3>Hope</h3>
        <p>We promise no dramatic transformation — only small, real moments of connection.</p></div>
      <div class="card" style="--card-bg:var(--surface-sunken)"><span class="kicker">And</span>
        <h3>Work for educators</h3>
        <p>Music educators mostly work in precarious freelance conditions. Employing them
           properly is our second social aim.</p></div>
    </div>
  </div>
</section>

<section class="band-photo">
  <img src="images/organ.jpg" alt="" width="1400" height="1050">
  <div class="wrap split split-center">
    <div class="reveal">
      <p class="eyebrow">The founder</p>
      <h2 style="font-size:clamp(28px,3.4vw,40px)">Andrew Seohyeon Kim</h2>
      <p class="lead" style="margin-top:18px;color:var(--fg-inverse-body)">
        Clarinettist, organist and community music practitioner. BMus (Hons) in Performance,
        TU Dublin Conservatoire, where his final-year research was the ten-week recorder ensemble
        he designed and led for seven retired Presentation Sisters.</p>
      <p style="margin-top:14px;color:var(--fg-inverse-muted)">
        Music Director at Our Lady of Dolours Church, Dolphin&rsquo;s Barn since 2022; organist at
        the Church of the Three Patrons, Rathgar since 2023. He founded Classical Music for
        Everyone and the Letters Ensemble in 2024.</p>
    </div>
    <div>
      <ul class="plainlist reveal" style="color:var(--fg-inverse-muted)">
        <li><strong style="color:var(--fg-inverse)">Clarinet</strong> — Dr Paul Roe, TU Dublin Conservatoire</li>
        <li><strong style="color:var(--fg-inverse)">Organ</strong> — Simon Harden</li>
        <li><strong style="color:var(--fg-inverse)">Conducting</strong> — IAYO · London Conducting Workshop</li>
        <li><strong style="color:var(--fg-inverse)">Social enterprise</strong> — TU Dublin Venture Lab</li>
        <li><strong style="color:var(--fg-inverse)">Scholarship</strong> — Myongdohoe, Lay Apostolate Committee,
            Catholic Bishops&rsquo; Conference of Korea</li>
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Where we have played</p>
      <h2>Rooms music does not usually enter.</h2>
      <p>Residential and nursing care · religious communities · parishes · a university ·
         a national concert hall · an HSE day service · a homeless hostel · community centres.</p>
    </div>
    <div class="split reveal">
      <div>
        <h4>Ireland</h4>
        <ul class="plainlist" style="margin-top:14px">
          <li>National Concert Hall &amp; TU Dublin, Grangegorman</li>
          <li>Tallaght University Hospital · Rua Red, Tallaght</li>
          <li>Our Lady of Dolours, Dolphin&rsquo;s Barn · Three Patrons, Rathgar</li>
          <li>Carmelite Community Centre · Blessed Sacrament Chapel</li>
          <li>Clondalkin Lodge · Warrenmount, Dublin 8</li>
          <li>Missionary Sisters of St Columban, Co. Wicklow</li>
          <li>Franciscan Missionaries of Mary, Dublin 5</li>
          <li>Dalgan Park &amp; Kilmessan Church, Co. Meath · Dysart, Co. Westmeath</li>
          <li>HSE EVE Goirtin Hub · Morning Star Hostel, Dublin 7</li>
          <li>Methodist Centenary Church, Ranelagh · Mulhuddart Community Centre, D15</li>
        </ul>
      </div>
      <div>
        <h4>Abroad</h4>
        <ul class="plainlist" style="margin-top:14px">
          <li>Sanctuary of Our Lady of Lourdes, France</li>
          <li>Missions Étrangères de Paris · Palais Brongniart, Paris</li>
          <li>London Korean Catholic Church, United Kingdom</li>
          <li>Gwandukjeong Martyrs Memorial Centre, Daegu, Korea</li>
        </ul>
        <div class="callout" style="margin-top:26px">
          <h4>What we do not claim</h4>
          <p class="small" style="margin-top:10px">Our evidence is participation, retention and
             testimony — not measured outcome. Wellbeing has not been measured with a validated
             instrument, and outreach audiences were never counted. From the autumn 2026 cohort we
             are introducing a simple pre/post measure and a consent framework.</p>
        </div>
      </div>
    </div>
  </div>
</section>

{CTA}"""


# ---------------------------------------------------------------------------
# Programmes
# ---------------------------------------------------------------------------

PROGRAMMES = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Programmes</p>
    <h1>What we actually run.</h1>
    <p>Five strands under two pillars, plus one faith-based sub-strand. The Recorder Ensemble
       course is the flagship; everything else feeds it or grows out of it.</p>
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
          <tr><td><strong>Recorder Ensemble course</strong></td><td>Learning</td>
              <td>Flagship · running</td><td>Pilot complete; first community class from Sept 2026</td></tr>
          <tr><td><strong>Getting to Know Classical Music</strong></td><td>Learning</td>
              <td>Running · free</td><td>17 lecture-recitals · 143 attendances</td></tr>
          <tr><td><strong>Concert Guide &amp; Companion</strong></td><td>Learning</td>
              <td>Running</td><td>10 recorded outings, incl. two summers at the BBC Proms</td></tr>
          <tr><td><strong>Outreach Concerts</strong></td><td>Sharing</td>
              <td>Running</td><td>20 performances · 4 countries · 15+ venues</td></tr>
          <tr><td style="padding-inline-start:34px">↳ Bringing Music to Sacred Places</td><td>Sharing</td>
              <td>Sub-strand</td><td>Around 16 of the 20 outreach performances</td></tr>
          <tr><td><strong>Letters Ensemble</strong></td><td>Sharing</td>
              <td>Running</td><td>4 formal concerts · weekly rehearsals since Jan 2024</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Flagship</p>
      <h2>A term, from nothing to a concert.</h2>
      <p>The recorder is gentle on the hands and breath, quick to a first satisfying sound,
         inexpensive, and made for playing together. That is why it works for absolute
         beginners.</p>
    </div>
    <div class="reveal">{dg.term(L)}</div>

    <div class="split" style="margin-top:52px">
      <div class="reveal">
        <h3>What it looks like</h3>
        <div class="table-scroll" style="margin-top:16px">
          <table><tbody>
            <tr><td><strong>Length</strong></td><td>One term, weekly</td></tr>
            <tr><td><strong>Session</strong></td><td>60–90 minutes</td></tr>
            <tr><td><strong>Group</strong></td><td>Small and friendly</td></tr>
            <tr><td><strong>Instrument</strong></td><td>Descant recorder — we advise on buying one,
                supply at cost, or lend you one</td></tr>
            <tr><td><strong>Materials</strong></td><td>Scores and handouts, printed by us. No cost
                to participants.</td></tr>
            <tr><td><strong>Ending</strong></td><td>A short concert for family and friends</td></tr>
          </tbody></table>
        </div>
      </div>
      <div class="reveal">
        <h3>What it gives people</h3>
        <ul class="checklist" style="margin-top:16px">
          <li><strong>Connection</strong> — a warm, weekly reason to gather.</li>
          <li><strong>Dignity and achievement</strong> — the quiet pride of &ldquo;I can make music.&rdquo;</li>
          <li><strong>Gentle stimulation</strong> — memory, coordination, breath and focus.</li>
          <li><strong>Friendship</strong> — bonds that often outlast the term.</li>
        </ul>
        <div class="callout" style="margin-top:24px">
          <span class="tag tag-live">Running now</span>
          <p style="margin-top:12px"><strong>Mulhuddart Community Centre, Dublin 15.</strong>
             Wednesdays 7:00–8:00pm from 9 September 2026, twelve weeks, free — ending with a
             festive concert before Christmas.</p>
          <div class="btn-row"><a class="btn btn-accent" href="get-involved.html">Join the class <span class="arrow">→</span></a></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split split-wide split-center">
    <div class="reveal">
      <p class="eyebrow">The pilot</p>
      <h2 style="font-size:clamp(26px,3.2vw,38px)">Where the model came from.</h2>
      <p class="lead" style="margin-top:18px">Seven retired Presentation Sisters. Ten weekly
         hours at Warrenmount, Dublin 8. An Easter concert of nine pieces at Clondalkin Lodge.
         Completed as Bachelor of Music research at TU Dublin Conservatoire.</p>
      <p style="margin-top:16px">Three months of preparation came first — a needs survey,
         permissions, vetting, individual lessons, part allocation. Descant, alto, tenor and bass
         recorders with melodica, xylophone and small percussion; enlarged scores. All seven
         completed and performed in public.</p>
    </div>
    <figure class="reveal">
      <div class="photo photo-4x3">
        <img src="images/conducting.jpg" width="1400" height="1050"
             alt="Conducting a small ensemble in a community setting">
      </div>
      <figcaption>Every course ends the same way — a concert, however small.</figcaption>
    </figure>
  </div>
</section>

<section class="band-sunken">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">The other programmes</p>
      <h2>Four more ways in.</h2>
    </div>
    <div class="grid grid-2 stagger">
      <article class="card"><span class="kicker">Learning</span>
        <h3>Getting to Know Classical Music</h3>
        <p>Free lecture-recitals, roughly monthly, with recorded and live performance. Three
           stages — <em>Getting Closer</em>, <em>Experiencing Together</em>,
           <em>Discovering My Taste</em> — plus seasonal specials on European summer festivals,
           the BBC Proms, Wexford Opera Festival and Christmas.</p>
        <div class="meta">17 sessions · typical attendance 6–14 · free</div>
      </article>
      <article class="card"><span class="kicker">Learning</span>
        <h3>Concert Guide &amp; Companion</h3>
        <p>Small groups accompanied to concerts they would not attend alone — the National
           Symphony Orchestra, Irish National Opera, the RTÉ Concert Orchestra, the NCH
           International Series, and the BBC Proms in two consecutive summers. Preparation before,
           guidance during, reflection after.</p>
        <div class="meta">Groups of about five · tickets can be as little as £8</div>
      </article>
      <article class="card"><span class="kicker">Sharing</span>
        <h3>Outreach Concerts</h3>
        <p>Live performance brought into care homes, parishes, hospitals, hostels and community
           spaces — from a homeless hostel in Dublin 7 to a martyrs&rsquo; shrine in Daegu.
           Priority counties for growth: Wicklow, Meath and Louth.</p>
        <div class="meta">Since 2023 · target ten or more per year</div>
      </article>
      <article class="card"><span class="kicker">Sharing</span>
        <h3>Letters Ensemble</h3>
        <p>Founded January 2024 by amateur musicians living in Dublin. Weekly Saturday rehearsals.
           Irish traditional, Korean traditional, sacred repertoire and accessible arrangements —
           chosen so that any room can meet the music halfway.</p>
        <div class="meta">4 formal concerts · open to amateur musicians</div>
      </article>
    </div>
    <div class="callout reveal" style="margin-top:26px">
      <span class="kicker" style="color:var(--accent);font-size:11px;font-weight:700;letter-spacing:.15em;text-transform:uppercase">Sub-strand</span>
      <h3 style="margin-top:8px">Bringing Music to Sacred Places</h3>
      <p style="margin-top:10px">The faith-based strand — parishes, shrines, convents, liturgies
         and retired religious communities, roughly sixteen of the twenty outreach performances.
         Described to religious audiences as a lay apostolate through music: a ministry of
         presence rather than a concert series.</p>
    </div>
  </div>
</section>

{CTA}"""


# ---------------------------------------------------------------------------
# Get involved
# ---------------------------------------------------------------------------

GET_INVOLVED = """<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Get involved</p>
    <h1>Four ways in. Pick the one that sounds like you.</h1>
    <p>No audition, no experience assumed, nothing to prepare. If you are not sure which one
       fits, say so — that is a normal enquiry.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="grid grid-2 stagger">
      <article class="card">
        <span class="kicker">For absolute beginners</span>
        <h3>Learn to play</h3>
        <p>Join the recorder ensemble course. First notes in week one, reading music from zero,
           your own part in the ensemble, and a short concert at the end of term.</p>
        <div class="meta">Mulhuddart Community Centre, D15 · Wednesdays 7:00–8:00pm ·
           from 9 September 2026 · free</div>
      </article>
      <article class="card">
        <span class="kicker">If you would rather listen first</span>
        <h3>Come and listen</h3>
        <p>A free lecture-recital, or a small group going to a live concert together — we prepare
           beforehand, sit together, and talk about it after. Especially welcome if you would
           never go alone, or are new to Ireland.</p>
        <div class="meta">Roughly monthly · groups of about five</div>
      </article>
      <article class="card">
        <span class="kicker">If you already play</span>
        <h3>Play with us</h3>
        <p>The Letters Ensemble is open to amateur musicians living in Dublin — weekly Saturday
           rehearsals and concerts in community settings. Volunteers also help with outreach
           logistics.</p>
        <div class="meta">Strings, winds and more welcome</div>
      </article>
      <article class="card">
        <span class="kicker">If you run a venue</span>
        <h3>Host or partner</h3>
        <p>Invite an outreach concert, or host a course for your community. We carry public
           liability insurance and complete Garda vetting where the work requires it.</p>
        <div class="meta">Dublin, Wicklow, Meath, Louth and beyond</div>
      </article>
    </div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">For venues</p>
      <h2>You provide a room and a name. We provide the rest.</h2>
    </div>
    <div class="split reveal">
      <div>
        <h3>The venue provides</h3>
        <ul class="checklist" style="margin-top:16px">
          <li>A warm room seating ten to twelve in a circle, weekly for the term</li>
          <li>Help spreading the word locally</li>
          <li>One named contact person</li>
          <li>Nothing else — no equipment, no admin, no piano</li>
        </ul>
      </div>
      <div>
        <h3>We provide</h3>
        <ul class="checklist" style="margin-top:16px">
          <li>The tutor and the full curriculum</li>
          <li>All scores and weekly materials, printed at our cost</li>
          <li>Guidance on low-cost instruments, and loans where needed</li>
          <li>The end-of-term concert</li>
          <li>Insurance and vetting documentation</li>
        </ul>
      </div>
    </div>
    <div class="callout reveal" style="margin-top:30px">
      <p><strong>On cost.</strong> Every programme keeps free and discounted places. Where a venue
         can pay a facilitation fee from its own budget, participation is free for everyone in the
         room — and that contribution keeps a door open elsewhere. Where it cannot, we will still
         talk.</p>
    </div>
  </div>
</section>

<section class="band-photo">
  <img src="images/quartet-hall.jpg" alt="" width="1400" height="788">
  <div class="wrap narrow reveal" style="text-align:center;margin-inline:auto">
    <p class="eyebrow" style="justify-content:center">Next step</p>
    <h2 style="font-size:clamp(28px,3.6vw,42px)">Write one line.</h2>
    <p class="lead" style="margin-top:18px;color:var(--fg-inverse-body)">Tell us which of the
       four sounds like you and roughly where you are. We will answer with the practical
       details.</p>
    <div class="btn-row" style="justify-content:center">
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
    <p class="eyebrow">News &amp; record</p>
    <h1>What is coming, and what has happened.</h1>
    <p>We keep a ledger rather than a highlight reel. Every session and performance is logged on
       the day, so any figure we quote traces back to a row.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Coming up</p>
      <h2>Autumn 2026.</h2>
    </div>
{WHATS_ON}
    <div class="callout reveal" style="margin-top:26px">
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
        <div class="photo photo-3x2"><img src="images/quartet-hall.jpg" width="1400" height="788"
             alt="An ensemble performing in a bright hall"></div>
        <div class="card-body">
          <span class="tag tag-live">First public funding</span>
          <h3 style="margin-top:12px">South Dublin Live 2026</h3>
          <p>SDCC&rsquo;s Arts Office selected the project for its 2026 programme — the first work
             funded by anyone other than ourselves.</p>
          <div class="meta">August 2026 · SDCC Arts Office</div>
        </div>
      </article>
      <article class="card">
        <span class="kicker">20 August 2026</span>
        <h3>Shared Voices of Care</h3>
        <p>A thirty-minute acoustic drop-in performance in the Atrium of Tallaght University
           Hospital with guest haegeum artist Jaewon Kim — for patients, families, visitors and
           staff. Hosted by the hospital&rsquo;s National Centre for Arts &amp; Health.</p>
        <div class="meta">Tallaght University Hospital</div>
      </article>
      <article class="card">
        <span class="kicker">29 August 2026</span>
        <h3>Shared Voices of Classical Tradition</h3>
        <p>A sixty-minute chamber recital for clarinet, piano and soprano in the Performance Space
           at Rua Red, South Dublin&rsquo;s contemporary arts centre. Free admission.</p>
        <div class="meta">Rua Red, Tallaght</div>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">The story so far</p>
      <h2>From one clarinet to a community.</h2>
    </div>
    <div class="split split-wide">
      <div class="timeline reveal">
        <div class="tl-item"><div class="tl-date">February 2023</div>
          <h4>Before the beginning</h4>
          <p>A clarinet solo at the English-language Mass in Lourdes — the outreach strand, two
             years before it had a name.</p></div>
        <div class="tl-item"><div class="tl-date">January 2024</div>
          <h4>It starts</h4>
          <p>CMFE is founded in Dublin, and the Letters Ensemble with it. The first lecture-recital
             is held in Dublin 18, for six people.</p></div>
        <div class="tl-item"><div class="tl-date">2024</div>
          <h4>Music goes out</h4>
          <p>Concerts at Dalgan Park and for the Missionary Sisters of St Columban; performances in
             London, Paris and Daegu. The lecture series moves to TU Dublin.</p></div>
        <div class="tl-item"><div class="tl-date">2024–2025</div>
          <h4>Going together</h4>
          <p>Accompanied concert-going becomes a strand of its own — the NSO, Irish National Opera,
             and the BBC Proms in two consecutive summers.</p></div>
        <div class="tl-item"><div class="tl-date">October 2025</div>
          <h4>An audience becomes players</h4>
          <p>Preparation begins for a recorder ensemble with seven retired Presentation Sisters —
             survey, permissions, vetting, individual lessons.</p></div>
        <div class="tl-item"><div class="tl-date">December 2025</div>
          <h4>To the National Concert Hall</h4>
          <p>The fifteenth learning session is a concert at Ireland&rsquo;s National Concert Hall,
             attended together.</p></div>
        <div class="tl-item"><div class="tl-date">Jan–Apr 2026</div>
          <h4>The pilot, and its concert</h4>
          <p>Ten weekly rehearsals at Warrenmount, then an Easter concert of nine pieces at
             Clondalkin Lodge. All seven completed.</p></div>
        <div class="tl-item"><div class="tl-date">August 2026</div>
          <h4>First public commission</h4>
          <p>Two concerts for South Dublin Live 2026 — Tallaght University Hospital and Rua Red.</p></div>
        <div class="tl-item"><div class="tl-date">September 2026</div>
          <h4>The model opens to the public</h4>
          <p>The first community recorder ensemble course begins at Mulhuddart Community Centre,
             Dublin 15 — twelve weeks, free.</p></div>
      </div>
      <div>
        <figure class="reveal">
          <div class="photo photo-4x3">
            <img src="images/letters-ensemble.jpg" width="1400" height="1050"
                 alt="The Letters Ensemble with their instruments">
          </div>
          <figcaption>The Letters Ensemble, founded January 2024.</figcaption>
        </figure>
        <div class="callout reveal" style="margin-top:26px">
          <h4>Press &amp; publication</h4>
          <ul class="plainlist" style="margin-top:12px">
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
       that carries music to rooms it would not otherwise reach.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">How the money works</p>
      <h2>A paid booking is what keeps a free seat free.</h2>
      <p>We are a social enterprise rather than a pure charity. That is not a technicality —
         it is what lets the free places survive a dip in goodwill.</p>
    </div>
    <div class="reveal">{dg.subsidy(L)}</div>
  </div>
</section>

<section class="band-raised">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Track record</p>
      <h2>Who has backed this so far.</h2>
      <p>Everything before 2026 was self-funded and voluntary. We publish the record because a
         funder&rsquo;s first question is who came before them.</p>
    </div>
    <div class="table-scroll reveal">
      <table>
        <thead><tr><th scope="col">Source</th><th scope="col">Detail</th><th scope="col">Status</th></tr></thead>
        <tbody>
          <tr><td><strong>South Dublin County Council</strong><br><span class="tiny">Arts Office ·
              South Dublin Live 2026</span></td>
              <td>A commission for <em>Shared Voices of South Dublin</em> — our first publicly
                  funded work.</td><td>Received</td></tr>
          <tr><td><strong>Myongdohoe Scholarship</strong><br><span class="tiny">Lay Apostolate
              Committee, Catholic Bishops&rsquo; Conference of Korea</span></td>
              <td>Termly support from March 2025 for the founder&rsquo;s musical apostolate.</td>
              <td>Concluded</td></tr>
          <tr><td><strong>Individual donors</strong></td>
              <td>Gifts from supporters in Europe and Korea towards making regular outreach
                  possible.</td><td>Ongoing</td></tr>
          <tr><td><strong>Partner venues, in kind</strong></td>
              <td>Tallaght University Hospital — venue and operating time. Mulhuddart Community
                  Centre — the room. TU Dublin — rehearsal space.</td><td>Continuing</td></tr>
          <tr><td><strong>TU Dublin Venture Lab</strong></td>
              <td>Social enterprise start-up programme, from September 2024.</td><td>Completed</td></tr>
        </tbody>
      </table>
    </div>
    <div class="split split-center reveal" style="margin-top:48px">
      <div class="quote">
        <p>&ldquo;Andrew does not undertake this work from a position of material abundance. Even
           within limited personal financial circumstances, he continues to give generously of his
           time, energy, and talent.&rdquo;</p>
        <cite>Donal Roche, Auxiliary Bishop of Dublin · 16 February 2026</cite>
      </div>
      <div>
        <h4>Letters of support</h4>
        <ul class="plainlist" style="margin-top:14px">
          <li><strong>Rua Red</strong> — South Dublin&rsquo;s contemporary arts centre</li>
          <li><strong>The Civic Theatre</strong>, Tallaght</li>
          <li><strong>Tallaght University Hospital</strong> — National Centre for Arts &amp; Health</li>
          <li><strong>SDCC Arts Office</strong> — selection for South Dublin Live 2026</li>
        </ul>
      </div>
    </div>
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
           activity record on request.</p></div>
      <div class="card"><span class="kicker">03</span><h3>Open a door</h3>
        <p>An introduction to a care home, parish, community centre or hospital is worth as much
           as a donation — often more.</p></div>
      <div class="card"><span class="kicker">04</span><h3>Give the room</h3>
        <p>A warm room once a week for a term is the most valuable in-kind gift there is. It
           converts directly into free places.</p></div>
    </div>
    <div class="btn-row reveal" style="justify-content:center;margin-top:36px">
      <a class="btn btn-accent" href="mailto:sby05034@gmail.com?subject=I%20would%20like%20to%20support%20CMFE">Offer support <span class="arrow">→</span></a>
      <a class="btn btn-quiet" href="mailto:sby05034@gmail.com?subject=Partnership%20and%20funding%20enquiry">Request the proposal</a>
    </div>
    <div class="callout reveal" style="margin-top:34px">
      <p class="small"><strong>Please note.</strong> CMFE is a volunteer-led social enterprise
         currently formalising as a not-for-profit company limited by guarantee. We are not yet a
         registered charity, so gifts are not eligible for charitable tax relief. We would rather
         say so plainly than let anyone assume otherwise.</p>
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
      <div class="table-scroll" style="margin-top:24px">
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
      <p class="small" style="margin-top:22px">We hold public liability insurance and complete
         Garda vetting where the work requires it. Documentation is available to partner venues on
         request.</p>
    </div>
    <div class="reveal">
      <h2>Who writes about what</h2>
      <ul class="checklist" style="margin-top:24px">
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
  <div class="wrap narrow reveal" style="text-align:center;margin-inline:auto">
    <p class="eyebrow" style="justify-content:center">Organisation</p>
    <h2>Classical Music for Everyone</h2>
    <p class="lead" style="margin-top:22px">A community music social enterprise founded in Dublin
       in January 2024, currently formalising as a not-for-profit company limited by guarantee.
       Volunteer-led. Community music · social enterprise · arts and health.</p>
  </div>
</section>"""
