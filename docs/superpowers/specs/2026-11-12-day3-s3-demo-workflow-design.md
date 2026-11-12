# Day 3 · Session 3 — Run 3 becomes a trainer demo

Date: 2026-11-12 · Status: draft for approval

## Intent

Trainees are tired by the third run, and building a saved opencode command teaches them an opencode-specific trick. So Run 3 stops being hands-on. The trainer demos a saved workflow from a ready-made folder, and a new slide tells trainees how to get skills and tools they don't have yet: ask the agent to find them, or install them by hand.

## Goals

- Trainees finish Session 3 after two hands-on runs (report, deck).
- They still see what a saved workflow does: one command, many steps, a new ticker.
- They leave knowing that skills and tools can be asked for or installed, with the trainer's own deck skills as examples.

## Non-goals

- No PPTX-versus-HTML comparison (dropped).
- No trainee work in Run 3, and no `s3-workflow` checkpoint for trainees.
- No changes to Runs 1 and 2 beyond what the cut forces.

## Anti-goals

- A demo that only works on the trainer's laptop on a good day. It must have a recorded backup.
- Claims on the slides that the demo didn't actually show.

## Approaches considered

- **A. Self-contained demo folder (picked).** `/data/training/deck` has its own SQLite database, refresh script and saved command. Ready and testable now; not literally the trainees' app.
- B. Demo from the reference app. Matches trainees exactly, but `financial-app/` has no code yet, so it can't be built or tested today.

## Deck changes (story gate: headlines)

Opening
1. AI-powered reports and presentations
2. Today the AI turns your app's data into a report and a slide deck
3. Start from your own app or switch to checkpoint s2-wiki

Workflows
4. A prompt does one thing; a workflow runs many steps in order *(kept)*
5. Prompt, skill and workflow are three levels of reuse *(kept)*
~~6. Is each of these a prompt, a skill or a workflow?~~ *(cut)*

Run 1 and Run 2: headlines unchanged, renumbered down by one (7→6, 8a/8b→7a/7b, 9→8, 10→9, 11→10, 12→11, 13a/13b→12a/12b, 14→13).

Demo: a saved workflow
14. If you'll do it again next month, save it as a workflow; brainstorm → spec → plan is one too *(kept)*
15. **Watch: one saved command builds the TLKM report and deck** *(replaces Run 3; trainer demo)*
16. **Need a skill or tool? Ask the agent to find it, or install it yourself** *(new)*
17. What should you still check by hand every time? *(kept quiz; wording says "a workflow" rather than "your command")*

Close
18. **In one day you built and upgraded a business app, then saw it automated** *(recap reworded)*
19. Questions
20. Day 4: connect your app to other services and the web

Total: 22 slides counting 7a/7b/12a/12b (unchanged: one cut, one added).

### Slide 15 — demo (visual, presenter-led)

- On screen: the command `/stock-report TLKM.JK` and the four steps lighting in order (refresh → report → check → deck), then two result thumbnails: TLKM report, TLKM deck.
- Notes: what to type, what to point at, and the fallback ("if it stalls, open `backup/`").
- Word budget: presented, ≤40.

### Slide 16 — skills and tools (visual)

- Two halves. **Ask the agent:** "Find a skill for … and use it." **Install it yourself:** the tool the agent asks for (e.g. the PowerPoint library).
- Example skills, by job: Coherence → `presentation-creator` · Humanizer → `clarity` · Design → `frontend-slides`.
- Word budget: presented, ≤40.

## Demo folder: `/data/training/deck`

- `prices.db`: SQLite with the trainees' schema, `stocks(ticker, name, added_at)` and `prices(ticker, date, open, high, low, close, volume)`, holding one year of NISP.JK and TLKM.JK.
- `refresh.py`: adds a ticker and loads its prices from Yahoo, run with `uv` so nothing is installed globally.
- `.opencode/commands/stock-report.md`: the saved workflow. It takes `$ARGUMENTS` as the ticker and runs refresh → report (`reports/<T>-report.html`) → check numbers against the database → deck (`reports/<T>-deck.pptx`).
- `backup/`: one finished TLKM report and deck from a tested run.
- `README.md`: a short trainer run sheet.

## Timing (180 min)

Workflows 20 → 15 (quiz cut). Run 3 35 → 15 (demo 8, skills slide 3, quiz 4). This frees 25 min.

**Builder's call, open to change:** give 10 min to a break after Run 1, 10 to Run 2, and 5 to Q&A.

## Left to the builder

- Exact visuals for slides 16 and 17, in the existing deck style.
- Speaker notes and copy-doc sync (`docs/copy/day3-s3-v2.md`, outline `docs/outlines/day3-s3-v2.md`).
- The deck renumbers from 1 to 21; the lint, render and word-count checks must pass as before.
- Testing the demo end to end on opencode 1.19.5, and recording the backup.
