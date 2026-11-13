# Day 3 · Session 2 deck v3 — design (outline → copy → deck)

Status: draft for approval · 2026-11-12
Input: `docs/reviews/2026-11-12-day3-s2-review.md` (synthesis of 3 independent gpt-6.1-sol reviews: material, storyline, visual). Finding IDs (P0-1, P1-3, P2-7 …) refer to that report.
Source deck: `decks/day3-s2.html` (24 slides, `data-n` 1…21 with 8a/8b/10a/10b/16a/16b). Output deck: `decks/day3-s2-v3.html`.
Reference for style, vocabulary and safety routine: `decks/day3-s1-v3.html` and its spec `docs/superpowers/specs/2026-11-12-day3-s1-v3-deck-design.md`.
Tags: *(user)* = decided by the owner · *(call)* = coordinator's call, correctable.

---

## 1. Intent

Session 2 upgrades the participants' Session 1 app: a database that keeps prices, a watchlist, and a chatbot that answers from official OJK/IDX pages. The v2 deck looks good and renders cleanly, but the review found that it (a) promises results its own prompts never ask for (dashboard follows watchlist, saved-data label), (b) describes the system prompt and the Wiki as guarantees, which is misleading for bank staff, (c) drops the safety routine Session 1 v3 teaches the same morning (read commands, review files before push), and (d) has no worked example and puts the source check after the push. The audience is bank business users with no coding background. The owner's top rule: **no misleading or ambiguous content or knowledge.**

v3 is rebuilt the way S1 v3 was: new outline, new copy, then the deck *(user: approach B)*. It keeps the three-run chain, the NISP example, the S1 visual style, the recap split and the Session 3 preview.

## 2. Goals, non-goals, anti-goals

**Goals**
- Every P0 and P1 finding in the review report is resolved; every P2/P3 finding is resolved or listed in §10 with a reason.
- Every result a run tells participants to check is explicitly requested by a prompt in that run (or an earlier one).
- The system prompt and the Wiki are described as guidance that must be tested, never as guarantees.
- Same workflow names, permission routine and two-step push as S1 v3.
- One presenter worked example before Run 1 and one before Run 3.
- Persistence after restart and an out-of-scope "I don't know" answer are both tested in a run.

**Non-goals**
- No new visual style, fonts or deck engine.
- No change to the S1 or S3 decks (follow-ups in §10).
- No end-to-end rehearsal of the runs, handout, recovery card, fallback data or checkpoint hosting. These are delivery blockers (§10).

**Anti-goals** (failure even if the deck "works")
- Replacing one absolute claim with another ("the Wiki makes answers correct", "checking the URL proves the rule is current").
- A copyable prompt that contains a placeholder (a URL, name or value the facilitator must fill in before class), or a "Copy" button that copies text different from what the slide shows. Exception: the one **fill-in template**, the fix prompt (§8.0 P-FIX), whose `[ … ]` brackets the participant replaces; its box is labelled `Fill in the brackets before sending`.
- Meeting the word budget by shrinking the type.
- Any wording that suggests the chatbot gives approved advice or is compliance-checked.

## 3. Constraints

- `AGENTS.md` deck rules: assertion titles (quiz questions go in the body), ≤ 40 visible words per reveal step on teaching slides, ≤ 60 on run slides, with **every** copyable prompt box excluded as a declared exception (one line per slide in the report), never shrink type, per-slide word-count report.
- One self-contained HTML file, same runtime as S1 v3: `[data-step]` click reveals, `.choices` reveal on quiz slides, speaker notes in `#notes-data` JSON keyed by `data-n`, ← undoes a reveal, 1920×1080 stage.
- No visible text under 28 px at 1920×1080, prompt boxes included (v2 `.prompt.sm` at 26 px goes).
- Motion: as in S1 v3 — loops run 3 times then settle; continuous loops only where repetition is the concept (none in S2 except the Q&A drifting shapes, owner's design) and text carets. All motion covered by `prefers-reduced-motion`.
- 180 minutes, no break.
- All S2 prompts are UNTESTED. Notes mark each one `[UNTESTED]` and `prompts/s2.md` lists them.

## 4. Approaches

| | Approach | Trade-off |
|---|---|---|
| A | Patch the 24 slides in place | Fast; cannot add the worked examples or split dense run slides |
| **B** | **New v3: outline → copy → deck** *(user, picked)* | Fixes everything; follows the AGENTS.md story gate; most work |
| C | Patch now, v3 later | Safe deck sooner; run slides edited twice |

Other owner decisions:
- **The dashboard follows the watchlist** *(user)*: the Run 2 spec states it; Run 2's browser test and the bug-report quiz stay.

## 5. Decisions that apply deck-wide

### 5.1 Workflow names *(call, matches S1 v3)*
**Interview → Plan → Execute → Test / Debug → Iterate.** Interview produces the spec update (`docs/spec.md`); Plan carries the `Approve / Edit / Reject` chip. Run-slide "you are here" chips use only these five names. Notes: "Same five steps as this morning, once per feature." "Brainstorm" may appear only as the skill name or inside a prompt ("Let's brainstorm…" is how the interview starts).

### 5.2 Recovery *(call, matches S1 v3)*
No copyable recovery prompt on any slide. Every "Stuck?" line reads `Stuck? Raise your hand — we move you to checkpoint <name>.` The recovery card and links live in the handout (delivery blocker). Notes for each run give a timebox: "At minute N, anyone without the expected result gets help to checkpoint X; don't keep debugging."

Checkpoints: `s1-chatbot` (start), `s2-database` (after Run 1), `s2-watchlist` (after Run 2), `s2-wiki` (after Run 3).

### 5.3 Permission and push routine (copied from S1 v3)
- Run slides that build show: `It asks to run a command? Read it. Installing or starting the app inside financial-app is expected. Anything else? Raise your hand.`
- Every push is two prompts with a human check between:
  1. `List the files you would commit, and point out anything that looks like a key or password. Don't commit or push yet.`
  2. (participant reads the list, stops on `backend/.env` or a key) P-PUSH2 (§8.0), with the run's fixed message.
- Notes: "Key leaked? Tell the facilitator — the key must be replaced." A push saves the participant's work to their GitHub repo; it does **not** create the course checkpoint (P0-5, M8).

### 5.4 Honest-limits wording (P0-4)
- System prompt = "instructions the chatbot should follow; it can still get them wrong, so we test."
- Wiki = "the app sends the matching page with the question; this helps the model use the source, but it can still misread or add things. Open the link and check."
- A visible chip on slides 17 and 23: `Training prototype — not investment advice.`
- "Only use what the page says" = "tells the agent not to fill gaps; you still compare its page with the original."

### 5.5 Vocabulary
As S1 v3: **the model**, **opencode**, **your financial app**, **AI service**, **latest available price** (never "live"). New in S2, each defined once on first use:
- **database** — "a place the app writes down what it must remember. Ours is SQLite, which keeps it in one file, `backend/data/app.db`."
- **ticker** — "the stock's code. `.JK` marks a Jakarta-listed stock on Yahoo Finance: `NISP.JK`."
- **Wiki** — "a folder of short pages the app can send to the model with a question."
- **system prompt** — as S1 v3 slide 6 row 1, but for the chatbot.

Technical prompt sentences carry a label under the box: `Course setup — copy as is; the agent handles the details.`

## 6. v3 slide sequence (headlines) and timing

`data-n` values are sequential 1…27. "From" = v2 `data-n`.

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

Total 180 min. Run slides: 15+20+15+15+15+15+15 = **110 min** (v2: 106). 27 slides (v2: 24).

## 7. Redesigned and new teaching slides

Visible text is on-slide wording; the builder may tighten it if the meaning stays and the budget holds.

### 7.1 Slide 8 — two tables linked by ticker
Left table `stocks`: header `ticker · name · added`; rows `NISP.JK · Bank OCBC NISP`, `BBRI.JK · …` (greyed, "added in Run 2"). Right table `prices`: header `ticker · date · close`; three readable rows `NISP.JK · Mon · 1,150`, `NISP.JK · Tue · 1,155`, `NISP.JK · Wed · 1,160`, tagged `Sample`.
Clicks: 0 stocks table · 1 prices table · 2 `NISP.JK` highlighted in both, connector labelled `Same ticker — one stock, many daily rows` · 3 note `.JK = listed in Jakarta (Yahoo code)`.
Notes: "Our app uses two tables; other designs are possible. The full column list is in the Run 1 spec prompt — you don't need to remember it." No travelling strip.

### 7.2 Slide 9 — free data can fail
Clicks: 0 Yahoo → yfinance → app, label `Free, unofficial, can be slow or limited` · 1 the feed breaks · 2 the database answers instead · 3 page badge `Saved prices · as of 12 Nov` and, beside it, `No saved prices yet → "No data yet — try again later"`.
Notes: "This is why Run 1 saves the prices, and why Run 2's spec asks for the date label. The label tells users the numbers may not be today's." Remove the v2 claim that "every checkpoint ships a cached copy" (unverified). Keep "Yahoo can limit a room of people asking at once" as "may".

### 7.3 Slide 10 — worked example: read one price row
The presenter shows, on the reference app at checkpoint `s2-database`, the agent's answer to the Run 1 "look inside" prompt. Slide shows a still of that answer as a card, tagged `Sample — your numbers will differ`: `Tables: stocks (1 row), prices (~240 rows)` · `Latest NISP.JK row: <date> · close <n>`.
Clicks: 0 card · 1 marker on the date: `Is the date the last trading day?` · 2 marker on the count: `About one row per trading day in a year?` · 3 takeaway `Check the date and the count, not whether the price looks "right".`
The card's numbers are **made-up samples** tagged `Sample` *(user, after spec review r2)*; they do not wait for a real run. Notes: do it live if the reference app is ready; otherwise use the slide card.

### 7.4 Slide 18 — the Wiki
Clicks: 0 user question · 1 the app looks in `wiki/` and picks pages whose words match (`keyword match`) · 2 sends `question + matching page` to the model · 3 answer with the page link · 4 warning chip `The model can still misread the page — open the link.` and a branch: `No matching page → "This Wiki doesn't cover that."`
Notes: §5.4 wording. Never "answers from the page, not from memory".

### 7.5 Slide 19 — official sources
Gate as v2 (two sources pass, others bounce; no green ticks). Step 3 card becomes the page header participants will save: `Title · URL · Last updated (if shown) · Checked on <date>`.
Notes: "An official page can be old, replaced or educational rather than the rule itself. If you can't tell whether it is current, the Wiki page says so. Our Wiki is a training set, not a verified rulebook."

### 7.6 Slide 20 — worked example: check one answer
One question, one illustrative answer, one real source line, tagged `Illustrative`. The builder picks a short, stable fact from a real OJK or IDX investor-education page, quotes the supporting sentence verbatim, and records the URL and date checked in the notes. *(call: builder verifies the page; if no stable page is found, use the OJK "what OJK supervises" description and say so in the report.)*
Clicks: 0 question + answer · 1 source link · 2 the matching sentence on the page, highlighted · 3 three checks `Source shown? · Matches the page? · Says "not covered" when it isn't?`

### 7.7 Slide 24 — quiz (from v2 17)
- Body question: `The chatbot quotes a rule but gives no source. Is that good enough?`
- A `Yes. It sounds right.` · B (correct) `No. Find which page the app sent, open it, and check the rule. No page? Add a checked official page.` · C `No. Switch to a bigger model.`
- Reveal: `B — A regulatory answer needs a source that actually supports it. A link alone is not proof.`
- Notes: asking the chatbot "which page did you use?" can produce an invented page; check the link yourself.

### 7.8 Slide 25 — recap finish check
Add: `Finish check: watchlist survives a restart · answers show a checked source · latest commit on GitHub — or checkpoint s2-wiki.` Keep the three-box split and its notes ("wrong number → database; wrong fact → Wiki; wrong tone or advice → system prompt"), plus "if it gives advice, don't use the answer; fix and retest".

## 8. Run slides

Slides 11–23 run slides are written from this section; v2 slides 8a/8b/10a/10b/16a/16b are reference only.

### 8.0 Shared prompts (quoted once, used by several runs; all UNTESTED)

- **P-PLAN(x)** (Tab: Plan mode): `Read docs/spec.md and give me a numbered step-by-step plan for the x only. Don't build anything yet.` — x = `price database`, `watchlist`, `Wiki`.
- **P-SAVE** (Tab: Build mode, Run 3a only): `Approved. Save that plan to docs/plan.md. Don't build anything yet.`
- **P-PUSH1**: `List the files you would commit, and point out anything that looks like a key or password. Don't commit or push yet.`
- **P-PUSH2(m)**: `Commit those files with the message "m" and push to GitHub.` — m is fixed per run: `Price database`, `Watchlist page`, `Wiki and system prompt`. Each run's Copy button copies the full text with its own message; no placeholder.
- **P-INT2** (Run 2a interview): `Let's brainstorm a watchlist for my financial app. I want to follow NISP, BBRI and TLKM, add or remove stocks myself, and see them on the dashboard. Ask me one question at a time, at most 3, in plain business language. Don't write any code or files yet.`
- **P-INT3** (Run 3a interview): `Let's brainstorm a Wiki for my chatbot: short pages from official ojk.go.id and idx.co.id investor-education pages only, each with its link. Ask me one question at a time, at most 3, in plain business language. Don't write any code or files yet.`
- **P-FIX** (fill-in template, handout and slide 15): `[What I did]. I expected [what should happen], but I saw [what happened]. Explain the cause in plain words, then fix it.`

Each run slide shows: title · time tag · Goal · five-step chip with the current step marked · every prompt listed for that run in §8, one per click step *(user)*: each click reveals the next prompt box with its Copy button and collapses the previous one to a one-line `✓ <step name>` chip, so at most one open prompt box shows at a time; participant check steps without a prompt get their own click · `You should see` · permission line where it builds · `Stuck?` line (§5.2). Prompt text ≥ 28 px. All prompts are new or changed and **UNTESTED**; the quoted text below is authoritative and goes into `prompts/s2.md`.

### Run 1a (slide 11) — Interview, Plan
1. Interview: `Let's brainstorm saving price history for my financial app. It should keep each stock's daily prices in a database, so the app still has them after a restart. Ask me one question at a time, at most 3, in plain business language. Don't write any code or files yet.`
2. Spec: `Add the price database to docs/spec.md. Use SQLite in backend/data/app.db with two tables: stocks (ticker, name, added_at) and prices (ticker, date, open, high, low, close, volume). Keep one row per ticker and date, so refreshing twice adds no duplicates. Store prices as Yahoo gives them, in IDR. POST /api/refresh fills prices from yfinance and returns rows_added. Start with NISP.JK. Don't build anything yet.` — label: course setup.
3. Plan (Tab: Plan mode): `Read docs/spec.md and give me a numbered step-by-step plan for the price database only. Don't build anything yet.` → approve / edit / reject.
You should see: `Up to 3 questions, an updated docs/spec.md, a plan. No database yet.`

### Run 1b (slide 12) — Execute, Test / Debug
1. Build (Tab: Build mode): `Approved. Save that plan to docs/plan.md, then build the price database from it. Fill it with NISP.JK's last year of prices and tell me how many rows were added.`
2. Look inside: `Show me what's inside the database in plain words: each table, how many rows it has, and the latest NISP.JK row. Don't change anything.`
3. Test: `Refresh the prices again and tell me how many rows were added. Don't change anything else.` — expect 0 or a few new days, not a full year.
4. Push: P-PUSH1, then P-PUSH2(`Price database`).
You should see: `Two tables, about one row per trading day, latest NISP row with a recent date; second refresh adds no duplicates.`

### Run 2a (slide 13) — Interview, Plan, Execute
0. Interview: P-INT2.
1. Spec: `Add a watchlist to docs/spec.md. Keep the quote, history and chat endpoints working. New: GET /api/watchlist → [{ticker, name, price, change_pct, price_date}]; POST /api/watchlist {ticker}, which also saves that stock's price history; DELETE /api/watchlist/{ticker}. Prices come from the database. The dashboard shows one price card for each stock on the watchlist, so adding or removing a stock changes the dashboard after a refresh. Show the date of each price. If Yahoo fails, keep showing saved prices labelled "Saved prices as of <date>"; with no saved prices, say "No data yet". Accept IDX tickers ending in .JK only; otherwise say "Enter the IDX ticker, for example NISP.JK" and save nothing. Don't build anything yet.` — label: course setup. (Over budget; exception: copyable spec.)
2. Plan: P-PLAN(`watchlist`) → approve / edit / reject.
3. Build (after the plan is approved): `Approved. Save that plan to docs/plan.md, then build the watchlist from it. Then tell me how to open the watchlist page.`
Permission line. You should see: `Up to 3 questions, an updated spec, an approved plan, then a watchlist page with NISP and its price date; the dashboard shows a NISP card.`
*(call)* `change_pct` = change against the previous trading day's close; stated in the notes, not the slide.

### Run 2b (slide 14) — Test / Debug, Iterate
Steps on the page (no prompt needed):
1. `Add BBRI.JK, then TLKM.JK.` → each appears on the watchlist and the dashboard, with history.
2. `Type NISP (no .JK).` → `Enter the IDX ticker…`; nothing saved.
3. `Remove BBRI.JK. Refresh the dashboard.` → its card is gone. *(call: remove BBRI, not TLKM, so NISP and TLKM history stay for Session 3, which reruns on TLKM.)*
4. `Stop the back end, start it again, reopen the app.` → watchlist and prices still there (P1-2).
5. Push: P-PUSH1, then P-PUSH2(`Watchlist page`).
If a step fails: P-FIX.

### Run 3a (slide 21) — record, Interview, Plan
1. In the browser, ask the chatbot and write down each answer: `What does OJK supervise?` · `What is an auto-rejection limit on IDX?` · `What should I check before investing in a stock?` (title calls them "three answers", not "three OJK questions"; "Baseline" is not used — P2-3).
2. Interview: P-INT3.
3. Spec: `Add a Wiki to docs/spec.md: Markdown pages in wiki/, one page per official page, from ojk.go.id or idx.co.id only. Each page starts with its title, URL, last-updated date if the page shows one, and the date we checked it. For each question, the back end picks matching Wiki pages by keyword and sends them with the question. If no page matches, the chatbot says the Wiki doesn't cover it. I'll write the system prompt. Don't build anything yet.` — label: course setup.
4. Plan: P-PLAN(`Wiki`), then P-SAVE.
You should see: `Three answers written down, an updated spec, a saved plan. No Wiki yet.`

### Run 3b (slide 22) — Execute (find and build)
Card labels describe what the copied prompt does (P1-7).
1. Find pages: `Find official investor-education pages on ojk.go.id and idx.co.id that explain what OJK supervises, what an auto-rejection limit is, and what to check before investing. For each, give the URL, the page title, the last-updated date if shown, and a one-line summary. Don't save anything yet.`
2. Participant check (no prompt): `Every address on ojk.go.id or idx.co.id? Open each one. Drop anything else.`
3. Build: `Turn the pages I approved into Wiki pages in wiki/, one Markdown file per page, with the header from the spec. Only use what the page says. Then connect the Wiki to the chatbot as the plan says.`
Notes: facilitator setup — webfetch works by default; `OPENCODE_ENABLE_EXA=1` adds web search (the `docs/project-log.md` entry "S2 copy v2 written" records it working in opencode 1.19.5 with no key; re-check in rehearsal). Fallback: the handout's verified URL list *(delivery blocker)*. Timebox: at minute 10 with no pages, use the handout list.

### Run 3c (slide 23) — Test / Debug, Iterate, push
1. System prompt: `Set the chatbot's system prompt to: You answer questions about Indonesian stocks for business users, using the Wiki pages and the app's data that come with each question. Give the Wiki page URL you used. If they don't cover the question, say so. If asked what to buy or sell, give facts and risks only, no recommendation.`
2. Check (on slide, before push): `Ask the same three questions. For each answer: open the link · find the sentence that supports it · fix and re-ask if it doesn't.`
3. Two more tests: `What is our bank's limit for staff share trading?` → says the Wiki doesn't cover it. `Should I buy NISP?` → facts and risks, no recommendation; if it recommends, don't use the answer, tighten the system prompt, retest.
4. Push: P-PUSH1, then P-PUSH2(`Wiki and system prompt`).
Prototype chip (§5.4). You should see: `Each answer links a Wiki page that supports it; "not covered" for the staff question; no recommendation.`

## 9. Animation and code fixes (deck-wide)

- Loops: reuse S1 v3 (`animation-iteration-count:3`, then settle) for `packet`, `pulse`, `flow`, `float` (P2-7).
- Arrow `.draw` paths inside a `[data-step]` group draw when that group gets `.in`, not on slide entry (P2-8).
- Unrevealed `[data-step]` containers are `inert`; the key handler ignores Space/Enter/arrows when focus is on a button, link or form field (P2-9). Port the same fix to nothing else (S1/S3 out of scope; §10).
- Reduced motion: transfer dots and delayed cards show in their final position with no delay (P2-10).
- Slide 7 column highlight sits inside the grid (P3-1).
- Render check: every slide at every step, 1920×1080 and 1280×720, no overflow, no text < 28 px, each step visibly changes something.

## 10. Related documents

To create or update in this work:
- `docs/outlines/day3-s2-v3.md` — headline list from §6 with a "changes from v2" header.
- `docs/copy/day3-s2-v3.md` — visible text, build steps, notes and handout blocks for all 27 slides, plus the AGENTS.md word-count report.
- `prompts/s2.md` — new file; every prompt in §8 and the handout under an "UNTESTED (v3)" heading.
- `tools/deck-check/` — make the lint usable for S2 (deck-specific banned list, workflow names, tested-prefix list) without changing its S1 results. S2 banned list: `[CHECKPOINT URL]`, `Replace my project`, `answers from the page, not from memory`, `stops the agent from filling gaps`, `learns the rules`, `allow them`, `must always`, `never tells anyone`, `cached copy`, `Baseline`, whole-word `live` (same exception as S1), and `brainstorm` on workflow chips.
- `docs/superpowers/specs/2026-11-11-day3-design.md` (find by content, not line number): the "Build method" paragraph gets one sentence "From S1 v3 on, the decks name the steps Interview → Plan → Execute → Test / Debug → Iterate"; the recovery sentence "Replace my project with checkpoint …" → "the facilitator moves you to the checkpoint"; the `s2-watchlist` checkpoint row adds "dashboard shows one card per watchlist stock".
- `docs/project-log.md` — one entry for the review, one for the build.

Follow-ups, **not** in this work:
- S3 deck still says "brainstorm, spec, plan, build, test" and assumes TLKM history; align it to §5.1 next.
- Embedding fonts for offline laptops (P3-2) applies to all three decks; test with the network off before class.
- The S1 v3 deck has the same focus/Space bug (P2-9).

Delivery blockers (before class, outside the deck):
- Rehearse every UNTESTED prompt end to end on Windows and Mac, including webfetch/websearch and GitHub sign-in (P0-6).
- Host checkpoints `s1-chatbot`, `s2-database`, `s2-watchlist`, `s2-wiki` with saved NISP/BBRI/TLKM prices; write the recovery card and the verified OJK/IDX URL list for the handout.

## 11. How we check it (acceptance)

1. Render every slide at every step at both sizes: no overflow, no text < 28 px, every step changes something; no JS errors.
2. Lint (§10 banned list) passes; workflow chips show only the five names.
3. Contract check: for every `You should see` and test step in §8, a prompt in the same or an earlier run asks for it.
4. Every Copy button copies exactly the visible prompt text, and that text equals `prompts/s2.md`.
5. Word-budget report per slide with exceptions named.
6. Timing sums to 180.
7. An independent read-only review (material, storyline, visual lenses) of `day3-s2-v3.html` finds no P0.

## 12. Left to the builder

- Coordinates, sizes, easing; reuse S2 v2 and S1 v3 CSS classes and helpers.
- Fine wording within budgets, without changing meaning in §5–8.
- Whether to edit by fragments or directly in the single HTML file.
- Sample numbers on slides 8 and 10 (must carry `Sample`).

## Review Decisions

- Run slides show every prompt on the slide, one open box per click, earlier ones collapsed to ✓ chips *(user, after spec review r1)*; the handout repeats them but is not the only source.
- Slide 10 card numbers are made-up samples tagged `Sample` *(user, after spec review r2)*.
- Spec review r2 ended NOT READY; owner chose "fix and approve as is". Fixed: Run 2a order, slide 10 samples, design-doc edits located by content, all prompt boxes are budget exceptions.
- P-FIX is the single fill-in template allowed to contain `[ … ]` brackets (§2, §8.0).
