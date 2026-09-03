# -*- coding: utf-8 -*-
"""English page content. Facts follow the canonical set (00_최종본, 2026-08-27)."""

BRAND = "Classical Music for Everyone"

# --------------------------------------------------------------------------
# Reusable blocks
# --------------------------------------------------------------------------

STATS = """<div class="stats">
  <div class="wrap stats-grid">
    <div class="stat"><div class="n">40+</div><div class="l">Sessions &amp; performances</div></div>
    <div class="stat"><div class="n">4</div><div class="l">Countries</div></div>
    <div class="stat"><div class="n">20+</div><div class="l">Venues &amp; institutions</div></div>
    <div class="stat"><div class="n">143</div><div class="l">Lecture attendances</div></div>
    <div class="stat"><div class="n">7 / 7</div><div class="l">Pilot participants completed</div></div>
  </div>
</div>"""

WHATS_ON = """<div class="grid grid-2">
  <div class="notice">
    <span class="kicker">Now enrolling</span>
    <h3>Recorder Ensemble — Mulhuddart</h3>
    <p class="small mt-s">A twelve-week course for complete beginners. No experience and no
       music reading required — you will play your first notes in week one.</p>
    <dl>
      <dt>Where</dt><dd>Mulhuddart Community Centre, Dublin 15</dd>
      <dt>When</dt><dd>Wednesdays, 7:00–8:00pm</dd>
      <dt>Starts</dt><dd>9 September 2026 · 12 weeks</dd>
      <dt>Cost</dt><dd>Free</dd>
    </dl>
    <div class="btn-row"><a class="btn btn-primary" href="get-involved.html">How to join</a></div>
  </div>
  <div class="notice">
    <span class="kicker">Coming up</span>
    <h3>An Autumn Concert</h3>
    <p class="small mt-s">Soprano, haegeum, clarinet and piano — Chopin, Pierné, Spohr, Schubert
       and Korean traditional songs. Everyone welcome.</p>
    <dl>
      <dt>Where</dt><dd>Methodist Centenary Church, Leeson Park, Ranelagh, Dublin 6</dd>
      <dt>When</dt><dd>Saturday 19 September 2026, 5:00pm</dd>
      <dt>Admission</dt><dd>Free · donations welcome</dd>
    </dl>
    <div class="btn-row"><a class="btn btn-outline" href="news.html">More dates</a></div>
  </div>
</div>"""

CTA_BAND = """<section class="band-ink">
  <div class="wrap center">
    <div class="section-head">
      <p class="eyebrow">Take part</p>
      <h2>There is a place for you here.</h2>
      <p>Whether you want to learn an instrument for the first time, come and listen,
         play alongside us, or open your venue to a concert — start with an email.</p>
    </div>
    <div class="btn-row" style="justify-content:center">
      <a class="btn btn-gold" href="get-involved.html">Get involved</a>
      <a class="btn btn-ghost-light" href="support.html">Support our work</a>
    </div>
  </div>
</section>"""

# --------------------------------------------------------------------------
# Home
# --------------------------------------------------------------------------

INDEX = """<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Community music · Dublin, Ireland</p>
      <h1>Classical music,<br><em>for everyone.</em></h1>
      <p class="lead">We teach people to play — not only to listen — and we bring live classical
         music to the places it rarely reaches: care homes, parishes, hospitals, hostels and
         community centres across Ireland.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="get-involved.html">Join a class</a>
        <a class="btn btn-outline" href="programmes.html">See what we do</a>
      </div>
    </div>
    <figure class="hero-figure" style="margin:0">
      <img src="images/hero-outreach.jpg" alt="Members of the Letters Ensemble playing a
           St Patrick&rsquo;s Day concert in a community hall" width="1800" height="1350">
      <figcaption class="figure-caption">The Letters Ensemble playing a St Patrick&rsquo;s Day
        concert for a religious community.</figcaption>
    </figure>
  </div>
</section>

""" + STATS + """

<section>
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">What&rsquo;s on</p>
      <h2>Happening now.</h2>
    </div>
""" + WHATS_ON + """
  </div>
</section>

<section class="band-paper">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Why we exist</p>
      <h2>It is playing, not only listening, that restores dignity.</h2>
      <p>Classical music is culturally rich and still out of reach for many people — because of
         age, mobility, income, geography or simple unfamiliarity.</p>
    </div>
    <div class="grid grid-3">
      <div class="card">
        <span class="kicker">One</span>
        <h3>Go to people</h3>
        <p>Rather than expecting people to come to music, we bring music to them. A care home,
           a hospital, a hostel or a rural parish is not a place without an audience — it is
           where the audience that has waited longest already is.</p>
      </div>
      <div class="card">
        <span class="kicker">Two</span>
        <h3>Don&rsquo;t stop at listening</h3>
        <p>A visit that is only a performance ends when the music does. The moment an instrument
           is placed in someone&rsquo;s hands they stop being an audience and become a player —
           and a term becomes a relationship.</p>
      </div>
      <div class="card">
        <span class="kicker">Three</span>
        <h3>A social enterprise</h3>
        <p>Contributions from those who can, and fees paid by institutions, cross-subsidise
           places for those who cannot. Every programme keeps free and discounted places, so
           cost is never the reason someone is left out.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">How it works</p>
      <h2>Two pillars, one loop.</h2>
      <p>Learning leads to lived musical experience; experience encourages sharing; and sharing
         draws people back into deeper participation. The two are not separate departments —
         they feed each other.</p>
    </div>
    <div class="grid grid-2">
      <div class="pillar">
        <span class="tag">Pillar I</span>
        <h3>Learning — opening the door</h3>
        <ul>
          <li><strong>Recorder Ensemble course</strong> — adults and older beginners learn, over a
              term, to play together. Our flagship programme.</li>
          <li><strong>Getting to Know Classical Music</strong> — free lecture-recitals, roughly
              monthly, with no prior knowledge required.</li>
          <li><strong>Concert Guide &amp; Companion</strong> — accompanying small groups to live
              concerts they would not attend alone.</li>
        </ul>
      </div>
      <div class="pillar">
        <span class="tag">Pillar II</span>
        <h3>Sharing — carrying the music out</h3>
        <ul>
          <li><strong>Outreach Concerts</strong> — music that comes to you: care, parish, hospital,
              hostel and community settings.</li>
          <li><strong>Letters Ensemble</strong> — amateur musicians in Dublin given a reason to
              keep playing.</li>
          <li><strong>Bringing Music to Sacred Places</strong> — the faith-based strand: parishes,
              shrines and retired religious communities.</li>
        </ul>
      </div>
    </div>
    <div class="callout mt-m">
      <p>A question — <em>&ldquo;could I do that?&rdquo;</em> — comes out of the rooms we play in,
         and that question becomes a recorder ensemble. In 2024 we played for the Missionary
         Sisters of St Columban; a sister asked whether she might play again. By 2026 seven
         retired sisters were an ensemble of their own.</p>
    </div>
  </div>
</section>

<section class="band-cream">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">What we run</p>
      <h2>Five programmes, one belief.</h2>
    </div>
    <div class="grid grid-3">
      <article class="card card-media">
        <img src="images/community-room.jpg" alt="Playing the clarinet in a community room"
             width="1400" height="1050">
        <div class="card-body">
          <span class="kicker">Flagship</span>
          <h3>Recorder Ensemble</h3>
          <p>A term-long course for complete beginners — first notes in week one, reading music
             from zero, then a part of your own in the ensemble, ending in a concert for family
             and friends.</p>
          <div class="meta">Weekly · community centres &amp; parishes</div>
        </div>
      </article>
      <article class="card card-media">
        <img src="images/care-christmas.jpg" alt="A quartet performing in a care setting at Christmas"
             width="1400" height="1050">
        <div class="card-body">
          <span class="kicker">Outreach</span>
          <h3>Music that comes to you</h3>
          <p>Live performance brought into care homes, parishes, hospitals, hostels and community
             spaces — twenty performances so far, across four countries and more than fifteen
             venues.</p>
          <div class="meta">Since 2023 · Dublin, Wicklow, Meath &amp; beyond</div>
        </div>
      </article>
      <article class="card card-media">
        <img src="images/lecture-recital.jpg" alt="A lecture-recital in progress"
             width="1400" height="1050">
        <div class="card-body">
          <span class="kicker">Learning</span>
          <h3>Getting to Know Classical Music</h3>
          <p>Free lecture-recitals, roughly monthly, open to all — music history, listening,
             composers and instruments, with seasonal specials and live performance.</p>
          <div class="meta">17 sessions · 143 attendances</div>
        </div>
      </article>
    </div>
    <div class="btn-row"><a class="btn btn-outline" href="programmes.html">All five programmes</a></div>
  </div>
</section>

<section class="band-paper">
  <div class="wrap split split-wide">
    <div>
      <p class="eyebrow">Endorsement</p>
      <div class="quote">
        <p>&ldquo;Through music, he offers encouragement, dignity, and spiritual accompaniment to
           those who may otherwise feel isolated. He seeks to build community rather than act
           independently.&rdquo;</p>
        <cite>Donal Roche, Auxiliary Bishop of Dublin · 16 February 2026</cite>
      </div>
    </div>
    <div>
      <h3>Backed by the record, not the rhetoric</h3>
      <p class="mt-s">In 2026 South Dublin County Council&rsquo;s Arts Office selected the project
         for <strong>South Dublin Live 2026</strong> — our first publicly funded commission.
         Everything before that had been self-funded and voluntary.</p>
      <p>Letters of support are held from Rua Red, The Civic and Tallaght University Hospital,
         whose National Centre for Arts &amp; Health hosted a concert in its Atrium.</p>
      <div class="btn-row"><a class="btn btn-outline" href="support.html">Funding &amp; support to date</a></div>
    </div>
  </div>
</section>

""" + CTA_BAND

# --------------------------------------------------------------------------
# About
# --------------------------------------------------------------------------

ABOUT = """<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">About us</p>
    <h1>Music should be a shared, everyday experience.</h1>
    <p>Classical Music for Everyone is a community music social enterprise founded in Dublin in
       January 2024. We were created in response to a simple observation: despite its cultural
       richness, classical music remains out of reach for many people.</p>
  </div>
</section>

<section>
  <div class="wrap split">
    <div>
      <h2>Mission</h2>
      <p class="lead mt-s">To make live classical music genuinely available to everyone —
         regardless of age, background, mobility, income or prior musical knowledge — by teaching
         people to play, playing alongside them, and bringing music to the places it does not
         normally reach.</p>
      <h2 class="mt-l">Vision</h2>
      <p class="lead mt-s">An Ireland in which every community — urban, rural, in care, and living
         with disability — has a realistic, welcoming pathway into making music together,
         delivered by educators in secure, properly paid employment.</p>
    </div>
    <div class="figure">
      <img src="images/clarinet.jpg" alt="Andrew Seohyeon Kim playing the clarinet during a
           liturgy" width="1400" height="1400">
      <p class="figure-caption">Playing at a parish liturgy in Dublin.</p>
    </div>
  </div>
</section>

<section class="band-paper">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">What guides us</p>
      <h2>Five values, described by what they cost us.</h2>
    </div>
    <div class="grid grid-2">
      <div>
        <div class="value" style="border-top:0">
          <h4>Dignity</h4>
          <p>Everyone is received with respect and treated as someone who can still create —
             regardless of age, health or circumstance.</p>
        </div>
        <div class="value">
          <h4>Accessibility</h4>
          <p>We lower the barriers of price, distance and unfamiliarity. Physical, environmental
             and psychological barriers should not prevent engagement with music.</p>
        </div>
        <div class="value">
          <h4>Accompaniment</h4>
          <p>We stay alongside people over a whole term, not for a one-off visit. Meaningful
             engagement grows through continuity.</p>
        </div>
      </div>
      <div>
        <div class="value" style="border-top:0">
          <h4>Community</h4>
          <p>Music that connects people across age, background and language.</p>
        </div>
        <div class="value">
          <h4>Hope</h4>
          <p>We do not promise dramatic transformation. We value small, real moments of connection
             — the quiet lift of learning something new, together.</p>
        </div>
        <div class="value">
          <h4>And — work for educators</h4>
          <p>Music educators mostly work in precarious freelance conditions. Our second social aim
             is to employ them properly.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">The founder</p>
      <h2>Andrew Seohyeon Kim</h2>
    </div>
    <div class="split split-wide">
      <div>
        <p class="lead">Andrew Seohyeon Kim is a clarinettist, organist and community music
           practitioner based in Dublin, and the founder and project lead of Classical Music for
           Everyone.</p>
        <p class="mt-m">He graduated from TU Dublin Conservatoire with a Bachelor of Music (Hons)
           in Performance, studying clarinet with Dr Paul Roe alongside organ, cello and piano,
           and completing conducting training with the Irish Association of Youth Orchestras and
           the London Conducting Workshop. His final-year research was a practice-based study of a
           ten-week recorder ensemble he designed and led for seven retired Presentation Sisters
           in Dublin.</p>
        <p>Since 2022 he has served as Music Director at Our Lady of Dolours Church,
           Dolphin&rsquo;s Barn, and since 2023 as organist at the Church of the Three Patrons,
           Rathgar. In 2024 he founded both Classical Music for Everyone and the Letters
           Ensemble.</p>
        <p>He has volunteered at World Youth Day Lisbon 2023, ClarinetFest 2024, the Dublin
           International Piano Competition 2025 and the Jubilee of Youth in Rome, and holds a
           Myongdohoe scholarship from the Lay Apostolate Committee of the Catholic
           Bishops&rsquo; Conference of Korea.</p>
      </div>
      <div class="figure">
        <img src="images/organ.jpg" alt="An organ console with music open on the stand"
             width="1400" height="1050">
        <p class="figure-caption">Weekly organ and music-direction duties in two Dublin parishes
           sit alongside the community work.</p>
      </div>
    </div>
  </div>
</section>

<section class="band-cream">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Where we have played</p>
      <h2>Venues and institutions to date.</h2>
      <p>Residential and nursing care · religious communities · parishes · a university ·
         a national concert hall · an HSE day service · a homeless hostel · community centres ·
         a public cultural event.</p>
    </div>
    <div class="split">
      <div>
        <h4>Ireland</h4>
        <ul class="plainlist mt-s">
          <li>National Concert Hall, Dublin — concert outings attended together</li>
          <li>TU Dublin, Grangegorman</li>
          <li>Tallaght University Hospital &amp; Rua Red, Tallaght</li>
          <li>Our Lady of Dolours Church, Dolphin&rsquo;s Barn</li>
          <li>Church of the Three Patrons, Rathgar</li>
          <li>Carmelite Community Centre &amp; Blessed Sacrament Chapel, Dublin</li>
          <li>Clondalkin Lodge &amp; Warrenmount, Dublin</li>
          <li>Missionary Sisters of St Columban, Co. Wicklow</li>
          <li>Franciscan Missionaries of Mary, Dublin 5</li>
          <li>Dalgan Park &amp; Kilmessan Church, Co. Meath</li>
          <li>Dysart Parish, Co. Westmeath</li>
          <li>HSE EVE Goirtin Hub &amp; Morning Star Hostel, Dublin 7</li>
          <li>Methodist Centenary Church, Ranelagh</li>
          <li>Mulhuddart Community Centre, Dublin 15</li>
        </ul>
      </div>
      <div>
        <h4>Abroad</h4>
        <ul class="plainlist mt-s">
          <li>Sanctuary of Our Lady of Lourdes, France</li>
          <li>Missions Étrangères de Paris, France</li>
          <li>Palais Brongniart, Paris, France</li>
          <li>London Korean Catholic Church, United Kingdom</li>
          <li>Gwandukjeong Martyrs Memorial Centre, Daegu, Korea</li>
        </ul>
        <div class="callout mt-m">
          <h4>What we do not claim</h4>
          <p class="small mt-s">Our evidence to date is participation, retention and testimony
             rather than measured outcome. We have not measured wellbeing with a validated
             instrument, and audience numbers at outreach performances were not recorded. Seven of
             seven pilot participants completed and performed publicly, and lecture attendance
             more than doubled over two years. From the autumn 2026 cohort we are introducing a
             simple pre/post measure and a consent framework.</p>
        </div>
      </div>
    </div>
  </div>
</section>

""" + CTA_BAND

# --------------------------------------------------------------------------
# Programmes
# --------------------------------------------------------------------------

PROGRAMMES = """<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Programmes</p>
    <h1>What we actually run.</h1>
    <p>Five programme strands under two pillars, plus one faith-based sub-strand. The Recorder
       Ensemble course is the flagship; everything else either feeds it or grows out of it.</p>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="table-scroll">
      <table>
        <thead>
          <tr><th scope="col">Programme</th><th scope="col">Pillar</th>
              <th scope="col">Status</th><th scope="col">Delivered to date</th></tr>
        </thead>
        <tbody>
          <tr><td><strong>Recorder Ensemble course</strong></td><td>Learning</td>
              <td>Flagship · running</td><td>Pilot complete; first community class from Sept 2026</td></tr>
          <tr><td><strong>Getting to Know Classical Music</strong></td><td>Learning</td>
              <td>Running · free</td><td>17 lecture-recitals · 143 attendances</td></tr>
          <tr><td><strong>Concert Guide &amp; Companion</strong></td><td>Learning</td>
              <td>Running</td><td>10 recorded outings, including two summers at the BBC Proms</td></tr>
          <tr><td><strong>Outreach Concerts</strong></td><td>Sharing</td>
              <td>Running</td><td>20 performances · 4 countries · 15+ venues</td></tr>
          <tr><td style="padding-left:34px">↳ Bringing Music to Sacred Places</td><td>Sharing</td>
              <td>Sub-strand</td><td>Around 16 of the 20 outreach performances</td></tr>
          <tr><td><strong>Letters Ensemble</strong></td><td>Sharing</td>
              <td>Running</td><td>4 formal concerts · weekly rehearsals since Jan 2024</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="band-paper">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Flagship programme</p>
      <h2>Recorder Ensemble — a term, from nothing to a concert.</h2>
      <p>A course for complete beginners. No experience and no music reading required. It is
         gentle on the hands and breath, quick to a first satisfying sound, inexpensive, and made
         for playing together — the friendliest possible doorway into making music.</p>
    </div>
    <div class="grid grid-4">
      <div class="card">
        <span class="kicker">Step 01</span><h3>Play your first notes</h3>
        <p>Hold it, breathe, play. Real sound in week one.</p>
      </div>
      <div class="card">
        <span class="kicker">Step 02</span><h3>Read music from zero</h3>
        <p>Small steps every week. Easier than you think.</p>
      </div>
      <div class="card">
        <span class="kicker">Step 03</span><h3>Play in harmony</h3>
        <p>Your own part in the ensemble. The moment it clicks.</p>
      </div>
      <div class="card">
        <span class="kicker">Step 04</span><h3>Perform a concert</h3>
        <p>A short concert for family and friends in the final week.</p>
      </div>
    </div>

    <div class="split mt-l">
      <div>
        <h3>What it looks like</h3>
        <div class="table-scroll mt-s">
          <table>
            <tbody>
              <tr><td><strong>Length</strong></td><td>One term, weekly</td></tr>
              <tr><td><strong>Session</strong></td><td>60–90 minutes</td></tr>
              <tr><td><strong>Group</strong></td><td>Small and friendly</td></tr>
              <tr><td><strong>Entry level</strong></td><td>Complete beginners</td></tr>
              <tr><td><strong>Instrument</strong></td><td>Descant recorder — low cost; we advise on
                  buying one, supply at cost, or lend you one</td></tr>
              <tr><td><strong>Materials</strong></td><td>Scores and weekly handouts, produced and
                  printed by us. No cost to participants.</td></tr>
              <tr><td><strong>Ending</strong></td><td>A short concert for family and friends</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div>
        <h3>What it gives people</h3>
        <ul class="checklist mt-s">
          <li><strong>Connection</strong> — a warm, weekly reason to gather and belong.</li>
          <li><strong>Dignity and achievement</strong> — the quiet pride of &ldquo;I can make
              music.&rdquo;</li>
          <li><strong>Gentle stimulation</strong> — for memory, coordination, breath and focus.</li>
          <li><strong>Friendship</strong> — bonds that often outlast the term itself.</li>
        </ul>
        <div class="callout mt-m">
          <span class="kicker">Running now</span>
          <p class="mt-s"><strong>Mulhuddart Community Centre, Dublin 15.</strong> Wednesdays
             7:00–8:00pm from 9 September 2026, twelve weeks, free of charge, ending with a
             festive concert for family and friends before Christmas.</p>
          <div class="btn-row"><a class="btn btn-gold" href="get-involved.html">Join the class</a></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">The pilot</p>
      <h2>Where the model came from.</h2>
    </div>
    <div class="split split-wide">
      <div>
        <p class="lead">The model grew from a practice-based pilot study — a ten-week recorder
           ensemble designed and led by the founder for seven retired Presentation Sisters at
           Warrenmount, Dublin 8, meeting weekly for one hour and concluding with an Easter
           concert of nine pieces at Clondalkin Lodge, completed as Bachelor of Music research at
           TU Dublin Conservatoire.</p>
        <p class="mt-m">Three months of preparation came first — a needs survey, permissions,
           vetting, individual lessons and part allocation. The ensemble used descant, alto, tenor
           and bass recorders alongside melodica, xylophone and small percussion, with enlarged
           scores. All seven participants completed the course and performed in public. The group
           continued in weekly sessions afterwards and concluded in August 2026.</p>
      </div>
      <div class="figure">
        <img src="images/conducting.jpg" alt="Conducting a small ensemble in a community setting"
             width="1400" height="1050">
        <p class="figure-caption">Every course ends the same way — a concert, however small.</p>
      </div>
    </div>
  </div>
</section>

<section class="band-cream">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">The other programmes</p>
      <h2>Four more ways in.</h2>
    </div>
    <div class="grid grid-2">
      <article class="card">
        <span class="kicker">Learning</span>
        <h3>Getting to Know Classical Music</h3>
        <p>Free lecture-recitals, roughly monthly, open to all with no prior knowledge required —
           a presentation with recorded and live performance. The curriculum runs in three stages:
           <em>Getting Closer</em>, <em>Experiencing Together</em>, <em>Discovering My Taste</em>,
           with seasonal specials on European summer festivals, the BBC Proms, the Wexford Opera
           Festival and Christmas.</p>
        <div class="meta">17 sessions since 2024 · typical attendance 6–14 · free</div>
      </article>
      <article class="card">
        <span class="kicker">Learning</span>
        <h3>Concert Guide &amp; Companion</h3>
        <p>Small groups accompanied to live concerts they would not attend alone — National
           Symphony Orchestra Friday concerts, Irish National Opera, the RTÉ Concert Orchestra,
           the TU Dublin Philharmonic and the National Concert Hall International Series, plus
           companion trips to the BBC Proms in two consecutive summers. Three stages: preparation
           before, guidance during, reflection after.</p>
        <div class="meta">Groups of about five · tickets can be as little as £8</div>
      </article>
      <article class="card">
        <span class="kicker">Sharing</span>
        <h3>Outreach Concerts</h3>
        <p>&lsquo;Music that comes to you&rsquo; — live performance brought into care homes,
           parishes, hospitals, hostels and community spaces. Twenty performances so far across
           four countries and more than fifteen venues, from a homeless hostel in Dublin 7 to a
           martyrs&rsquo; shrine in Daegu. Priority counties for growth: Wicklow, Meath and
           Louth.</p>
        <div class="meta">Since 2023 · target ten or more per year</div>
      </article>
      <article class="card">
        <span class="kicker">Sharing</span>
        <h3>Letters Ensemble</h3>
        <p>Founded in January 2024 by amateur musicians living in Dublin, and directed by
           CMFE&rsquo;s founder. Weekly Saturday rehearsals of about two hours in educational and
           community spaces. The repertoire is Irish traditional, Korean traditional, sacred
           repertoire, accessible contemporary arrangements and selected popular pieces — chosen
           so that any room can meet it halfway.</p>
        <div class="meta">4 formal concerts · open to amateur musicians</div>
      </article>
    </div>
    <div class="callout mt-m">
      <span class="kicker">Sub-strand</span>
      <h3 class="mt-s">Bringing Music to Sacred Places</h3>
      <p class="mt-s">The faith-based strand of the outreach work — parishes, shrines, convents,
         liturgies and retired religious communities, accounting for roughly sixteen of the twenty
         outreach performances. It is described to religious audiences as a lay apostolate through
         music: a ministry of presence and accompaniment rather than a concert series.</p>
    </div>
  </div>
</section>

""" + CTA_BAND

# --------------------------------------------------------------------------
# Get involved
# --------------------------------------------------------------------------

GET_INVOLVED = """<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Get involved</p>
    <h1>Four ways in — pick the one that sounds like you.</h1>
    <p>No audition, no experience assumed, and nothing to prepare. If you are unsure which one
       fits, write and say so — that is a normal enquiry, not a nuisance.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="grid grid-2">
      <article class="card">
        <span class="kicker">For absolute beginners</span>
        <h3>Learn to play</h3>
        <p>Join the recorder ensemble course. You will play your first notes in week one, learn to
           read music from zero, take a part of your own in the ensemble, and finish the term with
           a short concert for family and friends. Complete beginners are exactly who this is
           for.</p>
        <div class="meta">Mulhuddart Community Centre, D15 · Wednesdays 7:00–8:00pm ·
          from 9 September 2026 · 12 weeks · free</div>
      </article>
      <article class="card">
        <span class="kicker">If you would rather listen first</span>
        <h3>Come and listen</h3>
        <p>Come to a free lecture-recital, or join a small group going to a live concert together
           — we prepare beforehand, sit together, and talk about it afterwards. Especially welcome
           if you would never go to a concert on your own, or are new to Ireland.</p>
        <div class="meta">Free lecture-recitals, roughly monthly · groups of about five</div>
      </article>
      <article class="card">
        <span class="kicker">If you already play</span>
        <h3>Play with us</h3>
        <p>The Letters Ensemble is an amateur ensemble for people living in Dublin who want a
           reason to keep playing — weekly Saturday-afternoon rehearsals, and concerts in
           community settings. Volunteers also help with outreach logistics and facilitation.</p>
        <div class="meta">Weekly rehearsals · strings, winds and more welcome</div>
      </article>
      <article class="card">
        <span class="kicker">If you run a venue</span>
        <h3>Host or partner</h3>
        <p>Run a community centre, parish, care home, hospital or day service? Invite an outreach
           concert, or host a recorder ensemble course for your community. We hold public
           liability insurance and complete Garda vetting where required.</p>
        <div class="meta">Dublin, Wicklow, Meath, Louth and beyond</div>
      </article>
    </div>
  </div>
</section>

<section class="band-paper">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">For venues</p>
      <h2>What we ask, and what we bring.</h2>
      <p>Hosting a course is deliberately light on the venue. You provide a room and a name; we
         provide everything else.</p>
    </div>
    <div class="split">
      <div>
        <h3>The venue provides</h3>
        <ul class="checklist mt-s">
          <li>A warm room seating ten to twelve in a circle, once a week for the term</li>
          <li>Help spreading the word to local people</li>
          <li>One named contact person</li>
          <li>Nothing else — no equipment, no admin, no piano required</li>
        </ul>
      </div>
      <div>
        <h3>We provide</h3>
        <ul class="checklist mt-s">
          <li>The tutor and the full curriculum</li>
          <li>All scores and weekly materials, printed at our cost</li>
          <li>Guidance on low-cost instruments, and loans where needed</li>
          <li>The end-of-term concert</li>
          <li>Insurance and vetting documentation</li>
        </ul>
      </div>
    </div>
    <div class="callout mt-m">
      <p><strong>On cost.</strong> Every programme keeps free and discounted places. Where a venue
         or an institution can pay a facilitation fee from its own budget, participation is free
         for everyone in the room — and that contribution keeps the door open elsewhere. Where it
         cannot, we will still talk.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap narrow center">
    <div class="section-head">
      <p class="eyebrow">Next step</p>
      <h2>Write one line.</h2>
      <p>Tell us which of the four sounds like you and roughly where you are. That is enough to
         start — we will answer with the practical details.</p>
    </div>
    <div class="btn-row" style="justify-content:center">
      <a class="btn btn-gold" href="mailto:sby05034@gmail.com?subject=Getting%20involved%20with%20CMFE">Email us</a>
      <a class="btn btn-outline" href="contact.html">All contact details</a>
    </div>
  </div>
</section>"""

# --------------------------------------------------------------------------
# News
# --------------------------------------------------------------------------

NEWS = """<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">News &amp; record</p>
    <h1>What is coming, and what has happened.</h1>
    <p>Our record is kept as a ledger rather than a highlight reel — every session and performance
       is logged on the day, so that any figure we quote can be traced back to a row.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Coming up</p>
      <h2>Autumn 2026.</h2>
    </div>
""" + WHATS_ON + """
    <div class="callout mt-m">
      <p><strong>December 2026 —</strong> a festive pre-Christmas concert for family and friends
         closes the first Mulhuddart course. Details to follow.</p>
    </div>
  </div>
</section>

<section class="band-paper">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">This year</p>
      <h2>2026 so far.</h2>
    </div>
    <div class="grid grid-3">
      <article class="card card-media">
        <img src="images/quartet-hall.jpg" alt="An ensemble performing in a bright hall"
             width="1400" height="788">
        <div class="card-body">
          <span class="tag tag-live">First public funding</span>
          <h3 class="mt-s">Shared Voices of South Dublin</h3>
          <p>South Dublin County Council&rsquo;s Arts Office selected the project for <strong>South
             Dublin Live 2026</strong> — our first publicly funded commission.</p>
          <div class="meta">Aug 2026 · SDCC Arts Office</div>
        </div>
      </article>
      <article class="card">
        <span class="kicker">20 August 2026</span>
        <h3>Shared Voices of Care</h3>
        <p>A thirty-minute acoustic drop-in performance in the Atrium of Tallaght University
           Hospital, with guest haegeum artist Jaewon Kim — for patients, families, visitors and
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
    <div class="section-head">
      <p class="eyebrow">The story so far</p>
      <h2>From one clarinet to a community.</h2>
    </div>
    <div class="split split-wide">
      <div class="timeline">
        <div class="tl-item">
          <div class="tl-date">February 2023</div>
          <h4>Before the beginning</h4>
          <p>A clarinet solo at the English-language Mass in Lourdes — the first of what would
             become the outreach strand, two years before it had a name.</p>
        </div>
        <div class="tl-item">
          <div class="tl-date">January 2024</div>
          <h4>It starts</h4>
          <p>Classical Music for Everyone is founded in Dublin, and the Letters Ensemble with it.
             The first lecture-recital is held at Sandyford Hall Places, Dublin 18, for six
             people.</p>
        </div>
        <div class="tl-item">
          <div class="tl-date">2024</div>
          <h4>Music goes out</h4>
          <p>Concerts at Dalgan Park, Co. Meath and for the Missionary Sisters of St Columban in
             Co. Wicklow; performances in London, Paris and Daegu. The lecture series moves to
             TU Dublin and attendance grows.</p>
        </div>
        <div class="tl-item">
          <div class="tl-date">2024–2025</div>
          <h4>Going together</h4>
          <p>Accompanied concert-going becomes a strand of its own — the National Symphony
             Orchestra, Irish National Opera, and the BBC Proms in two consecutive summers.</p>
        </div>
        <div class="tl-item">
          <div class="tl-date">October 2025</div>
          <h4>An audience becomes players</h4>
          <p>Preparation begins for a recorder ensemble with seven retired Presentation Sisters —
             a needs survey, permissions, vetting and individual lessons.</p>
        </div>
        <div class="tl-item">
          <div class="tl-date">December 2025</div>
          <h4>To the National Concert Hall</h4>
          <p>The fifteenth learning session is a concert at Ireland&rsquo;s National Concert Hall,
             attended together.</p>
        </div>
        <div class="tl-item">
          <div class="tl-date">Jan–Apr 2026</div>
          <h4>The pilot, and its concert</h4>
          <p>Ten weekly rehearsals at Warrenmount, Dublin 8, then an Easter concert of nine pieces
             at Clondalkin Lodge. All seven participants completed.</p>
        </div>
        <div class="tl-item">
          <div class="tl-date">August 2026</div>
          <h4>First public commission</h4>
          <p>Two concerts for South Dublin Live 2026 — Tallaght University Hospital and Rua Red.
             The first work funded by anyone other than ourselves.</p>
        </div>
        <div class="tl-item">
          <div class="tl-date">September 2026</div>
          <h4>The model opens to the public</h4>
          <p>The first community recorder ensemble course begins at Mulhuddart Community Centre,
             Dublin 15 — twelve weeks, free of charge.</p>
        </div>
      </div>
      <div>
        <div class="figure">
          <img src="images/letters-ensemble.jpg" alt="The Letters Ensemble with their instruments"
               width="1400" height="1050">
          <p class="figure-caption">The Letters Ensemble, founded January 2024.</p>
        </div>
        <div class="callout mt-m">
          <h4>Press &amp; publication</h4>
          <ul class="plainlist mt-s">
            <li><strong>Kyunghyang Magazine</strong>, May 2026 — a commissioned article for the
                feature &ldquo;Young people, how are you?&rdquo;</li>
            <li><strong>Catholic University student paper</strong>, March 2026 — &ldquo;Fáilte go
                hÉirinn! Do you know Ireland?&rdquo;</li>
            <li><strong>Concert review</strong>, March 2025 — &ldquo;Music: a gift God gave to
                everyone&rdquo;</li>
            <li><strong>The Echo</strong>, August 2026 — advertisements for the Rua Red and
                Tallaght University Hospital concerts</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

""" + CTA_BAND

# --------------------------------------------------------------------------
# Support
# --------------------------------------------------------------------------

SUPPORT = """<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Support</p>
    <h1>Help keep the door open.</h1>
    <p>We are volunteer-led. Support pays for recorders and scores, room hire, and the travel that
       carries music to rooms it would not otherwise reach — and it keeps free places free.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">What support does</p>
      <h2>Three things money actually buys.</h2>
    </div>
    <div class="grid grid-3">
      <div class="card">
        <span class="kicker">Instruments &amp; materials</span>
        <h3>A recorder in every hand</h3>
        <p>A descant recorder is inexpensive, and that is the point — but it is not free. We advise
           on buying one, supply at cost, or lend one, and we print every score and handout so
           that participants pay nothing for materials.</p>
      </div>
      <div class="card">
        <span class="kicker">Rooms</span>
        <h3>A warm room, every week</h3>
        <p>Dublin community hall hire runs from roughly €15 to €40 an hour. Where a venue can offer
           the room free or reduced, the saving goes straight into free places; where it cannot,
           support covers the difference.</p>
      </div>
      <div class="card">
        <span class="kicker">Travel</span>
        <h3>Getting there at all</h3>
        <p>A &lsquo;go to people&rsquo; model lives or dies on transport. Moving performers,
           instruments and stands to care homes and rural parishes is our single largest cost per
           outreach concert.</p>
      </div>
    </div>
  </div>
</section>

<section class="band-paper">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Track record</p>
      <h2>Who has backed this so far.</h2>
      <p>Everything before 2026 was self-funded and voluntary. We publish the record because a
         funder&rsquo;s first question is who came before them.</p>
    </div>
    <div class="table-scroll">
      <table>
        <thead>
          <tr><th scope="col">Source</th><th scope="col">Detail</th><th scope="col">Status</th></tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>South Dublin County Council</strong><br><span class="small">Arts Office ·
                South Dublin Live 2026</span></td>
            <td>A commission for the series <em>Shared Voices of South Dublin</em> —
                our first publicly funded work.</td>
            <td>Received</td>
          </tr>
          <tr>
            <td><strong>Myongdohoe Scholarship</strong><br><span class="small">Lay Apostolate
                Committee, Catholic Bishops&rsquo; Conference of Korea</span></td>
            <td>Termly support from March 2025 for the founder&rsquo;s musical apostolate.</td>
            <td>Concluded</td>
          </tr>
          <tr>
            <td><strong>Individual donors</strong></td>
            <td>Gifts from supporters in Europe and Korea towards making regular outreach
                possible.</td>
            <td>Ongoing</td>
          </tr>
          <tr>
            <td><strong>Partner venues, in kind</strong></td>
            <td>Tallaght University Hospital — venue and operating time. Mulhuddart Community
                Centre — the room. TU Dublin — rehearsal space.</td>
            <td>Continuing</td>
          </tr>
          <tr>
            <td><strong>TU Dublin Venture Lab</strong></td>
            <td>Social enterprise start-up programme, from September 2024.</td>
            <td>Completed</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="split mt-l">
      <div class="quote">
        <p>&ldquo;Andrew does not undertake this work from a position of material abundance. Even
           within limited personal financial circumstances, he continues to give generously of his
           time, energy, and talent.&rdquo;</p>
        <cite>Donal Roche, Auxiliary Bishop of Dublin · 16 February 2026</cite>
      </div>
      <div>
        <h3>Letters of support</h3>
        <ul class="plainlist mt-s">
          <li><strong>Rua Red</strong> — South Dublin&rsquo;s contemporary arts centre</li>
          <li><strong>The Civic Theatre</strong>, Tallaght</li>
          <li><strong>Tallaght University Hospital</strong> — National Centre for Arts &amp;
              Health</li>
          <li><strong>SDCC Arts Office</strong> — selection for South Dublin Live 2026</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="band-cream">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">How to help</p>
      <h2>Four kinds of support, all of them useful.</h2>
    </div>
    <div class="grid grid-2">
      <div class="card">
        <h3>Give</h3>
        <p>A one-off or regular gift goes to instruments, materials, room hire and travel. Write to
           us and we will send the current payment details and tell you exactly what your gift is
           funding.</p>
        <div class="btn-row"><a class="btn btn-gold"
          href="mailto:sby05034@gmail.com?subject=I%20would%20like%20to%20support%20CMFE">Offer support</a></div>
      </div>
      <div class="card">
        <h3>Fund a programme</h3>
        <p>For trusts, foundations, councils and corporate funders: a full proposal, budget and
           cost breakdown is available on request, along with our activity record and letters of
           support.</p>
        <div class="btn-row"><a class="btn btn-outline"
          href="mailto:sby05034@gmail.com?subject=Partnership%20and%20funding%20enquiry">Request the proposal</a></div>
      </div>
      <div class="card">
        <h3>Open a door</h3>
        <p>An introduction to a care home, parish, community centre, day service or hospital is
           worth as much as a donation — often more, because it is where the work happens.</p>
      </div>
      <div class="card">
        <h3>Give the room</h3>
        <p>A warm room once a week for a term is the single most valuable in-kind gift there is.
           It converts directly into free places.</p>
      </div>
    </div>
    <div class="callout mt-m">
      <p class="small"><strong>Please note.</strong> Classical Music for Everyone is a
         volunteer-led social enterprise currently formalising as a not-for-profit company limited
         by guarantee. We are not yet a registered charity, so gifts are not eligible for charitable
         tax relief. We would rather say so plainly than let anyone assume otherwise.</p>
    </div>
  </div>
</section>"""

# --------------------------------------------------------------------------
# Contact
# --------------------------------------------------------------------------

CONTACT = """<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Contact</p>
    <h1>Write to us.</h1>
    <p>Every enquiry reaches the founder directly. A single line is enough — say roughly what you
       are asking about and where you are, and you will get a practical answer back.</p>
  </div>
</section>

<section>
  <div class="wrap split">
    <div>
      <h2>Details</h2>
      <div class="table-scroll mt-m">
        <table>
          <tbody>
            <tr><td><strong>Email</strong></td>
                <td><a href="mailto:sby05034@gmail.com">sby05034@gmail.com</a></td></tr>
            <tr><td><strong>Phone</strong></td>
                <td><a href="tel:+353830780635">+353 83 078 0635</a></td></tr>
            <tr><td><strong>Based in</strong></td><td>Dublin, Ireland</td></tr>
            <tr><td><strong>We travel to</strong></td>
                <td>Dublin, Co. Meath, Co. Wicklow, Co. Westmeath — and further by arrangement</td></tr>
            <tr><td><strong>Founder</strong></td>
                <td>Andrew Seohyeon Kim, BMus (Hons), TU Dublin Conservatoire</td></tr>
            <tr><td><strong>Languages</strong></td><td>English · 한국어</td></tr>
          </tbody>
        </table>
      </div>
      <p class="small mt-m">We hold public liability insurance and complete Garda vetting where
         the work requires it. Documentation is available to partner venues on request.</p>
    </div>
    <div>
      <h2>Who writes about what</h2>
      <ul class="checklist mt-m">
        <li><strong>Joining a class</strong> — say which venue, and whether you have played
            anything before. &ldquo;Never&rdquo; is a completely normal answer.</li>
        <li><strong>Inviting a concert</strong> — tell us the setting, roughly how many people, and
            a rough time of year. We will take it from there.</li>
        <li><strong>Hosting a course</strong> — a room, a day of the week, and a contact person is
            all we need to begin.</li>
        <li><strong>Funding and partnership</strong> — ask for the proposal and budget; we will
            send the current version with the activity record attached.</li>
        <li><strong>Press and media</strong> — biographies, photographs and programme details are
            available on request.</li>
      </ul>
      <div class="btn-row">
        <a class="btn btn-gold" href="mailto:sby05034@gmail.com?subject=Enquiry%20—%20Classical%20Music%20for%20Everyone">Email us</a>
        <a class="btn btn-outline" href="get-involved.html">Ways to take part</a>
      </div>
    </div>
  </div>
</section>

<section class="band-cream">
  <div class="wrap narrow center">
    <p class="eyebrow">Organisation</p>
    <h2>Classical Music for Everyone</h2>
    <p class="lead mt-m">A community music social enterprise founded in Dublin in January 2024,
       currently formalising as a not-for-profit company limited by guarantee. Volunteer-led.
       Sector: community music, social enterprise, arts and health.</p>
  </div>
</section>"""
