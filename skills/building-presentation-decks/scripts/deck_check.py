#!/usr/bin/env python3
"""deck_check: lint a .pptx and render what the audience sees at every click.

    python3 deck_check.py deck.pptx                 # lint only
    python3 deck_check.py deck.pptx --render out/   # lint + slide PNGs + storyboard.png
    python3 deck_check.py deck.pptx --min-font 18   # projected-room threshold (default 18)

Storyboard: one row per slide, one column per click state (click 0 = what appears
before any click). Static renders (LibreOffice/PDF) only show the final state, which
hides reveal-order bugs; the storyboard removes not-yet-revealed shapes per state.
Exit code 1 if any ERROR is reported.
"""
from __future__ import annotations

import argparse
import copy
import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile

from lxml import etree
from pptx import Presentation
from pptx.util import Emu

P = "http://schemas.openxmlformats.org/presentationml/2006/main"
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"


def q(ns, tag):
    return f"{{{ns}}}{tag}"


def click_groups(slide):
    """Return (list of spid-sets revealed per click on the main sequence, autostart spids, trigger targets)."""
    sld = slide._element
    timing = sld.find(q(P, "timing"))
    if timing is None:
        return [], set(), set()
    main = None
    for ctn in timing.iter(q(P, "cTn")):
        if ctn.get("nodeType") == "mainSeq":
            main = ctn
    trig = set()
    for ctn in timing.iter(q(P, "cTn")):
        if ctn.get("nodeType") == "interactiveSeq":
            body = ctn.find(q(P, "childTnLst"))  # skip the trigger shape in stCondLst
            if body is not None:
                trig |= {int(t.get("spid")) for t in body.iter(q(P, "spTgt"))}
    groups, auto = [], set()
    if main is not None:
        lst = main.find(q(P, "childTnLst"))
        for par in (lst if lst is not None else []):
            spids = {int(t.get("spid")) for t in par.iter(q(P, "spTgt"))}
            entr = any(c.get("presetClass") == "entr" for c in par.iter(q(P, "cTn")))
            first = next((c for c in par.iter(q(P, "cTn")) if c.get("nodeType")), None)
            if not entr:
                continue
            if first is not None and first.get("nodeType") in ("afterEffect", "withEffect") and not groups:
                auto |= spids
            else:
                groups.append(spids)
    return groups, auto, trig


def lint(path, min_font):
    prs = Presentation(path)
    W, H = prs.slide_width, prs.slide_height
    issues = []

    def add(level, sno, msg):
        issues.append((level, sno, msg))

    slide_ids = {s.slide_id for s in prs.slides}
    titles_seen = {}
    for sno, slide in enumerate(prs.slides, 1):
        sld = slide._element
        spids = {sh.shape_id for sh in slide.shapes}
        all_ids = [int(e.get("id")) for e in sld.iter(q(P, "cNvPr"))]
        dup = {i for i in all_ids if all_ids.count(i) > 1}
        if dup:
            add("ERROR", sno, f"duplicate shape ids {sorted(dup)}")
        # --- timing validity
        timing = sld.find(q(P, "timing"))
        if timing is not None:
            ids = [c.get("id") for c in timing.iter(q(P, "cTn"))]
            if len(ids) != len(set(ids)):
                add("ERROR", sno, "duplicate <p:cTn id> in timing (PowerPoint will 'repair' the file)")
            nested = {int(e.get("id")) for e in sld.iter(q(P, "cNvPr"))}
            for t in timing.iter(q(P, "spTgt")):
                if int(t.get("spid")) not in nested:
                    add("ERROR", sno, f"animation targets missing shape id {t.get('spid')}")
            order = [etree.QName(c).localname for c in sld]
            if "transition" in order and order.index("transition") > order.index("timing"):
                add("ERROR", sno, "<p:transition> must come before <p:timing>")
            groups, auto, trig = click_groups(slide)
            if len(groups) > 7:
                add("WARN", sno, f"{len(groups)} clicks on one slide; split the slide or merge steps")
            if trig:
                add("WARN", sno, "trigger animations: PowerPoint-only, and the hidden feedback shows in PDF/handouts. "
                                  "Prefer link() to feedback slides")
        # --- text
        title = None
        if slide.shapes.title is not None and slide.shapes.title.has_text_frame:
            title = slide.shapes.title.text_frame.text.strip()
        small = {}
        for sh in slide.shapes:
            if sh.left is not None and sh.width is not None:
                if sh.left < 0 or sh.top < 0 or sh.left + sh.width > W + 1 or sh.top + sh.height > H + 1:
                    add("WARN", sno, f"shape {sh.name!r} extends off the slide")
            if not sh.has_text_frame:
                continue
            # footer zone (shape ends in the bottom 10% of the slide) may use small text
            in_footer = sh.top is not None and sh.top > H * 0.85 and sh.top + sh.height > H * 0.9
            for para in sh.text_frame.paragraphs:
                for r in para.runs:
                    if (r.font.size is not None and r.text.strip() and r.font.size.pt < min_font
                            and not in_footer):
                        small.setdefault(r.font.size.pt, r.text.strip()[:40])
            # rough overflow estimate per paragraph: glyph width ~0.5em, line height 1.2em
            if sh.width and sh.height and sh.text_frame.word_wrap is not False:
                need, maxpt = 0.0, 0
                for para in sh.text_frame.paragraphs:
                    sizes = [r.font.size.pt for r in para.runs if r.font.size]
                    pt = max(sizes) if sizes else 18
                    per_line = max(1, int(Emu(sh.width).pt / (pt * 0.5)))
                    need += max(1, -(-len(para.text) // per_line)) * pt * 1.2
                    maxpt = max(maxpt, pt)
                if sh.text_frame.text.strip() and need > Emu(sh.height).pt * 1.15:
                    add("WARN", sno, f"text may overflow {sh.name!r} (needs ~{need:.0f}pt of "
                                     f"{Emu(sh.height).pt:.0f}pt height); check the render")
        for pt, sample in sorted(small.items()):
            add("WARN", sno, f"{pt:g}pt text < {min_font}pt (e.g. {sample!r}); unreadable when projected")
        words = sum(len(sh.text_frame.text.split()) for sh in slide.shapes if sh.has_text_frame)
        if words > 80:
            add("WARN", sno, f"{words} words on slide; move detail to speaker notes")
        if not (slide.has_notes_slide and slide.notes_slide.notes_text_frame.text.strip()):
            add("WARN", sno, "no speaker notes")
        if title:
            titles_seen.setdefault(title, []).append(sno)
        # --- links
        for el in sld.iter(q(A, "hlinkClick")):
            action = el.get("action") or ""
            rid = el.get(q(R, "id"))
            if "hlinksldjump" in action:
                rel = slide.part.rels.get(rid) if rid else None
                if rel is None:
                    add("ERROR", sno, "slide-jump link with no target")
                else:
                    tgt = rel.target_part
                    if not any(s.part is tgt for s in prs.slides):
                        add("ERROR", sno, "slide-jump link points outside the deck")
    for t, nos in titles_seen.items():
        if len(nos) > 2:
            add("INFO", nos[0], f"title {t!r} repeated on slides {nos}")
    return prs, issues


def render(path, outdir):
    os.makedirs(outdir, exist_ok=True)
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        print("render skipped: LibreOffice (soffice) not found")
        return
    prs = Presentation(path)
    per_slide = [click_groups(s) for s in prs.slides]
    max_clicks = max((len(g) + (1 if trig else 0) for g, _, trig in per_slide), default=0)
    tmp = tempfile.mkdtemp(prefix="deckchk-")
    states = {}  # k -> list of page png paths
    for k in range(0, max_clicks + 1):
        prs_k = Presentation(path)
        for slide, (groups, auto, trig) in zip(prs_k.slides, per_slide):
            slide._element.attrib.pop("show", None)  # PDF export drops hidden slides
            hide = set()
            for i, g in enumerate(groups):
                if i >= k:
                    hide |= g
            if k <= len(groups):
                hide |= trig
            for el in list(slide._element.iter(q(P, "sp"), q(P, "pic"), q(P, "cxnSp"), q(P, "grpSp"))):
                nv = el.find(".//" + q(P, "cNvPr"))
                if nv is not None and int(nv.get("id")) in hide and el.getparent() is not None:
                    el.getparent().remove(el)
        f = os.path.join(tmp, f"state{k}.pptx")
        prs_k.save(f)
        subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir", tmp, f],
                       check=True, capture_output=True, timeout=300)
        subprocess.run(["pdftoppm", "-r", "50", "-png", os.path.join(tmp, f"state{k}.pdf"),
                        os.path.join(tmp, f"s{k}")], check=True)
        states[k] = sorted(glob.glob(os.path.join(tmp, f"s{k}-*.png")))
    # full-size final-state slides (hidden slides included)
    prs_f = Presentation(path)
    for slide in prs_f.slides:
        slide._element.attrib.pop("show", None)
    final = os.path.join(tmp, "final.pptx")
    prs_f.save(final)
    subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir", tmp, final],
                   check=True, capture_output=True, timeout=300)
    pdf = os.path.join(tmp, "final.pdf")
    subprocess.run(["pdftoppm", "-r", "80", "-png", pdf, os.path.join(outdir, "slide")], check=True)
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        print("storyboard skipped: pip install pillow")
        return
    first = Image.open(states[0][0])
    w, h = first.size
    cols = max_clicks + 1
    rows = len(per_slide)
    pad = 6
    board = Image.new("RGB", (cols * (w + pad) + 60, rows * (h + pad) + 20), "white")
    d = ImageDraw.Draw(board)
    for r, (groups, auto, trig) in enumerate(per_slide):
        n = len(groups) + (1 if trig else 0)
        d.text((5, 20 + r * (h + pad) + h // 2), f"S{r + 1}", fill="black")
        for k in range(0, n + 1):
            img = Image.open(states[k][r])
            x, y = 60 + k * (w + pad), 20 + r * (h + pad)
            board.paste(img, (x, y))
            if r == 0:
                d.text((x, 4), f"click {k}", fill="black")
    out = os.path.join(outdir, "storyboard.png")
    board.save(out)
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"rendered: {outdir}/slide-*.png, storyboard: {out} (row=slide, column=click state)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pptx")
    ap.add_argument("--render", metavar="DIR")
    ap.add_argument("--min-font", type=float, default=18)
    a = ap.parse_args()
    prs, issues = lint(a.pptx, a.min_font)
    for level, sno, msg in sorted(issues, key=lambda x: (x[1], x[0])):
        print(f"{level:5} slide {sno:>2}: {msg}")
    n_err = sum(1 for i in issues if i[0] == "ERROR")
    print(f"{len(prs.slides)} slides, {n_err} errors, {sum(1 for i in issues if i[0] == 'WARN')} warnings")
    if a.render:
        render(a.pptx, a.render)
    sys.exit(1 if n_err else 0)


if __name__ == "__main__":
    main()
