# Day 3 · Session 1 — slide copy v2 (shorter, visual, 3 runs)

Course: AI Vibe Coding for Business Users · Session 1: Build your first AI Financial App · 3 hours · English deck, speaker-led and hands-on.
Sources: `docs/outlines/day3-s1-v2.md` (approved outline v2, 28 headlines, kept word for word), `docs/copy/day3-s1.md` (v1 copy, reviewed; wording, notes and diagrams reused), `prompts/s1.md` (tested prompts).

How to read this file:
- `visible:` is the on-slide text. Every label the diagram shows is listed in `visible:`; the `diagram:` line says where it goes. Quoted labels in `diagram:` that are not in `visible:` are counted too.
- `build:` lists the click steps. Step 0 is what shows when the slide arrives.
- Prompts in fenced blocks are not counted toward the word budget. `handout:` holds prompts that go in the printed handout, not on the slide.
- `status: tested` means the prompt is copied verbatim from `prompts/s1.md`. `UNTESTED` means it was written for v1 and has not been run in opencode; rehearse it before class.

## 1. Build your first AI Financial App
type: title
block: Opening · 3
visible:
Day 3 · Session 1
AI Vibe Coding for Business Users
diagram: none
build:
  0: title, subtitle and session line together
notes:
Welcome everyone. Today you build a real app, and nobody writes code by hand. You tell an AI coding agent called opencode what you want, you check what it gives you, and you steer it. By the end of these three hours you will have a BBCA dashboard and a chatbot, saved on GitHub. Before we start, check that opencode opens on every laptop, Windows and Mac, and that it answers a simple "hello". Anyone whose model does not reply, raise your hand now, so we fix it before the first exercise. Today is mostly hands-on: I explain for a few minutes, then you do it, and we check together.
words: 10 · budget: 40 · exception: none
status: n/a

## 2. Today you build a BBCA dashboard and chatbot without writing code
type: visual
block: Opening · 7
visible:
BBCA price
Daily change
1-year chart
Chatbot
Saved on GitHub
You direct. The AI writes the code.
diagram: A laptop browser frame, centre. Inside it the app mock-up: top-left a large price card "BBCA price"; beside it a small card "Daily change" with a green arrow; below them a wide line chart "1-year chart"; on the right a narrow chat panel "Chatbot" with two speech bubbles. Under the laptop a GitHub badge "Saved on GitHub" with an upward arrow from the laptop. Caption along the bottom: "You direct. The AI writes the code."
build:
  0: empty browser frame and title
  1: "BBCA price" and "Daily change" cards drop in
  2: "1-year chart" line draws left to right
  3: "Chatbot" panel slides in from the right
  4: arrow to "Saved on GitHub" badge; caption fades in
notes:
Say what the day produces, in business words. BBCA is Bank Central Asia, a stock many of you know. On step 1 point at the price card: the latest price in rupiah and how much it moved today. On step 2, the one-year chart. On step 3, the chatbot answers questions about that data. On step 4, the whole project is saved on GitHub. Optional quick look: open the finished app from checkpoint s1-chatbot at localhost:5173 and ask "What is BBCA's latest price?" Have both servers running before class. Then ask: how many of you have written code before? Few hands is fine. Your job is a manager's job: be clear about the goal, then judge the work. Mention that we show market data only. Nothing in the app tells anyone what to buy or sell.
words: 17 · budget: 40 · exception: none
status: n/a

## 3. An LLM predicts the next words from the text you send it
type: visual
block: How an AI coding agent works · 3
visible:
Text in: "BBCA is the ticker of Bank Central ..."
Text out: "Asia"
LLM = large language model
diagram: A wide input box on the left with the "Text in" sentence. An arrow into a central rounded box "LLM". An arrow out to a box on the right where the predicted word appears. Under the right box, three faint alternative words in a small ranked list with bars: "Asia" (longest bar), "Bank", "Group". Footer line: "LLM = large language model".
build:
  0: "Text in" box and the "LLM" box
  1: the sentence types out word by word into the input box
  2: arrow pulses through the LLM; the ranked list appears with bars growing
  3: "Asia" lifts out of the list into the output box
notes:
Start with what an LLM is: a very large text predictor. On step 1, read the sentence as it types. On step 2, point at the bars: the model scores likely next words. On step 3, it picks one, "Asia", and then repeats, one piece at a time. That is all it does. It can sound like an expert because it learned patterns from a huge amount of text. It can also be confidently wrong, because it predicts what sounds right, not what it has checked. This matters later: when the app needs real BBCA numbers, we have to hand them to the model. Ask the room: have you used ChatGPT or Copilot? Those are apps built on language models; the app is the screen you type into, and the model sits behind it.
words: 17 · budget: 40 · exception: none
status: n/a

## 4. The model is stateless, so the app resends the whole conversation every turn
type: visual
block: How an AI coding agent works · 4
visible:
Turn 1 sends: Question 1
Turn 2 sends: Question 1 + Answer 1 + Question 2
Turn 3 sends: everything so far + Question 3
The app resends it. The model doesn't remember.
diagram: Three horizontal rows, one per turn, each a row of small rounded boxes. Row "Turn 1 sends": one box "Question 1". Row "Turn 2 sends": three boxes "Question 1", "Answer 1", "Question 2". Row "Turn 3 sends": a longer box "everything so far" followed by "Question 3". Each row has an arrow on the right into one box "Model". Caption under the rows is the last line of visible.
build:
  0: title, the "Model" box and the "Turn 1" row
  1: "Turn 2" row slides in; its earlier boxes are copies of row 1
  2: "Turn 3" row slides in, the longest
  3: caption appears in accent colour
notes:
"Stateless" means each request starts from zero. The model does not keep a file about you. On step 0: turn one sends only the first question. Ask: if the model remembers nothing, why does ChatGPT seem to remember our chat? On step 1, answer it: the chat app keeps the whole conversation and sends all of it again, plus your new message. On step 2, point at the rows getting longer. The model reads everything from the top each time, so it looks like it remembers. On step 3, say the caption. Two consequences: long chats cost more and run slower, and anything that is not in what gets sent does not exist for the model. We build exactly this into our chatbot later: the page sends the whole message list every turn.
words: 31 · budget: 40 · exception: none
status: n/a

## 5. The context window is the most the model can read at once; when it fills, old details drop off
type: visual
block: How an AI coding agent works · 4
visible:
Context window
rules · your messages · its replies · tool results · files
Full → oldest details dropped or summarised
Fix: /new session. Rules in AGENTS.md.
diagram: A fixed-size frame labelled "Context window", like a window you look through. Blocks arrive in time order and line up left to right inside it: "rules" (first, red), "your messages", "its replies", "tool results", "files". When the frame is full, new blocks ("your messages", "its replies") slide in from the right, everything shifts left, and the oldest blocks, starting with "rules", slide out of the left edge into a faded, struck-through area. Caption line under the frame, then the fix line in a green box.
build:
  0: the empty frame
  1: the five blocks arrive one by one, left to right, until the frame is full
  2: two new blocks slide in from the right; the row shifts left and "rules" plus the oldest message slide out and fade; "Full →" caption appears
  3: the green "Fix" box appears
notes:
Every request has a limit on how much text the model can take in. That limit is the context window. Think of a desk: only what fits on the desk can be read. On step 1, name each block: everything counts toward it, not just your questions. The rules, the conversation so far, the answers, tool results and any file the agent opened. I won't quote numbers because they differ per model and change often. On step 2: when the desk is full, the oldest material is cut off or replaced by a short summary. Both lose detail. An instruction you gave an hour ago, like "always show prices in rupiah", may be gone without warning. On step 3, two habits: start a new session when a task is finished, and put standing rules in AGENTS.md.
words: 22 · budget: 40 · exception: none
status: n/a

## 6. Every request is one list of messages: system, user, assistant, tool
type: visual
block: How an AI coding agent works · 3
visible:
system: sets the rules
user: you ask
assistant: the model answers
tool: reports what a tool did
One list. Sent every turn.
diagram: A vertical stack of four message boxes, each with a coloured role chip on the left (system, user, assistant, tool) and its short description to the right. Caption below the stack.
build:
  0: empty stack outline and title
  1: "system" box drops in
  2: "user" and "assistant" boxes drop in
  3: "tool" box drops in; caption appears
notes:
Now look inside what gets sent. It is not one blob of text but a list of messages, and each message has a role. On step 1, system: the rules and the role, written by whoever builds the app. On step 2, user: that is you; assistant: the model's replies. On step 3, tool: the result of something the app ran on the model's behalf, like reading a file. The whole list goes to the model every turn, which links back to the last slide. You do not write these lists yourself; opencode and our app build them. Quick check: ask which role the AGENTS.md rules belong to. Most will guess system; that is close enough, since the agent loads it as standing instructions before your first message.
words: 22 · budget: 40 · exception: none
status: n/a

## 7. With tool calling, the model asks for a tool and the app runs it
type: visual
block: How an AI coding agent works · 4
visible:
App · Model · Tool
1 messages
2 "run read_file on docs/spec.md"
3 app runs it
4 tool message
5 answer
diagram: Three boxes: "App" (left centre), "Model" (top right), "Tool" (bottom right). Numbered arrows: 1 App → Model "messages"; 2 Model → App "run read_file on docs/spec.md"; 3 App → Tool "app runs it"; 4 Tool → App "tool message", then App → Model again; 5 Model → App "answer". The Model box never has an arrow to Tool.
build:
  0: the three boxes, no arrows
  1: arrow 1 animates App → Model
  2: arrow 2 animates Model → App with the request label
  3: arrow 3 App → Tool "app runs it", then arrow 4 Tool → App "tool message"
  4: arrow 4 continues App → Model, carrying the tool message (same "4" label)
  5: arrow 5 Model → App "answer"
notes:
So how does an agent read files or run commands? Tool calling. The app, here opencode, tells the model which tools exist. Step 1: the app sends the messages. Step 2: the model replies with a request, "please run this tool with these inputs". Step 3: opencode runs it, and the result comes back as a tool message. Step 4: opencode sends everything again, now with the tool message. Step 5: the model answers using the result. Stress this, and point at the gap between Model and Tool: the model asks, opencode runs. The model never touches your computer itself, and opencode can ask you for permission first. That is why a mistaken model is less scary than it sounds: you stay in the loop. Our chatbot will not use tools yet.
words: 19 · budget: 40 · exception: none
status: n/a

## 8. A coding agent is an LLM calling tools in a loop until the task is done
type: visual
block: How an AI coding agent works · 4
visible:
Goal
Model decides
Runs a tool
Reads the result
Task done
You: goal and judgement. Agent: typing.
diagram: A circular loop of three boxes, arrows clockwise: "Model decides" → "Runs a tool" → "Reads the result" → back to "Model decides". An arrow enters the loop from the left labelled "Goal". An arrow leaves to the right labelled "Task done". Caption under the loop.
build:
  0: "Goal" arrow and the empty circle
  1: the three loop boxes appear in order with their arrows
  2: a highlight dot travels round the loop twice
  3: "Task done" arrow appears; caption fades in
notes:
Put the last slides together. An agent is the loop you see here. On step 0, you give a goal. On step 1, the model decides what to do next, usually a tool; the app runs it; the model reads the result and decides again. On step 2, let the dot go round: it repeats until the model thinks the task is done. That is why one request can take a minute and touch many files. It is also why the first sentence of your request matters: every step builds on the goal you gave. If the goal is vague, the loop wanders. On step 3, the role split: you bring the goal, the choices and the approval; the agent writes the files and runs the commands. It can be wrong with great confidence, so you check.
words: 17 · budget: 40 · exception: none
status: n/a

## 9. AGENTS.md is a note the agent reads at the start of every session
type: visual
block: How an AI coding agent works · 4
visible:
Session 1 · Session 2 · Session 3
AGENTS.md
"Explain what you will do in plain business language before doing it."
diagram: A timeline of three session boxes left to right, "Session 1", "Session 2", "Session 3", each starting empty (grey). A document icon "AGENTS.md" sits above the timeline. At the start of each session a dashed arrow drops from the document into the session box, which turns coloured. The example rule appears as a sticky note on the document.
build:
  0: three empty session boxes
  1: "AGENTS.md" document appears above
  2: arrows drop into each session box in turn; boxes light up
  3: the example rule appears on the document as a sticky note
notes:
Since the model forgets between sessions, we need a place to keep standing instructions. On step 0: every session starts empty. On step 1, that place is AGENTS.md, a plain text file in the project folder. On step 2, opencode reads it at the start of every session and puts it in front of the model, so every session starts with the same rules. Typical contents: what the project is, how to run it, and rules like the one on step 3. That rule is the one you will add in the first run. It makes the agent say what it plans to do before it does it, which is very useful when you cannot read the code. Anything permanent goes here, not in a chat.
words: 19 · budget: 40 · exception: none
status: n/a

## 10. The agent forgot your preference overnight. Why, and how do you fix it?
type: check
block: How an AI coding agent works · 4
visible:
A. The agent was tired. Remind it every morning.
B. A new session starts empty. Put the preference in AGENTS.md.
C. The model was updated. Wait for the next version.
diagram: none
build:
  0: question and the three choices
  1: B highlights green; A and C fade; reveal line appears
reveal: B — Nothing carries over between sessions except files, and AGENTS.md is read every time.
notes:
Read the question aloud. Give them thirty seconds to think, then ask for a show of hands for A, B and C. Take one vote at a time. Choice A makes people laugh; ask why a model cannot be tired. Click to reveal the answer. B is right because the session starts empty and only files carry knowledge forward. If someone argues for C, say updates are possible but not the usual cause. Then ask one person to say, in their own words, what rule they would add for their own work. This closes the block on how an agent works and sets up choosing models.
words: 30 · budget: 60 · exception: none
status: n/a

## 11. Use fast models for small edits and smart models for planning and debugging
type: visual
block: Models and Git · 4
visible:
Fast · [FAST MODEL]
rename a title · fix a typo · change a colour
Smart · [SMART MODEL]
write the plan · find why something breaks
Switch with /models
diagram: Two horizontal lanes like a road. Top lane "Fast" with a small quick car icon and the model placeholder; its three job chips sit along the lane. Bottom lane "Smart" with a slower vehicle and a thinking icon; its two job chips. A badge at the right edge: "Switch with /models".
build:
  0: the two empty lanes with "Fast" and "Smart" labels
  1: fast-lane job chips drop in; the car zips across
  2: smart-lane job chips drop in; the vehicle moves slowly, a thought bubble appears
  3: "/models" badge appears
notes:
Before class, replace [FAST MODEL] and [SMART MODEL] with real names from the model list your participants share. Models come in different sizes. On step 1: a fast model replies in seconds and is fine for small, clear jobs where you see the result straight away. On step 2: a smart model spends longer working things out before it acts. Use it for planning, when a bad plan wastes the whole build, and for debugging, when the cause is not obvious. A wrong choice shows up in two ways: a fast model on a hard job gives a shallow answer; a smart model on a trivial job makes you wait. On step 3, show the picker: type /models in opencode. Names differ per provider, so say "pick one fast and one smart from your list". Today we use the smart model for the plan.
words: 25 · budget: 40 · exception: none
status: n/a

## 11b. Effort sets how long the model thinks before it answers
type: visual
block: Models and Git · 2
visible:
Low effort: quick answers, small edits
High effort: slower, deeper, plans and bugs
Ctrl+T switches effort in opencode
diagram: A horizontal dial with three marks, "low", "medium", "high". A red pointer slides along it. Under the dial, a "thinking" bar that grows as the pointer moves right, with a small clock icon whose hand turns faster at high. Two short lines under the dial, one at each end, from visible. A key badge "Ctrl+T" at the right.
build:
  0: the dial with the pointer at "low"; the low-effort line
  1: the pointer slides to "high"; the thinking bar grows; the high-effort line appears
  2: the "Ctrl+T" badge appears; the pointer keeps sliding low → high on a loop
notes:
Model choice is one lever; effort is the second. Many models can think for a short or a long time before they answer, and opencode calls these settings variants. On step 0: low effort replies fast, which is right for a typo or a colour change. On step 1: high effort spends more time reasoning first. Use it for the plan and for a bug you cannot explain. It costs time, so do not leave it on high for everything. On step 2: in opencode, Ctrl+T cycles through the efforts your model offers; the current one shows in the footer. Not every model has variants. If Ctrl+T changes nothing, your model has one setting, and that is fine. Rule of thumb: smart model and high effort for the plan, then lower effort while building.
words: 21 · budget: 40 · exception: none
status: n/a

## 12. Everyone works on a local copy and shares through GitHub
type: visual
block: Models and Git · 4
visible:
Budget_final_v2_REALLY.xlsx?
Your computer: local copy
GitHub: shared copy
push / pull
Nothing travels until you push or pull.
diagram: Left: a laptop "Your computer" with subtitle "local copy". Right: a cloud filing cabinet "GitHub" with subtitle "shared copy". A double-headed arrow between them labelled "push / pull". On arrival a messy pile of spreadsheet cards sits in the centre with the file name and a red question mark.
build:
  0: the messy file pile with the red question mark
  1: the pile shrinks into the laptop; "Your computer" appears
  2: "GitHub" appears on the right
  3: the "push / pull" arrow draws; caption appears
notes:
On step 0 ask: who has a folder of files like Budget_final_v2_REALLY? Hands up. With copies like these, nobody knows which file is the real one, who changed what, or what was lost. Git keeps one project with every version remembered. On step 1: your local copy is your own desk; only you see it. On step 2: GitHub is a website that hosts the team's filing cabinet, the shared copy. On step 3, the key sentence: nothing moves between the two until you decide to push or pull. Many beginners think saving a file shares it. It does not. Why this matters for an agent: it changes many files quickly, so you need a way to go back and a place where the work is safe.
words: 17 · budget: 40 · exception: none
status: n/a

## 13. A commit is a save point; push sends it to GitHub, pull brings changes back
type: visual
block: Models and Git · 5
visible:
Commit 1: Created the budget file
Commit 2: Added March figures
Commit 3: Fixed the totals
push → GitHub · pull ← GitHub
Routine: pull → edit → commit → push
diagram: Left: a laptop "Your computer" with a row of three commit dots joined by arrows, each with its note underneath. Right: "GitHub" box. Arrow "push" left → right; arrow "pull" right → left. Bottom: the routine as four small boxes joined by arrows.
build:
  0: laptop with "Commit 1" only
  1: "Commit 2" and "Commit 3" appear with their notes
  2: the three commits fly along "push" into GitHub
  3: a new teammate commit "Commit 4 (Tom)" appears in GitHub and flies back along "pull"
  4: the routine row appears
notes:
On step 0: a commit is a save point. Not just the file, but the whole project at that moment, with a short note about what changed. Think of a game save with a name. On step 1, the note matters: next month, "Fixed the totals" tells you what happened; "stuff" tells you nothing. Commits live on your own computer; nobody else sees them yet. On step 2, push sends your commits up to GitHub. On step 3, pull is the reverse: it brings a teammate's commits down. Nothing arrives by itself, so pull before you start. On step 4, the daily routine. Today you work alone, so you mostly push. With opencode you do not type Git commands; you ask the agent in plain English, which you do in the next run.
words: 27 · budget: 40 · exception: none
status: n/a

## 14a. Run 1: create your GitHub account, add AGENTS.md with one rule, and push
type: run
block: Run 1 · 13
visible:
**Goal:** A GitHub account and an AGENTS.md file.
**Steps:**
1. github.com → Sign up. Confirm the email.
2. In opencode, in financial-app: type `/init`, press Enter.
Permission box? Choose **Allow once** (Enter).
**You should see:** Your GitHub home page. An AGENTS.md file.
**Time:** 13 min
**Stuck?** Nothing for 2 minutes? Esc, send `/init` again. Checkpoint `s1-start`.
diagram: none
build:
  0: the whole run card
notes:
Two things at once, because GitHub sends a confirmation email. Start the sign-up first, then run /init while waiting. Tell people to check their spam folder if the email is late. Anyone who already has an account just signs in. Choose a username you don't mind showing: it appears in the web address of your projects. Then everyone types /init in the empty financial-app folder. It took 43 to 55 seconds in our tests, and the file is short, because the folder is empty. Sometimes a box appears: "Permission required, access external directory". The agent occasionally looks at a path outside the project folder, and opencode asks first. Choose Allow once; it is highlighted, so Enter is enough. Rejecting can leave you with no file; then send /init again. If nothing moves for two minutes, press Esc and resend.
words: 55 · budget: 60 · exception: none (`/init` is a command, counted)
status: tested (`/init`)

## 14b. Run 1: create your GitHub account, add AGENTS.md with one rule, and push
type: run
block: Run 1 · 12
visible:
**Goal:** Your rule in AGENTS.md, pushed to GitHub.
**Prompt 1:**
```text
Add one rule to AGENTS.md: Explain what you will do in plain business language before doing it.
```
**Prompt 2:**
```text
Commit all files in this project with the message "Start project". Create a new GitHub repository called financial-app and push to it. Tell me if I need to sign in.
```
**You should see:** A financial-app repo on github.com with AGENTS.md.
**Time:** 12 min
**Stuck?** Raise your hand. Checkpoint `s1-start`.
diagram: none
build:
  0: goal and Prompt 1
  1: Prompt 2, "You should see", time and stuck line
notes:
Send prompt one. Wording around the rule differs between people, and that is fine. Open AGENTS.md together and check the rule is there word for word. Then click to prompt two, the first push. It asks for a commit with a clear message, a new repository, and the push. If the agent says you need to sign in to GitHub, follow its instructions on screen. Agree the sign-in method for Windows and Mac in the pre-session checklist. Confirm success the human way: open github.com, refresh, and look for the financial-app repository containing AGENTS.md. Prompt two is untested and depends on how Git and GitHub sign-in are set up on the laptops, so rehearse it on both. A repository can be private; people can decide. Anyone stuck gets checkpoint s1-start.
words: 31 · budget: 60 · exception: fenced prompts not counted (17 + 30 words)
status: tested (Prompt 1) · UNTESTED (Prompt 2, v1 slide 29)

## 15. You can instruct the agent four ways: prompt, AGENTS.md, skill, workflow
type: visual
block: Skills · 4
visible:
Prompt: one task, now
AGENTS.md: every session
Skill: loaded when needed
Workflow: many steps (Session 3)
diagram: Four steps rising left to right like a staircase, each higher than the last: "Prompt", "AGENTS.md", "Skill", "Workflow", each with its short description on the step. A small figure stands on the second step.
build:
  0: empty staircase
  1: "Prompt" and "AGENTS.md" steps appear; the figure lands on step 2
  2: "Skill" step appears, highlighted
  3: "Workflow" step appears greyed, tagged "Session 3"
notes:
There are four ways to tell an agent what you want. On step 1: a prompt is the message you type now. AGENTS.md is a standing note that applies to every session. Ask: you have already used two today. Which? Prompt and AGENTS.md; that is why the figure stands on step two. On step 2: a skill is a package of expertise that the agent loads only when a task needs it. On step 3: a workflow strings many steps together; we build one in Session 3. This slide is a map. The rest of this block is about skills, because they are the one most people have not met. Do not explain workflows yet.
words: 16 · budget: 40 · exception: none
status: n/a

## 16. A skill is packaged expertise the agent loads only when a task needs it
type: visual
block: Skills · 5
visible:
Always loaded: name + description
brainstorming · page design · report writing
Your request
Task matches → full instructions load
diagram: Left: a box "Agent's context". Inside it, three short rows, one per skill name: "brainstorming", "page design", "report writing"; under each name, one thin grey line stands for its one-line description (no text). Above the box, a speech bubble labelled "Your request". Right: a shelf of three tall grey document cards, one per skill, each showing its name at the top ("brainstorming", "page design", "report writing") and grey lines for its full instructions. Step by step: the request bubble sends a red dashed line to the "brainstorming" row, which turns red. A red arrow labelled "Task matches → full instructions load" runs from that row to the "brainstorming" card, which turns red, then the same red card slides left into the context box, under the rows. Only one red card is ever shown.
build:
  0: the context box with the three name rows; the grey shelf of three cards on the right
  1: the "Your request" bubble appears; a red dashed line runs from it to the "brainstorming" row, which turns red
  2: the red arrow and its label draw from the row to the "brainstorming" card, which turns red
  3: the red card slides left into the context box; the other two cards stay grey on the shelf
notes:
A skill is a written playbook for one kind of job, packed so the agent can pick it up when needed. Think of a recipe card in a kitchen: the cook picks the right card for the dish. On step 0, connect it to the context window: if the agent loaded every skill in full, the desk would fill up with text it does not need. So the box holds only each skill's name and a one-line description; the full instructions stay on the shelf. On step 1: your request comes in, and it matches the brainstorming description. On step 2: that match tells the agent which skill to open. On step 3: only that one skill's full instructions move into the context, and the agent follows them. The other two stay on the shelf. One lesson: a skill is only found if its description is clear. Skills differ by person. We do not provide a course skill kit. If you have none, today's prompts work without any.
words: 18 · budget: 40 · exception: none
status: n/a

## 17. The same request gives a more structured result when a skill is loaded
type: visual
block: Skills · 6
visible:
"I want a simple page for my sales team to see BBCA before a client meeting."
Without a skill: a straight answer
With a brainstorming skill: questions first, then a summary
Same folder, model and settings.
diagram: The request in a speech bubble across the top. Below, two chat panels side by side. Left panel labelled "Without a skill: a straight answer": one long block of grey placeholder lines, no words. Right panel labelled "With a brainstorming skill: questions first, then a summary": a red "?" icon, then three short bubbles each holding a "?" and grey placeholder lines, then a box with three short grey placeholder bars. No other words in either panel. Footer line in small text.
build:
  0: the request bubble and both empty panels
  1: left panel fills with the straight answer
  2: right panel: the red "?" icon, then the question bubbles appear one by one
  3: right panel summary box appears; footer fades in
notes:
On step 0, read the request. Same folder, same model, same settings; the only change is the skill. On step 1: without a skill, the agent goes straight to an answer, a page idea, built on its guesses. On step 2: with a brainstorming skill loaded, it asks questions first. On step 3, it summarises what was agreed. Point out: compare the structure, not the sentences, because wording varies from run to run anyway. A skill pays off for work you repeat in the same way, like a weekly client memo in a fixed format. One-off questions need only a prompt. Optional two-minute presenter demo, rehearsed on your own setup: run the request in a fresh session, then /new and run it again starting with "Use the [SKILL NAME] skill." Show that the skill was loaded. Keep screenshots as backup.
words: 36 · budget: 40 · exception: none
status: n/a (illustration; the optional demo is UNTESTED)

## 18. An agent builds what it guesses you want, so make it ask first
type: visual
block: Run 2 · 3
visible:
"Build me a stock dashboard"
Guesses: which stocks? which period? what layout?
Better: let it ask you first.
diagram: Left: a speech bubble with the vague request. An arrow to a robot icon surrounded by three floating question marks, each with a guess label. The arrow continues to a lopsided dashboard sketch with a red cross. Below, a second path: the robot asks "Who will use this?" in a bubble; the user answers; the arrow ends at a tidy dashboard with a green tick.
build:
  0: the vague request bubble
  1: the guess question marks pop up around the robot
  2: the lopsided dashboard appears with a red cross
  3: the second path draws: question, answer, tidy dashboard with green tick
notes:
Show how a vague request goes wrong. On step 1: if you say "build me a stock dashboard", the agent fills every gap with a guess: which stocks, which period, what it looks like. On step 2: it will usually build something, quickly, and it may be far from what you meant. Then you spend your time undoing. On step 3, the fix costs two minutes: let it ask you questions first, one at a time, and answer in business terms: who uses it, what decision it supports, how fresh the data must be. This is what a good business analyst does with a stakeholder. Ask who has received work back that missed the point. This pattern is the most useful habit of the day.
words: 22 · budget: 40 · exception: none
status: n/a

## 19. Every build follows six steps: brainstorm, spec, plan, execute, test, iterate
type: visual
block: Run 2 · 3
visible:
Brainstorm → Spec → Plan → Execute → Test → Iterate
Approve / Edit / Reject
diagram: Six square boxes in a row joined by right arrows. A red return arrow runs from the top of "Iterate" up, left along a straight line above the row, and down into the top of "Plan" (square corners, clear arrowhead into "Plan"). A dot travels along it in the arrow's direction, Iterate → Plan. Under "Plan" a small tag "Approve / Edit / Reject". A small "Run 2" bracket under Brainstorm–Plan and "Run 3" bracket under Execute–Iterate.
build:
  0: six grey boxes
  1: "Brainstorm", "Spec", "Plan" light up in turn; the "Run 2" bracket appears
  2: the "Approve / Edit / Reject" tag pops under "Plan"
  3: "Execute", "Test", "Iterate" light up; "Run 3" bracket; the loop arrow back to "Plan" draws
notes:
This is the method for the rest of Day 3. On step 1: brainstorm, the agent asks and you answer. Spec, a written description of what to build. Plan, step by step how. That is Run 2. On step 2: you approve, edit or reject the plan before anything is built. On step 3: execute, the agent builds; test, you check the result in the browser; iterate, you ask for changes, which takes you back to the plan. That is Run 3. We use the same six steps for the dashboard now, the chatbot after, and the features of Sessions 2 and 3. Do not memorise them; they will be on the wall. Notice that nothing gets built until step four.
words: 13 · budget: 40 · exception: none
status: n/a

## 20. A spec says what and why; a plan says how, and you approve, edit or reject it
type: visual
block: Run 2 · 4
visible:
docs/spec.md: what and why
Spec = PRD (product requirements document)
Goals · Out of scope · How we'll know it works
docs/plan.md: how, in numbered steps
You: approve, edit or reject
diagram: Two document cards side by side. Left card "docs/spec.md" with a red tag "Spec = PRD" under its title, then three section headings: "Goals", "Out of scope", "How we'll know it works". Right card "docs/plan.md" with a numbered list 1–5 of grey lines. An arrow from spec to plan. Under the plan card, three buttons: green "Approve", amber "Edit", red "Reject".
build:
  0: the spec card, empty
  1: the three spec headings appear one by one
  2: the arrow draws; the plan card appears with its numbered lines
  3: the three buttons appear under the plan
notes:
Two documents, two jobs. On step 0: the spec is the contract between you and the agent: what we are building and why, in your words. If you work with product teams, this is the same thing as a PRD, a product requirements document; a short one is enough. On step 1, it needs only three parts. Goals say what the app must do. Out of scope says what it must not do, which stops the agent adding extras. How we'll know it works describes what you will see when it is right; without it you cannot judge the result. On step 2: the plan is the agent's proposal for how to build it, in numbered steps. On step 3: you approve, edit or reject the plan. Both are files in the project, so they survive when a session ends. A new session can read the spec and carry on.
words: 31 · budget: 40 · exception: none
status: n/a

## 21a. Run 2: brainstorm the dashboard, write the spec, then plan it
type: run
block: Run 2 · 10
visible:
**Goal:** Agree what to build, then write it down.
**Prompt 1 (brainstorm):**
```text
Let's brainstorm a BBCA stock dashboard together. It should show the latest price, the daily change and a 1-year price chart. Ask me one question at a time, at most 5, in plain business language. Don't write any code or files yet.
```
Answer each question in one short sentence.
**Prompt 2 (spec):**
```text
Write what we agreed to docs/spec.md. Use three sections: Goals, Out of scope, and How we'll know it works. Don't build anything yet. We'll use React + Vite, FastAPI (Python) and yfinance, with endpoints GET /api/quote/{ticker} and GET /api/history/{ticker}?period=1y, server on port 8000, page on port 5173.
```
**You should see:** Five questions, a summary, then docs/spec.md. No app yet.
**Time:** 10 min
**Stuck?** Checkpoint `s1-spec`.
diagram: none
build:
  0: goal, Prompt 1 and the answer tip
  1: Prompt 2, "You should see", time and stuck line
notes:
Everyone sends prompt one exactly as written. In our tests the agent asked five short questions, about five seconds each, then summarised in three bullets. The first question was about the audience. Others vary, so answer what is actually asked. Sample answers: sales team before client meetings; delayed is fine if it shows the update time; mostly laptops. Watch for anyone whose agent starts writing files. Never reply "Yes, go ahead" after the summary; that invites a build. Click to prompt two. Teach "Don't build anything yet": without it, our first test built the whole app in eight minutes. With it, three of three runs wrote only the spec in about half a minute. The stack is named in one plain sentence, so you need not understand it. Everybody opens docs/spec.md, reads it and corrects one thing.
words: 40 · budget: 60 · exception: fenced prompts not counted (42 + 47 words)
status: tested

## 21b. Run 2: brainstorm the dashboard, write the spec, then plan it
type: run
block: Run 2 · 10
visible:
**Goal:** A checked plan, saved to docs/plan.md.
**1. Plan mode:** Tab (footer: "plan"), then send:
```text
Read docs/spec.md and give me a numbered step-by-step plan to build it. Don't build anything yet.
```
**2. Check it against your spec.** Approve, edit or reject. Edit example: handout.
**3. Build mode:** Tab (footer: "build"), then send:
```text
Save that plan to docs/plan.md. Don't build anything yet.
```
**You should see:** A numbered plan, then docs/plan.md.
**Time:** 10 min
**Stuck?** Checkpoint `s1-spec`.
diagram: none
build:
  0: goal and step 1
  1: step 2 (approve / edit / reject)
  2: step 3, "You should see", time and stuck line
handout:
Edit example (send in Plan mode, same session):
```text
Add one more step at the end: write a short README that explains how to start the app. Show me the updated plan.
```
notes:
Tab switches opencode between two agents. Build can edit files. Plan can read and think but cannot edit files, so it is safe for planning. Step one takes about 20 seconds and returns a numbered list, eight steps in our tests. On step two, read it against your spec. Approve means go to step three. Edit means ask in plain words; the README example in the handout adds a ninth step and changes nothing else. Reject means say what is wrong, for example "This plan builds more than the spec asks for. Make it shorter." Plan mode cannot write files, so saving needs Build mode: press Tab, send the save prompt, same session. A one-off "Error: File not found" is a typo the agent corrects itself. Keep "Don't build anything yet" in both prompts.
words: 50 · budget: 60 · exception: fenced prompts not counted (16 + 9 words); edit prompt (23 words) moved to handout to keep 2 prompts per slide
status: tested (both prompts and the handout edit prompt)

## 22. Approve, edit or reject: what would you do with each of these three plans?
type: check
block: Run 2 · 5
visible:
Plan 1: 8 steps that follow the spec.
Plan 2: Same, plus a login screen nobody asked for.
Plan 3: Builds a phone app. Ignores the spec.
A. Approve 1 · Edit 2 · Reject 3
B. Approve all three
C. Reject 1 · Approve 2 · Edit 3
diagram: none
build:
  0: the three plans and the three choices
  1: A highlights green; reveal line appears
reveal: A — Approve what matches the spec, edit what adds extras, reject what ignores it.
notes:
You are the decision-maker. Three outcomes for any plan: approve it as is, edit it by asking the agent to change something, or reject it and ask for a new one. Read the three plans aloud. Vote by hand. B is the lazy choice: approving everything means skipping the review. Click to reveal A. Plan 2 shows scope creep: the agent adds things you never asked for. Edit means you tell the agent: remove the login screen. Plan 3 contradicts the spec, so it is rejected. Tell everyone to read their own plan before approving: check the ports, endpoints and that nothing extra sneaks in. Only an approved plan gets saved to docs/plan.md and built.
words: 45 · budget: 60 · exception: none
status: n/a

## 23. Your app has two parts: a React screen and a FastAPI back end that fetches data and talks to the AI
type: visual
block: Run 3 · 4
visible:
Screen (React) · port 5173
Back end (FastAPI) · port 8000
yfinance: BBCA data
The AI: the LLM in backend/.env
chat messages (later)
diagram: Left box "Screen (React)" with a browser icon. Middle box "Back end (FastAPI)". Arrow screen → back end labelled "GET /api/quote · /api/history" and a second dashed arrow labelled "chat messages (later)". From the back end, two arrows right: to "yfinance: BBCA data" and to "The AI: the LLM in backend/.env". A small padlock beside backend/.env.
build:
  0: the "Screen (React)" box
  1: request arrow flows to "Back end (FastAPI)"
  2: back end → "yfinance: BBCA data"; a data packet flows back to the screen and a mini chart appears
  3: dashed "chat messages (later)" arrow; back end → "The AI"; padlock appears
notes:
Give them a mental picture of what the agent is about to build, without code. On step 0: the screen is what you see in the browser. On step 1: the back end is a small program running behind it. The two talk through endpoints, which are just named addresses, like two counters in a bank. On step 2: the back end fetches BBCA prices from Yahoo through yfinance and sends them to the screen. On step 3: later, for the chatbot, it also talks to the AI. The key to the AI lives only in the back end, in a file called .env, so nobody can see it in the browser. Ports are door numbers: 5173 for the screen, 8000 for the back end. Both come from the spec you wrote.
words: 24 · budget: 40 · exception: none
status: n/a

## 24a. Run 3: build the dashboard, then add the chatbot through the same loop
type: run
block: Run 3 · 14
visible:
**Goal:** Build the dashboard from your approved plan.
**Prompt** (Build mode):
```text
Approved. Build the app from docs/plan.md: backend on port 8000, page on port 5173, with GET /api/quote/{ticker} and GET /api/history/{ticker}?period=1y. Then tell me how to open it.
```
Agent asks to run a command? Allow it.
**You should see:** localhost:5173 with BBCA's price, change and chart.
**Time:** 14 min
**Stuck?** Checkpoint `s1-dashboard` (Run 3 midpoint; Run 3 ends at `s1-chatbot`).
diagram: none
build:
  0: the whole run card
notes:
The plan was approved and saved in Run 2, so the prompt says "Approved". Each person glances at docs/plan.md once more; if they still want a change, they edit first and save again. Make sure they are in Build mode; Tab if not. Building takes a few minutes; the agent may ask permission to run commands, and they should allow it. While it works, walk the room. When it finishes, the agent should explain how to start the servers. They open localhost:5173 and check the price, the daily change and the one-year chart. Ask: do the numbers look plausible, in rupiah? This prompt is untested and relies on Python and Node being installed on every laptop; check that in the pre-session list. Anyone behind switches to s1-dashboard.
words: 43 · budget: 60 · exception: fenced prompt not counted (31 words)
status: UNTESTED (v1 slide 48)

## 24b. Run 3: build the dashboard, then add the chatbot through the same loop
type: run
block: Run 3 · 18
visible:
**Goal:** Add a chatbot, test, push.
**Same loop as Run 2:** brainstorm → **spec** → plan → build (see handout)
First: put the LLM details in backend/.env.
**Spec:**
```text
Add a chatbot to docs/spec.md. The page sends the whole message list each turn. The backend adds BBCA's current data, then calls the LLM in backend/.env (LLM_BASE_URL, LLM_API_KEY, LLM_MODEL). No buy/sell advice, no tool calling. Don't build yet.
```
**Test in chat:** "What is BBCA's latest price?" · "And a month ago?" · "Should I buy BBCA?"
**Push:**
```text
Commit all changes with the message "BBCA dashboard and chatbot". Make sure backend/.env is not committed. Then push to GitHub.
```
**You should see:** BBCA answers, no buy advice, no .env on GitHub.
**Time:** 18 min
**Stuck?** Checkpoint `s1-chatbot`.
diagram: Across the top of the card, the loop as four small chips: "brainstorm", "spec", "plan", "build", with "spec" highlighted and the others outlined. No extra labels: the visible line already says "(see handout)".
build:
  0: goal, loop chips, .env line and the spec prompt
  1: test questions
  2: push prompt, "You should see", time and stuck line
handout:
1. Brainstorm:
```text
Let's brainstorm a chatbot for the BBCA dashboard. Ask me one question at a time, at most 2, in plain business language. Don't write any code or files yet.
```
2. Spec: the prompt on the slide. Read the update and correct one thing.
3. Plan (Tab: Plan mode; approve, edit or reject):
```text
Read docs/spec.md and give me a step-by-step plan for the chatbot only. Don't build yet.
```
4. Build (Tab: Build mode, once approved):
```text
Approved. Save that plan to docs/plan.md, then build the chatbot from it.
```
5. Fix one thing that's wrong:
```text
The chatbot [describe what is wrong]. Explain the cause in plain words, then fix it.
```
notes:
Same loop as the dashboard, at speed; the handout has every prompt. Before the spec, participants put the class LLM details into backend/.env; never paste the key into the chat. The spec is shown because it carries the new content: the page sends the whole message list every turn, as on slide 4, and the back end adds BBCA's data, so no tools are needed. After the plan, they approve, edit or reject; the order is approve, save, build. On step 1, they type the three questions in the browser, not opencode. "A month ago" tests the resent conversation; "Should I buy" tests the no-advice rule. Fix one thing with the handout prompt. On step 2, the push: .env holds the key, and secrets never go to GitHub. All prompts here are untested; rehearse them in order.
words: 60 · budget: 60 · exception: fenced prompts not counted (38 + 21 words); 4 more prompts in handout
status: UNTESTED (spec, push and all 4 handout prompts; v1 slides 49, 51, 52)

## 25. When something breaks, paste the error and ask the agent to explain it
type: visual
block: Run 3 · 4
visible:
Copy the error
Paste it to the agent
"Explain this in plain words, then fix it."
Check it worked
diagram: Four boxes in a row joined by arrows, each with an icon: a red error box with a copy icon; a chat bubble with a paste icon; the quoted ask in a speech bubble; a browser with a green tick. Under the first box, three small source tags: "opencode", "server window", "browser".
build:
  0: the red error box
  1: "Paste it to the agent" box and arrow; the three source tags appear under the first box
  2: the "Explain…" bubble appears
  3: "Check it worked" box with the green tick
notes:
Things will break, and that is normal. On step 0: the best habit is to avoid describing the problem from memory and copy the real error text instead. On step 1: paste it to the agent; it reads errors better than you can. Point at the tags: errors show up in the opencode window, in the server window, and in the browser. If no error is visible, describe what you saw: "the chart is empty". On step 2: ask it to explain first. That way you learn what happened, and you can decide whether the fix makes sense. On step 3: check the result yourself. A fix that is claimed but not tested is not a fix. If the agent seems stuck for two minutes, stop it and re-send.
words: 23 · budget: 40 · exception: none
status: n/a

## 26. You built an app by directing an AI, not by writing code
type: recap
block: Close + Q&A · 4
visible:
✓ The model is stateless; the app resends the conversation
✓ AGENTS.md keeps standing rules
✓ Git and GitHub keep your work safe
✓ Brainstorm → Spec → Plan → Execute → Test → Iterate
Checkpoint: s1-chatbot
diagram: none
build:
  0: title
  1: the four ticks appear one by one; checkpoint line last
notes:
Do not re-teach; touch each point quickly and link it to what they did. The model forgets, so the app resends the conversation and AGENTS.md remembers your rules. Git kept the work safe and GitHub holds the second copy, which you pushed twice today. And the method: brainstorm, spec, plan, execute, test, iterate. You ran it twice, for the dashboard and the chatbot. The synthesis: the work you did was judgement, not typing. You decided what to build, checked the plan and tested the result. Anyone who has not finished can switch to checkpoint s1-chatbot, which is the starting point for Session 2. Make sure everybody knows where to find the checkpoint link in the handout.
words: 28 · budget: 40 · exception: none
status: n/a

## 27. Questions
type: Q&A
block: Close + Q&A · 5
visible:
Questions?
diagram: Large "Questions?" heading. Around it, five small shapes keep moving on slow loops: three square speech bubbles drifting along different paths, one red "?" orbiting the heading, and one dot bouncing between the bubbles. No text inside the shapes.
build:
  0: heading and moving shapes (they loop for as long as the slide is open)
notes:
Open the floor. Start with a prompt if no one speaks: what surprised you today? Or: where would you use a dashboard like this at work? Collect parking-lot items on a flip chart. If a question needs a long answer, say you will cover it in Session 2 or the handout. Repeat questions before answering so the room hears them. Keep investment questions neutral: the app shows data; it does not advise. Check one more time that everyone has pushed, and that anyone behind has the s1-chatbot checkpoint.
words: 1 · budget: 40 · exception: none
status: n/a

## 28. Next session: your app remembers prices and learns the rules
type: talk
block: Close + Q&A · 1
visible:
Session 2:
- A database that remembers prices
- A watchlist: BBCA, BBRI, TLKM
- A Wiki so the chatbot knows the rules
diagram: none
build:
  0: all lines together
notes:
Preview Session 2 in one minute. Today the app fetches prices live and forgets everything when it restarts. In Session 2 it keeps prices in a database and adds a watchlist. The chatbot will also learn from a Wiki, a set of pages from official Indonesian sources, so its answers can name where they came from. Same method: brainstorm, spec, plan, execute, test, iterate. Remind everyone to keep their project or use checkpoint s1-chatbot. Thank them and close. Mention the time of the next session and any homework: none.
words: 20 · budget: 40 · exception: none
status: n/a

## Word count check

| id | type | words | budget | over? | notes words |
|---|---|---|---|---|---|
| 1 | title | 10 | 40 | no | 110 |
| 2 | visual | 17 | 40 | no | 136 |
| 3 | visual | 17 | 40 | no | 134 |
| 4 | visual | 31 | 40 | no | 133 |
| 5 | visual | 22 | 40 | no | 136 |
| 6 | visual | 22 | 40 | no | 128 |
| 7 | visual | 19 | 40 | no | 132 |
| 8 | visual | 17 | 40 | no | 137 |
| 9 | visual | 19 | 40 | no | 126 |
| 10 | check | 30 | 60 | no | 106 |
| 11 | visual | 25 | 40 | no | 144 |
| 11b | visual | 21 | 40 | no | 134 |
| 12 | visual | 17 | 40 | no | 127 |
| 13 | visual | 27 | 40 | no | 133 |
| 14a | run | 55 | 60 | no | 139 |
| 14b | run | 31 | 60 | no | 129 |
| 15 | visual | 16 | 40 | no | 115 |
| 16 | visual | 18 | 40 | no | 168 ! |
| 17 | visual | 36 | 40 | no | 140 |
| 18 | visual | 22 | 40 | no | 125 |
| 19 | visual | 13 | 40 | no | 121 |
| 20 | visual | 31 | 40 | no | 150 |
| 21a | run | 40 | 60 | no | 137 |
| 21b | run | 50 | 60 | no | 134 |
| 22 | check | 45 | 60 | no | 115 |
| 23 | visual | 24 | 40 | no | 132 |
| 24a | run | 43 | 60 | no | 127 |
| 24b | run | 60 | 60 | no | 137 |
| 25 | visual | 23 | 40 | no | 129 |
| 26 | recap | 28 | 40 | no | 116 |
| 27 | Q&A | 1 | 40 | no | 88 |
| 28 | talk | 20 | 40 | no | 89 |

slides: 32 · minutes: 180
