"""Static lint for the S1 slide deck. Standard library only.

Usage: python check_deck.py DECK [--slides A-B] [--outline MD] [--copy MD] [--prompts MD]
Runs every check whose inputs were given; exits 1 on any error.
"""
import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path

BANNED = [
    r"\bAllow it\b",
    r"the LLM in backend/\.env",
    r"starts from zero",
    r"Nothing carries over",
    r"cannot edit files",
    r"Task done",
    r"\blive\b(?! there| where)",  # 'live prices' is banned; the verb in 'live there' / 'Live where?' is fine
    r"learns the rules",
    r"\bthe app\b",
]
APP_PATTERN = r"\bthe app\b"
WF = {"Interview", "Plan", "Execute", "Test / Debug", "Iterate"}
TESTED_PREFIXES = [
    "Add one rule to AGENTS.md",
    "Let's brainstorm a NISP",
    "Write what we agreed",
    "Read docs/spec.md and give me",
    "Save that plan to docs/plan.md",
]
PROFILES = {
    "s1": {"banned": BANNED, "tested_prefixes": TESTED_PREFIXES, "app_slides": (4, 11)},
    "s2": {
        "banned": [
            r"\[CHECKPOINT URL\]",
            r"Replace my project",
            r"answers from the page, not from memory",
            r"stops the agent from filling gaps",
            r"learns the rules",
            r"\ballow them\b",
            r"must always",
            r"never tells anyone",
            r"cached copy",
            r"\bBaseline\b",
            r"\blive\b(?! there| where)",
        ],
        "tested_prefixes": [],
        "app_slides": None,
    },
}
VOID = {"br", "img", "input", "hr", "meta", "link", "area", "base", "col", "embed", "source", "track", "wbr"}


@dataclass
class Slide:
    n: str
    title: str = ""
    visible: str = ""
    pres: list = field(default_factory=list)
    wf: list = field(default_factory=list)
    notes: str = ""
    words_max: "int | None" = None


def _norm(s):
    return re.sub(r"\s+", " ", s).strip()


class _Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.slides = []
        self.cur = None
        self.stack = []  # entries: [tag, kinds, buffer-or-None]
        self.notes_raw = None
        self.in_notes = False
        self.title_parts = []
        self.vis_parts = []

    def _active(self, kind):
        return any(kind in e[1] for e in self.stack)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        classes = (a.get("class") or "").split()
        kinds = set()
        if tag == "section" and "slide" in classes:
            wm = a.get("data-words-max")
            self.cur = Slide(n=a.get("data-n", ""), words_max=int(wm) if wm else None)
            self.slides.append(self.cur)
            self.title_parts, self.vis_parts = [], []
            kinds.add("slide")
        if self.cur is not None:
            if tag in ("h1", "h2") and not self.title_parts and not self._active("title"):
                kinds.add("title")
            if tag in ("script", "style") or "choices" in classes:
                kinds.add("skip")
            if "wf" in classes:
                kinds.add("wf")
            if tag == "pre" and self._active("prompt"):
                kinds.add("pre")
            if "prompt" in classes:
                kinds.add("prompt")
        if tag == "script" and a.get("id") == "notes-data":
            self.in_notes = True
            self.notes_raw = ""
        if tag in VOID:
            return
        self.stack.append([tag, kinds, [] if kinds & {"wf", "pre", "title"} else None])

    def handle_endtag(self, tag):
        if tag == "script":
            self.in_notes = False
        for idx in range(len(self.stack) - 1, -1, -1):
            if self.stack[idx][0] != tag:
                continue
            popped = self.stack[idx:]
            del self.stack[idx:]
            for _, kinds, buf in reversed(popped):
                if self.cur is None:
                    continue
                if "wf" in kinds:
                    self.cur.wf.append(_norm("".join(buf)))
                if "pre" in kinds:
                    self.cur.pres.append("".join(buf).strip())
                if "title" in kinds:
                    self.title_parts.append("".join(buf))
                if "slide" in kinds:
                    self.cur.title = _norm("".join(self.title_parts))
                    self.cur.visible = _norm(" ".join(self.vis_parts))
                    self.cur = None
            break

    def handle_data(self, data):
        if self.in_notes:
            self.notes_raw += data
            return
        if self.cur is None:
            return
        for e in self.stack:
            if e[2] is not None:
                e[2].append(data)
        if self._active("title") or self._active("skip") or self._active("pre"):
            return
        self.vis_parts.append(data)


def load_slides(html):
    p = _Parser()
    p.feed(html)
    p.close()
    notes = json.loads(p.notes_raw) if p.notes_raw else {}
    for s in p.slides:
        s.notes = notes.get(s.n, "")
    return p.slides


def parse_outline(md):
    out = {}
    for line in md.splitlines():
        m = re.match(r"\|\s*(\d+)\s*\|\s*(.+?)\s*\|", line)
        if m:
            out[m.group(1)] = m.group(2)
    return out


_STOP = re.compile(r"^(words|status|handout|visible|diagram|build|type|block|minutes):")


def parse_copy(md):
    out = {}
    cur = None
    in_notes = False
    for line in md.splitlines():
        m = re.match(r"##\s+(\w+)\.\s+(.*\S)\s*$", line)
        if m:
            cur = out[m.group(1)] = {"title": m.group(2), "type": "", "minutes": 0, "notes": "", "exception": "none", "_nl": []}
            in_notes = False
            continue
        if cur is None:
            continue
        if in_notes and _STOP.match(line):
            in_notes = False
        if in_notes:
            cur["_nl"].append(line)
        elif line.startswith("type:"):
            cur["type"] = line[5:].strip()
        elif line.startswith("block:"):
            mm = re.search(r"·\s*(\d+)\s*$", line)
            if mm:
                cur["minutes"] = int(mm.group(1))
        elif line.startswith("minutes:"):
            mm = re.search(r"\d+", line)
            if mm:
                cur["minutes"] = int(mm.group(0))
        elif line.startswith("notes:"):
            in_notes = True
            rest = line[6:].strip()
            if rest:
                cur["_nl"].append(rest)
        elif line.startswith("words:") or line.startswith("exception:"):
            mm = re.search(r"exception:\s*(.+?)\s*$", line)
            if mm:
                cur["exception"] = mm.group(1)
    for c in out.values():
        c["notes"] = "\n".join(c.pop("_nl")).strip()
    return out


def parse_prompts(md):
    return [b.strip() for b in re.findall(r"```text\n(.*?)```", md, re.S)]


def check_sequence(slides):
    got = [s.n for s in slides]
    want = [str(i) for i in range(1, len(slides) + 1)]
    return [] if got == want else [f"data-n sequence is {got}, expected {want}"]


def check_titles(slides, outline):
    errs = []
    for s in slides:
        want = outline.get(s.n)
        if want is None:
            errs.append(f"slide {s.n}: not in outline")
        elif _norm(want) != s.title:
            errs.append(f"slide {s.n}: title {s.title!r} != outline {want!r}")
    have = {s.n for s in slides}
    for n in outline:
        if n not in have:
            errs.append(f"slide {n}: in outline but missing from deck")
    return errs


def check_notes(slides):
    return [f"slide {s.n}: notes empty" for s in slides if not s.notes.strip()]


def check_prompts(slides, prompts, profile="s1"):
    errs = []
    known = {p.strip() for p in prompts}
    used = set()
    for s in slides:
        for pre in s.pres:
            used.add(pre)
            if pre not in known:
                errs.append(f"slide {s.n}: prompt not in prompts file: {pre[:50]!r}")
    for prefix in PROFILES[profile]["tested_prefixes"]:
        text = next((p for p in prompts if p.startswith(prefix)), None)
        if text is None:
            errs.append(f"prompts file has no tested prompt starting {prefix!r}")
        elif not any(text in u for u in used):
            errs.append(f"tested prompt missing from deck: {prefix!r}")
    return errs


def check_banned(slides, profile="s1"):
    errs = []
    prof = PROFILES[profile]
    for s in slides:
        try:
            num = int(s.n)
        except ValueError:
            num = None
        for pat in prof["banned"]:
            if pat == APP_PATTERN:
                lo, hi = prof["app_slides"] or (None, None)
                if lo is None or not (num is not None and lo <= num <= hi):
                    continue
            for where, text in (("visible", s.visible), ("notes", s.notes)):
                if re.search(pat, text, re.I):
                    errs.append(f"slide {s.n}: banned /{pat}/ in {where}")
    return errs

def check_placeholders(slides):
    errs = []
    for s in slides:
        for pre in s.pres:
            # Two exemptions: spec 8.0 P-FIX (fix-template fill-ins) and 8 Run 2a (saved-prices line).
            chk = pre.replace('"Saved prices as of <date>"', "")
            for tok in ("[What I did]", "[what should happen]", "[what happened]"):
                chk = chk.replace(tok, "")
            if re.search(r"\[[A-Za-z][^\]{}]*\]|<[^>]+>", chk):
                errs.append(f"slide {s.n}: placeholder in prompt: {pre[:50]}")
    return errs

def check_workflow(slides):
    return [f"slide {s.n}: workflow name {w!r} not in {sorted(WF)}" for s in slides for w in s.wf if w not in WF]


def check_timing(copy):
    errs = []
    total = sum(c["minutes"] for c in copy.values())
    if total != 180:
        errs.append(f"timing: minutes sum to {total}, expected 180")
    run = sum(c["minutes"] for c in copy.values() if c["type"] == "run")
    if run < 90:
        errs.append(f"timing: run minutes {run} < 90")
    return errs


def check_exceptions(slides, copy):
    errs = []
    for s in slides:
        if s.words_max is None:
            continue
        exc = (copy.get(s.n) or {}).get("exception", "none").strip().lower()
        if exc in ("", "none"):
            errs.append(f"slide {s.n}: data-words-max={s.words_max} but copy has no exception")
    return errs


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("deck", nargs="?", help="deck HTML (same as --html)")
    ap.add_argument("--html")
    ap.add_argument("--slides", help="A-B: only check slides with data-n in this range")
    ap.add_argument("--outline")
    ap.add_argument("--copy")
    ap.add_argument("--prompts")
    ap.add_argument("--profile", choices=sorted(PROFILES), default="s1")
    a = ap.parse_args(argv)

    def rd(p):
        return Path(p).read_text(encoding="utf-8")

    errs = []
    html_path = a.deck or a.html
    all_slides = load_slides(rd(html_path)) if html_path else []
    rng = None
    if a.slides:
        lo, _, hi = a.slides.partition("-")
        rng = (int(lo), int(hi or lo))

    def in_rng(n):
        if rng is None:
            return True
        try:
            return rng[0] <= int(n) <= rng[1]
        except ValueError:
            return False

    slides = [s for s in all_slides if in_rng(s.n)]
    copy = parse_copy(rd(a.copy)) if a.copy else None
    if all_slides:
        errs += check_sequence(all_slides)
    if slides:
        errs += check_notes(slides) + check_banned(slides, a.profile) + check_workflow(slides)
        if a.profile == "s2":
            errs += check_placeholders(slides)
        if a.outline:
            outline = {k: v for k, v in parse_outline(rd(a.outline)).items() if in_rng(k)}
            errs += check_titles(slides, outline)
        if a.prompts:
            perrs = check_prompts(slides, parse_prompts(rd(a.prompts)), a.profile)
            if rng is not None:  # deck-wide "tested five present" only applies to a full run
                perrs = [e for e in perrs if e.startswith("slide ")]
            errs += perrs
        if copy is not None:
            errs += check_exceptions(slides, copy)
    if copy is not None:
        errs += check_timing(copy)
    for e in errs:
        print(e)
    print(f"{len(errs)} error(s)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
