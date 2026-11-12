## 1. Verdict

**Revise before delivery.** The deck has a useful destination—participants direct opencode to produce a NISP dashboard and chatbot—and its three-run structure is stronger than a collection of unrelated exercises. However, the learning journey is still **technology-first rather than business-task-first**: the first substantial participant run begins about 55 minutes in, the central workflow is not introduced until slide 21, and participants encounter technical requirements before receiving the explanations needed to review them. The original brief is substantially covered in topics, but installation is assumed, skills and workflows receive little participant practice, and testing/debugging/iteration are compressed. More importantly, several explanations risk teaching incorrect mental models, particularly the AI being “in” `.env`, automatic removal of standing rules, and universal claims about conversation memory. My assessment uses the HTML, all extracted notes, supporting documents, and selected click-step screenshots; I did not reproduce the exercises. **Version-specific opencode loading order, message-role mappings, shortcuts and permission guarantees remain unverified unless explicitly supported by the supplied test record.**

## 2. Findings

### 1. P0 · Material — The architecture diagram puts the AI inside a settings file
**Slides:** slide 26 (data-n 23); slide 28 (data-n 24b).

**Evidence:** “The AI: the LLM in backend/.env”; the chatbot prompt similarly says “calls the LLM in backend/.env.” Screenshot: `26_n23_step3.png`.

**Why it matters:** A non-programmer can reasonably conclude that `.env` contains the AI, rather than connection settings and a secret key. The padlock also risks implying that the file itself provides security.

**Proposed fix:** Change the title to **“Your screen gets data and AI answers through a back-end program.”** Reveal:
1. Browser screen on the laptop.
2. Back-end program on the laptop.
3. Market-data source.
4. External AI service.
5. A separate small settings-file card beside the back end: **“`.env`: service address, model name and secret key—not the AI.”**

Notes should clarify that storing a key in this file is only part of protecting it: it must not be exposed to the browser, chat or repository.

### 2. P0 · Material / Animation — The context animation teaches that standing rules automatically fall out
**Slides:** slide 5 (data-n 5); slide 6 (data-n 6); slide 18 (data-n 16).

**Evidence:** Slide 5 visibly throws the struck-through “rules” block out of the window. Caption: “Full → oldest details dropped or summarised.” Slide 6 notes accept AGENTS.md belonging to the system role as “close enough.” Screenshot: `05_n5_step2.png`.

**Why it matters:** Participants are being shown a concrete mechanism, not merely a metaphor. They may learn that system instructions and project rules are discarded in simple chronological order. Actual truncation/compaction and rule handling are application-dependent; the exact opencode 1.19.5 behavior is **unverified** here.

**Proposed fix:** Separate **context assembly** from **context capacity**:
- First show the intended teaching sequence: system instructions → project instructions from AGENTS.md → available-skill descriptions → user request.
- Then show the model requesting relevant skill instructions/files and receiving tool results.
- On a separate capacity reveal, show **conversation details** being condensed, not system rules tumbling away.

Label the assembly diagram **“Simplified view; exact packaging depends on the agent.”** Verify the version-specific ordering before presenting it as literal runtime behavior. Do not teach a message-role mapping as “close enough.”

### 3. P0 · Material — “Stateless” is useful, but the surrounding absolutes overstate it
**Slides:** slide 4 (data-n 4); slide 9 (data-n 9); slide 10 (data-n 10).

**Evidence:** “The app resends the whole conversation every turn”; “every session starts empty”; quiz answer: “Nothing carries over between sessions except files.”

**Why it matters:** These statements conflate a model request with the surrounding product. Applications can store conversations, summaries, settings and other state; a resumed conversation is not the same thing as a fresh conversation. “Overnight” is also not itself a reset condition.

**Proposed fix:** Use **“The model answers from the context the application supplies for that request.”** Explain:  
> “Our classroom chatbot sends the conversation again. Other products may send selected history or summaries. Starting a new opencode conversation is different from continuing an existing one.”

Rewrite the quiz situation to specify **“You started a new conversation and had not saved the preference as a project rule.”**

### 4. P0 · Hands-on — The deck teaches automatic permission approval
**Slides:** slide 15 (data-n 14a); slide 27 (data-n 24a).

**Evidence:** “Permission box? Choose Allow once (Enter).” Later: “Agent asks to run a command? Allow it.”

**Why it matters:** For bank staff, the transferable lesson must not be “permission prompts are obstacles to click through.” External-folder access can expose unrelated files, and commands can make consequential changes.

**Proposed fix:** Replace with:
> **“Check what it wants to access or change. Allow only the expected classroom action; ask the facilitator if unsure.”**

Show one expected request with the project folder highlighted and one unexpected request outside it. The supplied test record explains why an occasional malformed path caused a permission request; that is a reason to inspect it, not a general reason to approve.

### 5. P1 · Storyline — The main learning method arrives after most introductory theory
**Slides:** slide 2 (data-n 2); slide 8 (data-n 8); slide 21 (data-n 19).

**Evidence:** The outcome appears on slide 2, but the complete workflow first appears on slide 21. Slides 3–10 explain model internals before participants see how those ideas support their own working method.

**Why it matters:** Participants have no organizing map for the theory. They must remember several mechanisms before learning what decisions they will actually make.

**Proposed fix:** Put the workflow immediately after the outcome/demo:
**“You define the need, approve the plan, and verify what the AI builds.”**  
Keep a small “you are here” version at the start of each run. Introduce technical concepts just before their practical use.

### 6. P1 · Storyline — The workflow terminology does not match the original brief
**Slides:** slide 21 (data-n 19); slide 23 (data-n 21a); slide 28 (data-n 24b); slide 30 (data-n 26).

**Evidence:** The brief specifies **Interview → Plan (Approve/Edit/Reject) → Execute → Test/Debug → Iterate**. The deck teaches six steps: **Brainstorm → Spec → Plan → Execute → Test → Iterate**, and the chatbot mini-map becomes **Brainstorm → Spec → Plan → Build**.

**Why it matters:** Beginners may interpret these as different methods. “Brainstorm” can imply idea generation, whereas the exercise is requirements interviewing. Debugging disappears from the named method.

**Proposed fix:** Use the brief’s five phases consistently:
**Interview → Plan: Approve/Edit/Reject → Execute → Test/Debug → Iterate.**

Place **“Save the agreed requirements in `docs/spec.md`”** as the Interview output, not an unexplained additional phase. Notes can say:
> “We call this an interview: the agent asks, and you answer. Some skills call it brainstorming.”

The internal course spec uses six phases, so this needs an explicit owner decision rather than an unnoticed wording substitution.

### 7. P1 · Storyline — Technology is used before participants can understand or review it
**Slides:** slide 7 (data-n 7); slide 23 (data-n 21a); slide 25 (data-n 22); slide 26 (data-n 23).

**Evidence:** Slide 7 uses `read_file` and `docs/spec.md` before explaining the project-file structure. Slide 23 requires React, Vite, FastAPI, Python, yfinance, endpoints and ports. Slide 25 notes instruct participants to “check the ports, endpoints”; explanations arrive on slide 26.

**Why it matters:** “Copy this; you need not understand it” conflicts with “you are the decision-maker.” Participants cannot reliably approve a plan against requirements they cannot interpret.

**Proposed fix:** Move the plain-language architecture before the spec prompt. Introduce:
- React/Vite: tools used to build the screen.
- FastAPI: a tool used to build the back-end service.
- yfinance: a library that retrieves Yahoo Finance data.
- Endpoint: a named request address.
- Port: a numbered access point for a running program.

Keep implementation strings in a clearly marked **“technical setup supplied by the course”** box. Require business checks first; make exact endpoint/port matching a guided check, not an assumed skill.

### 8. P1 · Material — “App” means different things without a visible distinction
**Slides:** slide 2 (data-n 2); slide 4 (data-n 4); slide 7 (data-n 7); slide 26 (data-n 23).

**Evidence:** Slide 2’s app is the financial dashboard; slide 7’s large black “App” box actually means opencode. Only the notes state “the app, here opencode.” Screenshot: `07_n7_step5.png`.

**Why it matters:** The audience can conclude that the financial app reads project files and runs build commands.

**Proposed fix:** Use three stable labels:
- **opencode — the coding agent**
- **Financial App — the software you are building**
- **AI model — the service used to generate answers**

On slide 7 label the box **“opencode on your laptop”**, and the tool **“Read a project file.”** Say explicitly that the classroom chatbot does not use tool calling in Session 1.

### 9. P1 · Material — AGENTS.md has an introduction but no maintenance model
**Slides:** slide 9 (data-n 9); slide 16 (data-n 14b); slide 30 (data-n 26).

**Evidence:** “Anything permanent goes here, not in a chat.” The only maintenance action is adding one rule; no later review is taught.

**Why it matters:** Participants may fill the file with changing requirements, old facts and duplicate rules. They also do not learn why maintaining it matters once the project evolves.

**Proposed fix:** Title: **“AGENTS.md keeps shared project instructions consistent across conversations.”** Show:
**Discover a lasting rule → ask for an update → read the change → commit it → revisit when the project changes.**

Notes:
> “Use it for project-wide working instructions. Put feature requirements in the spec and current implementation steps in the plan. After a major change, check whether project instructions are still accurate.”

For this audience, recommending agent-assisted edits reduces accidental deletions and helps keep instructions consistent. **Do not claim manual editing is prohibited or technically unsafe by definition:** it is a text file, and a careful human edit can be valid.

### 10. P1 · Hands-on — Installation is assumed rather than taught or explicitly closed out
**Slides:** slide 1 (data-n 1); slide 15 (data-n 14a).

**Evidence:** Opening notes only check whether opencode opens and answers “hello.” Run 1 starts “in opencode, in financial-app,” without showing how that folder was created/opened. The course spec assumes opencode, Python and Node.js are preinstalled; the original brief includes tool installation.

**Why it matters:** The brief is not fully met unless installation is consciously treated as prework. Non-programmers can be blocked before `/init` even starts.

**Proposed fix:** Add a brief readiness gate:
**“Start only when these four checks pass on your laptop.”**  
Show the approved opencode version, working model access, correct project folder, and required runtime checks. Put Windows/Mac installation and recovery steps in linked prework/handout material, and explicitly state that installation was completed before class. Do not attempt full mixed-platform installation inside the current run budget.

### 11. P1 · Storyline / Hands-on — The 180 minutes add up, but the teaching balance does not match “mostly hands-on”
**Slides:** slide 15 (data-n 14a); slide 23 (data-n 21a); slide 27 (data-n 24a); slide 28 (data-n 24b), across the deck.

**Evidence:** The copy’s per-slide allocations total 180 minutes. Explicit run-slide time is **25 + 20 + 32 = 77 minutes**, approximately **43%**. The first substantial run starts around minute 55; dashboard construction starts around minute 134.

**Why it matters:** The most failure-prone work is concentrated near the end, after a long sequence of concepts. The schedule leaves no unallocated recovery time.

**Proposed fix:** Shorten/merge the model-internals block, teach Git and skills alongside their use, and reserve explicit recovery capacity. Aim for **at least 100 minutes of participant work**, with a separately visible buffer. The 18-minute chatbot block needs timed rehearsal with novice users; model response times alone do not establish classroom completion time.

### 12. P1 · Hands-on — The required output depends on exercises explicitly marked untested
**Slides:** slide 16 (data-n 14b); slide 27 (data-n 24a); slide 28 (data-n 24b).

**Evidence:** Notes mark the GitHub push, dashboard build and chatbot prompts **“[UNTESTED PROMPT]”**. `prompts/s1.md` proves reported runs through spec/plan only; pushes used a local bare repository rather than GitHub.

**Why it matters:** The central promise—“you built it”—is not supported by an end-to-end rehearsal. Authentication, server startup and chatbot credentials are exactly where novice groups can stall.

**Proposed fix:** Treat delivery readiness as a gate: run the complete participant path on Windows and Mac, including real GitHub authentication, server startup, chatbot tests and recovery. Record novice completion times and common failure branches. **End-to-end success is unverified in the supplied evidence.**

### 13. P1 · Hands-on — The chatbot is a second project-sized exercise squeezed onto one slide
**Slides:** slide 28 (data-n 24b).

**Evidence:** In 18 minutes, participants must configure `.env`, repeat interview/spec/plan/approval/build, ask three test questions, fix something and push. Most prompts are in the notes/handout; the visible mini-map omits approval, testing and iteration. Screenshot: `28_n24b_step2.png`.

**Why it matters:** Participants are asked to transfer an unfamiliar method while also handling credentials and a second AI connection. Those who fall behind cannot locate their current step on the slide.

**Proposed fix:** Split into **“Agree and approve the chatbot”** and **“Build, test and save the chatbot.”** Provide an explicit safe configuration step and a numbered checklist synchronized with the handout. Keep the approval gate visible. Allocate time from the theory reduction, rather than shrinking the same work into 18 minutes.

### 14. P1 · Material / Hands-on — Skills and workflows are described, but participants do not learn to use or distinguish them
**Slides:** slide 17 (data-n 15); slide 18 (data-n 16); slide 19 (data-n 17).

**Evidence:** Workflow is tagged “Session 3”; notes say “Do not explain workflows yet.” There is no participant action to inspect available skills or identify when one has loaded. The course spec calls for listing and reading participants’ own skills.

**Why it matters:** The original brief asks for different ways to provide instructions and expertise, not merely recognition of four labels.

**Proposed fix:** Add one short applied choice:
> “A title change; a rule for every conversation; a repeatable report-writing method; a sequence that produces a report and deck—which instruction method fits each?”

Demonstrate inspecting one available skill using the version-tested method. If none is installed, say so and demonstrate a supplied example without implying participants have it. Define workflow now as a repeatable sequence; defer authoring one to Session 3.

### 15. P0 · Material — The skill comparison presents an illustrative outcome as a general guarantee
**Slides:** slide 19 (data-n 17).

**Evidence:** Title: “The same request gives a more structured result when a skill is loaded.” Panel labels: “Without a skill: a straight answer”; “With a brainstorming skill: questions first, then a summary.” Notes mark the demo untested.

**Why it matters:** Models can ask useful questions without a skill. A skill does not automatically guarantee higher quality, and poor skill instructions can worsen a result.

**Proposed fix:** Title: **“A relevant skill can make a repeatable method easier to follow.”** Show one short instruction excerpt—“Ask one business question at a time; summarize agreed requirements”—beside a demonstrated result. Label it **“Illustrative example”** until tested. Explain that the same behavior can also be requested directly in a prompt.

### 16. P1 · Material / Hands-on — Model choice is not yet actionable, and reasoning effort sounds like a guaranteed timer
**Slides:** slide 11 (data-n 11); slide 12 (data-n 11b).

**Evidence:** `[FAST MODEL]` and `[SMART MODEL]` remain visible. Title: “Effort sets how long the model thinks before it answers.” The dial implies universal low/medium/high settings. Notes acknowledge that not every model offers variants.

**Why it matters:** Participants need a concrete selection they can reproduce. “More effort” is not a promise of a fixed duration or a correct answer.

**Proposed fix:** Replace placeholders with approved classroom models and demonstrate one real selection. Title: **“Use more reasoning effort for difficult work when the selected model supports it.”** Put the support caveat on the slide. Add a two-scenario choice check: cosmetic change versus unexplained calculation error.

The exact Ctrl+T behavior and offered variants in the classroom configuration are **unverified** by the supplied prompt tests; verify them before using the shortcut as an instruction.

### 17. P1 · Quality / Storyline — Both quizzes largely reveal the answer inside the question
**Slides:** slide 10 (data-n 10); slide 25 (data-n 22).

**Evidence:** Quiz 1 offers “The agent was tired.” Quiz 2 labels plans “follow the spec,” “nobody asked for,” and “ignores the spec”; distractors include approving all three. Screenshots: `10_n10_step0.png`, `25_n22_step0.png`.

**Why it matters:** These check whether participants can identify an obviously sensible sentence, not whether they can apply the concepts. The plan quiz also comes after participants have already reviewed their plans.

**Proposed fix:** Move the plan check before live approval. Show a short agreed requirement and an actual plan excerpt with one subtle mismatch—for example, a price card with no update time despite delayed-data requirements. Ask participants to identify the mismatch and write the edit instruction.

For AGENTS.md, offer plausible actions such as resume the old conversation, save a reusable project rule, or change model; ask which addresses a fresh-conversation requirement and why. Remove “lazy choice” from facilitator notes.

### 18. P0 · Material — Git is described as remembering more than it actually saves
**Slides:** slide 13 (data-n 12); slide 14 (data-n 13); slide 30 (data-n 26).

**Evidence:** Notes say “every version remembered” and a commit saves “the whole project at that moment.” Recap says Git/GitHub “keep your work safe.”

**Why it matters:** Participants may think ordinary file saves are automatically recoverable, or that ignored/uncommitted files—including `.env`—are in the remote backup.

**Proposed fix:** Keep the save-point analogy, but qualify it:
> **“A commit records the project changes included in that commit. Push copies those commits to the remote repository.”**

Use three states: **edited locally → committed locally → pushed remotely**. Add a check: “You edited a file but did not commit. Is that edit in GitHub?” Show secrets as deliberately excluded. The core local-versus-remote explanation is useful and should remain.

### 19. P1 · Hands-on — Financial correctness is reduced to plausibility and successful-looking answers
**Slides:** slide 27 (data-n 24a); slide 28 (data-n 24b).

**Evidence:** Notes ask “do the numbers look plausible, in rupiah?” Chatbot tests list questions but not evidence or pass criteria. “And a month ago?” is expected to work although the visible spec says the back end adds “current data.”

**Why it matters:** A polished chart and fluent answer can both be wrong. “A month ago” also needs a defined date policy when the target date is not a trading day. It is **unverified** whether the chatbot is supplied the history required for that answer.

**Proposed fix:** Show a compact acceptance table:
- Ticker is NISP.JK; currency is IDR.
- Data date/time and freshness are visible.
- Displayed price/change match the same dated source.
- One historical point matches the chart/source.
- Chatbot figures match supplied data; missing data leads to “I don’t have that data.”
- Buy/sell request does not produce a recommendation.

Include sufficient dated history in the chatbot requirements, or change the historical test.

### 20. P1 · Storyline / Hands-on — Debugging is taught after participants have already needed it; iteration is not a visible completed action
**Slides:** slide 27 (data-n 24a); slide 28 (data-n 24b); slide 29 (data-n 25).

**Evidence:** Build and chatbot exercises precede the debugging explanation. “Fix one thing” is mainly in the chatbot handout notes; the dashboard has no explicit before/after improvement.

**Why it matters:** Beginners encountering their first server error lack a recovery routine. Participants whose first build appears to work may never practice iteration.

**Proposed fix:** Move the debugging routine immediately before the build. Give it a reusable structure:
**Expected result → actual result → exact error/screenshot → explanation → fix → rerun the failed check.**

After the first working dashboard, require one small business-driven improvement—for example, make the data timestamp clearer—then verify it. Distinguish **debugging a defect** from **iterating on a requirement or presentation**.

### 21. P1 · Storyline — The recap declares completion without an exit check, and the next-session bridge overstates memory and learning
**Slides:** slide 30 (data-n 26); slide 31 (data-n 27); slide 32 (data-n 28).

**Evidence:** “You built an app…” is followed mainly by conceptual recap. Recovery is a checkpoint name. Slide 32 notes say the app fetches prices “live” and “forgets everything when it restarts”; the title says it “learns the rules.”

**Why it matters:** Not everyone will have finished. Restarting does not erase project files or Git history. A Wiki supplies reference material at answer time; it does not necessarily retrain the model. “Live” is also inappropriate unless freshness is established.

**Proposed fix:** End with **“Show that your app works—and know how to resume next session.”** Require:
1. Open dashboard.
2. Pass one data check and one chatbot check.
3. Confirm the latest commit is on GitHub.
4. Confirm either the working project or the tested recovery checkpoint is ready.

Then bridge with:
> **“Next session, save price data between runs and give the chatbot official reference pages.”**

Notes: project files already persist; Session 2 adds application-data storage and sourced reference context. Provide a clickable checkpoint/recovery route. Its availability and recovery behavior are **unverified** in this review.

## 3. Add, cut and reorder

### Add or strengthen
- **One early business scenario:** “Prepare for a client meeting: inspect NISP’s price trend and ask a factual follow-up.” This supplies the “why” without adding investment-advice scope.
- **A readiness gate and three stable labels:** opencode, Financial App, AI model.
- **One genuine worked plan-review example before practice.**
- **Visible financial acceptance criteria and a final completion check.**
- **A safe AGENTS.md maintenance loop and a permission-review habit.**

### Cut or compress
- Compress the model-internals opening; retain only mechanisms that support participant decisions.
- Remove “Spec = PRD” unless this audience needs the acronym. “Agreed requirements” is sufficient.
- Remove silly quiz distractors and the unproven skill-quality comparison.
- Move exact technical setup strings to clearly identified course-supplied configuration; do not require unexplained technical judgment.
- Replace universal claims about memory, context removal and skill outcomes with scoped explanations.

### Proposed headline-only sequence

1. **Build a NISP dashboard and chatbot by directing the AI**
2. **Use the app to inspect a price trend and ask factual follow-up questions**
3. **You interview, approve, execute, test/debug and iterate**
4. **Check your laptop and model access before starting**
5. **opencode builds the Financial App; an AI model helps it decide what to do**
6. **The coding agent requests tools, runs permitted actions and checks results**
7. **The model answers from the context supplied for each request**
8. **opencode combines standing instructions, your request and relevant project information**
9. **Long conversations can lose detail, so save durable project instructions**
10. **AGENTS.md keeps project-wide instructions consistent—and needs review as work changes**
11. **Git records local save points; GitHub holds the commits you push**
12. **Run 1: create the project, add one reviewed rule and push**
13. **Check: distinguish an edited file, a local commit and a pushed commit**
14. **Choose a model and supported reasoning effort to match the task**
15. **Prompts, project rules, skills and workflows solve different instruction needs**
16. **Inspect a skill’s instructions before relying on its method**
17. **The Financial App has a browser screen and a back-end service**
18. **Interview the business need before asking the agent to build**
19. **Save agreed requirements, scope and acceptance checks in the spec**
20. **Approve, edit or reject a plan against those requirements**
21. **Check a worked plan before reviewing your own**
22. **Run 2: interview, save the requirements and approve the dashboard plan**
23. **When something breaks, report the evidence and rerun the failed check**
24. **Run 3A: build the dashboard and verify its dated financial data**
25. **Improve one dashboard detail and check the result again**
26. **Keep AI-service credentials in local configuration, not chat or GitHub**
27. **Run 3B: interview, approve and build the chatbot**
28. **Test factual answers, conversation follow-ups and the no-advice boundary**
29. **Commit and push the verified app without secrets**
30. **Show your working result—or recover to the shared starting point**
31. **Questions: explain one decision you made and how you checked it**
32. **Next session, save price data and add official reference pages**

This preserves roughly the current slide count but moves the business method forward, puts prerequisites before use, and makes verification—not merely construction—the culmination.