# -*- coding: utf-8 -*-
"""The reading budget, checked on every build (added 2026-10-02).

Andrew's verdict on the site (2 Oct 2026): too much running text, hard to
read. Rewriting the copy once fixes today's pages; this file keeps them
fixed. Every block of text on every built page is measured against the
budget of the component it sits in, and the build stops when one runs
over, the way it already stops on a missing string. Text can still grow,
but only by being turned into a pattern (facts, steps, a list, a fold) or
by someone changing a number here on purpose.

Units. English is counted in words. Korean is counted in characters
without spaces, each word in Latin script counting as 2 (so naming
"Mulhuddart Community Centre" costs 6, not 25), and text inside a
lang="en" span (the tagline) is not counted. By this unit a Korean block
runs about 2.4 times its English twin, which is how the Korean budgets
were set. A sentence ends at . ! or ? (abbreviations such as "Co." and
"St." do not end one).

The numbers come from the content-design review of 2 Oct 2026 (NALA plain
English: about 15 to 20 words a sentence on average; GOV.UK: one idea a
sentence; GDPR Art. 12: concise, clear and plain language).

The same pass also stops the build on words the site never uses: an em
dash, a cost word (Andrew, 1 Oct 2026), "charity" outside the status
sentence, "across Ireland", the bare acronym, an American spelling.

    CMFE_LINT=warn python3 _build/build.py   # report, do not stop
"""

import os
import re
import sys
from html.parser import HTMLParser

# component -> (max units in the block, max sentences, max units in one sentence)
BUDGET = {
    "en": {
        "hero-lead":    (20, 2, 14),
        "page-lead":    (20, 2, 14),
        "record-lead":  (12, 1, 12),
        "section-lead": (16, 1, 16),
        "mail-hint":    (10, 2, 8),
        "paragraph":    (45, 3, 20),
        "status-line":  (12, 2, 10),
        "step":         (16, 2, 14),
        "answer":       (22, 2, 16),
        "card-line":    (12, 1, 12),
        "news-card":    (12, 1, 12),
        "timeline":     (16, 2, 14),
        "clause":       (35, 3, 18),
        "clause-item":  (14, 2, 14),
        # a display statement may run to 14 words in one sentence: the premise
        # keeps Andrew's two verbs, miss and need, in one breath (2 Oct 2026)
        "statement":    (16, 2, 14),
        "value":        (12, 2, 12),
        "field":        (6, 1, 6),
        "pair-item":    (6, 1, 6),
        "note":         (16, 2, 14),
        "caption":      (16, 2, 14),
        "contents-row": (14, 1, 14),
        "list-item":    (24, 2, 22),
        "row":          (34, 3, 24),
        "other":        (24, 2, 18),
    },
    "ko": {
        "hero-lead":    (48, 2, 34),
        "page-lead":    (48, 2, 34),
        "record-lead":  (29, 1, 29),
        "section-lead": (38, 1, 38),
        "mail-hint":    (24, 2, 19),
        "paragraph":    (108, 3, 48),
        "status-line":  (29, 2, 24),
        "step":         (38, 2, 34),
        "answer":       (52, 2, 38),
        "card-line":    (29, 1, 29),
        "news-card":    (29, 1, 29),
        "timeline":     (38, 2, 34),
        "clause":       (84, 3, 43),
        "clause-item":  (34, 2, 34),
        "statement":    (38, 2, 32),
        "value":        (29, 2, 29),
        "field":        (14, 1, 14),
        "pair-item":    (14, 1, 14),
        "note":         (38, 2, 34),
        "caption":      (38, 2, 34),
        "contents-row": (34, 1, 34),
        "list-item":    (58, 2, 53),
        "row":          (82, 3, 58),
        "other":        (58, 2, 43),
    },
}

# A page as a whole (chief designer, 2 Oct 2026): open text in <main> stays
# under these, so pages cannot creep longer one acceptable block at a time.
PAGE_BUDGET = {"en": 500, "ko": 1200}

# measured and reported, never stops the build: rows drawn from the ledger
# (data, worded in ledger.py) and list items
WARN_ONLY = {"row", "list-item"}

# Text that must be quoted word for word wherever it appears (kit 27,
# facts.md) is measured but never stops the build.
ALLOW = (
    "is a not-for-profit community music initiative, forming a company limited by guarantee",
    "보증유한회사(CLG) 설립을 준비하고 있는 비영리 공동체 음악 단체입니다",
)

# Which component a block belongs to: the first rule whose marks (classes
# and tag names on the block and its ancestors) are all present wins.
RULES = [
    ("hero-lead",    ("hero-copy", "lead")),
    ("page-lead",    ("ph-lead",)),
    ("page-lead",    ("pp-intro", "lead")),
    ("status-line",  ("pp-now",)),
    ("record-lead",  ("band-ink", "sh-lead")),
    ("section-lead", ("sh-lead",)),
    ("mail-hint",    ("join", "lead")),
    ("mail-hint",    ("join-hint",)),
    ("field",        ("join-fields",)),
    ("statement",    ("why-premise",)),
    ("statement",    ("why-reasons",)),
    ("step",         ("steps",)),
    ("answer",       ("qa",)),
    ("pair-item",    ("pair",)),
    ("clause-item",  ("notice-list", "li", "ul")),
    ("clause-item",  ("facts-rows", "dd")),
    ("value",        ("notice-list", "dd")),
    ("clause",       ("notice-list",)),
    ("timeline",     ("timeline",)),
    ("card-line",    ("pc",)),
    ("card-line",    ("pi-main",)),
    ("value",        ("pi-facts", "dd")),
    ("news-card",    ("latest",)),
    ("contents-row", ("contents",)),
    ("row",          ("now-line",)),
    ("row",          ("others",)),
    ("row",          ("rec",)),
    ("caption",      ("figcaption",)),
    ("value",        ("dd",)),
    ("paragraph",    ("prose",)),
    ("note",         ("figs-note",)),
    ("note",         ("progs-note",)),
    ("note",         ("pi-note",)),
    ("note",         ("small",)),
    ("note",         ("callout",)),
    ("list-item",    ("li",)),
]

BLOCK = {"p", "li", "dd", "figcaption", "blockquote", "td", "summary"}
NESTED = {"p", "div", "h1", "h2", "h3", "h4", "dl", "ul", "ol", "figure", "article", "section"}
SKIP = {"script", "style", "svg", "title"}
VOID = {"br", "img", "meta", "link", "input", "hr", "source", "wbr"}

PAGES = ["index.html", "about.html", "programmes.html", "get-involved.html", "news.html", "contact.html",
         "programmes/getting-to-know.html", "programmes/outreach-concerts.html",
         "programmes/recorder-ensemble.html", "programmes/letters-ensemble.html",
         "programmes/concert-companion.html"]

# --- words the site never uses (visible text) -------------------------------
STATUS = {
    "en": ("Classical Music for Everyone is a not-for-profit community music initiative, forming a "
           "company limited by guarantee. It is not yet a registered charity."),
    "ko": ("Classical Music for Everyone은 보증유한회사(CLG) 설립을 준비하고 있는 비영리 공동체 음악 "
           "단체입니다. 아직 등록된 자선단체는 아닙니다."),
}
BANNED = {
    "en": [
        (r"—", "em dash"),
        (r"\bfree( of charge)?\b|\bno fee\b|\bno charge\b|\bnothing to pay\b|\bno tickets?\b", "cost word"),
        (r"\bcharit(y|ies|able)\b", "'charity' outside the status sentence"),
        (r"\bacross Ireland\b", "'across Ireland'"),
        (r"\bCMFE\b(?! Artists)", "the bare acronym"),
        (r"\b(organiz\w*|cent(er|ers)\b|colors?\b|favorite|traveled|catalog\b|program\b)",
         "US spelling"),
    ],
    "ko": [
        (r"—", "줄표"),
        (r"무료|참가비|회비|표값|공짜|표가 필요", "비용 낱말"),
        (r"자선\s?단체", "지위 문장 밖의 「자선단체」"),
        (r"아일랜드 전역", "「아일랜드 전역」"),
        (r"\bCMFE\b(?! Artists)", "단독 CMFE"),
    ],
}


class _Blocks(HTMLParser):
    """Collect the text of each outermost reading block inside <main>, with
    the classes and tag names of the block and its ancestors; and, for the
    banned-word check, all visible text on the page."""

    def __init__(self, lang):
        super().__init__(convert_charrefs=True)
        self.lang = lang
        self.stack, self.out, self.skip, self.main, self.cur = [], [], 0, False, None
        self.other_lang = 0     # depth inside a lang="en" span on a Korean page
        self.visible = []

    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            return
        a = dict(attrs)
        if tag == "main":
            self.main = True
        if tag in SKIP:
            self.skip += 1
        cls = (a.get("class") or "").split()
        # not measured: English inside a Korean page (the tagline), and a
        # status pill, which is a value set beside the sentence, not part of it
        foreign = (self.lang == "ko" and (a.get("lang") or "").startswith("en")) or "tag" in cls
        if self.cur and self.cur[0] in ("li", "dd") and tag in NESTED:
            self.cur = None
        self.stack.append((tag, cls, foreign))
        if foreign:
            self.other_lang += 1
        if self.cur is not None:
            self.cur[2].append(" ")
        if self.main and not self.skip and tag in BLOCK and self.cur is None:
            marks = set()
            for t, cs, _ in self.stack:
                marks.add(t)
                marks.update(cs)
            self.cur = [tag, marks, [], len(self.stack)]

    def handle_endtag(self, tag):
        if self.cur is not None:
            self.cur[2].append(" ")
        if tag == "main":
            self.main = False
        if tag in SKIP:
            self.skip = max(0, self.skip - 1)
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                depth = i + 1
                for _, _, f in self.stack[i:]:
                    if f:
                        self.other_lang -= 1
                del self.stack[i:]
                if self.cur and depth == self.cur[3]:
                    text = " ".join("".join(self.cur[2]).split())
                    if text:
                        self.out.append((self.cur[0], self.cur[1], text))
                    self.cur = None
                break

    def handle_data(self, data):
        if self.skip:
            return
        self.visible.append(data)
        if self.cur is not None and not self.other_lang:
            self.cur[2].append(data)


def _component(tag, marks):
    for name, need in RULES:
        if all(n in marks or n == tag for n in need):
            return name
    return "other"


_SPLIT = {
    "en": re.compile(r"(?<=[.!?])[”’)]?\s+(?=[“‘(A-Z0-9])"),
    "ko": re.compile(r"(?<=[.!?])\s+"),
}
# a full stop after these is not the end of a sentence
_ABBR = re.compile(r"\b(Co|St|Dr|Mr|Mrs|Ms|Fr|Sr|Rev|No|approx|e\.g|i\.e|etc|vs)\.(?=\s)")
_LATIN = re.compile(r"[A-Za-zÀ-ɏ][A-Za-z0-9À-ɏ'’.&-]*")


# zero-width characters the build inserts (a word joiner before a Korean list
# dot) are typesetting, not text
_ZW = re.compile("[\u200b-\u200d\u2060\ufeff]")


def units(s, lang):
    s = _ZW.sub("", s)
    if lang == "ko":
        latin = _LATIN.findall(s)
        rest = _LATIN.sub("", s)
        return len(re.sub(r"\s", "", rest)) + 2 * len(latin)
    return len(re.findall(r"[A-Za-z0-9À-ɏ&'’-]+", s))


# a middle dot separates the parts of a caption or a line of facts: each part
# is read on its own, so it is measured as its own run
_DOT = re.compile(r"\s\u00b7\s")


def measure(text, lang):
    """(units, sentences, units in the longest run). A run is a sentence, or a
    part of one between middle dots."""
    clean = _ABBR.sub(r"\1", text)
    sents = [s for s in _SPLIT[lang].split(clean) if s.strip()]
    runs = [r for s in sents for r in _DOT.split(s) if r.strip()]
    return units(text, lang), len(sents), max((units(r, lang) for r in runs), default=0)


def _banned(lang, text):
    """Banned words in a page's visible text, the status sentence excepted."""
    text = " ".join(text.split()).replace(" ".join(STATUS[lang].split()), "")
    found = []
    for pat, why in BANNED[lang]:
        for m in re.finditer(pat, text, flags=re.I if lang == "en" and why != "the bare acronym" else 0):
            found.append((why, text[max(0, m.start() - 40):m.end() + 40]))
    return found


def check(root, langs=("en", "ko")):
    """Return (rows, faults, warnings). rows: every block measured; faults:
    the ones that stop the build; warnings: reported only."""
    rows, faults, warns = [], [], []
    for lang in langs:
        for pg in PAGES:
            path = os.path.join(root, "" if lang == "en" else "ko", pg)
            if not os.path.exists(path):
                continue
            p = _Blocks(lang)
            with open(path, encoding="utf-8") as fh:
                p.feed(fh.read())
            for why, where in _banned(lang, "".join(p.visible)):
                faults.append((lang, pg, "words", 0, 0, 0, where, why))
            # the page's one ink band never runs into the ink footer (CLAUDE.md §00)
            with open(path, encoding="utf-8") as fh:
                html_ = fh.read()
            main = html_[html_.find("<main"):html_.find("</main>")]
            sections = re.findall(r'<section(?: class="([^"]*)")?', main)
            if sections and "band-ink" in (sections[-1] or "").split():
                faults.append((lang, pg, "layout", 0, 0, 0, "", "the ink band is the last section: it runs into the footer"))
            page_rows = []
            for tag, marks, text in p.out:
                comp = _component(tag, marks)
                n, ns, longest = measure(text, lang)
                rows.append((lang, pg, comp, n, ns, longest, text))
                # the page budget counts open text: a folded list (<details>)
                # is reference the reader opens on purpose
                if "details" not in marks:
                    page_rows.append(n)
                if any(a in text for a in ALLOW):
                    continue
                mx, ms, ml = BUDGET[lang][comp]
                why = []
                if n > mx:
                    why.append(f"{n}>{mx} {'words' if lang == 'en' else 'units'}")
                if ns > ms:
                    why.append(f"{ns}>{ms} sentences")
                if longest > ml:
                    why.append(f"sentence {longest}>{ml}")
                if why:
                    entry = (lang, pg, comp, n, ns, longest, text, ", ".join(why))
                    (warns if comp in WARN_ONLY else faults).append(entry)
            total = sum(page_rows)
            if total > PAGE_BUDGET[lang]:
                faults.append((lang, pg, "page", total, 0, 0, "",
                               f"{total}>{PAGE_BUDGET[lang]} {'words' if lang == 'en' else 'units'} on the page"))
    return rows, faults, warns


def report(root, verbose=False):
    rows, faults, warns = check(root)
    for lang in ("en", "ko"):
        sub = [r for r in rows if r[0] == lang]
        unit = "words" if lang == "en" else "units (characters; a Latin word = 2)"
        print(f"reading text, {lang}: {sum(r[3] for r in sub)} {unit} in {len(sub)} blocks")
    if warns and verbose:
        print(f"\nreading budget, notes only ({len(warns)}):")
        for lang, pg, comp, n, ns, longest, text, why in warns:
            print(f"  [{lang}] {pg} · {comp}: {why}\n      {text[:150]}")
    if faults:
        print(f"\nREADING BUDGET: {len(faults)} block(s) over budget or using a banned word")
        for lang, pg, comp, n, ns, longest, text, why in faults:
            print(f"  [{lang}] {pg} · {comp}: {why}\n      {text[:160]}")
    else:
        print("reading budget: every block within budget, no banned words")
    return faults


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    root = args[0] if args else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.exit(1 if report(root, verbose="-v" in sys.argv) else 0)
