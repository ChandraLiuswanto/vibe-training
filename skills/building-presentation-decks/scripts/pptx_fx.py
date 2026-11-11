"""pptx_fx: native PowerPoint animations, transitions and click navigation for python-pptx.

python-pptx has no animation API. This module writes the same <p:timing>/<p:transition>
XML PowerPoint itself writes, so you never hand-author timing trees.

    from pptx_fx import animate, step, transition, morph, link, hide_slide, lock_click_advance

    animate(slide, [
        step(title_box),                      # click 1
        step(box_a, arrow, after=[box_b]),    # click 2: box_a + arrow together, then box_b
        step((note, "wipe-left")),            # click 3 with a different effect
    ])
    transition(slide, "fade")
    link(button, target_slide)

Effects: "appear", "fade" (default), "wipe-left|right|up|down", "fly-bottom|top|left|right".
Use with `python3 deck_check.py deck.pptx` to lint and render click-by-click storyboards.
"""
from __future__ import annotations

import copy
from dataclasses import dataclass, field
from typing import Any, Iterable, Sequence

from lxml import etree

P = "http://schemas.openxmlformats.org/presentationml/2006/main"
MC = "http://schemas.openxmlformats.org/markup-compatibility/2006"
P14 = "http://schemas.microsoft.com/office/powerpoint/2010/main"
P159 = "http://schemas.microsoft.com/office/powerpoint/2015/09/main"
NSMAP = {"p": P}

# effect name -> (presetID, presetSubtype, kind, arg)
_EFFECTS = {
    "appear": (1, 0, "appear", None),
    "fade": (10, 0, "filter", "fade"),
    "wipe-left": (22, 8, "filter", "wipe(left)"),
    "wipe-right": (22, 2, "filter", "wipe(right)"),
    "wipe-up": (22, 4, "filter", "wipe(down)"),   # reveals bottom -> top
    "wipe-down": (22, 1, "filter", "wipe(up)"),   # reveals top -> bottom
    "fly-bottom": (2, 4, "fly", ("#ppt_x", "1+#ppt_h/2", "#ppt_x", "#ppt_y")),
    "fly-top": (2, 1, "fly", ("#ppt_x", "0-#ppt_h/2", "#ppt_x", "#ppt_y")),
    "fly-left": (2, 8, "fly", ("0-#ppt_w/2", "#ppt_y", "#ppt_x", "#ppt_y")),
    "fly-right": (2, 2, "fly", ("1+#ppt_w/2", "#ppt_y", "#ppt_x", "#ppt_y")),
}


@dataclass
class Step:
    """One click. `together` start on the click; `after` play one by one after them."""
    together: list
    after: list = field(default_factory=list)


def step(*shapes: Any, after: Sequence[Any] = ()) -> Step:
    """Build a click step. Each item is a shape or (shape, effect[, dur_ms])."""
    return Step(list(shapes), list(after))


def _norm(item: Any, default_effect: str, default_dur: int):
    if isinstance(item, tuple):
        shape, effect = item[0], item[1]
        dur = item[2] if len(item) > 2 else default_dur
    else:
        shape, effect, dur = item, default_effect, default_dur
    if effect not in _EFFECTS:
        raise ValueError(f"unknown effect {effect!r}; choose from {sorted(_EFFECTS)}")
    return shape, effect, (1 if effect == "appear" else dur)


class _Ids:
    def __init__(self):
        self.n = 0

    def __call__(self) -> str:
        self.n += 1
        return str(self.n)


def _ctn(ids, **attrs) -> str:
    a = " ".join(f'{k}="{v}"' for k, v in attrs.items())
    return f'<p:cTn id="{ids()}" {a}'.rstrip()


def _tgt(spid) -> str:
    return f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl>'


def _behaviours(ids, spid, effect, dur) -> str:
    _, _, kind, arg = _EFFECTS[effect]
    xml = (
        f'<p:set><p:cBhvr>{_ctn(ids, dur="1", fill="hold")}><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>'
        f'{_tgt(spid)}<p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr>'
        f'<p:to><p:strVal val="visible"/></p:to></p:set>'
    )
    if kind == "filter":
        xml += (f'<p:animEffect transition="in" filter="{arg}"><p:cBhvr>{_ctn(ids, dur=dur)}/>'
                f'{_tgt(spid)}</p:cBhvr></p:animEffect>')
    elif kind == "fly":
        x0, y0, x1, y1 = arg
        for attr, a, b in (("ppt_x", x0, x1), ("ppt_y", y0, y1)):
            xml += (f'<p:anim calcmode="lin" valueType="num"><p:cBhvr additive="base">'
                    f'{_ctn(ids, dur=dur, fill="hold")}/>{_tgt(spid)}<p:attrNameLst><p:attrName>{attr}</p:attrName>'
                    f'</p:attrNameLst></p:cBhvr><p:tavLst><p:tav tm="0"><p:val><p:strVal val="{a}"/></p:val></p:tav>'
                    f'<p:tav tm="100000"><p:val><p:strVal val="{b}"/></p:val></p:tav></p:tavLst></p:anim>')
    return xml


def _effect_par(ids, spid, effect, dur, node_type, grp) -> str:
    preset, sub, _, _ = _EFFECTS[effect]
    return (f'<p:par>{_ctn(ids, presetID=preset, presetClass="entr", presetSubtype=sub, fill="hold", grpId=grp, nodeType=node_type)}>'
            f'<p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>{_behaviours(ids, spid, effect, dur)}'
            f'</p:childTnLst></p:cTn></p:par>')


def _click_group(ids, st: Step, first_node: str, start_delay: str, eff: str, dur: int, seen: set) -> str:
    """One outer <p:par> = one click. Inner pars hold with-previous / after-previous runs."""
    inner, offset = [], 0
    runs = [(st.together, None)] + [([x], "afterEffect") for x in st.after]
    for i, (items, forced) in enumerate(runs):
        effs, longest = [], 0
        for j, item in enumerate(items):
            shape, e, d = _norm(item, eff, dur)
            spid = shape.shape_id
            if spid in seen:
                raise ValueError(f"shape {shape.name!r} (id {spid}) animated twice on one slide")
            seen.add(spid)
            node = forced or (first_node if j == 0 else "withEffect")
            effs.append(_effect_par(ids, spid, e, d, node, 0))
            longest = max(longest, d)
        inner.append(f'<p:par>{_ctn(ids, fill="hold")}><p:stCondLst><p:cond delay="{offset}"/></p:stCondLst>'
                     f'<p:childTnLst>{"".join(effs)}</p:childTnLst></p:cTn></p:par>')
        offset += longest
    return (f'<p:par>{_ctn(ids, fill="hold")}><p:stCondLst><p:cond delay="{start_delay}"/></p:stCondLst>'
            f'<p:childTnLst>{"".join(inner)}</p:childTnLst></p:cTn></p:par>')


def animate(slide, steps: Iterable[Step | Any], *, effect: str = "fade", dur: int = 400,
            autostart_first: bool = False, triggers: Sequence[tuple] = ()) -> None:
    """Replace the slide's animation with entrance effects, one Step per click.

    autostart_first: play step 1 when the slide appears (no click).
    triggers: (trigger_shape, target_shape[, effect]) pairs. Clicking trigger reveals target
              without advancing. PowerPoint-only; prefer link()-based quizzes for portability.
    """
    steps = [s if isinstance(s, Step) else step(s) for s in steps]
    ids, seen = _Ids(), set()
    root_id, seq_id = ids(), ids()
    groups = []
    for i, st in enumerate(steps):
        auto = autostart_first and i == 0
        groups.append(_click_group(ids, st, "afterEffect" if auto else "clickEffect",
                                   "0" if auto else "indefinite", effect, dur, seen))
    inter = []
    for trig in triggers:
        tshape, target = trig[0], trig[1]
        e = trig[2] if len(trig) > 2 else effect
        _, e, d = _norm((target, e), effect, dur)
        if target.shape_id in seen:
            raise ValueError(f"shape {target.name!r} animated twice on one slide")
        seen.add(target.shape_id)
        cond = f'<p:cond evt="onClick" delay="0">{_tgt(tshape.shape_id)}</p:cond>'
        inter.append(
            f'<p:seq concurrent="1" nextAc="seek">{_ctn(ids, restart="whenNotActive", fill="hold", evtFilter="cancelBubble", nodeType="interactiveSeq")}>'
            f'<p:stCondLst>{cond}</p:stCondLst><p:endSync evt="end" delay="0"><p:rtn val="all"/></p:endSync><p:childTnLst>'
            f'<p:par>{_ctn(ids, fill="hold")}><p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>'
            f'{_effect_par(ids, target.shape_id, e, d, "clickEffect", 0)}</p:childTnLst></p:cTn></p:par>'
            f'</p:childTnLst></p:cTn><p:nextCondLst>{cond}</p:nextCondLst></p:seq>')
    main = ""
    if groups:
        main = (f'<p:seq concurrent="1" nextAc="seek"><p:cTn id="{seq_id}" dur="indefinite" nodeType="mainSeq">'
                f'<p:childTnLst>{"".join(groups)}</p:childTnLst></p:cTn>'
                f'<p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>'
                f'<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst></p:seq>')
    # Build list: PowerPoint writes bldP for animated shapes that have a text body.
    bld = []
    spids_with_text = {sh.shape_id for sh in slide.shapes
                       if sh._element.tag == f"{{{P}}}sp"}
    for spid in sorted(seen):
        if spid in spids_with_text:
            bld.append(f'<p:bldP spid="{spid}" grpId="0" animBg="1"/>')
    xml = (f'<p:timing xmlns:p="{P}"><p:tnLst><p:par><p:cTn id="{root_id}" dur="indefinite" restart="never" nodeType="tmRoot">'
           f'<p:childTnLst>{main}{"".join(inter)}</p:childTnLst></p:cTn></p:par></p:tnLst>'
           + (f'<p:bldLst>{"".join(bld)}</p:bldLst>' if bld else "") + '</p:timing>')
    timing = etree.fromstring(xml)
    sld = slide._element
    for old in sld.findall(f"{{{P}}}timing"):
        sld.remove(old)
    _insert_after(sld, timing, ("cSld", "clrMapOvr", "transition", "AlternateContent"))


def _insert_after(sld, el, predecessors):
    """Keep CT_Slide child order: cSld, clrMapOvr, transition, timing, extLst."""
    idx = 0
    for i, child in enumerate(sld):
        if etree.QName(child).localname in predecessors:
            idx = i + 1
    sld.insert(idx, el)


def _clear_transition(sld):
    for child in list(sld):
        name = etree.QName(child).localname
        if name == "transition" or (name == "AlternateContent" and child.find(f".//{{{P}}}transition") is not None):
            sld.remove(child)


def transition(slide, kind: str = "fade", *, speed: str = "med", advance_on_click: bool = True,
               advance_after_ms: int | None = None) -> None:
    """kind: none|fade|push|wipe|cover|split. advance_on_click=False locks mouse-click advance
    (keyboard still works) - use on quiz and feedback slides so stray clicks don't skip them."""
    sld = slide._element
    _clear_transition(sld)
    body = {"none": "", "fade": "<p:fade/>", "push": '<p:push dir="u"/>', "wipe": '<p:wipe dir="r"/>',
            "cover": '<p:cover dir="l"/>', "split": '<p:split orient="vert" dir="out"/>'}[kind]
    attrs = f'spd="{speed}"' + ("" if advance_on_click else ' advClick="0"')
    if advance_after_ms is not None:
        attrs += f' advTm="{advance_after_ms}"'
    el = etree.fromstring(f'<p:transition xmlns:p="{P}" {attrs}>{body}</p:transition>')
    _insert_after(sld, el, ("cSld", "clrMapOvr"))


def morph(slide, *, advance_on_click: bool = True) -> None:
    """Morph into this slide (PowerPoint 2019/365), Fade elsewhere. Shapes are paired with the
    previous slide by type+text, or exactly by giving both the same name starting with '!!'."""
    sld = slide._element
    _clear_transition(sld)
    adv = "" if advance_on_click else ' advClick="0"'
    xml = (f'<mc:AlternateContent xmlns:mc="{MC}" xmlns:p="{P}" xmlns:p14="{P14}" xmlns:p159="{P159}">'
           f'<mc:Choice Requires="p159"><p:transition spd="slow" p14:dur="1000"{adv}><p159:morph option="byObject"/></p:transition></mc:Choice>'
           f'<mc:Fallback><p:transition spd="slow"{adv}><p:fade/></p:transition></mc:Fallback></mc:AlternateContent>')
    _insert_after(sld, etree.fromstring(xml), ("cSld", "clrMapOvr"))


def link(shape, target_slide) -> None:
    """Clicking `shape` in slideshow jumps to `target_slide` (works in PowerPoint, Keynote,
    LibreOffice, Google Slides, and exported PDF)."""
    shape.click_action.target_slide = target_slide


def hide_slide(slide, hidden: bool = True) -> None:
    """Hidden slides are skipped by normal advancing but still reachable by link()."""
    if hidden:
        slide._element.set("show", "0")
    elif "show" in slide._element.attrib:
        del slide._element.attrib["show"]


def lock_click_advance(slide) -> None:
    """Shortcut: keep current transition, but stop mouse clicks from advancing."""
    sld = slide._element
    trs = sld.findall(f".//{{{P}}}transition")
    if not trs:
        transition(slide, "none", advance_on_click=False)
    for tr in trs:
        tr.set("advClick", "0")
