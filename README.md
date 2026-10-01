# Classical Music for Everyone: the website

The public site for Classical Music for Everyone, a not-for-profit community music initiative
in Dublin. Static HTML and one stylesheet, hosted on GitHub Pages. No build step is needed to
view the site: open any `.html` file in a browser.

## What is where

Six pages in each language (Home, About, Programmes, Get involved, News & archive and Contact)
and a page for each of the five programmes, under `programmes/`. Older addresses (founder,
identity, impact, archive, support, partner) are small redirect pages that send old links to the
right part of the six.

| Path | What it is |
|---|---|
| `index.html`, `about.html`, `programmes.html`, `get-involved.html`, `news.html`, `contact.html` | The English site |
| `programmes/` | The five programme pages: how each works, what is on now, its record, how to take part |
| `ko/` | The Korean site: the same six pages and, in `ko/programmes/`, the same five programme pages |
| other `.html` files | Redirect pages for old addresses. Generated; do not delete |
| `styles.css` | The one stylesheet both languages share |
| `assets/` | The official logo files, and two square app icons made from the clef |
| `images/` | Photographs used on the site, and `images/README.md` on how to add one |
| `404.html`, `sitemap.xml`, `robots.txt`, `llms.txt`, `site.webmanifest` | Generated; do not edit by hand |
| `_build/` | The page generator. Not published (GitHub Pages skips `_`-prefixed folders) |

## Editing

Change the files in `_build/` and regenerate:

```bash
python3 _build/build.py
```

That rewrites the twenty-two pages, the redirect pages, `404.html`, `sitemap.xml`, `robots.txt`,
`llms.txt` and `site.webmanifest`. It never touches `styles.css`, `assets/` or `images/`.

- `_build/content_en.py`, `_build/content_ko.py`: the copy, one deck per language. Both decks
  fill the same keys, so the two languages always have the same sections in the same order.
  `PROGRAMMES_DATA` holds the five programmes and is read by the home page, the Programmes page
  and the structured data.
- `_build/parts.py`: the markup of every page, written once for both languages. One function
  draws all five programme pages, so they keep the same sections in the same order.
- `_build/artifacts.py`: the drawings made from data at build time, as inline SVG: the record of
  each programme month by month, the attendance at the talks, the forty sessions on the home
  page, the map of Ireland on About, and the video slot (empty until a link is given).
  `_build/geo_ireland.py` is the outline of the island (Natural Earth, public domain), made by
  `_build/make-ireland.py`.
- `_build/layout.py`: the shell (`<head>`, header, navigation, footer, structured data) and
  site-wide settings: the site URL, the contact details, the date shown as "Updated".
- `_build/build.py`: page titles and descriptions, redirects, sitemap, `llms.txt`.
- `_build/ledger.py`: the activity record. The News chart, the home page's forty squares and
  each programme page's record are drawn from it, so they cannot disagree.
- `_build/icons.py`: the line icons. `_build/notfound.py`: the 404 page.
- `_build/add-photo.sh`: prepare a photograph for `images/`: turn it upright, remove its camera
  metadata (including any GPS position), resize it, and write the 800px copy beside it.
  `_build/strip-meta.py` does the metadata part on its own.

## How it is built

**Stylesheet, three layers.** After LINE's `abc-def`: primitives (the brand colours, defined
once), semantic roles (`--surface`, `--fg`, `--accent`, `--line`) that components read, then
components. To restyle, change a semantic token, not a component.

**Type.** EB Garamond for headings, Plus Jakarta Sans for text, Noto Sans KR for Korean. One
fluid scale in `rem`, so a reader's own text size is respected; breakpoints are in `em` for the
same reason.

**Motion, without JavaScript.** Durations and easing curves come from the SEED design system.
A page head plays once when it opens, in about a second; a photograph develops in its frame (it
fades up and settles by 3 per cent; the frame itself never moves). Elsewhere things arrive as
they come into view: where the browser supports scroll triggers, an arrival is set off once and
plays at a fixed tempo; elsewhere it is tied to a short stretch of scrolling
(`animation-timeline: view()`). Drawings draw themselves: a programme cover's emblem, the line
between steps, the squares and columns of a chart in order. A programme's cover carries over to
its own page with a cross-document View Transition. Nothing loops. Everything sits behind `@supports`
and `prefers-reduced-motion`, so a browser without support, or a reader who asks for less motion,
gets the finished page with nothing hidden. The only script on the site belongs to the mobile
menu: it opens and closes it, closes it on Escape, and shuts it again on a page brought back with
the Back button.

**Numbers.** Every figure carries the period it covers, and the real number is in the HTML.
Where the browser supports it, the figure counts up as it scrolls into view (a registered custom
property and a CSS counter); the count always finishes before the figure is fully on screen.

**Photographs, used sparingly.** The five programmes are shown by drawn covers (number,
emblem, three words of the programme's own vocabulary), not by photographs; a programme's
photograph appears once, on its own page. Photographs show in their own colour, at their own
shape in the News gallery. See `images/README.md`.

**Accessibility.** Text and background pairs meet WCAG AA; gold used as text is the darker
`--accent-ink`. Headings run in order, every image has alt text, controls are at least 44px on
touch screens, focus is a two-tone ring that shows on every background, and nothing that moves
on its own lasts longer than five seconds.

## Previewing locally

Serve the **parent** directory, so the site sits at the same path it has on GitHub Pages
(`/classicalmusicforeveryone/`). `404.html` uses absolute paths and only renders correctly
this way.

```bash
python3 -m http.server 4173 --directory ..
```

Then open <http://localhost:4173/classicalmusicforeveryone/>.

## House rules

- **Facts come from the organisation's canonical records.** If a figure on the site and the
  record disagree, the site is corrected. No unconfirmed numbers or dates: say less rather than
  estimate.
- **Public role only.** The site says what we do now, how to take part now, and what a visitor
  needs to trust us. Plans that are not yet happening and internal matters stay off it.
- **Brand:** Ink Navy `#1D2430`, Gold Bronze `#B8893A`, Warm Cream `#FAF5EE`. No fourth
  typeface, and the logo is never recoloured.
- **No name or face without consent.** Photographs show performers, instruments and empty rooms;
  anyone else who can be recognised appears only with written consent.
- **Spelling:** Irish/British throughout: organisation, programme, centre.
- Both languages stay in step.
