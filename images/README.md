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

## Current set (2026-10-01, evening)

Since the evening of 1 October 2026 the site leans on drawn things more than on photographs
(Andrew: too many photographs, several unrelated to the text beside them). The five programmes are
shown by typographic **covers** (`parts.cover`), not photographs; each programme's own page shows its
one photograph under "In the room". Outside the News contact sheet there are now four photographs.

| File | Used on | Shows |
|---|---|---|
| `hero-outreach.jpg` | Home hero · News gallery | The Letters Ensemble and their conductor, St Patrick's Day concert (one non-performer at the back right, seen from behind and not recognisable; kept) |
| `recorders.jpg` | Home "Now running" · News gallery · the still behind the video on the Community Recorder Ensemble Class page | Six recorders of different sizes in a row, Nov 2025 (cropped to the instruments; see below) |
| `columban-ensemble.jpg` | About page head (3:2 over the text columns) · News gallery | Four string players of the Letters Ensemble and their conductor, Missionary Sisters of St Columban, 23 Nov 2024 |
| `founder-playing.jpg` | About `#founder` | The founder playing the clarinet in the chapel of Tallaght University Hospital, 20 Aug 2026 (from the TUH set; added 1 Oct 2026 through `add-photo.sh`, metadata stripped) · photo: Tallaght University Hospital |
| `lecture-recital.jpg` | Getting to Know Classical Music page | A lecture-recital in progress |
| `care-christmas.jpg` | Outreach Concerts page · News gallery | A clarinettist and three string players in a care setting at Christmas (20 Dec 2025) |
| `letters-ensemble.jpg` | Letters Ensemble page · News gallery | The Letters Ensemble with their instruments |
| `dalgan-hall.jpg` | News gallery | The hall at Dalgan Park set for a concert, 16 Mar 2024; no people |
| `proms-hall.jpg` | Concert Guide & Companion page ("In the room") and its share card | A full Royal Albert Hall during a BBC Prom, from high in the audience. A frame of the founder's own phone video (it sits in the BBC Proms lecture deck), cropped to the hall, stage and distant crowd so that no one close by is in it; added 1 Oct 2026 through `add-photo.sh`, metadata stripped. The year is not known, so the caption gives none. It is the founder's own view, not a group outing, and the caption says so |
| `tuh-trio.jpg` | News gallery · Programmes share card | Soprano, piano and clarinet in the TUH atrium. **Cropped on 1 Oct 2026 (1236×787)** to take out the back of an audience member's head at the bottom right · photo: Tallaght University Hospital |
| `tuh-atrium.jpg` | News gallery | Clarinet, haegeum and keyboard in the **chapel** at Tallaght University Hospital, 20 Aug 2026 · photo: Tallaght University Hospital |
| `tuh-haegeum.jpg` | News gallery | A haegeum player in the TUH atrium · photo: Tallaght University Hospital |
| `ruared-trio.jpg` | News gallery · News share card | The trio taking a bow at Rua Red · photo: Ben Ryan / SDCC |
| `church-aisle.jpg` | News gallery | A clarinet held up before the altar, Dysart parish church, Good Friday 2025; no people |
| `score-stand.jpg` | News gallery | A string trio rehearsing behind a part on a stand, Dec 2025 |
| `two-clarinets.jpg` | News gallery | Two clarinets on a piano lid (caption: "Instruments · two clarinets") |

The News gallery shows every frame at its own shape (portrait stays portrait), newest first.

**Retired on 1 October 2026 (evening)** to `_retired/images/`: `founder-speaking.jpg` (the projected
slide behind the founder shows other recognisable people) and `quartet-hall.jpg` (no longer used).

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

**Some components set the shape themselves**: the interior page heads (3:2, over the text columns)
and the News gallery (each photograph at its own shape). "In the room" on a programme page uses 4:5
for a portrait and 3:2 for a landscape. There the `.photo` wrapper carries no ratio class, or the one
the component chooses; everywhere else it does.

The South Dublin Live photographs come from two sources and both are credited where a caption
exists: Rua Red by **Ben Ryan Photography for South Dublin County Council** (folder
`연주 Proposal/SDCC/benryanphotography_…`), and the hospital set supplied by **Tallaght University
Hospital** (`wetransfer_photos-from-tuh-events-20-08-2026_…`). Only performers appear in the
shots used; the group photographs with hospital staff were left out.

A programme is identified everywhere by its **cover** (number, emblem, three words; `parts.cover`),
which is the same on the home page, the Programmes index and the programme's own page, and travels
between them. Its photograph appears once, under "In the room" on its own page. To change a
programme's photograph, change the `img` entry in `PROGRAMMES_DATA` in both content files; to give a
programme a video, set `page["video"]` (see CLAUDE.md §000).

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
