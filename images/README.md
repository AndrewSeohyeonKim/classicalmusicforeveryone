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
phones load) and, for a photograph wider than 1250px, a 1200px copy (`-1200.jpg`, what a phone
at three times its pixels loads), then the same steps in AVIF at quality 60 (`.avif`,
`-800.avif`, `-1200.avif`: the same look at about 40% of the weight; v8, 2026-10-11), and
prints the tuple to paste. Keep each JPEG under about 500 KB.

**Every AVIF has even sides.** Chrome draws an AVIF that sips wrote with an odd width or height
as a transparent box (2026-10-12: 8 of 42 photographs were blank in Chrome and fine in Safari).
The script takes one pixel off an odd side; the build stops if an AVIF with an odd side is in
this folder. Do not make AVIF files any other way.

**Never copy a phone photograph into `images/` by hand.** Phone pictures carry the GPS
position where they were taken; on 2026-10-01 several published files still did, some of them
taken in private houses. To clean a file already in the
folder: `python3 _build/strip-meta.py images/<name>.jpg`.

Then reference it from `_build/content_en.py` and `_build/content_ko.py` as an img tuple,
`("outreach-wicklow.jpg", 1400, 933, "An outreach concert in a Co. Wicklow nursing home")`.
The markup (`.photo` wrapper, a `<picture>` whose AVIF source comes first, `srcset` with the
800px and 1200px copies, `sizes`) comes from
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

## Consent first (2026-10-14)

Andrew, 14 October 2026: there is **no consent on record from the Letters Ensemble players**.
Consent and permission are on record only for the South Dublin Live performers and for the
photographs by Ben Ryan (SDCC) and Tallaght University Hospital. So the set now leans on the
founder alone and on players seen from behind, and where a Letters Ensemble player's face shows,
it is **softly blurred** before the file is made (`_build/face-blur.swift`: Vision finds the faces,
a feathered ellipse blurs them, hair and instruments stay sharp; then `add-photo.sh` on the
blurred file).

**`_build/photos.py` is the consent register.** Every photograph in this folder is listed there
with the reason it may be shown (`founder`, `sdcc`, `blurred`, `nobody`, `crowd`); the build stops
on a file that is not listed, on a listed file no page uses (an unused file is still public by its
address), and on a withdrawn name. The five unblurred files published until 14 October 2026
(`hero-outreach`, `columban-ensemble`, `letters-ensemble`, `care-christmas`, `score-stand`) were
moved to `_retired/images/` and their names never come back.

## Current set (2026-10-14)

| File | Used on | Shows | Register |
|---|---|---|---|
| `ruared-duo.jpg` | Home hero (1800px) · home share card · JSON-LD image | Clarinet and piano on the Rua Red stage, Aug 2026 · photo: Ben Ryan / SDCC (Ben Ryan 04) | sdcc |
| `christmas-conducting.jpg` | About page head · About share card · News gallery | The founder in a Santa hat conducting a violinist and a violist (both blurred), Christmas concert, Clondalkin Lodge, 20 Dec 2025 (IMG_9044) | blurred |
| `goirtin-solo.jpg` | Outreach Concerts page ("In the room", 4:5) · News gallery | The founder's clarinet solo at the HSE day service in Dublin 7, 17 Apr 2025, before a screen reading "Thank you". The one listener at the left edge is cropped out (IMG_8505) | founder |
| `letters-stpatricks.jpg` | Letters Ensemble page ("In the room") · News gallery | Four string players (faces blurred) and the founder conducting, St Patrick's Day concert (IMG_5452) | blurred |
| `rehearsal-stand.jpg` | News gallery | The founder's view over the stand at a string trio rehearsal, Dec 2025; the violist and the half face at the left edge blurred, the cellist's face is behind a hand (IMG_9012) | blurred |
| `ruared-back.jpg` | News gallery · Get involved share card | The founder from behind, playing towards the soprano, Rua Red, Aug 2026 · photo: Ben Ryan / SDCC (Ben Ryan 22) | sdcc |
| `founder-playing.jpg` | About `#founder` | The founder playing the clarinet in the TUH chapel, 20 Aug 2026 · photo: Tallaght University Hospital | founder |
| `lecture-recital.jpg` | Getting to Know Classical Music page | The founder giving a talk, a BBC Proms slide behind | founder |
| `recorders.jpg` | Recorder class page (video still) · News gallery | Six recorders in a row, Nov 2025 | nobody |
| `proms-hall.jpg` | Concert Guide & Companion page | The Royal Albert Hall from high in the audience (the founder's own video frame) | crowd |
| `tuh-trio.jpg` `tuh-atrium.jpg` `tuh-haegeum.jpg` | News gallery · Programmes share card (trio) · Contact share card (chapel) | South Dublin Live at Tallaght University Hospital, Aug 2026 · photo: TUH | sdcc |
| `ruared-trio.jpg` | News gallery · News share card | The trio taking a bow at Rua Red · photo: Ben Ryan / SDCC | sdcc |
| `church-aisle.jpg` | News gallery | The founder's hand holding a clarinet before the altar, Dysart, Good Friday 2025 | founder |
| `dalgan-hall.jpg` | News gallery | The hall at Dalgan Park set for a concert, Mar 2024; no people | nobody |
| `two-clarinets.jpg` | News gallery | Two clarinets on a piano lid | nobody |

Left out on purpose when the set was chosen again (14 Oct 2026): posed group photographs of the
Letters Ensemble (four blurred faces facing the camera read as a warning, not a photograph); the
Goirtin Hub frames with the day-service users, even from behind; the Advent concert frames whose
audience, seen from behind, looks like school pupils (the `ruared-stage` rule: no children); and
the frames from a funeral (Dalgan Park, June 2025).

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

**Consent and permission on record** (corrected 14 October 2026): the South Dublin Live
performers, and permission to use the photographs by Ben Ryan Photography for South Dublin County
Council and by Tallaght University Hospital. **Not** the Letters Ensemble players: their faces are
blurred (above). A new photograph of anyone else still needs written consent first, or a blurred
face. The site's own line is: "We show performers, instruments and empty rooms. Anyone else who
can be recognised appears only with their written consent."

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

1. **Consent.** Use photographs in which anyone's face is identifiable, performers included,
   only where consent is on record (`_build/photos.py`). Without it, blur the face or do not use
   the photograph. If you are not sure, do not use it: there are plenty of shots of the founder.
2. **Captions must be true.** Do not name an event, venue or date in a caption unless
   it is confirmed. A vaguer caption is better than a wrong one. Write `alt` text from the
   photograph itself, not from its file name: count the players and name the instruments
   you can see (in 2026-10 two descriptions had to be corrected for exactly that).

Source archive: iCloud → `프로젝트 전체 파일, 후원, 펀딩/영상, 사진 아카이브/대표사진/`.
