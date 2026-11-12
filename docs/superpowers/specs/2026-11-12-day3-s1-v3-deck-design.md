# Day 3 · Session 1 deck v3 — design (repair + targeted reorder)

Status: draft for approval · 2026-11-12
Input: `.review/day3-s1-v2-review-report.md` (synthesis of 5 reviews; raw reviews `.review/r-*.md`; screenshots `.review/s1-v2-shots/`).
Source deck: `decks/day3-s1-v2.html` (32 slides). Output deck: `decks/day3-s1-v3.html`.
Tags: *(user)* = decided by the owner · *(call)* = coordinator's call, correctable.

Finding IDs (M1, H1, S3, R1, A2 …) refer to the review report. Slide numbers "v2 N" mean the deck position "N / 32" in v2.

---

## 1. Intent

The v2 deck looks good, but it teaches a partly wrong picture of how a coding agent works (slides 4–10), builds unsafe habits in the runs (click Allow, paste errors with secrets, push without saying private), and shows the participants' actual job (the workflow) too late. The audience is bank business users with no coding background. The owner's top rule: **no misleading or ambiguous content or knowledge.**

v3 fixes every P0 finding, rebuilds the three slides the owner flagged (v2 5, 7, 9), applies one vocabulary across the deck, and reorders the places where the order hurts understanding. The look (Swiss Modern: white/black/red #ff3300, Archivo, Nunito, JetBrains Mono), the NISP example and the three-run structure stay.

## 2. Goals, non-goals, anti-goals

**Goals**
- No slide, label or speaker note teaches a wrong or absolute claim that is listed as P0 in the report.
- Slides 5, 7 and 9 are redesigned as in §6.
- The workflow uses the brief's five names everywhere *(user)*: **Interview → Plan (Approve / Edit / Reject) → Execute → Test / Debug → Iterate**.
- The participant's job appears near the start; checks come before the decision they check; debugging comes before the build.
- Hands-on time rises from 77 to about 91 of 180 minutes.
- The speaker notes match the slides.

**Non-goals**
- No new outline from scratch (scope C was rejected *(user)*).
- No new visual style, fonts or deck engine.
- No end-to-end rehearsal of the runs, handout, recovery card or checkpoint hosting (§9 lists them as delivery blockers outside this work).
- No changes to Sessions 2 and 3, except the one cross-reference in §8.

**Anti-goals** (failure even if the deck "works")
- Replacing one absolute claim with another ("opencode never drops anything", "Plan mode is safe").
- Changing the wording of a **tested** prompt (`prompts/s1.md`). Tested prompts stay verbatim; only their labels and the text around them change.
- Running out of word budget by shrinking the type.

## 3. Constraints

- Project deck rules in `AGENTS.md`: assertion titles, ≤ 40 visible words per reveal step on teaching slides, ≤ 60 on run slides (prompts in boxes don't count), never shrink type to fit, and a per-slide report of title, word count and any exception.
- One self-contained HTML file. Same runtime: `[data-step]` click reveals, a `.choices` reveal on quiz slides, speaker notes in `#notes-data` JSON keyed by `data-n`, ← undoes a reveal, 1920×1080 stage.
- Motion: continuous loops only where repetition is the concept (the agent loop). Everything else runs once and settles. All motion is covered by `prefers-reduced-motion`.
- Session length stays 180 minutes, with no break.

## 4. Approaches

| | Approach | Trade-off |
|---|---|---|
| A | Repair in place: fix the P0s and redesign 5/7/9, keeping order and 32 slides | Fastest, but leaves the order problems (workflow late, quiz after the decision, debug after the build, 77 min of hands-on) |
| **B** | **Repair plus targeted reorder** *(user, picked)* | Moves 4 slides, splits 1 run slide, replaces 1 slide; the approved outline is mostly kept |
| C | Full restructure around a business-task-first outline | Best story, but needs a new outline approval and re-copy of everything |

Other owner decisions:
- Workflow names: the brief's five steps.
- AGENTS.md editing: a **recommendation with a reason**, not a rule.
- Model names, GitHub account and AI-service naming: **leave as is** (`[FAST MODEL]` / `[SMART MODEL]` placeholders stay; participants use the GitHub account they create in Run 1; no provider or bank-approved name is added for the chatbot's service). "Leave as is" means no new name. It does not keep the wrong v2 phrase "the LLM in backend/.env": v3 uses the generic term **AI service** everywhere (finding M7).

## 5. v3 slide sequence (headlines) and timing

`data-n` values are new and sequential (1…33) so notes, file names and screenshots line up. "From" gives the v2 deck position.

| # | Headline (assertion title) | From | Change | Min |
|---|---|---|---|---|
| **Opening** | | | | **10** |
| 1 | Build your first AI Financial App | v2 1 | none | 2 |
| 2 | Today you direct opencode to build a NISP dashboard and chatbot, without writing code | v2 2 | title names opencode; notes say "latest available price" | 5 |
| 3 | Your job today: interview, approve the plan, then test what the agent builds | v2 21 | **moved**; 5 workflow steps (§6.5); brackets "Run 2" / "Run 3" | 3 |
| **How a coding agent works** | | | | **27** |
| 4 | An LLM writes its answer one small piece of text at a time | v2 3 | label the bars "Illustration"; fix notes (M13) | 3 |
| 5 | The model doesn't remember earlier requests; opencode sends the context it needs | v2 4 | title, caption and notes rescoped (M4); Turn-1 arrow fixed (A1) | 3 |
| 6 | On every turn, opencode sends the model a stack: rules, skills, the chat so far, your message | v2 5 | **redesign** §6.1 | 4 |
| 7 | The context window has a limit, so old chat gets summarised; save decisions in files | v2 6 | **replaces** the roles slide; §6.2 | 3 |
| 8 | The model asks for a tool; opencode checks permission and runs it | v2 7 | **redesign** §6.3 | 4 |
| 9 | A coding agent repeats model decisions and tool actions, then you check the result | v2 8 | title, exit boxes and punch line (M6) | 3 |
| 10 | AGENTS.md is the project's standing brief, so keep it current | v2 9 | **redesign** §6.4 | 4 |
| 11 | Check: a new conversation ignored your preference. What do you do? | v2 10 | new choices (§6.4) | 3 |
| **Models and Git** | | | | **12** |
| 12 | Use a quick model for small edits and a stronger one for planning and debugging | v2 11 | title softened; placeholders stay *(user)*; car/truck loops run once (A5) | 3 |
| 13 | On supported models, higher effort lets the model reason more before answering | v2 12 | title, caption, one-click dial, reduced-motion fix (M11, A3, A4) | 2 |
| 14 | Everyone works on a local copy and shares through GitHub | v2 13 | punch line "Saving alone doesn't upload your work" | 3 |
| 15 | A commit is a save point on your laptop; push copies it to GitHub, pull brings changes back | v2 14 | three states saved → committed → pushed; `.env` shown as left out (M12) | 4 |
| **Run 1** | | | | **26** |
| 16 | Run 1a: sign up to GitHub and draft AGENTS.md with /init | v2 15 | title (R1); permission line (H1); setup line (R2) | 12 |
| 17 | Run 1b: add your rule, check it, then push to a private repository | v2 16 | title (R1); check step (R3); "private" in Prompt 2 (H2) | 14 |
| **Skills** | | | | **11** |
| 18 | Choose how to instruct the agent by the job: this task, project rules, expertise or a sequence | v2 17 | equal cards instead of stairs (S9) | 3 |
| 19 | The agent sees each skill's name and description, and loads the full skill when it decides one fits | v2 18 | wording (M10); card stays inside the box, real text (A2) | 4 |
| 20 | A brainstorming skill makes "ask questions first" a repeatable habit | v2 19 | "Illustration" label; panels show short real text (M9) | 4 |
| **Run 2 — Interview and plan** | | | | **35** |
| 21 | An agent builds what it guesses you want, so interview first | v2 20 | "make it ask first" → "interview first" | 3 |
| 22 | The interview produces a spec (what and why); the plan says how, and you approve, edit or reject it | v2 22 | keep "Spec = PRD" *(user, from v2 edit)* | 4 |
| 23 | Check: approve, edit or reject these three plans | v2 25 | **moved before Run 2b** (S3); subtler plans (S6) | 4 |
| 24 | Run 2a: interview for the dashboard and save the spec | v2 23 | title (R1); "Up to five questions" (R7); tech line boxed as course-supplied (S5) | 12 |
| 25 | Run 2b: get the plan, approve, edit or reject it, then save it | v2 24 | title (R1); "stay in this conversation" (R4); Plan-mode wording (M14) | 12 |
| **Run 3 — Execute, test, iterate** | | | | **49** |
| 26 | Your financial app has a screen, a back end, a data source and an AI service | v2 26 | `.env` fix (M7); vocabulary | 4 |
| 27 | When something breaks, remove secrets, paste the error, and ask the agent to explain it | v2 29 | **moved before Run 3** (S4); redaction step (H4) | 4 |
| 28 | Run 3a: build the dashboard and check its numbers | v2 27 | title (R1); permission line (H1); acceptance list (S13, M16) | 15 |
| 29 | Run 3b: protect the key, then interview and plan the chatbot | v2 28 | **split** (S7); secrets first (H3); spec prompt fixes (M7, M8) | 12 |
| 30 | Run 3c: build and test the chatbot, then push without secrets | v2 28 | **split** (S7); tests and pass criteria (M8, S13); push checks the file list (H3) | 14 |
| **Close** | | | | **10** |
| 31 | You built a financial app by directing an AI and checking its work | v2 30 | recap fixed (M4, M12); 5 steps; finish check (S12) | 4 |
| 32 | Questions | v2 31 | none | 5 |
| 33 | Next session: your app stores price history and the chatbot reads reference pages | v2 32 | title and notes (M15) | 1 |

Total: 180 min. Hands-on run slides: 12 + 14 + 12 + 12 + 15 + 12 + 14 = **91 min** (v2: 77). 33 slides (v2: 32).

## 6. Redesigned slides

Visible text below is the on-slide wording. The builder may tighten wording if the meaning stays the same and the word budget holds.

### 6.1 Slide 6 — what the model reads on every turn (owner's slide 5 request)

Layout: a vertical stack of five rows on the left, read top to bottom; one arrow to a red **Model** box on the right. Colour key for slides 5–10: red = the model, black = opencode and its rules, grey/white = tools and data *(call)*.

| Click | Reveal | Visible text |
|---|---|---|
| 0 | Model box, empty stack frame, footnote | `opencode → Model` · `Simplified view` |
| 1 | row 1 | `System prompt — opencode's own rules` |
| 2 | row 2 | `AGENTS.md — your project rules` |
| 3 | row 3 | `Skill list — names and descriptions only` |
| 4 | row 4 (grey, visibly taller) | `Conversation so far — your messages, its replies, tool results` |
| 5 | row 5, then the stack is sent to the Model once | `Your new message` |
| 6 | brackets | rows 1–3: `Sent every turn`; row 4: `Grows` |

Notes must say: this is a teaching picture, not the exact request format. opencode rebuilds rows 1–3 for every call to the model, including calls after a tool result (verified in the opencode v1.19.5 source, `session/prompt.ts` and `session/instruction.ts`). The model only reads a file if a tool brings it into row 4. Messages carry roles (system, user, assistant, tool); the full role glossary moves to the handout.

### 6.2 Slide 7 — context has a limit (replaces v2 slide 6)

The same stack sits inside a fixed "Context window" frame with blank room at the bottom labelled `Room for the reply`.

| Click | Reveal | Visible text |
|---|---|---|
| 0 | frame, rows 1–3 in place, short row 4, room for reply | `Context window` · `Room for the reply` |
| 1 | row 4 grows toward the limit | `Long chat → near the limit` |
| 2 | the older part of row 4 shrinks into one block; rows 1–3 don't move | `Older chat → a short summary` · `Rules stay` |
| 3 | small warning | `Details can be lost` |
| 4 | takeaway bar | `Rules → AGENTS.md · requirements → spec · steps → plan. /new starts clean, so save first.` |

Nothing falls out of the frame and nothing labelled "rules" moves. Notes: how opencode shortens history depends on its settings; a summary keeps the gist, not every detail.

### 6.3 Slide 8 — tool calling (owner's slide 7 request)

Three lanes, left to right: **opencode** (black, labelled `on your laptop`) · **Model** (red) · **Tool: read a file** (white). Six rows run top to bottom, one per click, each with a number badge used once and a label above its arrow.

1. opencode → Model: `Your message + list of tools`
2. Model → opencode: `Please read docs/spec.md`
3. opencode → Tool: `Check permission, then run` (small gate icon on the arrow)
4. Tool → opencode: `File text`
5. opencode → Model: `Conversation + file text`
6. Model → opencode: `Answer, or another tool request`

Motion: each arrow draws once. No travelling packet loop and no pulsing model.
Notes: the model never touches your laptop; opencode does, within its permission settings. Some actions run without asking, depending on settings. The financial app's chatbot does not use tools. "Please read" is plain-language shorthand, not the real tool syntax.

### 6.4 Slide 10 — AGENTS.md (owner's slide 9 request) and slide 11 quiz

Analogy: **an onboarding note for a new colleague**. Each click replaces the previous frame instead of stacking on it.

| Click | Frame | Visible text |
|---|---|---|
| 0 | a new-conversation card with an empty chat bubble | `New conversation` · `Yesterday's chat isn't included` · `Like a new colleague on day one` |
| 1 | AGENTS.md slides into the card | `AGENTS.md is handed over every turn` · `The project's standing brief` |
| 2 | AGENTS.md opens into "in" and "out" lists | In: `What the project is` · `How to run and check it` · `Working rules`. Out: `Passwords and keys` · `Chat logs` · `Feature details (→ spec)` |
| 3 | a lifecycle loop, left to right | `/init drafts it → you spot a lasting rule or a repeated correction → ask the agent to update it → read the change → commit` |
| 4 | footer | `Today: ask the agent to edit AGENTS.md, then review it.` |

Speaker notes must give the reason *(user: recommendation, not a rule)*: "AGENTS.md is a plain text file, so you can edit it yourself. Today we ask the agent instead: you say the rule in plain words, the agent keeps the file's structure and wording consistent, and we avoid accidental deletions. It can still make mistakes, so read the change. Git makes the change reviewable and reversible whoever typed it." Also: "Rules guide the agent; they don't guarantee it obeys, so still check its work."
Never claim that manual edits break the file, or that the agent's edits are always right.

**Slide 11 quiz:**
- Question: "A new conversation ignored your 'explain first' preference. What do you do?"
- Choices: A `Repeat it at the start of every chat` · B (correct) `Ask opencode to add it to AGENTS.md, review it, commit` · C `Switch to a stronger model`
- Reveal: `B — A new conversation doesn't include old chats. AGENTS.md is sent every turn.`

### 6.5 Slide 3 — your job today (the v2 workflow slide, moved)

Five boxes left to right: **Interview · Plan · Execute · Test / Debug · Iterate**.
- Under Plan: a chip `Approve / Edit / Reject`.
- Under Interview: small text `→ docs/spec.md`.
- A square return arrow from Iterate back to Plan (keep the v2 drawing style).
- Brackets: `Run 2` under Interview + Plan; `Run 3` under Execute → Iterate.
- Step reveals as in v2.

Notes: "We call it an interview: the agent asks, you answer. Some skills call this brainstorming."
The same five names appear on slides 24 to 31: run-slide "you are here" chips, the Run 3b/3c mini-map, and the recap.

## 7. Changes to other slides (all must be made)

### Vocabulary (V1), deck-wide including notes

| Thing | Say | Avoid |
|---|---|---|
| LLM | **the model** (defined once on slide 4: "LLM = large language model") | "the AI" where it matters who acts |
| opencode | **opencode** (first mention: "opencode, our coding agent") | "the app" |
| ChatGPT and similar | **chat products** | "the app is just the screen" |
| What participants build | **your financial app** (dashboard + chatbot) | a bare "app" for opencode |

`financial-app` stays as the literal folder and repo name. `r-redesign.md` finding 4 lists every v2 occurrence of "app".

### Per-slide fixes (v3 numbers)

- **2:** notes say "latest available price", not "live" (M16).
- **4:** notes drop "That is all it does"; add "fluent is not the same as correct — we give it real data and check" (M13).
- **5:** caption `opencode resends it. The model doesn't remember.`; notes scope "whole conversation" to our chatbot and add "stateless doesn't mean the service stores nothing" (M4). Fix the Turn-1 arrow, which never appears (A1).
- **9:** exit boxes `Agent reports back` → `You test`; punch line `Agent: proposes and does. You: decide and check.`; notes add "it can also stop for an error, a limit or a question" (M6). The loop dot keeps looping; this is the one slide where repetition is the concept.
- **12:** title as in §5; placeholders stay. The car and truck run once, then stop (A5).
- **13:** caption `Ctrl+T cycles the options your model offers`; one click moves the dial from low to high and it stays; add `.eff-hand`, `.eff-ptr` and `.eff-bar` to the reduced-motion rule (A3, A4).
- **14:** punch line `Saving alone doesn't upload your work.`
- **15:** add a three-state strip `Saved on laptop → Committed (save point) → Pushed (on GitHub)`, with `.env` drawn as deliberately left out. Notes: "a commit records the files included in it; ignored files such as .env are not in it" (M12).
- **16 (Run 1a):** permission line `Permission box? Read the path. Inside financial-app? Allow once. Anything else or unsure? Raise your hand. Never "Allow always".` (H1). Setup line `opencode must be open in the financial-app folder (the path shown ends in financial-app).` (R2).
- **17 (Run 1b):**
  - Prompt 1 stays verbatim (tested).
  - Insert the step `Open AGENTS.md. Is your rule there? Then send Prompt 2.` (R3).
  - Prompt 2 adds **private** *(call)*: `Commit all files in this project with the message "Start project". Create a new private GitHub repository called financial-app and push to it. Tell me if I need to sign in.` (still UNTESTED).
  - "You should see": `A private financial-app repo on github.com with AGENTS.md.`
- **18:** four equal cards: `Prompt — this task` · `AGENTS.md — standing project rules` · `Skill — reusable expertise` · `Workflow — a repeatable sequence` (with the `Session 3` chip). Footer `They work together.` (S9).
- **19:** wording as in §5. The request bubble gets text: `Help me plan a dashboard`. Each skill row gets a one-line description. The loaded card lands fully inside the context box. The shelf is labelled `Not loaded`. Notes: "you can also name a skill; look for the 'skill loaded' line" (M10, A2).
- **20:** label `Illustration`. The left panel shows a 3-line straight answer; the right panel shows 3 short questions, then a 3-line summary. Notes: "the same habit can be asked for in a prompt; a skill makes it repeatable" (M9).
- **21:** title as in §5.
- **23 (quiz, moved):** plans become `Plan 1: follows the spec.` · `Plan 2: follows the spec, plus a login screen nobody asked for.` · `Plan 3: shows a chart, but for the wrong stock (BBRI).` Answer A stays `Approve 1 · Edit 2 · Reject 3`. Replace distractors B and C with plausible ones: `Approve 1 · Approve 2 · Edit 3` and `Edit 1 · Reject 2 · Reject 3`. Notes drop "lazy choice" (S3, S6).
- **24 (Run 2a):**
  - Prompts stay verbatim (tested). Label Prompt 1 `Prompt 1 (interview)`.
  - "You should see" becomes `Up to five questions, one at a time, a summary, then docs/spec.md. No code yet.` (R7).
  - The tech sentence inside Prompt 2 stays (tested). Add a small label under the box: `The last sentence is technical setup from the course — copy it as is.` (S5).
- **25 (Run 2b):**
  - Add `Stay in this conversation — no /new until the plan is saved.` (R4).
  - Step 2: `Check it against your spec: only price, change and 1-year chart? Nothing extra? Then approve, edit or reject.`
  - Notes replace "Plan cannot edit files" with "Plan mode is for proposing, not changing the app. Check the footer says plan." (M14).
- **26:**
  - Title as in §5.
  - External data box `Yahoo Finance: NISP data`; the back end shows `FastAPI · yfinance · 8000` (yfinance is a library on the laptop; final review).
  - The right-hand red box becomes `AI service (LLM)`, outside the laptop.
  - A small card beside the back end: `backend/.env — service address, model name, secret key. Not the AI.` Remove the padlock-in-label.
  - Label the screen `Screen (in your browser)`.
  - Notes: "localhost means this laptop; 5173 and 8000 are the ports we chose" (M7).
- **27 (debug, moved):** four boxes `Copy the error` → `Remove keys and private data` → `Ask: "Explain in plain words, then fix it."` → `Repeat the check that failed`. Source chips stay. Notes: "a quiet agent is not always stuck; check before re-sending" (H4).
- **28 (Run 3a):**
  - Prompt stays.
  - Replace "Agent asks to run a command? Allow it." with `It asks to run a command? Read it. Installing or starting the app inside financial-app is expected. Anything else? Raise your hand.` (H1).
  - "You should see" becomes the checklist `NISP.JK · prices in IDR · date and source shown · 1-year chart`.
  - The build prompt itself is unchanged. The Iterate prompt is a separate step shown on the slide: if the date/source isn't shown, participants use it as their **Iterate** step: "Show the date and source of the price under the price card." *(call — this gives every participant a real iteration)*.
- **29 (Run 3b):**
  1. Prompt (new, UNTESTED): `Add .env to .gitignore and create backend/.env.example with LLM_BASE_URL, LLM_API_KEY and LLM_MODEL and no values. Don't create or open backend/.env.`
  2. Step: `Copy backend/.env.example to backend/.env and fill in the class details. Never paste the key into the chat.`
  3. Spec prompt (UNTESTED, revised): `Add a chatbot to docs/spec.md. The page sends the whole message list each turn. The backend adds NISP's latest available price and the last year of daily closes, with dates, then calls the AI service using the settings in backend/.env (LLM_BASE_URL, LLM_API_KEY, LLM_MODEL). If the data doesn't answer the question, it says so. No buy, sell or hold advice. No tool calling. Don't build yet.` (M7, M8)
  4. Plan → approve, edit or reject → save, as in Run 2 (the mini-map uses the five names).
- **30 (Run 3c):**
  - Build prompt (the text quoted here is authoritative; it goes on the slide and into `prompts/s1.md` as untested): `Approved. Build the chatbot from docs/plan.md, then tell me how to open it.`
  - Tests with pass criteria:
    - `What is NISP's latest price?` → matches the price card and its date.
    - `Say "My name is Rina", then ask "What is my name?"` → Rina (memory). *(final review: the NISP question passes even without memory)*
    - `What was the close on <a date last month>?` → matches the chart, or says it has no data.
    - `Should I buy NISP?` → no buy, sell or hold advice.
  - Push in two prompts (UNTESTED; final review: one prompt let the agent push before the participant read the list): `List the files you would commit, and point out anything that looks like a key or password. Don't commit or push yet.` — the participant reads the list and stops on backend/.env or a key — then `Commit those files with the message "NISP dashboard and chatbot" and push to GitHub.` (H3)
  - Add `Key leaked? Tell the facilitator — the key must be replaced.`
- **31:**
  - Bullets: `The model doesn't remember; opencode sends the context` · `AGENTS.md: the project's standing brief` · `Commit and push save your work to GitHub` · five-step chips.
  - Add a finish check: `Dashboard opens · price check passes · chatbot check passes · latest commit on GitHub — or checkpoint s1-chatbot` (S12).
- **33:** title as in §5. Notes: "today's app fetches prices when asked and stores none; next time we save price history and give the chatbot reference pages to read — the model itself is not retrained" (M15).

### Animation rules (A5, A6)

- Allowed continuous loops: the slide 9 agent-loop dot (the only loop on slides 4–11); the slide 32 drifting shapes (the owner's own design); text carets.
- Everything else: `flow` dashes, travelling packets, `pulse`, `float`, the cars and the truck run a few times (or once), then stop, on the active slide.
- Every animated class is listed under `prefers-reduced-motion`.

## 8. Related documents to update

- `docs/outlines/day3-s1-v3.md`: the headline list from §5, with a "changes from v2" header.
- `docs/copy/day3-s1-v3.md`: visible text, build steps and notes for all 33 slides, plus the word-count report required by `AGENTS.md`.
- `docs/superpowers/specs/2026-11-11-day3-design.md` §3 (S1 objectives):
  - objective 1: "the model doesn't remember; the agent sends the context";
  - objective 3: "say what the model reads on every turn and what tool calling does" (the roles move to the handout);
  - objective 7: rename the workflow to the five steps.
- `docs/outlines/day3-s2-v2.md` item 13 (line 34): "links back to S1 message roles" → "links back to S1 slide 6 (system prompt row)".
- `docs/project-log.md`: one entry for the review and one for the v3 build.
- `prompts/s1.md`: add every UNTESTED prompt from §7 under a clearly marked "untested (v3)" heading: slide 17 Prompt 2, slide 28 build prompt and Iterate prompt, slide 29 `.env.example` prompt and spec prompt, slide 30 build prompt and push prompt. Tested prompts are unchanged.

## 9. Open items and delivery blockers (not part of this build)

- `[FAST MODEL]` / `[SMART MODEL]` placeholders on slide 12 *(user: leave as is)*.
- The GitHub account policy stays as in v2, and no specific name is given to the chatbot's AI service *(user: leave as is)*; v3 calls it the generic "AI service" (§4). Coordinator's call: Prompt 2 says **private** (see §7, slide 17). If the owner disagrees, drop the word.
- UNTESTED prompts (slides 17, 28, 29, 30) need an end-to-end rehearsal on Windows and Mac before class, including real GitHub sign-in.
- The handout, recovery card and checkpoint links don't exist yet.

## 10. How we check it (acceptance)

1. Render every slide at every click step at 1920×1080 and 1280×720: nothing overflows the stage, no text under 28 px, and each `data-step` causes a visible change.
2. Lint: each run slide's prompt text equals `prompts/s1.md` for tested prompts; no visible text or note matches the banned list `Allow it`, `the LLM in backend/.env`, `starts from zero`, `Nothing carries over`, `cannot edit files`, `Task done`, the whole word `live`, `learns the rules` (checked in visible text and notes only), and no bare "the app" used for opencode.
3. Workflow names: on the workflow chips, the run mini-maps and the recap, only the five names appear. Elsewhere "spec" stays as a document name, and "brainstorming" may appear as a skill name and in the tested prompt.
4. Word budget report per slide, as `AGENTS.md` requires.
5. Timing table sums to 180; run-slide time is ≥ 90.
6. An independent review (same 5 lenses, read-only) of the v3 deck finds no P0.

## 11. Left to the builder

- Exact coordinates, sizes and easing; reuse existing v2 CSS classes and helpers.
- How the "stop after a few loops" is implemented (iteration count or a class removed after a timeout).
- Fine wording, within word budgets and without changing the meaning in §6–7.
- Whether to build from an extracted fragment pipeline or to edit the single HTML file directly (the old `.scratch` pipeline no longer exists).

## Review Decisions

- Slide 17 Prompt 2 (the GitHub push) is not in `prompts/s1.md`; v2 marked it UNTESTED, so adding "private" does not change a tested prompt. The tested prompts that must stay verbatim are the Run 1 rule prompt and the Run 2 prompts (interview, spec, plan, save) (lines 22, 67, 97, 119, 147 of `prompts/s1.md`). The Run 3a build prompt is also untested, but v3 keeps its v2 wording.
