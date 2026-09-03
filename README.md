# Classical Music for Everyone — website

The public site for Classical Music for Everyone (CMFE), a community music social
enterprise based in Dublin. Static HTML, hosted on GitHub Pages. No build step is
needed to view or edit it — open any `.html` file in a browser.

## What is where

| Path | What it is |
|---|---|
| `index.html` and the six pages beside it | The English site |
| `ko/` | The Korean site — the same seven pages |
| `styles.css` | The one stylesheet both languages share |
| `assets/` | Official logo files, copied from `10_CMFE_로고·브랜드셋업/` |
| `images/` | Photographs used on the site |
| `sitemap.xml`, `robots.txt` | Generated — do not edit by hand |
| `_build/` | The page generator and the diagrams. Not published (GitHub Pages skips `_`-prefixed folders) |
| `02_CMFE_사이트_셋팅지침.md` | The original brief for the site |

## Editing

**A small text change** — edit the `.html` file directly and commit. Remember that
each page carries its own copy of the header and footer, so a change to the
navigation has to be made in all fourteen files (or made once in `_build/` and
rebuilt, which is easier).

**A change to structure, navigation, or anything repeated** — edit the files in
`_build/` and regenerate:

```bash
python3 _build/build.py
```

That rewrites all fourteen pages plus `sitemap.xml` and `robots.txt`. It never
touches `styles.css`, `assets/` or `images/`.

- `_build/layout.py` — the shell: `<head>`, header, navigation, footer, site URL
- `_build/content_en.py` — English page content
- `_build/content_ko.py` — Korean page content
- `_build/diagrams.py` — the four inline-SVG diagrams, with labels in both languages
- `_build/build.py` — page titles, meta descriptions, and the sitemap

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

**Diagrams instead of paragraphs** — four hand-authored inline SVGs carry the explanations
that would otherwise be long prose: the Learning/Sharing loop, the theory of change, the
term-long participant journey, and the cross-subsidy. They inherit `currentColor`, so the
same figure works on the cream, white and navy bands.

**Photographs, one treatment** — every image sits in `.photo` with a fixed aspect ratio and
a shared warm-cast overlay, so shots from many different rooms read as one set.

## Previewing locally

```bash
python3 -m http.server 4173
```

Then open <http://localhost:4173>. Opening the files directly with `file://` also
works, but a local server matches how GitHub Pages will serve them.

## House rules for this repository

- **Facts come from the canonical set** — the `00_최종본` documents in the CMFE
  iCloud folder. If a figure on the site and a figure in a canonical document
  disagree, the canonical document wins and the site is corrected. Do not restate
  a number here that cannot be traced to a row in `03 — Track Record`.
- **Brand** — Ink Navy `#1D2430`, Gold Bronze `#B8893A`, Warm Cream `#FAF5EE`,
  per `06 — Brand Standards`. Fraunces for headings, Plus Jakarta Sans for body,
  Noto Sans KR for Korean. Do not introduce a fourth typeface, and never recolour
  the logo.
- **Spelling** — Irish/British throughout: organisation, programme, centre.
- **No unconfirmed numbers or dates.** Say less rather than estimate.
- Both languages stay in step: a change to an English page needs the same change
  in `ko/`.
