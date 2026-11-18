# SDD ledger — plan: docs/superpowers/plans/2026-11-18-day4-decks-fixes.md

- Human decisions before the spec: ask-first approach B (reword and add an ask-first setting); Session 3 look approach A (restyle in place); workers are Sol ("spawn sol subagents as needed").
- Checkout: branch autopilot/day4-decks-fixes created from main.
- Spec review r1 (cc/claude-fable-5-2, medium): NOT READY, 1 BLOCKING (S3 prompt text is also stored in `pack`), 4 MINOR. All five confirmed against the decks and fixed in the spec.
- Spec review r2 (cc/claude-fable-5-2, medium, fresh reviewer): READY TO PLAN, 5 MINOR, all fixed in the spec (word-count rule, scope of the spelling bans, all S3 animation removed, S2 checklist item, outline and README stale lines).
- Human approved the reviewed spec (the one gate), 2026-11-18.
- Decision: how does the S3 worker keep the two copies of each slide in step? — a small helper tools/day4-s3-sync.mjs rebuilds the JSON copies from the sections; verified first that the JSON `visual` strings appear verbatim in the section source for all 16 slides — main
- Decision: how do parallel deck workers get screenshots without clobbering each other? — the check script gets a --shots option that writes only the folders of the decks in scope, under .review/day4-fix-shots/ (git-ignored); workers do not run .review/day4-render.mjs — main
- Decision: add check 14 (keyboard navigation and notes) beyond the spec's 13 — yes, from the plan's Review Focus; it is a test, not new scope — main
