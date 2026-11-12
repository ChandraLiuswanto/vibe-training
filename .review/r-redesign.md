## 1. Verdict

The deck has a useful teaching spine, but the three flagged slides currently encourage a misleading mental model: “the app” changes identity, context appears to work like a conveyor belt that throws away rules, and AGENTS.md looks like automatic memory rather than a maintained project brief. I recommend rebuilding slides 5–6 as a two-slide explanation of **what opencode supplies** and **what happens as context grows**, rebuilding slide 7 as a chronological sequence diagram, and rebuilding slide 9 around an onboarding analogy and a maintenance cycle. Keep the deck at 32 slides by reusing slide 6 rather than adding a slide. **Verification boundary:** the HTML, supplied notes, screenshots, and test report support the findings below; opencode 1.19.5’s exact request serialization, instruction placement, and compaction behavior remain **unverified**. Do not turn the requested conceptual order into a claim about the exact API payload without inspecting that version.

## 2. Findings

### 1. P0 · Material — The requested input order must not be presented as verified API order

**Slides:** slide 5 (data-n 5), slide 6 (data-n 6), and slide 18 (data-n 16).

**Evidence:** Slide 6 says, “Every request is one list of messages: system, user, assistant, tool.” Its notes accept “system” as “close enough” for the role of AGENTS.md. Slide 18 labels skill names and descriptions “Always loaded.”

**Why it matters:** The audience needs a dependable business-level model, not a simplified diagram later mistaken for a technical specification. A file’s purpose, its position in an explanation, and its API message role are different things. Tool definitions may also be supplied separately from chat messages.

**Fix:**

- Show the owner’s requested order as a **schematic of supplied context**: system prompt → AGENTS.md → skill list → conversation → latest user request.
- Put **“Schematic—not API order”** on the slide.
- Label AGENTS.md and the skill list **“when available”**, not universally present.
- Explain that “every turn” means **every model call**, including calls following tool results. A tool-result continuation does not require another new user prompt.
- Before removing the caveat, inspect opencode 1.19.5’s actual request construction for the course provider/model.

**Confidence:** High on the distinction; exact opencode ordering and role mapping are **unverified**.

---

### 2. P0 · Material / Animation — Replace slide 5’s falling blocks with a supplied-context diagram

**Slide:** slide 5 (data-n 5).

**Evidence:** `.review/s1-v2-shots/05_n5_step3.png` visibly shows **“rules”** falling out and crossed through. The title says old details “drop off”; the green panel says **“Fix: /new session. Rules in AGENTS.md.”**

**Why it matters:** Participants could conclude that opencode routinely discards standing rules just because they were placed first, and that `/new` recovers lost information. Neither is a safe general lesson.

### Proposed redesign A — use the existing slide 5

**Assertion title:**  
**opencode supplies instructions and working context—not just your latest message**

**Layout:** A vertical five-row packet on the left, one arrow to **Model** on the right. Read top to bottom. Bracket the first three rows as standing inputs; bracket conversation separately. Never animate instructions falling out.

**Exact click build:** Text accumulates unless stated otherwise. The final state has **36 non-title words**, so every state stays below 40.

| Step | Visual action | Exact new visible text |
|---|---|---|
| 0 | Show sender, receiver, and caveat | `opencode → Model` / `*When available. Schematic—not API order.` |
| 1 | Reveal first row | `Standing inputs` / `System prompt (opencode)` |
| 2 | Reveal second row | `AGENTS.md* (project rules)` |
| 3 | Reveal third row | `Skill list* (names + descriptions only)` |
| 4 | Reveal conversation area | `Conversation so far` / `User messages · model replies · tool results` |
| 5 | Reveal final row, then send the packet once | `New user prompt` |

**Speaker notes draft:**

> What you type is only part of what the model receives. opencode prepares the working context. Read this diagram from top to bottom: its own operating instructions; applicable project rules from AGENTS.md; a list of available skills; the conversation so far; and your new request.  
>   
> The skill list contains names and descriptions, not every skill’s full instructions. A selected skill can be opened later, adding more working text. Files the agent reads normally reach the model through tool results; merely having a file in the folder does not mean the model has read it.  
>   
> This is a teaching diagram, not a screenshot of the API request. Availability and exact packaging depend on the setup. On the first call, there is no earlier conversation. After a tool result, opencode can call the model again without waiting for another user message. Next, let’s see why this working context cannot grow forever.

**What it replaces:** All existing context-conveyor blocks, falling rules, and the `/new` “fix.”

---

### 3. P1 · Storyline / Material — Make this a two-slide explanation; repurpose slide 6 rather than stacking more concepts onto slide 5

**Slides:** slide 5 (data-n 5) and slide 6 (data-n 6).

**Evidence:** Slide 5 currently combines capacity, forgetting, dropped rules, summarization, session management, and AGENTS.md. Slide 6 then starts a separate role taxonomy.

**Why it matters:** “What gets supplied?” and “What happens when it grows?” are two different questions. Trying to answer both in one animated diagram makes the owner’s requested order harder to understand.

### Proposed redesign B — use the existing slide 6

**Assertion title:**  
**Context has a limit, so save important decisions outside the chat**

**Layout:** Reuse the packet vocabulary from slide 5, now inside a wide capacity frame. Standing inputs stay visually anchored. Conversation is the expandable region. Leave a separate unfilled area for the reply. These are schematic sizes, not measured proportions.

**Exact click build:** Final state: **30 non-title words**.

| Step | Visual action | Exact visible text added or replaced |
|---|---|---|
| 0 | Show capacity frame and anchored inputs | `Context window` / `Standing inputs*` / `Room for reply` / `*When available; schematic.` |
| 1 | Add two history regions | `Earlier conversation` / `Recent messages` |
| 2 | Expand earlier conversation toward capacity; stop before overflow | `Near the limit → compact earlier conversation` |
| 3 | Replace the earlier-history block with a smaller block; leave recent messages | Replace `Earlier conversation` with `Conversation summary`; add `Details can be lost` |
| 4 | Reveal the practical takeaway | `Save decisions in project files` |

**Speaker notes draft:**

> The model has a limited working space. Instructions, conversation, tool results, and the answer all need room. The blank area is deliberate: the answer needs space too. The block sizes are only illustrative.  
>   
> As a coding conversation becomes long, the program may shorten older working history—for example, by replacing it with a summary. Exact behavior depends on the program and configuration. A summary is useful, but it cannot preserve every detail. This is not a rule that the first item always falls out.  
>   
> Put standing working rules in AGENTS.md, requirements in the spec, and the approved steps in the plan. A new conversation can read those files. Starting a new conversation does not recover unsaved details.

**Role-slide decision:** Merge the **useful meaning** of roles into slide 5’s explanation and the handout, not four more large boxes. Preserve the handout glossary:

- **System:** program-supplied instructions.
- **User:** your messages.
- **Assistant:** model responses, including tool requests.
- **Tool:** tool results.

Do **not** assign AGENTS.md to a particular role without verification. Session 2 can briefly recap “system message” when participants actually use it; update its reference to the new slide 5.

**What it replaces:** Current slide 6’s standalone role diagram. No net slide increase.

**Technical caveat:** The precise compaction implementation in opencode 1.19.5 is **unverified**; do not describe the illustrative animation as its exact algorithm.

---

### 4. P0 · Material — Adopt four distinct terms and repair every “app” meaning shift

**Slides:** deck-wide; especially slide 3 (data-n 3), slide 4 (data-n 4), slide 6 (data-n 6), slide 7 (data-n 7), slide 8 (data-n 8), and slide 30 (data-n 26).

**Evidence:** Slide 4 says “the app resends”; slide 7 labels opencode **“App”**; slide 26 (data-n 23), not deck-position slide 23, says **“Your app has two parts.”** Slide 3’s notes move from the financial app to ChatGPT/Copilot apps within one paragraph.

**Why it matters:** Non-programmers can easily believe the financial app they are building is the same program that edits files and runs commands.

**Deck-wide vocabulary:**

| Thing | Audience-facing term | Rule |
|---|---|---|
| LLM | **Model**, defined once as “large language model” | Not “the AI” when a more precise actor matters |
| opencode program | **opencode, our coding agent** | Presenter-only technical synonym: **agent program / harness** |
| ChatGPT and similar interfaces | **Chat service** or **chat product** | Name the product; do not reduce it to “just a screen” |
| Participant deliverable | **Financial app**; later **NISP dashboard and chatbot** | Reserve unqualified “your app” for this deliverable |
| Folder/repository | **`financial-app`** | Keep this exact literal name |

**Full occurrence audit of “app/apps,” including speaker notes:**

- **Slide 1 (data-n 1):** title and notes mean financial deliverable. Keep; define it clearly.
- **Slide 2 (data-n 2):** notes’ “finished app” and “Nothing in the app…” mean financial deliverable. Prefer “financial app.”
- **Slide 3 (data-n 3):** notes’ “when the app needs real NISP numbers” means financial app; subsequent “Those are apps…” means ChatGPT/Copilot; “the app is the screen” oversimplifies those products. Name each actor explicitly.
- **Slide 4 (data-n 4):** title/caption’s “app” means generic chat program; notes mean ChatGPT’s service; final notes return to the classroom chatbot. Teach opencode here; make the classroom-chatbot connection explicit later.
- **Slide 6 (data-n 6):** notes use “app” for software constructing messages, then “opencode and our app” for two separate programs. Replace with those two names.
- **Slide 7 (data-n 7):** title, box, label, and notes’ “app” all mean opencode. Replace every occurrence with **opencode**.
- **Slide 8 (data-n 8):** notes’ “the app runs it” means opencode. Replace.
- **Slide 15 (data-n 14a):** `financial-app` is a literal folder name. Keep.
- **Slide 16 (data-n 14b):** `financial-app` is a literal repository name. Keep.
- **Slide 22 (data-n 20):** notes’ “what the app must do” means financial app. Qualify.
- **Slide 23 (data-n 21a):** “No app yet” and notes’ “whole app” mean financial deliverable. “No dashboard code yet” is clearer.
- **Slide 24 (data-n 21b):** handout prompt’s “start the app” means financial deliverable. Fine once vocabulary is established.
- **Slide 25 (data-n 22):** “phone app” means an out-of-scope mobile deliverable. Keep.
- **Slide 26 (data-n 23):** “Your app” means financial deliverable. Change title opening to **“Your financial app…”**
- **Slide 27 (data-n 24a):** build prompt’s “Build the app” means financial deliverable. Keep tested wording only if required; explain the referent.
- **Slide 30 (data-n 26):** title means financial deliverable, but bullet and notes’ “the app resends” revert to a generic chat program/opencode. Split the actors explicitly.
- **Slide 31 (data-n 27):** notes’ “the app shows data” means financial deliverable. Qualify.
- **Slide 32 (data-n 28):** title and notes mean financial deliverable. Qualify.

No other whole-word `app/apps` occurrences were found in the slide text or JSON speaker notes.

---

### 5. P0 · Material / Animation — Rebuild slide 7 as one top-to-bottom timeline, with each number used once

**Slide:** slide 7 (data-n 7).

**Evidence:** `.review/s1-v2-shots/07_n7_step5.png` shows chronological labels spatially ordered **1, 2, 4, 5, 3, 4**. The second “4” beside the model-bound arrow has no explanation.

**Why it matters:** The presenter is describing a sequence while the picture demands jumping down and back up. Duplicate numbering makes execution and returning the result look like the same step.

### Proposed redesign

**Assertion title:**  
**The model requests an action; opencode checks permissions and runs the tool**

**Layout:** Three fixed vertical lanes, left to right: **opencode | Model | File reader**. Six horizontal rows descend in chronological order. No looping dots or pulsing actor while the presenter explains a different row.

**Exact build:** One click per numbered row; accumulate all six. Final state: **35 non-title words**.

| Step | Arrow/action | Exact new visible text |
|---|---|---|
| 0 | Show lane headings and caveat | `opencode` / `Model` / `File reader` / `Permissions depend on settings.` |
| 1 | opencode → Model | `1 Send context + tools` |
| 2 | Model → opencode | `2 Request docs/spec.md` |
| 3 | opencode → File reader; small gate before arrow | `3 Check permissions; run tool` |
| 4 | File reader → opencode | `4 Return file text` |
| 5 | opencode → Model | `5 Send updated context` |
| 6 | Model → opencode | `6 Answer or request another tool` |

**Speaker notes draft:**

> The model requests the action; opencode carries it out. First, opencode supplies the working context and information about the tools available. The model can ask to read a file—in this example, docs/spec.md.  
>   
> opencode applies the configured permissions. Depending on those settings, it may ask you, allow the action, or refuse it. If permitted, the file reader returns text. opencode adds that result to the working conversation and calls the model again.  
>   
> The next response might answer the user, or it might request another action. “Read this file” is plain-language shorthand here, not the exact technical tool-call syntax. Our financial chatbot will receive selected market data from its back end; it does not need this file-reading tool loop.

**What it replaces:** The “App” box, six disconnected arrow positions, duplicate 4, and fictional-looking `read_file` command quotation.

---

### 6. P0 · Hands-on / Material — Permission language contradicts the promised human control

**Slides:** slide 7 (data-n 7), slide 15 (data-n 14a), and slide 27 (data-n 24a).

**Evidence:** Slide 7 notes reassure, “you stay in the loop.” Slide 15 instructs **“Permission box? Choose Allow once (Enter).”** Slide 27 says **“Agent asks to run a command? Allow it.”** The supplied `prompts/s1.md` says the external-directory request sometimes arose from a mistyped sibling path.

**Why it matters:** The course is teaching bank staff an operational habit. Automatically approving an unexplained external-directory request is the opposite of understanding a permission boundary.

**Fix:**

- Slide 15: **“Permission request? Check the path. Unsure? Ask the facilitator.”**
- Slide 27: **“Check the command and purpose before allowing it.”**
- Notes: “Approve expected actions in the training folder. If the path is outside it, or the purpose is unclear, pause. Do not choose Allow always as a shortcut.”
- Rehearse a recovery path for rejecting the unexpected request; the supplied report explicitly says that TUI rejection path was not tested.

“opencode can ask first” must not become “opencode asks before every action.”

---

### 7. P0 · Material / Storyline — The agent loop ends with a claim, not proof that the task is done

**Slide:** slide 8 (data-n 8).

**Evidence:** Title: “until the task is done.” Exit label: **“Task done.”** Footer: **“Agent: typing.”** Notes are more accurate: “until the model thinks the task is done.”

**Why it matters:** The audience’s essential responsibility is checking output. “Task done” risks equating an agent’s confident response with successful testing.

**Fix:**

**Title:** **opencode repeats model requests and tool actions; you check the result**

Keep the loop but name the actors:

1. **Model proposes**
2. **opencode acts**
3. **Model reads result**

Exit to **“Agent reports completion”**, then a separate **“You test”** box. In notes, add: “The loop can also pause for approval, hit a limit, or fail. A finished response is not a verified result.”

Replace “Agent: typing” with **“Agent: drafts and runs. You: decide and verify.”**

---

### 8. P1 · Storyline / Material — Slide 9 needs the reason, contents, and maintenance cycle—not only repeated sessions

**Slide:** slide 9 (data-n 9).

**Evidence:** `.review/s1-v2-shots/09_n9_step3.png` shows one file broadcasting to three session boxes. It does not show `/init`, revision, review, or Git. Notes say “every session starts empty” and “Anything permanent goes here.”

**Why it matters:** The current picture explains reuse but not why participants should maintain the file or how to distinguish it from the spec and plan.

### Proposed redesign

**Assertion title:**  
**AGENTS.md gives each new conversation the project’s standing brief**

**Layout:** Four successive frames in the same slide space. **Replace** the previous frame at each click; do not accumulate every label. The analogy is an onboarding note for a new colleague.

| Step | Visual | Exact visible text |
|---|---|---|
| 0 | New colleague/conversation beside an absent chat-history bubble | `New conversation` / `No previous chat automatically included` |
| 1 | AGENTS.md supplied to that conversation | `New conversation` / `AGENTS.md` / `The project's standing brief` / `Like onboarding a new colleague` / `opencode supplies applicable project rules` |
| 2 | Open the brief into three content areas | `AGENTS.md` / `Project purpose` / `How to run and check` / `Working rules` / `Explain before acting` / `Not secrets. Not a chat transcript.` |
| 3 | Show a left-to-right lifecycle | `/init → Starter brief` / `Decisions or repeated corrections → Ask agent to update AGENTS.md` / `Review → Commit → Next conversation` / `Today: ask the agent; don't edit by hand` |

Body counts by frame: **7 / 17 / 19 / 28 words**.

**Speaker notes draft:**

> AGENTS.md is the project’s standing brief. Think of a new colleague joining the project: they need a short onboarding note, not every conversation the team has ever had. A fresh conversation does not automatically include the previous chat. opencode can supply the applicable saved project rules.  
>   
> Keep the brief focused: what the project is for, how to run and check it, and working rules that should apply repeatedly. Today’s example is “Explain what you will do in plain business language before doing it.” Requirements for a feature belong in the spec; its approved build steps belong in the plan. Secrets do not belong in this file.  
>   
> `/init` produces a starting brief, based on what the agent finds. In an empty folder, it will be sparse. It is not a one-time form that updates itself. After an enduring decision—or when you keep correcting the same behavior—ask the agent to propose an update. Read the change, then commit it. The next conversation can use the revised brief.

**What it replaces:** The floating file and three identical red session boxes. The new lifecycle conveys persistence **and maintenance**.

**Confidence:** `/init` creating a starter file is supported by the supplied test report. Exact automatic inclusion behavior across all opencode configurations is **unverified**.

---

### 9. P0 · Material — “Never edit manually” would be a false technical prohibition

**Slides:** slide 9 (data-n 9) and slide 16 (data-n 14b).

**Evidence:** The current deck does not explain a manual-edit policy; slide 16 already models asking the agent to add a rule. The owner asks for a reason participants should not edit by hand.

**Why it matters:** AGENTS.md is a text file. Participants should not learn that an ordinary manual edit intrinsically damages it, or that an agent-written edit is intrinsically safe.

**Fix:** Make this an explicit **course recommendation**:

> **“For today’s exercises, ask opencode to update AGENTS.md, then review the change.”**

**Suggested notes:**

> You can edit this text file yourself. Today, use the agent so you do not need to learn the file’s formatting and can state the rule in plain language. Asking the agent can help preserve the existing structure, but it can still make mistakes. We review either way. Git makes a committed change reviewable and reversible regardless of who typed it.

Do not claim:

- The agent cannot break the file.
- Manual editing loses Git history.
- The update is automatically committed.
- Updating the file guarantees perfect compliance.

---

### 10. P0 · Material — Change the quiz from “empty memory” folklore to a maintained-rule decision

**Slide:** slide 10 (data-n 10).

**Evidence:** Answer: **“Nothing carries over between sessions except files, and AGENTS.md is read every time.”**

**Why it matters:** A fresh conversation is not literally empty: it may receive operating instructions and project context. A resumed conversation differs from a fresh one. The current answer also implies that the time interval “overnight” causes forgetting.

**Fix:**

**Assertion title:** **Save recurring project rules so a new conversation can use them**

**Question and choices — 29 body words:**

> A new conversation misses your “explain first” preference. What should you do?  
> **A** Repeat it every time  
> **B** Ask opencode to update AGENTS.md; review and commit  
> **C** Change models

On reveal, **replace** the choices with:

> **B — Save standing project rules in AGENTS.md.**  
> Ask opencode to update it.  
> Review the wording, then commit.  
> A fresh conversation can receive the saved rule.

**Notes:** “The issue is a new conversation, not the agent being tired or a clock striking midnight. If a saved rule still seems absent, check the project folder and loaded instructions rather than assuming AGENTS.md guarantees obedience.”

---

### 11. P1 · Hands-on — Close the lifecycle loop during Run 1, not only in explanation

**Slides:** slide 15 (data-n 14a) and slide 16 (data-n 14b).

**Evidence:** Slide 16’s notes say to open AGENTS.md and check the exact rule, but the slide itself jumps from the edit prompt to committing everything and creating a repository. Notes label the GitHub prompt **“UNTESTED.”** The supplied tests used a **local bare repository**, not the participants’ real GitHub setup.

**Why it matters:** “Ask → review → commit” will not become a habit if the hands-on run visibly models only “ask → push.”

**Fix:**

- Keep the tested rule-addition prompt unchanged.
- Insert a visible checkpoint between prompts:  
  **“Open AGENTS.md. Check your rule before committing.”**
- State the scope of the first checkpoint:  
  **“The file is saved; it is not shared until pushed.”**
- Rehearse account sign-in, repository creation, visibility, and push on Windows and Mac before treating this run as verified.
- After the dashboard exists, use a short maintenance demonstration: ask the agent to update the run/check instructions, inspect the change, and commit it.

Do not promise that `/init` in an empty folder already contains meaningful future run commands.

---

### 12. P1 · Storyline / Quality — The “four ways” should be four jobs, not a staircase of increasing sophistication

**Slide:** slide 17 (data-n 15).  
**Numbering clarification:** This is the “four ways” slide. Deck-position slide 16 is Run 1; data-n 16 is deck-position slide 18.

**Evidence:** `.review/s1-v2-shots/17_n15_step3.png` draws Prompt → AGENTS.md → Skill → Workflow as ascending steps, with a person standing on AGENTS.md.

**Why it matters:** The picture implies that skills replace prompts or workflows outrank project rules. They are complementary, and a workflow can itself be supplied through a prompt or skill.

**Fix:**

**Title:** **Choose instructions by their job: this task, project rules, expertise, or sequence**

Use four **equal-height cards**, not steps:

- **Prompt — This task**
- **AGENTS.md — Standing project rules**
- **Skill — Reusable task guidance**
- **Workflow — Repeatable sequence**

Add a small footer: **“They can work together.”**

Reveal Prompt and AGENTS.md first, labelled **“Used today”**; then Skill; then Workflow with **“Session 3.”**

**Notes:** “These are four useful patterns, not four mutually exclusive technical containers. You used a prompt to ask for an AGENTS.md update. A workflow can use project rules and skills.”

---

### 13. P0 · Material / Quality — Mark the model illustration as illustrative and remove “That is all it does”

**Slide:** slide 3 (data-n 3).

**Evidence:** The notes say **“That is all it does”** and “predicts what sounds right, not what it has checked.” The screenshot `03_n3_step3.png` presents three unlabelled probability-like bars for NISP, Indonesia, and Bank.

**Why it matters:** The numerical-looking graphic appears measured, but no model output or probabilities support it. The wording also undermines the later teaching that the model can reason over supplied tool evidence.

**Fix:**

- Keep the accessible core: generation proceeds in small pieces of text, often smaller than words.
- Add **“Illustration—not measured probabilities.”**
- Prefer a neutral sentence completion to the repeated ticker example.
- Replace the notes with:

> A language model generates text one small piece at a time, using patterns learned during training and the context supplied now. Fluent wording is not proof that a statement is correct. For current NISP prices, we supply data and check the answer against that source.

This teaches the practical limitation without claiming the model is incapable of using checked evidence.

---

### 14. P0 · Material — Repair the “whole conversation” and `/new` absolutes at both ends of the deck

**Slides:** slide 4 (data-n 4), slide 5 (data-n 5), and slide 30 (data-n 26).

**Evidence:** Slide 4 says **“whole conversation every turn”**; notes say **“each request starts from zero”** and “The model does not keep a file about you.” Slide 5 calls `/new` a fix. Slide 30 repeats the unqualified resend claim.

**Why it matters:** Model-call state, product memory, saved conversations, and provider data retention are different issues. “Stateless” must not sound like a privacy or non-retention guarantee.

**Fix:**

**Slide 4 title:**  
**opencode supplies earlier messages so the model can follow the conversation**

Keep the growing-message example, but add **“Simplified short conversation.”** Notes should say:

> The model uses the context supplied for this call; it does not independently retrieve an earlier call. The program manages conversation history. A long history may be shortened. This is separate from whether a service stores chats or provides a memory feature.

**Session-management notes:**

> Start a fresh conversation when moving to a separate task, after saving important decisions. For unfinished work, point the new conversation to the spec, plan, and relevant files. `/new` clears the conversation context; it does not retrieve what was never saved.

**Slide 30 recap replacement:**

- **opencode supplies the model’s working context**
- **AGENTS.md preserves standing project rules**
- **You review plans and verify results**

## 3. Add / cut recommendations

- **Add one small vocabulary key early:** Model / opencode / Financial app. Reuse these labels consistently; do not introduce “harness” as another term participants must memorize.
- **Add the AGENTS.md review checkpoint to Run 1.** It converts the owner’s handling recommendation into observable practice.
- **Add one maintenance example after building:** “Update AGENTS.md with the agreed way to start and check this project.” This demonstrates that the brief evolves.
- **Cut the falling-rules conveyor and `/new` “fix.”** They teach the wrong causal story.
- **Cut the standalone four-role animation, but retain the glossary in the handout and a brief Session 2 recap.** Use its slide slot for context capacity; keep 32 slides.
- **Cut automatic permission-approval instructions.** Teach expected path, purpose, and “pause if unsure.”
- **Do not add a universal “never manually edit” rule.** Present the agent-mediated approach as the course’s recommended workflow, with human review and Git—not agent infallibility—as the safeguards.