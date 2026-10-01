#!/usr/bin/env python3
"""Remove camera metadata from JPEGs before they are published.

    python3 _build/strip-meta.py images/*.jpg

Phone photographs carry EXIF and XMP: the camera, the time, and often the GPS
position where the picture was taken. On a public site that can point to a
private address. This drops the APP1 (EXIF, XMP) and APP13 (IPTC) segments
without re-encoding the picture, and keeps the colour profile (APP2).

A phone often stores a portrait photograph on its side, with an EXIF flag
that tells the viewer to turn it. Once the EXIF is gone that flag is gone
too, so the picture is first turned for real with sips (re-encoded at
quality 72), and then stripped. Prints one line per file.
"""

import struct
import subprocess
import sys

ROTATE = {3: 180, 6: 90, 8: 270}   # EXIF orientation -> degrees clockwise


def segments(data):
    """Yield (marker, start, end) for each header segment up to the scan."""
    if data[:2] != b"\xff\xd8":
        raise ValueError("not a JPEG")
    i = 2
    while i < len(data):
        if data[i] != 0xFF:
            raise ValueError("bad marker at %d" % i)
        marker = data[i + 1]
        if marker == 0xDA:                      # start of scan: image data follows
            yield marker, i, len(data)
            return
        length = struct.unpack(">H", data[i + 2:i + 4])[0]
        yield marker, i, i + 2 + length
        i += 2 + length


def orientation(data):
    for marker, s, e in segments(data):
        if marker == 0xE1 and data[s + 4:s + 10] == b"Exif\x00\x00":
            t = s + 10                              # TIFF header
            end = "<" if data[t:t + 2] == b"II" else ">"
            ifd = t + struct.unpack(end + "I", data[t + 4:t + 8])[0]
            for k in range(struct.unpack(end + "H", data[ifd:ifd + 2])[0]):
                entry = ifd + 2 + 12 * k
                tag, _typ, _cnt = struct.unpack(end + "HHI", data[entry:entry + 8])
                if tag == 0x0112:
                    return struct.unpack(end + "H", data[entry + 8:entry + 10])[0]
    return 1


def strip(data):
    out = bytearray(b"\xff\xd8")
    dropped = []
    for marker, s, e in segments(data):
        if marker in (0xE1, 0xED):              # APP1 EXIF/XMP, APP13 IPTC
            dropped.append("APP%d" % (marker - 0xE0))
            continue
        out += data[s:e]
    return bytes(out), dropped


def main(paths):
    for p in paths:
        data = open(p, "rb").read()
        o = orientation(data)
        if o in ROTATE:
            subprocess.run(["sips", "-r", str(ROTATE[o]), "-s", "formatOptions", "72", p, "--out", p],
                           check=True, stdout=subprocess.DEVNULL)
            data = open(p, "rb").read()
        clean, dropped = strip(data)
        if dropped:
            open(p, "wb").write(clean)
        turned = f", turned {ROTATE[o]}°" if o in ROTATE else ""
        print(f"{p}: removed {', '.join(dropped) or 'nothing'}{turned}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__.strip().splitlines()[2].strip())
        sys.exit(1)
    main(sys.argv[1:])
