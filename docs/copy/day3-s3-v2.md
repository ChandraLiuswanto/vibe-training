# Day 3 · Session 3 — slide copy v2 (visual, 3 runs)

Course: AI Vibe Coding for Business Users · Session 3: AI-powered reports and presentations · 3 hours · English deck, speaker-led and hands-on.
Sources: `docs/outlines/day3-s3-v2.md` (approved outline v2, 20 headlines, kept word for word), `docs/superpowers/specs/2026-11-11-day3-design.md` (§3 S3 objectives, §7 S3, §8 app and checkpoints), `docs/superpowers/plans/2026-11-11-day3-build.md` (fixed app interface, Task 5), `docs/copy/day3-s1-v2.md` (format and prompt style).

How to read this file:
- `visible:` is the on-slide text. Every label the diagram shows is listed in `visible:`; the `diagram:` line says where it goes. Quoted labels in `diagram:` that are not in `visible:` are counted too.
- `build:` lists the click steps. Step 0 is what shows when the slide arrives.
- Prompts in fenced blocks are not counted toward the word budget. `handout:` holds prompts that go in the printed handout, not on the slide.
- `status: UNTESTED` means the prompt was written for this copy and has not been run in opencode; rehearse it before class. No Session 3 prompt has been tested yet.
- Any number shown on a slide is a round, labelled sample. No real NISP or TLKM prices are quoted anywhere.

## 1. AI-powered reports and presentations
type: title
block: Opening · 2
visible:
Day 3 · Session 3
AI Vibe Coding for Business Users
diagram: none
build:
  0: title, subtitle and session line together
notes:
Welcome back for the last session of the day. This morning you built a NISP dashboard and a chatbot. In Session 2 your app got a database, a watchlist and a Wiki. Now we use all of that. In the next three hours the AI writes a report from your own data, turns it into a PowerPoint deck, and then you save the whole job so it runs again with one command. Before we start, check that opencode opens and that your app still starts: the page on localhost:5173 and the server on port 8000. Anyone whose app does not start, raise your hand now; the next slide gives you a way back in. Same rhythm as before: I explain for a few minutes, you do it, we check together.
words: 10 · budget: 40 · exception: none
status: n/a

## 2. Today the AI turns your app's data into a report and a slide deck
type: visual
block: Opening · 4
visible:
Your database: stocks, prices
Report: NISP-report.html
Deck: NISP-deck.pptx
Saved workflow: same job for TLKM
diagram: Three shapes left to right joined by arrows. Left: a database cylinder "Your database: stocks, prices". Middle: a document page "Report: NISP-report.html" with a small table, a line chart and one highlighted sentence drawn as grey lines (no numbers). Right: a stack of three slide cards "Deck: NISP-deck.pptx". Under all three, a curved arrow loops from the deck back to the database, labelled "Saved workflow: same job for TLKM". A dot travels the main arrows slowly on a loop.
build:
  0: the database cylinder
  1: the arrow draws; the report page appears, its table, chart and sentence filling in
  2: the arrow draws; the three slide cards fan out
  3: the loop arrow and its label appear; the travelling dot starts
notes:
Say what the session produces, in business words. On step 0: your database already holds two tables from Session 2. "stocks" is your watchlist; "prices" is the daily history. On step 1: in Run 1 the AI writes a NISP analysis report as a web page, built only from that database, and you check every number. On step 2: in Run 2 it turns the report into a PowerPoint deck, and you improve the deck with two rounds of feedback. On step 3: in Run 3 you save the steps as one opencode command, then run it on TLKM to get a new report and deck. Point out that the report describes data. Like the chatbot, it never tells anyone to buy or sell. The skill you practise all afternoon is judging the AI's work, not typing.
words: 14 · budget: 40 · exception: none
status: n/a

## 3. Start from your own app or switch to checkpoint s2-wiki
type: talk
block: Opening · 4
visible:
Your app works? Carry on.
Behind or broken? Send this to opencode:
```text
Replace my project with checkpoint s2-wiki from [CHECKPOINT URL], keep my .env.
```
Then start the app and open localhost:5173.
diagram: none
build:
  0: all lines together
notes:
Keep this short. Everyone needs the Session 2 app: the watchlist page, prices in the database, and the chatbot with its Wiki. If yours runs, carry on with your own project; you will learn more from your own app. If yours is broken or you missed part of Session 2, send this one sentence to opencode. It replaces your project with checkpoint s2-wiki and keeps your .env file, so your LLM key still works. The sentence is also in the handout, so nobody has to type it from the screen. When it finishes, start the app the way you did before and open localhost:5173. Check that NISP shows on the dashboard. Walk the room for two minutes and confirm every screen shows the app before moving on.
words: 19 · budget: 40 · exception: fenced recovery prompt not counted (12 words)
status: n/a (recovery sentence from spec §8.6; [CHECKPOINT URL] is a placeholder)

## 4. A prompt does one thing; a workflow runs many steps in order
type: visual
block: Workflows · 6
visible:
Prompt: one request, one result
Workflow: refresh → report → deck → check
One command starts the chain
diagram: Two rows. Top row: a single box "Prompt: one request, one result" with a chat bubble going in and one document coming out. Bottom row: four boxes joined by arrows, "refresh", "report", "deck", "check", with the row label "Workflow:" on the left. Above the first box of the bottom row, a small command chip; the caption "One command starts the chain" sits under the row. A dot runs along the bottom chain on a loop, lighting each box in turn.
build:
  0: the top row: one prompt box, bubble in, document out
  1: the bottom row's four grey boxes appear
  2: the command chip appears; the dot runs refresh → report → deck → check, each box lighting as it passes
  3: caption appears; the dot keeps looping
notes:
Compare two ways of getting work done. On step 0: a prompt is what you have typed all day. One request, one result, and then the agent waits for you. On step 1: a workflow is a chain of steps that always happen in the same order. Ours, by the end of today, will refresh the prices, write the report, build the deck and check the numbers. On step 2: point at the dot. You start it once and it runs each step in order, without you typing four prompts. On step 3: the caption. One command starts the whole chain. Ask the room: which of your monthly tasks are the same steps every time? A monthly sales summary, a board pack, a branch report. Those are workflow candidates.
words: 15 · budget: 40 · exception: none
status: n/a

## 5. Prompt, skill and workflow are three levels of reuse
type: visual
block: Workflows · 7
visible:
Prompt: used once
Skill: expertise loaded when needed
Workflow: steps saved as a command
Session 1: prompts and skills
Today: workflows
diagram: Three steps rising left to right like a staircase, each higher than the last: "Prompt: used once", "Skill: expertise loaded when needed", "Workflow: steps saved as a command". A small figure stands on the second step. Under the first two steps a grey bracket "Session 1: prompts and skills"; under the third a red bracket "Today: workflows". The same staircase style as Session 1 slide 15.
build:
  0: the empty staircase
  1: "Prompt" and "Skill" steps appear; the grey Session 1 bracket; the figure lands on step 2
  2: the "Workflow" step appears in red; the figure climbs onto it
  3: the red "Today: workflows" bracket appears
notes:
This is the staircase from this morning, now with the top step filled in. On step 1: in Session 1 you met two of these. A prompt is used once: you type it, you get an answer, it is gone. A skill is a packaged playbook the agent loads only when the task matches its description, like the brainstorming skill. On step 2: a workflow is the next level. It saves a whole sequence of steps under one command, so you can run it again tomorrow or next month. On step 3: that is today's work. A useful test: if you only need it now, it is a prompt. If it is know-how the agent should use whenever it fits, it is a skill. If it is the same steps in the same order every time, it is a workflow. AGENTS.md still holds the standing rules underneath all three.
words: 21 · budget: 40 · exception: none
status: n/a

## 6. Is each of these a prompt, a skill or a workflow?
type: check
block: Workflows · 7
visible:
1. "Summarise this report in three bullets."
2. A playbook for writing reports, loaded when you ask for one.
3. /stock-report TLKM.JK: refresh, report, deck, check.
A. 1 prompt · 2 skill · 3 workflow
B. 1 skill · 2 workflow · 3 prompt
C. All three are prompts
diagram: none
build:
  0: question, the three items and the three choices
  1: A highlights green; B and C fade; reveal line appears
reveal: A — A one-off request is a prompt, loaded expertise is a skill, and a saved chain of steps is a workflow.
notes:
Read the three items aloud. Give thirty seconds, then take a show of hands for A, B and C, one at a time. Click to reveal. A is right. Item 1 is a one-off request, so it is a prompt. Item 2 is know-how the agent picks up when a task matches, so it is a skill. Item 3 starts a chain of four steps with one command, so it is a workflow. If someone picks C, they have a point worth honouring: under the hood, a saved command does send text to the agent. The difference is reuse. You write it once, save it, and run it again on any ticker. Item 3 is exactly what you will build in Run 3, so tell them to remember its shape.
words: 45 · budget: 60 · exception: none
status: n/a

## 7. A good analysis report has data, charts and an insight you can defend
type: visual
block: Run 1 — report · 5
visible:
Summary table
Price chart
Key stats
Insight
Every number traces to your database
Sample
diagram: A report page in the centre, built from four blocks stacked top to bottom: "Summary table" (a small grid of grey cells with round placeholder values and a small "Sample" tag), "Price chart" (a line drawn left to right), "Key stats" (three small tiles with grey bars, no numbers), "Insight" (one sentence drawn as a highlighted grey line). On the right edge, thin dotted lines run from each block to a small database cylinder; the caption "Every number traces to your database" sits under the page.
build:
  0: the empty page and the database cylinder
  1: "Summary table" and "Price chart" drop in
  2: "Key stats" tiles drop in
  3: "Insight" line appears, highlighted
  4: the dotted lines draw from each block to the database; caption fades in
notes:
Before we ask the AI for a report, agree what good looks like. On step 1: a summary table, for example the latest close, the one-year high and low. The values on the slide are samples, not NISP numbers. Then a price chart from the prices table. On step 2: a few key stats, such as the change over the year. On step 3: one insight, a sentence that says what the data shows. "Defensible" means you can point to the rows that prove it. On step 4: the most important part. Every number on the page comes from your own database, the same one your dashboard reads. That is how you will check it: if the report and the dashboard disagree, one of them is wrong. Ask: who reads this report at your company, and what would they want first?
words: 14 · budget: 40 · exception: none
status: n/a

## 8a. Run 1: spec the report, generate it from your database, and check every number
type: run
block: Run 1 — report · 15
visible:
**Goal:** reports/NISP-report.html, made from your database.
**Same loop:** brainstorm → **spec** → plan → build (see handout)
**Spec:**
```text
Add a NISP report to docs/spec.md: reports/NISP-report.html, made only from the stocks and prices tables in our SQLite database. Sections: summary table, 1-year price chart, key stats, one insight the data supports. Every number must come from the database. Don't build anything yet.
```
**Build** (Build mode, after you approve the plan):
```text
Approved. Save that plan to docs/plan.md, then build reports/NISP-report.html from it. Tell me how to open it.
```
**You should see:** A report page in your browser.
**Time:** 15 min
**Stuck?** Raise your hand.
diagram: Across the top of the card, the loop as four small chips: "brainstorm", "spec", "plan", "build", with "spec" and "build" highlighted and the others outlined.
build:
  0: goal, loop chips and the spec prompt
  1: the build prompt, "You should see", time and stuck line
handout:
1. Brainstorm:
```text
Let's brainstorm a NISP analysis report made from our database. Ask me one question at a time, at most 3, in plain business language: who reads it, what goes in it, what counts as a defensible insight. Don't write any code or files yet.
```
2. Spec: the prompt on the slide. Read the update and correct one thing.
3. Plan (Tab: Plan mode; approve, edit or reject):
```text
Read docs/spec.md and give me a numbered step-by-step plan for the report only. Don't build anything yet.
```
4. Build (Tab: Build mode, once approved): the prompt on the slide.
notes:
Same loop as this morning, at speed; the handout has every prompt. Brainstorm first: the agent asks up to three questions. Answer in one short sentence each, and say who the reader is. On step 0, the spec. It names the file, the two tables, the four sections, and the rule that every number comes from the database. Read what the agent writes and correct one thing. Then Tab to Plan mode and ask for the plan. Approve, edit or reject; check it reads the database and does not fetch live prices. On step 1: Tab back to Build mode and send the build prompt. The agent may ask to run commands; allow them. Open the file in your browser. All these prompts are untested, so rehearse them before class. Anyone far behind can wait for the s3-report checkpoint at the end of Run 1.
words: 39 · budget: 60 · exception: fenced prompts not counted (43 + 17 words); brainstorm and plan prompts moved to handout to keep 2 prompts per slide
status: UNTESTED (spec, build, and both handout prompts)

## 8b. Run 1: spec the report, generate it from your database, and check every number
type: run
block: Run 1 — report · 12
visible:
**Goal:** Every number checked, then pushed.
**1. Ask the agent to show its sources:**
```text
List every number in reports/NISP-report.html. For each one, show the database query that gives it and the value the query returns. Mark any number that doesn't match. Don't change any files yet.
```
**2. Check 3 numbers yourself** against your dashboard.
**3. Push:**
```text
Commit all changes with the message "NISP report". Then push to GitHub.
```
**You should see:** Every number matched, and the commit on GitHub.
**Time:** 12 min
**Stuck?** Checkpoint `s3-report`.
diagram: none
build:
  0: goal and step 1
  1: step 2
  2: step 3, "You should see", time and stuck line
notes:
A report you have not checked is a draft. On step 0: send the first prompt. It asks the agent to show, for every number, where it came from: the query and the value it returns. "Don't change any files yet" keeps it from quietly fixing things before you see them. Read the list. Anything marked as not matching, ask the agent to explain why and fix it. On step 1: the agent checking its own work is not enough. Pick three numbers, for example the latest close, and compare them with your dashboard, which reads the same database. On step 2: commit and push. Open github.com and look for the reports folder. Both prompts are untested. Anyone whose report never appeared switches to checkpoint s3-report now, so they are ready for Run 2.
words: 41 · budget: 60 · exception: fenced prompts not counted (32 + 12 words)
status: UNTESTED (both prompts)

## 9. AI can write confident insights the data doesn't support
type: visual
block: Run 1 — report · 6
visible:
Supported: a number from your prices table
Unsupported: a reason the data can't show
Ask: which rows prove this?
diagram: Two claim cards side by side, each a speech bubble resting on a base. Left card "Supported: a number from your prices table" rests on three solid pillars, each pillar a small table row drawn as grey cells. Right card "Unsupported: a reason the data can't show" rests on nothing; a crack runs through it and it tilts. Under both, the question "Ask: which rows prove this?" in red.
build:
  0: both claim cards, level, with no base visible
  1: the left card's three row-pillars rise under it
  2: nothing rises under the right card; it cracks and tilts slowly, rocking on a loop
  3: the red question appears
notes:
The numbers were the easy check. The words are harder. On step 0: two sentences from a report. Both sound equally sure of themselves. On step 1: the left one is a fact your database can prove, such as how much the close changed over the year. You can point at the rows. On step 2: the right one gives a reason, such as investors trusting the bank or a market mood. Your database holds dates and prices. It holds nothing about why people bought or sold, so the claim stands on nothing, even though it reads well. AI models are good at writing sentences that sound right. On step 3: one question catches most of these. Ask the agent, or yourself: which rows prove this? If the answer is none, cut the sentence or rewrite it as a fact.
words: 19 · budget: 40 · exception: none
status: n/a

## 10. Which claim in this report does the data not prove?
type: check
block: Run 1 — report · 7
visible:
Sample report, illustrative numbers:
A. The close rose 10% over the year.
B. Average daily volume was 1,000,000 shares.
C. The price rose because investors trust the bank's management.
diagram: A report page frame with a grey "Sample" tag in the corner. The three claims sit inside as highlighted sentences, one under the other.
build:
  0: question, the sample tag and the three claims
  1: C highlights red; A and B get green ticks; reveal line appears
reveal: C — The prices table shows that the price moved, not why.
notes:
Read the three claims aloud. Stress that these are sample numbers on a made-up report, not NISP's real figures. Give thirty seconds, then vote by hand. Click to reveal. C is the one the data does not prove. A and B could each be checked with a query on the prices table: the close at two dates, and the average of the volume column. C gives a cause. Your database has no column for trust or management. The sentence might even be true, but this report cannot show it. Then ask everyone to open their own report and look at its insight. Does it pass the "which rows prove this?" test? If not, ask the agent to rewrite it as a fact the data supports. Replace C with a real unsupported claim from the reference build once it is tested.
words: 29 · budget: 60 · exception: none
status: n/a (claims are illustrative; C is a placeholder for a real claim from the reference build)

## 11. A report is for reading; a deck is for telling
type: visual
block: Run 2 — deck + feedback · 5
visible:
Report: read alone, every detail
Deck: told aloud, one point per slide
diagram: Left: a long report page densely filled with grey lines, a small table and a chart, labelled "Report: read alone, every detail". Right: three slide cards in a row, each with one short title bar and one big element (a chart, a single large tile, one sentence), labelled "Deck: told aloud, one point per slide". Between them, arrows lift the chart, one tile and the insight line out of the page and drop each onto its own slide.
build:
  0: the dense report page
  1: the chart lifts out and lands on slide card 1
  2: one stat tile lands on slide card 2
  3: the insight line lands on slide card 3; the right label appears
notes:
Your report is done. Now the same content has to work in a meeting. On step 0: a report is read alone, at the reader's pace. It can hold every detail, because the reader can stop and look. On step 1: a deck is different. Someone talks while the room looks. So each slide carries one point. The chart moves to its own slide. On step 2: one key number, shown large. On step 3: the insight, as a sentence. Notice that nothing new is invented. Every slide takes something that was already in the report, with the same numbers. That is the rule for Run 2: the deck may cut and reorder, but it may not add facts. Ask: how many slides do your managers sit through in a monthly review?
words: 12 · budget: 40 · exception: none
status: n/a

## 12. Give feedback like a brief: what, why and an example
type: visual
block: Run 2 — deck + feedback · 6
visible:
"Make it better."
What: titles state the point
Why: managers may read only the titles
Example: not "Price chart" but what the chart shows
diagram: Left: a small grey speech bubble "Make it better." with a question mark over a robot. Right: a feedback card with three labelled rows, "What", "Why", "Example", each with the text from visible. A green tick appears on the card.
build:
  0: the vague bubble and the confused robot
  1: the card appears; the "What" row fills in
  2: the "Why" row fills in
  3: the "Example" row fills in; the green tick appears
notes:
Feedback to an AI works like a brief to a colleague. On step 0: "make it better" gives the agent nothing to aim at, so it guesses, and you get random changes. On step 1: say what to change, specifically. Here: every slide title should state the point. On step 2: say why. The reason helps the agent make good choices you did not spell out. Here: managers may read only the titles. On step 3: give an example. Instead of the label "Price chart", a title that says what the chart shows. The example shows the agent the standard you mean. Three parts: what, why, example. You will use exactly this pattern in Run 2, twice. Remind them: feedback is about form and story. It should never ask the agent to change a number.
words: 24 · budget: 40 · exception: none
status: n/a

## 13a. Run 2: turn the report into PowerPoint, then improve it in two feedback rounds
type: run
block: Run 2 — deck + feedback · 15
visible:
**Goal:** reports/NISP-deck.pptx, made from your report.
**Same loop:** brainstorm → **spec** → plan → build (see handout)
**Spec:**
```text
Add a NISP deck to docs/spec.md: reports/NISP-deck.pptx, made from reports/NISP-report.html with the same numbers and no new facts. About 6 slides for managers, one point per slide. It must open in PowerPoint and Google Slides. Don't build anything yet.
```
**Build** (Build mode, after you approve the plan):
```text
Approved. Save that plan to docs/plan.md, then build reports/NISP-deck.pptx from it. Also save a copy as reports/NISP-deck-v1.pptx.
```
**Then:** Open the deck. Write down 3 things to fix.
**Time:** 15 min
**Stuck?** Raise your hand.
diagram: Across the top of the card, the loop as four small chips: "brainstorm", "spec", "plan", "build", with "spec" and "build" highlighted and the others outlined.
build:
  0: goal, loop chips and the spec prompt
  1: the build prompt, "Then", time and stuck line
handout:
1. Brainstorm:
```text
Let's brainstorm a short PowerPoint deck made from reports/NISP-report.html. Ask me one question at a time, at most 3, in plain business language: who watches it, how long the talk is, what the main message is. Don't write any code or files yet.
```
2. Spec: the prompt on the slide. Read the update and correct one thing.
3. Plan (Tab: Plan mode; approve, edit or reject):
```text
Read docs/spec.md and give me a numbered step-by-step plan for the deck only. Don't build anything yet.
```
4. Build (Tab: Build mode, once approved): the prompt on the slide.
notes:
Same loop again; the handout has the brainstorm and plan prompts. On step 0, the spec. It says the deck comes from the report, keeps the same numbers, and adds no new facts. About six slides is a starting point; change it if your brainstorm said otherwise. In the plan, check that it reads the report and does not invent content. On step 1: the build. The agent may install a Python library for writing PowerPoint files and ask to run commands; allow it. The v1 copy keeps the first version for the before and after later. Open the deck in PowerPoint, or upload it to Google Slides. Then each person writes down three things to fix, in plain words. Look at structure, visuals and story. These are your feedback for the next slide. All prompts here are untested.
words: 40 · budget: 60 · exception: fenced prompts not counted (39 + 17 words); brainstorm and plan prompts moved to handout to keep 2 prompts per slide
status: UNTESTED (spec, build, and both handout prompts)

## 13b. Run 2: turn the report into PowerPoint, then improve it in two feedback rounds
type: run
block: Run 2 — deck + feedback · 18
visible:
**Goal:** A better deck after two feedback rounds, pushed.
**Round 1** (example):
```text
Improve reports/NISP-deck.pptx. What: make each slide title a full sentence that states its point. Why: managers may read only the titles. Example: instead of "Price chart", say what the chart shows. Keep every number the same. Save a copy as reports/NISP-deck-v2.pptx.
```
**Round 2:** your own fix as what, why, example. Save as v3. Example: handout.
**Push:**
```text
Commit all changes, including the deck copies, with the message "NISP deck". Then push to GitHub.
```
**You should see:** v1, v2 and v3 in reports/, on GitHub.
**Time:** 18 min
**Stuck?** Checkpoint `s3-pptx`.
diagram: none
build:
  0: goal and round 1
  1: round 2
  2: push prompt, "You should see", time and stuck line
handout:
Round 2 example (if none of your three fixes is about visuals):
```text
Improve reports/NISP-deck.pptx. What: one chart or one key number per slide, shown large. Why: a room can't read a crowded slide. Example: move the stats table to a backup slide at the end. Keep every number the same. Save a copy as reports/NISP-deck-v3.pptx.
```
notes:
Two rounds, each one brief in three parts. On step 0: round one is the example from the last slide, about titles and story. You may send it as is, or replace it with one of your three fixes in the same shape. Keep the line "Keep every number the same" in every round. Open the new version and compare it with v1. On step 1: round two is yours. Pick another fix from your list, write it as what, why and example, and save as v3. If none of your fixes is about visuals, the handout has one. After each round, spot-check one number against the report. On step 2: commit and push. Check github.com shows all three versions. Anyone behind switches to checkpoint s3-pptx, which has the before and after versions. Prompts are untested.
words: 44 · budget: 60 · exception: fenced prompts not counted (41 + 16 words); round 2 example prompt moved to handout to keep 2 prompts per slide
status: UNTESTED (round 1, push, and the handout round 2 prompt)

## 14. Feedback changed the deck from a data dump into a story
type: visual
block: Run 2 — deck + feedback · 6
visible:
Before (v1)
Price chart
After (v3)
Title says the point
One chart per slide
Sample
diagram: Two slide thumbnails side by side, both tagged "Sample". Left "Before (v1)": the title "Price chart", a crowded grid of round sample numbers, a small chart squeezed in a corner and several bullet lines. Right "After (v3)": a full-sentence title drawn as a bold grey bar with the label "Title says the point", and one large chart filling the slide, labelled "One chart per slide". A thin arrow from left to right.
build:
  0: the "Before (v1)" thumbnail alone
  1: the arrow draws; the "After (v3)" thumbnail appears
  2: the two labels on the after slide appear one by one
notes:
Show the effect of two rounds. On step 0: the first version is typical of a first AI draft. Everything from the report is crammed in, the title is a topic label, and the chart is small. The numbers here are samples, not NISP data. On step 1: the version after two rounds. On step 2: the title is now a sentence that says the point, and the slide carries one chart, big enough to see from the back of the room. Nothing new was invented, and the numbers did not change. Only the form and the story did. Then ask two volunteers to show their own v1 and v3 side by side on screen. Ask the room: what did your feedback change? Replace this mock with the reference build's v1 and v3 from checkpoint s3-pptx once it is built.
words: 15 · budget: 40 · exception: none
status: n/a (mock thumbnails; placeholder until the reference v1/v3 exist)

## 15. If you'll do it again next month, save it as a workflow; brainstorm → spec → plan is one too
type: visual
block: Run 3 — workflow · 6
visible:
refresh → report → check → deck
/stock-report TLKM.JK
brainstorm → spec → plan → build
Same steps every time? Save them.
diagram: Top: four step cards in a row, "refresh", "report", "check", "deck", joined by arrows. They slide together and fold into one command chip "/stock-report TLKM.JK". Below, a second row of four chips "brainstorm", "spec", "plan", "build" with a faint dotted outline around them, the outline of a command chip with no label. Caption at the bottom: "Same steps every time? Save them."
build:
  0: the four step cards in a row
  1: the cards slide together and fold into the "/stock-report TLKM.JK" chip
  2: the second row appears; the dotted chip outline draws around it
  3: caption fades in; the top chip pulses gently on a loop
notes:
When is a workflow worth it? When you will do the same steps again. On step 0: look at what you did in Runs 1 and 2. Refresh the data, write the report, check the numbers, build the deck. Next month the steps are the same; only the dates change. For another stock, only the ticker changes. On step 1: so we fold the steps into one saved opencode command. You type its name and a ticker, and it runs the chain. On step 2: notice that the method you have used all day is a workflow too. Brainstorm, spec, plan, build, the same steps in the same order for every feature. You could save that as a command as well. On step 3: the test is simple. Same steps every time? Save them. One-off job? Just prompt.
words: 16 · budget: 40 · exception: none
status: n/a

## 16. Run 3: save the steps as an opencode command and run it on TLKM
type: run
block: Run 3 — workflow · 24
visible:
**Goal:** A saved opencode command that makes the report and deck for any ticker.
**Same loop:** brainstorm → **spec** → plan → build (see handout)
**Spec:**
```text
Add a workflow to docs/spec.md: a saved opencode command called stock-report that takes a ticker like TLKM.JK. It adds it with POST /api/watchlist, runs POST /api/refresh, makes the report and deck in reports/ like the NISP ones, and checks every number against the database. Don't build anything yet.
```
**Run it:**
```text
/stock-report TLKM.JK
```
**You should see:** TLKM-report.html and TLKM-deck.pptx in reports/.
**Time:** 24 min
**Stuck?** Checkpoint `s3-workflow`.
diagram: Across the top of the card, the loop as four small chips: "brainstorm", "spec", "plan", "build", with "spec" highlighted and the others outlined.
build:
  0: goal, loop chips and the spec prompt
  1: the run command, "You should see", time and stuck line
handout:
1. Brainstorm:
```text
Let's brainstorm saving our report and deck steps as a saved opencode command that works for any ticker. Ask me one question at a time, at most 3, in plain business language. Don't write any code or files yet.
```
2. Spec: the prompt on the slide. Read the update and correct one thing.
3. Plan (Tab: Plan mode; approve, edit or reject):
```text
Read docs/spec.md and give me a numbered step-by-step plan for the stock-report command only. Don't build anything yet.
```
4. Build (Tab: Build mode, once approved):
```text
Approved. Save that plan to docs/plan.md, then create the stock-report command from it. Tell me how to run it.
```
5. Run it: the command on the slide. Check 3 TLKM numbers against your dashboard.
6. Push:
```text
Commit all changes, including the TLKM report and deck, with the message "Stock report workflow". Then push to GitHub.
```
notes:
The last run puts it all together; the handout has all six steps. Brainstorm first, then on step 0 the spec. It names the command, the two endpoints that add the ticker and refresh its prices, the two output files, and the number check. In the plan, check it reuses what you built for NISP rather than starting over. Approve, edit or reject, then build. If the agent is unsure where to save the command, check the opencode docs for where commands live. On step 1: type a slash in opencode and the command should appear. If it does not, quit opencode and open it again in the project folder. Run it on TLKM.JK. Open both files and check three numbers against your dashboard. Then push. All prompts here are untested; rehearse the whole run. Anyone behind switches to checkpoint s3-workflow.
words: 39 · budget: 60 · exception: fenced prompts not counted (48 + 2 words); brainstorm, plan, build and push prompts moved to handout to keep 2 prompts per slide
status: UNTESTED (spec, run command, and all 4 handout prompts)

## 17. What should you still check by hand every time?
type: check
block: Run 3 — workflow · 5
visible:
A. Nothing. The command checks its own numbers.
B. A few numbers against the dashboard, and every claim in the insight.
C. Only that both files exist.
diagram: none
build:
  0: question and the three choices
  1: B highlights green; A and C fade; reveal line appears
reveal: B — The agent's own check can be wrong, and only you can judge whether a claim is supported.
notes:
Read the question aloud and vote by hand. Click to reveal B. A is the tempting one: the command already checks every number against the database, so why check again? Because the check is done by the same agent that wrote the report, and in Run 1 you saw how confident it can sound. Three numbers against the dashboard takes a minute. C is too little: a file can exist and still be wrong. The claims are the part only you can judge. The database cannot tell the agent why a price moved, and a new ticker means a new insight sentence to test with "which rows prove this?" Ask the room to name one more thing they would check before sending a deck to their boss.
words: 27 · budget: 60 · exception: none
status: n/a

## 18. In one day you built, upgraded and automated a business app
type: recap
block: Close + Q&A · 5
visible:
Session 1: built a dashboard and chatbot
Session 2: added a database, watchlist and Wiki
Session 3: automated a report, deck and workflow
Checkpoint: s3-workflow
diagram: Three columns rising left to right like the staircase from slide 5, one per session, each with its line from visible and a small icon: a browser for Session 1, a database cylinder for Session 2, a command chip for Session 3. A thin line joins them. The checkpoint line sits under the third column.
build:
  0: title
  1: Session 1 column appears
  2: Session 2 column appears
  3: Session 3 column appears; checkpoint line last
notes:
Do not re-teach; link each point to what they did. On step 1: this morning you built a NISP dashboard and a chatbot, and learned that the model forgets and the app resends the conversation. On step 2: in Session 2 the app got a memory: a database, a watchlist and a Wiki the chatbot cites. On step 3: this afternoon you turned that data into a report and a deck, checked the numbers and claims, and saved the job as a workflow that ran on TLKM. The synthesis: all day, the work you did was judgement. You decided what to build, read the plans, checked the numbers, and gave feedback like a manager. Anyone not finished can switch to checkpoint s3-workflow, the starting point for Day 4.
words: 25 · budget: 40 · exception: none
status: n/a

## 19. Questions
type: Q&A
block: Close + Q&A · 14
visible:
Questions?
diagram: Large "Questions?" heading. Around it, five small shapes keep moving on slow loops: three square speech bubbles drifting along different paths, one red "?" orbiting the heading, and one dot bouncing between the bubbles. No text inside the shapes.
build:
  0: heading and moving shapes (they loop for as long as the slide is open)
notes:
Open the floor. If no one speaks, start with: which report at your work would you turn into a workflow first? Or: what did the AI get wrong today that surprised you? Collect parking-lot items on a flip chart. If a question needs a long answer, say you will cover it on Day 4 or in the handout. Repeat questions before answering so the room hears them. Keep investment questions neutral: the app and its reports describe data; they do not advise. Use the spare time to help anyone whose TLKM run failed, and check that everyone has pushed and has the s3-workflow checkpoint link.
words: 1 · budget: 40 · exception: none
status: n/a

## 20. Day 4: connect your app to other services and the web
type: talk
block: Close + Q&A · 1
visible:
Day 4:
- Your back end serves other apps
- News from the web in your database and chatbot
- Login and roles
diagram: none
build:
  0: all lines together
notes:
Preview Day 4 in one minute. Your app so far talks only to itself and to Yahoo for prices. On Day 4 it opens up. First, your FastAPI back end gets endpoints that other apps can use, and we tour its built-in documentation page. Second, the app collects news from the web into the database, so the chatbot can use it. Third, we put a login and user roles in front of the page and the back end. Same method all the way: brainstorm, spec, plan, build, check. Remind everyone to keep their project or use checkpoint s3-workflow. Thank them for a full day and close. Mention the time Day 4 starts.
words: 20 · budget: 40 · exception: none
status: n/a

## Word count check

| id | type | words | budget | over? | notes words |
|---|---|---|---|---|---|
| 1 | title | 10 | 40 | no | 130 |
| 2 | visual | 14 | 40 | no | 137 |
| 3 | talk | 19 | 40 | no | 127 |
| 4 | visual | 15 | 40 | no | 129 |
| 5 | visual | 21 | 40 | no | 149 |
| 6 | check | 45 | 60 | no | 130 |
| 7 | visual | 14 | 40 | no | 141 |
| 8a | run | 39 | 60 | no | 145 |
| 8b | run | 41 | 60 | no | 134 |
| 9 | visual | 19 | 40 | no | 140 |
| 10 | check | 29 | 60 | no | 140 |
| 11 | visual | 12 | 40 | no | 132 |
| 12 | visual | 24 | 40 | no | 135 |
| 13a | run | 40 | 60 | no | 139 |
| 13b | run | 44 | 60 | no | 136 |
| 14 | visual | 15 | 40 | no | 140 |
| 15 | visual | 16 | 40 | no | 138 |
| 16 | run | 39 | 60 | no | 141 |
| 17 | check | 27 | 60 | no | 127 |
| 18 | recap | 25 | 40 | no | 128 |
| 19 | Q&A | 1 | 40 | no | 105 |
| 20 | talk | 20 | 40 | no | 112 |

slides: 22 · minutes: 180
