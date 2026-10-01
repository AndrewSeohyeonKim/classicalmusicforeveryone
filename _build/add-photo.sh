#!/bin/bash
# Resize and compress a photograph for the site.
#   _build/add-photo.sh <source image> <images/name.jpg> [long edge px]
# Defaults to 1400px on the long edge, quality 68 — about 200–450 KB.
# Also writes images/name-800.jpg, the copy that cards and phones load, and
# removes the camera metadata (GPS position, camera, time) from both.
set -euo pipefail

if [ $# -lt 2 ]; then
  sed -n '2,4p' "$0" | sed 's/^# \{0,1\}//'
  exit 1
fi

src="$1"; out="$2"; edge="${3:-1400}"
[ -f "$src" ] || { echo "No such file: $src" >&2; exit 1; }
mkdir -p "$(dirname "$out")"
here="$(cd "$(dirname "$0")" && pwd)"

# turn a portrait the phone stored on its side, and drop the metadata, first:
# a resize keeps the side-on pixels and the flag that turns them
# (sips first writes any source, HEIC included, as a full-size JPEG)
sips -s format jpeg -s formatOptions 95 "$src" --out "$out" > /dev/null
python3 "$here/strip-meta.py" "$out" > /dev/null
sips -Z "$edge" -s format jpeg -s formatOptions 68 "$out" --out "$out" > /dev/null

small="${out%.jpg}-800.jpg"
sips --resampleWidth 800 -s formatOptions 70 "$out" --out "$small" > /dev/null
# sips writes its own small EXIF block on save; take it off both files
python3 "$here/strip-meta.py" "$out" "$small" > /dev/null

read -r w h < <(sips -g pixelWidth -g pixelHeight "$out" | awk '/pixel/{printf "%s ", $2} END{print ""}')
size=$(du -h "$out" | cut -f1)

echo "$out  ${w}x${h}  $size   (and $small)"
echo
echo "Add it to _build/content_en.py and _build/content_ko.py as an img tuple:"
echo
echo "  (\"$(basename "$out")\", ${w}, ${h}, \"<alt text>\")"
echo
echo "Write the alt text from the photograph itself, then run: python3 _build/build.py"
