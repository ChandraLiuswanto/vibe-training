Size: small change (no spec reviewer)

# Day 4 visual decks — material and quality review — design

Status: approved by the owner on 2026-11-17 (popup: "Approve": three reviewers by angle across all three decks, one combined report, no deck edits).
Tags: *(user)* = decided by the owner · *(call)* = coordinator's call, correctable.

## 1. Intent

The owner wants to know how good the three Day 4 decks are before they are taught: whether the material is right, whether the decks are well made, and how easy they are for non-technical business users to follow *(user)*.

Decks under review (`decks/session-*`, Day 4) *(user)*:

- `decks/session-1-external-data-visual.html` — 18 slides, exchange-rate API and Google Drive MCP
- `decks/session-2-access-control-visual.html` — 18 slides, login, roles, admin page, audit trail
- `decks/session-3-vps-deployment-visual.html` — 16 slides, native VPS deployment

Audience of the decks: bank business users with no coding background who build with OpenCode (from the Day 4 Session 2 spec).

## 2. Goals, non-goals, anti-goals

**Goals**
- One combined report at `docs/reviews/2026-11-17-day4-decks-review.md` with a short verdict per deck, a ranked finding list, and a suggested fix for each finding.
- Findings cite the deck and the slide number shown on the slide, and quote the wording or name the screenshot they rest on.
- A plain answer, per deck, to "how easy is this for a non-technical business user", with the slides that are hardest for them.

**Non-goals**
- No edits to any deck, outline, prompt or tool *(user: review only)*.
- The Day 3 decks (`day3-*`) are out of scope.
- No classroom run of the practice prompts. Prompts are read, not executed, and the report says so.

**Anti-goals**
- Findings invented to fill a list, or praise with no evidence.
- A claim that something is technically wrong without saying how it was checked (deck text, project file, or the reviewer's own knowledge, marked as such).
- Jargon in the report that the owner would need to look up.

## 3. Approaches

- **A — three reviewers by angle, each across all three decks (chosen)** *(user)*. Angles: (1) material accuracy and safety habits, (2) storyline and ease for non-technical business users, (3) visual quality and slide craft from screenshots. One reviewer sees all three decks, so it can compare them and spot inconsistent vocabulary between sessions. Matches how the Day 3 decks were reviewed.
- **B — one reviewer per deck.** Simpler split, but each reviewer mixes three kinds of judgment and nobody compares the decks.
- **C — nine reviewers (angle × deck).** Most thorough, three times the cost, and the cross-deck view is lost again.

## 4. How

- **Screenshots first.** One worker renders every slide of the three decks to PNG at the 1600×900 stage size under `.review/day4-shots/<deck>/`, including the open practice-prompt panel where a deck has one. It writes any new script under `.review/` and does not change `tools/` *(call)*.
- **Three read-only reviewers**, created together, working independently so their views do not influence each other. Each gets the deck files, the screenshot folder, the headline outlines in `docs/outlines/session-*-visual.md`, the deck rules in `AGENTS.md`, and the Day 4 Session 2 spec.
- **Severity scale**, the same as earlier reviews in this repo:
  - **P0** — wrong, misleading or ambiguous knowledge, or an unsafe habit. Fix before teaching.
  - **P1** — the idea is right but poorly taught, missing, or in the wrong place; or a slide a non-technical user cannot follow.
  - **P2** — a visual or layout problem that hurts clarity.
  - **P3** — polish.
- **Ease for business users** is judged per slide on: unexplained technical terms, steps that assume earlier knowledge, how much the slide asks the reader to hold at once, and whether the practice instructions can be followed without help.
- **Synthesis.** The coordinator merges the three reviews into the report: removes duplicates, records how many reviewers raised each finding, checks the P0 findings against the deck text and screenshots, and keeps disagreements visible.
- **Known departure, not a finding:** Session 2 uses short titles instead of the `AGENTS.md` full-sentence rule because the owner asked for that *(user, 2026-11-17)*. The current outlines list full-sentence titles; reviewers report what the deck actually shows.

## 5. Left to the builder

- The exact rendering method and file names of the screenshots.
- The order and grouping of findings inside each severity level.
