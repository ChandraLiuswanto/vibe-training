# vibe-training

Day 3 of **AI Vibe Coding for Business Users**: three training sessions,
with single-file HTML decks for business users building a Financial App.

## Decks and supporting assets

| Path | Status |
| --- | --- |
| [decks/day3-s1-v3.html](decks/day3-s1-v3.html) | Current Session 1 deck, 33 slides |
| [decks/day3-s1-v2.html](decks/day3-s1-v2.html) | Previous Session 1 deck, 32 slides |
| [decks/day3-s1-v1.html](decks/day3-s1-v1.html) | Previous Session 1 deck |
| [decks/day3-s1.html](decks/day3-s1.html) | Byte-identical copy of v1, kept for existing links |
| [decks/day3-s2.html](decks/day3-s2.html) | Session 2 deck, 27 slides (v3: review fixes, worked examples) |
| [decks/day3-s3.html](decks/day3-s3.html) | Session 3 deck, 22 slides |
| [decks/session-1-external-data-visual.html](decks/session-1-external-data-visual.html) | Visual track, Session 1: Frankfurter FX + Google Drive MCP, 18 slides. Not a replacement for `day3-s*`: the visual track covers different topics |
| [decks/session-2-access-control-visual.html](decks/session-2-access-control-visual.html) | Visual track, Session 2: login, roles, admin page and audit trail, 18 slides |
| [decks/session-3-vps-deployment-visual.html](decks/session-3-vps-deployment-visual.html) | Visual track, Session 3: native VPS deployment, 16 slides. Outlines: `docs/outlines/session-*-visual.md` |
| [handouts/](handouts/) | Visual track participant sheets, one per session (`session-N-participant-sheet.html`): printable, two A4 pages each. The facilitator hands them out before practice |
| [demos/git-basics.html](demos/git-basics.html) | Reusable Git demo |
| [.frontend-slides/slide-previews/](.frontend-slides/slide-previews/) | Three style options used to choose Swiss Modern |

## Present a deck

Open the HTML file in a browser. No build step is needed.

- **→ / Space / PageDown**: next slide.
- **← / PageUp**: previous slide.
- **Home / End**: first / last slide.
- **S**: presenter window with notes and timer.
- **N**: notes bar.
- **#N** in the URL: jump to slide N (for example, `#5`).

Fonts (Archivo, Nunito, JetBrains Mono; SIL Open Font License 1.1) are embedded
in every current deck (S1 v3, S1 v2, S2, S3), so they present offline with no
network requests. The legacy v1 deck still loads Google Fonts.

## Build or revise decks

`presentation-creator` handles the story and approved outline; `frontend-slides`
builds the HTML; `clarity` polishes wording after outline approval.
See [AGENTS.md](AGENTS.md) for the rules and skill provisioning, including the
pinned [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) source.

## Planning and history

- [Design spec](docs/superpowers/specs/2026-11-11-day3-design.md)
- [Build plan](docs/superpowers/plans/2026-11-11-day3-build.md)
- [Outlines](docs/outlines/) and [slide copy](docs/copy/)
- [Project log](docs/project-log.md)

## Check the visual track decks

```bash
node tools/day4-deck-check.mjs                 # all three decks and the sheets
node tools/day4-deck-check.mjs --only=s3       # one deck: s1, s2, s3, or sheets
node tools/day4-s3-sync.mjs --check            # Session 3 keeps each slide twice; this confirms the copies match
```

Session 3 stores every slide both as a section and in its `deck-data` JSON. After
editing a Session 3 section, run `node tools/day4-s3-sync.mjs` to rebuild the JSON copy.

The practice prompts in all three visual track decks are untested and are labelled so.
Rehearse them before class.

## Open items

- The visual track participant sheets are in `handouts/`. The Day 3 participant handouts
  and the `verify.mjs` checker referenced in the project log are not in this repository.
- A licence has not yet been chosen.
