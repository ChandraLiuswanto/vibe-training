## Verdict

**The deck has a strong visual foundation, but I would not use it unchanged for this audience.** The large type, restrained layouts, continuous NISP example, and three-run structure support speaker-led teaching. The main risks are conceptual rather than cosmetic: several diagrams imply guarantees that the software does not provide, permission instructions encourage uncritical approval, and essential build/recovery steps remain unverified or unavailable. Slides 5, 7, and 9 need substantive clarification, not just tidying. I reviewed all **104 supplied screenshots across 32 slides**, including every captured click state, and inspected the HTML/CSS/JavaScript. This was read-only and independent; no files were changed or other reviewers contacted.

**Evidence limits:** Animation findings below combine captured states with source inspection; I did not run a live browser or participant build. `prompts/s1.md` documents successful spec-and-plan tests, but the notes explicitly mark several later prompts untested. Independent opencode documentation requests were blocked, so version-specific behaviour is identified as **unverified**, not asserted to be wrong.

Screenshot filenames below are relative to `vibe-training/.review/s1-v2-shots/`. Slide numbers mean the displayed **N / 32**.

## Findings

### Wrong, misleading, or ambiguous knowledge

1. **P0 · Material — The architecture puts the LLM inside a configuration file.**  
   **Slide 26 (data-n 23); also slide 28 (data-n 24b).**  
   **Evidence:** `26_n23_step3.png` labels the external component “The AI: the LLM in backend/.env.” The prompt in `28_n24b_step0.png` repeats “calls the LLM in backend/.env.” A `.env` file stores configuration values, not the model.  
   **Impact:** Participants can leave thinking the AI runs locally inside their project, obscuring where prompts and financial data travel. The padlock also overstates what a plain-text file protects.  
   **Fix:** Draw an external **“LLM service”** box. Inside the backend, show **“.env: service address, model name, secret key.”** Label the connection “sends messages; receives an answer.” High confidence.

2. **P0 · Hands-on — Permission instructions teach automatic approval.**  
   **Slide 15 (data-n 14a) and slide 27 (data-n 24a).**  
   **Evidence:** `15_n14a_step0.png`: “Permission box? Choose Allow once.” `27_n24a_step0.png`: “Agent asks to run a command? Allow it.” The test record attributes some external-directory requests to mistyped paths.  
   **Impact:** Bank staff are trained to bypass the very control that limits an agent’s access. This contradicts the earlier message that humans remain in control.  
   **Fix:** Replace with: **“Read what it wants to access or run. Approve only the expected training task inside your project. Unexpected folder, deletion, upload, or unfamiliar command? Stop and ask the facilitator.”** Show one worked permission example.

3. **P0 · Material — The context-window animation teaches indiscriminate deletion of rules and omits the requested reading order.**  
   **Slide 5 (data-n 5).**  
   **Evidence:** `05_n5_step1.png` shows generic buckets; `05_n5_step2.png` literally drops and crosses out “rules.” No build identifies system prompt → `AGENTS.md` → skill list → user prompt → subsequent conversation/tool results.  
   **Impact:** Learners may believe system rules simply fall out first, and that starting a new session automatically restores all lost task knowledge. Actual trimming and summarisation are application-dependent.  
   **Fix:** Separate **standing context assembled by the coding app** from **growing conversation history**. Number the requested conceptual order, then show older conversation becoming a summary. Say **“The app may summarise or trim history; details can be lost.”** Explain that `/new` needs a task handover. Exact opencode assembly order remains **unverified**; do not present it as universal instruction precedence.

4. **P0 · Material — “Stateless” is overextended into claims about all application memory.**  
   **Slide 4 (data-n 4) and slide 10 (data-n 10).**  
   **Evidence:** `04_n4_step3.png` says the app resends the *whole* conversation every turn. `10_n10_revealed.png` says “Nothing carries over between sessions except files.”  
   **Impact:** This conflates the model’s request-level behaviour with an application’s stored conversations, summaries, saved preferences, or other memory features. It can also sound like a privacy assurance.  
   **Fix:** Scope the claim: **“In our simple chatbot, the app sends the conversation with each request. The model does not remember earlier requests by itself.”** Change the quiz to **“You started a new conversation without including the preference.”** Add: **“Stateless does not mean the service stores no data.”**

5. **P0 · Quality — The tool-calling sequence is ambiguous and incorrectly numbered.**  
   **Slide 7 (data-n 7).**  
   **Evidence:** `07_n7_step5.png` has two arrows numbered **4**, one without a description. The final reading order is 1 → 2 → jump down to 3 → 4 → jump up to 4 → 5. “App” is not identified on-screen.  
   **Impact:** This is the key explanation of who acts on the computer, yet it is difficult to reconstruct without narration. “App” can mean the financial app participants are building.  
   **Fix:** Rename the left column **“Coding app: opencode.”** Use a top-to-bottom sequence numbered **1–6**: send messages/tools → request tool → run tool → return result → resend context plus result → answer. Give each arrow its own labelled click. The duplicate numbering is directly confirmed in HTML.

6. **P0 · Material — The message-role lesson treats a simplification as an exact universal structure.**  
   **Slide 6 (data-n 6).**  
   **Evidence:** `06_n6_step3.png` says “Every request” is system, user, assistant, tool. Notes accept “system” as “close enough” for the role of `AGENTS.md`.  
   **Impact:** Learners can infer that every request contains all four roles and that a project instruction file inherently has system-level authority. Tool availability is also different from a tool-result message.  
   **Fix:** Title it **“Messages have roles; these are four common ones.”** Show a simple request without a tool result, then add one after execution. Explain that `AGENTS.md` is project guidance inserted by the coding application; its exact API representation is implementation-specific and **unverified for this pinned setup**.

7. **P0 · Material — The skill comparison presents an untested illustration as a controlled result.**  
   **Slide 19 (data-n 17).**  
   **Evidence:** `19_n17_step3.png` asserts a more structured result and says “Same folder, model and settings,” but both outputs are grey placeholder bars. Notes mark the demonstration **[UNTESTED PROMPT]**.  
   **Impact:** Participants are shown apparent evidence for an outcome that was not established. An agent without a skill may ask questions; a skill does not guarantee better output.  
   **Fix:** Either label the slide **“Illustrative example—not a measured comparison”** and soften the title to “A brainstorming skill can encourage questions first,” or replace it with real, rehearsed outputs and disclose normal variation.

8. **P0 · Hands-on — The historical-price test exceeds the data explicitly supplied to the chatbot.**  
   **Slide 28 (data-n 24b).**  
   **Evidence:** `28_n24b_step1.png` asks “And a month ago?” after a spec that says the backend adds NISP’s **current data** and uses no tool calling. Neither the visible prompt nor its notes explicitly requires historical data in the LLM context.  
   **Impact:** A plausible invented price could be mistaken for both successful conversation memory and successful financial analysis. Remembering “NISP” does not supply last month’s price.  
   **Fix:** Test memory with **“Which stock are we discussing?”** Separately require historical data, its date, currency, and source if historical questions are in scope. Include an expected **“I don’t have that data”** response when it is absent. Actual generated-app behaviour is **unverified**.

9. **P0 · Hands-on — Secret handling is introduced too late and lacks a human verification gate.**  
   **Slide 28 (data-n 24b); related slide 29 (data-n 25).**  
   **Evidence:** `28_n24b_step2.png` says to populate `.env`, then later asks the agent to ensure it is not committed. `29_n25_step2.png` says to paste errors without a redaction warning. “Never paste the key into chat” exists only in notes.  
   **Impact:** Learners may expose credentials in chat, screenshots, logs, or Git history before the final push check. `.gitignore` does not remove a file already tracked.  
   **Fix:** Before entering credentials, visibly establish `.gitignore` and an empty `.env.example`. Before committing, inspect the file list and confirm `.env` is untracked. Add **“Remove keys and confidential data before sharing errors.”** Teach that an exposed key must be revoked/rotated, not merely deleted.

10. **P0 · Material — The Git “save point” analogy omits what actually gets saved.**  
    **Slide 14 (data-n 13), reinforced by slide 30 (data-n 26).**  
    **Evidence:** `14_n13_step4.png` presents commit as a save point; notes say “the whole project at that moment.” `30_n26_step1.png` says Git and GitHub keep work safe without qualification.  
    **Impact:** Participants may assume every saved file—including untracked or ignored files—is recoverable, or that a local commit already exists on GitHub.  
    **Fix:** Add a three-part distinction: **Save = update a file; commit = record selected changes locally; push = send commits to GitHub.** Ask the agent to list included/excluded files before committing. State that credentials are intentionally excluded and GitHub is not a backup of everything on the laptop.

### Material and teaching gaps

11. **P1 · Material — `AGENTS.md` needs a lifecycle and ownership explanation.**  
    **Slide 9 (data-n 9).**  
    **Evidence:** `09_n9_step3.png` shows one file feeding three “Session” boxes, but does not explain creation, maintenance, review, or retirement of rules. “Session 1/2/3” also resembles the course’s three sessions.  
    **Impact:** Participants understand persistence but not how to keep instructions correct. They may treat the file as immutable—or assume rules enforce themselves.  
    **Fix:** Use **“New coding conversation A/B/C.”** Show **create → ask agent to update → review the change → commit**. Add: **“For this class, ask the agent to make changes; don’t edit manually.”** Explain this as a teaching convention, not a technical restriction: the file is editable text. Retain useful rules, remove obsolete ones, and keep secrets out.

12. **P1 · Hands-on — Model selection remains an unfinished instruction.**  
    **Slide 11 (data-n 11) and slide 12 (data-n 11b).**  
    **Evidence:** `11_n11_step3.png` still displays `[FAST MODEL]` and `[SMART MODEL]`. `12_n11b_step2.png` states that Ctrl+T switches effort without the model-support caveat visible in notes.  
    **Impact:** Beginners cannot reliably select the class configuration, distinguish model choice from effort, or diagnose an unavailable setting.  
    **Fix:** Insert the actual approved class model names and a real picker/footer screenshot. Add **“Available effort options depend on the selected model.”** `/models`, Ctrl+T, and exact footer behaviour are **unverified independently for 1.19.5**; rehearse on both operating systems before teaching.

13. **P1 · Material — The skills block never shows participants how to inspect or confirm a skill.**  
    **Slides 17–19 (data-n 15–17).**  
    **Evidence:** `17_n15_step3.png` names four instruction mechanisms; `18_n16_step3.png` explains loading abstractly; `19_n17_step3.png` offers no real skill name, file content, or loading confirmation. The course spec explicitly requires seeing which skills are available.  
    **Impact:** Learners can repeat the definition but cannot apply it or recognise when no skill was loaded.  
    **Fix:** Replace some abstract explanation with one real skill’s **name, description, short instruction excerpt, and visible load confirmation**. Include a supported way to inspect available skills, verified on the pinned installation, plus a “no skills installed” fallback.

14. **P1 · Hands-on — The first exercise assumes participants already know how to enter the correct project.**  
    **Slide 15 (data-n 14a).**  
    **Evidence:** `15_n14a_step0.png` jumps to “In opencode, in financial-app” without showing folder creation, launching there, or checking the current folder.  
    **Impact:** Non-programmers can create instructions in the wrong location before the first checkpoint. Preinstallation does not establish the working directory.  
    **Fix:** Add a short Windows/Mac setup card: create/open the training folder, launch opencode there, confirm the folder, select the class model, and send “hello.” Link installation troubleshooting separately; the supplied spec says tools are preinstalled, so a full installation lecture is unnecessary.

15. **P1 · Hands-on — The most consequential exercises are explicitly untested.**  
    **Slide 16 (data-n 14b), slide 27 (data-n 24a), slide 28 (data-n 24b).**  
    **Evidence:** `16_n14b_step1.png`, `27_n24a_step0.png`, and `28_n24b_step2.png` contain the GitHub, build, and chatbot prompts. Their notes mark them untested. `prompts/s1.md` proves the earlier spec/plan sequence, using a local bare remote—not real participant GitHub authentication.  
    **Impact:** The deck’s central promise depends on flows not yet demonstrated under classroom conditions.  
    **Fix:** Rehearse the exact copyable sequence from a clean folder through GitHub sign-in, dashboard, chatbot, tests, and push on Windows and Mac. Record timings and expected outputs. **Success of these flows is currently unverified; this is not evidence that they fail.**

16. **P1 · Hands-on — Recovery instructions point to missing participant materials.**  
    **Slide 24 (data-n 21b) and slide 28 (data-n 24b); checkpoint references recur elsewhere.**  
    **Evidence:** `24_n21b_step2.png` refers to a handout; `28_n24b_step2.png` shows only the spec and push prompts, with planning/building delegated to that handout. The expected `handouts/day3-s1.md`, facilitator directory, and reference-app directory are absent from this workspace.  
    **Impact:** A participant who falls behind has checkpoint names, not an executable recovery path.  
    **Fix:** Publish and test the handout and checkpoint links before delivery. Provide one safe recovery instruction that preserves `.env`, followed by a visible success check. Materials hosted elsewhere are **unverified**; include their actual URLs/QR codes rather than assuming availability.

17. **P1 · Storyline — The plan-review check comes after participants have already approved their plans.**  
    **Slide 24 (data-n 21b), followed by slide 25 (data-n 22).**  
    **Evidence:** `24_n21b_step2.png` completes review and saving; only then does `25_n22_revealed.png` teach the approve/edit/reject distinction. The conceptual plan on slide 22 is placeholder lines, not a worked example.  
    **Impact:** Beginners make the decision before practising the judgement the decision requires.  
    **Fix:** Move the quiz before the participant approval step. Add a tiny worked plan with one unnecessary feature and demonstrate the exact edit request. Keep the quiz as a check of understanding, not the first concrete instruction.

### Visual and animation clarity

18. **P2 · Animation — The effort control moves by itself after the keyboard instruction appears.**  
    **Slide 12 (data-n 11b).**  
    **Evidence:** `12_n11b_step2.png` shows the final instructional state. CSS makes `.eff-ptr` and `.eff-bar` cycle continuously between low and high in `.st2`; no participant action drives this.  
    **Impact:** A control that should represent a deliberate choice appears automatic. It also distracts while participants locate the shortcut.  
    **Fix:** Use one click to move from low to high, then stop. On the final build, hold the selected setting and reveal an actual footer example. Change the title to **“Higher effort usually allows more reasoning work”**, rather than suggesting a fixed time setting.

19. **P2 · Quality — The loaded skill visibly crosses the context boundary.**  
    **Slide 18 (data-n 16).**  
    **Evidence:** In `18_n16_step3.png`, the red brainstorming card extends below the context box. The “description” remains a grey placeholder, and the request contains no actual task text.  
    **Impact:** The diagram intended to explain what is *inside* context does not cleanly contain the loaded instructions. It also hides the matching relationship it asks learners to understand.  
    **Fix:** Land the full-instructions card completely inside the box. Give the request and description short, readable text, and label the remaining shelf **“Not loaded.”** Prefer a horizontal instruction panel over a tall vertical book.

20. **P2 · Animation — The first stateless-request arrow never appears.**  
    **Slide 4 (data-n 4).**  
    **Evidence:** `04_n4_step3.png` shows arrows for turns 2 and 3 but none for turn 1. Its `.link` starts at `scaleX(0)` and has neither its own `.in` class nor an `.in` ancestor to activate it.  
    **Impact:** The first request appears disconnected from the model, weakening the base case of the explanation.  
    **Fix:** Make the initial arrow visible on arrival, or give it an explicit build state. Confirm the packet travels from the first question to the model rather than remaining on an invisible connector.

21. **P2 · Animation — Reduced-motion support misses the effort animations.**  
    **Slide 12 (data-n 11b).**  
    **Evidence:** `12_n11b_step2.png` identifies the affected dial/bar/clock. The explicit reduced-motion list excludes `.eff-hand`, `.eff-ptr`, and `.eff-bar`. The global rule reduces duration to `0.01ms` but does not remove their infinite repetitions.  
    **Impact:** The source does not reliably provide the intended static alternative for motion-sensitive participants. Exact browser rendering under that preference is **unverified**.  
    **Fix:** Explicitly disable those animations under `prefers-reduced-motion`, set stable final positions, and use static clock/bar alternatives. Check all builds with reduced motion enabled.

22. **P2 · Animation — Several loops continue after they have finished teaching their point.**  
    **Slide 7 (data-n 7), slide 11 (data-n 11), slide 22 (data-n 20), and slide 29 (data-n 25).**  
    **Evidence:** `07_n7_step5.png`, `11_n11_step3.png`, `22_n20_step3.png`, and `29_n25_step3.png` correspond to source-defined infinite packets, vehicles, floating cards, pulses, and carets. These are active throughout explanation or hands-on waiting time.  
    **Impact:** Motion repeatedly pulls attention away from labels, decisions, and participant screens. A looping packet can also imply repeated execution rather than one completed exchange.  
    **Fix:** Let instructional motion run once or twice, then settle. Keep continuous motion only where repetition is the concept—principally the agent loop—and provide a presenter motion toggle. Stop the copying-error pulse once the next action becomes the focus.

## Recommended additions and cuts

**Add**
- **One “three things, three jobs” visual:** opencode builds the app; the financial app displays/analyzes data; the external LLM service generates answers. This resolves recurring “app/model/agent” ambiguity.
- **A visible safety checkpoint before the first permission approval and before the first credential entry.** These habits need to precede the risky actions.
- **A small financial acceptance checklist:** correct ticker, rupiah, price timestamp, source/delay label, chart period, missing-data response, and no investment recommendation. Plausible-looking numbers are not sufficient verification.
- **A real worked spec and plan excerpt.** Replace placeholder bars where participants are being taught to judge content.
- **Verified setup, handout, and recovery links.** These are delivery dependencies, not optional supporting material.

**Cut or replace**
- **Cut the unqualified “Nothing carries over except files” wording.** Teach the narrower model/application distinction.
- **Replace the synthetic skill “comparison” with a labelled illustration or real evidence.**
- **Cut persistent decorative movement from instructional and exercise slides.** Preserve purposeful reveals and the agent-loop demonstration.
- **Do not add more architecture terminology.** Correct the existing labels and boundaries first; the audience needs a trustworthy mental model, not more technical vocabulary.

**Priority:** resolve findings **1–10** before polishing motion, then prove the participant paths in **12–17** before classroom delivery.