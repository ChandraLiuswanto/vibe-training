## 1. Verdict

**Revise before teaching: the core model → tool → result explanation is sound, but several absolute statements would teach the wrong mental model.** The most important correction is the relationship between context compaction and standing instructions: slide 5 explicitly ejects “rules”, whereas opencode 1.19.5 rebuilds normal agent requests with its system instructions, applicable instruction files and available skill descriptions; it compacts older conversation separately. Other material problems are the implication that permissions make every action human-approved, the statement that Plan mode cannot write any files, the “LLM in `.env`” label, and a historical-price test without an explicit historical-data requirement. I checked the HTML, extracted notes, supplied design/test materials and selected relevant screenshots. For opencode behaviour, I also checked the upstream **v1.19.5 tag**, commit `810c0eba1a7348036f8bdf61e6632d0c36c6876c`; this is source verification, not a Windows/Mac classroom runtime test. No project files were changed.

## 2. Findings

### 1. P0 · Material / Animation — Standing rules must not fall out of the context window
**Slide 5 (data-n 5), connected to slides 9–10 (data-n 9–10)**  
**Classification: misleading. Confidence: high.**

- **Evidence:** `05_n5_step2.png` shows a crossed-out “rules” block falling outside the window. Notes: “when the desk is full, the oldest material is cut off or replaced by a short summary.”
- **Technical check:** In v1.19.5, `session/prompt.ts` calls `instruction.system()` and `sys.skills(agent)` inside the agent loop, then supplies those separately from compacted conversation messages. `session/instruction.ts` reads the applicable standing instruction files. Older conversation/tool outputs are handled by compaction/pruning.
- **Why it matters:** Participants could conclude that persistent project rules disappear merely because they are old.
- **Fix:** Title: **“The context window is limited; opencode summarises older conversation to make room.”** Reveal:
  1. Built-in instructions.
  2. Applicable `AGENTS.md` rules.
  3. Available skill names/descriptions and tools.
  4. Conversation plus the current request.
  5. Older conversation becomes a shorter summary; the standing-instruction area stays.
  
  Label this **“A simplified view of each request”**, not a universal literal read sequence. Reserve space for the model’s reply; do not imply input alone uses the entire capacity.

### 2. P0 · Material — “Stateless” does not mean every request starts with no knowledge
**Slide 4 (data-n 4), repeated on slide 30 (data-n 26)**  
**Classification: correct core concept, misleading absolutes. Confidence: high.**

- **Evidence:** “each request starts from zero”; “the chat app keeps the whole conversation and sends all of it again”; “anything that is not in what gets sent does not exist for the model.”
- **Why it matters:** This confuses model-call state, learned knowledge, app-managed memory and retained history. Actual apps may select or summarise history, retrieve saved information or use provider-managed conversation state. Prompt caching also makes “reads everything from the top each time” a poor performance explanation.
- **Fix:** **“The model does not automatically remember previous requests; the app supplies the context it needs.”** Notes: “That includes relevant conversation history, sometimes summarised. The model also has knowledge learned during training, but that is not a reliable source of current stock prices. In our small chatbot, we send the full chat history each turn.” Say longer contexts **can** increase cost and delay.

### 3. P0 · Material — Explain AGENTS.md as persistent guidance, not a one-time session read or guaranteed compliance
**Slide 9 (data-n 9), reinforced by slide 16 (data-n 14b)**  
**Classification: simplified but incomplete; enforcement implication misleading. Confidence: high.**

- **Evidence:** “reads at the start of every session”; notes: “It makes the agent say what it plans to do before it does it.”
- **Why it matters:** The benefit is not simply surviving overnight. Applicable root/global instruction text is supplied again during ordinary agent requests, including after conversation compaction. Being in context does not guarantee obedience or implement a permission gate.
- **Fix:** Title: **“AGENTS.md keeps project guidance available across requests and new sessions.”** Notes: “Keep it short: project purpose, how to run/check the app, and standing preferences. opencode includes applicable rules when preparing requests. These guide the model; you still review its work. The explanation rule asks it to explain first—it does not require it to wait for approval.” If waiting is intended, explicitly add that requirement and use appropriate permissions.

### 4. P0 · Material — The overnight quiz gives an unjustified diagnosis and an incorrect universal rule
**Slide 10 (data-n 10)**  
**Classification: misleading. Confidence: high.**

- **Evidence:** “The agent forgot your preference overnight”; answer: “Nothing carries over between sessions except files.”
- **Why it matters:** Overnight is irrelevant. Reopening the same saved session differs from `/new`. A missed preference may also be an instruction-following failure. Apps can persist configuration, memory and other state, not just project files.
- **Fix:** Ask: **“You gave a preference only in yesterday’s chat. Today you use `/new`. How do you make it reusable?”** Answer: **“Put the project preference in AGENTS.md. A new chat does not automatically include yesterday’s chat.”** Notes: “Project files remain on disk; they are not all automatically read.”

### 5. P0 · Material — Four roles are a useful example, not the universal shape of every API request
**Slide 6 (data-n 6)**  
**Classification: simplified but fair if explicitly scoped; currently overgeneralised. Confidence: high.**

- **Evidence:** “Every request is one list of messages: system, user, assistant, tool”; notes treat guessing AGENTS.md’s role as “close enough”.
- **Why it matters:** Providers differ: some use a separate system/instructions field, developer messages or tool-result content blocks. Tools are also defined separately from ordinary chat messages.
- **Fix:** Title: **“Messages label instructions, user requests, model replies and tool results.”** Caption: **“Common roles in a chat API.”** Notes: “opencode translates these for the selected provider. In opencode, applicable AGENTS.md text becomes standing instruction context; you do not choose a message role when editing the file.” Remove the role-guessing quiz.

### 6. P0 · Material / Quality — Identify “App” as opencode, not the financial app participants will build
**Slide 7 (data-n 7)**  
**Classification: mechanism correct; naming ambiguous. Confidence: high.**

- **Evidence:** `07_n7_step5.png` labels the controller only “App”; slide 26 later uses “Your app” for the React/FastAPI application.
- **Why it matters:** Participants may think the dashboard runs development commands or that the LLM directly accesses their laptop.
- **Fix:** Rename the left box **“opencode — the coding-agent program”**, the bottom-right box **“Tool — e.g. read a project file”**, and the other box **“LLM service”**. Label the return-to-model arrow **“Context + tool result”**. Use unique action numbers: request → proposed tool call → permission check/execution → result → next model response. If showing the literal native tool name, use `read`; otherwise mark `read_file` as an illustrative name.

### 7. P0 · Hands-on / Material — Remove blanket permission approval and the resulting false reassurance
**Slides 7, 15 and 27 (data-n 7, 14a and 24a)**  
**Classification: misleading and unsafe guidance. Confidence: high.**

- **Evidence:** “you stay in the loop”; “Permission box? Choose Allow once”; “Agent asks to run a command? Allow it.”
- **Technical check:** v1.19.5 Build defaults allow many operations without individual confirmation. External-directory access normally asks, with exceptions/configuration. Source: `agent/agent.ts`, default permission rules.
- **Why it matters:** The model’s inability to execute directly does not stop opencode executing a damaging request. “Allow once” limits approval duration, not the possible consequence.
- **Fix:** **“Read what the agent wants to do before approving. Approve only access and commands needed for this exercise; ask the facilitator if unsure.”** Notes: “Some actions run automatically under the configured permissions. A request for access outside the project is a reason to inspect the path—not automatically approve it.”

### 8. P0 · Material — A finished agent loop is not proof that the task is correct
**Slide 8 (data-n 8)**  
**Classification: simplified but misleading endpoint. Confidence: high.**

- **Evidence:** “until the task is done”; notes more accurately say “until the model thinks the task is done”.
- **Why it matters:** Agents also stop for errors, limits, questions or interruption. Reporting completion does not establish acceptance.
- **Fix:** Title: **“A coding agent repeats model decisions and tool actions, then you check the result.”** Replace “Task done” with **“Reports back / asks for input”**, followed by **“You test against the agreed goal.”** “You: goal and judgement. Agent: typing” is memorable but undersells autonomous decision-making; use **“Agent: proposes and carries out steps.”**

### 9. P1 · Material — Keep next-piece prediction, but remove “That is all it does”
**Slide 3 (data-n 3)**  
**Classification: simplified but fair at headline level; explanatory overreach in notes. Confidence: high.**

- **Evidence:** “scores likely next words”; “That is all it does”; illustrative candidate bars.
- **Why it matters:** Models generate tokens—pieces of text—not necessarily whole words. Predicting continuations describes generation, not a complete explanation of learned capabilities, reasoning or factual reliability.
- **Fix:** **“An LLM generates a response one small piece of text at a time.”** Notes: “These pieces are called tokens. Training teaches useful language and problem-solving patterns, but fluent output is not proof of truth. Supply current data and check important claims.” Label the bars **“Illustration—not measured probabilities.”** The NISP completion itself is a reasonable simple example.

### 10. P1 · Material / Hands-on — Fast versus smart is a rule of thumb, not a technical model taxonomy
**Slide 11 (data-n 11)**  
**Classification: simplified but fair recommendation; unsupported absolutes/placeholders. Confidence: high.**

- **Evidence:** `[FAST MODEL]`, `[SMART MODEL]`; “fast model replies in seconds”; “a smart model spends longer working things out before it acts.”
- **Why it matters:** Capability, latency, cost, tool reliability and reasoning configuration are different dimensions. A more capable model need not always be slower, and a fast one is not necessarily shallow.
- **Fix:** **“Use a quick, lower-cost model for easy checks; use a more capable model for harder decisions.”** Add: “Compare results on your actual task; either can be wrong.” `/models` is **verified correct** for listing/selecting available models. Actual course model names, availability, latency and cost remain **unverified** until the shared provider setup is supplied.

### 11. P0 · Material — Effort does not set a fixed amount of thinking time, and variants need not mean effort
**Slide 12 (data-n 11b)**  
**Classification: misleading title; shortcut correct. Confidence: high.**

- **Evidence:** “Effort sets how long the model thinks before it answers”; “If Ctrl+T changes nothing, your model has one setting.”
- **Technical check:** The tagged docs confirm default `variant_cycle: ctrl+t`. Variants are model/provider configuration bundles; reasoning effort/budget is one use.
- **Why it matters:** Higher effort can increase reasoning work, latency and cost, but does not guarantee a better answer or a particular time. No visible key response is not proof of only one setting.
- **Fix:** **“On supported models, higher reasoning effort allows more work before answering.”** Caption: **“Ctrl+T cycles the available variants; names and effects depend on the model.”** Notes: “If nothing changes, inspect available variants/configuration or ask the facilitator.” Do not universally prescribe low effort for building; implementation can be difficult too.

### 12. P0 · Material — Git remembers commits, not every edit or literally every file
**Slides 13–14 and 30 (data-n 12–13 and 26)**  
**Classification: core commit/push/pull explanation fair; snapshot/safety absolutes misleading. Confidence: high.**

- **Evidence:** “every version remembered”; commit: “the whole project at that moment”; “your local copy … only you see it”; “Git and GitHub keep your work safe.”
- **Why it matters:** Uncommitted work is not necessarily recoverable. Untracked/ignored files do not automatically enter a commit. Local files are not inherently private, and a remote is not inherently access-controlled.
- **Fix:** **“A commit records a named version of the project files included in it.”** Notes: “Save, review, then commit. Push copies commits to the configured remote; pull fetches and integrates remote changes and may need conflict resolution. GitHub is our chosen remote host.” Replace “nothing travels” with **“Saving alone does not upload your work.”** The ordinary `pull → edit → commit → push` routine is fair with “pull may need help if changes conflict.”

### 13. P1 · Hands-on — `/init` is verified, but teach what to inspect rather than treating any generated file as correct
**Slide 15 (data-n 14a)**  
**Classification: command correct; expected outcome needs qualification. Confidence: high.**

- **Evidence:** “type `/init`”; fixed 43–55-second expectation in notes; retry after two minutes.
- **Technical check:** Tagged rules documentation says `/init` creates **or updates** AGENTS.md after inspecting the project and may ask questions. The supplied tests support the quoted timing only for those runs.
- **Why it matters:** An empty project cannot yield meaningful build/test instructions yet. Later updates must be reviewed. Blind retries may repeat work rather than explain a failure.
- **Fix:** **“Run `/init` to draft AGENTS.md, then read it.”** Notes: “In an empty folder, a short file is normal. Check the agent is in `financial-app`, inspect any error or access request, and check whether the file already exists before retrying. Update the project guidance after the app has real run/test commands.”

### 14. P1 · Material — Do not invent a prohibition on manually editing AGENTS.md
**Slides 9 and 16 (data-n 9 and 14b); owner’s review question**  
**Classification: asking the agent to edit is correct; ‘shouldn’t edit manually’ would be wrong. Confidence: high.**

- **Evidence:** Slide 16 asks the agent to add one rule. Nothing in the reviewed deck establishes a technical reason manual editing is disallowed; upstream rules documentation explicitly permits creating it manually.
- **Why it matters:** This is a plain Markdown instruction file, not protected program machinery. Participants need ownership of consequential project guidance.
- **Fix:** Notes: **“You can edit AGENTS.md yourself or ask the agent. Today we ask the agent for convenience, then read the change. Keep rules clear, short and consistent; do not put passwords or API keys here. Shared projects should review and commit rule changes.”**

### 15. P0 · Hands-on — GitHub creation/push needs tested authentication and an explicit privacy choice
**Slide 16 (data-n 14b)**  
**Classification: plausible action request, unverified classroom outcome; privacy ambiguity.**

- **Evidence:** “Create a new GitHub repository … and push”; notes: “[UNTESTED PROMPT]”; “A repository can be private; people can decide.”
- **Why it matters:** Git alone cannot create a GitHub repository. The agent needs an authenticated supported mechanism, such as the GitHub CLI/API, or manual setup. For bank staff, repository visibility should not be an incidental agent choice.
- **Fix:** Specify **“Create a private training repository in the approved account/location.”** Supply and rehearse the exact Windows/Mac sign-in route. Show success checks: intended account, private visibility, expected files, no secrets. Mark the end-to-end push **unverified** until this is rehearsed; the supplied local-bare-repository tests do not verify GitHub sign-in or repository creation.

### 16. P1 · Material — Present the four instruction methods as a useful map, not exhaustive or mutually exclusive categories
**Slide 17 (data-n 15)**  
**Classification: simplified but fair with small qualification. Confidence: high.**

- **Evidence:** “You can instruct the agent four ways”; workflow defined as “many steps”.
- **Why it matters:** A workflow can be written in a prompt, AGENTS.md, a skill or a command. A skill can itself contain a multi-step workflow.
- **Fix:** **“Four useful ways to organise instructions: a task prompt, project rules, a skill and a workflow.”** Explain: “A workflow is the agreed sequence; a skill or saved command can package that sequence.” Preserve “prompt: this task” and “AGENTS.md: standing project guidance”.

### 17. P0 · Material — Skill discovery is not guaranteed automatic matching or guaranteed obedience
**Slide 18 (data-n 16)**  
**Classification: progressive loading correct; automatic/absolute language misleading. Confidence: high.**

- **Evidence:** “Always loaded: name + description”; “Task matches → full instructions load”; notes: “only that one skill’s full instructions … and the agent follows them.”
- **Technical check:** v1.19.5 supplies available, permitted skills to the model and offers a `skill` tool. Tool availability and permissions can remove skills. The model chooses calls; more than one skill may apply.
- **Why it matters:** A relevant skill can be missed; loading it does not ensure compliant output. Participants need a way to detect that.
- **Fix:** **“The agent sees available skill summaries and can load the relevant playbooks.”** Diagram: **“Model chooses a skill → skill tool loads its instructions → model uses them.”** Notes: “You can name a skill explicitly. Check the loading message and resulting behaviour. A task may need several skills. Skills provide reusable guidance, not newly trained expertise.”

### 18. P0 · Material — The with/without skill comparison is an illustration, not a verified causal result
**Slide 19 (data-n 17)**  
**Classification: misleading as a guaranteed comparison; demonstration unverified.**

- **Evidence:** “The same request gives a more structured result when a skill is loaded”; “Without a skill: a straight answer”; notes mark the demo “[UNTESTED PROMPT]”.
- **Why it matters:** A model without a skill can ask good questions. A poor skill can worsen a result. Installed background skills/rules and stochastic variation affect comparisons.
- **Fix:** Title: **“A brainstorming playbook can make ‘questions first’ a reusable habit.”** Label panels **“Illustrative responses.”** Explain that the useful difference comes from the actual skill’s instructions. A live comparison needs fresh sessions, inspected rules/skills, demonstrated loading and a rehearsed result—not just “same model and settings”.

### 19. P0 · Material — Plan mode is intended for planning, not an absolute “cannot write files” guarantee
**Slide 24 (data-n 21b)**  
**Classification: correct course procedure; misleading universal capability claim. Confidence: high from source.**

- **Evidence:** “Plan can read and think but cannot edit files, so it is safe for planning”; “Plan mode cannot write files.”
- **Technical check:** v1.19.5 `agent/agent.ts` denies ordinary edit operations but explicitly permits designated plan-file paths. Configuration can override permissions. The experimental Plan reminder also explicitly instructs writing its designated plan file. The tagged prose docs and implementation are not completely aligned; use the source and test the course setup.
- **Why it matters:** Participants should not treat selecting Plan as an all-purpose safety sandbox.
- **Fix:** **“Use Plan to propose the work without changing the application. Use Build to save our approved plan to docs/plan.md.”** Notes: “Plan has restricted permissions; some setups allow a designated planning file. Our course uses this tested save sequence.” Tab switching is **verified as the default**, subject to autocomplete/custom keybindings.

### 20. P0 · Material — The LLM is not inside `.env`, and `.env` is not automatic secret protection
**Slides 26 and 28 (data-n 23 and 24b)**  
**Classification: wrong label and overstated security. Confidence: high.**

- **Evidence:** `26_n23_step3.png`: “The AI: the LLM in backend/.env”; notes: “so nobody can see it in the browser.”
- **Why it matters:** `.env` holds configuration values, normally plaintext—not the model. A backend can still expose secrets through responses, logs, accidental static serving or commits.
- **Fix:** Diagram box: **“LLM service”**. Put a smaller note beside the backend: **“Connection settings and API key: backend/.env — keep private.”** Notes: “The backend reads these values and calls the service. Do not send the key to the browser, paste it into agent chat, log it or commit it.” Add `.env` to ignore rules **before** entering credentials, and inspect staged files before pushing. Ports 5173/8000 are fair as **our chosen development ports**, not intrinsic React/FastAPI ports; `localhost` means this laptop.

### 21. P0 · Hands-on / Material — Conversation history cannot supply a historical stock price never provided
**Slide 28 (data-n 24b), connected to slide 4 (data-n 4)**  
**Classification: missing data requirement; misleading test explanation. Confidence: high.**

- **Evidence:** Spec prompt: “backend adds NISP’s current data”; test: “And a month ago?”; notes: “‘A month ago’ tests the resent conversation.”
- **Why it matters:** Resending a question about the latest price helps resolve “NISP”, but does not create last month’s price. Without historical data in context or a retrieval tool, an answer may be invented.
- **Fix:** Require the backend to include **dated latest-quote data and relevant dated history** for this exercise, or require the chatbot to say it lacks historical data. Test separately:
  - “What is NISP’s latest available price?” → compare with supplied quote and timestamp.
  - “What currency is that?” → checks conversational reference.
  - “What was the closing price on [specific trading date]?” → checks supplied history.
  
  Define “a month ago” if retaining it.

### 22. P0 · Material — “Latest” and “live” market data need source, timestamp and delay status
**Slides 2, 27–28 and 32 (data-n 2, 24a–24b and 28)**  
**Classification: plausible data flow, misleading freshness implication. Confidence: high.**

- **Evidence:** “latest price”; “how much it moved today”; closing notes: “fetches prices live”.
- **Why it matters:** yfinance is an unofficial Yahoo Finance client. A returned value may be delayed, cached or the last available close. “Today” can be wrong outside trading hours or on holidays. Plausibility is not sufficient verification.
- **Fix:** Use **“latest available price”**, display **source, market timestamp, currency and delayed/cached status**, and define change against the previous trading close. If retrieval fails, show an explicit error or a clearly labelled cached result—not a silent substitute. **Freshness, reliability and numerical correctness of the proposed checkpoint app remain unverified here.**

### 23. P0 · Hands-on — Error-copying guidance needs a secret/data check
**Slide 29 (data-n 25)**  
**Classification: good debugging habit with a consequential missing condition. Confidence: high.**

- **Evidence:** “Copy the error / Paste it to the agent”; sources include server output.
- **Why it matters:** Logs can contain credentials, request content, personal information and internal paths. Bank staff should not learn indiscriminate copying into a hosted model.
- **Fix:** **“Copy the relevant error, remove secrets and sensitive data, then ask the agent to explain and fix it.”** Keep the final human verification step. For a stall, inspect status before interrupting/repeating: a quiet process is not necessarily stuck, and repeated actions can have side effects.

### 24. P0 · Material — Persistence and supplied knowledge are not the same as model training
**Slide 32 (data-n 28), and its Session 2 bridge**  
**Classification: misleading absolutes/metaphor. Confidence: high.**

- **Evidence:** “Today … forgets everything when it restarts”; “your chatbot learns the rules”; “A Wiki so the chatbot knows the rules.”
- **Why it matters:** Source files, configuration and caches can persist without a database. Chat retention depends on implementation and whether the browser or server restarts. A Wiki normally supplies reference material during requests; it does not retrain the model or guarantee correct regulatory interpretation.
- **Fix:** **“Next session: store price history and let the chatbot consult sourced reference pages.”** Notes: “Our current app does not deliberately maintain its own price-history database. Next session we add persistence and supply relevant Wiki content when answering. The model itself is not retrained; we still check sources, dates and claims.”

### 25. P1 · Hands-on — The deck promises a working end-to-end result beyond the supplied test evidence
**Slides 1–2, 16, 27–28 and 30 (data-n 1–2, 14b, 24a–24b and 26)**  
**Classification: unverified, not proven wrong.**

- **Evidence:** Dashboard, chatbot and real-GitHub prompts are marked untested in notes/copy. `prompts/s1.md` verifies initialization/spec/planning and explicitly says test pushes used a **local bare repository**. The supplied course spec requires end-to-end and cross-platform validation.
- **Why it matters:** A successful spec-writing test does not prove package installation, two running servers, provider integration, correct market data, historical answers, refusal behaviour or GitHub push. The material’s biggest practical risk lies after the tested section.
- **Fix:** Release only after a clean Windows and Mac rehearsal of the exact displayed prompts and current checkpoints. Record the chosen models, variants, permissions, dependencies, private-repo authentication, data fallback and acceptance results. Until then, call these outcomes **“target results—end-to-end rehearsal pending”**, rather than implying they have already been demonstrated.

### Claims that can be retained

These are not errors and should not be burdened with implementation detail on the slides:

- **Slide 3 (data-n 3):** “LLM” means large language model; next-piece generation and the risk of confident falsehood are fair introductory concepts after finding 9’s adjustment.
- **Slides 5–6 (data-n 5–6):** Instructions, conversation, included file contents and tool results consume context. The model does **not** automatically see every file merely because it exists on disk.
- **Slide 7 (data-n 7):** The model requests a tool action; opencode executes it and returns the result. This is the right central distinction.
- **Slide 8 (data-n 8):** Repeated model/tool interactions are a fair explanation of an agent loop, provided stopping is separated from verified success.
- **Slides 9, 15–17 (data-n 9, 14a–14b, 15):** AGENTS.md is editable project guidance; `/init` is a valid creation/update command; prompting the agent to add a rule is valid.
- **Slide 11 (data-n 11):** `/models` is valid.
- **Slide 12 (data-n 11b):** Ctrl+T is the documented default variant-cycle shortcut; it remains the **Control** key on Mac, not automatically Command.
- **Slide 5 and slide 19 notes (data-n 5 and 17):** `/new` starts a new session. It does not erase project files, reset the machine or stop running development servers.
- **Slides 13–14 (data-n 12–13):** Local repository versus GitHub-hosted remote, commit as a save point, push and pull are fair business-level simplifications after finding 12.
- **Slides 21–25 (data-n 19–22):** Interview/spec/plan/approval/build/test/iterate is a valid **course workflow**, not an automatic universal agent behaviour. A spec is reasonably described as a short requirements agreement; “Spec = PRD” is an analogy, not a strict document standard.
- **Slide 26 (data-n 23):** A React frontend communicating with a FastAPI backend, with the backend fetching data and calling an LLM service, is a coherent architecture. Backend-supplied data can support a chatbot without model tool calling.

**Verification references:** [v1.19.5 request construction](https://github.com/anomalyco/opencode/blob/v1.19.5/packages/opencode/src/session/prompt.ts), [standing instructions](https://github.com/anomalyco/opencode/blob/v1.19.5/packages/opencode/src/session/instruction.ts), [LLM request preparation](https://github.com/anomalyco/opencode/blob/v1.19.5/packages/opencode/src/session/llm/request.ts), [agent permissions](https://github.com/anomalyco/opencode/blob/v1.19.5/packages/opencode/src/agent/agent.ts), [skills](https://github.com/anomalyco/opencode/blob/v1.19.5/packages/web/src/content/docs/skills.mdx), [models/variants](https://github.com/anomalyco/opencode/blob/v1.19.5/packages/web/src/content/docs/models.mdx), [keybindings](https://github.com/anomalyco/opencode/blob/v1.19.5/packages/web/src/content/docs/keybinds.mdx), [TUI commands](https://github.com/anomalyco/opencode/blob/v1.19.5/packages/web/src/content/docs/tui.mdx), [rules/manual editing](https://github.com/anomalyco/opencode/blob/v1.19.5/packages/web/src/content/docs/rules.mdx).

## 3. Add or cut

**Add**
- A compact **“What goes into each model request”** diagram linking standing instructions, skill summaries, conversation and on-demand tool results. This repairs slides 4–10 with one consistent mental model.
- A short **“Before approving or sharing”** checklist: intended command/path, approved account, private repository, no secrets/sensitive data.
- A distinction between **opencode’s model/configuration** and **the dashboard chatbot’s model/configuration**. Selecting a model in `/models` does not automatically configure the app’s `.env`.
- A visible acceptance check for **source, timestamp, currency, actual data values and graceful failure**, not only “looks plausible”.
- A brief way to **inspect available skills and confirm a skill loaded**; otherwise the skill lesson remains mostly conceptual.

**Cut or replace**
- The animation ejecting standing rules; “starts from zero”; “nothing carries over except files”.
- “Agent asks … Allow it”, “Plan cannot write files”, “the LLM in `.env`”, and unqualified “live” prices.
- The untested skill comparison as evidence that a skill necessarily improves output. Retain it only as an explicitly labelled illustration or rehearse a genuine demonstration.