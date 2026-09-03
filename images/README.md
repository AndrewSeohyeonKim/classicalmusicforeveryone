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
| `church-concert.jpg` | Home photo band | Ensemble in a church |
| `conducting.jpg` | Home card 1 + Programmes: Recorder Ensemble | Conducting a small ensemble |
| `lecture-recital.jpg` | Home card 2 + Programmes: Getting to Know Classical Music | A lecture-recital in progress |
| `quartet-hall.jpg` | Home card 3 + Programmes: Concert Guide + News + Get involved band | Ensemble performing in a bright hall |
| `care-christmas.jpg` | Home card 4 + Programmes: Outreach Concerts | Quartet in a care setting at Christmas |
| `letters-ensemble.jpg` | Home card 5 + Programmes: Letters Ensemble + News | The Letters Ensemble with their instruments |
| `community-room.jpg` | spare | Clarinet in a community room |
| `clarinet.jpg` | About | The founder playing at a parish liturgy |
| `organ.jpg` | About band | Organ console |

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
