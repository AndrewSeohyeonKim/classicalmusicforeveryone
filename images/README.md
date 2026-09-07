# Photographs

Every image on the site sits inside a `.photo` wrapper with a fixed aspect ratio and
one shared warm overlay, so shots taken in very different rooms still read as one set.
That means **you can swap any photograph for a better one without touching the layout** —
only the file and the `alt` text change.

## Adding or replacing a photograph

```bash
_build/add-photo.sh ~/Pictures/IMG_1234.JPG images/outreach-wicklow.jpg
```

That resizes to 1400px on the long edge, re-encodes at quality 68, and prints the
resulting size. Keep each file under about 500 KB.

Then reference it from `_build/content_en.py` and `_build/content_ko.py`:

```html
<div class="photo photo-3x2">
  <img src="images/outreach-wicklow.jpg" width="1400" height="933"
       alt="An outreach concert in a Co. Wicklow nursing home">
</div>
```

`loading`, `decoding` and `fetchpriority` are added automatically at build time —
do not write them by hand.

## Aspect ratio classes

| Class | Ratio | Where it suits |
|---|---|---|
| `.photo-3x2` | 3:2 | The default. Hero, card tops, most figures. |
| `.photo-4x3` | 4:3 | Figures beside a column of text. |
| `.photo-1x1` | 1:1 | Square crops. |
| `.photo-4x5` | 4:5 | Portrait — a person, an instrument, a tall room. |

For a full-bleed band, put the `<img>` directly inside `<section class="band-photo">`
with `alt=""` (it is decorative — the heading carries the meaning) and let the
gradient do the work.

## Current set

| File | Used on | Shows |
|---|---|---|
| `hero-outreach.jpg` | Home hero | Letters Ensemble, St Patrick's Day concert for a religious community |
| `church-concert.jpg` | Home photo band + Archive milestones | Ensemble in a church |
| `conducting.jpg` | Home card 1 + Programmes + `programmes/recorder-ensemble` | Conducting a small ensemble |
| `lecture-recital.jpg` | Home card 2 + Programmes + `programmes/getting-to-know` | A lecture-recital in progress |
| `quartet-hall.jpg` | Home card 3 + Programmes + `programmes/concert-companion` + News + Get involved band | Ensemble performing in a bright hall |
| `care-christmas.jpg` | Home card 4 + Programmes + `programmes/outreach-concerts` | Quartet in a care setting at Christmas |
| `letters-ensemble.jpg` | Home card 5 + Home "one story" + Impact story + Programmes + `programmes/letters-ensemble` | The Letters Ensemble with their instruments |
| `quartet-hall.jpg` (also) | Partner closing band | — |
| `community-room.jpg` | spare | Clarinet in a community room |
| `clarinet.jpg` | About | The founder playing at a parish liturgy |
| `organ.jpg` | About founder band + Founder closing band | Organ console |
| `founder-portrait.jpg` | Founder hero + About founder band | The founder playing beneath stained glass (portrait, 4:5) |
| `founder-speaking.jpg` | Founder page | The founder speaking at a lecture-recital (portrait, 4:5) |
| `ruared-stage.jpg` | Home "why we exist" band + News + Founder gallery | The trio on the Rua Red stage, 29 Aug 2026 — **Ben Ryan / SDCC**, credit in the caption |
| `ruared-trio.jpg` | News (South Dublin Live card) | The trio taking a bow at Rua Red — Ben Ryan / SDCC |
| `ruared-andrew.jpg` | About founder band + Founder gallery | The founder playing under stage light at Rua Red — Ben Ryan / SDCC |
| `ruared-pianist.jpg` | Founder (collaborating artists) | Dr Soo-Jung Ann at Rua Red — Ben Ryan / SDCC |
| `ruared-soprano.jpg` | Founder (collaborating artists) | Hyelee Jung at Rua Red — Ben Ryan / SDCC |
| `tuh-trio.jpg` | News + Founder gallery | Soprano, piano and clarinet in the TUH Atrium, 20 Aug 2026 — Tallaght University Hospital |
| `tuh-haegeum.jpg` | Support + Founder (collaborating artists) | Jaewon Kim, haegeum, TUH Atrium — Tallaght University Hospital |
| `tuh-atrium.jpg` | Partner closing band | The performers in the TUH Atrium — Tallaght University Hospital |
| `tuh-andrew.jpg` | Founder gallery | The founder playing in the TUH Atrium — Tallaght University Hospital |

The South Dublin Live photographs come from two sources and both are credited where a caption
exists: Rua Red by **Ben Ryan Photography for South Dublin County Council** (folder
`연주 Proposal/SDCC/benryanphotography_…`), and the hospital set supplied by **Tallaght University
Hospital** (`wetransfer_photos-from-tuh-events-20-08-2026_…`). Only performers appear in the
shots used; the group photographs with hospital staff were left out.

Each programme detail page uses its own photograph three times — the figure, the
closing photographic band, and the card for it in the "other four" strip at the foot of
the other pages. That is deliberate: a programme is identified by one image everywhere it
appears, so a reader recognises it before reading the name. Replacing that one file
updates all three places at once, in both languages.

The five home cards and the five programme blocks use **one photograph each, in the
same order**. That pairing is what makes the five programmes read as equals — do not
give one of them two photographs or a larger crop.

## Paths

Write `src="images/…"` in **both** content files, English and Korean. Korean pages sit
in `ko/` and need `../images/`, but that prefix is added at build time by `_images()`
in `_build/layout.py`. Writing `../images/` by hand in `content_ko.py` is how a broken
hero once shipped on the Korean home page.

## Two rules that are not negotiable

1. **Consent.** Use photographs in which participants' or audience members' faces are
   identifiable only where consent is on record. If you are not sure, do not use it —
   there are plenty of shots of the performers.
2. **Captions must be true.** Do not name an event, venue or date in a caption unless
   it is confirmed. A vaguer caption is better than a wrong one.

Source archive: iCloud → `프로젝트 전체 파일, 후원, 펀딩/영상, 사진 아카이브/대표사진/`.
