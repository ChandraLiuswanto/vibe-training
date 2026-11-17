# Day 3 · Session 2 — outline v3 (review fixes, worked examples, safer wording)

Source: spec `docs/superpowers/specs/2026-11-12-day3-s2-v3-deck-design.md` §6 (headlines copied verbatim).
Input deck: `decks/day3-s2.html` (24 slides). Output deck: `decks/day3-s2-v3.html` (renamed to `decks/day3-s2.html` on merge; v2 kept as `tools/deck-check/fixtures/day3-s2-v2.html`) (27 slides, `data-n` 1…27).
Finding IDs (P0-1, P1-3, P2-7 …) refer to `docs/reviews/2026-11-12-day3-s2-review.md`. "From" = v2 `data-n`.

## Slide sequence and timing

| # | Headline (assertion title) | From | Change | Min |
|---|---|---|---|---|
| **Opening** | | | | **10** |
| 1 | Upgrade your Financial App: watchlist and AI knowledge | 1 | none | 1 |
| 2 | Today your app saves prices and your chatbot answers from official pages | 2 | title (P1-5); notes "latest available price", drop "never tells anyone" → "is told not to recommend; we test it" | 4 |
| 3 | Same five steps as this morning, once for each new feature | new | five-step strip (§5.1) with three run brackets: Run 1 database, Run 2 watchlist, Run 3 Wiki | 2 |
| 4 | Keep your Session 1 app if it works; otherwise we move you to checkpoint s1-chatbot | 3 | no copy prompt (§5.2); 3-item check: both servers start · NISP loads · chatbot replies | 3 |
| **Why an app needs memory** | | | | **20** |
| 5 | Your app keeps prices only while the back end is running | 4 | title precise; v2 animation kept | 3 |
| 6 | A database keeps what the app must remember, in tables of rows and columns | 5 | notes: "Ours is SQLite, one file" (P2-1) | 4 |
| 7 | A row holds one record; a column holds one kind of value | 6 | assertion title; question + choices in body (P2-5); highlight aligned to grid (P3-1) | 3 |
| 8 | Our app uses two tables, linked by the ticker | 7 | redesign §7.1 (P1-8, P2-1) | 3 |
| 9 | Free Yahoo data can fail, so the app shows saved prices and their date | 9 | **moved before Run 1** (P0-3); §7.2 | 3 |
| 10 | Worked example: read one saved price row and check its date | new | presenter demo §7.3 (P1-3) | 4 |
| **Run 1 — Save prices** | | | | **35** |
| 11 | Run 1a: interview for the price database, update the spec, approve the plan | 8a | §8 Run 1a | 15 |
| 12 | Run 1b: build the database, look inside, refresh twice, push safely | 8b | §8 Run 1b | 20 |
| **Run 2 — Watchlist** | | | | **35** |
| 13 | Run 2a: spec, plan and build a watchlist the dashboard follows | 10a | §8 Run 2a (P0-2, P0-3, P1-10) | 15 |
| 14 | Run 2b: test it like a user, including a restart, then push | 10b | §8 Run 2b (P1-2) | 15 |
| 15 | A useful bug report says what you did, what you expected and what you saw | 11 | assertion title; v2 choices and answer B kept; question in body | 5 |
| **Why the chatbot needs knowledge** | | | | **20** |
| 16 | The model's training is not a reliable source for current rules | 12 | title + notes (P1-5): "may be incomplete or out of date; our app adds data and reference text to each request; the model is not retrained" | 3 |
| 17 | The system prompt tells the chatbot its role and rules, and we test that it follows them | 13 | §5.4; "must always" → "should"; prototype chip | 4 |
| 18 | A Wiki lets the app send matching official text with each question | 14 | §7.4 (P0-4) | 4 |
| 19 | Only OJK and IDX pages go in, each with its link and the date you checked it | 15 | §7.5 (P1-4) | 4 |
| 20 | Worked example: check one answer against its source page | 18 (replaces) | presenter demo §7.6 (P1-3); v2 placeholder before/after slide removed | 5 |
| **Run 3 — Teach the chatbot** | | | | **45** |
| 21 | Run 3a: record three answers, then interview and plan the Wiki | 16a (ref) | §8 Run 3a | 15 |
| 22 | Run 3b: find official pages, check each one, build the Wiki | 16a/16b (ref) | §8 Run 3b (P1-7) | 15 |
| 23 | Run 3c: set the system prompt, check answers against their pages, then push | 16b | §8 Run 3c (P1-1) | 15 |
| **Close** | | | | **15** |
| 24 | A regulatory answer needs a source you can open and check | 17 | quiz §7.7 (P1-6) | 4 |
| 25 | Data lives in the database, knowledge in the Wiki, behaviour in the system prompt | 19 | recap kept; add finish check §7.8 | 4 |
| 26 | Questions | 20 | none; notes: check pushes, not "investment questions neutral" only | 6 |
| 27 | Next session: turn your data into a report and a deck | 21 | notes use five step names | 1 |

180 min · run 110

## Changes from v2

- **Honest limits (P0-4, P1-5):** the system prompt and the Wiki are described as guidance that must be tested, not guarantees; no "learns the rules", "must always", "never tells anyone", "answers from the page, not from memory". Prototype chip on slides 17 and 23.
- **Results the prompts ask for (P0-2, P0-3, P1-10):** every result a run says to check is requested by a prompt in that run or an earlier one (dashboard follows the watchlist, saved-prices date label, `.JK`-only tickers).
- **Same safety routine as Session 1 (P0-5):** read each command, list files before every push, two-step push.
- **Recovery (P0-1):** no copyable recovery prompt and no placeholder URL; the facilitator moves you to a checkpoint.
- **Worked examples (P1-3):** new slides 10 and 20, one before Run 1 and one before Run 3.
- **Persistence and "I don't know" tested (P1-1, P1-2):** restart check in Run 2b; out-of-scope question in Run 3c, before the push.
- **Source discipline (P1-4, P1-6):** page header records title, URL, last-updated date and date checked; quiz answer says to check the page the app supplied.
- **Design fixes (P1-8, P2-1, P2-5):** two tables linked by a readable ticker; "Our app uses…" instead of universal claims; assertion titles and questions in the body.
- **Method names (P1-9):** Interview → Plan → Execute → Test / Debug → Iterate, as in Session 1 v3; new slide 3.
- **Run slides (P1-7, P2-4, P2-6):** prompts shown one open box per click; cards labelled by what the prompt does; notes carry timeboxes.
- **Order (P0-3):** the Yahoo-failure slide moves before Run 1 so the saved-prices label has a reason.
- **Motion and code (P2-7 to P2-10, P3-1):** loops run 3 times, arrows draw when revealed, hidden buttons inert, reduced-motion fixes, aligned highlight.
