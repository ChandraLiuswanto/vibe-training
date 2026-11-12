# Day 3 S3 — Run 3 Trainer Demo Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace Run 3 with a trainer demo backed by a tested folder at `/data/training/deck`, cut quiz slide 6, and add a "skills and tools" slide.

**Architecture:** The demo folder is standalone: SQLite `prices.db`, a `uv`-run `refresh.py`, and an opencode command that drives the agent through refresh → report → check → deck. The deck (`decks/day3-s3.html`) is edited in place, keeping its existing reveal, notes and style system. The copy doc and the outline follow the deck.

**Tech Stack:** Python 3 + `uv` inline script deps (`yfinance`, `python-pptx`), SQLite, opencode 1.19.5, single-file HTML deck, playwright-core render script.

**Spec:** `docs/superpowers/specs/2026-11-12-day3-s3-demo-workflow-design.md`

## Global Constraints

- Demo folder path: `/data/training/deck`. It is not in the git repo, so the README there doubles as the run sheet.
- Schema verbatim: `stocks(ticker, name, added_at)`, `prices(ticker, date, open, high, low, close, volume)`.
- Command file: `.opencode/commands/stock-report.md`, taking `$ARGUMENTS` as the ticker.
- Outputs: `reports/<T>-report.html`, `reports/<T>-deck.pptx`. The backup copy goes in `backup/`.
- Deck rules (AGENTS.md): full-sentence assertion titles; presented ≤40 visible words; no shrinking type to fit.
- New headlines, verbatim:
  - 15: "Watch: one saved command builds the TLKM report and deck"
  - 16: "Need a skill or tool? Ask the agent to find it, or install it yourself"
  - 18: "In one day you built and upgraded a business app, then saw it automated"
- Skill examples, verbatim: Coherence → `presentation-creator` · Humanizer → `clarity` · Design → `frontend-slides`.
- Final slide count: 22 (`data-n` 1–6, 7a, 7b, 8–11, 12a, 12b, 13–20 after renumbering).

## Review Focus

- **Re-running refresh for a ticker that's already loaded** should add no duplicate rows. Test: `test_refresh_idempotent`.
- **An unknown or mistyped ticker** (`XXXX.JK`) should make refresh exit non-zero with a clear message and leave nothing in `stocks`. Test: `test_refresh_bad_ticker`.
- **The command run with no ticker** should ask for one instead of guessing. This is written into the command text and checked manually in Task 2.
- **The network failing in class** should leave the trainer with the `backup/` outputs and the slide 15 notes that point there. Checked in Task 2 and Task 3.
- **Deck keyboard navigation** after removing a slide: the last slide must be reachable, and `#N` hashes must map to the new numbers. Checked in the Task 4 render (22 slides, 0 errors).

---

### Task 1: Demo database and refresh script

**Files:**
- Create: `/data/training/deck/refresh.py`
- Create: `/data/training/deck/test_refresh.py`
- Create: `/data/training/deck/prices.db` (generated)

**Interfaces:**
- Produces:
  - `refresh(ticker: str, db: str = "prices.db", fetch=yf_fetch) -> int`, which returns the number of rows upserted.
  - CLI `uv run refresh.py TICKER`.
  - `fetch(ticker) -> list[dict]` with keys `date, open, high, low, close, volume`. An empty list means the ticker is unknown.

- [ ] **Step 1:** Write `test_refresh.py` with a fake fetch:
  - `test_refresh_creates_schema`: both tables exist with the exact columns.
  - `test_refresh_idempotent`: two runs give the same row count.
  - `test_refresh_bad_ticker`: the fetch returns `[]`, so it raises `SystemExit` with a non-zero code and `stocks` stays empty.
- [ ] **Step 2:** Run `uv run --with pytest --with yfinance pytest -q`. Expected: FAIL, because there's no module yet.
- [ ] **Step 3:** Implement `refresh.py` with PEP 723 inline deps (`yfinance`):
  - Use `CREATE TABLE IF NOT EXISTS`.
  - Upsert on `(ticker, date)` as the primary key.
  - Fetch 1 year of daily data.
- [ ] **Step 4:** Run the tests. Expected: 3 pass.
- [ ] **Step 5:** Load real data with `uv run refresh.py NISP.JK`. Expected: about 240 rows. Leave TLKM out so the demo shows the refresh step adding it.

### Task 2: Saved workflow, end-to-end run, backup

**Files:**
- Create: `/data/training/deck/.opencode/commands/stock-report.md`
- Create: `/data/training/deck/AGENTS.md` (plain-language guidance, plus "use `uv run` for Python")
- Create: `/data/training/deck/README.md` (run sheet)
- Create: `/data/training/deck/backup/TLKM.JK-report.html`, `/data/training/deck/backup/TLKM.JK-deck.pptx`

**Interfaces:**
- Consumes: `uv run refresh.py TICKER` from Task 1.
- Produces: `/stock-report <TICKER>`, which writes `reports/<TICKER>-report.html` and `reports/<TICKER>-deck.pptx`.

- [ ] **Step 1:** Write the command. Frontmatter `description: Refresh a ticker, then build and check its report and deck`. The body has numbered steps:
  1. If `$ARGUMENTS` is empty, ask for a ticker and stop.
  2. Run `uv run refresh.py $ARGUMENTS`.
  3. Build `reports/$ARGUMENTS-report.html` from `prices.db` only, with a summary table, 1-year chart, key stats and one insight the data supports.
  4. List each number with its query and value, and fix any mismatch.
  5. Build `reports/$ARGUMENTS-deck.pptx` (about 6 slides, sentence titles, same numbers) using `uv run --with python-pptx`.
  6. Report the file paths, plus 3 numbers for the trainer to spot-check.
- [ ] **Step 2:** Run it non-interactively with `cd /data/training/deck && opencode run --command stock-report TLKM.JK`. If the flag differs on 1.19.5, use `opencode run "/stock-report TLKM.JK"`. Expected: both files exist and TLKM rows are in `prices.db`.
- [ ] **Step 3:** Verify the outputs:
  - Open the HTML in headless Chrome: 0 errors.
  - Open the `.pptx` with `python-pptx`: ≥4 slides.
  - Check 3 report numbers against `sqlite3 prices.db`.
- [ ] **Step 4:** Copy the outputs to `backup/`. Write `README.md`:
  - Setup: `uv`, opencode.
  - Reset: delete `reports/` and the TLKM rows.
  - The demo command.
  - The fallback: open `backup/`.
  - The measured run time.

### Task 3: Deck edits

**Files:**
- Modify: `decks/day3-s3.html`. Remove the slide-6 quiz section and its notes key. Rewrite Run 3's run slide as the demo slide. Insert the new skills slide after it. Reword the quiz and recap. Renumber `data-n` and the notes keys.

**Interfaces:**
- Consumes: the measured run time, file names and the `backup/` path from Task 2, for the notes.

- [ ] **Step 1:** Delete slide 6: the `<section>` and its `notes-data` entry. Renumber the later `data-n` values and notes keys down by 1 (8a→7a, 13b→12b), keeping the a/b suffixes; update any on-slide cross-references ("slide 4", "slides 10 and 14") to match.
- [ ] **Step 2:** Slide 15 demo (visual, ≤40 words):
  - The `/stock-report TLKM.JK` chip.
  - Four step boxes that light in order, reusing the `.seq2` classes from slide 4.
  - At step 2, two result thumbnails (TLKM report, TLKM deck), reusing the `.thumb` SVGs.
  - Block tag "Demo · Trainer".
  - Notes: what to type, what to point at, the run time, and the `backup/` fallback.
- [ ] **Step 3:** Slide 16 skills (visual, ≤40 words):
  - The left card, "Ask the agent", holds an example line: "Find a skill for clear writing and use it."
  - The right card, "Install it yourself", gives an example: the PowerPoint library.
  - Below, three skill chips revealed one by one, using the exact text from Global Constraints.
- [ ] **Step 4:** Reword the quiz:
  - A: "Nothing. The workflow checks every number against the database."
  - Keep B and C.
  - Recap headline per Global Constraints.
  - Session 3 line: "Session 3: wrote a report and deck, then watched them automated". Checkpoint line: `s3-pptx`.
- [ ] **Step 5:** Run `python3 tools/deck-check/check_deck.py decks/day3-s3.html`. Expected: only the pre-existing `data-n` numeric-sequence error, and no word-budget or title errors.

### Task 4: Docs sync and verification

**Files:**
- Modify: `docs/copy/day3-s3-v2.md`. Remove §6, renumber §7–§20 down by one, rewrite §14–§18 per the new headlines, and update the word-count table.
- Modify: `docs/outlines/day3-s3-v2.md`. Update the headlines list, the "Demo" block and the timing table, with the builder's call marked.
- Modify: `README.md`, if it lists the S3 slide count.

- [ ] **Step 1:** Update the outline and the copy doc. Notes must match the deck: the script check is that every notes value appears in the copy doc.
- [ ] **Step 2:** Render with `OUT=$PWD/shots3 node .scratch/s3-review/render.mjs`. Expected: `"n":22`, `errs: []`. Then run the overflow check with `node .scratch/s3-review/chk.mjs`: `over: []`.
- [ ] **Step 3:** View the screenshots of the new slides 15, 16, 17 and 18.
- [ ] **Step 4:** Commit:
  - `git add decks/day3-s3.html docs/ README.md`
  - `git commit -m "S3: Run 3 becomes trainer demo; cut slide-6 quiz; add skills slide"`
  - Push only after the user approves.
