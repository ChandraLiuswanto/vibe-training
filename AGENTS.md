# vibe-training

## HTML slide decks

Default deck output is a single self-contained HTML file. Two project skills split the work:

1. **`presentation-creator`** owns the story: brief, story spine, headline-only outline, slide copy, speaker notes. Ignore its Marp default and its visual system.
2. **`frontend-slides`** owns the HTML: style previews, layout, type, animation, the single `.html` file. Pass it the approved outline and copy; it must not add slides, bullets or claims. Pick its "Low density / speaker-led" mode for presented decks and "High density / reading-first" for read-alone ones.

Use `building-presentation-decks` only when the user asks for a `.pptx`. Use `clarity` to polish wording after the outline is approved, not to rebuild the outline.

### Rules for every deck

- **Story gate:** show the user the headline-only slide sequence and get approval before building. Every slide serves a spine beat or a learning objective; otherwise cut it.
- **Titles:** content slides use full-sentence assertions ("Push sends your commits to the shared copy"), not topic labels or questions. Exercise and quiz prompts may be questions in the body.
- **Word budget:** count visible non-title text, including labels, captions and table text. Speaker notes don't count.
  - Presented: ≤40 words
  - Training explanation: ≤40 per reveal step
  - Exercise or instructions: ≤60
  - Read-alone: ≤80
- **Over budget:** split the slide, move narration to speaker notes, or use a handout. Never shrink the type to fit. Code, commands, quiz choices and essential reference tables may exceed the budget; give a one-line reason in the report.
- **Teaching decks:** prerequisites → worked example → practice → check is a valid spine. Don't force a dramatic arc, invented conflict or contestable thesis.
- **No invented bridges:** never strengthen claims or invent evidence to make the story flow. List placeholders (mock data, unverified numbers) in the final report.
- **Report:** for each slide, give the title, word count, and any budget exception.

The budgets are project defaults, not proven limits. Tune them after real English/Bahasa decks.
