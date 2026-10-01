# Photographs

Every image on the site sits inside a `.photo` wrapper with a fixed aspect ratio and
one shared warm overlay, so shots taken in very different rooms still read as one set.
That means **you can swap any photograph for a better one without touching the layout**:
only the file and the `alt` text change.

## Adding or replacing a photograph

```bash
_build/add-photo.sh ~/Pictures/IMG_1234.JPG images/outreach-wicklow.jpg
```

That turns a portrait the phone stored on its side, removes the camera metadata (EXIF,
XMP, IPTC: **the GPS position**, the camera, the time), resizes to 1400px on the long edge at
quality 68, writes an 800px copy beside it (`outreach-wicklow-800.jpg`, the file cards and
phones load), and prints the tuple to paste. Keep each file under about 500 KB.

**Never copy a phone photograph into `images/` by hand.** Phone pictures carry the GPS
position where they were taken; on 2026-10-01 several published files still did, some of them
taken in private houses. To clean a file already in the
folder: `python3 _build/strip-meta.py images/<name>.jpg`.

Then reference it from `_build/content_en.py` and `_build/content_ko.py` as an img tuple,
`("outreach-wicklow.jpg", 1400, 933, "An outreach concert in a Co. Wicklow nursing home")`.
The markup (`.photo` wrapper, `srcset` with the 800px copy, `sizes`) comes from
`_build/parts.py`; `loading`, `decoding` and `fetchpriority` are added at build time. Do not
write any of them by hand.

## Aspect ratio classes

| Class | Ratio | Where it suits |
|---|---|---|
| `.photo-3x2` | 3:2 | The default. Hero, card tops, most figures. |
| `.photo-4x3` | 4:3 | Figures beside a column of text. |
| `.photo-1x1` | 1:1 | Square crops. |
| `.photo-4x5` | 4:5 | Portrait: a person, an instrument, a tall room. |

For a full-bleed band, put the `<img>` directly inside `<section class="band-photo">`
with `alt=""` (it is decorative; the heading carries the meaning) and let the
gradient do the work.

## Current set (2026-10-01)

| File | Used on | Shows |
|---|---|---|
| `hero-outreach.jpg` | Home hero · News gallery | The Letters Ensemble and their conductor, St Patrick's Day concert |
| `lecture-recital.jpg` | Programme 01 (home card, Programmes block) | A lecture-recital in progress |
| `care-christmas.jpg` | Programme 02 · Get involved `#invite` · News gallery | A clarinettist and three string players in a care setting at Christmas (20 Dec 2025) |
| `recorders.jpg` | Programme 03 · Home "Now running" · News gallery | Six recorders of different sizes in a row, Nov 2025. Cropped on 2026-10-01 from the original (`무제 폴더/IMG_8160.JPG`, 1343×1400) to the instruments alone: the full frame showed a private room, with a laptop, a backpack and bags |
| `letters-ensemble.jpg` | Programme 04 · News gallery | The Letters Ensemble with their instruments |
| `dalgan-hall.jpg` | Programme 05 (Concert Guide & Companion) · News gallery | The hall at Dalgan Park set for a concert, 16 Mar 2024; no people |
| `tuh-atrium.jpg` | Home full-bleed band | Clarinet, haegeum and keyboard in the **chapel** at Tallaght University Hospital, 20 Aug 2026 (the hospital set had an atrium half and a chapel half; the file name is older than that check) · photo: Tallaght University Hospital |
| `columban-ensemble.jpg` | About page head · News gallery | Four string players of the Letters Ensemble and their conductor, Missionary Sisters of St Columban, 23 Nov 2024 |
| `founder-speaking.jpg` | About `#founder` | The founder speaking at a lecture-recital (portrait, 4:5) |
| `tuh-trio.jpg` | Programmes page head · News gallery | Soprano, piano and clarinet in the TUH atrium · photo: Tallaght University Hospital |
| `ruared-trio.jpg` | Programmes `#cmfe-artists` · News gallery | The trio taking a bow at Rua Red · photo: Ben Ryan / SDCC |
| `church-aisle.jpg` | Get involved page head · News gallery | A clarinet held up before the altar, Dysart parish church, Good Friday 2025; no people. Portrait (1050×1400); the page head shows a 2:1 band of it |
| `quartet-hall.jpg` | News page head | A string quartet and its conductor in a hall decorated for St Patrick's Day |
| `score-stand.jpg` | News gallery | A string trio rehearsing behind a part on a stand, Dec 2025 (caption names no venue). Portrait (1050×1400) |
| `two-clarinets.jpg` | News gallery | Two clarinets on a piano lid. Portrait (1050×1400) |
| `tuh-haegeum.jpg` | News gallery | A haegeum player in the TUH atrium · photo: Tallaght University Hospital |

**Retired on 2026-10-01 and moved out of this folder** to `_retired/images/`, which is neither
published nor committed (`.gitignore`): a file in `images/` can be opened by anyone who guesses
its address, used or not. `conducting.jpg` was the recorder course's
photograph, but it shows a string group at a Christmas concert in a care setting, not a class;
`recorders.jpg` replaced it. `ruared-stage.jpg` is not used because the dark audience includes
what may be a child seen from behind. `founder-portrait.jpg`, `founder-hall.jpg`,
`founder-sea.jpg`, `ruared-andrew.jpg`, `ruared-pianist.jpg`, `ruared-soprano.jpg`,
`tuh-andrew.jpg`, `clarinet.jpg`, `organ.jpg`, `community-room.jpg`, `church-concert.jpg` and
`fingering-chart.jpg` belonged to pages that no longer exist.

**Consent and permission are on record** (confirmed 1 October 2026): web consent from the
performers shown, including the Letters Ensemble and the South Dublin Live performers, and
permission to use the photographs by Ben Ryan Photography for South Dublin County Council and by
Tallaght University Hospital. A new photograph of anyone else still needs written consent first.
The site's own line is: "We show performers, instruments and empty rooms. Anyone else who can be
recognised appears only with their written consent."

The nine files added on 2026-09-13 (`columban-ensemble` `founder-hall` `founder-sea` `two-clarinets`
`recorders` `fingering-chart` `score-stand` `dalgan-hall` `church-aisle`) came from
`영상, 사진 아카이브/무제 폴더`. They were chosen from about 260 candidates by one rule: performers,
instruments and empty rooms only. Every frame with an identifiable participant or audience face was
left out, however good the picture. Where a caption names an event, the photograph's capture date
matches a row in `_build/ledger.py`; where it does not match a row, the caption names no event.

**Some components set the shape themselves**: the home programme cards (4:5), the interior page
heads (2:1, 4:3 on a phone), the full-bleed band and the gallery (3:2). There the `.photo` wrapper
carries no ratio class; everywhere else it does.

The South Dublin Live photographs come from two sources and both are credited where a caption
exists: Rua Red by **Ben Ryan Photography for South Dublin County Council** (folder
`연주 Proposal/SDCC/benryanphotography_…`), and the hospital set supplied by **Tallaght University
Hospital** (`wetransfer_photos-from-tuh-events-20-08-2026_…`). Only performers appear in the
shots used; the group photographs with hospital staff were left out.

A programme is identified by one photograph everywhere it appears: its home card, its block on
the Programmes page and, for the outreach and recorder programmes, the sections that point to
them. Moving from a home card to its block, the photograph travels across the page change. To
replace a programme's photograph, change the `img` entry in `PROGRAMMES_DATA` in both content
files.

The five home cards and the five programme blocks use **one photograph each, in the
same order**. That pairing is what makes the five programmes read as equals. Do not
give one of them two photographs or a larger crop.

## Paths

Write `src="images/…"` in **both** content files, English and Korean. Korean pages sit
in `ko/` and need `../images/`, but that prefix is added at build time by `_images()`
in `_build/layout.py`. Writing `../images/` by hand in `content_ko.py` is how a broken
hero once shipped on the Korean home page.

## Two rules that are not negotiable

1. **Consent.** Use photographs in which participants' or audience members' faces are
   identifiable only where consent is on record. If you are not sure, do not use it:
   there are plenty of shots of the performers.
2. **Captions must be true.** Do not name an event, venue or date in a caption unless
   it is confirmed. A vaguer caption is better than a wrong one. Write `alt` text from the
   photograph itself, not from its file name: count the players and name the instruments
   you can see (in 2026-10 two descriptions had to be corrected for exactly that).

Source archive: iCloud → `프로젝트 전체 파일, 후원, 펀딩/영상, 사진 아카이브/대표사진/`.
