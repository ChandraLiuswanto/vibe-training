import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import check_deck as cd

ROOT = Path(__file__).resolve().parents[2]


def deck(*sections, notes=None):
    notes = notes if notes is not None else {}
    import json
    return (
        "<html><body>" + "".join(sections)
        + '<script type="application/json" id="notes-data">' + json.dumps(notes) + "</script></body></html>"
    )


def sec(n, title="T", body="", extra=""):
    return f'<section class="slide" data-n="{n}" {extra}><h2>{title}</h2>{body}</section>'


def test_load_slides_reads_title_pre_wf_notes():
    html = deck(
        sec("1", "A title", '<p>hello</p><div class="prompt"><pre>Say &quot;hi&quot;</pre><button>Copy</button></div>'),
        sec("2", "B title", '<span class="wf">Plan</span><div class="choices">A B C</div>'),
        notes={"1": "note one", "2": "note two"},
    )
    slides = cd.load_slides(html)
    assert [s.n for s in slides] == ["1", "2"]
    assert slides[1].title == "B title"
    assert slides[0].pres == ['Say "hi"']
    assert slides[1].wf == ["Plan"]
    assert slides[0].notes == "note one"
    assert "hello" in slides[0].visible and "Say" not in slides[0].visible
    assert "A B C" not in slides[1].visible
    assert "A title" not in slides[0].visible


def mk(n, visible="", notes="x"):
    return cd.Slide(n=n, title="t", visible=visible, pres=[], wf=[], notes=notes, words_max=None)


def test_banned_flags_allow_it_and_live_whole_word():
    errs = cd.check_banned([mk("1", "Allow it now"), mk("2", "live prices"), mk("3", "deliver alive")])
    assert len(errs) == 2
    assert cd.check_banned([mk("3", "deliver alive", notes="deliver")]) == []


def test_the_app_only_banned_on_slides_4_to_11():
    assert cd.check_banned([mk("3", "the app"), mk("12", "The App")]) == []
    assert len(cd.check_banned([mk("4", "the app"), mk("11", "x", notes="the app")])) == 2


def test_workflow_rejects_brainstorm():
    s = mk("1")
    s.wf = ["Brainstorm"]
    assert len(cd.check_workflow([s])) == 1
    s.wf = ["Interview", "Plan", "Execute", "Test / Debug", "Iterate"]
    assert cd.check_workflow([s]) == []


TESTED = [
    "Add one rule to AGENTS.md: x",
    "Let's brainstorm a NISP stock dashboard",
    "Write what we agreed to docs/spec.md",
    "Read docs/spec.md and give me a plan",
    "Save that plan to docs/plan.md and build",
]


def test_prompts_require_tested_five():
    def with_pres(pres):
        s = mk("1")
        s.pres = pres
        return [s]

    assert cd.check_prompts(with_pres(TESTED), TESTED) == []
    errs = cd.check_prompts(with_pres(TESTED[:4]), TESTED)
    assert len(errs) == 1
    assert len(cd.check_prompts(with_pres(TESTED + ["invented"]), TESTED)) == 1


def copy_of(minutes, types):
    return {str(i): {"title": "t", "type": t, "minutes": m, "notes": "", "exception": "none"}
            for i, (m, t) in enumerate(zip(minutes, types))}


def test_timing_sum_and_run_floor():
    assert cd.check_timing(copy_of([90, 90], ["run", "talk"])) == []
    assert cd.check_timing(copy_of([89, 90], ["run", "talk"]))  # sum 179
    errs = cd.check_timing(copy_of([89, 91], ["run", "talk"]))  # sum ok, run 89
    assert len(errs) == 1


def test_v2_deck_fails_known_checks():
    html = (ROOT / "decks" / "day3-s1-v2.html").read_text(encoding="utf-8")
    errs = cd.check_banned(cd.load_slides(html))
    assert any("24a" in e and "Allow it" in e for e in errs)
    assert any(e.startswith("slide 23") and "backend/" in e for e in errs)


def test_words_max_needs_copy_exception():
    slides = cd.load_slides(deck(sec("1", "T", "", 'data-words-max="70"'), notes={"1": "n"}))
    assert slides[0].words_max == 70
    bad = {"1": {"title": "T", "type": "visual", "minutes": 1, "notes": "n", "exception": "none"}}
    good = {"1": dict(bad["1"], exception="dense table")}
    assert len(cd.check_exceptions(slides, bad)) == 1
    assert cd.check_exceptions(slides, good) == []


def test_parse_copy_reads_words_line_exception_and_block_minutes():
    md = (
        "## 4. The model is stateless\ntype: run\nblock: Run 1 · 13\nvisible:\nfoo\nnotes:\nLine a\nLine b\n"
        "words: 31 · budget: 40 · exception: dense table\nstatus: n/a\n\n"
        "## 5. Next\ntype: visual\nblock: Opening · 3\nnotes:\nn5\nwords: 2 · budget: 40 · exception: none\n"
    )
    c = cd.parse_copy(md)
    assert c["4"]["minutes"] == 13 and c["4"]["type"] == "run"
    assert c["4"]["exception"] == "dense table" and c["4"]["notes"] == "Line a\nLine b"
    assert c["5"]["exception"] == "none" and c["5"]["title"] == "Next"


def test_parse_outline_and_prompts_and_real_copy():
    md = "| # | H | From |\n|---|---|---|\n| **Opening** | | |\n| 1 | Build it | v2 1 |\n| 2 | Two | x |\n"
    assert cd.parse_outline(md) == {"1": "Build it", "2": "Two"}
    assert cd.parse_prompts("a\n```text\n hi \n```\n```bash\nno\n```\n") == ["hi"]
    c = cd.parse_copy((ROOT / "docs/copy/day3-s1-v2.md").read_text(encoding="utf-8"))
    assert len(c) == 32 and c["1"]["minutes"] == 3


def test_sequence_titles_notes():
    ss = [mk("1"), mk("3")]
    assert len(cd.check_sequence(ss)) >= 1
    assert cd.check_sequence([mk("1"), mk("2")]) == []
    assert len(cd.check_titles([mk("1")], {"1": "other"})) == 1
    assert len(cd.check_notes([mk("1", notes="")])) == 1

def test_cli_positional_deck_and_slides_filter(tmp_path, capsys):
    html = deck(sec("1", "One"), sec("2", "Two", "<p>Allow it</p>"), notes={"1": "a", "2": "b"})
    p = tmp_path / "d.html"
    p.write_text(html, encoding="utf-8")
    assert cd.main([str(p), "--slides", "1-1"]) == 0
    assert cd.main([str(p), "--slides", "2-2"]) == 1
    assert cd.main([str(p)]) == 1
    out = capsys.readouterr().out
    assert "slide 2" in out
