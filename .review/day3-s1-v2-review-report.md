# Review report — `decks/day3-s1-v2.html` (Day 3 · Session 1)

Date: 2026-11-12. Five independent reviewers (gpt-6.1-sol, high thinking): accuracy, storyline, hands-on, visuals/animation, redesign of slides 5/7/9. Synthesised by the coordinator; screenshots checked for slides 4, 5, 7, 9, 18.
Raw reviews: `.review/r-accuracy.md`, `r-storyline.md`, `r-handson.md`, `r-visuals.md`, `r-redesign.md`. Screenshots: `.review/s1-v2-shots/` (104 click states).

Slide numbers = the "N / 32" shown on the slide; data-n in brackets.
"Agreed by" = how many of the 5 reviewers raised it independently.

Severity:
- **P0** — wrong, misleading or ambiguous knowledge, or an unsafe habit. Fix before teaching.
- **P1** — material or storyline weakness: the idea is right but poorly taught, missing, or in the wrong place.
- **P2** — visual or animation problem that hurts clarity.
- **P3** — polish.

Verification note: the accuracy reviewer checked opencode's source at tag v1.19.5 (commit 810c0eb). Items marked *(source-checked)* rest on that. That is a source read, not a classroom run.

---

## Summary

The deck looks good, the example (NISP) runs all the way through, and the three-run structure works. But the concept block (slides 4–10) teaches a mental model that is partly wrong, and the hands-on runs teach two unsafe habits: clicking Allow, and pasting errors without removing secrets. Your three flagged slides (5, 7, 9) are confirmed problems. Fix all P0 items first, then the storyline order, then the visuals.

---

## P0 — Wrong, misleading or unsafe (fix before teaching)

### Material (knowledge)

| # | Slide | Problem | Agreed by | Fix |
|---|---|---|---|---|
| M1 | 5 (5) | **The "rules" block falls out of the context window.** In opencode, the system prompt, AGENTS.md and the skill list are rebuilt for every model call; only older conversation is compacted (summarised) *(source-checked)*. This also contradicts slides 9–10. The required reading order (your note) is not shown at all. | 5/5 | Redesign — see "Your three slides" below. |
| M2 | 7 (7) | **"App" is ambiguous.** Here it means opencode, but slide 2 and slide 26 use "app" for the financial app participants build. **Two arrows are numbered "4"**, one has no label, and reading order jumps 1→2→(down)3→4→(up)4→5. | 5/5 | Redesign — see below. Adopt one vocabulary deck-wide (V1). |
| M3 | 9 (9) | **Shows reuse, not why AGENTS.md matters or how it is maintained.** "Session 1/2/3" boxes look like the course's own Sessions 1–3. | 5/5 | Redesign — see below. |
| M4 | 4, 10, 30 (4, 10, 26) | **"Stateless" is stated too absolutely**: "each request starts from zero", "resends the whole conversation", quiz answer "Nothing carries over between sessions except files". Real products may summarise history, store chats, or have memory features. "Overnight" is not what resets anything; a new conversation is. The claim can also sound like a privacy guarantee. | 5/5 | Title: "The model doesn't remember earlier requests; opencode sends the context it needs". Scope "whole conversation" to *our chatbot*. Rewrite the quiz around "you started a new conversation". |
| M5 | 6 (6) | **"Every request is one list of messages: system, user, assistant, tool"** is presented as universal. Providers differ, and tools are defined separately from messages. The notes say putting AGENTS.md in the "system" role is "close enough". | 4/5 | Merge into the new slide 5 (one line: "messages have roles"), keep the role glossary in the handout. Reuse this slot for "Context has a limit" (see redesign). |
| M6 | 8 (8) | **"…until the task is done" / "Task done"** equates the agent *saying* it is finished with the work being correct. "Agent: typing" undersells what the agent decides. | 3/5 | Title: "A coding agent repeats model decisions and tool actions; then you check the result". Exit box "Agent reports back" → separate box "You test". Punch line: "Agent: proposes and does. You: decide and check." |
| M7 | 26, 28 (23, 24b) | **"The AI: the LLM in backend/.env"** — the model does not live in a settings file. The padlock suggests the file protects itself. | 5/5 | External box "AI service (LLM)". Small card beside the back end: "`.env` = service address, model name, secret key — not the AI". Same fix in the 24b prompt: "calls the AI service using the settings in backend/.env". |
| M8 | 28 (24b) | **The test "And a month ago?" needs historical data the spec never supplies** ("backend adds NISP's *current* data"). A made-up price would look like a pass. | 4/5 | Either add "and the last year of daily closes, with dates" to the chatbot spec prompt, or test memory with "Which stock are we discussing?" and expect "I don't have that data" for history. |
| M9 | 19 (17) | **"The same request gives a more structured result when a skill is loaded"** is presented as a proven comparison; the demo is marked UNTESTED, and both panels show placeholder bars. | 4/5 | Title: "A brainstorming skill makes 'ask questions first' a repeatable habit". Label "Illustration". Better: replace with a real, rehearsed before/after excerpt. |
| M10 | 18 (16) | **"Task matches → full instructions load"** suggests automatic, guaranteed matching. In opencode the *model* chooses to load a skill via a skill tool, and may miss it *(source-checked)*. | 3/5 | "The agent sees skill names and descriptions, and loads a skill's full instructions when it decides one fits." Notes: you can name a skill explicitly; check the "loaded skill" message. |
| M11 | 12 (11b) | **"Effort sets how long the model thinks"** suggests a fixed timer and a guaranteed better answer. Ctrl+T cycles model *variants*, which only sometimes means effort *(source-checked: ctrl+t = variant_cycle is correct)*. | 3/5 | Title: "On supported models, higher effort lets the model reason more before answering". Caption: "Ctrl+T cycles the options your model offers." |
| M12 | 13, 14, 30 (12, 13, 26) | **Git oversold**: notes say "every version remembered" and a commit saves "the whole project"; recap says "Git and GitHub keep your work safe". Uncommitted, untracked and ignored files (e.g. `.env`) are not saved. | 4/5 | Three states on slide 14: **saved on laptop → committed (local save point) → pushed (on GitHub)**. Recap: "Commit and push save your work to GitHub." |
| M13 | 3 (3) | Notes say "That is all it does"; the probability bars look like measured data. | 3/5 | Label "Illustration". Notes: "generates text one small piece at a time; fluent is not the same as correct — we give it real data and check." |
| M14 | 24 notes (21b) | **"Plan mode cannot edit files"** — not strictly true: Plan can write a designated plan file, and config can change permissions *(source-checked)*. | 3/5 | "Plan mode is for proposing, not changing the app. Check the footer says *plan*." |
| M15 | 32 (28) | "…learns the rules"; notes say the app "forgets everything when it restarts". A Wiki gives the chatbot reference pages; the model is not retrained. | 2/5 | Title: "Next session: your app stores price history and the chatbot reads reference pages". |
| M16 | 2, 27, 32 | "Latest price", "today", "live": yfinance data may be delayed, and "today" is wrong outside market hours. | 3/5 | Say "latest available price"; make **date/time and source on screen** a spec requirement. |

### Hands-on safety (habits for bank staff)

| # | Slide | Problem | Agreed by | Fix |
|---|---|---|---|---|
| H1 | 15, 27 (14a, 24a) | **"Permission box? Choose Allow once" / "Agent asks to run a command? Allow it"** teaches clicking through the one safety gate. The /init request sometimes comes from a *mistyped path outside the project* (`prompts/s1.md`). | 5/5 | "Read what it wants to open or run. Inside financial-app and expected? Allow once. Anything else, or unsure? Raise your hand. Never 'Allow always'." |
| H2 | 16, 28 (14b, 24b) | **Repository visibility is left to the agent** ("Create a new GitHub repository…"). Notes: "people can decide". | 3/5 | Prompt: "…create a **private** GitHub repository called financial-app…". Check: "Open the link: correct account, 'Private' label, AGENTS.md present." Confirm with the bank which account is allowed. |
| H3 | 28 (24b) | **Secrets are checked too late.** `.env` is filled in first and only excluded at push time. | 4/5 | Before the key goes in: the agent creates `.gitignore` with `.env` plus a placeholder `.env.example`. Before the push: "list the files you will commit". If a key leaks: tell the facilitator, and the key must be replaced. |
| H4 | 29 (25) | **"Copy the error → paste it to the agent"** gives no warning to remove keys or customer data. | 3/5 | Sequence: "Copy the error → **remove keys and private data** → ask the agent to explain and fix → repeat the failed check." |

---

## P1 — Storyline and teaching weaknesses

| # | Slide(s) | Problem | Fix |
|---|---|---|---|
| S1 | 21, 23, 28, 30 | **Workflow name doesn't match the brief.** Brief: Interview → Plan (Approve/Edit/Reject) → Execute → Test/Debug → Iterate. Deck: Brainstorm → Spec → Plan → Execute → Test → Iterate; the 24b mini-map shortens it again to 4 steps. "Debug" disappears. | **Owner decision.** Recommended: use the brief's five names everywhere; make "save the spec" the output of Interview, and say once "skills call this brainstorming". |
| S2 | 2→21 | **The workflow (the participant's actual job) first appears on slide 21**, after ~50 min of model internals. | Show the five-step workflow right after slide 2 ("Your job today: interview, approve, check"), with a "you are here" marker on each run slide. |
| S3 | 24→25 | **The approve/edit/reject quiz comes *after* participants approved their own plan.** | Move slide 25 before Run 2b. Use a short real plan excerpt with one subtle extra (not "builds a phone app"). |
| S4 | 27–29 | **Debugging is taught after both builds.** | Move slide 29 to just before Run 3. |
| S5 | 23, 25, 26 | **Jargon arrives before it's explained**: the spec prompt has React, Vite, FastAPI, yfinance, endpoints and ports, but the architecture slide (26) comes after. Notes ask participants to "check the ports, endpoints". | Move slide 26 before Run 2, or put the tech line in a box labelled "Technical setup supplied by the course — copy as is". Participants check business items only. |
| S6 | 10, 25 | **Quizzes give the answer away** ("The agent was tired"; "plan that ignores the spec"). | Plausible distractors (see M4 and S3). |
| S7 | 28 (24b) | **The chatbot run is a second full project in 18 minutes** (key setup, brainstorm, spec, plan, build, 3 tests, fix, push). | Split it into 24b "Agree and approve the chatbot" and 24c "Build, test, push". Take the time from the trimmed concept block. |
| S8 | whole | **Hands-on time is 77 of 180 min (43%)**, though the brief says mostly hands-on, and the riskiest work sits at the end. | Trim the concept block (merge 5+6; shorten 3–4). Target ≥100 min of participant work plus a visible buffer. |
| S9 | 17 (15) | **The "four ways" picture is a staircase**, which implies workflow > skill > AGENTS.md > prompt. | Four equal cards by job: *Prompt — this task · AGENTS.md — standing project rules · Skill — reusable expertise · Workflow — a repeatable sequence (Session 3)*. Footer: "They work together." |
| S10 | 17–19 | **Skills are only described**: participants never see a real skill or check that one loaded (the course spec requires seeing available skills). | Show one real skill's name, description and a 2-line excerpt, plus the "skill loaded" message. Add a one-question choice drill: which of the four ways fits each case? |
| S11 | 11 (11) | **`[FAST MODEL]` / `[SMART MODEL]` placeholders are still on screen.** | **Owner input:** the actual class model names. Title: "Use a quick model for small edits and a stronger one for planning and debugging". |
| S12 | 30 (26) | The recap declares success with no exit check. | Add a 4-item finish check: dashboard opens · one data check · one chatbot check · latest commit on GitHub (or checkpoint ready). |
| S13 | 27–28 | **Financial correctness is "looks plausible"**. | Acceptance list: NISP.JK, IDR, date/time and source shown, change vs previous close, chatbot numbers match the app, "I don't have that data" when missing, no buy/sell/hold advice. |

## P1 — Hands-on completeness

| # | Slide(s) | Problem | Fix |
|---|---|---|---|
| R1 | 15 (14a) | **The title says "add AGENTS.md with one rule, and push"**, but this slide only covers sign-up and /init. All six run slides repeat the whole-run title. | Per-slide titles: "Run 1a: Sign up to GitHub and draft AGENTS.md" · "Run 1b: Add your rule, check it, push privately" · "Run 2a: Interview and save the spec" · "Run 2b: Review the plan, then save it" · "Run 3a: Build and check the dashboard" · "Run 3b: Add, test and push the chatbot". |
| R2 | 15 | "In opencode, in financial-app" assumes participants know how to open opencode in that folder. | One setup line plus a handout card: "Open opencode in the financial-app folder; the path shown must end in financial-app." |
| R3 | 16 | No visible "check AGENTS.md before committing" step. | Insert: "Open AGENTS.md. Is your rule there? Then send Prompt 2." This makes ask → review → commit visible. |
| R4 | 24 (21b) | "Save **that** plan" only works in the same conversation; that condition is only in `prompts/s1.md`. | On the slide: "Stay in this conversation — no /new until it's saved." |
| R5 | 16, 27, 28 | **The GitHub push, dashboard build and chatbot prompts are marked UNTESTED.** Tests stopped at the plan and used a local bare repo, not GitHub. | Outside the deck: rehearse end to end on Windows and Mac before class. On slides: no change, but the report lists them. |
| R6 | 15–28 | Checkpoints (`s1-start`, `s1-spec`, `s1-dashboard`, `s1-chatbot`) are names with no recovery steps; the handout file doesn't exist yet. | Outside the deck: write the handout and recovery card. On slides: "Stuck? Raise your hand — we'll restore checkpoint X." |
| R7 | 23 (21a) | "Five questions" — the prompt says *at most* 5. | "Up to five questions, one at a time". |

---

## P2 — Visual and animation

| # | Slide | Problem | Fix |
|---|---|---|---|
| A1 | 4 (4) | **The Turn 1 arrow never appears** (its `.link` starts at scaleX(0) and nothing triggers it; confirmed in `04_n4_step3.png`). The base case looks disconnected. | Show it on arrival. |
| A2 | 18 (16) | **The loaded skill card sticks out below the context box** (`18_n16_step3.png`). Descriptions are grey bars; the request has no text. | Card lands fully inside the box; real one-line descriptions; request text, e.g. "Help me plan a dashboard". Label the shelf "not loaded". |
| A3 | 12 (11b) | At step 2 the dial and bar loop between low and high by themselves, so a deliberate choice looks automatic. | One click moves low → high, then it stays. |
| A4 | 12 (11b) | `prefers-reduced-motion` misses `.eff-hand/.eff-ptr/.eff-bar`. | Add them to the reduced-motion rule. |
| A5 | 7, 11, 20, 22, 29 | Endless loops (packets, cars, floats, pulse) keep running while the speaker explains or participants work. | Run once or twice, then stop. Keep the continuous loop only on slide 8 (the agent loop is the concept). |
| A6 | all | Colour meaning varies: red = model, user, warning, skill, emphasis. | Fix a colour key: red = model/AI, black = opencode/you, grey = data/tool. Note it in the plan. |

## P3 — Polish

- 28 (24b): the title is smaller than on 27 (24a); this goes away when run titles shrink (R1).
- 20 (19 notes) "Spec = PRD": keep it only if the audience knows "PRD"; otherwise say "the agreed requirements".
- Slide 25 notes: remove "lazy choice".

---

## Your three slides — recommended redesigns

### Slide 5 → two slides (reuse slide 6's slot; deck stays 32 slides)

**5 · "Every turn, opencode sends the model a stack: its rules, your project rules, skills, the chat so far, and your new message"** (shorter variant: "What the model reads on every turn")
Vertical stack, read top to bottom, one arrow to **Model**. Click by click:
1. **System prompt** — opencode's own rules
2. **AGENTS.md** — your project's rules
3. **Skill list** — names and descriptions only
4. **Conversation so far** — your messages, its replies, tool results
5. **Your new message** → the stack goes to the Model
Bracket 1–3 as "**sent every turn, never dropped**" (black). Bracket 4 as "**grows**" (grey). Footnote: "Simplified view." *(source-checked: rules and skill list are rebuilt every call)*

**6 · "The context window has a limit, so old chat gets summarised — save decisions in files"**
The same stack inside a fixed frame, with room left for the reply.
1. The conversation grows toward the limit.
2. The older chat shrinks into one "summary" block — **rules stay**.
3. "Details can be lost" appears.
4. Takeaway: "Rules → AGENTS.md · requirements → spec · steps → plan. `/new` starts clean, so save first."
The 4-role list moves to the handout.

### Slide 7 — tool calling

Title: **"The model asks for a tool; opencode checks permission and runs it"**
Three lanes, left to right: **opencode (on your laptop) | Model | Tool: read a file**. Six rows top to bottom, each number used once:
1. opencode → Model: "your message + list of tools"
2. Model → opencode: "please read docs/spec.md"
3. opencode → Tool: "check permission, then run"
4. Tool → opencode: "file text"
5. opencode → Model: "conversation + file text"
6. Model → opencode: "answer (or another tool request)"
Notes: "The model never touches your laptop; opencode does, within its permissions. Our chatbot doesn't use tools."

### Slide 9 — AGENTS.md

Title: **"AGENTS.md is the project's standing brief, so keep it current"**
Analogy: an onboarding note for a new colleague.
1. A new conversation starts with no previous chat — "like a new colleague on day one".
2. AGENTS.md is handed over every turn (consistent with slide 5).
3. What goes in it: *what the project is · how to run and check it · working rules*. What stays out: *passwords/keys, chat logs, feature details (→ spec)*.
4. Over time, a cycle: **/init drafts it → you notice a lasting rule or a repeated correction → ask the agent to update it → read the change → commit**.
5. Footer: "**Today: ask the agent to edit AGENTS.md, then review it.**"

**On "don't edit manually"** — all reviewers agree that this must be a *course recommendation with a reason*, not a rule. It is a plain text file, and opencode's own docs say you may create or edit it by hand *(source-checked)*. Reasons that hold:
- you state the rule in plain language and the agent keeps the file's structure and wording consistent;
- it avoids accidental deletions or formatting slips by non-technical users;
- the change is still reviewed and committed, so Git makes it reversible whoever typed it.
Don't claim that manual edits break anything or that the agent can't make mistakes.

Slide 10 quiz becomes: "A new conversation ignored your 'explain first' preference. What do you do?" A) Repeat it in every chat B) **Ask opencode to add it to AGENTS.md, review, commit** C) Switch to a smarter model.

---

## Vocabulary (V1) — apply deck-wide, including notes

| Thing | Say | Never |
|---|---|---|
| LLM | **the model** (defined once: large language model) | "the AI" where the actor matters |
| opencode | **opencode, the coding agent** | "the app" |
| ChatGPT and similar | **chat products** | "the app is just a screen" |
| What participants build | **your financial app** (dashboard + chatbot) | an unqualified "app" when opencode is meant |
| `financial-app` | the literal folder/repo name | — |

The redesign review lists all 18 "app" occurrences by slide (`r-redesign.md`, finding 4).

---

## Owner decisions needed

1. Workflow names: the brief's five steps or the current six (S1).
2. Scope: repair in place, or also reorder (S2–S5, S7, S8).
3. AGENTS.md wording: "recommended, with reason" vs a strict "don't" (slide 9).
4. Bank policy: GitHub account, private repo, approved AI service for the chatbot (H2, M7).
5. Actual class model names for slide 11 (S11).

## Outside the deck (delivery blockers, not slide edits)

- Rehearse end to end on Windows and Mac: GitHub sign-in and private push, dashboard, chatbot, tests (R5).
- Handout, recovery card, checkpoint links (R6).
- Re-run `prompts/s1.md` for every changed prompt (H2, H3, M7, M8).
