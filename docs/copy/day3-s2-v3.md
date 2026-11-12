# Day 3 · Session 2 — slide copy v3 (review fixes, worked examples, 27 slides)

Course: AI Vibe Coding for Business Users · Session 2: Watchlist & AI knowledge · 3 hours, no break · English deck, speaker-led and hands-on.
Sources: `docs/outlines/day3-s2-v3.md` (27 headlines from spec §6, kept word for word), spec `docs/superpowers/specs/2026-11-12-day3-s2-v3-deck-design.md` (§5 deck-wide wording, §7 redesigned slides, §8 runs), `docs/copy/day3-s2-v2.md` and the notes in `decks/day3-s2.html` (v2 text reused where still correct), `docs/reviews/2026-11-12-day3-s2-review.md` (finding IDs P0-1 … P3-2).
This file holds slides 1–27, the contract check and the word-count table.

How to read this file:
- Ids are the v3 `data-n` values, in deck order.
- `visible:` is the on-slide text. Every label the diagram shows is listed in `visible:`; the `diagram:` line says where it goes.
- `build:` lists the click steps. Step 0 is what shows when the slide arrives. Unless a step says "replaces", text stays on screen once revealed.
- `words:` is the largest number of visible non-title words on screen at any one step, counted as AGENTS.md says: split on spaces, so stand-alone separators such as `·`, `→`, `—` count as words when they are shown. Table cells are written with `·` between them in this file only; the deck shows each cell as its own grid cell with no `·` glyph, and the count does not include those separators. Quiz choices are listed in `visible:` but not counted, with the reason in `exception:`.
- Budgets (AGENTS.md): 40 per reveal step on teaching slides, 60 on run and check slides.
- `status: UNTESTED` means a prompt has not been run in opencode; rehearse it before class. Every S2 prompt is UNTESTED.
- Vocabulary (spec §5.5): "the model" · "opencode" · "your financial app" · "AI service" · "latest available price". New in S2, defined once on first use: database (slide 6), ticker and `.JK` (slide 6 notes; `.JK` again on slide 8), Wiki (slide 18), system prompt (slide 17).
- Workflow names, exactly: Interview → Plan (Approve / Edit / Reject) → Execute → Test / Debug → Iterate.
- Sample numbers in diagrams are made up, tagged `Sample`, and are not real NISP prices.

## 1. Upgrade your Financial App: watchlist and AI knowledge
type: title
block: Opening · 1
visible:
Day 3 · Session 2
AI Vibe Coding for Business Users
diagram: none
build:
  0: title, subtitle and session line together
notes:
Welcome back. In Session 1 you built a NISP dashboard and a chatbot by directing opencode, and you may have saved it on GitHub. This session upgrades that same app in two ways. First, it gets a memory: a database that keeps prices, and a watchlist of the stocks you follow. Second, the chatbot gets reference text: a small Wiki built from official Indonesian pages, and a system prompt that you set and test. The method is the same as this morning: Interview, Plan, Execute, Test / Debug, Iterate. Before we start, check that opencode opens on every laptop and that your app from Session 1 still starts. Anyone whose app does not start, raise your hand now; the next slides show what happens then.
words: 11 · budget: 40 · exception: none
status: n/a

## 2. Today your app saves prices and your chatbot answers from official pages
type: visual
block: Opening · 4
visible:
Your app from Session 1
Database: price history
Watchlist: NISP · BBRI · TLKM
Wiki: OJK and IDX pages
Shows its source link
diagram: Centre: a laptop browser frame "Your app from Session 1" showing the small dashboard and chat panel. Below it a cylinder icon "Database: price history" plugs into the frame with a short connector. To the right of the dashboard a narrow list card "Watchlist: NISP · BBRI · TLKM" slides in. Next to the chat panel a book icon "Wiki: OJK and IDX pages" opens. A speech bubble from the chat panel ends with a small link chip: "Shows its source link".
build:
  0: the browser frame with the Session 1 app
  1: the database cylinder plugs in under the frame; the three watchlist rows fill one by one
  2: the book icon opens beside the chat panel
  3: the chat bubble with the source chip appears; the book and bubble pulse three times, then settle
notes:
Say what the session produces. On step 0: this is the app you have now. It shows the latest available price for NISP from Yahoo Finance, and the chatbot answers from that data. On step 1: today it gets a database, a file that keeps every day's price, so the app remembers. On that database we build a watchlist: NISP, plus BBRI and TLKM, which you add yourself, and you can remove one. On step 2: the chatbot gets a Wiki, a few pages saved from the official OJK and IDX websites. On step 3: the app sends the matching page along with the question, and the chatbot is asked to show the page link. The model can still misread a page, so you open the link and check it. Three runs today, each building on the last. As before, the app shows data and facts only. The chatbot is told not to recommend what to buy or sell; we test that, we don't assume it. This is a training prototype, not investment advice.
words: 23 · budget: 40 · exception: none
status: n/a

## 3. Same five steps as this morning, once for each new feature
type: visual
block: Opening · 2
visible:
Interview
→ docs/spec.md
Plan
Approve / Edit / Reject
Execute
Test / Debug
Iterate
Run 1 database
Run 2 watchlist
Run 3 Wiki
diagram: Five square boxes in a row joined by right arrows: "Interview", "Plan", "Execute", "Test / Debug", "Iterate" (these five are the `.wf` workflow names). Under "Interview", small text "→ docs/spec.md". Under "Plan", a chip "Approve / Edit / Reject". A red return arrow runs from the top of "Iterate" back to the top of "Plan" (same style as the S1 v3 strip). Under the row, three full-width brackets stacked one below the other, each spanning all five boxes: "Run 1 database", "Run 2 watchlist", "Run 3 Wiki".
build:
  0: five grey boxes
  1: "Interview" and "Plan" light up in turn; "→ docs/spec.md" appears under Interview; the "Approve / Edit / Reject" chip pops under "Plan"
  2: "Execute", "Test / Debug" and "Iterate" light up; the return arrow from Iterate back to Plan draws once
  3: the three run brackets appear one after the other
notes:
Same five steps as this morning, once per feature. You do the whole strip three times today: Run 1 saves prices in a database, Run 2 builds the watchlist, Run 3 teaches the chatbot from a Wiki. On step 1: Interview. The agent asks questions one at a time, you answer, and it writes what you agreed into docs/spec.md. Then Plan: the agent proposes numbered steps, and you approve, edit or reject them before anything is built. On step 2: Execute, the agent builds. Test / Debug: you check the result in the browser and, if something breaks, find the cause with the agent. Iterate: you ask for a change, which takes you back to Plan. On step 3, say the three runs. Nothing is built until Execute. "Brainstorm" is the name of the skill and the word our first prompt uses to start the interview; on the slides the step is called Interview. Each run slide shows these five names with a "you are here" marker.
words: 23 · budget: 40 · exception: none
status: n/a

## 4. Keep your Session 1 app if it works; otherwise we move you to checkpoint s1-chatbot
type: talk
block: Opening · 3
visible:
Your app works? Keep it.
Both servers start
NISP loads
Chatbot replies
Stuck? Raise your hand — we move you to checkpoint s1-chatbot.
diagram: none. Three check lines with empty tick boxes under the first line; the stuck line at the bottom.
build:
  0: the first line and the three checks
  1: the stuck line
notes:
Everyone starts this session from a working Session 1 app. On step 0: if both servers start, the NISP price loads at localhost:5173 and the chatbot replies to a simple question, keep your app; you are ready. On step 1: if one of these fails, or you missed part of Session 1, raise your hand. We move you to checkpoint s1-chatbot, our reference version of the Session 1 app. There is no recovery prompt to copy; the facilitator does the move and the recovery card is in the handout. Your own work stays on GitHub if you pushed it. Timebox: at minute 3, anyone whose app does not pass the three checks is moved to s1-chatbot; don't keep debugging. Every "Stuck?" line today works the same way, with a different checkpoint name. Before class, check that the checkpoint is available for everyone.
words: 23 · budget: 40 · exception: none
status: n/a

## 5. Your app keeps prices only while the back end is running
type: visual
block: Why an app needs memory · 3
visible:
Page shows NISP
Server restarts
Nothing kept
Fetch it all again from Yahoo
Today: no saved history. No list of stocks you follow.
diagram: A loop of four boxes, left to right then back: a browser "Page shows NISP" with a small chart; a power icon "Server restarts"; an empty grey box with a dashed outline "Nothing kept"; a cloud "Fetch it all again from Yahoo" with an arrow back to the browser. Caption under the loop is the last line of visible.
build:
  0: the browser box with the chart
  1: "Server restarts": the chart and numbers fade out of the browser box
  2: "Nothing kept" empty box appears
  3: arrow to the Yahoo cloud and back to the browser; caption appears in accent colour (the arrow pulses three times, then settles)
notes:
Start with what the app does today. On step 0: the page shows NISP, with prices fetched from Yahoo Finance. On step 1: stop the back end, or close the laptop, and start it again. On step 2: nothing was kept. The back end held the prices only while it was running. On step 3: when it starts again, it has to ask Yahoo for everything. Two problems follow. If Yahoo is slow or limits us, the page has nothing to show. And the app cannot remember anything you chose, like which stocks you want to follow. Ask the room: where does your own business keep things it must not forget? Spreadsheets, a customer system, a ledger. An app needs the same: a place to write things down. That place is a database.
words: 23 · budget: 40 · exception: none
status: n/a

## 6. A database keeps what the app must remember, in tables of rows and columns
type: visual
block: Why an app needs memory · 4
visible:
Database: where the app writes down what it must remember
backend/data/app.db
Table: prices
ticker · date · close
NISP.JK · Mon · 1,150
NISP.JK · Tue · 1,155
NISP.JK · Wed · 1,160
Sample
Row
Column
diagram: A file icon "backend/data/app.db" at top left, with the definition line above it. From the file, a spreadsheet-like grid "Table: prices" with three column headers "ticker · date · close" (separate cells). Three rows below. A small grey tag "Sample" in the corner of the grid. Labels "Row" (beside one row) and "Column" (above one column), in two colours.
build:
  0: the definition line and the file icon "backend/data/app.db"
  1: the empty grid with the three column headers
  2: the three rows fill in one at a time, top to bottom; the "Sample" tag appears
  3: one row highlights with the label "Row", then one column with the label "Column"
notes:
A database is a place the app writes down what it must remember. Ours is SQLite, which keeps it in one file, app.db, in the back end folder. Other databases are set up differently; this is how our app does it. On step 1: a database holds tables. This one is called prices, and its columns say what we store: the ticker, the date and the closing price. The ticker is the stock's code; .JK marks a stock listed in Jakarta, in the codes Yahoo Finance uses: NISP.JK. On step 2: each row is one record, here one day for NISP. Point at the Sample tag: these numbers are made up for the picture, not real prices. On step 3: the two words to keep are row, one record, and column, one kind of value. You don't need to open the file yourself. Today you ask the agent to look inside it and tell you in plain words.
words: 28 · budget: 40 · exception: none
status: n/a

## 7. A row holds one record; a column holds one kind of value
type: check
block: Why an app needs memory · 3
visible:
In this price table, which is a row and which is a column?
ticker · date · close
NISP.JK · Mon · 1,150
NISP.JK · Tue · 1,155
Sample
A. A row is one day for one stock; "close" is a column.
B. "close" is a row; each day is a column.
C. Rows and columns are the same thing.
A — A row is one record; a column is one kind of value, like the closing price.
diagram: The question at the top. Under it the small sample grid from slide 6 (header row plus two rows, separate cells) with the grey "Sample" tag. The three choices below it in a `.choices` block. The column highlight sits inside the grid's own bounds (P3-1).
build:
  0: the question and the grid
  1: the three choices appear
  2: A highlights green; the Tuesday row and the close column highlight inside the grid; B and C fade; the reveal line appears
notes:
Read the question aloud and point at the grid. Give the room twenty seconds, then take a show of hands for A, B and C. Many people mix the two up, so do not rush. Click to reveal. A is right: a row runs across and holds one record, here NISP on Tuesday. A column runs down and holds one kind of value, here the closing price for every day. B swaps them; if someone chose B, trace one row with your finger, then one column. C is never right. Remind everyone that the numbers are samples. Then ask one person: if we add BBRI tomorrow, do we get new rows or a new column? Answer: new rows, one per day, with BBRI.JK in the ticker column.
words: 41 · budget: 60 · exception: quiz choices (A, B, C) are not counted; the 41 = question (13) + grid and Sample tag (10) + reveal line (18)
status: n/a

## 8. Our app uses two tables, linked by the ticker
type: visual
block: Why an app needs memory · 3
visible:
stocks
ticker · name · added
NISP.JK · Bank OCBC NISP
BBRI.JK · Run 2
prices
ticker · date · close
NISP.JK · Mon · 1,150
NISP.JK · Tue · 1,155
NISP.JK · Wed · 1,160
Sample
Same ticker — one stock, many daily rows
.JK = listed in Jakarta (Yahoo code)
diagram: Two table cards side by side, cells as grid cells. Left card "stocks": header "ticker · name · added"; row "NISP.JK · Bank OCBC NISP"; a greyed row "BBRI.JK" with a small tag "Run 2" (the tag stands for "added in Run 2"). Right card "prices": header "ticker · date · close"; three readable rows; a grey "Sample" tag. On click 2 the `NISP.JK` cell in the left card and the three `NISP.JK` cells on the right highlight, joined by a connector labelled "Same ticker — one stock, many daily rows". No travelling strip.
build:
  0: the "stocks" table
  1: the "prices" table slides in
  2: `NISP.JK` highlights in both tables; the connector and its label draw
  3: the note ".JK = listed in Jakarta (Yahoo code)" appears
notes:
Our app uses two tables; other designs are possible. On step 0: the first table, stocks, is the list of stocks the app follows. Today it has NISP; BBRI is greyed because you add it in Run 2. On step 1: the second table, prices, holds one row for each stock for each day. These prices are made up, tagged Sample. On step 2: the ticker links them. A ticker is the stock's code. Every row in prices says which stock it belongs to by repeating that code, so one stock has many daily rows. On step 3: the .JK ending marks a stock listed in Jakarta, in the codes Yahoo Finance uses: NISP.JK. The full column list, including open, high, low and volume, is in the Run 1 spec prompt. You don't need to remember it.
words: 40 · budget: 40 · exception: none
status: n/a

## 9. Free Yahoo data can fail, so the app shows saved prices and their date
type: visual
block: Why an app needs memory · 3
visible:
Yahoo Finance
yfinance
Your app
Free, unofficial, can be slow or limited
Feed breaks
The database answers instead
Saved prices · as of 12 Nov
Sample
No saved prices yet → "No data yet — try again later"
diagram: Left: a cloud "Yahoo Finance". A line runs through a small connector chip "yfinance" to the box "Your app" on the right; a label above the line reads "Free, unofficial, can be slow or limited". Later the line breaks with the label "Feed breaks". A cylinder icon in front of the app, labelled "The database answers instead". In the corner of the app's page, a badge "Saved prices · as of 12 Nov" with a tiny "Sample" tag, and beside it a second badge with the empty-database message.
build:
  0: Yahoo cloud → yfinance → your app, with the label "Free, unofficial, can be slow or limited"; data flows along the line three times, then settles
  1: the line breaks; "Feed breaks" appears
  2: the database cylinder rises in front of the app; "The database answers instead" appears
  3: the badge "Saved prices · as of 12 Nov" (with "Sample") and, beside it, the message "No saved prices yet → "No data yet — try again later""
notes:
Before Run 1, one honest point about the data. On step 0: our prices come from Yahoo Finance through yfinance, a free tool maintained by volunteers. It is not an official Yahoo product. On step 1: it can be slow or limited, Yahoo may limit a room of thirty people asking at once, and the data can change without notice. On step 2: the database you build in Run 1 is what the app falls back on. On step 3: when the app shows saved prices it says so, with the date, so users know the numbers may not be today's. If the database has nothing yet, the app says "No data yet" rather than showing a blank page. This is why Run 1 saves the prices, and why Run 2's spec prompt asks for the date label. The date in the badge is a sample. Ask: why does the date matter for a business user? Because old numbers shown as if they were current can mislead people.
words: 37 · budget: 40 · exception: none
status: n/a

## 10. Worked example: read one saved price row and check its date
type: demo
block: Why an app needs memory · 4
visible:
Sample — yours will differ
Tables: stocks (1 row), prices (~240 rows)
Latest NISP.JK row: 11 Nov, close 1,160
Is the date the last trading day?
About one row per trading day in a year?
Check the date and the count, not whether the price looks "right".
diagram: A chat-style card showing the agent's answer to the Run 1 "look inside" prompt: header tag "Sample — yours will differ", then the line "Tables: stocks (1 row), prices (~240 rows)" and the line "Latest NISP.JK row: 11 Nov, close 1,160". Marker callouts point at the date and at the row count. At the last click the two markers are replaced by the takeaway line under the card.
build:
  0: the answer card with the tag
  1: a marker on the date: "Is the date the last trading day?"
  2: a marker on the count: "About one row per trading day in a year?"
  3: the two markers fade and are replaced by the takeaway "Check the date and the count, not whether the price looks "right"."
notes:
Presenter demo. Use the reference app at checkpoint s2-database: send the same look-inside prompt as Run 1b ("Show me what's inside the database in plain words: each table, how many rows it has, and the latest NISP.JK row. Don't change anything.") and read the answer with the room. [UNTESTED prompt.] If the reference app is not ready, use the slide card. Its numbers are made-up samples, so say so; yours will differ. Step 1: is the date the last trading day? If it is old, the refresh did not work or Yahoo returned nothing new. Step 2: a year has about 240 trading days, so about 240 rows is plausible, and 3 rows or 3,000 is not. Step 3: the date and the count catch missing or duplicated data. They do not prove that a price is correct, so don't judge by whether it looks right. In Run 1b participants do exactly this, on their own database. The look-inside prompt is the Run 1b one, so it is UNTESTED until rehearsed.
words: 35 · budget: 40 · exception: none
status: UNTESTED

## 11. Run 1a: interview for the price database, update the spec, approve the plan
type: run
block: Run 1 — Save prices · 15
visible:
Goal: interview, update the spec, approve a plan.
Interview · Plan · Execute · Test / Debug · Iterate
Current: Interview
15 min
1. Interview — send:
```text
Let's brainstorm saving price history for my financial app. It should keep each stock's daily prices in a database, so the app still has them after a restart. Ask me one question at a time, at most 3, in plain business language. Don't write any code or files yet.
```
✓ Interview
2. Update the spec — send:
```text
Add the price database to docs/spec.md. Use SQLite in backend/data/app.db with two tables: stocks (ticker, name, added_at) and prices (ticker, date, open, high, low, close, volume). Keep one row per ticker and date, so refreshing twice adds no duplicates. Store prices as Yahoo gives them, in IDR. POST /api/refresh fills prices from yfinance and returns rows_added. Start with NISP.JK. Don't build anything yet.
```
Course setup — copy as is; the agent handles the details.
✓ Update the spec
Current: Plan
3. Plan mode (press Tab) — send:
```text
Read docs/spec.md and give me a numbered step-by-step plan for the price database only. Don't build anything yet.
```
Approve / Edit / Reject
✓ Plan
You should see: Up to 3 questions, an updated docs/spec.md, a plan. No database yet.
Stuck? Raise your hand — we move you to checkpoint s2-database.
diagram: Workflow mini-map (.wf) above one open prompt panel at a time; each finished prompt collapses to a one-line ✓ chip. The mini-map shows Interview for steps 0–1 and Plan from step 2. An Approve / Edit / Reject chip sits under the Plan box. No unattended motion.
build:
  0: goal, mini-map (Current: Interview), time tag, the open Interview box with its Copy button
  1: Interview collapses to a ✓ chip; the Update-the-spec box opens, labelled "Course setup — copy as is; the agent handles the details."
  2: Update the spec collapses; Current: Plan; the Plan box opens ("Plan mode (press Tab)") with the chip Approve / Edit / Reject
  3: Plan collapses to a ✓ chip; the "You should see" line and the Stuck line appear
notes:
[UNTESTED] All three prompts are new and untested; rehearse them in the class opencode build before the session. Same five steps as this morning, now for a database. Timebox 15 minutes. Step 0: send the interview prompt. The agent should ask at most 3 questions, one at a time. Answer in plain words; if you are unsure, say "you decide". Nothing is written yet. Step 1: the spec prompt is technical on purpose; it is course setup, so copy it as is and let the agent handle the details. It names SQLite, the file backend/data/app.db, two tables, one row per ticker and date, and the refresh endpoint. Point at "refreshing twice adds no duplicates": Run 1b tests exactly that. Step 2: press Tab for Plan mode, then send the plan prompt. Read the plan, then approve it, edit it or reject it and ask again. Do not skip this. Step 3: check the expected result: questions asked, spec updated, a plan, and no database yet. At minute 12, anyone without an updated spec and a plan gets help from the facilitator; do not keep debugging. If nothing moves for 2 minutes, press Esc and send the same prompt again.
words: 51 · budget: 60 · exception: prompt boxes (copyable prompts, including the long spec prompt) are not counted; chips and labels are counted
status: UNTESTED

## 12. Run 1b: build the database, look inside, refresh twice, push safely
type: run
block: Run 1 — Save prices · 20
visible:
Goal: build it, look inside, test it, push.
Interview · Plan · Execute · Test / Debug · Iterate
Current: Execute
20 min
1. Build mode (press Tab) — send:
```text
Approved. Save that plan to docs/plan.md, then build the price database from it. Fill it with NISP.JK's last year of prices and tell me how many rows were added.
```
It asks to run a command? Read it. Installing or starting the app inside financial-app is expected. Anything else? Raise your hand.
✓ Build
Current: Test / Debug
2. Look inside — send:
```text
Show me what's inside the database in plain words: each table, how many rows it has, and the latest NISP.JK row. Don't change anything.
```
Two tables? About one row per trading day? A recent latest date?
✓ Look inside
3. Refresh again — send:
```text
Refresh the prices again and tell me how many rows were added. Don't change anything else.
```
Expect 0 or a few new days, not a full year.
✓ Refresh again
4. Check files — send:
```text
List the files you would commit, and point out anything that looks like a key or password. Don't commit or push yet.
```
Read the list. backend/.env or a key in it? Stop and raise your hand.
✓ Check files
5. List clean? Push — send:
```text
Commit those files with the message "Price database" and push to GitHub.
```
Key leaked? Tell the facilitator — the key must be replaced.
You should see: Two tables, about one row per trading day, a recent latest NISP row; a second refresh adds no duplicates.
Stuck? Raise your hand — we move you to checkpoint s2-database.
diagram: Workflow mini-map (.wf) above one open prompt panel at a time; finished prompts collapse to ✓ chips. Current changes from Execute to Test / Debug at step 1. No unattended motion.
build:
  0: goal, mini-map (Current: Execute), time tag, the open Build box with its Copy button and the permission line
  1: Build collapses to a ✓ chip; Current: Test / Debug; the Look-inside box opens with the three things to read
  2: Look inside collapses; the Refresh box opens with "Expect 0 or a few new days, not a full year."
  3: Refresh collapses; the Check-files box opens with the stop line
  4: Check files collapses; the Push box opens with the key-leak line
  5: Push collapses to a ✓ chip; the "You should see" line and the Stuck line appear
notes:
[UNTESTED] Every prompt here is untested; rehearse them first. Timebox 20 minutes. Step 0: confirm Build mode (Tab) and the approved plan, then send the build prompt. Read each command it asks to run: installing or starting the app inside financial-app is expected; anything else, raise your hand. The agent fetches a year of NISP.JK prices from Yahoo, which is free and unofficial, so it can be slow, and reports the rows added. Step 1: the look-inside prompt asks the agent to show what is in the database, in plain words. This is slide 10 on your own database: two tables, a row count of about one per trading day (about 240 for a year), and a recent latest date. The date and the count catch missing or duplicated data; they do not prove that a price is correct. Step 2: the refresh prompt tests the "no duplicates" promise from the spec. A second refresh should add 0 rows or a few new days, not another year. If it adds a year, use the fix template from slide 15. Step 3: the check-files prompt lists what would be saved. Read it: if backend/.env or anything that looks like a key is on the list, stop and raise your hand. Step 4: only after a clean list, send the push prompt. It commits with the message "Price database" and pushes to your own GitHub repo. A push saves your work to GitHub; it does not create the course checkpoint. Key leaked? Tell the facilitator — the key must be replaced. Step 5: compare with the expected result. At minute 17, anyone without two tables and prices gets help to checkpoint s2-database; do not keep debugging. If nothing moves for 2 minutes, press Esc and send the same prompt again.
words: 60 · budget: 60 · exception: prompt boxes (copyable prompts) are not counted; chips and labels are counted
status: UNTESTED

## 13. Run 2a: spec, plan and build a watchlist the dashboard follows
type: run
block: Run 2 — Watchlist · 15
visible:
Goal: a watchlist the dashboard follows.
Interview · Plan · Execute · Test / Debug · Iterate
Current: Interview
15 min
1. Interview — send:
```text
Let's brainstorm a watchlist for my financial app. I want to follow NISP, BBRI and TLKM, add or remove stocks myself, and see them on the dashboard. Ask me one question at a time, at most 3, in plain business language. Don't write any code or files yet.
```
✓ Interview
2. Update the spec — send:
```text
Add a watchlist to docs/spec.md. Keep the quote, history and chat endpoints working. New: GET /api/watchlist → [{ticker, name, price, change_pct, price_date}]; POST /api/watchlist {ticker}, which also saves that stock's price history; DELETE /api/watchlist/{ticker}. Prices come from the database. The dashboard shows one price card for each stock on the watchlist, so adding or removing a stock changes the dashboard after a refresh. Show the date of each price. If Yahoo fails, keep showing saved prices labelled "Saved prices as of <date>"; with no saved prices, say "No data yet". Accept IDX tickers ending in .JK only; otherwise say "Enter the IDX ticker, for example NISP.JK" and save nothing. Don't build anything yet.
```
Course setup — copy as is; the agent handles the details.
✓ Update the spec
Current: Plan
3. Plan mode (press Tab) — send:
```text
Read docs/spec.md and give me a numbered step-by-step plan for the watchlist only. Don't build anything yet.
```
Approve / Edit / Reject
✓ Plan
Current: Execute
4. Build mode (press Tab) — send:
```text
Approved. Save that plan to docs/plan.md, then build the watchlist from it. Then tell me how to open the watchlist page.
```
It asks to run a command? Read it. Installing or starting the app inside financial-app is expected. Anything else? Raise your hand.
✓ Build
You should see: Questions asked, spec updated, plan approved, a watchlist page with NISP and its price date, and a NISP card on the dashboard.
Stuck? Raise your hand — we move you to checkpoint s2-watchlist.
diagram: Workflow mini-map (.wf) above one open prompt panel at a time; finished prompts collapse to ✓ chips. Current changes Interview → Plan → Execute. An Approve / Edit / Reject chip sits under the Plan box. No unattended motion.
build:
  0: goal, mini-map (Current: Interview), time tag, the open Interview box
  1: Interview collapses; the Update-the-spec box opens, labelled "Course setup — copy as is; the agent handles the details."
  2: Update the spec collapses; Current: Plan; the Plan box opens with the chip Approve / Edit / Reject
  3: Plan collapses; Current: Execute; the Build box opens with the permission line
  4: Build collapses; the "You should see" line and the Stuck line appear
notes:
[UNTESTED] All four prompts are untested; rehearse them first. Timebox 15 minutes. Same five steps as this morning, now for the watchlist. Step 0: the interview prompt says what we want: follow NISP, BBRI and TLKM, add and remove stocks, see them on the dashboard. At most 3 questions, nothing written yet. Step 1: the spec prompt is long and technical on purpose; it is course setup, so copy it as is. Read the plain-language parts aloud: the dashboard shows one price card for each stock on the watchlist, so adding or removing a stock changes the dashboard after a refresh; each price shows its date; if Yahoo fails the app shows saved prices labelled "Saved prices as of" a date, or "No data yet" if it has none; only tickers ending in .JK are accepted, otherwise "Enter the IDX ticker, for example NISP.JK" and nothing is saved. For the facilitator: change_pct means the change against the previous trading day's close; it is stated here, not on the slide. Step 2: Plan mode (Tab), then read the plan and approve, edit or reject. Step 3: Build mode (Tab). Read each command it asks to run, and raise your hand for anything outside financial-app. Step 4: check the expected result. If the dashboard shows no NISP card, use the fix template from slide 15. At minute 12, anyone without a watchlist page gets help to checkpoint s2-watchlist; do not keep debugging. If nothing moves for 2 minutes, press Esc and send the same prompt again. In plain words: the stocks table from Run 1 is the watchlist, and Run 1 starts with NISP.JK in it, so NISP is on the watchlist from the start and the watchlist is stored in the database.
words: 59 · budget: 60 · exception: prompt boxes (copyable prompts, including the long spec prompt) are not counted; chips and labels are counted
status: UNTESTED

## 14. Run 2b: test it like a user, including a restart, then push
type: run
block: Run 2 — Watchlist · 15
visible:
Goal: test it like a user, then push.
Interview · Plan · Execute · Test / Debug · Iterate
Current: Test / Debug
15 min
1. Add BBRI.JK, then TLKM.JK. Each appears on the watchlist and the dashboard.
2. Type NISP (no .JK). You see: Enter the IDX ticker, for example NISP.JK. Nothing is saved.
3. Remove BBRI.JK. Refresh the dashboard. Its card is gone.
4. Stop the back end, start it again, reopen the app. The watchlist and prices are still there.
A step failed? Fill in the brackets before sending:
```text
[What I did]. I expected [what should happen], but I saw [what happened]. Explain the cause in plain words, then fix it.
```
Current: Iterate
5. Check files — send:
```text
List the files you would commit, and point out anything that looks like a key or password. Don't commit or push yet.
```
Read the list. backend/.env or a key in it? Stop and raise your hand.
6. List clean? Push — send:
```text
Commit those files with the message "Watchlist page" and push to GitHub.
```
Key leaked? Tell the facilitator — the key must be replaced.
You should see: BBRI and TLKM added, NISP alone rejected, BBRI removed, data still there after a restart.
Stuck? Raise your hand — we move you to checkpoint s2-watchlist.
diagram: Workflow mini-map (.wf) above one open panel at a time. Checks 1–4 need no prompt: each shows the action and its expected result, then collapses to a ✓ chip. The fill-in box and the two push boxes open one at a time. Current changes from Test / Debug to Iterate at the files check. No unattended motion.
build:
  0: goal, mini-map (Current: Test / Debug), time tag, check 1 with its expected result
  1: check 1 collapses to a ✓ chip; check 2 appears
  2: check 2 collapses; check 3 appears
  3: check 3 collapses; check 4 appears
  4: check 4 collapses; the fill-in box opens, labelled "A step failed? Fill in the brackets before sending:"
  5: the fill-in box collapses; Current: Iterate; the Check-files box opens with the stop line
  6: Check files collapses; the Push box opens with the key-leak line
  7: Push collapses to a ✓ chip; the "You should see" line and the Stuck line appear
notes:
[UNTESTED] The push prompts and the fix template are untested; rehearse them first. Timebox 15 minutes. Steps 1 to 4 are checks you do yourself in the browser: no prompt needed. Step 1: add BBRI.JK, then TLKM.JK; each should appear on the watchlist and on the dashboard. Step 2: type NISP without .JK; the app should say "Enter the IDX ticker, for example NISP.JK" and save nothing, because the spec accepts tickers ending in .JK only. Step 3: remove BBRI.JK and refresh the dashboard; its card should be gone. We remove BBRI and not TLKM so that NISP and TLKM prices stay for Session 3, which reruns on TLKM. Step 4: stop the back end, start it again and reopen the app; the watchlist and the prices should still be there, because they are saved in the database. Ask the facilitator if you are unsure how to restart the back end. Step 5: if a check failed, use the fix template: fill in the three brackets (what you did, what you expected, what you saw) before sending. It is the only prompt in the course you edit. Then repeat the check that failed. Steps 6 and 7: the same two-step push as Run 1b, with the message "Watchlist page". Read the list and stop on backend/.env or a key. Key leaked? Tell the facilitator — the key must be replaced. At minute 12, anyone whose checks still fail gets help to checkpoint s2-watchlist; do not keep debugging. In plain words: the stocks table from Run 1 is the watchlist, and Run 1 starts with NISP.JK in it, so NISP is on the watchlist from the start and the watchlist is stored in the database. That is why the restart check (step 4) keeps the watchlist.
words: 54 · budget: 60 · exception: prompt boxes (copyable prompts) are not counted; chips and labels are counted
status: UNTESTED

## 15. A useful bug report says what you did, what you expected and what you saw
type: check
block: Run 2 — Watchlist · 5
visible:
You removed a stock but it's still on the dashboard. What do you tell the agent?
A. "It's broken. Fix it."
B. "I removed TLKM from the watchlist, but the dashboard still shows it after a refresh. Explain why in plain words, then fix it."
C. "Rebuild the whole app."
B — It says what you did, what you expected and what you saw, and asks for the cause before the fix.
Fill in the brackets before sending:
```text
[What I did]. I expected [what should happen], but I saw [what happened]. Explain the cause in plain words, then fix it.
```
diagram: The question in the body, then three choice cards stacked (A, B, C). At step 1 B turns green, A and C fade and the reveal line appears. At step 2 the fill-in template box appears under it, labelled "Fill in the brackets before sending:".
build:
  0: the question and the three choices
  1: B highlights green; A and C fade; the reveal line appears
  2: the fill-in template box appears, labelled "Fill in the brackets before sending:"
notes:
This can happen in real projects, and in your own app it may just have happened in Run 2b. Read the question and the three choices aloud and vote by hand. A feels natural, but the agent has to guess what "it" is, and it may change the wrong thing. C throws away your work for one small fault, and the new build can have new faults. Click to reveal B. It says what you did (removed TLKM), what you expected (it disappears) and what you saw (still there after a refresh), and then asks for the cause before the fix, so you learn the cause. A likely cause is that the dashboard keeps its own list instead of reading the watchlist. Click again for the fill-in template: the three brackets are what you did, what you expected and what you saw. You use it in Run 2b if a check fails. It is the only prompt in the course that you edit before sending, and it is UNTESTED until rehearsed. Same habit as Session 1: paste the real error, ask for an explanation, check the fix yourself.
words: 28 · budget: 60 · exception: quiz choices A, B, C and the prompt box are not counted
status: UNTESTED (fill-in template)

## 16. The model's training is not a reliable source for current rules
type: visual
block: Why the chatbot needs knowledge · 3
visible:
Model
Trained on: general text, up to a cut-off date
May be missing: your company's rules · recent OJK pages · your app's data
Result: may be incomplete or out of date
diagram: A large rounded box "Model" shaped like a bookshelf, mostly full of grey books labelled together "Trained on: general text, up to a cut-off date". One shelf has a visible gap with a dashed outline; three faded book spines float outside it, labelled "May be missing: your company's rules · recent OJK pages · your app's data". Below the box, a speech bubble "Result: may be incomplete or out of date" with a small question mark. The floating spines drift for 3 cycles, then settle.
build:
  0: the bookshelf "Model", full of grey books
  1: the "Trained on" label appears
  2: the gap on one shelf appears; the three possibly-missing books float beside it
  3: the result bubble appears under the model
notes:
Switch to the chatbot. On step 0: the model behind your chatbot learned from a huge amount of general text. On step 1: that learning stopped at a cut-off date, and it was general, not about your company. On step 2: so some things may be missing from its shelf: your company's own rules, anything OJK published after the cut-off, pages it rarely saw. And your app's data, which is why in Session 1 the back end added NISP's prices to every request. The model is not retrained by us; our app adds data and reference text to each request. On step 3: when asked about something it may not have, a model can still give a smooth answer that is incomplete or out of date. For regulation that is a real risk, so training alone is not a reliable source for current rules. The fix is the same as for prices: put the right text in front of it, and check it.
words: 32 · budget: 40 · exception: none
status: n/a

## 17. The system prompt tells the chatbot its role and rules, and we test that it follows them
type: visual
block: Why the chatbot needs knowledge · 4
visible:
system: role and rules (you set it)
user
assistant
Role: answer stock questions for business users
Rules: name the source, say if unsure, no buy/sell advice
It can still be wrong, so we test.
Training prototype — not investment advice.
diagram: The message stack from Session 1 slide 6: role chips "system", "user", "assistant" stacked vertically. The system box grows and lifts forward, labelled "system: role and rules (you set it)". Two sticky notes attach to it: "Role: answer stock questions for business users" and "Rules: name the source, say if unsure, no buy/sell advice". The user and assistant boxes stay small and faded below. The chip "Training prototype — not investment advice." sits at the bottom from step 1. At the last click the line "It should follow them. It can still get them wrong, so we test." appears under the notes.
build:
  0: the three-box stack from Session 1, small
  1: the system box grows and lifts forward with its label; the prototype chip appears
  2: the Role sticky note attaches
  3: the Rules sticky note attaches
  4: the line "It should follow them. It can still get them wrong, so we test." appears
notes:
Remember this list from Session 1? Every request is a list of messages with roles. On step 0: system, user, assistant. In Session 1 the system message holds the role and rules, written by whoever builds the app. On step 1: today that is you. The system message goes at the top of every request, before the user's question. Point at the chip: this is a training prototype. It is not investment advice and it is not compliance-checked. On step 2: the role says who the chatbot is: here, an assistant that answers stock questions for business users. On step 3: the rules say what it should do: name the Wiki page or data it used, say when it does not know, and not recommend buying or selling. On step 4: these are instructions the chatbot should follow. It can still get them wrong, which is why Run 3c tests them with real questions, including one it cannot answer and one that asks for advice. Ask: which rule matters most for a bank? Usually the last one. You set it in Run 3c, and you can tighten it if a test fails.
words: 40 · budget: 40 · exception: none
status: n/a

## 18. A Wiki lets the app send matching official text with each question
type: visual
block: Why the chatbot needs knowledge · 4
visible:
Question
wiki/ = short Markdown pages
Keyword match
question + matching page → model
Answer + page link
The model can still misread the page — open the link.
No matching page → "This Wiki doesn't cover that."
diagram: Four boxes left to right, joined by arrows: a speech bubble "Question"; a folder "wiki/ = short Markdown pages" with three page icons, one of which lifts out labelled "Keyword match"; a box "question + matching page → model"; a reply bubble "Answer + page link" with a small link chip. Under the reply bubble, a warning chip "The model can still misread the page — open the link." From the folder a second arrow branches down to a grey bubble "No matching page → "This Wiki doesn't cover that."". Each arrow draws when its step is revealed; any pulse runs 3 times, then settles.
build:
  0: the "Question" bubble
  1: the wiki folder appears; the app picks pages whose words match ("Keyword match")
  2: "question + matching page → model" appears
  3: the answer bubble appears with its link chip
  4: the warning chip and the "No matching page" branch appear
notes:
So how does the app put the right text in front of the model? With a Wiki: a folder of short pages the app can send to the model with a question. On step 0: a user asks a question. On step 1: the app looks in the folder called wiki and picks the pages whose words match the question. No magic: it is a keyword match. On step 2: it sends the matching page together with the question to the model, inside the context window you saw in Session 1. On step 3: the answer comes back with the link to the page it was given. This helps the model use the source, but it can still misread the page or add things that are not on it. On step 4: so open the link and check. And if no page matches, our spec says the chatbot should say "This Wiki doesn't cover that." We test that in Run 3c. The Wiki stays small on purpose: a few pages, each short. You can open and read every page yourself, which is the point: you can check what the chatbot was given.
words: 28 · budget: 40 · exception: none
status: n/a

## 19. Only OJK and IDX pages go in, each with its link and the date you checked it
type: visual
block: Why the chatbot needs knowledge · 4
visible:
wiki/
ojk.go.id
idx.co.id
Blogs · forums · social posts
Title · URL · Last updated (if shown) · Checked on (date)
Each Wiki page starts with this header
diagram: A gate in the centre, with no ticks. From the left, five page cards slide towards it. Two cards "ojk.go.id" and "idx.co.id" pass through the gate into a folder labelled "wiki/". Three cards "Blogs · forums · social posts" bounce off the gate and fade, each with a red cross. Under the folder, a page card shows the header line "Title · URL · Last updated (if shown) · Checked on (date)", captioned "Each Wiki page starts with this header". The cards slide once, then settle.
build:
  0: the gate and the empty wiki folder
  1: the two official cards pass through the gate into the folder
  2: the three other cards bounce off and fade
  3: the header card appears under the folder
notes:
What goes into the Wiki decides what the chatbot is given, so we are strict. On step 1: two sources only. ojk.go.id is the Financial Services Authority, the regulator. idx.co.id is the Indonesia Stock Exchange. On step 2: anything else bounces: blogs, forums, social media posts, even good articles that summarise the rules. They may be out of date or wrong, and the web search in Run 3 may find some of them. Your job is to check the address of every page before it goes in. On step 3: each Wiki page starts with a header: the page title, its web address, the last-updated date if the page shows one, and the date you checked it. That address is what the chatbot shows as its source, and what you click to check it. An official page can be old, replaced, or educational rather than the rule itself. If you cannot tell whether it is current, the Wiki page says so. Our Wiki is a training set, not a verified rulebook. If the agent offers a page from another site, say no.
words: 28 · budget: 40 · exception: none
status: n/a

## 20. Worked example: check one answer against its source page
type: demo
block: Why the chatbot needs knowledge · 5
visible:
Illustrative
Question: What is OJK?
Answer: An independent state institution that regulates and supervises.
Source: ojk.go.id — Task and Functions
“OJK is an independent state institution that has the function, duty, and authority to regulate, supervise, examine, and investigate.”
Source shown? · Matches the page? · Says “not covered” when it isn't?
diagram: A chat-style card with the grey tag "Illustrative": the question "What is OJK?" and the answer "An independent state institution that regulates and supervises." Step 1: a link chip shaped like an address bar appears under the card: "Source: ojk.go.id — Task and Functions". Step 2: a page panel opens with the sentence highlighted in yellow, quoted verbatim from the page. Step 3: the page panel is replaced by a three-item check strip. Only the question and the answer are illustrative; the quoted sentence is real.
build:
  0: the answer card with the Illustrative tag
  1: the source link chip appears under the card
  2: the page panel opens with the matching sentence highlighted
  3: the page panel is replaced by the three checks: "Source shown? · Matches the page? · Says “not covered” when it isn't?"
notes:
Presenter demo. One question, one illustrative answer, one real source line. The question and answer are tagged Illustrative: they show the pattern, not real chatbot output. The source line is real. Source facts for the facilitator: page "Task and Functions" on the OJK English site, https://www.ojk.go.id/en/tentang-ojk/Pages/Tugas-dan-Fungsi.aspx . Date checked: 2026-11-12. Verbatim sentence on that page: "OJK is an independent state institution that has the function, duty, and authority to regulate, supervise, examine, and investigate." The slide's answer ("an independent state institution that regulates and supervises") is supported by that sentence. Be open about the choice: this is OJK's general "Task and Functions" page, not an investor-education page. We could not reach an OJK or IDX investor-education page from the build machine: idx.co.id refused automated requests with HTTP 403, and ojk.go.id refuses requests that do not look like a browser. So we used the fallback the spec allows: the OJK description of what OJK is and does, as a short, stable fact. Before class, open the page in a browser and confirm the sentence is still there; if the page or wording has changed, replace the quoted sentence with the current one. Step 0: read the question and the answer. Step 1: where did it come from? Click the link. Step 2: find the matching sentence on the page and ask: does it support the answer? Here it does: "independent state institution" and "regulate, supervise". Step 3: three checks, and you use them again in Run 3c. Is a source shown? Does the answer match the page? And when the Wiki has nothing on the question, does the chatbot say "not covered" instead of guessing? A link alone is not proof: open it and find the sentence. Ask: if the page said something different, what would you do? Fix the page or the system prompt, then ask again.
words: 39 · budget: 40 · exception: none
status: n/a (source line is real; question and answer are illustrative)

## 21. Run 3a: record three answers, then interview and plan the Wiki
type: run
block: Run 3 — Teach the chatbot · 15
visible:
Goal: record three answers, interview, plan the Wiki.
Interview · Plan · Execute · Test / Debug · Iterate
Current: Interview
15 min
1. In your browser, ask your chatbot these three questions. Write down each answer:
"What does OJK supervise?" · "What is an auto-rejection limit on IDX?" · "What should I check before investing in a stock?"
✓ Record answers
2. Interview — send:
```text
Let's brainstorm a Wiki for my chatbot: short pages from official ojk.go.id and idx.co.id investor-education pages only, each with its link. Ask me one question at a time, at most 3, in plain business language. Don't write any code or files yet.
```
✓ Interview
3. Update the spec — send:
```text
Add a Wiki to docs/spec.md: Markdown pages in wiki/, one page per official page, from ojk.go.id or idx.co.id only. Each page starts with its title, URL, last-updated date if the page shows one, and the date we checked it. For each question, the back end picks matching Wiki pages by keyword and sends them with the question. If no page matches, the chatbot says the Wiki doesn't cover it. I'll write the system prompt. Don't build anything yet.
```
Course setup — copy as is; the agent handles the details.
✓ Update the spec
Current: Plan
4. Plan mode (press Tab) — send:
```text
Read docs/spec.md and give me a numbered step-by-step plan for the Wiki only. Don't build anything yet.
```
Approve / Edit / Reject
✓ Plan
5. Build mode (press Tab) — send:
```text
Approved. Save that plan to docs/plan.md. Don't build anything yet.
```
You should see: Three answers written down, an updated spec, a saved plan. No Wiki yet.
Stuck? Raise your hand — we move you to checkpoint s2-wiki.
diagram: Workflow mini-map (.wf) above one open panel at a time; finished steps collapse to ✓ chips. Step 1 is a check with no prompt: the three questions. The mini-map shows Interview for steps 0–2 and Plan from step 3. An Approve / Edit / Reject chip sits under the Plan box. No unattended motion.
build:
  0: goal, mini-map (Current: Interview), time tag, the three questions to ask the chatbot
  1: the questions collapse to a ✓ chip; the Interview box opens
  2: Interview collapses; the Update-the-spec box opens, labelled "Course setup — copy as is; the agent handles the details."
  3: Update the spec collapses; Current: Plan; the Plan box opens with the chip Approve / Edit / Reject
  4: Plan collapses; the Save box opens (Build mode)
  5: the Save box collapses; the "You should see" line and the Stuck line appear
notes:
[UNTESTED] The interview, spec, plan and save prompts are untested; rehearse them first. Timebox 15 minutes. Same five steps as this morning, now for the Wiki. Step 0: before changing anything, ask your chatbot the three questions in the browser and write down each answer. This records where you start. The answers may be right, vague or wrong; we do not know yet, and neither does a reader without a source. You compare them in Run 3c. Step 1: the interview prompt asks for short pages from official ojk.go.id and idx.co.id investor-education pages only, each with its link: at most 3 questions, nothing written yet. Step 2: the spec prompt is technical on purpose; copy it as is. Plain-language parts: pages in wiki/; each page starts with its title, its URL, the last-updated date if the page shows one, and the date we checked it; for each question the back end picks matching pages by keyword and sends them with the question; if no page matches, the chatbot says the Wiki does not cover it. You set the system prompt in Run 3c. Step 3: Plan mode (Tab), then read the plan and approve, edit or reject. Step 4: switch to Build mode and send the save prompt; it only saves the plan to docs/plan.md and builds nothing. At minute 12, anyone without a saved plan gets help from the facilitator, because Run 3b needs it. If nothing moves for 2 minutes, press Esc and send the same prompt again.
words: 59 · budget: 60 · exception: prompt boxes (copyable prompts, including the long spec prompt) are not counted; chips and labels are counted
status: UNTESTED

## 22. Run 3b: find official pages, check each one, build the Wiki
type: run
block: Run 3 — Teach the chatbot · 15
visible:
Goal: find official pages, check them, build the Wiki.
Interview · Plan · Execute · Test / Debug · Iterate
Current: Execute
15 min
1. Find pages — send:
```text
Find official investor-education pages on ojk.go.id and idx.co.id that explain what OJK supervises, what an auto-rejection limit is, and what to check before investing. For each, give the URL, the page title, the last-updated date if shown, and a one-line summary. Don't save anything yet.
```
✓ Find pages
2. Check: every address on ojk.go.id or idx.co.id? Open each one. Tell opencode which to drop.
✓ Check addresses
3. Build mode (press Tab) — send:
```text
Turn the pages I approved into Wiki pages in wiki/, one Markdown file per page, with the header from the spec. Only use what the page says. Then connect the Wiki to the chatbot as the plan says.
```
It asks to run a command? Read it. Installing or starting the app inside financial-app is expected. Anything else? Raise your hand.
✓ Build the Wiki
You should see: wiki/ with one page for each approved page, each starting with its title, URL and dates; the chatbot connected.
Stuck? Raise your hand — we move you to checkpoint s2-wiki.
diagram: Workflow mini-map (.wf) above one open panel at a time; finished steps collapse to ✓ chips. Step 1 is a participant check with no prompt. Current stays Execute. No unattended motion.
build:
  0: goal, mini-map (Current: Execute), time tag, the open Find-pages box
  1: Find pages collapses to a ✓ chip; the address check appears (no prompt)
  2: the check collapses; the Build box opens with the permission line
  3: Build collapses; the "You should see" line and the Stuck line appear
notes:
[UNTESTED] Both prompts are untested, and they depend on the agent reaching the web; rehearse them first. Timebox 15 minutes. Facilitator setup: the project log (entry "S2 copy v2 written") records that opencode's web fetch works by default and that web search needs OPENCODE_ENABLE_EXA=1, in opencode 1.19.5 with no key. That is recorded in the project log; verify in rehearsal. The OJK and IDX sites may refuse automated requests, so the agent may not be able to open every page. Fallback: the handout's verified URL list (a delivery blocker, to be prepared before class). At minute 10 with no usable pages, everyone uses the handout list. Step 0: the find prompt asks for investor-education pages on ojk.go.id and idx.co.id on three topics, with the URL, title, last-updated date if shown and a one-line summary for each. Nothing is saved yet. Step 1: this check is yours, with no prompt. Is every address on ojk.go.id or idx.co.id? Open each page. Drop anything else, even a good article. Reply in the chat with the pages to drop before you send the build prompt. An official page can be old, replaced, or educational rather than the rule itself; note any page whose date is unclear. Step 2: switch to Build mode and send the build prompt. It turns the pages you approved into Wiki pages, one Markdown file per page, with the header from the spec. "Only use what the page says" tells the agent not to fill gaps; you still compare its page with the original. Read each command it asks to run, and raise your hand for anything outside financial-app. Step 3: open wiki/ and compare with the expected result. If nothing moves for 2 minutes, press Esc and send the same prompt again.
words: 61 · budget: 60 · exception: prompt boxes (copyable prompts) are not counted; chips and labels are counted
status: UNTESTED

## 23. Run 3c: set the system prompt, check answers against their pages, then push
type: run
block: Run 3 — Teach the chatbot · 15
visible:
Goal: set the rules, test them, push.
Training prototype — not investment advice.
Interview · Plan · Execute · Test / Debug · Iterate
Current: Execute
15 min
1. Set the system prompt — send:
```text
Set the chatbot's system prompt to: You answer questions about Indonesian stocks for business users, using the Wiki pages and the app's data that come with each question. Give the Wiki page URL you used. If they don't cover the question, say so. If asked what to buy or sell, give facts and risks only, no recommendation.
```
✓ System prompt
Current: Test / Debug
2. Ask the same three questions. For each answer: open the link · find the sentence that supports it.
✓ Three answers checked
3. Ask: Our bank's staff share trading limit? → Wiki doesn't cover it. Ask: Should I buy NISP? → facts and risks only. Recommends? Don't use it.
✓ Two tests
Current: Iterate
Fix what failed, then re-ask.
4. Check files — send:
```text
List the files you would commit, and point out anything that looks like a key or password. Don't commit or push yet.
```
Read the list. backend/.env or a key in it? Stop and raise your hand.
✓ Check files
5. List clean? Push — send:
```text
Commit those files with the message "Wiki and system prompt" and push to GitHub.
```
Key leaked? Tell the facilitator — the key must be replaced.
You should see: Each answer should link a supporting Wiki page; “not covered” for the staff question; no recommendation.
Stuck? Raise your hand — we move you to checkpoint s2-wiki.
diagram: Workflow mini-map (.wf) above one open panel at a time; finished steps collapse to ✓ chips. The chip "Training prototype — not investment advice." stays visible beside the goal. Current changes Execute → Test / Debug → Iterate. No unattended motion.
build:
  0: goal, prototype chip, mini-map (Current: Execute), time tag, the open System-prompt box
  1: the system prompt collapses to a ✓ chip; Current: Test / Debug; the three-question check
  2: that check collapses; the two extra tests appear
  3: the tests collapse; Current: Iterate; the fix line and the Check-files box open with the stop line
  4: Check files collapses; the Push box opens with the key-leak line
  5: Push collapses to a ✓ chip; the "You should see" line and the Stuck line appear
notes:
[UNTESTED] The system prompt and the push prompts are untested; rehearse them first. Timebox 15 minutes. Point at the chip: this is a training prototype, not investment advice and not compliance-checked. Step 0: the system prompt gives the chatbot its role and rules: use the Wiki pages and the app's data that come with each question, give the page URL, say so when they do not cover the question, and give facts and risks only if asked what to buy or sell. These are instructions the chatbot should follow; it can still get them wrong, so we test. Step 1: ask the same three questions you recorded in Run 3a. For each answer, open the link, find the sentence on the page that supports it, and if there is none, fix it and ask again. Compare with your earlier answers: is there a source now, and does it match the page? Slide 20 showed the check. Step 2: two more tests. "What is our bank's limit for staff share trading?" is not in the Wiki, so the chatbot should say the Wiki does not cover it, not guess. "Should I buy NISP?" should give facts and risks and no recommendation. If it recommends, do not use the answer: tighten the system prompt and test again. Step 3: fix what failed, then check the files; read the list and stop on backend/.env or a key. Step 4: push with the message "Wiki and system prompt". A push saves your work to your own GitHub repo; it does not create the course checkpoint. Key leaked? Tell the facilitator — the key must be replaced. At minute 12, anyone whose answers still fail gets help to checkpoint s2-wiki; do not keep debugging. If nothing moves for 2 minutes, press Esc and send the same prompt again.
words: 60 · budget: 60 · exception: prompt boxes (copyable prompts) are not counted; chips and labels are counted
status: UNTESTED

## 24. A regulatory answer needs a source you can open and check
type: check
block: Close + Q&A · 4
visible:
The chatbot quotes a rule but gives no source. Is that good enough?
A. Yes. It sounds right.
B. No. Find which page the app sent, open it, and check the rule. No page? Add a checked official page.
C. No. Switch to a bigger model.
B — A regulatory answer needs a source that actually supports it. A link alone is not proof.
diagram: The question in the body, then three choice cards stacked (A, B, C). At step 1 B turns green, A and C fade and the reveal line appears.
build:
  0: the question and the three choices
  1: B highlights green; A and C fade; the reveal line appears
notes:
Read the question and vote by hand. A is the trap: sounding right is exactly what a model is good at, even when it is wrong. For a rule from a regulator, a smooth answer you cannot check is not good enough. C may help a little, but a bigger model still cannot show you a page it was never given. Click to reveal B. Find which page the app sent, open it, and check that it supports the rule. A missing source has two likely causes: the system prompt does not ask for one, so you strengthen that rule; or there is no Wiki page for that question, so you add a checked official page, or accept "not covered". Careful: asking the chatbot "which page did you use?" can produce a page that is invented, so check the link yourself. And a link alone is not proof: open it and find the sentence. Ask: in your own job, would you forward a regulatory answer to a client without checking its source? That is the standard.
words: 18 · budget: 60 · exception: quiz choices A, B, C are not counted
status: n/a

## 25. Data lives in the database, knowledge in the Wiki, behaviour in the system prompt
type: recap
block: Close + Q&A · 4
visible:
Database: data
prices · watchlist
Wiki: knowledge
OJK and IDX pages
System prompt: behaviour
role · rules
Finish check: watchlist survives a restart · answers show a checked source · latest commit on GitHub — or checkpoint s2-wiki.
diagram: Three boxes side by side, each with an icon: a cylinder "Database: data" with "prices · watchlist" under it; a book "Wiki: knowledge" with "OJK and IDX pages" under it; a speech bubble with a gear "System prompt: behaviour" with "role · rules" under it. All three feed one arrow into a small chatbot icon. The finish-check line sits at the bottom.
build:
  0: title
  1: the database box appears
  2: the Wiki box appears
  3: the system prompt box appears; arrows join into the chatbot
  4: the finish-check line appears
notes:
Do not re-teach; link each box to what they did. On step 1: the database holds data. You built it in Run 1 and the watchlist reads from it, so the app keeps prices and the stocks you follow, even when Yahoo is down. On step 2: the Wiki holds knowledge: a few official pages the app can send to the model with a question, so the answer can name a source you check. On step 3: the system prompt holds behaviour: who the chatbot is and the rules it should follow. You set it and tested it. When something is wrong later, this split tells you where to look: wrong number, check the database; wrong fact, check the Wiki; wrong tone or advice, check the system prompt. If it gives advice, don't use the answer: fix the system prompt and retest. On step 4: the finish check. Does the watchlist survive a restart? Does each answer show a source you checked? Is your latest commit on GitHub? Anyone not finished can switch to checkpoint s2-wiki for Session 3; the facilitator confirms the move.
words: 28 · budget: 40 · exception: none
status: n/a

## 26. Questions
type: Q&A
block: Close + Q&A · 6
visible:
Questions?
diagram: Large "Questions?" heading. Around it, five small shapes keep moving on slow loops: three square speech bubbles drifting along different paths, one red question mark orbiting the heading, and one dot bouncing between the bubbles. No text inside the shapes.
build:
  0: heading and moving shapes (they loop for as long as the slide is open)
notes:
Open the floor. If no one speaks, start with a prompt: which official page surprised you? Or: what would you put in a Wiki for your own team? Collect parking-lot items on a flip chart. Repeat each question before answering so the room hears it. Take questions for the first minutes, and use the last ones to check that everyone has pushed. Ask by show of hands: who has the watchlist surviving a restart? Who has a commit on GitHub? Anyone without: tell the facilitator, who confirms checkpoint s2-wiki for them. A push saves your work to your own GitHub repo; it is not the same as the checkpoint. Anyone whose key may have appeared in a push: tell the facilitator; the key must be replaced. Keep investment questions neutral: the app shows data and official facts; it does not advise. If a question is about how the database or the Wiki works inside, say that is beyond today's session.
words: 1 · budget: 40 · exception: none
status: n/a

## 27. Next session: turn your data into a report and a deck
type: talk
block: Close + Q&A · 1
visible:
Session 3:
- A NISP analysis report from your database
- A PowerPoint deck made from the report
- A saved workflow you rerun on TLKM
diagram: none
build:
  0: all lines together
notes:
Preview Session 3 in one minute. Today the app saved prices and began answering rules questions with a source you can check. In Session 3 you use that data. First, the agent writes a NISP analysis report from your own database, and you check every number against the dashboard. Then it turns the report into a PowerPoint deck, and you improve it with feedback. Finally, you save the whole process as a workflow and run it again on TLKM; that is why Run 2b removed BBRI and not TLKM. Same five steps as today: Interview, Plan, Execute, Test / Debug, Iterate. Keep your project, or use checkpoint s2-wiki. Thank everyone and close.
words: 26 · budget: 40 · exception: none
status: n/a

## Contract check

Spec §11.3: every `You should see` item and every test step in spec §8 maps to a prompt in the same or an earlier run that asks for it. Steps are the click order on each slide. "Participant step" means the slide asks the person to do it and no prompt is needed; the prompt that makes the result possible is named in the same row.

| Run / step | Result checked | Asked for by |
|---|---|---|
| Run 1a | Up to 3 questions | Slide 11 step 1: P-INT interview prompt ("Ask me one question at a time, at most 3") |
| Run 1a | An updated docs/spec.md | Slide 11 step 2: spec prompt ("Add the price database to docs/spec.md") |
| Run 1a | A plan | Slide 11 step 3: plan prompt ("give me a numbered step-by-step plan for the price database only") |
| Run 1a | No database yet | Slide 11 steps 1–3: every prompt ends "Don't write any code or files yet" or "Don't build anything yet" |
| Run 1b | Two tables (stocks, prices) | Slide 11 step 2 (spec names both tables), built by slide 12 step 1 (build prompt); read in slide 12 step 2 (look-inside prompt) |
| Run 1b | About one row per trading day | Slide 12 step 1 ("last year of prices", reports rows added); read in slide 12 step 2 ("how many rows it has") |
| Run 1b | Latest NISP row with a recent date | Slide 12 step 2: look-inside prompt ("the latest NISP.JK row") |
| Run 1b | Second refresh adds no duplicates (0 or a few new days, not a full year) | Slide 12 step 3: refresh prompt; the rule comes from slide 11 step 2 ("one row per ticker and date, so refreshing twice adds no duplicates") |
| Run 1b | Push without a key or password | Slide 12 step 4: P-PUSH1 (files list, flags keys); slide 12 step 5: P-PUSH2 |
| Run 2a | Up to 3 questions | Slide 13 step 1: P-INT2 ("at most 3") |
| Run 2a | An updated spec | Slide 13 step 2: watchlist spec prompt |
| Run 2a | An approved plan | Slide 13 step 3: P-PLAN(watchlist) |
| Run 2a | Watchlist page with NISP and its price date | Slide 11 step 2: spec prompt (stocks table, seeded with NISP.JK; the stocks table is the watchlist, spec §7.1) plus slide 13 step 2: watchlist spec prompt ("Show the date of each price"; GET /api/watchlist returns price_date); built by slide 13 step 4 (build prompt) |
| Run 2a | Dashboard shows a NISP card (dashboard follows the watchlist) | Slide 11 step 2: spec prompt (NISP.JK is in the stocks table, which is the watchlist) plus slide 13 step 2: "The dashboard shows one price card for each stock on the watchlist, so adding or removing a stock changes the dashboard after a refresh" |
| Run 2a (saved-prices label) | Saved prices as of <date> / No data yet when Yahoo fails (slide 9 promise) | Slide 13 step 2: "If Yahoo fails, keep showing saved prices labelled ... with no saved prices, say "No data yet"" |
| Run 2b test 1 | BBRI.JK then TLKM.JK appear on the watchlist and dashboard | Slide 13 step 2: "POST /api/watchlist {ticker}, which also saves that stock's price history" and "dashboard shows one price card for each stock" |
| Run 2b test 2 | NISP without .JK → "Enter the IDX ticker, for example NISP.JK", nothing saved | Slide 13 step 2: "Accept IDX tickers ending in .JK only; otherwise say ... and save nothing" |
| Run 2b test 3 | Remove BBRI.JK; its card is gone after a refresh | Slide 13 step 2: "DELETE /api/watchlist/{ticker}" and "removing a stock changes the dashboard after a refresh" |
| Run 2b test 4 | After a restart the watchlist and prices are still there | Slide 11 step 2: spec prompt (SQLite database backend/data/app.db; the stocks table is the watchlist) plus slide 13 step 2: watchlist spec prompt ("Prices come from the database"); slide 11 step 1 ("so the app still has them after a restart") |
| Run 2b | If a step fails: fix it | Slide 14 step 5: P-FIX template (also slide 15) |
| Run 2b | Push without a key or password | Slide 14 step 5: P-PUSH1; slide 14 step 6: P-PUSH2 |
| Run 3a | Three answers written down | Slide 21 step 1: the three questions (a participant step; no prompt) |
| Run 3a | An updated spec | Slide 21 step 3: Wiki spec prompt |
| Run 3a | A saved plan | Slide 21 step 4: P-PLAN(Wiki) then P-SAVE ("Save that plan to docs/plan.md") |
| Run 3a | No Wiki yet | Slide 21 steps 2–5: every prompt ends "Don't write any code or files yet" or "Don't build anything yet" |
| Run 3b | Only ojk.go.id / idx.co.id addresses | Slide 22 step 1: find prompt ("on ojk.go.id and idx.co.id"); slide 22 step 2: participant check (no prompt) |
| Run 3b | Each page starts with title, URL, last-updated date, date checked | Slide 21 step 3: spec prompt ("Each page starts with its title, URL, last-updated date if the page shows one, and the date we checked it"); slide 22 step 3: build prompt ("with the header from the spec") |
| Run 3b | wiki/ folder with one page per approved page; chatbot connected | Slide 22 step 3: build prompt ("one Markdown file per page ... connect the Wiki to the chatbot") |
| Run 3c | Each answer links a Wiki page that supports it | Slide 23 step 1: system prompt ("Give the Wiki page URL you used"); check on slide 23 step 2 (a participant step) |
| Run 3c | "Not covered" for the staff-limit question | Slide 23 step 1: system prompt ("If they don't cover the question, say so"); slide 21 step 3 ("If no page matches, the chatbot says the Wiki doesn't cover it"); test on slide 23 step 3 |
| Run 3c | No recommendation for "Should I buy NISP?" | Slide 23 step 1: system prompt ("If asked what to buy or sell, give facts and risks only, no recommendation"); test on slide 23 step 3 |
| Run 3c | Push without a key or password | Slide 23 step 4: P-PUSH1; slide 23 step 5: P-PUSH2 |

## Word count check

Count = largest number of visible non-title words at any one reveal step, split on spaces. Prompt boxes (the copyable text) and quiz choices are excluded; their labels and chips are counted. 

id | type | words | budget | over? | exception
---|---|---|---|---|---
1 | title | 11 | 40 | no | none
2 | visual | 23 | 40 | no | none
3 | visual | 23 | 40 | no | none
4 | talk | 23 | 40 | no | none
5 | visual | 23 | 40 | no | none
6 | visual | 28 | 40 | no | none
7 | check | 41 | 60 | no | quiz choices (A, B, C) are not counted; the 41 = question (13) + grid and Sample tag (10) + reveal line (18)
8 | visual | 40 | 40 | no | none
9 | visual | 37 | 40 | no | none
10 | demo | 35 | 40 | no | none
11 | run | 51 | 60 | no | prompt boxes (copyable prompts, including the long spec prompt) are not counted; chips and labels are counted
12 | run | 60 | 60 | no | prompt boxes (copyable prompts) are not counted; chips and labels are counted
13 | run | 59 | 60 | no | prompt boxes (copyable prompts, including the long spec prompt) are not counted; chips and labels are counted
14 | run | 54 | 60 | no | prompt boxes (copyable prompts) are not counted; chips and labels are counted
15 | check | 28 | 60 | no | quiz choices A, B, C and the prompt box are not counted
16 | visual | 32 | 40 | no | none
17 | visual | 40 | 40 | no | none
18 | visual | 38 | 40 | no | none
19 | visual | 28 | 40 | no | none
20 | demo | 39 | 40 | no | none
21 | run | 59 | 60 | no | prompt boxes (copyable prompts, including the long spec prompt) are not counted; chips and labels are counted
22 | run | 59 | 60 | no | prompt boxes (copyable prompts) are not counted; chips and labels are counted
23 | run | 60 | 60 | no | prompt boxes (copyable prompts) are not counted; chips and labels are counted
24 | check | 18 | 60 | no | quiz choices A, B, C are not counted
25 | recap | 38 | 40 | no | none
26 | Q&A | 1 | 40 | no | none
27 | talk | 26 | 40 | no | none

slides: 27 · minutes: 180 · run minutes: 110
