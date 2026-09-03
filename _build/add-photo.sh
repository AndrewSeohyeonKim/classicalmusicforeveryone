#!/bin/bash
# Resize and compress a photograph for the site.
#   _build/add-photo.sh <source image> <images/name.jpg> [long edge px]
# Defaults to 1400px on the long edge, quality 68 — about 200–450 KB.
set -euo pipefail

if [ $# -lt 2 ]; then
  sed -n '2,4p' "$0" | sed 's/^# \{0,1\}//'
  exit 1
fi

src="$1"; out="$2"; edge="${3:-1400}"
[ -f "$src" ] || { echo "No such file: $src" >&2; exit 1; }
mkdir -p "$(dirname "$out")"

sips -Z "$edge" "$src" --out "$out" > /dev/null
sips -s format jpeg -s formatOptions 68 "$out" --out "$out" > /dev/null

read -r w h < <(sips -g pixelWidth -g pixelHeight "$out" | awk '/pixel/{printf "%s ", $2}')
size=$(du -h "$out" | cut -f1)

echo "$out  ${w}x${h}  $size"
echo
echo "Paste into _build/content_en.py and _build/content_ko.py:"
echo
echo "  <div class=\"photo photo-3x2\">"
echo "    <img src=\"${out}\" width=\"${w}\" height=\"${h}\""
echo "         alt=\"\">"
echo "  </div>"
echo
echo "Fill in the alt text, then run: python3 _build/build.py"
