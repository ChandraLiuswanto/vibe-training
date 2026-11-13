# S2 v3 deck — verification report

Deck: `decks/day3-s2.html` (built as `decks/day3-s2-v3.html`; v2 kept as `tools/deck-check/fixtures/day3-s2-v2.html`). Merged onto `origin/main`, keeping its S2 runtime fixes (offline fonts, hidden-step visibility, settle, presenter timer, copy fallback, hash parsing). Date: 2026-11-12.

## Automated checks
- Lint (`check_deck.py` with outline, copy, prompts, `--profile s2`): **0 errors**. Titles match the outline, notes on every slide, no banned phrases, only the five workflow names, prompts verbatim from `prompts/s2.md`, timing 180 min (run 110).
- Render (`render.mjs`, Edge, 1920×1080 and 1280×720): all 27 slides, every step (216 shots), **0 failures**, normal and `--reduced-motion`. After the fix wave, slides 6–8 and 13–25 re-rendered: 0 failures.
- Notes re-injected from the copy doc; the deck matches.
- S1 regression: S1 v3 lint 0 errors; `pytest tools/deck-check` 20 passed.
- Word counts for slides 14, 17, 18, 19, 22, 23, 25 re-measured in the browser after the fix wave (same rule as render.mjs); the table below uses the measured values.

## Per slide (title, type, words · budget · exception)
| # | Title | Type | Words · budget · exception |
|---|---|---|---|
| 1 | Upgrade your Financial App: watchlist and AI knowledge | title | 11 · 40 · none |
| 2 | Today your app saves prices and your chatbot answers from official pages | visual | 23 · 40 · none |
| 3 | Same five steps as this morning, once for each new feature | visual | 23 · 40 · none |
| 4 | Keep your Session 1 app if it works; otherwise we move you to checkpoint s1-chatbot | talk | 23 · 40 · none |
| 5 | Your app keeps prices only while the back end is running | visual | 23 · 40 · none |
| 6 | A database keeps what the app must remember, in tables of rows and columns | visual | 28 · 40 · none |
| 7 | A row holds one record; a column holds one kind of value | check | 41 · 60 · quiz choices (A, B, C) are not counted; the 41 = question (13) + grid and Sample tag (10) + reveal line (18) |
| 8 | Our app uses two tables, linked by the ticker | visual | 40 · 40 · none |
| 9 | Free Yahoo data can fail, so the app shows saved prices and their date | visual | 37 · 40 · none |
| 10 | Worked example: read one saved price row and check its date | demo | 35 · 40 · none |
| 11 | Run 1a: interview for the price database, update the spec, approve the plan | run | 51 · 60 · prompt boxes (copyable prompts, including the long spec prompt) are not counted; chips and labels are counted |
| 12 | Run 1b: build the database, look inside, refresh twice, push safely | run | 60 · 60 · prompt boxes (copyable prompts) are not counted; chips and labels are counted |
| 13 | Run 2a: spec, plan and build a watchlist the dashboard follows | run | 59 · 60 · prompt boxes (copyable prompts, including the long spec prompt) are not counted; chips and labels are counted |
| 14 | Run 2b: test it like a user, including a restart, then push | run | 50 · 60 · prompt boxes (copyable prompts) are not counted; chips and labels are counted |
| 15 | A useful bug report says what you did, what you expected and what you saw | check | 28 · 60 · quiz choices A, B, C and the prompt box are not counted |
| 16 | The model's training is not a reliable source for current rules | visual | 32 · 40 · none |
| 17 | The system prompt tells the chatbot its role and rules, and we test that it follows them | visual | 40 · 40 · none |
| 18 | A Wiki lets the app send matching official text with each question | visual | 38 · 40 · none |
| 19 | Only OJK and IDX pages go in, each with its link and the date you checked it | visual | 38 · 40 · none |
| 20 | Worked example: check one answer against its source page | demo | 39 · 40 · none |
| 21 | Run 3a: record three answers, then interview and plan the Wiki | run | 59 · 60 · prompt boxes (copyable prompts, including the long spec prompt) are not counted; chips and labels are counted |
| 22 | Run 3b: find official pages, check each one, build the Wiki | run | 57 · 60 · prompt boxes (copyable prompts) are not counted (rendered count); chips and labels are counted |
| 23 | Run 3c: set the system prompt, check answers against their pages, then push | run | 57 · 60 · prompt boxes (copyable prompts) are not counted (rendered count); chips and labels are counted |
| 24 | A regulatory answer needs a source you can open and check | check | 18 · 60 · quiz choices A, B, C are not counted |
| 25 | Data lives in the database, knowledge in the Wiki, behaviour in the system prompt | recap | 39 · 40 · none |
| 26 | Questions | Q&A | 1 · 40 · none |
| 27 | Next session: turn your data into a report and a deck | talk | 26 · 40 · none |


## Contract check
Every result a run asks participants to check is requested by a prompt in that run or an earlier one (copy doc, "Contract check"). The fix wave removed the one gap the review found: slide 14 no longer asks to see each stock's history on the dashboard.

## Independent review (gpt-6.1-sol, low thinking, three lenses, independent)
| Lens | Verdict | v2 findings |
|---|---|---|
| Material | P0 found — v2 P0-6 only (untested prompts, no verified URL list / fallback data) | P0-2, P0-4, P0-5 and most P1 fixed; P0-1, P0-3, P1-4, P2-1, P2-2 partly |
| Storyline | P0 found — v2 P0-6 only | P0-2, P0-4, P0-5, P1-1/2/5–10, P2-1/3/5 fixed; P0-1, P0-3, P1-3, P1-4, P2-4, P2-6 partly |
| Visual / animation | No P0 | P0-1, P1-3, P1-7, P1-8, P2-9, P2-10, P3-1 fixed; P2-4, P2-7, P2-8 partly; P3-2 not fixed |

P0-6 is a delivery task, not a slide edit (spec §2 non-goal, §10 delivery blockers). No P0 remains in the deck content.

### Fixed in the fix wave (commit 364b723 + word-count correction)
1. Slide 14: removed "with history" from the test (no prompt asks the app to show history).
2. Slides 2, 17, 21, 23, 25: participants "set and test" the system prompt; they do not "write" it. Slide 23 title updated in outline, copy, spec.
3. Slide 22: "Tell opencode which to drop" before the build prompt ("the pages I approved").
4. Slide 25 gear (`.spin`) bounded to 3 cycles.
5. Arrows inside an unrevealed step no longer draw on slide arrival.

### Not changed (reasons)
- Slide 19 visible "Official is not the same as current" line: would take step 3 to 49 words (>40). Stays in notes; slide 21 spec still records last-updated and checked dates.
- Slide 13 spec block is dense on a 720p projector (28px authored ≈ 18.7px). Put the full spec in the handout; never shrink type.
- Price policy: adjusted vs unadjusted yfinance prices and the `change_pct` basis are not stated in the spec prompt (P2). Settle in rehearsal.
- Slide 6 title describes a relational (tables) database; notes scope it to our SQLite app (P2).
- Slide 20 worked example shows answer vs source page, not the full page → Wiki entry → answer chain (P1-3 partly).
- Slide 14 marks file review and push as "Iterate" (P2, storyline). Kept as written in the copy.
- Remaining infinite rules: `.seq`, `.dot.loop` (unused in S2), Q&A drifting shapes and text carets (allowed by spec §3).
- Google Fonts (P3-2): offline laptops may wrap differently. Follow-up for all three decks.

## Delivery blockers (spec §10, before class)
- Rehearse every UNTESTED prompt end to end on Windows and Mac, including web search/fetch and GitHub sign-in (P0-6).
- Host checkpoints `s1-chatbot`, `s2-database`, `s2-watchlist`, `s2-wiki` with saved NISP/BBRI/TLKM prices.
- Write the recovery card and the verified OJK/IDX URL list for the handout; re-open the slide 20 OJK page before class.

## Follow-ups (spec §10)
- S3 deck: align workflow names; it assumes TLKM history.
- Embed fonts for offline laptops (all decks).
- S1 v3 deck has the same focus/Space bug (P2-9).
