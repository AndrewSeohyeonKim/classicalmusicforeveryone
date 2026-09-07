# Classical Music for Everyone — website

The public site for Classical Music for Everyone (CMFE), a community music social
enterprise based in Dublin. Static HTML, hosted on GitHub Pages. No build step is
needed to view or edit it — open any `.html` file in a browser.

## What is where

| Path | What it is |
|---|---|
| `index.html` and the ten pages beside it | The English site: home, about, programmes, get involved, what's on, impact, the record (archive), support, partner, the mark (identity), contact |
| `programmes/` | One detail page per programme — five more English pages |
| `ko/` | The Korean site — the same sixteen pages, same structure |
| `styles.css` | The one stylesheet both languages share |
| `assets/` | The five official logo variants, copied from `10_CMFE_로고·브랜드셋업/` |
| `images/` | Photographs used on the site |
| `404.html`, `sitemap.xml`, `robots.txt`, `llms.txt`, `site.webmanifest` | Generated — do not edit by hand |
| `images/README.md` | Which photograph is used where, and how to add one |
| `_build/` | The page generator and the diagrams. Not published (GitHub Pages skips `_`-prefixed folders) |
| `02_CMFE_사이트_셋팅지침.md` | The original brief for the site |

## Editing

**A small text change** — edit the `.html` file directly and commit. Remember that
each page carries its own copy of the header and footer, so a change to the
navigation has to be made in all twenty-four files (or made once in `_build/` and
rebuilt, which is easier).

**A change to structure, navigation, or anything repeated** — edit the files in
`_build/` and regenerate:

```bash
python3 _build/build.py
```

That rewrites all thirty-two pages plus `404.html`, `sitemap.xml`, `robots.txt`,
`llms.txt` and `site.webmanifest`. It never touches `styles.css`, `assets/` or `images/`.

- `_build/layout.py` — the shell: `<head>`, header, navigation, footer, site URL
- `_build/content_en.py` — English page content
- `_build/content_ko.py` — Korean page content
- `_build/diagrams.py` — the fourteen inline-SVG diagrams, with labels in both languages
- `_build/ledger.py` — the activity ledger, 2023 to date: the one list behind the Archive tables, the chronicle diagram and the counts on the Impact page
- `_build/archive.py` — renders the year-by-year tables from the ledger
- `_build/programmes_sub.py` — the shared skeleton for the five programme detail pages
- `_build/prog_en.py`, `_build/prog_ko.py` — the prose for those five, one file per language
- `_build/notfound.py` — the 404 page
- `_build/build.py` — page titles, meta descriptions, the 404 and the sitemap
- `_build/add-photo.sh` — resize and compress a photograph for `images/`

## How it is built

**Stylesheet, three layers** — after LINE's `abc-def` (`packages/styles`): primitives (the
canonical brand hexes, defined once), semantic roles (`--surface`, `--fg`, `--accent`,
`--line`) that components actually read, then component tokens and selectors. To restyle,
change a semantic token, not a component.

**Motion, no JavaScript** — the duration and easing scales come from the SEED design system
(`packages/rootage/duration.yaml`, `timing-function.yaml`). Reveals run on CSS
`animation-timeline: view()`, the reading-progress bar on `scroll()`, and page-to-page
transitions on the native cross-document View Transitions API. All of it is wrapped in
`@supports` and `prefers-reduced-motion`, so an older browser simply shows a static page.
There is one line of JavaScript on the site: the mobile menu toggle.

**Diagrams instead of paragraphs** — fourteen hand-authored inline SVGs carry the explanations
that would otherwise be long prose: the Learning/Sharing loop, the theory of change, the
term-long participant journey, the cross-subsidy, one figure per programme, the four ways in,
the chronicle of every activity since 2023, lecture attendance session by session, the road
ahead, and the three ways to partner. All are drawn from the same four marks — stave,
note-head, bracket, crescendo — and inherit `currentColor`, so the same figure works on the
cream, white and navy bands. The key to reading them is on the Identity page.

**Numbers with dates** — every figure on the Impact and Partner pages carries the period it
covers and traces to a row in `_build/ledger.py`. The tiles count up as they scroll into view,
in CSS alone (a registered custom property and a counter); the real number is in the markup.

**Photographs, one treatment** — every image sits in `.photo` with a fixed aspect ratio and
a shared warm-cast overlay, so shots from many different rooms read as one set. That is what
makes photographs swappable: to use a better one, run `_build/add-photo.sh` and change the
filename and `alt` text. Nothing in the layout moves. See `images/README.md`.

**Accessibility, measured not assumed** — every body/background pair on the site clears
WCAG AA (4.5:1, or 3:1 for large text), checked in the browser rather than by eye. The one
thing to know before changing a colour: gold as *text* uses `--accent-ink` (#7F5C1C), while
`--accent` (#B8893A) is for fills, rules, arrows and the logo. Swapping them drops body text
to 2.9:1. Headings never skip a level, images all carry `alt`, and each diagram is an
`<svg role="img">` with an `aria-label` restating its caption.

**Performance** — images are `loading="lazy" decoding="async"` except the hero, which is
`fetchpriority="high"`; the attributes are added at build time, not written by hand. No
JavaScript framework, no animation library: the whole site is ~200 KB of HTML plus one
stylesheet. Swapping in
a better photograph is a one-line change: see `images/README.md` and `_build/add-photo.sh`.

**Accessibility** — every text/background pair on the site meets WCAG AA (4.5:1, or 3:1 for
large text); the check that proves it is in the repository history. Headings run in order,
images carry alt text, the mobile menu reports `aria-expanded`, and the whole site works
with `prefers-reduced-motion: reduce`.

## Previewing locally

Serve the **parent** directory, so the site sits at the same path it will have on
GitHub Pages (`/classicalmusicforeveryone/`). `404.html` uses absolute paths and only
renders correctly this way.

```bash
python3 -m http.server 4173 --directory ..
```

Then open <http://localhost:4173/classicalmusicforeveryone/>.

## House rules for this repository

- **Facts come from the canonical set** — the `00_최종본` documents in the CMFE
  iCloud folder. If a figure on the site and a figure in a canonical document
  disagree, the canonical document wins and the site is corrected. Do not restate
  a number here that cannot be traced to a row in `03 — Track Record`.
- **Brand** — Ink Navy `#1D2430`, Gold Bronze `#B8893A`, Warm Cream `#FAF5EE`,
  per `06 — Brand Standards`. EB Garamond for headings, Plus Jakarta Sans for body,
  Noto Sans KR for Korean. Do not introduce a fourth typeface, and never recolour
  the logo. The standard is published at `identity.html`.
- **No name without consent.** The one story on the site names no participant. Stories,
  quotations and identifiable photographs of participants go up only with written consent.
- **Spelling** — Irish/British throughout: organisation, programme, centre.
- **No unconfirmed numbers or dates.** Say less rather than estimate.
- Both languages stay in step: a change to an English page needs the same change
  in `ko/`.
