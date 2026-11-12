# Day 3 · Session 2 — slide copy v2 (visual, 3 runs)

Course: AI Vibe Coding for Business Users · Session 2: Watchlist & AI knowledge · 3 hours · English deck, speaker-led and hands-on.
Sources: `docs/outlines/day3-s2-v2.md` (approved outline v2, 21 headlines, kept word for word), `docs/superpowers/specs/2026-11-11-day3-design.md` (§3 S2 objectives, §7 S2, §8 app), `docs/superpowers/plans/2026-11-11-day3-build.md` (fixed app interface), `prompts/s1.md` (style of the tested prompts).

How to read this file:
- `visible:` is the on-slide text. Every label the diagram shows is listed in `visible:`; the `diagram:` line says where it goes. Quoted labels in `diagram:` that are not in `visible:` are counted too.
- `build:` lists the click steps. Step 0 is what shows when the slide arrives.
- Prompts in fenced blocks are not counted toward the word budget. `handout:` holds prompts that go in the printed handout, not on the slide.
- `status: UNTESTED` means the prompt was written for this session and has not been run in opencode; rehearse it before class. Every Session 2 prompt is UNTESTED.
- Sample numbers in diagrams are round, labelled "sample", and are not real NISP prices.

## 1. Upgrade your Financial App: watchlist and AI knowledge
type: title
block: Opening + recovery · 2
visible:
Day 3 · Session 2
AI Vibe Coding for Business Users
diagram: none
build:
  0: title, subtitle and session line together
notes:
Welcome back. In Session 1 you built a NISP dashboard and a chatbot by directing opencode, and you pushed it to GitHub. This session upgrades that same app in two ways. First, it gets a memory: a database that keeps prices, and a watchlist of the stocks you follow. Second, the chatbot gets knowledge: a small Wiki built from official Indonesian sources, and a system prompt that you write yourself. The method stays the same as this morning: brainstorm, spec, plan, build, test. Before we start, check that opencode opens on every laptop and that the app from Session 1 still starts. Anyone whose app does not start, raise your hand now; the next slides show how to catch up in a minute.
words: 10 · budget: 40 · exception: none
status: n/a

## 2. Today your app remembers prices and your chatbot learns the rules
type: visual
block: Opening + recovery · 5
visible:
Your app from Session 1
Database: price history
Watchlist: NISP · BBRI · TLKM
Wiki: OJK and IDX pages
Answers with a source
diagram: Centre: a laptop browser frame "Your app from Session 1" showing the small dashboard and chat panel. Below it a cylinder icon "Database: price history" plugs into the frame with a short connector. To the right of the dashboard a narrow list card "Watchlist: NISP · BBRI · TLKM" slides in. Next to the chat panel a book icon "Wiki: OJK and IDX pages" opens. A speech bubble from the chat panel ends with a small link chip: "Answers with a source".
build:
  0: the browser frame with the Session 1 app
  1: the database cylinder plugs in under the frame; the three watchlist rows fill one by one
  2: the book icon opens beside the chat panel
  3: the chat bubble with the source chip appears; the book and bubble pulse gently
notes:
Say what the session produces. On step 0: this is the app you have now. It fetches NISP live from Yahoo and the chatbot answers from that data. On step 1: today it gets a database, a file that keeps every day's price, so the app remembers. On that database we build a watchlist: NISP, plus BBRI and TLKM, which you add yourself, and you can remove one. On step 2: the chatbot gets a Wiki, a few pages taken from the official OJK and IDX websites. On step 3: when it answers a rules question, it says which page the answer came from. Three runs today, each building on the last. As before, the app shows data and facts only. It never tells anyone what to buy or sell.
words: 21 · budget: 40 · exception: none
status: n/a

## 3. Start from your own app or switch to checkpoint s1-chatbot
type: talk
block: Opening + recovery · 3
visible:
Your app works? Keep it.
Behind? Send this to opencode:
```text
Replace my project with checkpoint s1-chatbot from [CHECKPOINT URL], keep my .env.
```
Check: both servers start, NISP loads, the chatbot replies.
diagram: none
build:
  0: the first line
  1: the recovery sentence and the check line
notes:
Everyone starts this session from a working Session 1 app. On step 0: if your app starts and the chatbot answers, keep it; you are ready. On step 1: if it does not, or you missed part of Session 1, send this one sentence to opencode. It swaps your project for our reference version at checkpoint s1-chatbot and keeps your .env file, which holds the AI key. Your own work stays on GitHub if you pushed it. Then check three things: both servers start, the NISP price loads at localhost:5173, and the chatbot replies to a simple question. The same sentence, with a different checkpoint name, is in the handout for every "Stuck?" line today. Before class, replace [CHECKPOINT URL] with the real link. Give this two minutes, then move on.
words: 19 · budget: 40 · exception: fenced recovery sentence not counted (12 words)
status: UNTESTED (recovery sentence, spec §8.6)

## 4. Your app forgets everything when it restarts
type: visual
block: Why an app needs memory · 5
visible:
Page shows NISP
Server restarts
Nothing kept
Fetch it all again from Yahoo
No history. No list of stocks you follow.
diagram: A loop of four boxes, left to right then back: a browser "Page shows NISP" with a small chart; a power icon "Server restarts"; an empty grey box with a dashed outline "Nothing kept"; a cloud "Fetch it all again from Yahoo" with an arrow back to the browser. Caption under the loop is the last line of visible.
build:
  0: the browser box with the chart
  1: "Server restarts": the chart and numbers fade out of the browser box
  2: "Nothing kept" empty box appears
  3: arrow to the Yahoo cloud and back to the browser; caption appears in accent colour
notes:
Start with what the app does today. On step 0: the page shows NISP, fetched live. On step 1: stop the back end, or close the laptop, and start it again. On step 2: nothing was kept. The back end held the prices only while it was running. On step 3: when it starts again, it has to ask Yahoo for everything, every time. Two problems follow. If Yahoo is slow or blocks us, the page has nothing to show. And the app cannot remember anything you chose, like which stocks you want to follow. Ask the room: where does your own business keep things it must not forget? Spreadsheets, a customer system, a ledger. An app needs the same: a place to write things down. That place is a database.
words: 21 · budget: 40 · exception: none
status: n/a

## 5. A database keeps what the app must remember, in tables of rows and columns
type: visual
block: Why an app needs memory · 6
visible:
backend/data/app.db
Table: prices
ticker · date · close
NISP.JK · Mon · 1,000
NISP.JK · Tue · 1,010
NISP.JK · Wed · 1,020
sample
Column = one kind of value · Row = one record
diagram: A file icon "backend/data/app.db" at top left. From it, a spreadsheet-like grid "Table: prices" with three column headers "ticker · date · close". Three rows below. A small grey tag "sample" in the corner of the grid. Caption under the grid is the last line of visible, with the word Column in one colour pointing at a column and the word Row in another pointing at a row.
build:
  0: the file icon "backend/data/app.db"
  1: the empty grid with the three column headers
  2: the three rows fill in one at a time, top to bottom; the "sample" tag appears
  3: the caption appears; one column and one row highlight in turn, slowly alternating
notes:
A database is a file where an app writes down what it must remember. Ours will be one file, app.db, in the back end folder. The database type is called SQLite. You never open it in Excel, but it looks like a spreadsheet inside. On step 1: a database holds tables. This one is called prices, and its columns say what we store: the ticker, the date and the closing price. On step 2: each row is one record, here one day for NISP. Point at the sample tag: these numbers are made up for the picture, not real prices. On step 3: the two words to keep are column, one kind of value, and row, one record. Today you will ask the agent to show you the real rows in your own database.
words: 24 · budget: 40 · exception: none (sample values are mock data, counted)
status: n/a

## 6. In this price table, which is a row and which is a column?
type: check
block: Why an app needs memory · 4
visible:
ticker · date · close
NISP.JK · Mon · 1,000
NISP.JK · Tue · 1,010
sample
A. A row is one day for one stock; "close" is a column.
B. "close" is a row; each day is a column.
C. Rows and columns are the same thing.
diagram: The small sample grid from slide 5, two rows, with the grey "sample" tag. The three choices below it.
build:
  0: the grid and the three choices
  1: A highlights green; the Tuesday row and the close column highlight; B and C fade; reveal line appears
reveal: A — A row is one record; a column is one kind of value, like the closing price.
notes:
Read the question aloud and point at the grid. Give the room twenty seconds, then take a show of hands for A, B and C. Many people mix the two up, so do not rush. Click to reveal. A is right: a row runs across and holds one record, here NISP on Tuesday. A column runs down and holds one kind of value, here the closing price for every day. B swaps them; if someone chose B, trace one row with your finger, then one column. C is never right. Remind everyone that the numbers are samples. Then ask one person: if we add BBRI tomorrow, do we get a new row or a new column? Answer: new rows, one per day, with BBRI.JK in the ticker column.
words: 58 (incl. 17-word reveal) · budget: 60 · exception: none
status: n/a

## 7. A watchlist needs two tables: the stocks you follow and their daily prices
type: visual
block: Why an app needs memory · 5
visible:
stocks
ticker · name · added_at
one row per stock you follow
prices
ticker · date · open · high · low · close · volume
one row per stock per day
linked by ticker
diagram: Two table cards side by side. Left card "stocks" with its column line and caption "one row per stock you follow", three short rows with tickers "NISP.JK", "BBRI.JK", "TLKM.JK". Right card "prices" with its column line and caption "one row per stock per day", many thin rows with no numbers. A line joins the ticker column of the left card to the ticker column of the right card, labelled "linked by ticker".
build:
  0: the "stocks" card with its three rows
  1: the "prices" card slides in; its rows fill quickly
  2: the "linked by ticker" line draws; one ticker lights up in both tables
  3: the highlight moves from NISP.JK to BBRI.JK to TLKM.JK on a slow loop
notes:
Now the design the agent will build. On step 0: the first table, stocks, is the watchlist itself. One row per stock you follow: its ticker, its name, and when you added it. Adding TLKM means one new row here; removing it means deleting that row. On step 1: the second table, prices, holds the history: one row per stock per day, with the usual daily values: open, high, low, close and volume. On step 2: the ticker joins them. The app looks up which stocks you follow, then fetches their rows from prices. On step 3, point out that the ticker carries .JK, the Yahoo code for the Indonesia Stock Exchange. You do not need to remember the columns: the spec prompt in the next run names them, so every app comes out the same shape.
words: 30 (incl. 3 diagram-only tickers) · budget: 40 · exception: none
status: n/a

## 8a. Run 1: brainstorm the watchlist, update the spec, then save NISP's price history to a database
type: run
block: Run 1 — database · 15
visible:
**Goal:** Agree the database, write it into the spec, plan it.
**Prompt 1 (brainstorm):**
```text
Let's brainstorm a watchlist for the app. It should keep each stock's daily price history in a database, so the app remembers it after a restart. Ask me one question at a time, at most 3, in plain business language. Don't write any code or files yet.
```
**Prompt 2 (spec):**
```text
Add the price database to docs/spec.md. Use SQLite in backend/data/app.db with two tables: stocks (ticker, name, added_at) and prices (ticker, date, open, high, low, close, volume). POST /api/refresh fills prices from yfinance and returns rows_added. Start with NISP.JK. Don't build anything yet.
```
**Then:** Plan mode (Tab), plan, approve, edit or reject (handout).
**You should see:** Three questions, a summary, an updated docs/spec.md, a plan. No database yet.
**Time:** 15 min
**Stuck?** Checkpoint `s1-chatbot`, then continue.
diagram: Across the top of the card, the loop as four small chips: "brainstorm", "spec", "plan", "build", with brainstorm, spec and plan highlighted and build outlined.
build:
  0: goal, loop chips and Prompt 1
  1: Prompt 2
  2: the "Then" line, "You should see", time and stuck line
handout:
3. Plan (Tab: Plan mode; footer says "plan"):
```text
Read docs/spec.md and give me a numbered step-by-step plan for the price database only. Don't build anything yet.
```
Read the plan against the spec. Approve, edit ("Change step 3 to …") or reject ("This plan builds more than the spec asks for. Make it shorter.").
notes:
Same loop as Session 1, for a new feature. On step 0: send the brainstorm prompt as written. It caps the agent at three questions, because the shape is already decided. Answer each in one short sentence; for example, refresh once a day, keep one year, start with NISP only. If the agent starts writing files, press Esc. On step 1: the spec prompt names the two tables and the refresh endpoint, so you do not need to know them; it adds to the spec you already have. Open docs/spec.md and check the new section is there and the dashboard part is unchanged. On step 2: Tab to Plan mode, send the plan prompt from the handout, and read it before deciding. Look for extras, like a login. These prompts are untested; rehearse them.
words: 51 · budget: 60 · exception: fenced prompts not counted (47 + 42 words); plan prompt (18 words) in handout to keep 2 prompts per slide
status: UNTESTED (brainstorm, spec, handout plan prompt)

## 8b. Run 1: brainstorm the watchlist, update the spec, then save NISP's price history to a database
type: run
block: Run 1 — database · 20
visible:
**Goal:** Build the database, fill it with NISP, look inside.
**Prompt 1 (build, Tab: Build mode):**
```text
Approved. Save that plan to docs/plan.md, then build the price database from it. Fill it with NISP.JK's last year of prices and tell me how many rows were added.
```
**Prompt 2 (look inside):**
```text
Show me what's inside the database in plain words: each table, how many rows it has, and the latest NISP.JK row. Don't change anything.
```
**Then:** commit and push (handout).
**You should see:** Two tables, a row count, the latest NISP row.
**Time:** 20 min
**Stuck?** Checkpoint `s2-database`.
diagram: none
build:
  0: goal and Prompt 1
  1: Prompt 2
  2: the "Then" line, "You should see", time and stuck line
handout:
4. Commit and push:
```text
Commit all changes with the message "Price database". Make sure backend/.env is not committed. Then push to GitHub.
```
If something breaks:
```text
The database [describe what is wrong]. Explain the cause in plain words, then fix it.
```
notes:
On step 0: press Tab back to Build mode; the footer says build. The prompt starts with "Approved", saves the plan and builds it. Building takes a few minutes and the agent may ask to run commands; allow them. While it works, walk the room. On step 1: the second prompt is the point of this run. You cannot open the database file yourself, so you ask the agent to read it for you. Expect two tables, stocks and prices, a row count for prices of roughly one per trading day, and the latest NISP row with a date and a close. Do not judge the price; check that the date is recent. On step 2: commit and push with the handout prompt. That is checkpoint s2-database. Anyone behind switches to it.
words: 43 · budget: 60 · exception: fenced prompts not counted (29 + 24 words); push and fix prompts in handout
status: UNTESTED (build, look-inside, handout push and fix prompts)

## 9. yfinance is free but unofficial, so the app keeps a cached copy
type: visual
block: Run 2 — watchlist · 5
visible:
Yahoo Finance
yfinance: free, unofficial
Slow? Blocked? Changed?
Database + cache
Page: cached as of [date]
diagram: Left: a cloud "Yahoo Finance". A dotted line runs from it through a small connector chip "yfinance: free, unofficial" towards the app on the right. Midway, a shield icon "Database + cache" stands in front of the app. Above the dotted line, three warning chips "Slow? Blocked? Changed?" appear and bounce off the shield. In the corner of the app's page, a small grey label with the last line of visible.
build:
  0: the Yahoo cloud, the connector chip and the app, with data flowing along the line
  1: the line breaks; the three warning chips appear
  2: the shield rises in front of the app; the chips bounce off it; the page stays full
  3: the cached-as-of label appears on the page; the data flow resumes slowly in a loop
notes:
Before the watchlist, one honest point about the data. On step 0: our prices come from Yahoo Finance through yfinance, a free tool written by volunteers. It is not an official Yahoo product. On step 1: that means it can be slow, Yahoo can block a room of thirty people asking at once, and it can change without notice. On step 2: the database you just built is our shield. The watchlist reads from the database, not live, and every checkpoint also ships a cached copy, so the page still works when Yahoo does not. On step 3: when the app shows saved data, it says so, with a "cached as of" date. Ask: why does that label matter for a business user? Because stale numbers presented as fresh mislead people.
words: 15 · budget: 40 · exception: none
status: n/a

## 10a. Run 2: build a watchlist page, add BBRI and TLKM, remove one, and push
type: run
block: Run 2 — watchlist · 12
visible:
**Goal:** A watchlist page that reads from the database.
**Loop:** brainstorm → **spec** → plan → build (handout)
**Spec:**
```text
Add a watchlist to docs/spec.md. Keep the quote, history and chat endpoints unchanged. New: GET /api/watchlist → [{ticker, name, price, change_pct}]; POST /api/watchlist {ticker} → {ticker}, also saving its price history; DELETE /api/watchlist/{ticker} → 204. Prices come from the database. Reject unknown tickers. Don't build anything yet.
```
**Build** (after you approve the plan):
```text
Approved. Save that plan to docs/plan.md, then build the watchlist from it. Adding a ticker must also save its price history. Then tell me how to open the watchlist page.
```
**You should see:** A watchlist page with NISP.
**Time:** 12 min
**Stuck?** Checkpoint `s2-database`, then continue.
diagram: Across the top of the card, the loop as four small chips: "brainstorm", "spec", "plan", "build", with spec highlighted and the others outlined.
build:
  0: goal, loop chips and the spec prompt
  1: the build prompt, "You should see", time and stuck line
handout:
1. Brainstorm:
```text
Let's brainstorm a watchlist page for the app. I want to follow NISP, BBRI and TLKM and add or remove stocks myself. Ask me one question at a time, at most 3, in plain business language. Don't write any code or files yet.
```
2. Spec: the prompt on the slide. Read the update and correct one thing.
3. Plan (Tab: Plan mode; approve, edit or reject):
```text
Read docs/spec.md and give me a numbered step-by-step plan for the watchlist only. Don't build anything yet.
```
4. Build (Tab: Build mode): the prompt on the slide.
notes:
Same loop again, faster; the handout has the brainstorm and plan prompts. On step 0: the spec prompt carries what the agent must not guess. The quote, history and chat endpoints stay as they are, so nothing from Session 1 breaks. Three new endpoints, with the exact shapes the checkpoints use: list, add, remove. Adding a ticker also saves its price history, so the browser test works. Prices come from the database, the shield from the last slide, with the cached-as-of label. Unknown tickers get rejected, so nothing wrong gets saved. Check docs/spec.md, then Tab to Plan mode and send the plan prompt. Read the plan; approve, edit or reject. On step 1: Tab to Build mode and send the build prompt. It takes a few minutes; allow commands when asked. When it finishes, open the page it names. NISP should already be on it, from Run 1. These prompts are untested.
words: 38 · budget: 60 · exception: fenced prompts not counted (47 + 30 words); brainstorm and plan prompts in handout
status: UNTESTED (spec, build, handout brainstorm and plan prompts)

## 10b. Run 2: build a watchlist page, add BBRI and TLKM, remove one, and push
type: run
block: Run 2 — watchlist · 12
visible:
**Goal:** Change the watchlist and see the dashboard follow.
**Steps on the page:**
1. Add BBRI.JK, then TLKM.JK.
2. Try NISP without .JK: expect a clear message.
3. Remove one stock. Refresh the dashboard.
**Push:**
```text
Commit all changes with the message "Watchlist page". Make sure backend/.env is not committed. Then push to GitHub.
```
**You should see:** Added stocks with history; the removed one gone.
**Time:** 12 min
**Stuck?** Checkpoint `s2-watchlist`.
diagram: none
build:
  0: goal and the three steps
  1: the push prompt, "You should see", time and stuck line
handout:
If something is wrong:
```text
The watchlist [describe what is wrong]. Explain the cause in plain words, then fix it.
```
notes:
Now test it the way a user would, in the browser, not in opencode. On step 0, take the three steps in order. First, add BBRI.JK, then TLKM.JK. Each should appear with its price and history, because adding a ticker also fills its rows in the prices table. Second, a deliberate mistake: type NISP without .JK. A good app says the ticker is unknown and saves nothing. If it saves a broken row, fix it with the handout prompt. Third, remove one stock and refresh the dashboard; it should disappear there too. If it does not, hold that thought: the next slide is about exactly that. On step 1: commit and push. That is checkpoint s2-watchlist. This push prompt is untested; rehearse it.
words: 52 · budget: 60 · exception: fenced prompt not counted (18 words); fix prompt in handout
status: UNTESTED (push, handout fix prompt)

## 11. You removed a stock but it's still on the dashboard. What do you tell the agent?
type: check
block: Run 2 — watchlist · 6
visible:
A. "It's broken. Fix it."
B. "I removed TLKM from the watchlist, but the dashboard still shows it after a refresh. Explain why in plain words, then fix it."
C. "Rebuild the whole app."
diagram: none
build:
  0: the question and the three choices
  1: B highlights green; A and C fade; reveal line appears
reveal: B — It says what you did, what you expected and what you saw, and asks for the cause before the fix.
notes:
This happens in real projects, and in some of your apps it may have just happened. Read the three choices aloud and vote by hand. A feels natural, but the agent must guess what "it" is, and it may change the wrong thing. C throws away an hour of work for one small fault, and the new build may have new faults. Click to reveal B. It names the action, removing TLKM; the expected result; and what you actually saw, after a refresh. Then it asks for an explanation first, so you learn the cause; a likely one is that the dashboard still keeps its own list instead of reading the watchlist. That is the same habit as Session 1: paste the real error, ask to explain, check the fix yourself. If your app had this fault, send B now.
words: 55 (incl. 21-word reveal) · budget: 60 · exception: none (quiz choices)
status: n/a

## 12. A chatbot knows what it was trained on, not your rules
type: visual
block: Why the chatbot needs knowledge · 5
visible:
Model
Trained on: general text, up to a cut-off date
Missing: your rules · recent OJK pages · your app's data
Result: guesses, or out of date
diagram: A large rounded box "Model" shaped like a bookshelf, mostly full of grey books labelled together "Trained on: general text, up to a cut-off date". One shelf has a visible gap with a dashed outline; three faded book spines float outside it, labelled "Missing: your rules · recent OJK pages · your app's data". Below the box, a speech bubble "Result: guesses, or out of date" with a small question mark.
build:
  0: the bookshelf "Model", full of grey books
  1: the "Trained on" label appears
  2: the gap on one shelf appears; the three missing books float beside it, drifting slowly
  3: the result bubble appears under the model
notes:
Switch to the chatbot. On step 0: the model behind your chatbot learned from a huge amount of general text. On step 1: that learning stopped at a cut-off date, and it was general, not about your company. On step 2: so some things are not on its shelf. Your company's own rules. Anything OJK published after the cut-off, or pages it rarely saw. And your app's data, which is why in Session 1 the back end added NISP's prices to every request. On step 3: when asked about something missing, a model does not always say "I don't know". It may answer smoothly and be wrong or out of date. For questions about regulation, that is a real risk. The fix is the same as for prices: put the right text in front of it.
words: 25 · budget: 40 · exception: none
status: n/a

## 13. The system message sets the chatbot's role and rules; you write it
type: visual
block: Why the chatbot needs knowledge · 5
visible:
system: role and rules (you write it)
user
assistant
Role: answer stock questions for business users
Rules: name the source · say I don't know · no buy/sell advice
diagram: The message stack from Session 1 slide 6: role chips "system", "user", "assistant" stacked vertically. The system box grows and lifts forward, labelled "system: role and rules (you write it)". Two sticky notes attach to it: "Role: answer stock questions for business users" and "Rules: name the source · say I don't know · no buy/sell advice". The user and assistant boxes stay small and faded below.
build:
  0: the three-box stack from Session 1, small
  1: the system box grows and lifts forward with its label
  2: the Role sticky note attaches
  3: the Rules sticky note attaches; the system box glows softly in a loop
notes:
Remember this list from Session 1? Every request is a list of messages with roles. On step 0: system, user, assistant. In Session 1 we said the system message holds the rules and the role, written by whoever builds the app. On step 1: today, that is you. The system message goes at the top of every request, before the user's question, so the model reads it every turn. On step 2: it says who the chatbot is: here, an assistant that answers stock questions for business users. On step 3: and what it must always do: name the Wiki page or data it used, say when it does not know, and never advise buying or selling. Ask: which of these rules matters most for a bank? Usually the last one. You write this text yourself in Run 3.
words: 28 (incl. 1-word diagram label "system") · budget: 40 · exception: none
status: n/a

## 14. A Wiki is a set of pages the chatbot reads before it answers
type: visual
block: Why the chatbot needs knowledge · 5
visible:
Question
Find the matching Wiki page
Page + question → model
Answer + source link
wiki/ = short Markdown pages
diagram: Four boxes left to right, joined by arrows: a speech bubble "Question"; a folder "wiki/ = short Markdown pages" with three page icons, one of which lifts out labelled "Find the matching Wiki page"; a box "Page + question → model" showing the page and the bubble entering the model; a reply bubble "Answer + source link" with a small link chip.
build:
  0: the "Question" bubble
  1: the wiki folder appears; one page lifts out
  2: the page and the question travel together into the model
  3: the answer bubble appears with its link chip; a soft pulse runs along the arrows in a loop
notes:
So how do we put the right text in front of the model? A Wiki. On step 0: a user asks a question. On step 1: the back end looks in a folder called wiki, a few short text pages, and picks the ones whose words match the question. No magic: it is a search by keywords. On step 2: it sends the matching page together with the question, inside the context window you saw in Session 1. So the model answers from the page, not from memory. On step 3: because it knows which page it used, it can say so, with the link. The Wiki stays small on purpose: a few pages, each short. You can open and read every page yourself, which is the point: you can check what the chatbot knows.
words: 16 · budget: 40 · exception: none
status: n/a

## 15. Only official sources go in: ojk.go.id and idx.co.id, each page with its link
type: visual
block: Why the chatbot needs knowledge · 5
visible:
ojk.go.id ✓
idx.co.id ✓
Blogs · forums · social posts ✗
wiki/
One Wiki page per source, URL at the top
diagram: A gate in the centre with a green tick on it. From the left, five page cards slide towards it on a conveyor. Two cards "ojk.go.id ✓" and "idx.co.id ✓" pass through the gate into a folder labelled "wiki/". Three cards "Blogs · forums · social posts ✗" bounce off the gate and fade, each with a red cross. Under the folder, a page card shows a URL bar at its top, captioned "One Wiki page per source, URL at the top".
build:
  0: the gate and the empty wiki folder
  1: the two official cards pass through the gate into the folder
  2: the three other cards bounce off and fade
  3: the page card with the URL bar appears under the folder; new cards keep arriving slowly in a loop
notes:
What goes into the Wiki decides what the chatbot says, so we are strict. On step 1: two sources only. ojk.go.id is the Financial Services Authority, the regulator. idx.co.id is the Indonesia Stock Exchange. On step 2: anything else bounces: blogs, forums, social media posts, even good articles that summarise the rules. They may be out of date or wrong, and the web search in Run 3 may find some of them. Your job is to check the address of every page before it goes in. On step 3: one Wiki page per source page, with its web address at the top. That address is what the chatbot shows as its source, and what you click to check it. If the agent offers a page from another site, say no.
words: 16 · budget: 40 · exception: none
status: n/a

## 16a. Run 3: ask three OJK questions, build the Wiki from official sources, then ask again
type: run
block: Run 3 — Wiki + system prompt · 20
visible:
**Goal:** Baseline, then a Wiki plan.
**Loop:** brainstorm → **spec** → plan → build (handout)
**1. Ask your chatbot; note each answer:**
"What does OJK supervise?" · "What is an auto-rejection limit on IDX?" · "What should I check before investing?"
**2. Brainstorm, then spec:**
```text
Add a Wiki to docs/spec.md: Markdown pages in wiki/, one page per official source, ojk.go.id or idx.co.id only, each with its source URL at the top. The chatbot reads the matching pages before it answers. I'll write the system prompt. Don't build anything yet.
```
**3. Plan, save, find pages:**
```text
Find official investor-education pages on ojk.go.id and idx.co.id that explain what OJK supervises, what an auto-rejection limit is, and what to check before investing. Search if you can; otherwise open those sites directly. List each URL with a one-line summary. Don't save anything yet.
```
**You should see:** Only ojk.go.id or idx.co.id URLs.
**Time:** 20 min
**Stuck?** Checkpoint `s2-watchlist`.
diagram: Across the top of the card, the loop as four small chips: "brainstorm", "spec", "plan", "build", with spec highlighted and the others outlined, as in Session 1 slide 24b.
build:
  0: goal, loop chips and step 1 (the three questions)
  1: step 2, the spec prompt
  2: step 3 and the find-pages prompt, "You should see", time and stuck line
handout:
1. Brainstorm (do this before the spec):
```text
Let's brainstorm a Wiki for the chatbot: short pages of investor-education facts from ojk.go.id and idx.co.id only. Ask me one question at a time, at most 3, in plain business language. Don't write any code or files yet.
```
2. Spec: the prompt on the slide. Read the update and correct one thing.
3. Plan (Tab: Plan mode; approve, edit or reject):
```text
Read docs/spec.md and give me a numbered step-by-step plan for the Wiki only. Don't build anything yet.
```
4. Save (Tab: Build mode):
```text
Approved. Save that plan to docs/plan.md. Don't build anything yet.
```
5. Find pages: the prompt on the slide. The build is on the next slide.
notes:
Facilitator setup: opencode's webfetch tool opens pages directly; setting OPENCODE_ENABLE_EXA=1 before starting opencode adds a web search tool, no key needed. On step 0: a baseline. Ask your chatbot the three questions in the browser and note each answer; we compare after the Wiki. On step 1: same loop as Runs 1 and 2. Brainstorm first with the handout prompt, then send the spec: two sites only, one page per source, the address on top, your own system prompt. On step 2: plan and save with the handout, without building; you choose the sources first. Then send the find-pages prompt. Read every address; drop anything not on ojk.go.id or idx.co.id. Only if finding pages fails, use checkpoint s2-wiki. All prompts are untested.
words: 59 · budget: 60 · exception: fenced prompts not counted (44 + 44 words); brainstorm, plan and save prompts in handout
status: UNTESTED (spec, find-pages, handout brainstorm, plan and save prompts; opencode 1.19.5 webfetch reached an ojk.go.id page, websearch only with OPENCODE_ENABLE_EXA=1)

## 16b. Run 3: ask three OJK questions, build the Wiki from official sources, then ask again
type: run
block: Run 3 — Wiki + system prompt · 17
visible:
**Goal:** Wiki pages, your system prompt, better answers.
**1. Build the Wiki:**
```text
Turn the pages you found into Wiki pages in wiki/, one Markdown file per page, with its URL at the top. Only use what the page says. Then connect the Wiki to the chatbot as the plan says.
```
**2. Your system prompt** (edit the wording if you like):
```text
Set the chatbot's system prompt to: You answer questions about Indonesian stocks for business users, using the Wiki and the app's data. Cite the Wiki page URL you used. If you don't know, say so. If asked what to buy or sell, give facts and risks only, no recommendation.
```
**3. Ask the same three questions again.** Then push (handout).
**You should see:** Answers that name a Wiki page and its URL.
**Time:** 17 min
**Stuck?** Checkpoint `s2-wiki`.
diagram: none
build:
  0: goal and step 1
  1: step 2, the system prompt
  2: step 3, "You should see", time and stuck line
handout:
Test the rule, too: ask "Should I buy NISP?" It should give facts and risks only, no recommendation.
Commit and push:
```text
Commit all changes with the message "Wiki and system prompt". Make sure backend/.env is not committed. Then push to GitHub.
```
notes:
On step 0: the build prompt turns the pages you approved into Wiki files. "Only use what the page says" stops the agent from filling gaps with its own knowledge. Open one file in wiki: check the address on top and skim the text. On step 1: this is your system prompt. Change the wording if you want, but keep the three rules: cite the Wiki page URL, say when it does not know, and on buy or sell questions give facts and risks only, no recommendation. On step 2: ask the same three questions, in the same words, and compare with your note. Look for the page name and address in each answer. Also ask "Should I buy NISP?" from the handout; expect facts and risks, no recommendation. Then commit and push: checkpoint s2-wiki. These prompts are untested; rehearse the whole run.
words: 50 · budget: 60 · exception: fenced prompts not counted (38 + 49 words); push prompt in handout
status: UNTESTED (Wiki build, system prompt, handout push prompt)

## 17. The chatbot quotes a rule but gives no source. Is that good enough?
type: check
block: Run 3 — Wiki + system prompt · 4
visible:
A. Yes. It sounds right.
B. No. Ask which Wiki page it used. No page? Fix the system prompt or add the page.
C. No. Switch to a bigger model.
diagram: none
build:
  0: the question and the three choices
  1: B highlights green; A and C fade; reveal line appears
reveal: B — An answer without a source cannot be checked, and the system prompt says to name one.
notes:
Read the question and vote by hand. A is the trap: sounding right is exactly what a model is good at, even when it is wrong. For a rule from a regulator, a smooth answer you cannot check is not good enough. C may help a little, but a bigger model still cannot name a page it never read. Click to reveal B. Two possible causes. Either the system prompt does not insist on a source, so you strengthen that rule; or there is no Wiki page for that question, so the model answered from memory, and you add an official page or accept "I don't know". Ask: in your own job, would you forward a regulatory answer to a client without a link? That is the standard.
words: 47 (incl. 17-word reveal) · budget: 60 · exception: none (quiz choices)
status: n/a

## 18. Before and after: the same question, now with a source
type: visual
block: Run 3 — Wiki + system prompt · 4
visible:
Same question
Illustrative
Before: an answer, no source
Illustrative
After: an answer from the Wiki + its URL
Compare: source · matches the page · says I don't know
diagram: One question bubble "Same question" at the top centre, with two arrows down to two answer cards side by side. Left card "Before: an answer, no source" with a grey "Illustrative" tag in its corner: grey placeholder lines of text, no link. Right card "After: an answer from the Wiki + its URL" with the same grey "Illustrative" tag: placeholder lines and a link chip shaped like an address bar, with no real URL text. Under both cards a checklist strip with the last line of visible. No real answer text appears on the slide.
build:
  0: the question bubble
  1: the Before card appears
  2: the After card appears; its link chip pulses gently
  3: the compare strip appears
notes:
Both cards are tagged Illustrative: they show the pattern, not real output. Your class's real before and after answers may differ, so compare your own. Do the comparison together. Ask two or three volunteers to read one question aloud with both answers: the note from before and the new one. On step 1: the before answer may be fine, vague or wrong; we do not know, and neither does the reader, because there is no source. On step 2: the after answer names a Wiki page and its address. Click the link and check that the page really says it. On step 3: compare three things. Is there a source? Does the answer match the page? And when the Wiki has nothing, does it say "I don't know" instead of guessing? This is the before-and-after record from the session goals. If an answer is still weak, the fix is a better page or a stricter system prompt.
words: 26 · budget: 40 · exception: none
status: n/a

## 19. Data lives in the database, knowledge in the Wiki, behaviour in the system prompt
type: recap
block: Close + Q&A · 4
visible:
Database: data
prices · watchlist
Wiki: knowledge
OJK and IDX pages
System prompt: behaviour
role · rules
Checkpoint: s2-wiki
diagram: Three boxes side by side, each with an icon: a cylinder "Database: data" with "prices · watchlist" under it; a book "Wiki: knowledge" with "OJK and IDX pages" under it; a speech bubble with a gear "System prompt: behaviour" with "role · rules" under it. All three feed one arrow into a small chatbot icon. Checkpoint line at the bottom.
build:
  0: title
  1: the database box appears
  2: the Wiki box appears
  3: the system prompt box appears; arrows join into the chatbot; checkpoint line appears
notes:
Do not re-teach; link each box to what they did. On step 1: the database holds data. You built it in Run 1 and the watchlist reads from it, so the app remembers prices and the stocks you follow, even when Yahoo is down. On step 2: the Wiki holds knowledge: a few official pages that the chatbot reads before it answers, so it can name a source. On step 3: the system prompt holds behaviour: who the chatbot is and the rules it follows. You wrote it yourself. When something is wrong later, this split tells you where to look: wrong number, check the database; wrong fact, check the Wiki; wrong tone or advice, check the system prompt. Anyone not finished can switch to checkpoint s2-wiki for Session 3.
words: 17 · budget: 40 · exception: none
status: n/a

## 20. Questions
type: Q&A
block: Close + Q&A · 10
visible:
Questions?
diagram: Large "Questions?" heading. Around it, five small shapes keep moving on slow loops: three square speech bubbles drifting along different paths, one red question mark orbiting the heading, and one dot bouncing between the bubbles. No text inside the shapes.
build:
  0: heading and moving shapes (they loop for as long as the slide is open)
notes:
Open the floor. If no one speaks, start with a prompt: which official page surprised you? Or: what would you put in a Wiki for your own team? Collect parking-lot items on a flip chart. Repeat each question before answering so the room hears it. Keep investment questions neutral: the app shows data and official facts; it does not advise. If a question is about how the database or the Wiki works inside, say Day 4 looks at the back end in more detail. Use the last minutes to check that everyone has pushed, and that anyone behind has checkpoint s2-wiki and the recovery sentence from the handout.
words: 1 · budget: 40 · exception: none
status: n/a

## 21. Next session: turn your data into a report and a deck
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
Preview Session 3 in one minute. Today the app learned to remember prices and to answer rules questions with a source. In Session 3 you use that data. First, the agent writes a NISP analysis report from your own database, and you check every number against the dashboard. Then it turns the report into a PowerPoint deck, and you improve it with feedback. Finally, you save the whole process as a workflow and run it again on TLKM. Same method: brainstorm, spec, plan, build, test. Keep your project, or use checkpoint s2-wiki. Thank everyone and close.
words: 23 · budget: 40 · exception: none
status: n/a

## Word count check

| id | type | words | budget | over? | notes words |
|---|---|---|---|---|---|
| 1 | title | 10 | 40 | no | 123 |
| 2 | visual | 21 | 40 | no | 130 |
| 3 | talk | 19 | 40 | no | 131 |
| 4 | visual | 21 | 40 | no | 131 |
| 5 | visual | 24 | 40 | no | 134 |
| 6 | check | 58 (incl. reveal) | 60 | no | 128 |
| 7 | visual | 30 | 40 | no | 137 |
| 8a | run | 51 | 60 | no | 134 |
| 8b | run | 43 | 60 | no | 132 |
| 9 | visual | 15 | 40 | no | 131 |
| 10a | run | 38 | 60 | no | 152 |
| 10b | run | 52 | 60 | no | 123 |
| 11 | check | 55 (incl. reveal) | 60 | no | 140 |
| 12 | visual | 25 | 40 | no | 136 |
| 13 | visual | 28 (incl. diagram label "system") | 40 | no | 139 |
| 14 | visual | 16 | 40 | no | 135 |
| 15 | visual | 16 | 40 | no | 130 |
| 16a | run | 59 | 60 | no | 122 |
| 16b | run | 50 | 60 | no | 143 |
| 17 | check | 47 (incl. reveal) | 60 | no | 128 |
| 18 | visual | 26 | 40 | no | 157 |
| 19 | recap | 17 | 40 | no | 130 |
| 20 | Q&A | 1 | 40 | no | 108 |
| 21 | talk | 23 | 40 | no | 96 |

slides: 24 · minutes: 180
