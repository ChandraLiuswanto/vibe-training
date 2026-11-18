# Day 4 Decks Fixes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix review findings #1–#47 in the three Day 4 decks, add one participant sheet per session, and add one check script that all of them pass.

**Architecture:** A check script and the updated outlines come first, so every later task has a failing test to work against. Then four workers run in parallel on disjoint files: one per deck, and one for the participant sheets. The coordinator finishes with the README, the review report, the project log and fresh screenshots.

**Tech Stack:** Single-file HTML decks with inline CSS, SVG and JavaScript. Node with `playwright-core` from `tools/deck-check/node_modules`, driving Microsoft Edge at `C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe`.

**Spec:** `docs/superpowers/specs/2026-11-18-day4-decks-fixes-design.md`. The spec holds the change tables. This plan does not repeat them: a task that says "apply spec §5.2" means every row of that table.

## Global Constraints

- Repository `C:/Users/HP/OCBC/brown-bag/vibe-training`, branch `autopilot/day4-decks-fixes`.
- Short names: **S1** = `decks/session-1-external-data-visual.html` (18 slides), **S2** = `decks/session-2-access-control-visual.html` (18 slides), **S3** = `decks/session-3-vps-deployment-visual.html` (16 slides).
- No slide is added or removed.
- Never edit `decks/day3-*`, `prompts/`, `demos/` or `tools/deck-check/`.
- No prompt and no OpenCode setting is run or tested. Every prompt stays labelled untested.
- Each deck stays one self-contained HTML file with no network requests.
- Visible words per slide, counted as spec §4.1 says: at most 40; at most 60 on S1 slide 17, S2 slide 17, S3 slide 15. Over budget: move existing lower-value text into that slide's speaker notes. Never shrink type, never delete a warning.
- Shared wording, exact strings (spec §4.3):
  - ASK = `The prompt asks. Settings enforce.`
  - DATA = `What the agent reads goes to the AI provider. Made-up files only, never customer or bank data.`
  - UNTESTED = `Untested — rehearse before class.`
- Spelling "back end" / "front end" and the name "practice password": scope as spec §4.3 (slides and notes; not prompt text, `pack`, help windows, class names).
- Ask-first setting: worded as an outcome, no OpenCode configuration keys in any slide or prompt (spec §4.4).
- S1 and S2: lines 7 and 10 of each file are a shared shell. They stay byte-identical to each other and unchanged.
- S3: every slide is stored in a `<section>` and again in the `deck-data` JSON; every prompt is stored in `prompts[i].text` and again in `pack`. Both copies always change together (spec §4.2).
- Anti-goals of spec §2 apply to every task.
- Git: stage explicit paths only, one commit per task, never push, pull, fetch or rebase.

## Review Focus

- **A wrong quiz answer must not reveal the result.** On S1 slide 7, clicking a wrong option leaves the "÷" and the result tile hidden. Pinned by check 10 (Task 1).
- **The decks must still navigate after the edits.** Pressing ArrowRight from slide 1 reaches the last slide, the counter reads N / N, and the Notes control shows that slide's note. Pinned by check 14 (Task 1).
- **S3's JSON must stay valid and complete.** `deck-data` parses; `slides` has 16 items; `prompts` has 7; `card` keeps its 11 assignment fields and `notice`. Pinned by check 8 (Task 1).
- **A narrow projector.** New lines must not push content off the stage at 1280×720. Pinned by check 3 (Task 1).
- **The printed prompt handout.** S1 and S2's `#print-prompts` still holds seven prompts after the prompt edits. Pinned by check 5 (Task 1).

---

## File Structure

| File | Responsibility | Task |
|---|---|---|
| `tools/day4-deck-check.mjs` | The check script (spec §9, plus check 14) | 1 |
| `tools/session-2-visual-check.mjs` | Deleted | 1 |
| `docs/outlines/session-{1-external-data,2-access-control,3-vps-deployment}-visual.md` | New titles | 1 |
| `decks/session-1-external-data-visual.html` | S1 fixes | 2 |
| `decks/session-2-access-control-visual.html` | S2 fixes | 3 |
| `decks/session-3-vps-deployment-visual.html` | S3 fixes and restyle | 4 |
| `tools/day4-s3-sync.mjs` | Rebuilds S3's JSON slide copies from its sections | 4 |
| `handouts/session-{1,2,3}-participant-sheet.html` | Participant sheets | 5 |
| `README.md`, `docs/reviews/2026-11-17-day4-decks-review.md`, `docs/project-log.md` | Records | 6 |

Task 1 runs first. Tasks 2, 3, 4 and 5 write disjoint files and run in parallel. Task 6 runs last.

---

### Task 1: Check script and outlines

**Files:**
- Create: `tools/day4-deck-check.mjs`
- Delete: `tools/session-2-visual-check.mjs`
- Modify: the three outline files in `docs/outlines/`

**Interfaces:**
- Produces: `node tools/day4-deck-check.mjs [--only=s1|s2|s3|sheets] [--shots]`.
  - Output: one line `FAIL <check> <deck> slide <n>: <reason>` per problem (`slide 0` when the problem is not tied to a slide), then `PASS` or `FAILED: <n>`. Exit code 1 on any failure.
  - `--only` limits the run to one deck or to the sheets. Checks that compare two decks (check 11) run only when both are in scope or no `--only` is given.
  - `--shots` also saves one PNG per slide of each deck in scope to `.review/day4-fix-shots/<s1|s2|s3>/sNN.png` at 1600×900 (git-ignored). It deletes and rewrites only the folders of the decks in scope, so parallel workers do not disturb each other.
- Consumes: the outlines' numbered items as the expected titles.

- [ ] **Step 1: Update the outlines.** In each outline, replace the numbered titles named in spec §5.1 with the new titles. Add one line under the heading: `The owner approved these titles on 2026-11-18 with docs/superpowers/specs/2026-11-18-day4-decks-fixes-design.md.` In the S3 outline, replace the sentence "They are unchanged." with a sentence saying four titles changed spelling on 2026-11-18.

- [ ] **Step 2: Write the check script** with checks 1–13 exactly as spec §9 defines them, and these additions and clarifications:
  - Check 2 and the `words` comparison in check 8 count visible words with the same rule as the `collect` function in `.review/day4-render.mjs` (lines 49–64): every rendered text node of the active slide except those inside `h1`, `h2`, `.speaker-note`, `footer`, `.foot`, `script`, `style`.
  - Check 5 also requires, for S1 and S2, that `#print-prompts` holds seven prompts.
  - Check 8 reads the file as text. For each S3 slide: the section source contains `slides[i].visual` verbatim; `slides[i].title` equals `data-title`; `slides[i].notes` equals the speaker note's text; `slides[i].minutes` equals `data-minutes`; `slides[i].words` equals the check-2 count. Also: `deck-data` parses as JSON; `slides.length` is 16; `prompts.length` is 7 and every prompt has a non-empty `summary`; `card` has `notice` and the 11 fields listed in spec §7; `pack` contains every `prompts[i].text` in full and contains UNTESTED; the sum of `minutes` is 60.
  - Check 9 measures font size as `.review/day4-fontsize.mjs` does and reports the text and its size for each failure.
  - Check 10 clicks a wrong option first and requires, on S1 slide 7, that the "÷" and the result tile are still not visible; then clicks the correct option. To find them, the check uses two hooks that Task 2 must add: `data-quiz-hidden` on the "÷" element and on the result tile.
  - **Check 14 (new):** from slide 1, press ArrowRight until the last slide; the counter text is `N / N`; pressing the Notes control makes `#notes` visible with non-empty text; no page error occurred.
  - Check 13 prints each sheet to PDF with Playwright's `page.pdf({ format: 'A4' })` and counts pages.

- [ ] **Step 3: Run it against today's decks and confirm it fails for the right reasons.**

Run: `node tools/day4-deck-check.mjs`
Expected: exit code 1, with failures from checks 1 (the thirteen changed titles), 5 (no UNTESTED in S1 and S3; no S3 summaries), 6, 7, 8 (`words` and `pack`), 9, 10, 12 and 13. Expected to report **no** failure from checks 4, 11 and 14, and no check-1 failure about slide counts. A failure from 4, 11 or 14 on untouched decks means the check is wrong: fix the check.

- [ ] **Step 4: Confirm `--only` and `--shots`.**

Run: `node tools/day4-deck-check.mjs --only=s2 --shots`
Expected: only `s2` lines in the output, and 18 PNGs in `.review/day4-fix-shots/s2/`.

- [ ] **Step 5: Delete the old script and commit.**

```bash
git rm -q tools/session-2-visual-check.mjs
git add tools/day4-deck-check.mjs docs/outlines/session-1-external-data-visual.md docs/outlines/session-2-access-control-visual.md docs/outlines/session-3-vps-deployment-visual.md
git commit -m "Tools: one check script for the Day 4 decks; outlines carry the new titles"
```

---

### Tasks 2, 3, 4: shared steps for the deck workers

Each deck worker owns one deck file and follows this cycle:

- [ ] **Watch it fail.** Run `node tools/day4-deck-check.mjs --only=<deck> --shots` before editing and keep the list of failures.
- [ ] **Look before editing.** Open the PNGs in `.review/day4-fix-shots/<deck>/` for every slide the task changes.
- [ ] **Make the changes** in the order the task gives.
- [ ] **Watch it pass.** Run the same command until it prints `PASS`. Then open the PNG of every changed slide and confirm: the new line is readable, nothing overlaps, arrows do not cross labels, and the reading order is clear.
- [ ] **Commit** the owned files only.

Do not run `.review/day4-render.mjs`; it rewrites the screenshots of all three decks. Do not run a practice prompt or install anything.

### Task 2: S1 fixes

**Files:**
- Modify: `decks/session-1-external-data-visual.html`

**Interfaces:**
- Consumes: check script from Task 1; the hook name `data-quiz-hidden`.

- [ ] **Step 1:** Run the shared "watch it fail" and "look before editing" steps for `s1`.
- [ ] **Step 2: Titles.** Apply the seven S1 rows of spec §5.1 to both the `data-title` attribute and the heading.
- [ ] **Step 3: Safety wording.** Apply spec §5.2 rows #1, #2, #3, #4, #5 and #36: ASK on slides 10 and 16, DATA on slide 13, UNTESTED in `promptDialog`, the `drive-setup` prompt changes (ask-first step per spec §4.4 before the first read; "the version the facilitator chose (not a security review)"), and the slide 14 lines.
- [ ] **Step 4: Teaching fixes.** Apply spec §5.2 rows #14 (slide 7 quiz, with `data-quiz-hidden` on the "÷" element and the result tile, both hidden until the correct option is clicked), #16, #17, #29 (the six-step order given in the spec), #38.
- [ ] **Step 5: Visual fixes.** Apply spec §5.2 rows #30, #31, #32, #33, #46, #47. New styles go in a new block that starts with `/* Session 1 additions */`, placed after line 10. Lines 7 and 10 stay untouched.
- [ ] **Step 6: Facilitator checklist.** Add the S1 items of spec §8 to the "Setup help" window.
- [ ] **Step 7:** Run the shared "watch it pass" step, then commit:

```bash
git add decks/session-1-external-data-visual.html
git commit -m "Deck S1: review fixes (ask-first wording, data rule, quiz, labels)"
```

### Task 3: S2 fixes

**Files:**
- Modify: `decks/session-2-access-control-visual.html`

- [ ] **Step 1:** Run the shared "watch it fail" and "look before editing" steps for `s2`.
- [ ] **Step 2: Titles.** Apply the two S2 rows of spec §5.1.
- [ ] **Step 3: Wording.** Apply spec §5.3 rows #2, #6, #7, #12, #13, #15, #39.
- [ ] **Step 4: Quiz.** Apply spec §5.3 row #14 (slide 9).
- [ ] **Step 5: Visual fixes.** Apply spec §5.3 rows #33, #34, #35, #45. New styles go in the existing `/* Session 2 additions */` block. Lines 7 and 10 stay untouched.
- [ ] **Step 6: Facilitator checklist.** Add the S2 item of spec §8 ("Rehearse every prompt; all are untested") to the help window.
- [ ] **Step 7:** Run the shared "watch it pass" step, then commit:

```bash
git add decks/session-2-access-control-visual.html
git commit -m "Deck S2: review fixes (ask-first wording, audit and directory wording, quiz, Session 3 readiness)"
```

### Task 4: S3 fixes and restyle

**Files:**
- Modify: `decks/session-3-vps-deployment-visual.html`
- Create: `tools/day4-s3-sync.mjs`

**Interfaces:**
- Produces: `node tools/day4-s3-sync.mjs` rewrites, for each of the 16 slides, `slides[i].title`, `eyebrow`, `visual`, `notes`, `minutes`, `actions` and `words` in the `deck-data` JSON from the slide's `<section>`. `visual` is the exact source text between `<div class="visual">` and its closing tag; `words` uses the check-2 counting rule. It leaves `kind`, `prompts`, `pack` and `card` alone, keeps the JSON on one line, and prints how many fields changed. With `--check` it changes nothing and exits 1 if any field differs.

- [ ] **Step 1:** Run the shared "watch it fail" and "look before editing" steps for `s3`.
- [ ] **Step 2: Write the sync helper first.** Run `node tools/day4-s3-sync.mjs --check` on the untouched deck. Expected: it reports differences only in `words` (the stored counts used another rule) and in no other field. Any other difference means the helper reads the sections wrongly: fix the helper. From here on, edit the sections and run the helper after each step.
- [ ] **Step 3: Titles and spelling.** Apply the four S3 rows of spec §5.1, then "back end", "front end" and "practice password" within the scope of spec §4.3.
- [ ] **Step 4: Restyle (spec §6).** Opening slide in the hero layout; footer text on every slide; filled main buttons placed with their content; solid `#f30` arrows; white rounded cards; title spacing; remove all animation (four `@keyframes`, every `animation` declaration, every inline `animation-delay`).
- [ ] **Step 5: Redraw the flagged diagrams.** Apply spec §5.4 rows #8 (slide 4, including the visible quiz question and "A ·" / "B ·" options), #9 (slide 5), #21 (slide 13), #25 (slide 8), #26 (slide 3), #27 (slide 6), #28 (slide 14), #42 (slide 9), #43 (slide 8).
- [ ] **Step 6: New visible lines.** Apply spec §5.4 rows #2 (slide 8, ASK, conditional notes), #10 (slide 6), #11 (slide 2), #18 (slide 3), #19 (slide 11), #20 (slide 15).
- [ ] **Step 7: Prompts.** In `prompts` **and** in `pack`: add the ask-first step of spec §4.4 to prompt `plan`. Add a `summary` key to each of the seven prompts and show it above the prompt text in the prompt window. Show UNTESTED in every prompt window, keeping the existing "Training VPS only…" line. Add UNTESTED once to the header of `pack`.
- [ ] **Step 8: Facilitator checklist.** Add the S3 items of spec §8 to the "Facilitator setup + limitations" window.
- [ ] **Step 9:** Run `node tools/day4-s3-sync.mjs`, then the shared "watch it pass" step. Open all 16 PNGs, not only the changed slides, and compare three of them side by side with `.review/day4-shots/s1/s05.png` and `.review/day4-shots/s2/s10.png` for the look. Then commit:

```bash
git add decks/session-3-vps-deployment-visual.html tools/day4-s3-sync.mjs
git commit -m "Deck S3: review fixes and restyle to match Sessions 1 and 2"
```

### Task 5: Participant sheets

**Files:**
- Create: `handouts/session-1-participant-sheet.html`, `handouts/session-2-participant-sheet.html`, `handouts/session-3-participant-sheet.html`

**Interfaces:**
- Consumes: the prompt numbers, titles and full texts in `.review/day4-text/s1.md`, `s2.md`, `s3.md` (section "Practice prompts"). Prompt titles do not change in this plan. The "unexplained words" tables in `docs/reviews/2026-11-17-day4-decks-review.md` list the words that must be translated or avoided.

- [ ] **Step 1: Watch it fail.** Run `node tools/day4-deck-check.mjs --only=sheets`. Expected: check 13 fails because the files do not exist.
- [ ] **Step 2: Write the three sheets** as spec §7 defines them: the four-column table with seven rows, the untested notice and DATA at the top, and the session-specific blocks of the spec §7 table. Each row is written from the full prompt text, in plain words. Mark every table row for a prompt with the attribute `data-prompt-row` so the check can count them.
- [ ] **Step 3: Watch it pass.** Run `node tools/day4-deck-check.mjs --only=sheets` until it prints `PASS`.
- [ ] **Step 4: Read each sheet as a participant.** For every cell in "What you are approving", confirm it uses no word from the review's unexplained-words tables without translating it in the same cell. Fix any that do.
- [ ] **Step 5: Commit.**

```bash
git add handouts/session-1-participant-sheet.html handouts/session-2-participant-sheet.html handouts/session-3-participant-sheet.html
git commit -m "Handouts: one participant sheet per Day 4 session"
```

---

### Task 6: Records and final render (coordinator)

**Files:**
- Modify: `README.md`, `docs/reviews/2026-11-17-day4-decks-review.md`, `docs/project-log.md`

- [ ] **Step 1: Full check.** Run `node tools/day4-deck-check.mjs` and `node tools/day4-s3-sync.mjs --check`. Expected: `PASS` and exit code 0 from both.
- [ ] **Step 2: Render.** Run `node .review/day4-render.mjs && node .review/day4-render.mjs --check`. Expected: `PASS`.
- [ ] **Step 3: Scope guard.** Run `git diff --stat main -- decks/day3-s1.html decks/day3-s1-v1.html decks/day3-s1-v2.html decks/day3-s1-v3.html decks/day3-s2.html decks/day3-s3.html prompts demos tools/deck-check`. Expected: no output.
- [ ] **Step 4: Records.** Apply spec §10: the README row for `handouts/`, the check command and the reworded open item; the "Corrections after the review" section in the review report with the #8 correction and a pointer to the spec; one dated entry at the end of `docs/project-log.md` listing what changed, the untested prompts and the two findings left to the facilitator (spec §8).
- [ ] **Step 5: Commit.**

```bash
git add README.md docs/reviews/2026-11-17-day4-decks-review.md docs/project-log.md
git commit -m "Docs: Day 4 deck fixes recorded in README, review report and project log"
```
