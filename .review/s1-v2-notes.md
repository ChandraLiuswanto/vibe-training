# Speaker notes, day3-s1-v2.html (deck position: data-n)

## Deck slide 1 (data-n 1)
Welcome everyone. Today you build a real app, and nobody writes code by hand. You tell an AI coding agent called opencode what you want, you check what it gives you, and you steer it. By the end of these three hours you will have a NISP dashboard and a chatbot, saved on GitHub. Before we start, check that opencode opens on every laptop, Windows and Mac, and that it answers a simple "hello". Anyone whose model does not reply, raise your hand now, so we fix it before the first exercise. Today is mostly hands-on: I explain for a few minutes, then you do it, and we check together.

## Deck slide 2 (data-n 2)
Say what the day produces, in business words. NISP is Bank OCBC NISP, listed as NISP.JK on the Indonesia Stock Exchange. On step 1 point at the price card: the latest price in rupiah and how much it moved today. On step 2, the one-year chart. On step 3, the chatbot answers questions about that data. On step 4, the whole project is saved on GitHub. Optional quick look: open the finished app from checkpoint s1-chatbot at localhost:5173 and ask "What is NISP's latest price?" Have both servers running before class. Then ask: how many of you have written code before? Few hands is fine. Your job is a manager's job: be clear about the goal, then judge the work. Mention that we show market data only. Nothing in the app tells anyone what to buy or sell.

## Deck slide 3 (data-n 3)
Start with what an LLM is: a very large text predictor. On step 1, read the sentence as it types. On step 2, point at the bars: the model scores likely next words. On step 3, it picks one, "NISP", and then repeats, one piece at a time. That is all it does. It can sound like an expert because it learned patterns from a huge amount of text. It can also be confidently wrong, because it predicts what sounds right, not what it has checked. This matters later: when the app needs real NISP numbers, we have to hand them to the model. Ask the room: have you used ChatGPT or Copilot? Those are apps built on language models; the app is the screen you type into, and the model sits behind it.

## Deck slide 4 (data-n 4)
"Stateless" means each request starts from zero. The model does not keep a file about you. On step 0: turn one sends only the first question. Ask: if the model remembers nothing, why does ChatGPT seem to remember our chat? On step 1, answer it: the chat app keeps the whole conversation and sends all of it again, plus your new message. On step 2, point at the rows getting longer. The model reads everything from the top each time, so it looks like it remembers. On step 3, say the caption. Two consequences: long chats cost more and run slower, and anything that is not in what gets sent does not exist for the model. We build exactly this into our chatbot later: the page sends the whole message list every turn.

## Deck slide 5 (data-n 5)
Every request has a limit on how much text the model can take in. That limit is the context window. Think of a desk: only what fits on the desk can be read. On step 1, name each block: everything counts toward it, not just your questions. The rules, the conversation so far, the answers, tool results and any file the agent opened. I won't quote numbers because they differ per model and change often. On step 2: when the desk is full, the oldest material is cut off or replaced by a short summary. Both lose detail. An instruction you gave an hour ago, like "always show prices in rupiah", may be gone without warning. On step 3, two habits: start a new session when a task is finished, and put standing rules in AGENTS.md.

## Deck slide 6 (data-n 6)
Now look inside what gets sent. It is not one blob of text but a list of messages, and each message has a role. On step 1, system: the rules and the role, written by whoever builds the app. On step 2, user: that is you; assistant: the model's replies. On step 3, tool: the result of something the app ran on the model's behalf, like reading a file. The whole list goes to the model every turn, which links back to the last slide. You do not write these lists yourself; opencode and our app build them. Quick check: ask which role the AGENTS.md rules belong to. Most will guess system; that is close enough, since the agent loads it as standing instructions before your first message.

## Deck slide 7 (data-n 7)
So how does an agent read files or run commands? Tool calling. The app, here opencode, tells the model which tools exist. Step 1: the app sends the messages. Step 2: the model replies with a request, "please run this tool with these inputs". Step 3: opencode runs it, and the result comes back as a tool message. Step 4: opencode sends everything again, now with the tool message. Step 5: the model answers using the result. Stress this, and point at the gap between Model and Tool: the model asks, opencode runs. The model never touches your computer itself, and opencode can ask you for permission first. That is why a mistaken model is less scary than it sounds: you stay in the loop. Our chatbot will not use tools yet.

## Deck slide 8 (data-n 8)
Put the last slides together. An agent is the loop you see here. On step 0, you give a goal. On step 1, the model decides what to do next, usually a tool; the app runs it; the model reads the result and decides again. On step 2, let the dot go round: it repeats until the model thinks the task is done. That is why one request can take a minute and touch many files. It is also why the first sentence of your request matters: every step builds on the goal you gave. If the goal is vague, the loop wanders. On step 3, the role split: you bring the goal, the choices and the approval; the agent writes the files and runs the commands. It can be wrong with great confidence, so you check.

## Deck slide 9 (data-n 9)
Since the model forgets between sessions, we need a place to keep standing instructions. On step 0: every session starts empty. On step 1, that place is AGENTS.md, a plain text file in the project folder. On step 2, opencode reads it at the start of every session and puts it in front of the model, so every session starts with the same rules. Typical contents: what the project is, how to run it, and rules like the one on step 3. That rule is the one you will add in the first run. It makes the agent say what it plans to do before it does it, which is very useful when you cannot read the code. Anything permanent goes here, not in a chat.

## Deck slide 10 (data-n 10)
Read the question aloud. Give them thirty seconds to think, then ask for a show of hands for A, B and C. Take one vote at a time. Choice A makes people laugh; ask why a model cannot be tired. Click to reveal the answer. B is right because the session starts empty and only files carry knowledge forward. If someone argues for C, say updates are possible but not the usual cause. Then ask one person to say, in their own words, what rule they would add for their own work. This closes the block on how an agent works and sets up choosing models.

## Deck slide 11 (data-n 11)
Before class, replace [FAST MODEL] and [SMART MODEL] with real names from the model list your participants share. Models come in different sizes. On step 1: a fast model replies in seconds and is fine for small, clear jobs where you see the result straight away. On step 2: a smart model spends longer working things out before it acts. Use it for planning, when a bad plan wastes the whole build, and for debugging, when the cause is not obvious. A wrong choice shows up in two ways: a fast model on a hard job gives a shallow answer; a smart model on a trivial job makes you wait. On step 3, show the picker: type /models in opencode. Names differ per provider, so say "pick one fast and one smart from your list". Today we use the smart model for the plan.

## Deck slide 12 (data-n 11b)
Model choice is one lever; effort is the second. Many models can think for a short or a long time before they answer, and opencode calls these settings variants. On step 0: low effort replies fast, which is right for a typo or a colour change. On step 1: high effort spends more time reasoning first. Use it for the plan and for a bug you cannot explain. It costs time, so do not leave it on high for everything. On step 2: in opencode, Ctrl+T cycles through the efforts your model offers; the current one shows in the footer. Not every model has variants. If Ctrl+T changes nothing, your model has one setting, and that is fine. Rule of thumb: smart model and high effort for the plan, then lower effort while building.

## Deck slide 13 (data-n 12)
On step 0 ask: who has a folder of files like Budget_final_v2_REALLY? Hands up. With copies like these, nobody knows which file is the real one, who changed what, or what was lost. Git keeps one project with every version remembered. On step 1: your local copy is your own desk; only you see it. On step 2: GitHub is a website that hosts the team's filing cabinet, the shared copy. On step 3, the key sentence: nothing moves between the two until you decide to push or pull. Many beginners think saving a file shares it. It does not. Why this matters for an agent: it changes many files quickly, so you need a way to go back and a place where the work is safe.

## Deck slide 14 (data-n 13)
On step 0: a commit is a save point. Not just the file, but the whole project at that moment, with a short note about what changed. Think of a game save with a name. On step 1, the note matters: next month, "Fixed the totals" tells you what happened; "stuff" tells you nothing. Commits live on your own computer; nobody else sees them yet. On step 2, push sends your commits up to GitHub. On step 3, pull is the reverse: it brings a teammate's commits down. Nothing arrives by itself, so pull before you start. On step 4, the daily routine. Today you work alone, so you mostly push. With opencode you do not type Git commands; you ask the agent in plain English, which you do in the next run.

## Deck slide 15 (data-n 14a)
Two things at once, because GitHub sends a confirmation email. Start the sign-up first, then run /init while waiting. Tell people to check their spam folder if the email is late. Anyone who already has an account just signs in. Choose a username you don't mind showing: it appears in the web address of your projects. Then everyone types /init in the empty financial-app folder. It took 43 to 55 seconds in our tests, and the file is short, because the folder is empty. Sometimes a box appears: "Permission required, access external directory". The agent occasionally looks at a path outside the project folder, and opencode asks first. Choose Allow once; it is highlighted, so Enter is enough. Rejecting can leave you with no file; then send /init again. If nothing moves for two minutes, press Esc and resend.

## Deck slide 16 (data-n 14b)
[UNTESTED PROMPT] Send prompt one. Wording around the rule differs between people, and that is fine. Open AGENTS.md together and check the rule is there word for word. Then click to prompt two, the first push. It asks for a commit with a clear message, a new repository, and the push. If the agent says you need to sign in to GitHub, follow its instructions on screen. Agree the sign-in method for Windows and Mac in the pre-session checklist. Confirm success the human way: open github.com, refresh, and look for the financial-app repository containing AGENTS.md. Prompt two is untested and depends on how Git and GitHub sign-in are set up on the laptops, so rehearse it on both. A repository can be private; people can decide. Anyone stuck gets checkpoint s1-start.

## Deck slide 17 (data-n 15)
There are four ways to tell an agent what you want. On step 1: a prompt is the message you type now. AGENTS.md is a standing note that applies to every session. Ask: you have already used two today. Which? Prompt and AGENTS.md; that is why the figure stands on step two. On step 2: a skill is a package of expertise that the agent loads only when a task needs it. On step 3: a workflow strings many steps together; we build one in Session 3. This slide is a map. The rest of this block is about skills, because they are the one most people have not met. Do not explain workflows yet.

## Deck slide 18 (data-n 16)
A skill is a written playbook for one kind of job, packed so the agent can pick it up when needed. Think of a recipe card in a kitchen: the cook picks the right card for the dish. On step 0, connect it to the context window: if the agent loaded every skill in full, the desk would fill up with text it does not need. So the box holds only each skill's name and a one-line description; the full instructions stay on the shelf. On step 1: your request comes in, and it matches the brainstorming description. On step 2: that match tells the agent which skill to open. On step 3: only that one skill's full instructions move into the context, and the agent follows them. The other two stay on the shelf. One lesson: a skill is only found if its description is clear. Skills differ by person. We do not provide a course skill kit. If you have none, today's prompts work without any.

## Deck slide 19 (data-n 17)
[UNTESTED PROMPT] On step 0, read the request. Same folder, same model, same settings; the only change is the skill. On step 1: without a skill, the agent goes straight to an answer, a page idea, built on its guesses. On step 2: with a brainstorming skill loaded, it asks questions first. On step 3, it summarises what was agreed. Point out: compare the structure, not the sentences, because wording varies from run to run anyway. A skill pays off for work you repeat in the same way, like a weekly client memo in a fixed format. One-off questions need only a prompt. Optional two-minute presenter demo, rehearsed on your own setup: run the request in a fresh session, then /new and run it again starting with "Use the [SKILL NAME] skill." Show that the skill was loaded. Keep screenshots as backup.

## Deck slide 20 (data-n 18)
Show how a vague request goes wrong. On step 1: if you say "build me a stock dashboard", the agent fills every gap with a guess: which stocks, which period, what it looks like. On step 2: it will usually build something, quickly, and it may be far from what you meant. Then you spend your time undoing. On step 3, the fix costs two minutes: let it ask you questions first, one at a time, and answer in business terms: who uses it, what decision it supports, how fresh the data must be. This is what a good business analyst does with a stakeholder. Ask who has received work back that missed the point. This pattern is the most useful habit of the day.

## Deck slide 21 (data-n 19)
This is the method for the rest of Day 3. On step 1: brainstorm, the agent asks and you answer. Spec, a written description of what to build. Plan, step by step how. That is Run 2. On step 2: you approve, edit or reject the plan before anything is built. On step 3: execute, the agent builds; test, you check the result in the browser; iterate, you ask for changes, which takes you back to the plan. That is Run 3. We use the same six steps for the dashboard now, the chatbot after, and the features of Sessions 2 and 3. Do not memorise them; they will be on the wall. Notice that nothing gets built until step four.

## Deck slide 22 (data-n 20)
Two documents, two jobs. On step 0: the spec is the contract between you and the agent: what we are building and why, in your words. If you work with product teams, this is the same thing as a PRD, a product requirements document; a short one is enough. On step 1, it needs only three parts. Goals say what the app must do. Out of scope says what it must not do, which stops the agent adding extras. How we'll know it works describes what you will see when it is right; without it you cannot judge the result. On step 2: the plan is the agent's proposal for how to build it, in numbered steps. On step 3: you approve, edit or reject the plan. Both are files in the project, so they survive when a session ends. A new session can read the spec and carry on.

## Deck slide 23 (data-n 21a)
Everyone sends prompt one exactly as written. In our tests the agent asked five short questions, about five seconds each, then summarised in three bullets. The first question was about the audience. Others vary, so answer what is actually asked. Sample answers: sales team before client meetings; delayed is fine if it shows the update time; mostly laptops. Watch for anyone whose agent starts writing files. Never reply "Yes, go ahead" after the summary; that invites a build. Click to prompt two. Teach "Don't build anything yet": without it, our first test built the whole app in eight minutes. With it, three of three runs wrote only the spec in about half a minute. The stack is named in one plain sentence, so you need not understand it. Everybody opens docs/spec.md, reads it and corrects one thing.

## Deck slide 24 (data-n 21b)
Tab switches opencode between two agents. Build can edit files. Plan can read and think but cannot edit files, so it is safe for planning. Step one takes about 20 seconds and returns a numbered list, eight steps in our tests. On step two, read it against your spec. Approve means go to step three. Edit means ask in plain words; the README example in the handout adds a ninth step and changes nothing else. Reject means say what is wrong, for example "This plan builds more than the spec asks for. Make it shorter." Plan mode cannot write files, so saving needs Build mode: press Tab, send the save prompt, same session. A one-off "Error: File not found" is a typo the agent corrects itself. Keep "Don't build anything yet" in both prompts.

HANDOUT:
Edit example (send in Plan mode, same session):
```text
Add one more step at the end: write a short README that explains how to start the app. Show me the updated plan.
```

## Deck slide 25 (data-n 22)
You are the decision-maker. Three outcomes for any plan: approve it as is, edit it by asking the agent to change something, or reject it and ask for a new one. Read the three plans aloud. Vote by hand. B is the lazy choice: approving everything means skipping the review. Click to reveal A. Plan 2 shows scope creep: the agent adds things you never asked for. Edit means you tell the agent: remove the login screen. Plan 3 contradicts the spec, so it is rejected. Tell everyone to read their own plan before approving: check the ports, endpoints and that nothing extra sneaks in. Only an approved plan gets saved to docs/plan.md and built.

## Deck slide 26 (data-n 23)
Give them a mental picture of what the agent is about to build, without code. On step 0: the screen is what you see in the browser. On step 1: the back end is a small program running behind it. The two talk through endpoints, which are just named addresses, like two counters in a bank. On step 2: the back end fetches NISP prices from Yahoo through yfinance and sends them to the screen. On step 3: later, for the chatbot, it also talks to the AI. The key to the AI lives only in the back end, in a file called .env, so nobody can see it in the browser. Ports are door numbers: 5173 for the screen, 8000 for the back end. Both come from the spec you wrote.

## Deck slide 27 (data-n 24a)
[UNTESTED PROMPT] The plan was approved and saved in Run 2, so the prompt says "Approved". Each person glances at docs/plan.md once more; if they still want a change, they edit first and save again. Make sure they are in Build mode; Tab if not. Building takes a few minutes; the agent may ask permission to run commands, and they should allow it. While it works, walk the room. When it finishes, the agent should explain how to start the servers. They open localhost:5173 and check the price, the daily change and the one-year chart. Ask: do the numbers look plausible, in rupiah? This prompt is untested and relies on Python and Node being installed on every laptop; check that in the pre-session list. Anyone behind switches to s1-dashboard.

## Deck slide 28 (data-n 24b)
[UNTESTED PROMPT] Same loop as the dashboard, at speed; the handout has every prompt. Before the spec, participants put the class LLM details into backend/.env; never paste the key into the chat. The spec is shown because it carries the new content: the page sends the whole message list every turn, as on slide 4, and the back end adds NISP's data, so no tools are needed. After the plan, they approve, edit or reject; the order is approve, save, build. On step 1, they type the three questions in the browser, not opencode. "A month ago" tests the resent conversation; "Should I buy" tests the no-advice rule. Fix one thing with the handout prompt. On step 2, the push: .env holds the key, and secrets never go to GitHub. All prompts here are untested; rehearse them in order.

HANDOUT:
1. Brainstorm:
```text
Let's brainstorm a chatbot for the NISP dashboard. Ask me one question at a time, at most 2, in plain business language. Don't write any code or files yet.
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

## Deck slide 29 (data-n 25)
Things will break, and that is normal. On step 0: the best habit is to avoid describing the problem from memory and copy the real error text instead. On step 1: paste it to the agent; it reads errors better than you can. Point at the tags: errors show up in the opencode window, in the server window, and in the browser. If no error is visible, describe what you saw: "the chart is empty". On step 2: ask it to explain first. That way you learn what happened, and you can decide whether the fix makes sense. On step 3: check the result yourself. A fix that is claimed but not tested is not a fix. If the agent seems stuck for two minutes, stop it and re-send.

## Deck slide 30 (data-n 26)
Do not re-teach; touch each point quickly and link it to what they did. The model forgets, so the app resends the conversation and AGENTS.md remembers your rules. Git kept the work safe and GitHub holds the second copy, which you pushed twice today. And the method: brainstorm, spec, plan, execute, test, iterate. You ran it twice, for the dashboard and the chatbot. The synthesis: the work you did was judgement, not typing. You decided what to build, checked the plan and tested the result. Anyone who has not finished can switch to checkpoint s1-chatbot, which is the starting point for Session 2. Make sure everybody knows where to find the checkpoint link in the handout.

## Deck slide 31 (data-n 27)
Open the floor. Start with a prompt if no one speaks: what surprised you today? Or: where would you use a dashboard like this at work? Collect parking-lot items on a flip chart. If a question needs a long answer, say you will cover it in Session 2 or the handout. Repeat questions before answering so the room hears them. Keep investment questions neutral: the app shows data; it does not advise. Check one more time that everyone has pushed, and that anyone behind has the s1-chatbot checkpoint.

## Deck slide 32 (data-n 28)
Preview Session 2 in one minute. Today the app fetches prices live and forgets everything when it restarts. In Session 2 it keeps prices in a database and adds a watchlist. The chatbot will also learn from a Wiki, a set of pages from official Indonesian sources, so its answers can name where they came from. Same method: brainstorm, spec, plan, execute, test, iterate. Remind everyone to keep their project or use checkpoint s1-chatbot. Thank them and close. Mention the time of the next session and any homework: none.

