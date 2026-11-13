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

## Open items

- Participant handouts and the `verify.mjs` checker referenced in the project log
  are not in this repository.
- A licence has not yet been chosen.
