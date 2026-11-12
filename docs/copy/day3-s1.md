# Day 3 · Session 1 — slide copy and speaker notes

Course: AI Vibe Coding for Business Users · Session 1: Build your first AI Financial App · 3 hours · English deck, speaker-led and hands-on.
Sources: `docs/outlines/day3-outline.md` (55 approved titles, kept word for word), `prompts/s1.md` (tested prompts), `docs/superpowers/specs/2026-11-11-day3-design.md` §3, §7, §8, §9.

How to read this file:
- `visible:` is the text on the slide. The `diagram:` line describes shapes, positions and arrows, and may add short labels in quotes. The word count includes those extra labels.
- Hands-on prompts marked `tested` are copied from `prompts/s1.md`. Marked `UNTESTED` means written for this deck and not yet run in opencode. Run it before class.
- Slides that contain no prompt have `status: n/a (no prompt)`.
- Word counts: the visible words include every quoted diagram label, counted once, plus the reveal line on check slides. Fenced prompts are excluded and shown separately.
- Untested prompts by slide: 8, 11, 22, 29, 35, 36 (presenter prompts in the notes), 48, 49 (four prompts), 51, 52. Slides 18, 41, 44 and 45 are quoted verbatim from `prompts/s1.md` (tested).
- `[SKILL NAME]` on slide 36 is the skill the facilitator uses in the demo.
- `[FAST MODEL]` and `[SMART MODEL]` on slide 22 are placeholders for the facilitator to fill in once the class model list is known.
- Everyone works inside one empty project folder named `financial-app` from slide 8 onward. Create it with them (or put it in the handout) before slide 8.

Time plan (matches spec §7, total 180 min):

| Block | Slides | Min |
|---|---|---|
| Opening | 1–4 | 10 |
| LLM basics | 5–19 | 35 |
| Model selection | 20–23 | 10 |
| Git | 24–30 | 30 |
| Break | 31 | 10 |
| Skills | 32–37 | 20 |
| Brainstorm → Spec → Plan → Execute | 38–49 | 45 |
| Test, debug, iterate | 50–52 | 10 |
| Close | 53–55 | 10 |

---

## 1. Build your first AI Financial App
type: title
block: Opening · 1 min
visible:
Day 3 · Session 1
AI Vibe Coding for Business Users
diagram: none
notes:
Welcome everyone. Today you build a real app, and nobody writes code by hand. You tell an AI coding agent called opencode what you want, you check what it gives you, and you steer it. By the end of these three hours you will have a BBCA dashboard and a chatbot, saved on GitHub. Before we start, check that opencode opens on every laptop, Windows and Mac, and that it answers a simple "hello". Anyone whose model does not reply, raise your hand now, so we fix it before the first exercise.
words: 10 · budget: 40 · exception: none
status: n/a (no prompt)

## 2. Today you build a BBCA dashboard and chatbot without writing code
type: talk
block: Opening · 2 min
visible:
- A dashboard: BBCA price, daily change, 1-year chart
- A chatbot that answers questions about BBCA
- Your project, saved on GitHub

You direct. The AI writes the code.
diagram: none
notes:
Say what the day produces, in business words. BBCA is Bank Central Asia, a stock many of you know. The dashboard shows its latest price in rupiah, how much it moved today, and a one-year chart. The chatbot answers questions about that data. Then ask: how many of you have written code before? Few hands is fine. Make the point that your job is the same as a manager's: be clear about the goal, then judge the work. The agent does the typing. Mention that we show market data only. Nothing in the app tells anyone what to buy or sell.
words: 27 · budget: 40 · exception: none
status: n/a (no prompt)

## 3. This is the app you will have by the end of this session
type: demo
block: Opening · 5 min
visible:
Finished app
BBCA price · daily change · 1-year chart · chat panel
diagram: none
notes:
You show the finished app. Have both servers running before class.
1. Open the page from checkpoint s1-chatbot in the browser (localhost:5173).
2. Point at the latest price in rupiah, the daily change, and the one-year chart.
3. In the chat panel type: "What is BBCA's latest price?"
4. Then type: "And a month ago?" The answer should still make sense.
5. Say: none of this was written by hand. You will build it in the next hours.
If Yahoo is slow, the checkpoint ships cached data, so the page still loads. Only try "Should I buy BBCA?" if you rehearsed it.
words: 10 · budget: 40 · exception: none
status: n/a (no prompt)

## 4. You will be at the keyboard for most of these three hours
type: talk
block: Opening · 2 min
visible:
1. LLM basics
2. Fast vs smart models
3. Git and GitHub
4. Skills
5. Build the dashboard, then the chatbot
6. Test, fix, push
diagram: none
notes:
Walk through the agenda quickly. Explain the rhythm: I explain for a few minutes, then you do it, then we check together. Elapsed times for orientation: LLM basics starts at 0:10, models at 0:45, Git at 0:55, break at 1:25 for ten minutes, skills at 1:35, the build at 1:55, test and push at 2:40, Q&A at 2:50. If you fall behind, do not stop. Raise your hand, and I will send you to a checkpoint, which is a saved version of the project you can switch to.
words: 25 · budget: 40 · exception: none
status: n/a (no prompt)

## 5. An LLM predicts the next words from the text you send it
type: talk
block: LLM basics · 2 min
visible:
Text in: "BBCA is the ticker of Bank Central ..."
Text out: "Asia"

Large language model = LLM
diagram: none
notes:
Start with what an LLM is: a very large text predictor. You send text, it predicts the most likely next words, one piece at a time. That is all it does. It can sound like an expert because it learned patterns from a huge amount of text. It can also be confidently wrong, because it predicts what sounds right, not what it has checked. This matters later: when the app needs real BBCA numbers, we have to hand them to the model. Ask the room: have you used ChatGPT or Copilot? Those are apps built on language models; the app is the screen you type into, and the model sits behind it.
words: 16 · budget: 40 · exception: none
status: n/a (no prompt)

## 6. The model is stateless: it remembers nothing between requests
type: talk
block: LLM basics · 2 min
visible:
Request 1: "My name is Sari."
Reply: "Nice to meet you, Sari."

Request 2, sent alone: "What is my name?"
Reply: "I don't know."
diagram: none
notes:
"Stateless" means each request starts from zero. The model does not keep a file about you. When you ask the second question, the model has no idea there was a first one, unless that first message is sent again. Most people expect software to remember, so this feels odd. Ask: if the model remembers nothing, why does ChatGPT seem to remember our chat? Let them guess for a moment, then move on. The next slide answers it. Keep the tone light; this is the most important idea in the first block.
words: 24 · budget: 40 · exception: none
status: n/a (no prompt)

## 7. The app resends the whole conversation every turn, which looks like memory
type: talk, diagram
block: LLM basics · 3 min
visible:
Turn 1 sends: Question 1
Turn 2 sends: Question 1 + Answer 1 + Question 2
Turn 3 sends: everything so far + Question 3
The app does this. The model doesn't remember.
diagram: Three horizontal rows, one per turn, each a row of small rounded boxes. Row "Turn 1 sends": one box "Question 1". Row "Turn 2 sends": three boxes "Question 1", "Answer 1", "Question 2". Row "Turn 3 sends": a longer box "everything so far" followed by a box "Question 3". Each row has an arrow on the right pointing to a box labelled "Model". Rows grow longer from top to bottom. Caption under the rows is the last line of visible.
notes:
This is the answer to the previous question. The chat app keeps the whole conversation, and every turn it sends all of it again, plus your new message. Point at the rows getting longer. The model reads everything from the top each time, so it looks like it remembers. Two consequences: long chats cost more and run slower, and anything that is not in what gets sent does not exist for the model. We will build exactly this into our chatbot later: the page sends the whole message list every turn. Keep the phrase "the app resends it" in their heads.
words: 30 · budget: 40 · exception: none
status: n/a (no prompt)

## 8. Start a new opencode session and ask what you told it before
type: hands-on
block: LLM basics · 3 min
visible:
**Goal:** See that a new session remembers nothing.

**Prompt 1:**
```text
My favourite stock is BBCA and I work in the sales team. Just say OK. Don't create or edit any files.
```
**Then type** `/new`

**Prompt 2:**
```text
Which stock is my favourite, and which team do I work in?
```
**You should see:** The agent doesn't know.
**Time:** 3 min
**Stuck?** Raise your hand.
diagram: none
notes:
First exercise, and it should be quick. Everyone opens opencode inside the empty financial-app folder. Check this before you start: some people will be in the wrong folder. Send prompt one, wait for the reply, then type /new, which starts a new session. Send prompt two. The agent should say it does not know. Ask a few people what they saw. Then connect it to slide 6: the second session never received the first message, so the model could not use it. If someone's agent does answer correctly, ask them whether they typed prompt two in the same session. This prompt is untested, so rehearse it first.
words: 29 · budget: 60 · exception: fenced prompt not counted (33 words)
status: UNTESTED

## 9. The context window is the most text the model can read at once
type: talk
block: LLM basics · 2 min
visible:
Context window = everything the model reads for one reply

It holds:
- rules
- your messages
- its replies
- tool results
- files it opened
diagram: none
notes:
Every request has a limit on how much text the model can take in. That limit is the context window. Think of a desk: only what fits on the desk can be read. Everything counts toward it, not just your questions. The rules, the whole conversation so far, the answers, and any file the agent opened are all on the desk. I won't quote numbers because they differ per model and change often. In opencode there is a counter that shows how much you have used. We will watch it in a moment. Ask: what do you think fills it fastest, your questions or the files the agent reads?
words: 21 · budget: 40 · exception: none
status: n/a (no prompt)

## 10. When the context fills up, old details get dropped or summarised
type: talk
block: LLM basics · 2 min
visible:
Window full → oldest details are dropped or summarised.

Early instructions can quietly disappear.

Fix: start a /new session. Keep rules in AGENTS.md.
diagram: none
notes:
When the desk is full, something has to go. Either the oldest material is cut off, or it is replaced by a short summary. Both lose detail. The risk for you: an instruction you gave an hour ago, like "always show prices in rupiah", may be gone without any warning. The agent does not tell you it forgot. Two habits help. Start a new session when a task is finished, instead of one endless chat. And put rules that must always apply into a file, which is the AGENTS.md we use in a few minutes. Ask: when would you start a new session?
words: 22 · budget: 40 · exception: none
status: n/a (no prompt)

## 11. Watch the context counter in opencode grow as you chat
type: hands-on
block: LLM basics · 3 min
visible:
**Goal:** See the context counter rise.

**Prompt:**
```text
Explain in plain words what a stock's daily change and a 1-year price chart show. Use about 300 words. Don't create any files.
```
Then ask two follow-up questions of your own.

**You should see:** The counter rises after every reply.
**Time:** 3 min
**Stuck?** Raise your hand.
diagram: none
notes:
Tell them to look at the counter in opencode before they send anything, and note the number. Where it appears depends on the version and window size, so walk the room and point at it on a screen. Send the prompt. The counter jumps because the reply is long, and the whole conversation gets resent next turn. Ask follow-ups and watch it climb. Say it out loud: the number goes up with their words and the model's words. Do not state any limit; ask them to find, in the same place, whether opencode shows how full it is. Untested prompt, so rehearse it first.
words: 31 · budget: 60 · exception: fenced prompt not counted (23 words)
status: UNTESTED

## 12. Every request is a list of messages: system, user, assistant, tool
type: talk
block: LLM basics · 2 min
visible:
system: "You are a careful banking assistant."
user: "What is BBCA?"
assistant: "Bank Central Asia, a listed Indonesian bank."
tool: (result of a tool the app ran)

One list. Sent every turn.
diagram: A vertical stack of four message boxes, each with a coloured label chip on the left: "system", "user", "assistant", "tool". The text next to each chip is the quoted example from visible. Use a different chip colour per role. Caption "One list. Sent every turn." below the stack.
notes:
Now look inside what gets sent. It is not one blob of text but a list of messages, and each message has a role. There are four roles. We will name them one by one on the next slide. For now notice that the list is ordered, and the whole list goes to the model every turn, which links back to the slides on statelessness. When you later read about "prompts" or "context", this list is what they mean. You do not need to write these lists yourself; opencode and our app build them. But knowing they exist explains why the agent behaves the way it does.
words: 32 · budget: 40 · exception: none
status: n/a (no prompt)

## 13. System sets the rules, user asks, assistant answers, tool reports results
type: talk
block: LLM basics · 2 min
visible:
system — sets the rules
user — you ask
assistant — the model answers
tool — reports what a tool did
diagram: none
notes:
Take the four roles in turn. System: the rules and the role, written by whoever builds the app. In our chatbot, you will see this one again in Session 2, when you write your own. User: that is you. Assistant: the model's replies. Tool: the result of something the app ran on the model's behalf, like reading a file. Quick check: ask the room which role the AGENTS.md rules belong to, system or user. Most will guess system; that is close enough, since the agent loads it as standing instructions before your first message.
words: 17 · budget: 40 · exception: none
status: n/a (no prompt)

## 14. With tool calling, the model asks for a tool and the app runs it
type: talk, diagram
block: LLM basics · 2 min
visible:
1. App sends the messages to the model
2. Model replies: "run read_file on docs/spec.md"
3. App runs the tool
4. App adds a tool message and asks again
5. Model answers using the result
diagram: Three boxes left to right: "App" (centre), "Model" (top right), "Tool" (bottom right). Numbered arrows: 1 App → Model labelled "messages"; 2 Model → App labelled "run read_file on docs/spec.md"; 3 App → Tool; 4 Tool → App labelled "tool message", then App → Model again; 5 Model → App labelled "answer".
notes:
So how does an agent read files or run commands? Tool calling. The app, here opencode, tells the model which tools exist. The model asks for a tool: "please run this tool with these inputs". Then opencode runs it, then adds the result as a tool message and sends everything back. The model continues. Stress this: the model asks, opencode runs. The model never touches your computer itself, and opencode can ask you for permission first. This is also why a mistaken model is less scary than it sounds: you stay in the loop. Our chatbot will not use tools yet.
words: 35 · budget: 40 · exception: none
status: n/a (no prompt)

## 15. A coding agent is an LLM calling tools in a loop until the task is done
type: talk
block: LLM basics · 2 min
visible:
Goal → Model decides → Runs a tool → Reads the result → Decides again…

Stops when the task is done.
diagram: A circular loop of three boxes with arrows clockwise: "Model decides", "Runs a tool", "Reads the result", back to "Model decides". An arrow enters the loop from the left labelled "Goal". An arrow leaves the loop to the right labelled "Task done".
notes:
Put the last two slides together. An agent is the loop you see here. You give a goal. The model decides what to do next, usually a tool. The app runs it. The model reads the result and decides again. It repeats until it thinks the task is done. That is why one request can take a minute and touch many files. It is also why the first sentence of your request matters so much: every step in the loop builds on the goal you gave. If the goal is vague, the loop wanders. Next slide: what that means for your role.
words: 19 · budget: 40 · exception: none
status: n/a (no prompt)

## 16. You bring the goal and the judgement; the agent does the typing
type: talk
block: LLM basics · 1 min
visible:
You: the goal, the choices, the approval
Agent: the typing, the files, the commands

The agent can be wrong. You check.
diagram: none
notes:
This is the role split for the whole course. You bring the goal in business terms, you decide between options, and you approve or reject. The agent writes the files and runs the commands. Because the model predicts rather than verifies, it will sometimes be wrong with great confidence. So your judgement is not a formality. Ask yourself on every result: is this what I wanted, and how would I know? You do not need to read code for that. You can open the page, try the feature, and compare against what you asked. We practise that all day.
words: 21 · budget: 40 · exception: none
status: n/a (no prompt)

## 17. AGENTS.md is a note the agent reads at the start of every session
type: talk
block: LLM basics · 2 min
visible:
AGENTS.md: a plain text file in your project.
The agent reads it at the start of every session.

Example rule: "Explain what you will do in plain business language before doing it."
diagram: none
notes:
Since the model forgets between sessions, we need a place to keep standing instructions. That place is AGENTS.md, a plain text file in the project folder. opencode reads it at the start of every session and puts it in front of the model. Typical contents: what the project is, how to run it, and rules like the one on the slide. The rule on screen is the one you will add in a moment. It makes the agent say what it plans to do before it does it, which is very useful when you cannot read the code. Anything permanent goes here, not in a chat.
words: 32 · budget: 40 · exception: none
status: n/a (no prompt)

## 18. Run /init to create AGENTS.md, then add one rule of your own
type: hands-on
block: LLM basics · 5 min
visible:
**Goal:** Create AGENTS.md with one rule of your own.

**Prompt 1:** type `/init` and press Enter.
A permission box appears? Choose **Allow once** (Enter).

**Prompt 2:**
```text
Add one rule to AGENTS.md: Explain what you will do in plain business language before doing it.
```
**You should see:** An AGENTS.md file that contains your rule.
**Time:** 5 min
**Stuck?** No reply after 2 minutes? Stop it and send the same prompt again.
diagram: none
notes:
Everyone types /init in the empty financial-app folder. It took 43 to 55 seconds in our tests, and the file is short, because the folder is empty. Sometimes a box appears: "Permission required, access external directory". The agent occasionally looks at a path outside the project folder, and opencode asks first. Tell them to choose Allow once; it is highlighted, so Enter is enough. Rejecting can leave you with no file, and then you send /init again. Then send prompt two. Wording around the rule differs between people, and that is fine. Open AGENTS.md together and check the rule. If nothing moves for two minutes, stop the agent and resend the same prompt. Do not commit yet.
words: 53 · budget: 60 · exception: fenced prompt not counted (17 words)
status: tested
## 19. The agent forgot your preference overnight. Why, and how do you fix it?
type: check
block: LLM basics · 2 min
visible:
A. The agent was tired. Remind it every morning.
B. A new session starts empty. Put the preference in AGENTS.md.
C. The model was updated. Wait for the next version.
reveal: B — Nothing carries over between sessions except files, and AGENTS.md is read every time.
diagram: none
notes:
Read the question aloud. Give them thirty seconds to think, then ask for a show of hands for A, B and C. Take one vote at a time. Choice A makes people laugh; ask why a model cannot be tired. Click to reveal the answer. B is right because the session starts empty and only files carry knowledge forward. If someone argues for C, say updates are possible but not the usual cause. Then ask one person to say, in their own words, what rule they would add for their own work. This closes the LLM basics block and sets up model selection.
words: 44 · budget: 60 · exception: none
status: n/a (no prompt)

## 20. Fast models answer in seconds; smart models reason before they act
type: talk
block: Model selection · 2 min
visible:
Fast model: quick answers, good for small jobs
Smart model: slower, thinks first, good for hard jobs

In opencode: type /models to pick one.
diagram: none
notes:
Models come in different sizes. A fast model replies in a few seconds and is fine for small, clear jobs. A smart model spends longer working things out before it acts, which helps when the task is unclear or the answer needs several steps. Show the picker: type /models in opencode and let them see the list on their own laptops. Names differ between people depending on which provider they use, so do not say "everybody pick X". Say "pick one fast and one smart from your list". Ask the room to find the two they will use in the next exercise. Do not talk about prices; ask them to look at the model list for hints.
words: 24 · budget: 40 · exception: none
status: n/a (no prompt)

## 21. Use fast models for small edits and smart models for planning and debugging
type: talk
block: Model selection · 2 min
visible:
Fast: rename a title, fix a typo, change a colour
Smart: write the plan, find why something breaks

Wrong choice costs time, or quality.
diagram: none
notes:
Give the rule of thumb. Fast models for small edits where you can see the result straight away. Smart models for planning, when a bad plan wastes the whole build, and for debugging, when the cause is not obvious. Use a restaurant picture: a fast model is the quick cook who makes the toast; a smart model is the chef you ask for the new menu. A wrong choice shows up in two ways: a fast model on a hard job gives a shallow answer, a smart model on a trivial job makes you wait. Today the plan step in our build is where we use the smart model. Then you do the next exercise.
words: 24 · budget: 40 · exception: none
status: n/a (no prompt)

## 22. Give the same task to a fast and a smart model and compare
type: hands-on
block: Model selection · 4 min
visible:
**Goal:** Feel the difference between a fast and a smart model.

**Steps:** `/models` → [FAST MODEL] → send the prompt. Then `/new`, `/models` → [SMART MODEL] → send it again.

**Prompt:**
```text
Give three risks of holding only one bank stock, such as BBCA. Explain each in one sentence. Don't create any files.
```
**You should see:** Two answers. Compare speed and depth.
**Time:** 4 min
**Stuck?** Raise your hand.
diagram: none
notes:
Before class, replace [FAST MODEL] and [SMART MODEL] on this slide with real names from the model list your participants share. Walk them through the steps: choose the fast model with /models, send the prompt, note how long it took. Type /new so the second try starts clean. Pick the smart model, send the same prompt. Ask three people to compare: which was faster, which gave better reasons, and did it matter for this task? Likely answer: both are fine for a small question, and the difference shows on harder work. This prompt is untested, so rehearse it with both models first. Remind them the answers are general information, not investment advice.
words: 43 · budget: 60 · exception: fenced prompt not counted (21 words)
status: UNTESTED

## 23. Which model would you pick for each of these three tasks?
type: check
block: Model selection · 2 min
visible:
Tasks: (1) fix a typo in a page title (2) plan the whole dashboard (3) find out why the chart is empty

A. 1 fast · 2 smart · 3 smart
B. 1 smart · 2 fast · 3 fast
C. Fast for all three, to save time
reveal: A — Small edits need speed. Planning and debugging need careful thinking.
diagram: none
notes:
Read the three tasks. Let people think for twenty seconds, then vote by raising hands for A, B or C. Choice C is tempting because fast feels efficient. Ask someone who voted C what happens if the plan is shallow: the whole build rests on it. Click to reveal A. Add the nuance that it is a rule of thumb, not a law: if a fast model keeps failing at a task, switch to a smart one before trying a tenth time. Switching models mid-session is allowed with /models. Then move on to Git, which keeps our work safe whatever model we use.
words: 55 · budget: 60 · exception: none
status: n/a (no prompt)

## 24. Without version control, nobody knows which file is the real one
type: talk
block: Git · 3 min
visible:
Budget_final.xlsx
Budget_final_v2.xlsx
Budget_final_v2_REALLY.xlsx
Budget_final_v2_Tom-edits.xlsx

Which one is latest? Who changed what?
diagram: A stack of four file cards, each a rounded rectangle with a small spreadsheet icon and one of the file names from visible. Slight offsets so they look piled up. A red question mark badge on the top card.
notes:
Ask: who has a folder that looks like this? Hands up. This is the problem version control solves. With copies like these, nobody knows which file is the real one, who changed what, or what was lost. Git is a tool that keeps one project, every version of it remembered, and one shared copy for the team. GitHub is a website that hosts that shared copy. Why this matters for an AI agent: the agent changes many files quickly, and you need a way to go back and a place where the work is safe. That is why we do Git before building anything big.
words: 11 · budget: 40 · exception: none
status: n/a (no prompt)

## 25. Everyone works on a local copy and shares through one remote
type: talk
block: Git · 4 min
visible:
Your computer: local copy. Only you see it.
GitHub: remote copy. The team shares it.

Nothing travels between them until you push or pull.
diagram: Two large boxes side by side. Left box "Your computer" with subtitle "Local copy", styled like a desk. Right box "GitHub" with subtitle "Remote copy", styled like a shared filing cabinet. Between them a double-headed arrow labelled "push / pull". Caption below the boxes is the last line of visible.
notes:
Explain with the desk and the filing cabinet from the Git demo. The local copy is your own desk: only you see it. The remote copy is the team's filing cabinet, which is GitHub: everyone can reach it. The key sentence is on the slide: nothing moves between the two until you decide to push or pull. Many beginners think saving a file shares it. It does not. Ask one person to explain in their own words where their opencode project is stored right now. Answer: only on their laptop. After the GitHub exercise there will be a second copy.
words: 26 · budget: 40 · exception: none
status: n/a (no prompt)

## 26. A commit is a save point with a note, and it stays on your computer
type: talk
block: Git · 3 min
visible:
Commit 1: Created the budget file
Commit 2: Added March figures
Commit 3: Fixed the totals

Saved on YOUR computer only, until you push.
diagram: Three rounded boxes in a row joined by right-pointing arrows, labelled "Commit 1", "Commit 2", "Commit 3", each with its note underneath as in visible. A laptop icon behind the row. The last line of visible is the caption underneath.
notes:
A commit is a save point. Not just the file, but the whole project at that moment, with a short note about what changed. Think of a game save with a name. You can go back to any commit. Commits live on your own computer. Nobody else can see them yet. With opencode you do not type Git commands. You ask the agent in plain English: "commit my project with this message". Show the idea that the note matters: next month, "Fixed the totals" tells you what happened; "stuff" tells you nothing. Ask the agent for a clear message. We do this on slide 29.
words: 24 · budget: 40 · exception: none
status: n/a (no prompt)

## 27. Push sends your commits to GitHub; pull brings your teammates' commits back
type: talk
block: Git · 4 min
visible:
Push: your computer → GitHub
Pull: GitHub → your computer

Routine: pull → edit → commit → push
diagram: Two panels stacked. Top panel: left box "Your computer" holding "Commit 1", "Commit 2", "Commit 3"; arrow pointing right labelled "push"; right box "GitHub" holding "Commit 1", "Commit 2" and "Commit 3" appearing in a highlight colour. Bottom panel: right box "GitHub" holding "Commit 1", "Commit 2" and "Commit 3 (Tom)" highlighted; arrow pointing left labelled "pull"; left box "Your computer" holding "Commit 1", "Commit 2". Below both, the routine line from visible as four boxes with arrows between them.
notes:
Push sends your commits up to GitHub. After that your teammates can see them. Pull is the reverse: it brings their commits down to your computer. Nothing arrives by itself, so pull before you start working. Today you work alone, so you will mostly push. The daily routine is pull, edit, commit, push. Ask the room which order breaks things if you swap it: if you edit first and pull later, your changes may clash with a teammate's. We do not go further in this course. The agent will do the Git commands for you.
words: 36 · budget: 40 · exception: none
status: n/a (no prompt)

## 28. Create your GitHub account
type: hands-on
block: Git · 7 min
visible:
**Goal:** Have a GitHub account you can sign in to.

**Steps:**
1. Open github.com and choose Sign up.
2. Enter your email, a password and a username.
3. Open the email from GitHub and confirm it.

**You should see:** Your GitHub home page, signed in.
**Time:** 7 min
**Stuck?** Raise your hand. Already have an account? Skip ahead.
diagram: none
notes:
Signup can be slow because GitHub sends a confirmation email. Start it now, and tell people to check their spam folder if the email is late. Anyone who already has an account can sign in to make sure the password still works. Suggest using a personal or work email they can open right now. Choose a username they will not mind showing: it appears in the web address of their projects. While people wait for the email, walk the room. If anyone is blocked, note their name and let them continue after the break. We need everyone signed in before the next slide. Facilitator guide has the fallback if GitHub signup fails for the whole room.
words: 58 · budget: 60 · exception: browser sign-up, no agent prompt
status: n/a (no prompt)

## 29. Ask opencode to commit your project and push it to GitHub
type: hands-on
block: Git · 7 min
visible:
**Goal:** Put your first commit on GitHub.

**Prompt:**
```text
Commit all files in this project with the message "Start project". Create a new GitHub repository called financial-app and push to it. Tell me if I need to sign in.
```
**You should see:** A financial-app repo on github.com with AGENTS.md.
**Time:** 7 min
**Stuck?** Raise your hand. Checkpoint `s1-start`.
diagram: none
notes:
This is the first push. The prompt asks for a commit with a clear message, a new repository, and the push. If the agent says you need to sign in to GitHub, follow its instructions on screen. Agree the sign-in method for Windows and Mac in the pre-session checklist. Confirm success the human way: open github.com, refresh, and look for the financial-app repository containing AGENTS.md. This prompt is untested and depends on how Git and GitHub sign-in are set up on the laptops, Windows and Mac, so rehearse it on both. Anyone stuck gets checkpoint s1-start. A repository can be private; say that people can decide.
words: 27 · budget: 60 · exception: fenced prompt not counted (30 words)
status: UNTESTED

## 30. Which copy survives if your laptop breaks?
type: check
block: Git · 2 min
visible:
You pushed three commits yesterday. Today your laptop falls in a river.

A. Your local copy
B. The copy on GitHub
C. None of them: the work is gone
reveal: B — GitHub still holds everything you pushed. Work you never pushed is lost.
diagram: none
notes:
Read the scenario with a straight face. Vote by hands. Choice A makes the room laugh; ask how a copy on a broken laptop can survive. Choice C is the fearful answer; this is exactly what Git protects against. Click to reveal B. Add the caveat from the reveal: GitHub only holds what you pushed. Anything committed but not pushed on the broken laptop is gone. So the habit is to push at the end of every work block, which we do again after the chatbot. Then announce the break: ten minutes. Anyone without a GitHub account should use it to finish signup.
words: 42 · budget: 60 · exception: none
status: n/a (no prompt)

## 31. Break, 10 minutes
type: break
block: Break · 10 min
visible:
Break
10:00
Back at: [TIME]
diagram: Large countdown timer, 10:00 counting down, centred.
notes:
Start the timer and write the return time on the board. Use the break to help anyone who is still stuck on GitHub signup or the first push. Check that every laptop still has opencode open in the financial-app folder. Check the LLM quota is fine. Suggest people stand up and stretch. When the timer reaches 1:00 remaining, call people back. Resume with the skills block. Do not start new content before most people are back, or you will have to repeat it. Keep the next block in mind: skills, then the big build, which is the heart of the day.
words: 5 · budget: 40 · exception: none
status: n/a (no prompt)

## 32. You can instruct the agent four ways: prompt, AGENTS.md, skill, workflow
type: talk
block: Skills (focus block) · 3 min
visible:
Prompt: one task, right now
AGENTS.md: rules for every session
Skill: expertise loaded when a task needs it
Workflow: many steps in order (Session 3)
diagram: Four boxes in a row, increasing in height from left to right, labelled "Prompt", "AGENTS.md", "Skill", "Workflow", each with its one-line description from visible under the label.
notes:
Welcome back. There are four ways to tell an agent what you want. A prompt is the message you type now. AGENTS.md is a standing note that applies to every session. A skill is a package of expertise that the agent loads only when a task needs it. A workflow strings many steps together; we build one in Session 3. Ask: you have already used two today. Which? Prompt and AGENTS.md. This slide is a map; the rest of this block is about skills, because they are the one most people have not met. Do not explain workflows yet.
words: 25 · budget: 40 · exception: none
status: n/a (no prompt)

## 33. A skill is packaged expertise the agent loads when a task needs it
type: talk
block: Skills (focus block) · 2 min
visible:
A skill = instructions for doing one kind of job well.

Examples: how to brainstorm, how to design a page, how to write a report.
diagram: none
notes:
A skill is a written playbook for one kind of job, packed so the agent can pick it up when needed. Think of a recipe card in a kitchen. The cook does not memorise every recipe, but picks the right card for the dish. Examples: a skill for brainstorming ideas before building, one for page design, one for writing a report. Skills differ by person because everyone has their own set. We do not provide a course skill kit. You will use whatever skills your opencode already has. If you have none, you still follow the course; today's prompts are built to work without any.
words: 24 · budget: 40 · exception: none
status: n/a (no prompt)

## 34. The agent sees only each skill's name and description until a task needs it
type: talk, diagram
block: Skills (focus block) · 3 min
visible:
Always loaded: each skill's name and description
Loaded on demand: the full instructions
diagram: Left side: a box "Agent's context" containing a short list of three rows, each row "name and description". Right side: a stack of three tall document boxes, greyed out, with no label. One arrow from the second row of the list to the second document, labelled "task matches: load it". The loaded document is highlighted and labelled "full instructions".
notes:
Connect this to the context window. If the agent loaded every skill in full at the start, the desk would fill up with text it does not need. So it sees only the name and a one-line description of each. When your request matches a description, it loads that one skill in full and follows it. One lesson: a skill is only found if its description is clear. Ask: where have you seen this idea before? AGENTS.md, which is always loaded, versus a skill, which is loaded on demand.
words: 19 · budget: 40 · exception: none
status: n/a (no prompt)

## 35. Ask opencode which skills you have, then open one and read it
type: hands-on
block: Skills (focus block) · 4 min
visible:
**Goal:** See your own skills and read one.

**Prompt:**
```text
List the skills you have, with each name and one-line description. Then show me the full text of one skill and explain in plain words what it does.
```
**You should see:** A list of skills, then one explained.
**Time:** 4 min
**Stuck?** No skills in your list? Read your neighbour's.
diagram: none
notes:
Participants have different setups, so their lists will differ. Some may have many skills; some may have none, which is fine. For those people, ask them to look over a neighbour's screen. Walk the room and note interesting skills to mention afterwards. Ask two people to read out the name of one skill they found. The prompt asks the agent to explain in plain words, so no one needs to read the raw file, though they may look at it. Point out that the file is just text with a name, a description and instructions. This prompt is untested and depends on the agent finding skills, so rehearse it on your own setup first.
words: 31 · budget: 60 · exception: fenced prompt not counted (28 words)
status: UNTESTED

## 36. The same request gives a different result with a skill than without
type: demo
block: Skills (focus block) · 5 min
visible:
Same folder, model and settings.
Run 1: the request alone
Run 2: the request + "Use the [SKILL NAME] skill"
diagram: none
notes:
Presenter demo using a skill on your own setup, for example a brainstorming or frontend-design skill. Rehearse it and keep screenshots as a backup.
1. Use one empty folder, one model and one config. Start a new session for each run (/new).
2. Run 1: "I want a simple page for my sales team to see BBCA before a client meeting. Don't create files."
3. Run 2: the same request, starting with "Use the [SKILL NAME] skill."
4. Show on screen that the skill was loaded before the agent answered.
5. Compare the structure, such as questions first versus a straight answer. Wording varies from run to run anyway, so don't compare sentences. Verify on your setup first.
words: 19 · budget: 40 · exception: none
status: UNTESTED

## 37. Would a skill help here, or is a plain prompt enough?
type: check
block: Skills (focus block) · 3 min
visible:
Which job benefits most from a skill?

A. Ask what "dividend" means
B. Every week, write a client memo in your firm's fixed format
C. Rename one button on the dashboard
reveal: B — A skill pays off for work you repeat in the same way. One-off questions need only a prompt.
diagram: none
notes:
Vote by hands. A and C are one-off jobs that a plain prompt handles in seconds, so writing a skill would be wasted effort. B is a repeating job with a fixed format, which is where packaged expertise earns its keep. Click to reveal B. Add a second point: a skill helps only if the agent can find it and its description matches the job, so name skills clearly. Ask if anyone has a repeated task at work that would make a good skill. Collect two examples. Say that Session 3 takes this further with workflows. Then move on to the big part: building the app, starting with asking questions first.
words: 50 · budget: 60 · exception: none
status: n/a (no prompt)

## 38. An agent builds what it guesses you want, so make it ask first
type: talk
block: Brainstorm → Spec → Plan → Execute · 2 min
visible:
"Build me a stock dashboard"
→ the agent guesses the data, the layout, the features.

Better: let it ask you first.
diagram: none
notes:
Show how a vague request goes wrong. If you say "build me a stock dashboard", the agent fills every gap with a guess: which stocks, which period, what it looks like. It will usually build something, quickly, and it may be far from what you meant. Then you spend your time undoing. The fix costs two minutes: let it ask you questions first. This is the same thing a good business analyst does with a stakeholder. For the rest of the session you will see this pattern again and again, and it is the most useful habit of the day. Ask who has received work back that missed the point.
words: 20 · budget: 40 · exception: none
status: n/a (no prompt)

## 39. Every build follows six steps: brainstorm, spec, plan, execute, test, iterate
type: talk
block: Brainstorm → Spec → Plan → Execute · 2 min
visible:
Brainstorm → Spec → Plan → Execute → Test → Iterate

Plan is where you approve, edit or reject.
diagram: Six rounded boxes in a row connected by right arrows: "Brainstorm", "Spec", "Plan", "Execute", "Test", "Iterate". An arrow curves from "Iterate" back to "Plan". Under "Plan" a small tag reading "Approve / Edit / Reject". Caption below is the last line of visible.
notes:
This is the method for the rest of Day 3. Brainstorm: the agent asks, you answer. Spec: a written description of what to build. Plan: step by step how. You approve, edit or reject the plan before anything is built. Execute: the agent builds. Test: you check the result in the browser. Iterate: you ask for changes. We use the same six steps for the dashboard now, the chatbot after, and the features of Sessions 2 and 3. Do not memorise them; they will be on the wall as a diagram. Notice that nothing gets built until step four.
words: 17 · budget: 40 · exception: none
status: n/a (no prompt)

## 40. In a brainstorm the agent asks one question at a time and you answer in business terms
type: talk
block: Brainstorm → Spec → Plan → Execute · 2 min
visible:
Agent: "Who will use this?"
You: "Our sales team, before client meetings."

One question. One short answer. No technical words.
diagram: none
notes:
Set up the exercise. In the brainstorm, the agent asks and you answer. One question at a time keeps the answers short and the thinking clear. Answer in business terms: who uses it, what decision it supports, how fresh the data needs to be. You do not need to name technology. If you do not know, say so: "I don't know, suggest one." Tip: answer exactly what the agent asked, in one sentence. Answers that do not match still work, but they leave gaps in the spec later. It will ask at most five questions in our prompt. We keep the technology out of the brainstorm and add it in the spec step.
words: 20 · budget: 40 · exception: none
status: n/a (no prompt)

## 41. Ask opencode to brainstorm the BBCA dashboard with you, one question at a time
type: hands-on
block: Brainstorm → Spec → Plan → Execute · 5 min
visible:
**Goal:** Let the agent ask you what the dashboard should do.

**Prompt:**
```text
Let's brainstorm a BBCA stock dashboard together. It should show the latest price, the daily change and a 1-year price chart. Ask me one question at a time, at most 5, in plain business language. Don't write any code or files yet.
```
**You should see:** One short question per reply. No files created.
**Time:** 5 min
**Stuck?** Raise your hand.
diagram: none
notes:
Everyone sends the prompt, exactly as written. In our tests the agent asked five short questions, about five seconds each, and then summarised what was agreed in three bullets. The first question was always the same: who will use this. Others vary, so let people answer what is actually asked. Sample answers: sales team preparing for client meetings; delayed price is fine if it shows the update time; mostly laptops; just the figures and the chart. Watch for anyone whose agent starts writing files; tell them to stop it and re-send. Do not worry if answers differ between neighbours. That variety is the point.
words: 30 · budget: 60 · exception: fenced prompt not counted (42 words)
status: tested

## 42. A spec says what to build and why; a plan says how, step by step
type: talk
block: Brainstorm → Spec → Plan → Execute · 2 min
visible:
Spec: what and why.
Plan: how, in numbered steps.

Spec in docs/spec.md. Plan in docs/plan.md.
diagram: none
notes:
Two documents, two jobs. The spec is the contract between you and the agent: what we are building and why, in your words. The plan is the agent's proposal for how to build it, in numbered steps. You write, or at least correct, the spec, because it holds your intent. You review the plan, because it shows how the agent wants to spend the next hour. Both are files in the project, so they survive when a session ends. That solves the memory problem from the start of the session: a new session can read the spec and carry on. Ask: if you changed your mind about a feature, which document would you change first?
words: 15 · budget: 40 · exception: none
status: n/a (no prompt)

## 43. A good spec lists goals, what's out of scope, and how you'll know it works
type: talk
block: Brainstorm → Spec → Plan → Execute · 2 min
visible:
Goals: show BBCA's price, daily change and 1-year chart
Out of scope: live prices, other stocks
How we'll know it works: the page loads with real BBCA numbers
diagram: none
notes:
A spec needs only three parts. Goals say what the app must do. Out of scope says what it must not do, which stops the agent adding extras. How we'll know it works describes what you will see when it is right. Without this third part you cannot judge the result. The examples on the slide are plausible answers from our BBCA brainstorm; your own spec will differ, because your brainstorm answers differ. Remind people that they are the ones who judge: after the agent writes the spec, they read it and correct anything that is not what they meant. That correction step is the exercise.
words: 28 · budget: 40 · exception: none
status: n/a (no prompt)

## 44. Ask the agent to write the spec to docs/spec.md, then read and correct it
type: hands-on
block: Brainstorm → Spec → Plan → Execute · 5 min
visible:
**Goal:** Get a written spec, then fix anything wrong.

**Prompt:**
```text
Write what we agreed to docs/spec.md. Use three sections: Goals, Out of scope, and How we'll know it works. Don't build anything yet. We'll use React + Vite, FastAPI (Python) and yfinance, with endpoints GET /api/quote/{ticker} and GET /api/history/{ticker}?period=1y, server on port 8000, page on port 5173.
```
**You should see:** docs/spec.md with three sections. No app yet.
**Time:** 5 min
**Stuck?** Checkpoint `s1-spec`.
diagram: none
notes:
Teach the sentence "Don't build anything yet". In our first test this sentence was missing, and the prompt said "Build it". The agent built the entire app: frontend, backend, tests. It took almost eight minutes. With "Don't build anything yet", three of three runs wrote only the spec in about half a minute. Agents like to be helpful, so you must say when not to act. The stack is named here, in one plain sentence, so you need not understand it. After it writes the spec, everybody opens docs/spec.md, reads it and fixes one thing: send a short correction prompt.
words: 26 · budget: 60 · exception: fenced prompt not counted (46 words)
status: tested

## 45. Switch opencode to Plan mode and ask for a step-by-step plan from the spec
type: hands-on
block: Brainstorm → Spec → Plan → Execute · 5 min
visible:
**Goal:** Get a plan you have checked, then save it.

**1. Plan mode.** Press Tab (footer says "plan"), then send:
```text
Read docs/spec.md and give me a numbered step-by-step plan to build it. Don't build anything yet.
```
**2. Read the plan.** Approve it, edit it, or reject it.
To edit, send:
```text
Add one more step at the end: write a short README that explains how to start the app. Show me the updated plan.
```
**3. Build mode.** Approved? Press Tab (footer says "build"), then send:
```text
Save that plan to docs/plan.md. Don't build anything yet.
```
**You should see:** A numbered plan, then docs/plan.md.
**Time:** 5 min
**Stuck?** Checkpoint `s1-spec`.
diagram: none
notes:
Tab switches opencode between two agents. Build can edit files. Plan can read and think but cannot edit files, so it is safe for planning. Step one takes about 20 seconds and returns a numbered list, eight steps in our tests, with the right ports and endpoints. Step two is the checkpoint: read it against your spec. Approve means go to step three. Edit means ask in plain words, as in the second prompt; it adds a ninth step and changes nothing else. Reject means say what is wrong, for example "This plan builds more than the spec asks for. Make it shorter", or ask for a new plan. Plan mode cannot write files, so saving needs Build mode: press Tab, send the third prompt, same session. A one-off "Error: File not found" is a typo the agent corrects itself. Keep "Don't build anything yet" in both prompts.
words: 59 · budget: 60 · exception: fenced prompt not counted (48 words)
status: tested
## 46. Approve, edit or reject: what would you do with each of these three plans?
type: check
block: Brainstorm → Spec → Plan → Execute · 2 min
visible:
Plan 1: 8 steps that follow the spec.
Plan 2: Same, plus a login screen nobody asked for.
Plan 3: Builds a phone app. Ignores the spec.

A. Approve 1 · Edit 2 · Reject 3
B. Approve all three
C. Reject 1 · Approve 2 · Edit 3
reveal: A — Approve what matches the spec, edit what adds extras, reject what ignores it.
diagram: none
notes:
You are the decision-maker. Three outcomes for any plan: approve it as is, edit it by asking the agent to change something, or reject it and ask for a new one. Read the three plans aloud. Vote by hand. B is the lazy choice: approving everything means skipping the review. Click to reveal A. Plan 2 shows scope creep: the agent adds things you never asked for. Edit means you tell the agent: remove the login screen. Plan 3 contradicts the spec, so it is rejected. Tell everyone to read their own plan before approving: check the ports, endpoints and that nothing extra sneaks in. Only an approved plan gets saved to docs/plan.md and built.
words: 59 · budget: 60 · exception: none
status: n/a (no prompt)

## 47. Your app has two parts: a React screen and a FastAPI back end that fetches data and talks to the AI
type: talk, diagram
block: Brainstorm → Spec → Plan → Execute · 2 min
visible:
Screen (React) · port 5173
Back end (FastAPI) · port 8000
yfinance: BBCA data
The AI: the LLM in backend/.env
diagram: Left box "Screen (React)" with subtitle "port 5173", showing a browser window icon. Middle box "Back end (FastAPI)" with subtitle "port 8000". Arrow from the screen to the back end labelled "GET /api/quote/{ticker}, GET /api/history/{ticker}?period=1y" and a second arrow labelled "chat messages (later)". From the back end, two arrows to the right: one to a box "yfinance: BBCA data", one to a box "The AI: the LLM in backend/.env". A small padlock beside backend/.env.
notes:
Give them a mental picture of what the agent is about to build, without code. The screen is what you see in the browser. The back end is a small program running behind it. It fetches BBCA prices from Yahoo through yfinance, and later it talks to the AI for the chatbot. The two parts talk through endpoints, which are just named addresses, like two counters in a bank. The key to the AI lives only in the back end, in a file called .env, so nobody can see it in the browser. Ports are like door numbers: 5173 for the screen, 8000 for the back end. Both come from the spec you wrote.
words: 25 · budget: 40 · exception: none
status: n/a (no prompt)

## 48. Approve the plan, let the agent build the dashboard, then open it in your browser
type: hands-on
block: Brainstorm → Spec → Plan → Execute · 8 min
visible:
**Goal:** Build the dashboard from your approved plan.

**Prompt** (Build mode):
```text
Approved. Build the app from docs/plan.md: backend on port 8000, page on port 5173, with GET /api/quote/{ticker} and GET /api/history/{ticker}?period=1y. Then tell me how to open it.
```
**You should see:** A page at localhost:5173 with BBCA's price, change and chart.
**Time:** 8 min
**Stuck?** Checkpoint `s1-dashboard`.
diagram: none
notes:
The plan was approved and saved on slide 45, so the prompt says "Approved". Each person glances at docs/plan.md once more; if they still want a change, they edit first and save again. Make sure they are in Build mode; Tab if not. Building takes a few minutes; the agent may ask permission to run commands, and they should allow it. While it works, walk the room. When it finishes, the agent should explain how to start the servers. They open localhost:5173 in the browser and check the price, the daily change and the one-year chart. Ask: do the numbers look plausible, in rupiah? This prompt is untested and relies on Python and Node being installed on every laptop; check that in the pre-session list. Anyone behind should switch to s1-dashboard.
words: 30 · budget: 60 · exception: fenced prompt not counted (27 words)
status: UNTESTED

## 49. Add the chatbot: update the spec, get a new plan, approve, build
type: hands-on
block: Brainstorm → Spec → Plan → Execute · 8 min
visible:
**Goal:** Add a chat panel through the same loop.

**1. Brainstorm:**
```text
Let's brainstorm a chatbot for the BBCA dashboard. Ask me one question at a time, at most 2, in plain business language. Don't write any code or files yet.
```
**2. Spec** (read, correct):
```text
Add a chatbot to docs/spec.md. The page sends the whole message list each turn. The backend adds BBCA's current data, then calls the LLM in backend/.env (LLM_BASE_URL, LLM_API_KEY, LLM_MODEL). No buy/sell advice, no tool calling. Don't build yet.
```
**3. Plan** (Tab: Plan mode; approve, edit or reject):
```text
Read docs/spec.md and give me a step-by-step plan for the chatbot only. Don't build yet.
```
**4. Build** (Tab: Build mode, once approved):
```text
Approved. Save that plan to docs/plan.md, then build the chatbot from it.
```
**You should see:** A chat panel that answers questions about BBCA.
**Time:** 8 min
**Stuck?** Checkpoint `s1-chatbot`.
diagram: none
notes:
Same loop as the dashboard, at speed: brainstorm (one or two questions, answered in business terms), spec, plan, build. After step 2, everyone reads the spec update and corrects one thing. After step 3, they read the plan in Plan mode and approve, edit or reject it. The order is always approve, then save, then build. Step 4 overwrites the dashboard plan in docs/plan.md, which is fine because the dashboard is built. Before step 2, participants put the class LLM details into backend/.env; never paste the key into the chat. Connect it to slide 7: the page sends the whole message list every turn, and the backend adds BBCA's data, so no tools are needed. Eight minutes is tight, so send anyone behind to s1-chatbot. All four prompts are untested; rehearse them in order.
words: 48 · budget: 60 · exception: fenced prompt not counted (94 words)
status: UNTESTED

## 50. When something breaks, paste the error and ask the agent to explain it
type: talk
block: Test, debug, iterate · 2 min
visible:
1. Copy the whole error message.
2. Paste it to the agent.
3. Ask: "Explain this in plain words, then fix it."
4. Check that it worked.
diagram: none
notes:
Things will break, and that is normal. The best habit is to avoid describing the problem from memory and paste the real error text instead; the agent can read it better than you can. Ask it to explain first. That way you learn what happened, and you can decide whether the fix makes sense. Where to find errors: in the opencode window, in the server window, and in the browser. If an error is not visible, describe what you saw instead: "the chart is empty". Then check the result yourself. A fix that is claimed but not tested is not a fix. If the agent seems stuck for two minutes, stop it and re-send.
words: 27 · budget: 40 · exception: none
status: n/a (no prompt)

## 51. Ask your chatbot three questions and fix one thing that's wrong
type: hands-on
block: Test, debug, iterate · 5 min
visible:
**Goal:** Test the chatbot and fix one problem.

**Ask the chatbot:** "What is BBCA's latest price?" · "And a month ago?" · "Should I buy BBCA?"

**Then ask opencode:**
```text
The chatbot [describe what is wrong]. Explain the cause in plain words, then fix it.
```
**You should see:** A fixed answer. No buy advice.
**Time:** 5 min
**Stuck?** Raise your hand.
diagram: none
notes:
Each person types the three questions into the chat panel in the browser, not in opencode. Question two tests whether the page really resends the conversation, because "a month ago" only makes sense with the first answer. Question three tests the no-advice rule: a good answer declines and gives facts or risks instead. Find at least one thing that is wrong or could be better: the wording, the format, an answer that is wrong. Describe it in the bracket and send. If everything works, ask for a small improvement, such as showing prices as rupiah. The prompt is untested, so rehearse it with a deliberately broken chatbot.
words: 43 · budget: 60 · exception: fenced prompt not counted (15 words)
status: UNTESTED

## 52. Commit and push your working app
type: hands-on
block: Test, debug, iterate · 3 min
visible:
**Goal:** Save your working app on GitHub.

**Prompt:**
```text
Commit all changes with the message "BBCA dashboard and chatbot". Make sure backend/.env is not committed. Then push to GitHub.
```
**You should see:** New commit on github.com. No .env file there.
**Time:** 3 min
**Stuck?** Raise your hand.
diagram: none
notes:
Same routine as before: commit, then push. The new part is the safety line. backend/.env holds the LLM key, and a key on GitHub can be copied by anyone who sees the repository. Teach this plainly: secrets never go to GitHub. After the push, ask participants to open the repository in their browser and confirm two things: the new commit is there, and there is no .env file in the backend folder. If a key was pushed by mistake, tell the facilitator straight away so it can be replaced. The prompt is untested; check the .gitignore result on your own rehearsal.
words: 26 · budget: 60 · exception: fenced prompt not counted (20 words)
status: UNTESTED

## 53. You built an app by directing an AI, not by writing code
type: recap
block: Close · 3 min
visible:
✓ Model is stateless; the app resends the conversation
✓ AGENTS.md keeps standing rules
✓ Git and GitHub keep your work safe
✓ Brainstorm → Spec → Plan → Build → Test
Checkpoint: s1-chatbot
diagram: none
notes:
Do not re-teach; touch each point quickly and link it to what they did. The model forgets, so the app resends and AGENTS.md remembers. Git kept the work safe and GitHub holds the second copy. And the method: brainstorm, spec, plan, execute, test, iterate. You ran it twice today, for the dashboard and the chatbot. The synthesis: the work you did was judgement, not typing. Anyone who has not finished can switch to checkpoint s1-chatbot, which is the starting point for Session 2. Make sure everybody knows where to find the checkpoint link in the handout.
words: 26 · budget: 40 · exception: none
status: n/a (no prompt)

## 54. Questions
type: Q&A
block: Close · 5 min
visible:
Questions?
Timer: 5:00
diagram: Large "Questions?" heading, with a countdown timer 5:00 in a corner.
notes:
Open the floor. Start with a prompt if no one speaks: what surprised you today? Or: where would you use a dashboard like this at work? Collect parking-lot items on a flip chart. If a question needs a long answer, say you will cover it in Session 2 or the handout. Repeat questions before answering so the room hears them. Keep investment questions neutral: the app shows data; it does not advise. Check one more time that everyone has pushed, and that anyone behind has the s1-chatbot checkpoint.
words: 3 · budget: 40 · exception: none
status: n/a (no prompt)

## 55. Next session: your app remembers prices and learns the rules
type: talk
block: Close · 2 min
visible:
Session 2:
- A database that remembers prices
- A watchlist: BBCA, BBRI, TLKM
- A Wiki so the chatbot knows the rules
diagram: none
notes:
Preview Session 2 in one minute. Today the app fetches prices live and forgets everything when it restarts. In Session 2 it keeps prices in a database and adds a watchlist. The chatbot will also learn from a Wiki, a set of pages from official Indonesian sources, so its answers can name where they came from. Same method: brainstorm, spec, plan, execute, test, iterate. Remind everyone to keep their project or use checkpoint s1-chatbot. Thank them and close. Mention the time of the next session and any homework: none.
words: 20 · budget: 40 · exception: none
status: n/a (no prompt)

## Word count check

Total visible words = text on the slide below the title, plus every quoted diagram label every time it is drawn (a label whose text already appears in the visible block is the same on-screen text, so it is not added twice), plus the reveal line on check slides. Fenced prompt text is excluded and shown separately. Check slides count the reveal line. Notes must be 60–150 words.

| Slide | Type | Total visible words | of which diagram labels | Prompt words | Budget | Notes words | Over? |
|---|---|---|---|---|---|---|---|
| 1 | title | 10 | 0 | 0 | 40 | 92 | no |
| 2 | talk | 27 | 0 | 0 | 40 | 101 | no |
| 3 | demo | 10 | 0 | 0 | 40 | 102 | no |
| 4 | talk | 25 | 0 | 0 | 40 | 88 | no |
| 5 | talk | 16 | 0 | 0 | 40 | 112 | no |
| 6 | talk | 24 | 0 | 0 | 40 | 91 | no |
| 7 | talk, diagram | 30 | 0 | 0 | 40 | 101 | no |
| 8 | hands-on | 29 | 0 | 33 | 60 | 107 | no |
| 9 | talk | 21 | 0 | 0 | 40 | 109 | no |
| 10 | talk | 22 | 0 | 0 | 40 | 103 | no |
| 11 | hands-on | 31 | 0 | 23 | 60 | 104 | no |
| 12 | talk | 32 | 0 | 0 | 40 | 107 | no |
| 13 | talk | 17 | 0 | 0 | 40 | 94 | no |
| 14 | talk, diagram | 35 | 0 | 0 | 40 | 101 | no |
| 15 | talk | 19 | 2 | 0 | 40 | 102 | no |
| 16 | talk | 21 | 0 | 0 | 40 | 99 | no |
| 17 | talk | 32 | 0 | 0 | 40 | 106 | no |
| 18 | hands-on | 53 | 0 | 17 | 60 | 117 | no |
| 19 | check | 44 | 0 | 0 | 60 | 103 | no |
| 20 | talk | 24 | 0 | 0 | 40 | 117 | no |
| 21 | talk | 24 | 0 | 0 | 40 | 115 | no |
| 22 | hands-on | 43 | 0 | 21 | 60 | 112 | no |
| 23 | check | 55 | 0 | 0 | 60 | 103 | no |
| 24 | talk | 11 | 0 | 0 | 40 | 105 | no |
| 25 | talk | 26 | 2 | 0 | 40 | 100 | no |
| 26 | talk | 24 | 0 | 0 | 40 | 105 | no |
| 27 | talk | 36 | 23 | 0 | 40 | 95 | no |
| 28 | hands-on | 58 | 0 | 0 | 60 | 116 | no |
| 29 | hands-on | 27 | 0 | 30 | 60 | 106 | no |
| 30 | check | 42 | 0 | 0 | 60 | 103 | no |
| 31 | break | 5 | 0 | 0 | 40 | 101 | no |
| 32 | talk | 25 | 0 | 0 | 40 | 99 | no |
| 33 | talk | 24 | 0 | 0 | 40 | 105 | no |
| 34 | talk, diagram | 19 | 6 | 0 | 40 | 89 | no |
| 35 | hands-on | 31 | 0 | 28 | 60 | 114 | no |
| 36 | demo | 19 | 0 | 0 | 40 | 118 | no |
| 37 | check | 50 | 0 | 0 | 60 | 111 | no |
| 38 | talk | 20 | 0 | 0 | 40 | 110 | no |
| 39 | talk | 17 | 3 | 0 | 40 | 99 | no |
| 40 | talk | 20 | 0 | 0 | 40 | 113 | no |
| 41 | hands-on | 30 | 0 | 42 | 60 | 104 | no |
| 42 | talk | 15 | 0 | 0 | 40 | 115 | no |
| 43 | talk | 28 | 0 | 0 | 40 | 106 | no |
| 44 | hands-on | 26 | 0 | 46 | 60 | 100 | no |
| 45 | hands-on | 59 | 0 | 48 | 60 | 148 | no |
| 46 | check | 59 | 0 | 0 | 60 | 115 | no |
| 47 | talk, diagram | 25 | 7 | 0 | 40 | 114 | no |
| 48 | hands-on | 30 | 0 | 27 | 60 | 131 | no |
| 49 | hands-on | 48 | 0 | 94 | 60 | 134 | no |
| 50 | talk | 27 | 0 | 0 | 40 | 114 | no |
| 51 | hands-on | 43 | 0 | 15 | 60 | 107 | no |
| 52 | hands-on | 26 | 0 | 20 | 60 | 101 | no |
| 53 | recap | 26 | 0 | 0 | 40 | 96 | no |
| 54 | Q&A | 3 | 0 | 0 | 40 | 88 | no |
| 55 | talk | 20 | 0 | 0 | 40 | 89 | no |

**Block minutes (spec §7):**

| Block | Minutes |
|---|---|
| Opening | 10 |
| LLM basics | 35 |
| Model selection | 10 |
| Git | 30 |
| Break | 10 |
| Skills (focus block) | 20 |
| Brainstorm → Spec → Plan → Execute | 45 |
| Test, debug, iterate | 10 |
| Close | 10 |
| **Total** | **180** |
