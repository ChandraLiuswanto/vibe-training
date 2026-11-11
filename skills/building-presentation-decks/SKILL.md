---
name: building-presentation-decks
description: Use when asked to create, generate, or improve a slide deck, presentation, or PowerPoint (.pptx), including training, workshop, course, onboarding, or lesson material, business updates, and pitches, especially when animation, click-to-reveal, quizzes, or clickable navigation are wanted.
---

# Building Presentation Decks

## Overview

A deck is a sequence of **click states the audience sees in a room**, not a document. Design the click states first, and generate the .pptx from code second. Then **look at every click state** before you call it done.

Tools (python-pptx; run from `scripts/`, or add the directory to `sys.path`):
- `scripts/pptx_fx.py`: native animations, transitions, Morph, slide links, hidden slides, click-lock. Do not hand-write `<p:timing>` XML.
- `python3 scripts/deck_check.py deck.pptx --render out/`: lints the deck (font size, overflow, IDs, broken links, missing notes) and writes `out/storyboard.png` (one row per slide, one column per click).

## Process

1. **Brief, in 5 lines:** audience, room/medium (projected, shared screen, read alone), duration, and the one decision or ability the audience should leave with. If the deck teaches, add 3-5 measurable objectives ("can explain X", "can do Y").
2. **Storyline:** write only the slide titles. Each one is a full-sentence claim ("Push sends your commits to the shared copy"), not a topic label ("Push"). Read the titles in order: they should tell the whole story.
3. **Teaching decks:** follow the structure in [references/training-design.md](references/training-design.md). It covers hooks, chunking, worked examples, hands-on steps, spaced quiz checks, and the recap.
4. **Build:** follow the layout and type rules in [references/visual-design.md](references/visual-design.md). Every slide gets speaker notes containing what to say and the timing.
5. **Animate for meaning:** use `pptx_fx.animate` to reveal a diagram or process one step per click, in the order you explain it. Use Fade/Appear/Wipe, keep 1-5 clicks per slide, and add a Fade transition. Morph only between two slides that show the same diagram in two states. Never add decorative motion, sound, bounce, or spin.
6. **Interactivity = links, not triggers:** build agenda/menu hubs, "back to menu" buttons, and quizzes as `link()` jumps to feedback slides. Put feedback on hidden slides (`hide_slide`) and `lock_click_advance` the quiz slide. Anything hidden by animation (trigger feedback, an exercise answer that wipes in) shows in a PDF, a handout, Google Slides or a static render. Put answers on the *next* or a hidden slide.
7. **Verify:** run `deck_check.py --render`, fix every ERROR, and fix or justify every WARN. Then **open storyboard.png and read it**. Check what the audience sees at click 0, whether each reveal is in speaking order, and whether anything overlaps.
8. **Report honestly:** list the slides and interactions, list any placeholder (mock screenshots, unverified numbers, invented examples) so the user can replace it, and say that animation timing was checked as a storyboard, not played in PowerPoint.

## pptx_fx in 10 lines

```python
from pptx_fx import animate, step, transition, morph, link, hide_slide, lock_click_advance
animate(s, [step(title),                          # click 1
            step(local_box, arrow, after=[remote_box]),  # click 2: together, then remote
            step((result, "wipe-left"))])         # click 3, other effect
animate(s, [step(hook)], autostart_first=True)   # plays on slide entry
transition(s, "fade")                            # or morph(s) (fades in old viewers)
link(answer_b, correct_slide); link(answer_a, retry_slide); link(back_btn, quiz_slide)
hide_slide(correct_slide); lock_click_advance(quiz_slide)
```
Effects: `appear`, `fade`, `wipe-left/right/up/down`, `fly-bottom/top/left/right`. Each shape can be animated once per slide.

## Common Mistakes

| Mistake | Fix |
|---|---|
| Body text 11-16pt "to fit" | Cut words or split the slide. Use ≥18pt, and ≥24pt for body text in a room |
| Topic titles ("CSV export") | Assertion titles ("Customers can now export to Excel in one click") |
| All quizzes massed at the end | One 1-2 question check after each chunk, plus a recap at the start of the next section |
| Lecture-only training | Every chunk has a "your turn" step the learner does |
| Checking only a PDF render | PDF shows the final state; read the storyboard per click |
| Shape mock-ups shown as if they were product screenshots | Label them as illustrations, or use real screenshots, and tell the user |
| Agenda links with no way back | Every section ends with a link back to the hub |
