"""The site's three families, served from this site (2026-10-13). A reader's browser
asks nothing of Google: the privacy notice lost its Google Fonts row, and a phone on
a slow line opens two connections fewer before the first words appear.

The files and the rules are Google Fonts' own, unchanged but for the addresses: the
same subsets (unicode-range), the same weights and the same font-display, so the
pages render exactly as they did. Korean keeps its two weights, 400 and 700.

Writes fonts/*.woff2, fonts/latin.css (EB Garamond, Plus Jakarta Sans: every page)
and fonts/korean.css (Noto Sans KR: the Korean pages and the 404). Do not edit those
two stylesheets by hand; run this again instead.

usage:  python3 _build/fetch-fonts.py              fetch the stylesheet and every file from Google
        python3 _build/fetch-fonts.py CSS DIR      write from a stylesheet and files already fetched

All three families are under the SIL Open Font License 1.1 (fonts/OFL.txt).
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "fonts")
SOURCE = ("https://fonts.googleapis.com/css2?"
          "family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500"
          "&family=Plus+Jakarta+Sans:wght@400;500;600;700"
          "&family=Noto+Sans+KR:wght@400;700&display=swap")
# Google answers each browser with what it can read: this one reads woff2 with unicode-range
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0 Safari/537.36")
SLUG = {"EB Garamond": "eb-garamond", "Plus Jakarta Sans": "plus-jakarta-sans",
        "Noto Sans KR": "noto-sans-kr"}
KOREAN = {"Noto Sans KR"}


def curl(url, dest):
    # curl, not urllib: this Mac's Python has no certificate store
    subprocess.run(["curl", "-sSf", "--retry", "4", "--retry-delay", "2", "-A", UA, "-o", dest, url],
                   check=True)


def faces(css):
    """Each @font-face as (family, style, url, name, rule), in Google's order."""
    out = []
    for m in re.finditer(r"@font-face\s*\{(.*?)\}", css, re.S):
        rule = m.group(1)
        fam = re.search(r"font-family:\s*'([^']+)'", rule).group(1)
        style = re.search(r"font-style:\s*(\w+)", rule).group(1)
        url = re.search(r"url\((https://[^)]+)\)", rule).group(1)
        # the named subsets carry a comment (/* latin */); Korean slices are numbered in the file name
        note = re.search(r"/\*\s*([^*]*?)\s*\*/$", css[:m.start()].rstrip())
        sub = note.group(1).strip("[] ") if note else re.search(r"\.(\d+)\.woff2$", url).group(1)
        name = f"{SLUG[fam]}{'-italic' if style == 'italic' else ''}-{sub}.woff2"
        out.append((fam, style, url, name, rule))
    return out


def rule_css(rule, name):
    """One rule on one line, the address made local (the file sits beside the stylesheet)."""
    body = re.sub(r"url\(https://[^)]+\)", f"url({name})", rule)
    parts = [p.strip() for p in body.split(";") if p.strip()]
    return "@font-face{" + ";".join(re.sub(r":\s+", ":", p, count=1) for p in parts) + "}"


def write(css, files):
    rows = faces(css)
    names = {}
    for fam, style, url, name, rule in rows:
        if names.setdefault(url, name) != name:
            sys.exit(f"two names for one file: {url}")
    if len(set(names.values())) != len(names):
        sys.exit("one name for two files")
    os.makedirs(OUT, exist_ok=True)
    for url, name in names.items():
        src = os.path.join(files, name)
        with open(src, "rb") as fh:
            if fh.read(4) != b"wOF2":
                sys.exit(f"not a woff2 file: {name}")
        shutil.copyfile(src, os.path.join(OUT, name))
    versions = sorted(set(re.findall(r"/s/(\w+/v\d+)/", css)))
    head = ("/* Google Fonts' rules for this site, the addresses made local (written by "
            "_build/fetch-fonts.py: run it again, do not edit). " + ", ".join(versions) +
            ". SIL Open Font License 1.1, see OFL.txt. */\n")
    for fname, keep in (("latin.css", lambda f: f not in KOREAN), ("korean.css", lambda f: f in KOREAN)):
        lines = [rule_css(rule, name) for fam, style, url, name, rule in rows if keep(fam)]
        with open(os.path.join(OUT, fname), "w", encoding="utf-8") as fh:
            fh.write(head + "\n".join(lines) + "\n")
        print(f"wrote fonts/{fname}: {len(lines)} rules")
    total = sum(os.path.getsize(os.path.join(OUT, n)) for n in names.values())
    print(f"{len(names)} font files, {total / 1048576:.2f} MB")


def main():
    if len(sys.argv) == 3:
        with open(sys.argv[1], encoding="utf-8") as fh:
            write(fh.read(), sys.argv[2])
        return
    with tempfile.TemporaryDirectory() as tmp:
        sheet = os.path.join(tmp, "google.css")
        curl(SOURCE, sheet)
        with open(sheet, encoding="utf-8") as fh:
            css = fh.read()
        for url, name in {r[2]: r[3] for r in faces(css)}.items():
            curl(url, os.path.join(tmp, name))
        write(css, tmp)


if __name__ == "__main__":
    main()
