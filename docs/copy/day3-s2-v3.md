# Day 3 · Session 2 — slide copy v3 (review fixes, worked examples, 27 slides)

Course: AI Vibe Coding for Business Users · Session 2: Watchlist & AI knowledge · 3 hours, no break · English deck, speaker-led and hands-on.
Sources: `docs/outlines/day3-s2-v3.md` (27 headlines from spec §6, kept word for word), spec `docs/superpowers/specs/2026-11-12-day3-s2-v3-deck-design.md` (§5 deck-wide wording, §7 redesigned slides, §8 runs), `docs/copy/day3-s2-v2.md` and the notes in `decks/day3-s2.html` (v2 text reused where still correct), `docs/reviews/2026-11-12-day3-s2-review.md` (finding IDs P0-1 … P3-2).
This file holds slides 1–10; slides 11–27 are added by later tasks.

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
Welcome back. In Session 1 you built a NISP dashboard and a chatbot by directing opencode, and you may have saved it on GitHub. This session upgrades that same app in two ways. First, it gets a memory: a database that keeps prices, and a watchlist of the stocks you follow. Second, the chatbot gets reference text: a small Wiki built from official Indonesian pages, and a system prompt that you write yourself. The method is the same as this morning: Interview, Plan, Execute, Test / Debug, Iterate. Before we start, check that opencode opens on every laptop and that your app from Session 1 still starts. Anyone whose app does not start, raise your hand now; the next slides show what happens then.
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
