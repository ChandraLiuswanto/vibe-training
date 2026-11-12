## Verdict

**The three-run structure is sound, but the hands-on material is not yet safe or complete enough for independent use by non-programmers.** The Run 1 rule prompt and all four on-slide Run 2 prompts match `prompts/s1.md` exactly; however, GitHub creation/push and the entire Run 3 sequence remain explicitly untested in the notes. The largest problems are blanket permission approval, unspecified repository visibility, insufficient secret-handling instructions, an inaccurate description of `.env`, and a historical-price test that is not supported by the chatbot specification. Beginners also lack the concrete steps for opening the project, inspecting files, starting both app components, and recovering from checkpoints. These are delivery and knowledge risks, not merely wording issues. I reviewed the HTML, notes, supplied supporting documents, and relevant screenshots without changing files. **All new prompt wording proposed below is untested and must be rehearsed before publication.**

## Findings

1. **P0 · Hands-on — Repository visibility is left to chance.**  
   **Slides:** slide 16 (data-n 14b); carried forward to slide 28 (data-n 24b).  
   **Evidence:** “Create a new GitHub repository called financial-app and push to it.” Notes say: “A repository can be private; people can decide.”  
   **Why it matters:** Staff may interpret public publishing as the standard approved workflow. Even a private personal repository is not automatically an approved destination for bank material.  
   **Proposed fix:** Establish the permitted account and hosting policy before class. For an approved GitHub exercise, rewrite the prompt:
   > “Create a **private** GitHub repository called financial-app in the account approved for this class. If it already exists, stop and tell me. Commit the training files with the message ‘Start project’, then push. Give me the repository link.”
   
   Add a human check: **“Open the link. Confirm the correct account, the ‘Private’ label, and AGENTS.md.”** Do not let an agent choose visibility implicitly.

2. **P0 · Hands-on — Permission approval is taught as automatic rather than a decision.**  
   **Slides:** slide 15 (data-n 14a), slide 27 (data-n 24a).  
   **Evidence:** “Permission box? Choose Allow once (Enter).” / “Agent asks to run a command? Allow it.” `prompts/s1.md` explains that the occasional `/init` permission concerns access **outside** the project directory.  
   **Why it matters:** This trains the opposite of the desired bank-user habit: approving unfamiliar access because the AI requested it. “Once” limits the grant’s duration; it does not establish that the access is appropriate.  
   **Proposed fix:** Replace with:
   > “Read what access is requested. Approve only the class-rehearsed action in your training folder. If it requests another folder, deletion, credentials, publishing, or something you do not understand, pause and raise your hand. Do not choose ‘Allow always’.”
   
   Notes should acknowledge that `/init` may need retrying after a rejected request. The exact Reject behavior in the TUI is **unverified in the supplied test record**.

3. **P0 · Material — The diagram incorrectly puts the LLM inside `.env`.**  
   **Slides:** slide 26 (data-n 23), slide 28 (data-n 24b).  
   **Evidence:** Diagram: “The AI: the LLM in backend/.env.” Prompt: “calls the LLM in backend/.env.” Screenshot: `26_n23_step3.png`.  
   **Why it matters:** A participant can learn that the model is stored locally in a configuration file. The lock icon also risks suggesting that the filename itself provides protection.  
   **Proposed fix:** Draw three distinct objects:
   1. **Browser screen on your laptop**
   2. **Back-end program on your laptop**
   3. **Approved external AI service**
   
   Place a small `.env` card beside the back end: **“Local settings: service address, model name, secret key.”** Draw the AI-service arrow from the back end. Rewrite the prompt clause:
   > “The backend calls the approved AI service using the settings in backend/.env.”
   
   Notes: **“.env is a settings file, not the AI and not an encrypted vault. Keeping secrets out of the browser requires correct implementation.”**

4. **P0 · Hands-on — The secret-protection check happens too late and is incomplete.**  
   **Slide:** slide 28 (data-n 24b).  
   **Evidence:** “First: put the LLM details in backend/.env.” Later: “Make sure backend/.env is not committed.” Success: “no .env on GitHub.”  
   **Why it matters:** There is no demonstrated ignore rule before the key is created, and absence from the latest GitHub file listing does not establish absence from commit history. Secrets could also be copied into another file or log.  
   **Proposed fix:** Before distributing or entering keys:
   - Have the agent create a placeholder-only `.env.example`.
   - Have it configure Git exclusions and verify that the real `.env` is ignored and untracked.
   - Participants enter the key locally, not in opencode or the app chatbot.
   - Before pushing, inspect the outgoing file list without printing secret values.
   
   Add: **“If a key was committed, pasted into a chat, or exposed on screen, stop and contact the facilitator. Removing the file is not enough; the key may need revoking and replacing.”**

5. **P0 · Material — “And a month ago?” requires historical data that the chatbot prompt does not require supplying.**  
   **Slide:** slide 28 (data-n 24b).  
   **Evidence:** Spec prompt: “The backend adds NISP’s **current data**.” Test: “And a month ago?” Notes describe that question as testing resent conversation.  
   **Why it matters:** Conversation history can identify that “a month ago” refers to NISP; it cannot supply an absent historical price. A plausible invented answer could be mistaken for a successful test.  
   **Proposed fix:** Require the backend to supply both the latest quote and relevant historical prices, with dates and source labels. Define the expected date policy, such as the most recent available trading day on or before the requested date. Alternatively, retain current-data-only scope and require:
   > “I do not have that historical price in the data provided.”
   
   Teach **remembering the question** and **having the evidence to answer it** as separate checks.

6. **P1 · Hands-on — The most consequential participant actions are not covered by the tested prompt set.**  
   **Slides:** slide 16 (data-n 14b), slides 27–28 (data-n 24a–24b).  
   **Evidence:** Their notes explicitly label these prompts `[UNTESTED PROMPT]`. `prompts/s1.md` ends at saving the approved plan and confirms that final test runs created **no `frontend/` or `backend/`**. Test pushes used a local bare repository, not GitHub.  
   **Why it matters:** Successful specification/planning tests do not validate software installation, GitHub authentication, a running dashboard, chatbot integration, or secret exclusion.  
   **Proposed fix:** Treat these as release blockers. Rehearse the exact participant TUI sequence from an empty folder through a private GitHub push and all app checks, on Windows and macOS. Record model/configuration, timings, failure handling, and checkpoint creation. Do not describe the full course path as tested until that exists.

7. **P1 · Hands-on — Run 1 begins after an unexplained setup step.**  
   **Slide:** slide 15 (data-n 14a).  
   **Evidence:** “In opencode, in financial-app: type /init.” Neither this run nor earlier participant instructions explain how to create/open that project folder or launch opencode there.  
   **Why it matters:** “In financial-app” is not an executable instruction for someone unfamiliar with terminals or working folders. Launching from the wrong folder also changes the scope of file access.  
   **Proposed fix:** Add a short Windows/Mac setup card in the handout, demonstrated once:
   > “Create an empty folder named financial-app in the class-approved location. Open opencode in that folder using the illustrated steps. Confirm the displayed project path ends in financial-app. Then type /init into opencode’s message box.”
   
   Use actual rehearsed screenshots rather than assuming an operating-system launch method.

8. **P1 · Hands-on — A checkpoint name is not a recovery procedure, and the referenced handout is missing.**  
   **Slides:** slides 15–16 (data-n 14a–14b), slides 23–24 (data-n 21a–21b), slides 27–28 (data-n 24a–24b).  
   **Evidence:** “Stuck? Checkpoint s1-spec,” etc. The promised `handouts/day3-s1.md`, printable `.html`, and `facilitator/day3-guide.md` do not exist at their specified project paths. The course spec §8.6 still leaves checkpoint hosting open.  
   **Why it matters:** A stalled beginner cannot infer whether to download, replace, clone, or switch a version. Replacing the wrong directory can lose work or overwrite configuration.  
   **Proposed fix:** Supply a single class resource link/QR and a tested recovery card:
   > “Raise your hand. Open the class handout → Recovery → s1-dashboard. The facilitator will help you preserve your work, restore the checkpoint, keep your local key file, and restart the app.”
   
   Do not use “replace my project” instructions without explaining their consequences. Verify checkpoint links and contents before class.

9. **P1 · Hands-on — GitHub browser sign-in is conflated with permission to push from the laptop.**  
   **Slides:** slide 15 (data-n 14a), slide 16 (data-n 14b).  
   **Evidence:** Success on slide 15 is “Your GitHub home page”; slide 16 says only “Tell me if I need to sign in.” Notes defer the method to a pre-session checklist.  
   **Why it matters:** A signed-in browser does not by itself demonstrate working Git authentication. Account selection, authorization, repository creation, and Git identity can each interrupt the first push.  
   **Proposed fix:** Explain:
   > “Creating/signing into GitHub gives you a website account. Connecting this laptop so it can upload files is a separate step.”
   
   Provide one approved, rehearsed Windows/Mac connection path. State: **“Enter passwords or authorization codes only in the approved sign-in screen—not in the agent chat.”** Add checks for correct account, first commit, and successful remote upload.

10. **P1 · Hands-on — Participants are told to check files without being shown how to view or correct them.**  
    **Slides:** slide 16 (data-n 14b), slide 23 (data-n 21a), slide 24 (data-n 21b).  
    **Evidence:** Notes say “Open AGENTS.md together,” “Everybody opens docs/spec.md,” and “reads it and corrects one thing.” The on-slide steps do not provide a viewing method or correction prompt.  
    **Why it matters:** A path such as `docs/spec.md` may be mistaken for a web address or text to type into a terminal. Participants may also overwrite the file accidentally.  
    **Proposed fix:** Explain once: **“docs is a folder inside financial-app; spec.md is a text document inside it.”** Provide an illustrated viewing method and a prompt alternative:
    > “Show me docs/spec.md in plain business language. Don’t change it yet.”
   
    Then demonstrate a factual correction: **“Change the audience to internal training participants. Don’t build anything yet.”** Ask for a real correction **if needed**, not a gratuitous change.

11. **P0 · Material — Plan mode is described as an absolute safety boundary without sufficient verification.**  
    **Slide:** slide 24 (data-n 21b).  
    **Evidence:** Notes: “Plan can read and think but cannot edit files, so it is safe for planning.” The supplied test record shows no file changes in the tested Plan runs; that does not establish an unconditional tool-permission guarantee for every participant configuration.  
    **Why it matters:** Users may stop reading permission requests because a mode label supposedly makes all actions safe.  
    **Proposed fix:** Use the narrower claim:
    > “Use the class-configured Plan mode to request a proposal rather than a build. Confirm the footer says plan. Keep ‘Don’t build anything yet’ in the prompt, and still inspect permission requests.”
   
    **Verification status:** The exact edit restrictions and overrides in opencode 1.19.5 are **unverified by this review**. Verify against the pinned installation before teaching “cannot.”

12. **P1 · Hands-on — Approval is not sufficiently operationalized in business language.**  
    **Slides:** slide 24 (data-n 21b), slide 25 (data-n 22).  
    **Evidence:** “Check it against your spec. Approve, edit or reject. Edit example: handout.” Notes additionally ask participants to check “ports, endpoints,” although those concepts are explained on the following architecture slide.  
    **Why it matters:** Participants need criteria they can assess, not responsibility for recognizing unfamiliar API syntax. They may also type “Approved” prematurely instead of following the save-only step.  
    **Proposed fix:** Put three review questions beside the plan:
    - Does it build only NISP’s price, change, and one-year chart?
    - Does it avoid extras we excluded?
    - Does it explain how we will open and check the result?
   
    Add explicit branches: **“Edit: ask for a change, then reread. Reject: explain the mismatch and request a replacement. Satisfied: switch to Build mode and send the save-only prompt below—not ‘go ahead’.”** Move the quiz before participants must make that decision.

13. **P0 · Hands-on — Saving the plan depends on staying in the same conversation, but that condition is hidden in notes.**  
    **Slides:** slide 24 (data-n 21b); slide 28 (data-n 24b) handout prompts.  
    **Evidence:** “Save **that plan** to docs/plan.md.” `prompts/s1.md` explicitly says “stay in the same conversation”; the slide does not. Earlier guidance recommends starting fresh sessions when tasks finish.  
    **Why it matters:** “That plan” is a conversation reference. A participant who starts a fresh chat may save an inferred or newly generated plan rather than the approved one.  
    **Proposed fix:** Add: **“Stay in this same conversation while switching modes. Do not use /new between reviewing and saving.”** Confirm that the saved numbered steps match the final reviewed version before building.

14. **P1 · Hands-on — Dashboard startup is delegated to an untested generated explanation.**  
    **Slide:** slide 27 (data-n 24a).  
    **Evidence:** Prompt ends “Then tell me how to open it.” Success says only “localhost:5173 with NISP’s price, change and chart.”  
    **Why it matters:** Generated instructions may introduce terminals, commands, dependencies, and separate server processes without preparation. `localhost` can be mistaken for a public website.  
    **Proposed fix:** Demonstrate a rehearsed startup card:
    > “The app has two running parts: the screen and the back end. Start both using the class instructions. Keep their windows open. In your browser’s address bar, open **http://localhost:5173**. ‘Localhost’ means this laptop; this is not a published website.”
   
    Include a safe “port already in use” response: **“Do not close unfamiliar processes; show the facilitator the message.”**

15. **P1 · Hands-on — Run 3 checks appearance, not correctness of financial information.**  
    **Slide:** slide 27 (data-n 24a), slide 28 (data-n 24b).  
    **Evidence:** “You should see … NISP’s price, change and chart.” Notes ask only whether numbers “look plausible, in rupiah.” Chatbot success is “NISP answers.”  
    **Why it matters:** A polished chart can display the wrong listing, currency, date, or fabricated figures. Plausibility is particularly weak validation for banking staff.  
    **Proposed fix:** Provide a compact acceptance checklist:
    - Instrument is **NISP.JK**, Bank OCBC NISP; currency is IDR.
    - Latest available quote has a date/time and source.
    - Daily change identifies its comparison basis.
    - Chart covers the requested period.
    - Chatbot price and historical answer match the supplied app data and date.
   
    Compare with the same timestamp/basis, not an unrelated live quote. If data is unavailable, expect a clear unavailable message—not invented numbers.

16. **P1 · Hands-on — “Put the LLM details in backend/.env” is not a complete beginner instruction.**  
    **Slide:** slide 28 (data-n 24b).  
    **Evidence:** That is the entire on-slide configuration procedure. The build prompt before it does not guarantee a ready-made `.env` template.  
    **Why it matters:** Users have not been shown hidden filenames, local text editing, which of the three values is secret, or how the class AI service differs from the model selected in opencode.  
    **Proposed fix:** Give a facilitator-led, illustrated local setup procedure using a template containing:
    ```text
    LLM_BASE_URL=<class-approved service address>
    LLM_API_KEY=<your training key>
    LLM_MODEL=<class-approved model ID>
    ```
    Explain: **“These settings connect the chatbot you are building. They are separate from opencode’s model picker.”** Demonstrate only with dummy keys; include the verified restart/check procedure and never ask the agent to display the real key.

17. **P1 · Material — Data use and training limitations are too easy to miss.**  
    **Slides:** slide 23 (data-n 21a), slides 27–28 (data-n 24a–24b).  
    **Evidence:** “Latest price” is prominent, but freshness/source requirements depend partly on brainstorm answers. No visible instruction prohibits customer/internal information in either chat. The “market data only” warning is in opening notes.  
    **Why it matters:** A corporate exercise can be mistaken for an approved client-use tool. Third-party data, generated analysis, and external AI transmission need explicit boundaries.  
    **Proposed fix:** Add a visible run-entry rule:
    > “Training prototype only. Use public training data—no customer, personal, confidential, or internal bank information. Market data may be delayed or unavailable. Not for trading decisions or client advice.”
   
    Make source, timestamp, delayed/cached status, and an investment-advice disclaimer acceptance requirements rather than optional brainstorm outcomes. Approved providers and permitted usage require owner/compliance confirmation.

18. **P1 · Hands-on — The advice-refusal test is useful but underspecified.**  
    **Slide:** slide 28 (data-n 24b).  
    **Evidence:** Prompt: “No buy/sell advice.” Test: “Should I buy NISP?” Success: “no buy advice.”  
    **Why it matters:** A response can avoid the word “buy” while still recommending a position or giving a personal suitability judgment. One passing response is not proof of reliable compliance.  
    **Proposed fix:** State the expected behavior:
    > “The chatbot declines to recommend buying, selling, holding, or making a personalized investment decision. It can summarize supplied facts and uncertainties.”
   
    Test at least one sell/recommendation variant as well. Notes should say: **“These checks demonstrate the intended training behavior; they do not certify a compliant production advisory system.”**

19. **P1 · Hands-on — Run 3’s timing has no supporting end-to-end measurement.**  
    **Slides:** slide 15 (data-n 14a), slide 16 (data-n 14b), slides 23–24 (data-n 21a–21b), slides 27–28 (data-n 24a–24b).  
    **Evidence:** Marked exercise times total **77 minutes**: 25 + 20 + 32. Slide 28 gives 18 minutes for local secret setup, brainstorming, spec review, planning/review, building, three tests, one fix, and push. Those prompts are untested.  
    **Why it matters:** Machine-response times in `prompts/s1.md` exclude beginner reading, typing, authentication, errors, and facilitator support. The marked exercise time is also less than half of a three-hour session despite “mostly hands-on” positioning.  
    **Proposed fix:** Reallocate time toward Run 3 and measure a mixed-OS novice rehearsal before fixing the exact split. Publish timed checkpoints and a clear switch-to-reference-app deadline. Keep Run 1’s 25-minute allowance conditional on a rehearsed sign-in path. Do not present an invented replacement duration as validated.

20. **P0 · Hands-on — Debugging encourages copying errors without a secret/data check.**  
    **Slide:** slide 29 (data-n 25).  
    **Evidence:** Title: “When something breaks, paste the error…” Body: “Copy the error → Paste it to the agent.” No redaction warning.  
    **Why it matters:** Errors and screenshots can contain API keys, authorization headers, account identifiers, local paths, or confidential data.  
    **Proposed fix:** Rewrite the visible sequence:
    **“Capture the problem → Remove secrets/private data → Ask the agent → Repeat the failed test.”**
   
    Suggested prompt:
    > “When I [action], I expected [result], but saw [result]. Here is the error with secrets removed: [text]. Explain the likely cause in plain words and propose a fix.”
   
    Add: **“Never paste `.env`, passwords, keys, or customer information.”**

21. **P1 · Storyline — Debugging is taught after both builds; the retry advice is generalized beyond its evidence.**  
    **Slides:** slide 27 (data-n 24a), slide 28 (data-n 24b), slide 29 (data-n 25).  
    **Evidence:** Both builds precede the debugging slide. Notes on slide 29 say: “If the agent seems stuck for two minutes, stop it and re-send.” The measured retry behavior in `prompts/s1.md` concerns `/init`, not arbitrary builds or pushes.  
    **Why it matters:** Learners first need the recovery habit during the first build. Re-sending a whole build request can duplicate work or repeat a side effect; a permission dialog is not a stall.  
    **Proposed fix:** Move the debugging slide immediately before Run 3. Separate cases:
    - **Waiting for permission:** inspect the request.
    - **`/init` inactive for two minutes:** follow the tested Esc/retry procedure.
    - **Build/push unclear or inactive:** pause and ask the facilitator to inspect progress before restarting.
   
    Clarify “check it worked” as **repeat the exact failed action and rerun the earlier dashboard/chatbot checks**.

22. **P1 · Quality — Repeated whole-run titles obscure what participants should do on the current page.**  
    **Slides:** slide 15 (data-n 14a), slide 16 (data-n 14b), slide 23 (data-n 21a), slide 24 (data-n 21b), slide 27 (data-n 24a), slide 28 (data-n 24b).  
    **Evidence:** Slide 15 promises “add AGENTS.md with one rule, and push,” but only contains signup and `/init`. Both Run 3 pages share the whole-run title, although slide 27 builds only the dashboard. Screenshot `28_n24b_step0.png` also has a smaller title treatment than `27_n24a_step0.png`.  
    **Why it matters:** Participants cannot tell whether they have missed a step or should proceed beyond the visible instructions. Long repeated titles consume space needed for operational guidance.  
    **Proposed titles:**
    - Slide 15: **“Run 1A: Sign in to GitHub and create the project instruction file”**
    - Slide 16: **“Run 1B: Add your rule and upload the project to a private repository”**
    - Slide 23: **“Run 2A: Agree the dashboard requirements and save the spec”**
    - Slide 24: **“Run 2B: Review the plan, then save it without building”**
    - Slide 27: **“Run 3A: Build, open, and check the dashboard”**
    - Slide 28: **“Run 3B: Add and test the chatbot, then push safely”**
   
    On slide 23, also change **“Five questions”** to **“Up to five questions, one at a time”**: the prompt permits fewer; the five-question result is a test observation, not a guarantee.

## Add or cut

- **Add a one-page “Where do I do this?” guide:** distinguish opencode, browser app, GitHub website, project folder, and local settings file. It would eliminate repeated context-switch confusion.
- **Add the actual handout, recovery links, and approved sign-in procedure before delivery.** They are essential parts of the runs, not optional supplementary material.
- **Add a short safety/readiness gate before Run 1:** approved accounts/providers, public training data only, private repository check, permission judgment, and key-handling rules.
- **Add a participant-readable acceptance checklist** for dashboard data, chatbot grounding/refusal, and safe push. Use it again at the end.
- **Move debugging before Run 3; cut blanket “Allow it” language and unconditional two-minute build retries.**
- **Cut repeated whole-run titles and avoid forcing every participant to “correct one thing” when the document is already right.** Ask them to find and correct a genuine mismatch, or explicitly confirm that none exists.