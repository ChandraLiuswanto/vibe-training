# Day 4 Session 2 Deck (Access Control) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build one self-contained 18-slide HTML deck for Day 4 Session 2 (login with a mock directory, two roles, admin page, audit trail) that looks and behaves like the Session 1 deck, plus a script that checks it.

**Architecture:** The deck is a copy of the Session 1 shell (two CSS blocks byte-for-byte, the same script with a short list of changes) with 18 new slides and 7 new practice prompts. A Node check script drives Edge through `playwright-core` and is the test for every deck task.

**Tech Stack:** Plain HTML, CSS and JavaScript in one file; Node 18+ with `tools/deck-check/node_modules/playwright-core`; Microsoft Edge.

**Spec:** `docs/superpowers/specs/2026-11-17-day4-s2-access-control-design.md` (read it; this plan does not repeat its tables)

**Reference deck ("S1", read-only, never edit):** `C:\Users\HP\pr-reviews\vibe-training-pr4\decks\session-1-external-data-visual.html`

## Global Constraints

- Work in `C:\Users\HP\OCBC\brown-bag\vibe-training` on branch `autopilot/day4-s2-access-control`. Never push, never switch branch.
- Language: English.
- One HTML file, no network requests, no external fonts, images or scripts.
- S1's two CSS blocks (reference file line 7 and line 10) are copied byte-for-byte into the deck's `<style>`, in the same positions (line 7 and line 10, with the same blank lines and comment between them). New styles go only in a third block that starts with `/* Session 2 additions */`.
- Stage fixed at 1600×900. Only S1's CSS variables and Arial/Helvetica. Never shrink type to fit; move words to the speaker note instead.
- Visible words per slide (title, footer and speaker note excluded): at most 40; slide 17 at most 60.
- Every slide: `<section class="slide visual-slide" data-title="…">` with the `data-title` and visible title from spec §5, one `h1` (slide 1) or `h2`, and one `<aside class="speaker-note">` of 35 to 90 words.
- Logos: only S1's embedded React, FastAPI and OpenCode images. New pictures are inline SVG in S1's `.vi` style: `<svg class="vi" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">`.
- The words `Frankfurter`, `Google Drive`, `Session 1` and `csv` (any case) must not appear in visible slide text or in the script. Speaker notes are exempt.
- Never write that hiding a button protects a feature, or that the mock directory is real security. No prompt may ask to log passwords, tokens or session IDs.
- Test command for the deck: `node tools/session-2-visual-check.mjs` from the repo root; exit code 0 means pass.

## Review Focus

1. A long name or label in a mock-up (for example an audit row) wraps and pushes content off the slide at 1280×720: expected no overflow at both sizes (check 3 covers every slide).
2. Pressing Space or an arrow key while a button has focus: expected the S1 behaviour, unchanged (Task 2 must not edit the key handler).
3. Opening the deck at `#slide-18` or an out-of-range hash such as `#slide-99`: expected the last slide, no error (Task 1 adds this check as check 10).
4. Printing: expected the handout to list all 7 prompts under the Session 2 heading (Task 1 adds this to check 5: `#print-prompts` contains 7 `article` elements and the heading text).
5. Clipboard blocked (file URL): expected S1's select-text fallback, unchanged (Task 2 must not edit `copyPrompt`).

## File Structure

| File | Responsibility | Tasks |
|---|---|---|
| `tools/session-2-visual-check.mjs` | The checks of spec §8 plus Review Focus 3 and 4 | 1 |
| `decks/session-2-access-control-visual.html` | The deck | 2, then 3, then 4 (in sequence) |
| `docs/project-log.md` | One dated entry | 5 |

Tasks 1, 2 and 5 touch disjoint files and run in parallel. Tasks 3 and 4 follow Task 2 in sequence and need Task 1 finished.

---

### Task 1: Check script

**Files:**
- Create: `tools/session-2-visual-check.mjs`

**Interfaces:**
- Produces: `node tools/session-2-visual-check.mjs [deckPath] [--only=1,2,…]`. `deckPath` defaults to `decks/session-2-access-control-visual.html`. `--only` limits the run to the listed check numbers. Each failure prints one line `FAIL <check number> slide <n>: <message>` (omit `slide <n>` when not slide-specific); the last line is `PASS` or `FAILED: <count>`; exit code 0 or 1. It also prints one line per slide: `slide <n> "<visible title>" words=<count>`.
- Consumes: the deck's DOM contract: `.slide`, `.slide.active`, `.speaker-note`, `footer.foot`, `#counter`, `#modal`, `#modal-title`, `#modal-body`, `[data-prompt]`, `[data-action="prompts"]`, `.quiz[data-correct]`, `.answer`, `#print-prompts`, and a top-level `const prompts=[…]` in the page script. `prompts` is a `const` and so is not on `window`; read it with `page.evaluate(() => prompts)`.

- [ ] **Step 1: Write the script with checks 1 to 10**

Import `chromium` from `./deck-check/node_modules/playwright-core/index.mjs` (path relative to the script file); launch with `executablePath: 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'`. Navigate between slides with `location.hash = '#slide-N'` and wait 250 ms.

Checks 1 to 9 are spec §8 items 1 to 9, with these exact rules:
- Check 1 expected `data-title` list, in order: the 18 values of spec §5's table, column 2. Hard-code them.
- Word count (checks 1, 2, 5): split text on whitespace, count tokens that contain at least one letter or digit. Visible words of a slide = `innerText` of the slide after removing, in a clone, `.speaker-note`, `footer`, and the `h1`/`h2`.
- Check 3 at viewports 1920×1080 and 1280×720: for each element in the active slide outside `.speaker-note`, with non-zero size, fail when its rectangle exceeds the slide's rectangle by more than 1 px on the right, bottom or left; fail when the slide's `scrollHeight` exceeds `clientHeight` by more than 2.
- Check 5 prompt ids in order: `access-plan`, `login-build`, `roles-build`, `admin-build`, `audit-build`, `access-test`, `finish`; each `text` 120 to 330 words; `#print-prompts` holds 7 `article` elements and its text includes `Session 2 · Practice handout`.
- Check 6: on slide 14 click `.slide.active [data-prompt]` and expect `#modal` open with `#modal-title` equal to `prompts[0].title` and `#modal-body` text including `Untested`; close with Escape; click `[data-action="prompts"]` in `#controls` and expect 7 `[data-prompt]` buttons inside `#modal-body`; on slide 9 click the second `.quiz` and expect `.answer` text to start with `B.`.
- Check 7 compares lines 7 and 10 of the deck with lines 7 and 10 of the reference file (split on `\n`, strip a trailing `\r`). If the reference file is missing, print `WARN 7: reference deck not found, skipped`.
- Check 8: case-insensitive search for the four words in (a) each slide's visible text including its title and (b) the text of the page's last `<script>` element.
- Check 9: screenshots at 1920×1080 to `.review/session-2-shots/sNN.png` (create the folder).
- Check 10: loading `#slide-18` shows `18 / 18` in `#counter`; loading `#slide-99` shows `18 / 18`; neither raises a page error.

- [ ] **Step 2: Run it against the S1 reference and confirm it fails for the right reasons**

Run: `node tools/session-2-visual-check.mjs "C:/Users/HP/pr-reviews/vibe-training-pr4/decks/session-1-external-data-visual.html"`
Expected: exit code 1; `FAIL 1` lines for `data-title` mismatches; `FAIL 5` for prompt ids; `FAIL 8` for banned words; no `FAIL 3`, no `FAIL 4`, no `FAIL 7`; 18 `slide …` lines; the script does not crash.

- [ ] **Step 3: Run it with no deck present**

Run: `node tools/session-2-visual-check.mjs decks/does-not-exist.html`
Expected: one line `FAIL 0: deck not found: …` and exit code 1.

- [ ] **Step 4: Commit**

```bash
git add tools/session-2-visual-check.mjs
git commit -m "test: add Session 2 deck check script"
```

---

### Task 2: Deck shell, script, prompts and placeholder slides

**Files:**
- Create: `decks/session-2-access-control-visual.html`

**Interfaces:**
- Consumes: the reference deck; spec §6 and §7.
- Produces: a deck whose head, styles, controls, dialog and script are final, with 18 placeholder slides that Tasks 3 and 4 replace. Each placeholder is exactly:
  `<section class="slide visual-slide" data-title="<spec §5 data-title>">` newline `<div class="eyebrow">Placeholder</div><h2><spec §5 visible title></h2>` newline `<aside class="speaker-note">Placeholder note.</aside></section>`
  (slide 1 also carries the class `active`; slide 9 also contains `<div class="quiz-row"><button class="quiz" data-correct="false">A</button><button class="quiz" data-correct="true">B</button><button class="quiz" data-correct="false">C</button><p class="answer" aria-live="polite"></p></div>`; slide 14 also contains `<button class="btn primary" data-prompt="access-plan">Planning prompt ↗</button>`.)
  A third style block `/* Session 2 additions */` exists (empty apart from the comment) for Tasks 3 and 4 to fill.

- [ ] **Step 1: Run the check and watch it fail**

Run: `node tools/session-2-visual-check.mjs` (if Task 1 is not finished yet, skip this step and note it in your report)
Expected: `FAIL 0: deck not found`.

- [ ] **Step 2: Create the file from the reference**

Copy the reference file's lines 1 to 15 and 70 to 206, then apply spec §6. Keep lines 7 and 10 byte-for-byte (copy the file with a tool, then edit other lines; do not retype CSS). Concretely:
- Line 5 `<title>` and line 15 `aria-label` as in spec §6.
- After the second CSS block add a blank line and the line `/* Session 2 additions */`.
- Remove `const csv=…`, the `#download-csv` click assignment, and any other reference to `csv`.
- Footer string: `Financial App · Session 2 · Access control`.
- `promptDialog()`: intro paragraph becomes `<p><b>Untested — rehearse before class.</b> Copy this prompt into OpenCode. Read the plan and approve changes deliberately.</p>`.
- `promptList()`: intro from spec §6; the help button label becomes `Setup help`.
- `help()`: title and three sections from spec §6, each section an `<h4>` and one `<p>`; no links.
- Download file name `session-2-practice-prompts.txt`.
- Quiz handler: the `.answer` text is always `B. The back end must refuse the request.`; keep the `right`/`wrong` class logic.
- Print handout: heading `Session 2 · Practice handout`; intro `Four pieces, in order: login, roles, admin page, audit trail. Every prompt is untested — rehearse before class.`
- Leave `render`, `resize`, `copyPrompt`, `download`, `openDialog`, the key handler and the hash handler unchanged.

- [ ] **Step 3: Write the 7 prompts**

Replace the `prompts` array with the 7 prompts of spec §7 (ids, titles and required content from its table; the four "rules for all seven" worked into each prompt's own wording). Model the voice and layout on S1's prompts (reference lines 78 to 186): a first sentence that sets the scope, a blank line, numbered or dashed requirements, a closing paragraph on what to report and what not to do. Each 120 to 330 words. Use the names `alya`, `budi`, `citra` and the practice password `Training-2026` only where the spec's table asks for accounts. Do not use backticks or `${` inside prompt text (they sit in template literals).

- [ ] **Step 4: Add the 18 placeholder slides**

Between the `<main …>` line and `</main></div>`, in spec §5 order, in the exact form given under Produces.

- [ ] **Step 5: Run the checks that apply now**

Run: `node tools/session-2-visual-check.mjs --only=3,4,5,6,7,8,10`
Expected: `PASS`. (Checks 1 and 2 fail until Tasks 3 and 4 because the placeholder notes are short; that is expected and is not run here.) If Task 1 is still not finished, open the deck yourself with a short throw-away Playwright snippet to confirm no console errors, and say so in your report.

- [ ] **Step 6: Commit**

```bash
git add decks/session-2-access-control-visual.html
git commit -m "feat: add Session 2 deck shell, prompts and placeholder slides"
```

---

### Task 3: Slides 1 to 9 (Act 1: login and roles)

**Files:**
- Modify: `decks/session-2-access-control-visual.html` (the first 9 `<section class="slide …">` elements and the `/* Session 2 additions */` block only)

**Interfaces:**
- Consumes: Task 2's placeholders; S1's component classes (`.hero-grid`, `.visual`, `.v-rail`, `.v-tile`, `.v-arrow`, `.vi`, `.split-v…`, `.quiz-row`, `.quiz`, `.answer`, `.tag`, `.brand`); the screenshots of S1 in `C:\Users\HP\pr-reviews\vibe-training-pr4\.review\shots\s01.png … s18.png` as the visual standard.
- Produces: final slides 1 to 9. New CSS class names start with `s2-` so Task 4 cannot collide. Reusable pieces Task 4 will use, defined here: `.s2-person` (avatar circle with initial + name + role chip; modifier `.admin`), `.s2-chip` (small role label; modifier `.admin` uses `--accent`), `.s2-app` (browser-window frame for app mock-ups with a header row that can hold a `.s2-person`).

- [ ] **Step 1: Run the check for these slides and watch it fail**

Run: `node tools/session-2-visual-check.mjs --only=1,2`
Expected: `FAIL 1` on the speaker-note length for slides 1 to 18.

- [ ] **Step 2: Build slides 1 to 9**

For each slide replace the placeholder with the eyebrow, title and main visual of spec §5 (slide 9: spec §5.1 exactly; slide 8: the table of spec §4.1 as a tick/cross grid with 5 rows and 2 role columns; slide 6: the three practice accounts and the label `Practice accounts only`, password `Training-2026`). Eyebrows: slide 1 `Financial App · Session 2 of 3`; others a 2 to 5 word label in S1's style (for example `Concept · Authentication`). Reuse S1's markup patterns for the matching slide type before writing new CSS: slide 1 ← S1 slide 1, slide 2 ← S1 slide 2, slide 3 ← S1 slide 3, slide 4 ← S1 slide 5, slides 5 to 7 ← S1 slide 4 rails, slide 9 ← S1 slide 7. Cast: Alya (Admin) and Budi (User) appear from slide 3 on. Write each speaker note per spec §5.4 (35 to 90 words), including the required content for slides 2 or 3, 6 and 7.

- [ ] **Step 3: Run the checks**

Run: `node tools/session-2-visual-check.mjs --only=1,2,3,4,6,7,8,9`
Expected: no `FAIL` line that names slides 1 to 9 (slides 10 to 18 still fail check 1).

- [ ] **Step 4: Look at your screenshots**

Open `.review/session-2-shots/s01.png` to `s09.png` and compare each with the S1 screenshot of the same slide type: same margins, same title size, the visual fills the area between title and footer, nothing collides with the control bar at the bottom centre, text is readable. Fix and re-run Step 3 until they hold up.

- [ ] **Step 5: Commit**

```bash
git add decks/session-2-access-control-visual.html
git commit -m "feat: add Session 2 slides 1-9 (login and roles)"
```

---

### Task 4: Slides 10 to 18 (Act 2: admin page, audit trail, practice)

**Files:**
- Modify: `decks/session-2-access-control-visual.html` (the last 9 slide sections and the `/* Session 2 additions */` block only)

**Interfaces:**
- Consumes: Task 3's `.s2-person`, `.s2-chip`, `.s2-app`; S1's `.demo-layout`, `.v-terminal`, `.term-line`, `.term-approval`, `.v-step`, `.lab-timeline`, `.lab-row`, `.lab-time`, `.actions`, `.btn`, `.finish…` classes.
- Produces: the finished deck.

- [ ] **Step 1: Run the check and watch it fail**

Run: `node tools/session-2-visual-check.mjs --only=1,2`
Expected: `FAIL 1` lines for slides 10 to 18 only.

- [ ] **Step 2: Build slides 10 to 18**

Per spec §5, §5.2, §5.3 and §5.4. Fixed content:
- Slide 10: Budi's request shows `GET /api/admin/users` and `403`.
- Slide 11: rows Alya · Admin (lock icon, no Demote button), Budi · User · `Promote`, Citra · User · `Promote`; a count tile `3 users`.
- Slide 13: five event types: Sign-in and sign-out · Watchlist change · Role change · Refused request · Protected API call.
- Slide 14: S1 slide 10's terminal with lines `YOU Add a login and two roles.` / `AGENT 1. Inspect existing app 2. Mock directory + sign-in 3. Roles + back-end check 4. Admin page + audit trail` / `Review plan  Approve ✓` / `AGENT Build only the approved stage.`; three steps `Keep existing features`, `Check at the back end`, `Approve one stage at a time`; one button `Planning prompt ↗` with `data-prompt="access-plan"`.
- Slide 16 rows (time · user · action · result): `09:02 · budi · Sign-in · OK`, `09:03 · budi · Watchlist add BBRI.JK · OK`, `09:04 · budi · GET /api/admin/users · 403`, `09:06 · alya · Promote citra to Admin · OK`, `09:07 · unknown · Sign-in · Failed`.
- Slide 17: tag `Your practice · 60 minutes`; the six rows of spec §5.2; buttons `All practice prompts ↗` (`data-action="prompts"`) and `Setup help ↗` (`data-action="help"`); the small text of spec §5.2.
- Slide 18: the four cards of spec §5.3 shortened to at most 8 words each, and `Next → Session 3`.

- [ ] **Step 3: Run the full check**

Run: `node tools/session-2-visual-check.mjs`
Expected: `PASS`, exit code 0.

- [ ] **Step 4: Look at your screenshots**

As Task 3 Step 4, for `s10.png` to `s18.png`, and skim `s01.png` to `s09.png` to confirm nothing changed.

- [ ] **Step 5: Commit**

```bash
git add decks/session-2-access-control-visual.html
git commit -m "feat: add Session 2 slides 10-18 (admin page and audit trail)"
```

---

### Task 5: Project log entry

**Files:**
- Modify: `docs/project-log.md`

- [ ] **Step 1: Read the file's last 30 lines and match its entry format**

- [ ] **Step 2: Append one entry dated 2026-11-17**

Content, in the file's own style: Day 4 Session 2 deck = one deck, 60 min presentation + 60 min practice, covering login with mock LDAP, roles, admin page and audit trail *(user)*; same visual design as the Session 1 deck in PR #4, short titles *(user)*; approach A, two acts with one cast *(user)*; Users do regular app actions including watchlist edits, Admins alone promote or demote users and see usage *(user)*; deck file `decks/session-2-access-control-visual.html`; spec path; prompts untested.

- [ ] **Step 3: Commit**

```bash
git add docs/project-log.md
git commit -m "docs: log Day 4 Session 2 deck decisions"
```
