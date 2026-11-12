# Day 3 · Session 1 — slide copy v3 (repair + targeted reorder, 33 slides)

Course: AI Vibe Coding for Business Users · Session 1: Build your first AI Financial App · 3 hours, no break · English deck, speaker-led and hands-on.
Sources: `docs/outlines/day3-s1-v3.md` (33 headlines from spec §5, kept word for word), spec `docs/superpowers/specs/2026-11-12-day3-s1-v3-deck-design.md` (§6 redesigns, §7 vocabulary and per-slide fixes), `docs/copy/day3-s1-v2.md` (v2 copy; wording, notes and diagrams reused where still correct), `prompts/s1.md` (tested prompts), `.review/day3-s1-v2-review-report.md` (finding IDs).

How to read this file:
- Ids are the v3 `data-n` values, 1…33, in deck order.
- `visible:` is the on-slide text. Every label the diagram shows is listed in `visible:`; the `diagram:` line says where it goes.
- `build:` lists the click steps. Step 0 is what shows when the slide arrives. Unless a step says "replaces", text stays on screen once revealed.
- `words:` is the largest number of visible non-title words on screen at any one step, counted the way the deck renderer counts: split on spaces, so separators such as `·`, `→`, `—`, `+` and `/` count as words when they stand alone. Badge numbers count too. Prompts in fenced blocks are not counted. On check slides the count includes the choices, although the renderer leaves them out.
- Budgets (from `AGENTS.md`): 40 per reveal step on teaching slides, 60 on run and check slides.
- `status: tested` means the prompt is copied verbatim from `prompts/s1.md`. `UNTESTED` means it has not been run in opencode; rehearse it before class.
- Vocabulary (spec §7 V1): "the model" (LLM, defined on slide 4) · "opencode" (first mention "opencode, our coding agent") · "chat products" for ChatGPT and similar · "your financial app" for what participants build. `financial-app` is the literal folder and repository name.
- Colour key for slides 5–11: red = the model; black = opencode and its rules; grey/white = tools and data.
- Workflow names, exactly: Interview → Plan (Approve / Edit / Reject) → Execute → Test / Debug → Iterate.

## 1. Build your first AI Financial App
type: title
block: Opening · 2
visible:
Day 3 · Session 1
AI Vibe Coding for Business Users
diagram: none
build:
  0: title, subtitle and session line together
notes:
Welcome everyone. Today you build a real financial app, and nobody writes code by hand. You tell opencode, our coding agent, what you want, you check what it gives you, and you steer it. By the end of these three hours you will have a NISP dashboard and a chatbot, saved on GitHub. Before we start, check that opencode opens on every laptop, Windows and Mac, and that it answers a simple "hello". Anyone whose model does not reply, raise your hand now, so we fix it before the first exercise. About half of today is hands-on: I explain for a few minutes, then you do it, and we check together.
words: 11 · budget: 40 · exception: none
status: n/a

## 2. Today you direct opencode to build a NISP dashboard and chatbot, without writing code
type: visual
block: Opening · 5
visible:
NISP price
Daily change
1-year chart
Chatbot
Saved on GitHub
You direct. opencode writes the code.
diagram: A laptop browser frame, centre. Inside it the financial app mock-up: top-left a large price card "NISP price"; beside it a small card "Daily change" with a green arrow; below them a wide line chart "1-year chart"; on the right a narrow chat panel "Chatbot" with two speech bubbles. Under the laptop a GitHub badge "Saved on GitHub" with an upward arrow from the laptop. Caption along the bottom: "You direct. opencode writes the code."
build:
  0: empty browser frame and title
  1: "NISP price" and "Daily change" cards drop in
  2: "1-year chart" line draws left to right
  3: "Chatbot" panel slides in from the right
  4: arrow to "Saved on GitHub" badge; caption fades in
notes:
Say what the day produces, in business words. NISP is Bank OCBC NISP, listed as NISP.JK on the Indonesia Stock Exchange. On step 1, point at the cards: the latest available price in rupiah, and the daily change. Prices come from Yahoo Finance and can be delayed, so in Run 3 you check that your financial app shows the date and source. On step 2, the one-year chart. On step 3, the chatbot answers questions about that data. On step 4, the project is saved on GitHub. Optional quick look: open the finished financial app from checkpoint s1-chatbot at localhost:5173 and ask "What is NISP's latest price?" Have both servers running before class. Then ask: who has written code before? Few hands is fine. Your job is a manager's job: be clear about the goal, then judge the work. We show market data only, never advice to buy or sell.
words: 16 · budget: 40 · exception: none
status: n/a

## 3. Your job today: interview, approve the plan, then test what the agent builds
type: visual
block: Opening · 3
visible:
Interview
→ docs/spec.md
Plan
Approve / Edit / Reject
Execute
Test / Debug
Iterate
Run 2
Run 3
diagram: Five square boxes in a row joined by right arrows: "Interview", "Plan", "Execute", "Test / Debug", "Iterate" (these five are the `.wf` workflow names). Under "Interview", small text "→ docs/spec.md". Under "Plan", a chip "Approve / Edit / Reject". A red square return arrow (v2 drawing style) runs from the top of "Iterate" up, left along a straight line above the row, and down into the top of "Plan", with a clear arrowhead into "Plan". A bracket "Run 2" under Interview + Plan; a bracket "Run 3" under Execute → Iterate.
build:
  0: five grey boxes
  1: "Interview" and "Plan" light up in turn; "→ docs/spec.md" appears under Interview; the "Run 2" bracket appears
  2: the "Approve / Edit / Reject" chip pops under "Plan"
  3: "Execute", "Test / Debug", "Iterate" light up; the "Run 3" bracket; the return arrow from Iterate back to Plan draws once
notes:
This is your job for the rest of the day, so you see it before we look inside the agent. On step 1: Interview. The agent asks questions one at a time, you answer, and it writes what you agreed into docs/spec.md. We call it an interview: the agent asks, you answer. Some skills call this brainstorming. Then Plan: the agent proposes numbered steps. That is Run 2. On step 2, point at the chip: you approve, edit or reject the plan before anything is built. On step 3: Execute, the agent builds. Test / Debug: you check the result in the browser and, if something breaks, find the cause with the agent. Iterate: you ask for a change, which takes you back to Plan. That is Run 3. Nothing is built until Execute. The Run 2 and Run 3 slides show these five names, with a "you are here" marker.
words: 18 · budget: 40 · exception: none
status: n/a

## 4. An LLM writes its answer one small piece of text at a time
type: visual
block: How a coding agent works · 3
visible:
Text in: "NISP is the ticker of Bank OCBC ..."
LLM
Text out: "NISP"
NISP · Indonesia · Bank
Illustration
LLM = large language model
diagram: A wide input box on the left with the "Text in" sentence. An arrow into a central red rounded box "LLM". An arrow out to a box on the right where the next piece appears ("Text out"). Under the right box, three candidate pieces in a small ranked list with bars: "NISP" (longest bar), "Indonesia", "Bank", with the small label "Illustration" beside the bars (they are not measured numbers). Footer line: "LLM = large language model".
build:
  0: "Text in" box and the "LLM" box
  1: the sentence types out word by word into the input box
  2: arrow pulses through the LLM a few times, then stops; the ranked list appears with bars growing and the "Illustration" label
  3: "NISP" lifts out of the list into the output box
notes:
Start with what an LLM is: a large language model. It writes its answer one small piece of text at a time. The pieces are called tokens; a piece is often a word, sometimes part of one. On step 1, read the sentence as it types. On step 2, point at the bars: the model scores possible next pieces. Say clearly that the bars are an illustration, not measured numbers. On step 3, it picks one, here "NISP", adds it, and repeats. It learned language patterns from a huge amount of text, so it can sound like an expert. But fluent is not the same as correct: it can be confidently wrong, and its training is no source for current stock prices. So we give it real data and check. From now on we call it the model. Ask: who has used ChatGPT or Copilot? Those are chat products built on a model.
words: 25 · budget: 40 · exception: none
status: n/a

## 5. The model doesn't remember earlier requests; opencode sends the context it needs
type: visual
block: How a coding agent works · 3
visible:
Turn 1 sends: Question 1
Turn 2 sends: Question 1 + Answer 1 + Question 2
Turn 3 sends: the chat so far + Question 3
Model
opencode resends it. The model doesn't remember.
diagram: Three horizontal rows, one per turn, each a row of small rounded boxes. Row "Turn 1 sends": one box "Question 1". Row "Turn 2 sends": three boxes "Question 1", "Answer 1", "Question 2". Row "Turn 3 sends": a longer box "the chat so far" followed by "Question 3". Each row has an arrow on the right into one red box "Model". The Turn 1 arrow is visible from step 0 (fix A1). Caption under the rows is the last line of visible.
build:
  0: title, the "Model" box, the "Turn 1" row and its arrow into "Model"
  1: "Turn 2" row slides in, with its arrow; its earlier boxes are copies of row 1
  2: "Turn 3" row slides in, the longest, with its arrow
  3: caption appears in accent colour
notes:
The model doesn't remember earlier requests; each call to it stands alone. On step 0, point at turn one and its arrow: the conversation part of turn one is just Question 1; on the next slide we add what opencode sends alongside it. Ask: then why does a chat seem to remember? On step 1, answer it: opencode keeps the conversation and sends it again with your new message; chat products do something similar. On step 2, the rows get longer. Apart from its training, the model works only with what it is sent: longer chats can cost more and run slower, and messages not sent, it can't see. On step 3, say the caption. One caution: this is called stateless, but that doesn't mean the service stores nothing; products may keep chat history or offer memory features. Our own chatbot later sends the whole message list every turn. This slide shows only the conversation part, simplified.
words: 34 · budget: 40 · exception: none
status: n/a

## 6. On every turn, opencode sends the model a stack: rules, skills, the chat so far, your message
type: visual
block: How a coding agent works · 4
visible:
opencode
Model
Simplified view
System prompt — opencode's own rules
AGENTS.md — your project rules
Skill list — names and descriptions only
Conversation so far — your messages, its replies, tool results
Your new message
Sent every turn
Grows
diagram: Left: an empty black-outlined stack frame labelled "opencode", holding five rows read top to bottom. One arrow from the stack to a red "Model" box on the right. Rows 1–3 are black (opencode and its rules): "System prompt — opencode's own rules", "AGENTS.md — your project rules", "Skill list — names and descriptions only". Row 4 is grey and visibly taller: "Conversation so far — your messages, its replies, tool results". Row 5 is white: "Your new message". At step 6 a bracket beside rows 1–3 reads "Sent every turn" and a bracket beside row 4 reads "Grows". Footnote bottom-left: "Simplified view".
build:
  0: the "Model" box, the empty "opencode" stack frame with its arrow, and the footnote "Simplified view"
  1: row 1 "System prompt — opencode's own rules"
  2: row 2 "AGENTS.md — your project rules"
  3: row 3 "Skill list — names and descriptions only"
  4: row 4 (grey, visibly taller) "Conversation so far — your messages, its replies, tool results"
  5: row 5 "Your new message"; then the whole stack is sent along the arrow to the Model once
  6: the brackets "Sent every turn" (rows 1–3) and "Grows" (row 4)
notes:
Now look at what opencode sends. This is a simplified view, not the exact request format. Red is the model; black is opencode and its rules. On step 1, the system prompt: opencode's own instructions. On step 2, AGENTS.md, your project rules; you make yours in Run 1. On step 3, the skill list: names and descriptions only. A full skill is loaded later, if the agent decides one fits. On step 4, the tall grey row: the conversation so far, including tool results. Apart from AGENTS.md, the model only reads a file if a tool brings its text into this row. On step 5, your new message, and the stack goes to the model. On step 6: opencode rebuilds the top three rows for every call to the model, even calls after a tool result; this was checked in the opencode source, version 1.19.5. Messages also carry roles: system, user, assistant, tool. The handout has the glossary.
words: 39 · budget: 40 · exception: none
status: n/a

## 7. The context window has a limit, so old chat gets summarised; save decisions in files
type: visual
block: How a coding agent works · 3
visible:
Context window
Room for the reply
Long chat → near the limit
Older chat → a short summary
Rules stay
Details can be lost
Rules → AGENTS.md · requirements → spec · steps → plan. /new starts clean, so save first.
diagram: A fixed frame labelled "Context window". Inside it, the same stack as slide 6, in the same colours and order but without row text: three black rows (rules) at the top, a short grey row 4 (the chat) below them, and blank space at the bottom labelled "Room for the reply". At step 1 row 4 grows downward toward the limit, with the label "Long chat → near the limit" beside it; it stops before the frame edge. At step 2 the older part of row 4 shrinks into one smaller block labelled "Older chat → a short summary", which replaces the step-1 label; the label "Rules stay" points at rows 1–3, which do not move. At step 3 a small warning tag "Details can be lost" sits beside the summary block. At step 4 a takeaway bar runs across the bottom of the slide. Nothing ever leaves the frame, and nothing labelled rules moves.
build:
  0: the frame "Context window", rows 1–3 in place, a short row 4, the blank "Room for the reply"
  1: row 4 grows toward the limit; "Long chat → near the limit"
  2: the older part of row 4 shrinks into one summary block; "Older chat → a short summary" replaces the step-1 label; "Rules stay" points at rows 1–3, which don't move
  3: the warning tag "Details can be lost"
  4: the takeaway bar
notes:
Same stack, now inside a frame: the context window, the most text the model can handle in one call, its reply included. Limits differ by model, so no numbers, and these sizes are only illustrative. On step 0, point at the blank space: the reply needs room too. On step 1, a long chat grows toward the limit. On step 2, opencode shortens the older chat into a summary. Point at the top rows: they don't move, because they are sent every turn. How opencode shortens history depends on its settings. On step 3: a summary keeps the gist, not every detail, so an instruction from an hour ago can be lost. On step 4, the habit: save decisions in files. Rules in AGENTS.md, requirements in the spec, steps in the plan. /new starts a conversation without the earlier chat. It doesn't delete files, and it can't bring back what you never saved, so save first.
words: 35 · budget: 40 · exception: none
status: n/a

## 8. The model asks for a tool; opencode checks permission and runs it
type: visual
block: How a coding agent works · 4
visible:
opencode
on your laptop
Model
Tool: read a file
1 Your message + list of tools
2 Please read docs/spec.md
3 Check permission, then run
4 File text
5 Conversation + file text
6 Answer, or another tool request
diagram: Three vertical lanes, left to right: "opencode" (black header, small label "on your laptop"), "Model" (red header), "Tool: read a file" (white header). Six rows run top to bottom, one per click. Each row is one arrow with a number badge (1–6, each used once) and its label above the arrow: 1 opencode → Model "Your message + list of tools"; 2 Model → opencode "Please read docs/spec.md"; 3 opencode → Tool "Check permission, then run", with a small gate icon on the arrow; 4 Tool → opencode "File text"; 5 opencode → Model "Conversation + file text"; 6 Model → opencode "Answer, or another tool request". The Model lane never has an arrow to the Tool lane. Each arrow draws once; no travelling packets, no pulsing model.
build:
  0: the three lane headers and "on your laptop", no arrows
  1: row 1 opencode → Model
  2: row 2 Model → opencode
  3: row 3 opencode → Tool, with the gate icon
  4: row 4 Tool → opencode
  5: row 5 opencode → Model
  6: row 6 Model → opencode
notes:
How does the agent read files or run commands? Tool calling. Three lanes: opencode on your laptop, the model, and a tool that reads a file. On step 1, opencode sends your message plus the list of tools it can run. On step 2, the model asks: please read docs/spec.md. That is plain-language shorthand, not the real tool syntax. On step 3, point at the gate: opencode checks its permission settings, then runs the tool. Depending on the settings, some actions run without asking, some ask you first, some are refused. On step 4, the file text comes back. On step 5, opencode calls the model again with the conversation plus that text. On step 6: an answer, or another tool request. The key point: the model never touches your laptop; opencode does, within its permission settings. When a permission box appears, read it. Your financial app's chatbot won't use tools; its back end adds the data.
words: 39 · budget: 40 · exception: none
status: n/a

## 9. A coding agent repeats model decisions and tool actions, then you check the result
type: visual
block: How a coding agent works · 3
visible:
Goal
Model decides
opencode runs a tool
Model reads the result
Agent reports back
You test
Agent: proposes and does. You: decide and check.
diagram: A circular loop of three boxes, arrows clockwise: red "Model decides" → black "opencode runs a tool" → red "Model reads the result" → back to "Model decides". An arrow enters the loop from the left labelled "Goal". An arrow leaves to the right into a box "Agent reports back", then a second arrow into a separate box "You test". Punch line under the loop. A highlight dot travels round the loop continuously from step 2 (the only continuous loop on slides 4–11, because repetition is the concept).
build:
  0: "Goal" arrow and the empty circle
  1: the three loop boxes appear in order with their arrows
  2: a highlight dot starts travelling round the loop and keeps going
  3: exit arrow to "Agent reports back", then "You test"; punch line fades in
notes:
Put the last slides together. When we say "the agent", we mean opencode and the model working in this loop. On step 0, you give a goal. On step 1, the model decides the next action, usually a tool; opencode runs it; the model reads the result and decides again. On step 2, let the dot go round. This is the one animation that keeps moving, because repetition is the point. One request can take minutes and touch many files, and every step builds on your goal, so a vague goal makes the loop wander. On step 3, the loop ends when the agent reports back. It can also stop for an error, a limit or a question for you. Reporting back is a claim, not proof, so the next box is you, testing. Read the punch line: the agent proposes and does; you decide and check.
words: 24 · budget: 40 · exception: none
status: n/a

## 10. AGENTS.md is the project's standing brief, so keep it current
type: visual
block: How a coding agent works · 4
visible:
New conversation
Yesterday's chat isn't included
Like a new colleague on day one
AGENTS.md is handed over every turn
The project's standing brief
AGENTS.md
In: What the project is · How to run and check it · Working rules
Out: Passwords and keys · Chat logs · Feature details (→ spec)
/init drafts it → you spot a lasting rule or a repeated correction → ask the agent to update it → read the change → commit
Today: ask the agent to edit AGENTS.md, then review it.
diagram: One frame area; each click replaces the previous frame instead of stacking on it. Frame 0: a "New conversation" card with an empty chat bubble, and the lines "Yesterday's chat isn't included" and "Like a new colleague on day one" (an onboarding-note picture). Frame 1: the same New conversation card; a black document labelled "AGENTS.md" slides into it, with "AGENTS.md is handed over every turn" and "The project's standing brief" beside the card. Frame 2: the document opens into two lists under the heading "AGENTS.md": "In" (What the project is · How to run and check it · Working rules) and "Out" (Passwords and keys · Chat logs · Feature details (→ spec)). Frame 3: a one-time entry "/init drafts it" leads into the maintenance loop, read left to right: "you spot a lasting rule or a repeated correction" → "ask the agent to update it" → "read the change" → "commit". The return arrow goes from commit back to spotting a rule, not to /init. Step 4 adds a footer bar under the frame-3 loop. Pressing ← restores the previous frame exactly.
build:
  0: frame 0: "New conversation" card, empty bubble, "Yesterday's chat isn't included", "Like a new colleague on day one"
  1: frame 1 replaces frame 0: AGENTS.md slides into the card; "AGENTS.md is handed over every turn" · "The project's standing brief"
  2: frame 2 replaces frame 1: AGENTS.md opens into the "In" and "Out" lists
  3: frame 3 replaces frame 2: /init as a one-time entry, then the maintenance loop left to right; commit returns to spotting a rule
  4: the footer "Today: ask the agent to edit AGENTS.md, then review it." appears under the loop
notes:
Think of AGENTS.md as an onboarding note for a new colleague. On step 0: a new conversation doesn't include yesterday's chat. On step 1: opencode hands AGENTS.md over every turn, as in the stack. On step 2, read the two lists; feature details belong in the spec. On step 3, /init drafts the file once. Then follow the upkeep cycle left to right: spot a lasting rule or a repeated correction, ask the agent to update the file, read the change, commit. The return arrow goes back to spotting another rule, not to running /init again. On step 4, why we work this way today. AGENTS.md is a plain text file, so you can edit it yourself. Today we ask the agent instead: you say the rule in plain words, the agent keeps the file's structure and wording consistent, and we avoid accidental deletions. It can still make mistakes, so read the change. Git makes the change reviewable and reversible whoever typed it. Rules guide the agent; they don't guarantee it obeys, so still check its work.
words: 36 · budget: 40 · exception: none
status: n/a

## 11. Check: a new conversation ignored your preference. What do you do?
type: check
block: How a coding agent works · 3
visible:
A new conversation ignored your "explain first" preference. What do you do?
A. Repeat it at the start of every chat
B. Ask opencode to add it to AGENTS.md, review it, commit
C. Switch to a stronger model
diagram: none
build:
  0: question and the three choices
  1: B highlights green; A and C fade; reveal line appears
reveal: B — A new conversation doesn't include old chats. AGENTS.md is sent every turn.
notes:
Read the question aloud. Give them thirty seconds, then take a show of hands for A, B and C, one at a time. A works, but only while you remember to type it in every new chat. C is tempting, but a stronger model doesn't see yesterday's chat either. Click to reveal B. A new conversation doesn't include old chats, and AGENTS.md is sent on every turn, so a rule saved there reaches every new conversation in this project. The order matters: ask opencode to add the rule, read the change, then commit. If a saved rule still seems ignored, remember the last slide: rules guide the agent, they don't guarantee it obeys. Check the file is in the project folder, and check the work. Then ask one person what rule they would add for their own work. This closes the block on how a coding agent works.
words: 52 · budget: 60 · exception: none
status: n/a

## 12. Use a quick model for small edits and a stronger one for planning and debugging
type: visual
block: Models and Git · 3
visible:
Quick · [FAST MODEL]
rename a title · fix a typo · change a colour
Stronger · [SMART MODEL]
write the plan · find why something breaks
Switch with /models
diagram: Two horizontal lanes like a road. Top lane "Quick" with a small car icon and the [FAST MODEL] placeholder; its three job chips sit along the lane. Bottom lane "Stronger" with a truck icon and a thinking icon, and the [SMART MODEL] placeholder; its two job chips. A badge at the right edge: "Switch with /models". The car and the truck each cross their lane once, then stop (A5).
build:
  0: the two empty lanes with "Quick" and "Stronger" labels and the placeholders
  1: quick-lane job chips drop in; the car crosses once and stops
  2: stronger-lane job chips drop in; the truck crosses slowly once and stops; a thought bubble appears
  3: "/models" badge appears
notes:
Before class, replace [FAST MODEL] and [SMART MODEL] with real names from the model list your participants share. This is a rule of thumb, not a law. On step 1: a quick model usually replies faster and costs less. It suits small, clear jobs where you see the result straight away. On step 2: a stronger model usually does better on harder reasoning, and is often slower. Use it for planning, where a bad plan wastes the whole build, and for debugging, when the cause is not obvious. Either model can be wrong, so compare results on your real task and check them. On step 3, show the picker: type /models in opencode. Names differ by provider, so say "pick one quick and one stronger model from your list". Today we use the stronger model for the plan.
words: 30 · budget: 40 · exception: none
status: n/a

## 13. On supported models, higher effort lets the model reason more before answering
type: visual
block: Models and Git · 2
visible:
low · medium · high
Low effort: quicker replies, small edits
High effort: reasons more, usually slower; plans and hard bugs
Ctrl+T cycles the options your model offers
diagram: A horizontal dial with three marks, "low", "medium", "high". A red pointer sits at "low". Under the dial, a "thinking" bar and a small clock icon. The low-effort line sits under the left end of the dial, the high-effort line under the right end. A caption with a key badge "Ctrl+T" at the bottom right. No looping motion: one click moves the pointer from low to high and it stays there (A3). The pointer, bar and clock hand (`.eff-hand`, `.eff-ptr`, `.eff-bar`) are listed in the reduced-motion rule (A4).
build:
  0: the dial with the pointer at "low"; the low-effort line
  1: the pointer slides once from "low" to "high" and stays; the thinking bar grows and stays; the high-effort line appears
  2: the caption "Ctrl+T cycles the options your model offers" appears
notes:
Model choice is one lever; effort is a second, on models that support it. On step 0: low effort replies quicker, which is right for a typo or a colour change. On step 1, the one click: the pointer moves to high and stays there. High effort lets the model reason more before it answers. That usually takes longer and can cost more, and it doesn't guarantee a better answer. Use it for the plan, for a bug you cannot explain, or for any step that is hard. On step 2: in opencode, Ctrl+T cycles the options your model offers. opencode calls them variants; their names and effects depend on the model, and effort is a common one. On a Mac it is also the Control key, not Command. If Ctrl+T changes nothing, your model may offer no options; ask me if unsure.
words: 28 · budget: 40 · exception: none
status: n/a

## 14. Everyone works on a local copy and shares through GitHub
type: visual
block: Models and Git · 3
visible:
Budget_final_v2_REALLY.xlsx?
Your computer: local copy
GitHub: shared copy
push / pull
Saving alone doesn't upload your work.
diagram: Left: a laptop "Your computer" with subtitle "local copy". Right: a cloud filing cabinet "GitHub" with subtitle "shared copy". A double-headed arrow between them labelled "push / pull". On arrival a messy pile of spreadsheet cards sits in the centre with the file name and a red question mark. Punch line under the diagram.
build:
  0: the messy file pile with the red question mark
  1: the pile shrinks into the laptop; "Your computer: local copy" appears
  2: "GitHub: shared copy" appears on the right
  3: the "push / pull" arrow draws; the punch line appears
notes:
On step 0 ask: who has a folder of files like Budget_final_v2_REALLY? Hands up. With copies like these, nobody knows which file is the real one, who changed what, or what was lost. Git keeps one project and records each version you commit. On step 1: your local copy is the project folder on your laptop. On step 2: GitHub is a website that hosts a shared copy; it is the host we use today. On step 3, the key sentence: saving alone doesn't upload your work. Your work reaches GitHub only when you push, and a teammate's changes reach you when you pull. Many beginners think saving a file shares it. It doesn't. Why this matters with an agent: it changes many files quickly, so you want save points to go back to, and a copy that is not only on your laptop.
words: 17 · budget: 40 · exception: none
status: n/a

## 15. A commit is a save point on your laptop; push copies it to GitHub, pull brings changes back
type: visual
block: Models and Git · 4
visible:
Saved on laptop → Committed (save point) → Pushed (on GitHub)
.env: left out
Created the budget file
Added March figures
Fixed the totals
push
pull
Tom's change
pull → edit → commit → push
diagram: A three-state strip across the top forms three zones, left to right: "Saved on laptop" (a laptop with a few file icons, one of them ".env") → "Committed (save point)" (a row of commit dots on the laptop, each with its note underneath) → "Pushed (on GitHub)" (a GitHub box). The ".env" file is drawn greyed with a small "left out" tag, ".env: left out", and never moves into a commit. Arrow "push" from the commit zone to GitHub; arrow "pull" from GitHub back. A teammate commit "Tom's change" appears in GitHub. Bottom: the routine as four small boxes joined by arrows: "pull → edit → commit → push".
build:
  0: the "Saved on laptop" zone with its files, including ".env"
  1: "→ Committed (save point)" appears; the first commit dot "Created the budget file"; ".env" greys out with "left out"
  2: commits "Added March figures" and "Fixed the totals" appear with their notes
  3: "→ Pushed (on GitHub)" appears; the three commits travel along "push" into GitHub once
  4: "Tom's change" appears in GitHub and travels back along "pull" once
  5: the routine row appears
notes:
On step 0: saved on laptop means the file is on your disk, nothing more. On step 1: a commit is a save point with a short note. It records the files included in it. Point at .env: it will hold the secret key. In Run 3 we put .env on Git's ignore list before the key goes in, and before pushing we ask the agent to list the files, to confirm .env is not there. On step 2: "Fixed the totals" tells you what happened; "stuff" doesn't. Commits stay on your laptop until you push. On step 3: push copies your commits to GitHub. On step 4: pull brings a teammate's commits down; if two people changed the same lines, it may need help. On step 5, the routine: pull, edit, commit, push. Today you work alone, so you mostly push, and you ask opencode in plain English instead of typing Git commands.
words: 35 · budget: 40 · exception: none
status: n/a

## 16. Run 1a: sign up to GitHub and draft AGENTS.md with /init
type: run
block: Run 1 · 12
visible:
github.com → Sign up. Confirm email.
opencode must be open in the financial-app folder (the path shown ends in financial-app).
Type /init.
Permission box? Read the path. Inside financial-app? Allow once. Anything else or unsure? Raise your hand. Never "Allow always".
AGENTS.md exists.
12 min · Stuck? Raise your hand.
diagram: Run card with three replacement panels: setup, permission, result.
build:
  0: sign-up, setup and /init
  1: permission line replaces setup panel
  2: result and time replace permission panel
notes:
Start GitHub sign-up first, because the confirmation email can take time. On step 0, point at the path in opencode: it must end in financial-app. Anyone with an account can sign in instead. Check spam if the email is late. Type /init while waiting. On step 1, read the permission wording aloud. A request outside the project can be a mistyped path, not something needed for the exercise. Do not approve it automatically; raise a hand and let me check. On step 2, open AGENTS.md and confirm it exists. If nothing changes for two minutes, check whether opencode is waiting for permission or input before pressing Esc and retrying /init. Help anyone still stuck reach checkpoint s1-start.
words: 22 · budget: 60 · exception: none
status: tested (/init)

## 17. Run 1b: add your rule, check it, then push to a private repository
type: run
block: Run 1 · 14
visible:
Prompt 1:
```text
Add one rule to AGENTS.md: Explain what you will do in plain business language before doing it.
```
Open AGENTS.md. Is your rule there? Then send Prompt 2.
Prompt 2:
```text
Commit all files in this project with the message "Start project". Create a new private GitHub repository called financial-app and push to it. Tell me if I need to sign in.
```
You should see: A private financial-app repo on github.com with AGENTS.md.
14 min · Stuck? Raise your hand. Checkpoint s1-start.
diagram: Two prompt panels with the review line between them.
build:
  0: Prompt 1 and review line
  1: Prompt 2, result, time and stuck line
notes:
On step 0, send Prompt 1 exactly as written. Open AGENTS.md together and point at the added rule. The surrounding bullets may differ; the rule must be there before anyone continues. If it is missing, ask opencode to correct the file and read it again. Click to step 1 only after that check. Prompt 2 requests a private repository, a commit and a push. Follow the sign-in instructions on screen, but do not paste passwords or access keys into chat. Open github.com and check the account, the Private label, and AGENTS.md inside financial-app. Saving locally is not enough. The push prompt is untested, so rehearse real sign-in on both laptop platforms before class. Anyone blocked gets help with checkpoint s1-start.
words: 34 · budget: 60 · exception: none
status: tested (Prompt 1) · UNTESTED (Prompt 2)

## 18. Choose how to instruct the agent by the job: this task, project rules, expertise or a sequence
type: visual
block: Skills · 3
visible:
Prompt — this task
AGENTS.md — standing project rules
Skill — reusable expertise
Workflow — a repeatable sequence
Session 3
They work together.
diagram: Four equal-size cards, not stairs. Session 3 is attached to Workflow. Each card settles after one entrance.
build:
  0: four empty equal cards
  1: Prompt and AGENTS.md text
  2: Skill text
  3: Workflow text, Session 3 chip and footer
notes:
On step 0, point at the equal cards: none is a higher rank. On step 1, connect the first two to what participants just did. The message was a prompt for one task; AGENTS.md keeps standing project rules. On step 2, a skill packages expertise for reuse, such as interviewing before proposing a design. On step 3, a workflow gives a repeatable sequence; we return to that in Session 3. Read the footer: these can work together. Ask which card fits a one-off title change, then a rule for every new conversation. If someone confuses a skill with AGENTS.md, use the distinction between expertise for a particular job and rules for this project.
words: 23 · budget: 40 · exception: none
status: n/a

## 19. The agent sees each skill's name and description, and loads the full skill when it decides one fits
type: visual
block: Skills · 4
visible:
Context
brainstorming — ask before proposing
page design — arrange a readable page
report writing — structure findings
Not loaded
Help me plan a dashboard
Full skill
Ask one question at a time.
Summarise the agreed requirements.
diagram: Context box on left holds the names and descriptions. Shelf on right is labelled Not loaded; no duplicate skill-name labels. A request bubble appears. The full brainstorming card lands entirely inside Context. Text is illustrative, not a quoted installed skill.
build:
  0: Context with name-description rows and Not loaded shelf
  1: request bubble
  2: brainstorming row highlights; arrow to shelf
  3: request bubble disappears; Full skill card slides fully inside Context
notes:
On step 0, connect the context box to the earlier stack. Names and short descriptions help opencode choose; full instructions are not all loaded at once. These short descriptions and instructions illustrate the mechanism, not a supplied course skill kit. On step 1, point at the request to plan a dashboard. On step 2, opencode decides whether brainstorming fits. It can miss a useful skill; matching is not guaranteed. On step 3, the full card is inside the context box, where its instructions can guide the next response. You can also name a skill; look for the "skill loaded" line. If someone has no skills installed, reassure them that today's prompts ask for the same habits directly.
words: 32 · budget: 40 · exception: none
status: n/a

## 20. A brainstorming skill makes "ask questions first" a repeatable habit
type: visual
block: Skills · 4
visible:
Illustration
Request: NISP page for client meetings
Straight answer
Show price.
Add change.
Draw chart.
Questions first
Who uses it?
How fresh?
Which device?
Summary
Sales team.
Dated prices.
Laptop page.
diagram: Request above two panels. The left is a three-line straight answer; the right has three questions and a three-line summary. No placeholder bars.
build:
  0: Illustration, request and panel headings
  1: left answer
  2: right questions
  3: summary below questions
notes:
Point at Illustration on step 0: this is a teaching example, not the result of a controlled comparison. On step 1, read the straight answer. It may be useful, but the agent has guessed the audience and freshness requirements. On step 2, the questions make those decisions visible to the business user. On step 3, the summary records what the answers meant before any building begins. The same habit can be asked for in a prompt; a skill makes it repeatable. If someone asks whether a skill guarantees better work, say no: check the questions, summary and result. If the example feels abstract, ask which missing question would matter before a client meeting, without introducing customer information.
words: 31 · budget: 40 · exception: none
status: n/a

## 21. An agent builds what it guesses you want, so interview first
type: visual
block: Run 2 · 3
visible:
"Build me a stock dashboard"
Guesses: which stocks? which period? what layout?
Who will use this?
Sales team before client meetings.
Interview first.
diagram: Vague request leads to question marks and a mismatched dashboard. A lower path shows a question, answer and checked dashboard. Each arrow draws once and settles.
build:
  0: vague request
  1: guesses
  2: mismatched dashboard
  3: interview path with question, answer and takeaway
notes:
On step 0, read the vague request. On step 1, point at each gap: which stocks, which period and what layout? opencode can fill these gaps with guesses, but those guesses are not your requirements. On step 2, the result may look polished and still solve the wrong problem. On step 3, show the interview path: a question and a business answer make the intended use clear. We call it an interview; some skills call this brainstorming. If someone cannot answer a technical question, ask them to describe the business outcome instead. Before the next run, remind everyone to answer one question at a time and check the summary, rather than approving a build immediately.
words: 23 · budget: 40 · exception: none
status: n/a

## 22. The interview produces a spec (what and why); the plan says how, and you approve, edit or reject it
type: visual
block: Run 2 · 4
visible:
docs/spec.md: what and why
Spec = PRD (product requirements document)
Goals · Out of scope · How we'll know it works
docs/plan.md: how, in numbered steps
Approve / Edit / Reject
diagram: Two document cards joined by one arrow. Spec headings on left; numbered plan lines on right; three decision buttons below right.
build:
  0: spec card and Spec = PRD line
  1: spec headings
  2: plan card and arrow
  3: decision buttons
notes:
On step 0, point at docs/spec.md. It records what your financial app should do and why; here a spec is a short PRD, or product requirements document. On step 1, explain the three sections. Goals name the result, Out of scope blocks extras, and How we'll know it works gives checks you can perform. On step 2, the plan is different: numbered steps for making that result. On step 3, you approve, edit or reject it against the spec. If someone cannot judge a technical step, ask whether its business outcome belongs in the spec and call me over for the technical detail. Saving these documents makes decisions available beyond the current conversation.
words: 31 · budget: 40 · exception: none
status: n/a

## 23. Check: approve, edit or reject these three plans
type: check
block: Run 2 · 4
visible:
Plan 1: follows the spec.
Plan 2: follows the spec, plus a login screen nobody asked for.
Plan 3: shows a chart, but for the wrong stock (BBRI).
A. Approve 1 · Edit 2 · Reject 3
B. Approve 1 · Approve 2 · Edit 3
C. Edit 1 · Reject 2 · Reject 3
diagram: Three plan summaries above three choices. On reveal replace summaries with answer explanation while choices remain.
build:
  0: plans and choices
  1: A highlights green; summaries disappear; reveal line appears
reveal: A — Approve what matches the spec, edit what adds extras, reject what contradicts it.
notes:
Read the three plans on step 0, then give people time to choose. Ask for hands for A, B and C before revealing anything. Plan 2 is tempting: a login screen may sound sensible, but it adds work nobody requested. Plan 3 has the right kind of picture but the wrong stock, so it misses a central requirement. On step 1, point at A. Approve 1, edit 2 to remove the extra login, and reject 3 for a corrected plan. If someone chose to edit 3, acknowledge that a clear correction can work too; here the quiz treats the wrong stock as a reason to request a replacement plan. Bring the discussion back to comparing your own plan against your spec.
words: 55 · budget: 60 · exception: none
status: n/a

## 24. Run 2a: interview for the dashboard and save the spec
type: run
block: Run 2 · 12
visible:
Interview · Plan · Execute · Test / Debug · Iterate
Current: Interview
Prompt 1 (interview):
```text
Let's brainstorm a NISP stock dashboard together. It should show the latest price, the daily change and a 1-year price chart. Ask me one question at a time, at most 5, in plain business language. Don't write any code or files yet.
```
Answer briefly.
Prompt 2 (spec):
```text
Write what we agreed to docs/spec.md. Use three sections: Goals, Out of scope, and How we'll know it works. Don't build anything yet. We'll use React + Vite, FastAPI (Python) and yfinance, with endpoints GET /api/quote/{ticker} and GET /api/history/{ticker}?period=1y, server on port 8000, page on port 5173.
```
The last sentence is technical setup from the course — copy it as is.
You should see: Up to five questions, one at a time, a summary, then docs/spec.md. No code yet.
12 min · Stuck? s1-spec.
diagram: Workflow mini-map (.wf) above two replacement prompt panels. Current step Interview. The course-supplied label sits directly under Prompt 2.
build:
  0: mini-map, current step, Prompt 1 and answer tip
  1: Prompt 2 and course-supplied label replace Prompt 1 and tip
  2: result, time and stuck line replace prompt panel; mini-map remains
notes:
On step 0, point at Interview on the mini-map. Send Prompt 1 as written and answer each question in one short sentence. Questions vary; the limit is five, not a promise of exactly five. Use business terms, such as sales team before client meetings, delayed prices with a date, and mostly laptops. If opencode starts building, stop it and repeat that no code or files are wanted yet. On step 1, send the spec prompt after the summary, not a general go-ahead. Point at the label: the technical sentence is course setup, so copy it unchanged. On step 2, open docs/spec.md and check the business requirements. Anyone stuck raises a hand for help reaching checkpoint s1-spec.
words: 36 · budget: 60 · exception: none
status: tested (both prompts)

## 25. Run 2b: get the plan, approve, edit or reject it, then save it
type: run
block: Run 2 · 12
visible:
Interview · Plan · Execute · Test / Debug · Iterate
Current: Plan
Stay in this conversation — no /new until the plan is saved.
1. Tab: footer "plan". Send:
```text
Read docs/spec.md and give me a numbered step-by-step plan to build it. Don't build anything yet.
```
2. Check it against your spec: only price, change and 1-year chart? Nothing extra? Then approve, edit or reject.
3. Tab: footer "build". Send:
```text
Save that plan to docs/plan.md. Don't build anything yet.
```
You should see: docs/plan.md.
12 min · Stuck? s1-spec.
diagram: Workflow mini-map (.wf), current Plan, then three replacement instruction panels. The same-conversation warning remains throughout.
build:
  0: mini-map, current step, conversation warning and step 1
  1: step 2 replaces step 1
  2: step 3, result, time and stuck line replace step 2; conversation warning remains
notes:
On step 0, point at the footer: it must say plan. Plan mode is for proposing, not changing your financial app; still check what opencode does. Send the plan prompt and stay in this conversation. On step 1, compare the plan with docs/spec.md, not with how impressive the proposal sounds. Ask for changes if it adds login, other stocks or features you did not agree. Reject a plan that misses the purpose and read its replacement. If someone is unsure about a technical step, call me over rather than approving blindly. On step 2, switch the footer to build and send the save prompt. Open docs/plan.md and check it matches the approved version. Help anyone behind reach checkpoint s1-spec.
words: 44 · budget: 60 · exception: none
status: tested (both prompts)

## 26. Your financial app has a screen, a back end, a data source and an AI service
type: visual
block: Run 3 · 4
visible:
Screen (in your browser)
React · 5173
Back end
FastAPI · 8000
yfinance: NISP data
AI service (LLM)
backend/.env — service address, model name, secret key. Not the AI.
diagram: Laptop boundary contains screen and back end; yfinance data source and red AI service box are outside it. Settings card beside back end, no padlock in label. Unlabelled arrows avoid extra visible words.
build:
  0: laptop and Screen, with React and port
  1: Back end, FastAPI and port, joined to screen
  2: data source and arrows; one data packet returns and stops
  3: AI service and settings card appear
notes:
On step 0, point at the screen: this is what you open in your browser. On step 1, the back end is a program on your laptop that handles requests from the screen. localhost means this laptop; 5173 and 8000 are the ports we chose. On step 2, the back end fetches NISP prices through yfinance and sends the data to the screen. On step 3, the AI service is outside the laptop. backend/.env holds its address, model name and secret key, not the model itself. The file does not protect itself; we keep it out of chat and Git. If someone opens the wrong address, check which server and port opencode told them to use.
words: 29 · budget: 40 · exception: none
status: n/a

## 27. When something breaks, remove secrets, paste the error, and ask the agent to explain it
type: visual
block: Run 3 · 4
visible:
Copy the error
Remove keys and private data
Ask: "Explain in plain words, then fix it."
Repeat the check that failed
opencode · server window · browser
diagram: Four boxes left to right with arrows. Source chips below the first box. Each arrow draws once and settles.
build:
  0: Copy the error and source chips
  1: Remove keys and private data
  2: Ask box
  3: Repeat the check that failed
notes:
On step 0, point at the source chips. The error may be in opencode, the server window or the browser; copy the actual text rather than reconstructing it from memory. On step 1, remove keys and private data before sending anything. Do not paste customer details or the contents of backend/.env. If unsure what is sensitive, raise a hand first. On step 2, ask opencode to explain in plain words before fixing it, so you can judge the proposed action. On step 3, repeat the exact check that failed. A quiet agent is not always stuck; check whether it is running a command or waiting for input before re-sending. If a secret has already been shared, tell me immediately so it can be replaced.
words: 27 · budget: 40 · exception: none
status: n/a

## 28. Run 3a: build the dashboard and check its numbers
type: run
block: Run 3 · 15
visible:
Interview · Plan · Execute · Test / Debug · Iterate
Current: Execute
Build mode. Send:
```text
Approved. Build the app from docs/plan.md: backend on port 8000, page on port 5173, with GET /api/quote/{ticker} and GET /api/history/{ticker}?period=1y. Then tell me how to open it.
```
It asks to run a command? Read it. Installing or starting the app inside financial-app is expected. Anything else? Raise your hand.
Current: Test / Debug
NISP.JK · prices in IDR · date and source shown · 1-year chart
Current: Iterate
Date/source missing? Send:
```text
Show the date and source of the price under the price card.
```
Repeat the check.
15 min · Stuck? s1-dashboard.
diagram: Workflow mini-map (.wf) stays above three replacement panels; current step changes from Execute to Test / Debug to Iterate. No unattended motion.
build:
  0: mini-map, Current: Execute, build prompt and command-permission line
  1: Current: Test / Debug and checklist replace execute panel
  2: Current: Iterate, missing-date/source prompt, repeat check, time and stuck line replace test panel
notes:
On step 0, confirm Build mode and the approved docs/plan.md before sending the prompt. Read any requested command: installing or starting within financial-app is expected, but unfamiliar actions need my help. On step 1, open the dashboard and point at each check: NISP.JK, rupiah, date and source, one-year chart. Compare daily change with the previous close, not just a plausible colour. This fulfils the date-and-source check promised at the start. On step 2, use the Iterate prompt if either is missing, then check again. If both are already present, review whether they are readable and correct; do not invent a change. Building is untested and needs Python and Node ready. Help anyone blocked reach checkpoint s1-dashboard.
words: 38 · budget: 60 · exception: none
status: UNTESTED (build and Iterate prompts)

## 29. Run 3b: protect the key, then interview and plan the chatbot
type: run
block: Run 3 · 12
visible:
Interview · Plan · Execute · Test / Debug · Iterate
Current: Interview
Protect the key:
```text
Add .env to .gitignore and create backend/.env.example with LLM_BASE_URL, LLM_API_KEY and LLM_MODEL and no values. Don't create or open backend/.env.
```
Copy backend/.env.example to backend/.env and fill in the class details. Never paste the key into the chat.
Spec:
```text
Add a chatbot to docs/spec.md. The page sends the whole message list each turn. The backend adds NISP's latest available price and the last year of daily closes, with dates, then calls the AI service using the settings in backend/.env (LLM_BASE_URL, LLM_API_KEY, LLM_MODEL). If the data doesn't answer the question, it says so. No buy, sell or hold advice. No tool calling. Don't build yet.
```
Current: Plan
Plan → approve, edit or reject → save, as in Run 2.
12 min · Stuck? s1-dashboard.
diagram: Workflow mini-map (.wf) above replacement panels: protection, interview/spec, plan/save. Current Interview changes to Plan. Only the five approved names are mini-map labels.
build:
  0: mini-map, Current: Interview, protection prompt and manual-copy step
  1: spec prompt replaces protection panel; Current: Interview remains
  2: Current: Plan, plan/review/save step, time and stuck line replace spec panel
notes:
On step 0, run the protection prompt before entering a key. Open .gitignore and confirm .env is excluded; check backend/.env.example has names but no values. Participants copy and fill backend/.env themselves with class details, never in chat. If anyone is unsure, raise a hand without displaying the key. On step 1, interview briefly about the chatbot's business purpose, then send the spec prompt and read the update. It supplies dated price history and requires an honest no-data answer, not investment advice. Keep the dashboard date and source visible for later comparison. On step 2, use the same tested plan and save prompts from slide 25 in this conversation, approving, editing or rejecting before saving. These new setup and spec prompts need rehearsal. Help blocked participants from checkpoint s1-dashboard.
words: 33 · budget: 60 · exception: none
status: UNTESTED (protection and spec prompts); tested plan/save text reused from slide 25

## 30. Run 3c: build and test the chatbot, then push without secrets
type: run
block: Run 3 · 14
visible:
Interview · Plan · Execute · Test / Debug · Iterate
Current: Execute
Build:
```text
Approved. Build the chatbot from docs/plan.md, then tell me how to open it.
```
Current: Test / Debug
What is NISP's latest price? → matches the price card and its date.
Which stock are we talking about? → NISP (memory).
What was the close on <a date last month>? → matches the chart, or says it has no data.
Should I buy NISP? → no buy, sell or hold advice.
Current: Iterate
Fix failures; repeat checks.
Push:
```text
List the files you will commit. If backend/.env is in the list, stop and tell me. Otherwise commit with the message "NISP dashboard and chatbot" and push to GitHub.
```
Key leaked? Tell the facilitator — the key must be replaced.
14 min · Stuck? s1-chatbot.
diagram: Workflow mini-map (.wf) stays above replacement panels: build; first two tests; last two tests; iterate/push. Current step named on each. The visible angle-bracket date is the spec's existing test template, not a new placeholder.
build:
  0: mini-map, Current: Execute and build prompt
  1: Current: Test / Debug and first two tests replace build panel
  2: last two tests replace first two; Current: Test / Debug remains
  3: Current: Iterate, fix/recheck line, push prompt, key warning, time and stuck line replace tests
notes:
On step 0, send the build prompt only after the chatbot plan is saved. On step 1, ask the first two questions in your financial app, in the same chat: price and date must match the card, then the stock must remain NISP. Point at the dashboard date and source. On step 2, replace the date template with a real date last month; compare with the chart or accept an honest no-data answer. The advice question must not produce buy, sell or hold advice. On step 3, fix failures and repeat checks before pushing. Read the listed files; backend/.env must be absent. If a key leaked, stop and tell me so it is replaced. Help anyone behind reach checkpoint s1-chatbot.
words: 45 · budget: 60 · exception: none
status: UNTESTED (build and push prompts)

## 31. You built a financial app by directing an AI and checking its work
type: recap
block: Close · 4
visible:
The model doesn't remember; opencode sends the context
AGENTS.md: the project's standing brief
Commit and push save your work to GitHub
Interview · Plan · Execute · Test / Debug · Iterate
Dashboard opens · price check passes · chatbot check passes · latest commit on GitHub — or checkpoint s1-chatbot
diagram: Recap panel replaces with finish-check panel; workflow chips appear only on recap panel.
build:
  0: title only
  1: three recap statements and five-step chips
  2: finish check replaces recap panel
notes:
On step 1, point quickly at each statement and connect it to what people did. opencode sends context; AGENTS.md keeps the project's standing brief; commit and push copy included work to GitHub. Ignored secrets are not part of that copy. Trace the five workflow chips: Interview, Plan, Execute, Test / Debug, Iterate. The business user's work was deciding and checking, not typing code. On step 2, do the finish check rather than declaring everybody finished. Ask participants to open the dashboard, confirm a price check and a chatbot check, and find the latest commit on GitHub. If someone is behind, help them use checkpoint s1-chatbot for Session 2. The recovery link still needs preparation before class.
words: 32 · budget: 40 · exception: none
status: n/a

## 32. Questions
type: Q&A
block: Close · 5
visible:
Questions?
diagram: Large question heading and five drifting shapes: three speech bubbles, one question mark and a dot. No text within shapes. Slow continuous movement is permitted here; reduced-motion freezes all shapes.
build:
  0: question and shapes together
notes:
Open the floor on step 0. Point at the question and invite one thing that surprised people, or one place they might use a dashboard at work. If nobody speaks, ask which part needed the most judgement: the interview, plan review or tests. Repeat each question before answering so the whole room hears it. Keep investment questions neutral: your financial app shows data, not investment advice. Park anything needing a long demonstration for the next session instead of rushing through it. If someone is stuck rather than asking a general question, arrange individual help and confirm they have the s1-chatbot checkpoint before leaving. Check that nobody is displaying a secret while sharing their screen.
words: 1 · budget: 40 · exception: none
status: n/a

## 33. Next session: your app stores price history and the chatbot reads reference pages
type: talk
block: Close · 1
visible:
Session 2:
Store price history
Watchlist: NISP, BBRI, TLKM
Reference pages for the chatbot
diagram: Three short preview lines, no implied model retraining.
build:
  0: all lines together
notes:
Point at the three preview lines on step 0. Today your financial app fetches prices when asked and stores none; next time we save price history and give the chatbot reference pages to read. The model itself is not retrained. The watchlist extends the same pattern to NISP, BBRI and TLKM, rather than changing how you direct opencode. Keep the distinction clear: stored data belongs to your financial app, while reference pages supply information for an answer. If someone has not finished today, remind them to keep their project and ask for help with checkpoint s1-chatbot before Session 2. Close by thanking the group; do not introduce a new exercise in this final minute.
words: 14 · budget: 40 · exception: none
status: n/a



## Word count check

| id | type | words | budget | over? | notes words |
|---|---|---|---|---|---|
| 1 | title | 11 | 40 | no | 111 |
| 2 | visual | 16 | 40 | no | 150 |
| 3 | visual | 18 | 40 | no | 151 |
| 4 | visual | 25 | 40 | no | 153 |
| 5 | visual | 34 | 40 | no | 157 |
| 6 | visual | 39 | 40 | no | 158 |
| 7 | visual | 35 | 40 | no | 156 |
| 8 | visual | 39 | 40 | no | 157 |
| 9 | visual | 24 | 40 | no | 147 |
| 10 | visual | 36 | 40 | no | 137 |
| 11 | check | 52 | 60 | no | 148 |
| 12 | visual | 30 | 40 | no | 138 |
| 13 | visual | 28 | 40 | no | 143 |
| 14 | visual | 17 | 40 | no | 144 |
| 15 | visual | 35 | 40 | no | 154 |
| 16 | run | 22 | 60 | no | 117 |
| 17 | run | 34 | 60 | no | 120 |
| 18 | visual | 23 | 40 | no | 113 |
| 19 | visual | 32 | 40 | no | 117 |
| 20 | visual | 31 | 40 | no | 117 |
| 21 | visual | 23 | 40 | no | 115 |
| 22 | visual | 31 | 40 | no | 113 |
| 23 | check | 55 | 60 | no | 121 |
| 24 | run | 36 | 60 | no | 116 |
| 25 | run | 44 | 60 | no | 119 |
| 26 | visual | 29 | 40 | no | 116 |
| 27 | visual | 27 | 40 | no | 124 |
| 28 | run | 38 | 60 | no | 116 |
| 29 | run | 33 | 60 | no | 128 |
| 30 | run | 45 | 60 | no | 120 |
| 31 | recap | 32 | 40 | no | 116 |
| 32 | Q&A | 1 | 40 | no | 114 |
| 33 | talk | 14 | 40 | no | 114 |

slides: 33 · minutes: 180 · run minutes: 91
