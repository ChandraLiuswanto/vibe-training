# Day 4 Visual Decks Review Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce one combined review report on the three Day 4 decks covering material, quality, and ease for non-technical business users, without editing any deck.

**Architecture:** One worker renders every slide to PNG. Three reviewers then work independently, one angle each across all three decks, and each writes one raw review file. The coordinator merges the three raw reviews into the report and checks every P0 against the deck.

**Tech Stack:** Node with `playwright-core` from `tools/deck-check/node_modules`, Microsoft Edge at `C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe`, Markdown.

**Spec:** `docs/superpowers/specs/2026-11-17-day4-decks-review-design.md`

## Global Constraints

- Repository: `C:/Users/HP/OCBC/brown-bag/vibe-training`, branch `autopilot/day4-decks-review`.
- Decks under review, and their short names used in every file below:
  - `s1` = `decks/session-1-external-data-visual.html` (18 slides)
  - `s2` = `decks/session-2-access-control-visual.html` (18 slides)
  - `s3` = `decks/session-3-vps-deployment-visual.html` (16 slides)
- Never edit anything under `decks/`, `docs/outlines/`, `prompts/`, `tools/` or `demos/`. `git diff --stat main -- decks docs/outlines prompts tools demos` must stay empty.
- The Day 3 decks (`decks/day3-*`) are out of scope.
- Practice prompts are read, not executed. No app is built or run.
- Slide numbers in findings are the position of the slide in the deck (1-based), which is the number the deck shows.
- Severity scale, copied from the spec:
  - **P0** — wrong, misleading or ambiguous knowledge, or an unsafe habit. Fix before teaching.
  - **P1** — the idea is right but poorly taught, missing, or in the wrong place; or a slide a non-technical user cannot follow.
  - **P2** — a visual or layout problem that hurts clarity.
  - **P3** — polish.
- Every finding names the deck, the slide number, the evidence (quoted wording or screenshot file name), and a suggested fix. A technical claim says how it was checked: `deck text`, `project file <path>`, or `reviewer knowledge`.
- No finding invented to fill a list. A deck or angle with few problems gets a short list.
- Session 2's short titles are an owner decision of 2026-11-17 and are not a finding. Reviewers report the titles the deck actually shows.
- Report language: plain English, no term the owner would need to look up.
- Audience of the decks: bank business users with no coding background who build with OpenCode.

## Review Focus

- A deck slide that only shows its full content after a click or with a panel open: the screenshots must show the opened state too, or the reviewers judge an incomplete slide.
- A screenshot that is blank or cut off because the page was captured before it finished drawing: Task 1's check rejects files under 15 KB.
- Speaker notes: they are hidden by default, so Task 1 extracts them to text for the reviewers.
- A finding that two reviewers describe differently for the same slide: Task 5 merges them and records the count.
- A reviewer's P0 that rests on a misreading of the slide: Task 5 re-checks every P0 against the deck text and the screenshot.

---

## File Structure

| File | Responsibility | Owner |
|---|---|---|
| `.review/day4-render.mjs` | Renders slides, prompt panels, and extracts notes and prompts | Task 1 |
| `.review/day4-shots/<s1\|s2\|s3>/sNN.png` | One PNG per slide (git-ignored by `.review/*-shots/`) | Task 1 |
| `.review/day4-shots/<deck>/pNN.png` | One PNG per practice prompt with the prompt panel open | Task 1 |
| `.review/day4-text/<deck>.md` | Per slide: title, visible text, word count, speaker notes; then every practice prompt in full | Task 1 |
| `.review/day4-r-material.md` | Raw review: accuracy and safety habits | Task 2 |
| `.review/day4-r-audience.md` | Raw review: storyline and ease for business users | Task 3 |
| `.review/day4-r-visuals.md` | Raw review: visual quality and slide craft | Task 4 |
| `docs/reviews/2026-11-17-day4-decks-review.md` | The combined report | Task 5 |
| `docs/project-log.md` | One dated entry | Task 5 |

Tasks 2, 3 and 4 write disjoint files and run in parallel after Task 1. Task 5 runs last.

---

### Task 1: Render the slides and extract the text

**Files:**
- Create: `.review/day4-render.mjs`
- Create: `.review/day4-shots/{s1,s2,s3}/*.png`, `.review/day4-text/{s1,s2,s3}.md`

**Interfaces:**
- Consumes: the three deck files. Each deck holds its slides as `<section class="slide …">` elements, moves with ArrowRight, and accepts `#N` in the URL to jump to slide N. Elements carrying a `data-prompt` attribute open a practice prompt whose text appears in `#prompt-text`. Speaker notes show in `#notes` after `#notes-toggle` is used. Read each deck's script before relying on these; they are observations, not a contract.
- Produces: the PNG and Markdown files named in File Structure. `sNN` and `pNN` are zero-padded to two digits.

- [ ] **Step 1: Write the check first.** In `.review/day4-render.mjs`, add a `--check` mode that reads only the output folders and exits 1 unless: `s1` has `s01.png`–`s18.png`, `s2` has `s01.png`–`s18.png`, `s3` has `s01.png`–`s16.png`; every PNG is at least 15 KB; every deck has at least one `pNN.png`; each `.review/day4-text/<deck>.md` has one `## Slide N` heading per slide and a `## Practice prompts` heading. It prints one `FAIL <reason>` line per problem, then `PASS` or `FAILED: <n>`.

- [ ] **Step 2: Run the check and watch it fail.**

Run: `node .review/day4-render.mjs --check`
Expected: `FAILED: <n>` with exit code 1, because nothing is rendered yet.

- [ ] **Step 3: Implement the renderer.** `node .review/day4-render.mjs` (no flag) opens each deck from its file URL in Edge through `playwright-core` (import from `../tools/deck-check/node_modules/playwright-core/index.mjs`, as `tools/session-2-visual-check.mjs` does) at a 1600×900 viewport, and for each slide: goes to it, waits for animations to settle, advances any in-slide reveal steps so the slide is fully shown, and saves `sNN.png`. For each distinct practice prompt it opens the prompt panel and saves `pNN.png`. It writes `.review/day4-text/<deck>.md` with, per slide, the title, the visible text, the visible word count excluding title and footer, and the speaker notes; then every practice prompt in full under `## Practice prompts`. The page must make no network requests; print a `NETWORK <url>` line for any request that is not a `file:` or `data:` URL.

- [ ] **Step 4: Run the renderer, then the check.**

Run: `node .review/day4-render.mjs && node .review/day4-render.mjs --check`
Expected: `PASS`, exit code 0.

- [ ] **Step 5: Look at the result.** Open six PNGs (first, a middle and last slide of two decks) and one `pNN.png` and confirm the slide is complete, readable and not cut off. Report any deck whose slide cannot be fully shown, and any `NETWORK` line.

- [ ] **Step 6: Commit.**

```bash
git add .review/day4-render.mjs .review/day4-text/s1.md .review/day4-text/s2.md .review/day4-text/s3.md
git commit -m "Review: render and text extraction for the Day 4 decks"
```

The PNG folders are git-ignored and stay uncommitted.

---

### Tasks 2, 3, 4: The three raw reviews

Each reviewer works alone, edits only its own file, and reads: the three deck files, `.review/day4-shots/`, `.review/day4-text/`, `docs/outlines/session-*-visual.md`, `AGENTS.md`, and `docs/superpowers/specs/2026-11-17-day4-s2-access-control-design.md`. Each raw review uses this shape:

```markdown
# Day 4 decks — <angle> review

Checked: <what was read and looked at; what was not checked>

## Verdict per deck
- s1: <two or three sentences>
- s2: …
- s3: …

## Findings
| ID | Sev | Deck | Slide | Problem | Evidence | How checked | Suggested fix |

## What works well
<up to five points, each with a deck and slide>
```

IDs are `M1…` for Task 2, `A1…` for Task 3, `V1…` for Task 4.

### Task 2: Material accuracy and safety habits

**Files:**
- Create: `.review/day4-r-material.md`

- [ ] **Step 1: Review.** For every slide, speaker note and practice prompt, check: is each statement true; is it stated more absolutely than it should be; does any picture or label teach a wrong mental model; do the three decks use one word for one thing; does any instruction teach an unsafe habit for bank staff (approving without reading, secrets in code or Git or pasted errors, public repositories, real credentials, practice set-ups presented as real security, customer data sent to outside services); do the practice prompts ask for what the slides taught; are untested prompts labelled as untested. Topics to check with care: what an API is and how the exchange-rate request and conversion work (s1); MCP and Google Drive OAuth (s1); authentication versus authorization, the mock directory, sessions, back-end role checks and the audit trail (s2); SSH, HTTPS, secrets, data surviving updates, the managed service, logs and backups (s3).
- [ ] **Step 2: Write `.review/day4-r-material.md`** in the shape above, findings ordered by severity.
- [ ] **Step 3: Verify.** Every finding row has all eight cells filled, and the slide number matches the screenshot file with that number. Run: `git status --short` and confirm the only new file from this task is `.review/day4-r-material.md`.
- [ ] **Step 4: Commit.**

```bash
git add .review/day4-r-material.md
git commit -m "Review: Day 4 decks, material and safety"
```

### Task 3: Storyline and ease for non-technical business users

**Files:**
- Create: `.review/day4-r-audience.md`

- [ ] **Step 1: Review.** Read each deck in slide order as a bank business user with no coding background. Per deck, check: does the order follow prerequisites → worked example → practice → check; does each slide follow from the one before; is the business reason given before the technique. Per slide, check the four points in the spec: technical terms used without a plain explanation at first use (list each term); steps that assume knowledge not yet taught in this deck or stated as a prerequisite; how many separate ideas the slide asks the reader to hold at once; whether the practice instructions and prompts can be followed without help. Also check: does the title say what the slide teaches; is the 60-minute practice realistic for this audience; does the participant know when they have finished and whether it worked; do the three decks connect as one day.
- [ ] **Step 2: Write `.review/day4-r-audience.md`** in the shape above. Add, after "Verdict per deck", a section `## Ease for business users` with, per deck, a rating of `Easy`, `Manageable with a facilitator`, or `Hard`, the reason in two sentences, the three hardest slides, and a table of every unexplained term with the slide of first use.
- [ ] **Step 3: Verify.** Same checks as Task 2 Step 3, for `.review/day4-r-audience.md`; plus all three decks have a rating.
- [ ] **Step 4: Commit.**

```bash
git add .review/day4-r-audience.md
git commit -m "Review: Day 4 decks, storyline and audience"
```

### Task 4: Visual quality and slide craft

**Files:**
- Create: `.review/day4-r-visuals.md`

- [ ] **Step 1: Review.** Look at every PNG in `.review/day4-shots/`. Per slide, check: text that is too small to read from the back of a room, cut off, overlapping or low in contrast; diagrams whose reading order is unclear, whose arrows are ambiguous or unlabelled, or that do not match the title; crowding; visible word count against the `AGENTS.md` budgets (40 presented, 60 for exercise slides), using the counts in `.review/day4-text/`; whether the prompt panel is readable. Per deck and across decks, check: one consistent visual language, and whether s3 looks like the same course as s1 and s2; whether titles follow the `AGENTS.md` full-sentence rule (s2's short titles are an owner decision: record the fact once, not as a finding). Open one deck in a browser only if a screenshot is unclear.
- [ ] **Step 2: Write `.review/day4-r-visuals.md`** in the shape above. Evidence cells name the PNG file.
- [ ] **Step 3: Verify.** Same checks as Task 2 Step 3, for `.review/day4-r-visuals.md`.
- [ ] **Step 4: Commit.**

```bash
git add .review/day4-r-visuals.md
git commit -m "Review: Day 4 decks, visuals"
```

---

### Task 5: Combined report (coordinator)

**Files:**
- Create: `docs/reviews/2026-11-17-day4-decks-review.md`
- Modify: `docs/project-log.md` (append one entry)

**Interfaces:**
- Consumes: the three raw review files and their finding IDs.

- [ ] **Step 1: Merge.** List every finding from the three raw reviews. Merge findings about the same problem on the same slide into one, keep the highest severity given, and record which reviewers raised it (`1/3`, `2/3`, `3/3`) and the raw IDs.
- [ ] **Step 2: Check every P0.** For each P0, read the slide's text in `.review/day4-text/` and open its PNG. Keep it, lower it, or drop it, and note the reason for any change in a `Coordinator notes` section. Where reviewers disagree, show both views.
- [ ] **Step 3: Write the report** with these sections in this order: how the review was done and what was not checked (prompts not run); a summary of five lines at most; a verdict per deck; `Ease for non-technical business users` per deck with the rating, hardest slides and the unexplained-term table; findings as one table per severity (`#`, deck, slide, problem, raised by, fix); what works well; a suggested order of fixes; coordinator notes.
- [ ] **Step 4: Verify.** Every P0 and P1 in the raw reviews appears in the report or in the coordinator notes with the reason it was dropped. Run `git diff --stat main -- decks docs/outlines prompts tools demos` and confirm it prints nothing.
- [ ] **Step 5: Append to `docs/project-log.md`** one entry dated 2026-11-17: the decks reviewed, the three angles and models, the finding counts per severity, and the report path.
- [ ] **Step 6: Commit.**

```bash
git add docs/reviews/2026-11-17-day4-decks-review.md docs/project-log.md
git commit -m "Review: combined report for the Day 4 decks"
```
