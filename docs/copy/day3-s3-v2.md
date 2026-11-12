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
Workflow: refresh → report → check → deck
/stock-report
One command starts the chain
diagram: Two rows. Top row: a single box "Prompt: one request, one result" with a chat bubble going in and one document coming out. Bottom row: four boxes joined by arrowed lines, "refresh", "report", "check", "deck", with the label "Workflow:" on the left. A black command chip "/stock-report" sits above "refresh" with a line down to it. Check comes before deck, the same order used on slides 6 and 17 and in the Run 3 spec.
build:
  0: the top row: one prompt box, bubble in, document out
  1: the bottom row's four grey boxes appear; the arrows draw between them
  2: the "/stock-report" chip pops in; the boxes light red one after another, refresh → report → check → deck, on a loop
  3: caption appears
notes:
Compare two ways of getting work done. On step 0: a prompt is what you have typed all day. One request, one result, and then the agent waits for you. On step 1: a workflow is a chain of steps saved in a fixed order. Ours, by the end of today, will refresh the prices, write the report, check the numbers, then build the deck. Checking comes before the deck so a wrong number never reaches a slide. On step 2: the command /stock-report starts it, and the boxes light up in order. You type one command instead of four prompts. It is still the agent doing the work, so it can stop and ask you, or fail, and you still read what it made. On step 3: the caption. One command starts the whole chain. Ask the room: which of your monthly tasks are the same steps every time? A monthly sales summary, a board pack, a branch report. Those are workflow candidates.
words: 16 · budget: 40 · exception: none
status: n/a

## 5. Prompt, skill and workflow are three levels of reuse
type: visual
block: Workflows · 7
visible:
Prompt: typed each time
Skill: expertise loaded when needed
Workflow: steps saved as a command
Session 1: prompts and skills
Today: workflows
diagram: Three steps rising left to right like a staircase, each higher than the last: "Prompt: typed each time", "Skill: expertise loaded when needed", "Workflow: steps saved as a command". Inside the red workflow step, four small outlined boxes light white one after another, echoing the chain on slide 4. A small figure stands on the second step, then climbs to the third. Under the steps, a grey bracket spans prompt and skill, labelled "Session 1: prompts and skills"; a red bracket spans the workflow step, labelled "Today: workflows". The figure does not bob.
build:
  0: the empty staircase
  1: "Prompt" and "Skill" steps appear; the grey Session 1 bracket; the figure lands on step 2
  2: the "Workflow" step appears in red; the figure climbs onto it
  3: the red "Today: workflows" bracket appears
notes:
This is the staircase from this morning, now with the top step filled in. On step 1: in Session 1 you met two of these. A prompt is typed each time: you write it, you get an answer, and next time you write it again. A skill is a packaged playbook the agent loads only when the task matches its description, like the brainstorming skill. On step 2: a workflow is the next level. It saves a whole sequence of steps under one command, so you can run it again tomorrow or next month. On step 3: that is today's work. A useful test: if you only need it now, it is a prompt. If it is know-how the agent should use whenever it fits, it is a skill. If it is the same steps in the same order every time, it is a workflow. AGENTS.md still holds the standing rules underneath all three.
words: 22 · budget: 40 · exception: none
status: n/a

## 6. Is each of these a prompt, a skill or a workflow?
type: check
block: Workflows · 7
visible:
1. "Summarise this report in three bullets."
2. Your team's report-writing rules, used whenever a task fits.
3. /stock-report TLKM.JK: refresh, report, check, deck.
A. 1 prompt · 2 skill · 3 workflow
B. 1 prompt · 2 workflow · 3 workflow
C. 1 prompt · 2 skill · 3 prompt
prompt / skill / workflow (answer tags)
diagram: none; on reveal a small tag slides in after each item: "prompt", "skill", "workflow" (red), one after another.
build:
  0: question, the three items and the three choices
  1: A highlights red; B and C fade; the three answer tags slide in; reveal line appears
reveal: A — Rules used when they fit are a skill; a saved chain of steps is a workflow.
notes:
Read the three items aloud. Give thirty seconds, then take a show of hands for A, B and C, one at a time. Click to reveal: the labels appear next to each item. A is right. Item 1 is a one-off request, so it is a prompt. Item 2 is the tricky one: it sounds like a process, but it is know-how the agent picks up whenever a task fits, so it is a skill, not a workflow. That is why B tempts people. Item 3 is a saved chain of four steps started by one command, so it is a workflow. C tempts anyone who thinks 'it is just text I type': yes, a saved command sends text to the agent, but you wrote it once and reuse it on any ticker. Item 3 is exactly what you will build in Run 3, so tell them to remember its shape.
words: 27 visible + 42 choices and reveal · budget: 60 · exception: quiz choices and answer reveal (allowed: quiz choices may exceed). Distractors are near-misses: B mistakes the skill for a workflow, C mistakes the saved command for a prompt.
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
diagram: A report page in the centre, built from four blocks stacked top to bottom: "Summary table" (a grid of 2 rows × 3 columns of blank grey cells, no numbers, with a small "Sample" tag), "Price chart" (a line drawn left to right), "Key stats" (three small tiles with grey bars, no numbers), "Insight" (one sentence drawn as a highlighted grey line). On the right edge, thin dotted lines run from each block to a small database cylinder; the caption "Every number traces to your database" sits under the page.
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
**Spec:**
```text
Add a NISP report to docs/spec.md: reports/NISP-report.html, made only from the stocks and prices tables in our SQLite database. Sections: summary table, 1-year price chart, key stats, one insight the data supports. Every number must come from the database. Don't build anything yet.
```
**Build** (after you approve the plan):
```text
Approved. Save that plan to docs/plan.md, then build reports/NISP-report.html from it. Tell me how to open it.
```
**You should see:** (sketch) This page in your browser.
**Stuck?** Raise your hand.
diagram: Below the title, the loop as six chips joined by arrows: "brainstorm", "spec", "plan", "execute", "test", "iterate". Small grey captions under three chips: "handout" (brainstorm), "Plan mode" (plan), "Build mode" (execute). Chips turn red while current and black when done, so the tracker shows where the trainee is on each click. Step 0: brainstorm and spec red. Step 1: those turn black; plan and execute turn red. Under "You should see", a small sketch of the expected report page: a table, a line chart, three stat boxes and a red insight line.
build:
  0: goal, tracker (brainstorm, spec current) and the spec prompt
  1: tracker moves to plan and execute; the build prompt, the expected-result sketch and stuck line
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
[UNTESTED PROMPT] Same loop as this morning, at speed; the handout has every prompt. Brainstorm first: the agent asks up to three questions. Answer in one short sentence each, and say who the reader is. On step 0, the spec. It names the file, the two tables, the four sections, and the rule that every number comes from the database. Read what the agent writes and correct one thing. Then Tab to Plan mode and ask for the plan. Approve, edit or reject; check it reads the database and does not download fresh prices from the internet. On step 1: the tracker moves to plan and execute. Tab back to Build mode and send the build prompt. The agent may ask to run commands; allow them. Open the file in your browser; it should look roughly like the sketch: a table, a chart, three stat boxes and one insight line. All these prompts are untested, so rehearse them before class. Anyone far behind can wait for the s3-report checkpoint at the end of Run 1.
words: 36 · budget: 60 · exception: fenced prompts not counted (43 + 17 words); brainstorm and plan prompts in the handout
status: UNTESTED (spec, build, and both handout prompts)

## 8b. Run 1: spec the report, generate it from your database, and check every number
type: run
block: Run 1 — report · 12
visible:
**Goal:** Numbers traced, then pushed.
**1. Ask the agent to show its sources:**
```text
List every number in reports/NISP-report.html. For each one, show the database query that gives it and the value the query returns. Mark any number that doesn't match. Don't change any files yet.
```
**2.** Compare 3 with your dashboard. Mismatch? Ask why.
**Your 3 numbers** (Sample): Query · Dashboard
Latest close 1,250 · 1,250 ✓
Day change +1.2% · +1.2% ✓
Year start 1,140 · chart ✓
**3.** Insight: which rows prove it? None? Cut it.
**4. Push:**
```text
Commit all changes with the message "NISP report". Then push to GitHub.
```
**Stuck?** Checkpoint `s3-report`.
diagram: Below the title, the loop as six chips joined by arrows: "brainstorm", "spec", "plan", "execute", "test", "iterate". Small grey captions under three chips: "handout" (brainstorm), "Plan mode" (plan), "Build mode" (execute). Chips turn red while current and black when done, so the tracker shows where the trainee is on each click. Test is red throughout; iterate turns red on steps 1–2 (fixing mismatches and the insight) and black after. On the left, a three-row sample table worked example: each number the dashboard shows (latest close, day change, start-of-year price read off the chart), the agent's query value and the dashboard value, each with a green tick. Numbers are round samples, labelled "Sample".
build:
  0: goal, tracker (test current) and step 1
  1: step 2 and the worked three-number table
  2: step 3, the insight check, before anything is pushed
  3: step 4 push prompt and stuck line
notes:
[UNTESTED PROMPT] A report you have not checked is a draft. The tracker is now on test. On step 0: send the first prompt. It asks the agent to show, for every number, where it came from: the query and the value it returns. "Don't change any files yet" keeps it from quietly fixing things before you see them. On step 1: the agent checking its own work is not enough. The sample table shows what to do: take three numbers your dashboard already shows, the latest close, the day's change, and the price at the start of the year from the chart, and compare them with the agent's query values. The numbers on the slide are samples, not NISP data. Any mismatch: ask the agent why and fix it. On step 2: the insight. Ask "Which rows prove this?" If nothing in the database proves it, cut it or rewrite it as a fact. We look at this more closely in two slides. On step 3: commit and push, and look for the reports folder on github.com. Both prompts are untested. Anyone whose report never appeared switches to checkpoint s3-report now, so they are ready for Run 2.
words: 60 · budget: 60 · exception: fenced prompts not counted (32 + 12 words)
status: UNTESTED (both prompts). Confirm the dashboard shows latest close and day change (/api/quote) and a 1-year chart (/api/history) on the reference build.

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
C. Volume jumped in the week before the earnings release.
prices: close ✓ / prices: volume ✓ / earnings dates ✗ (answer tags)
diagram: A report page frame with a grey "Sample" tag in the corner. The three claims sit inside one under the other. On reveal, a tag slides in at the right of each claim naming the data it needs: green "prices: close ✓", green "prices: volume ✓", black "earnings dates ✗".
build:
  0: question, the sample tag and the three claims
  1: C highlights red; A and B fade; the three data tags slide in one by one; reveal line appears
reveal: C — Volume is in your database; earnings dates aren't. Half-proved is unproved.
notes:
Read the three claims aloud. Stress that these are sample numbers on a made-up report, not NISP's real figures. Give thirty seconds, then vote by hand. Click to reveal: a tag on each claim shows what data it needs. A and B are each one query on the prices table: the close at two dates, and the average of the volume column. C is the subtle one. The volume jump is in your database, so half of it looks proved. But the database has no earnings dates, so 'before the earnings release' stands on nothing. Half-proved is unproved. This is the kind of sentence AI writes most often: a real number joined to an outside event. Then ask everyone to reread their own insight with the same question: which rows prove this? If not all of it, ask the agent to rewrite it as a fact the data supports. Replace C with a real unsupported claim from the reference build once it is tested.
words: 5 visible + 41 choices and reveal · budget: 60 · exception: none
status: n/a (claims are illustrative; C is a subtle half-supported claim, replace with a real one from the reference build once tested)

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
Example: "Price chart" → "The close rose 10% over the year"
diagram: Left: a small grey speech bubble "Make it better." with a question mark over a robot. Right: a feedback card with three labelled rows, "What", "Why", "Example", each with the text from visible. A green tick appears on the card.
build:
  0: the vague bubble and the confused robot
  1: the card appears; the "What" row fills in
  2: the "Why" row fills in
  3: the "Example" row fills in; the green tick appears
notes:
Feedback to an AI works like a brief to a colleague. On step 0: "make it better" gives the agent nothing to aim at, so it guesses, and you get random changes. On step 1: say what to change, specifically. Here: every slide title should state the point. On step 2: say why. The reason helps the agent make good choices you did not spell out. Here: managers may read only the titles. On step 3: give an example. Instead of the label "Price chart", a sentence like "The close rose 10% over the year". That number is a sample; their deck uses its own. The example shows the agent the standard you mean. Three parts: what, why, example. You will use exactly this pattern in Run 2, twice. Remind them: feedback is about form and story. It should never ask the agent to change a number.
words: 25 · budget: 40 · exception: none (the 10% is the same labelled sample as slides 10 and 14)
status: n/a

## 13a. Run 2: turn the report into PowerPoint, then improve it in two feedback rounds
type: run
block: Run 2 — deck + feedback · 15
visible:
**Goal:** reports/NISP-deck.pptx, made from your report.
**Spec:**
```text
Add a NISP deck to docs/spec.md: reports/NISP-deck.pptx, made from reports/NISP-report.html with the same numbers and no new facts. About 6 slides for managers, one point per slide. It must open in PowerPoint and Google Slides. Don't build anything yet.
```
**Build** (after you approve the plan):
```text
Approved. Save that plan to docs/plan.md, then build reports/NISP-deck.pptx from it. Also save a copy as reports/NISP-deck-v1.pptx.
```
**You should see:** (sketch) About 6 slides. Write down 3 things to fix.
**Stuck?** Raise your hand.
diagram: Below the title, the loop as six chips joined by arrows: "brainstorm", "spec", "plan", "execute", "test", "iterate". Small grey captions under three chips: "handout" (brainstorm), "Plan mode" (plan), "Build mode" (execute). Chips turn red while current and black when done, so the tracker shows where the trainee is on each click. Step 0: brainstorm and spec red. Step 1: plan and execute red. Under "You should see", a sketch of a short deck: three slide thumbnails with title bars and two faded ones.
build:
  0: goal, tracker and the spec prompt
  1: tracker moves to plan and execute; the build prompt, deck sketch and stuck line
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
[UNTESTED PROMPT] Same loop again; the handout has the brainstorm and plan prompts. On step 0, the spec. It says the deck comes from the report, keeps the same numbers, and adds no new facts. About six slides is a starting point; change it if your brainstorm said otherwise. In the plan, check that it reads the report and does not invent content. On step 1: the build. The agent may install a Python library for writing PowerPoint files and ask to run commands; say yes. The v1 copy keeps the first version for the before and after later. Open the deck in PowerPoint, or upload it to Google Slides; expect about six slides like the sketch. Then each person writes down three things to fix, in plain words. Look at structure, visuals and story. These are your feedback for the next slide. All prompts here are untested.
words: 40 · budget: 60 · exception: fenced prompts not counted (39 + 17 words); brainstorm and plan prompts in the handout
status: UNTESTED (spec, build, and both handout prompts)

## 13b. Run 2: turn the report into PowerPoint, then improve it in two feedback rounds
type: run
block: Run 2 — deck + feedback · 18
visible:
**Goal:** A clearer deck after two feedback rounds, pushed.
**Round 1** (example):
```text
Improve reports/NISP-deck.pptx. What: make each slide title a full sentence that states its point. Why: managers may read only the titles. Example: instead of "Price chart", something like "The close rose 10% over the year", using our real numbers. Keep every number the same. Save a copy as reports/NISP-deck-v2.pptx.
```
**Round 2:** your own fix as what, why, example. Save as v3.
**Push:**
```text
Commit all changes, including the deck copies, with the message "NISP deck". Then push to GitHub.
```
**You should see:** A partner reads only your v3 titles and gets the message. Numbers unchanged.
**Stuck?** Checkpoint `s3-pptx`.
diagram: Below the title, the loop as six chips joined by arrows: "brainstorm", "spec", "plan", "execute", "test", "iterate". Small grey captions under three chips: "handout" (brainstorm), "Plan mode" (plan), "Build mode" (execute). Chips turn red while current and black when done, so the tracker shows where the trainee is on each click. Earlier chips black; test and iterate red throughout.
build:
  0: goal, tracker and round 1
  1: round 2
  2: push prompt, "You should see" (the partner title test) and stuck line
handout:
Round 2 example (if none of your three fixes is about visuals):
```text
Improve reports/NISP-deck.pptx. What: one chart or one key number per slide, shown large. Why: a room can't read a crowded slide. Example: move the stats table to a backup slide at the end. Keep every number the same. Save a copy as reports/NISP-deck-v3.pptx.
```
notes:
[UNTESTED PROMPT] Two rounds, each one brief in three parts. On step 0: round one is the example from the last slide, about titles and story. You may send it as is, or replace it with one of your three fixes in the same shape. Keep the line "Keep every number the same" in every round. Open the new version and compare it with v1: the titles should now read as sentences. On step 1: round two is yours. Pick another fix from your list, write it as what, why and example, and save as v3. If none of your fixes is about visuals, the handout has one. After each round, spot-check one number against the report. On step 2: the test. Swap laptops with a neighbour. They read only your v3 titles and say the message back to you. If they can, the feedback worked. Spot-check one number against the report. Then commit and push. Anyone behind switches to checkpoint s3-pptx, which has the before and after versions. Prompts are untested.
words: 50 · budget: 60 · exception: fenced prompts not counted (49 + 16 words); round 2 example prompt in the handout
status: UNTESTED (round 1, push, and the handout round 2 prompt)

## 14. Feedback changed the deck from a data dump into a story
type: visual
block: Run 2 — deck + feedback · 6
visible:
Before (v1)
Price chart
After (v3)
The close rose 10% over the year
Title says the point
One chart per slide
Sample
diagram: Two slide thumbnails side by side, both tagged "Sample". Left "Before (v1)": the title "Price chart", a crowded grid of 4 × 4 blank grey cells (no numbers), a small chart squeezed in a corner and several bullet lines. A red arrow with a moving square. Right "After (v3)": the real sentence title "The close rose 10% over the year" (the same sample as slides 10 and 12), one large chart that draws itself. Two red labels pop in: "Title says the point" and "One chart per slide".
build:
  0: the "Before (v1)" thumbnail alone
  1: the arrow draws; the "After (v3)" thumbnail appears
  2: the two labels on the after slide appear one by one
notes:
Show the effect of two rounds. On step 0: the first version is typical of a first AI draft. Everything from the report is crammed in, the title is a topic label, and the chart is small. The numbers here are samples, not NISP data. On step 1: the version after two rounds. The new title is a sentence that says the point, here the sample 'The close rose 10% over the year'. On step 2: the labels name the two changes: the title says the point, and the slide carries one chart, big enough to see from the back of the room. Nothing new was invented, and the numbers did not change. Only the form and the story did. Then ask two volunteers to show their own v1 and v3 side by side on screen. Ask the room: what did your feedback change? Replace this mock with the reference build's v1 and v3 from checkpoint s3-pptx once it is built.
words: 23 · budget: 40 · exception: none
status: n/a (mock thumbnails; placeholder until the reference v1/v3 exist)

## 15. If you'll do it again next month, save it as a workflow; brainstorm → spec → plan is one too
type: visual
block: Run 3 — workflow · 6
visible:
refresh → report → check → deck
/stock-report TLKM.JK
brainstorm → spec → plan
/new-feature
Same steps every time? Save them.
diagram: Top: four step cards in a row, "refresh", "report", "check", "deck", joined by arrows (the order from slide 4). They slide right and fold into one black command chip "/stock-report TLKM.JK"; a small grey line under the chip keeps the four steps visible. Below: three cards "brainstorm", "spec", "plan" appear and fold the same way into a red chip "/new-feature" (an example name), with "brainstorm → spec → plan" under it. The two parallel folds show the title's claim.
build:
  0: the four step cards in a row
  1: the cards fold into the "/stock-report TLKM.JK" chip; the step line appears under it
  2: the brainstorm → spec → plan cards appear below
  3: they fold into the "/new-feature" chip; caption fades in
notes:
When is a workflow worth it? When you will do the same steps again. On step 0: look at what you did in Runs 1 and 2. Refresh the data, write the report, check the numbers, build the deck. The same order as on the workflows slide this morning. Next month the steps are the same; only the dates change. For another stock, only the ticker changes. On step 1: so we fold the steps into one saved opencode command. The small line under it reminds you the four steps are still inside. You type its name and a ticker, and the agent follows the saved steps. On step 2: notice that the method you have used all day is a workflow too: brainstorm, spec, plan, the same steps in the same order for every feature. On step 3: it folds the same way into a command of its own; /new-feature is just an example name. The test is simple. Same steps every time? Save them. One-off job? Just prompt.
words: 23 · budget: 40 · exception: none
status: n/a

## 16. Run 3: save the steps as an opencode command and run it on TLKM
type: run
block: Run 3 — workflow · 24
visible:
**Goal:** One saved command that makes the report and deck for any ticker.
**Spec:**
```text
Add a workflow to docs/spec.md: an opencode command, stock-report, that takes a ticker like TLKM.JK. It adds the ticker to my watchlist and refreshes its prices the way the app already does, checks every number against the database, then makes the report and deck in reports/ like my NISP ones, keeping the fixes from my feedback rounds. Don't build anything yet.
```
**Build** (after you approve the plan):
```text
Approved. Save that plan to docs/plan.md. Then create the command as .opencode/commands/stock-report.md, using $ARGUMENTS for the ticker. Tell me how to run it.
```
**Run it, then check 3 numbers and push:**
```text
/stock-report TLKM.JK
```
**You should see:** (sketch: TLKM report, TLKM deck) Titles as sentences, like v3.
**Stuck?** Restart opencode, or `s3-workflow`.
diagram: Below the title, the loop as six chips joined by arrows: "brainstorm", "spec", "plan", "execute", "test", "iterate". Small grey captions under three chips: "handout" (brainstorm), "Plan mode" (plan), "Build mode" (execute). Chips turn red while current and black when done, so the tracker shows where the trainee is on each click. Step 0: brainstorm and spec red. Step 1: plan and execute red. Step 2: test red. Under "You should see", two file icons labelled "TLKM report" and "TLKM deck".
build:
  0: goal, tracker and the spec prompt
  1: the spec stays; the build prompt appears
  2: the spec hides to make room; the run command, the expected files, and stuck line (restart opencode if /stock-report is not listed)
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
4. Build (Tab: Build mode, once approved): the prompt on the slide.
5. Run it: the command on the slide. Check 3 TLKM numbers against your dashboard, and the insight sentence.
6. Push:
```text
Commit all changes, including the TLKM report and deck, with the message "Stock report workflow". Then push to GitHub.
```
notes:
[UNTESTED PROMPT] The last run puts it all together; the handout has all six steps. Brainstorm first, then on step 0 the spec, in plain words. It names the command, says to add the ticker to the watchlist and refresh its prices the way the app already does, puts the number check before the deck, and keeps the fixes from your feedback rounds so TLKM comes out at v3 quality, not v1. In the plan, check it reuses what you built for NISP rather than starting over. On step 1: approve, then the build prompt. It names where the command lives, .opencode/commands, and $ARGUMENTS, which carries the ticker you type after the command. On step 2: type a slash in opencode and look for stock-report. If it is not there, quit and reopen opencode. Rehearse this before class to confirm whether a restart is needed on your setup. Run it on TLKM.JK. Open both files: the deck titles should read as sentences, like your NISP v3. Check three numbers against your dashboard and the insight sentence. Then push. All prompts here are untested; rehearse the whole run. Anyone behind switches to checkpoint s3-workflow.
words: 56 · budget: 60 · exception: fenced prompts not counted (61 + 23 + 2 words). The spec now uses plain words instead of endpoint names and carries the Run 2 feedback; the build prompt is back on the slide.
status: UNTESTED (spec, build, run command, and the handout prompts). Folder .opencode/commands and $ARGUMENTS verified on opencode 1.19.5 (project log 2026-11-12); whether a new command appears without a restart is not yet verified.

## 17. What should you still check by hand every time?
type: check
block: Run 3 — workflow · 5
visible:
A. Nothing. The command checks every number against the database.
B. Three numbers against the dashboard, and the insight sentence.
C. Every number in both files, one by one.
checks itself / 1 minute ✓ / 30 minutes (answer tags)
diagram: none; on reveal a tag slides in after each choice: "checks itself", green "1 minute ✓", "30 minutes".
build:
  0: question and the three choices
  1: B highlights red; A and C fade; the cost tags slide in; reveal line appears
reveal: B — Spot-check the numbers; only you can judge the claim.
notes:
Read the question aloud and vote by hand. Click to reveal B; the tags show the cost of each answer. A is the tempting one: the command already checks every number against the database, so why check again? Because the check is done by the same agent that wrote the report, and in Run 1 you saw how confident it can sound. C is the opposite trap: checking every number by hand takes half an hour and you will stop doing it. Three numbers against the dashboard takes a minute and catches a broken query. The insight sentence is the part only you can judge. The database cannot tell the agent why a price moved, and a new ticker means a new insight to test with "which rows prove this?" Ask the room to name one more thing they would check before sending a deck to their boss.
words: 0 visible + 41 choices and reveal · budget: 60 · exception: none
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
| 4 | visual | 16 | 40 | no | 164 |
| 5 | visual | 22 | 40 | no | 154 |
| 6 | check | 69 (incl. choices + reveal) | 60 | yes — quiz-choice exception | 151 |
| 7 | visual | 14 | 40 | no | 141 |
| 8a | run | 36 | 60 | no | 175 |
| 8b | run | 60 | 60 | no | 199 |
| 9 | visual | 19 | 40 | no | 140 |
| 10 | check | 46 (incl. choices + reveal) | 60 | no | 164 |
| 11 | visual | 12 | 40 | no | 132 |
| 12 | visual | 25 | 40 | no | 147 |
| 13a | run | 40 | 60 | no | 148 |
| 13b | run | 50 | 60 | no | 172 |
| 14 | visual | 23 | 40 | no | 161 |
| 15 | visual | 23 | 40 | no | 170 |
| 16 | run | 56 | 60 | no | 193 |
| 17 | check | 41 (incl. choices + reveal) | 60 | no | 148 |
| 18 | recap | 25 | 40 | no | 128 |
| 19 | Q&A | 1 | 40 | no | 105 |
| 20 | talk | 20 | 40 | no | 112 |

slides: 22 · minutes: 180

