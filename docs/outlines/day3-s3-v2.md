# Day 3 · Session 3 — outline v2

Headlines approved 2026-11-12 with the design (`docs/superpowers/specs/2026-11-12-day3-s3-demo-workflow-design.md`).

These are the Session 1 v2 rules applied to Session 3:
- about 22 slides
- **2 participant runs** that build on each other, then a trainer demo of a saved workflow
- one 10-minute break after Run 1
- animated diagrams with gentle looping motion

Example stock: **NISP (NISP.JK)**. The trainer demos the saved workflow on TLKM.

Legend: [visual] = animated diagram · [run] = participant hands-on · [demo] = trainer only · [check] = quiz

## Opening
1. AI-powered reports and presentations [title]
2. Today the AI turns your app's data into a report and a slide deck [visual: database → report → deck]
3. Start from your own app or switch to checkpoint s2-wiki [talk, short; recovery sentence]

## Workflows
4. A prompt does one thing; a workflow runs many steps in order [visual: one box vs a chain that runs itself]
5. Prompt, skill and workflow are three levels of reuse [visual: rising steps, links back to S1]

## Run 1 — Write the report
6. A good analysis report has data, charts and an insight you can defend [visual: report page assembles]
7. Run 1: spec the report, generate it from your database, and check every number [run, 2 slides: 7a spec + generate; 7b number check]
8. AI can write confident insights the data doesn't support [visual: a claim with no data underneath cracks]
9. Which claim in this report does the data not prove? [check]

## Run 2 — Turn it into a deck
10. A report is for reading; a deck is for telling [visual: page of text → three slides]
11. Give feedback like a brief: what, why and an example [visual: three-part feedback card]
12. Run 2: turn the report into PowerPoint, then improve it in two feedback rounds [run, 2 slides: 12a generate + note 3 fixes; 12b two rounds]
13. Feedback changed the deck from a data dump into a story [visual: before/after]

## Demo — a saved workflow (trainer)
14. If you'll do it again next month, save it as a workflow; brainstorm → spec → plan is one too [visual: steps fold into one command]
15. Watch: one saved command builds the TLKM report and deck [demo, trainer only]
16. Ask the agent to find a skill or tool, or install it yourself [visual; taught while the demo runs]
17. What should you still check by hand every time? [check]

Demo block:
- Folder: `/data/training/deck` (run sheet in its README.md). opencode 1.19.5, model `9router/opus`, 4 project skills in `.opencode/skills/`.
- On slide 15 the trainer types `/stock-report TLKM.JK`. The command runs refresh → report → check → deck: `reports/TLKM.JK-report.html` and an HTML slide deck, `reports/TLKM.JK-deck.html`, built with the frontend-slides skill, both opened in the browser.
- The run takes about 4 minutes (227 s measured 12 Nov 2026, HTML deck step). The trainer teaches slide 16 while it runs, then goes back and opens both files.
- Fallback: if it errors or passes 7 minutes, open the copies in `backup/`.
- Trainees type nothing in this block. Run 2 stays PowerPoint (`NISP-deck.pptx`); the end-of-session checkpoint is `s3-pptx`.

## Close
18. In one day you built and upgraded a business app, then saw its reporting automated [recap visual: S1 → S2 → S3]
19. Questions [Q&A, moving shapes]
20. Day 4: connect your app to other services and the web

Total: 20 headlines, 22 slides counting the run parts (7a/7b, 12a/12b).

## Timing (180 min)
| Block | Min | Slides |
|---|---|---|
| Opening + recovery | 10 | 1–3 |
| Workflows | 15 | 4–5 |
| Run 1 — report | 45 | 6–9 |
| Break | 10 | after slide 9 (builder's call) |
| Run 2 — deck + feedback | 60 | 10–13 (+10, builder's call) |
| Demo — saved workflow | 15 | 14–17 |
| Close + Q&A | 25 | 18–20 (+5, builder's call) |

Demo block split: slide 14 = 3; slides 15 + 16 = 9, one shared slot, because slide 16 is taught while the agent runs (about 4 min run, 7 min cutoff, + 2 min to open the results); quiz 17 = 3. 3 + 9 + 3 = 15. Slide 15's tag reads "Time · 9 min" to match.

Arithmetic: the old plan was 10 + 20 + 45 + 50 + 35 + 20 = 180. Cutting the slide-6 quiz takes Workflows 20 → 15 (−5); the demo replaces Run 3, 35 → 15 (−20). That frees 25 min. Builder's call, open to change: break +10, Run 2 +10, Q&A +5. New total 10 + 15 + 45 + 10 + 60 + 15 + 25 = 180.
