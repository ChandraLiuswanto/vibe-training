# Visual design defaults

Use the user's brand or template when one exists. Otherwise use these defaults.

**Canvas:** 16:9, `prs.slide_width = Inches(13.333)`, `prs.slide_height = Inches(7.5)`. Margins 0.6-0.8". Title band at the top ~1", content area below, and a small footer (section · page).

**Type** (sizes for a projected room; screen-share can go about 2pt smaller, but never below 16pt):

| Role | Size |
|---|---|
| Title | 32-40pt bold |
| Body / card text | 20-28pt |
| Labels inside diagrams | ≥18pt |
| Footer | 12pt (the only small text) |

Fonts: Segoe UI or Calibri for Windows audiences, Aptos for Office 365, and Consolas for code and prompts. Set the font explicitly on every run. At most ~6 lines or ~40 words of body text per slide; the rest goes in the notes.

**Color:** one dark neutral for text (#0F172A), one light canvas (#F8FAFC), one brand/accent color (e.g. #2563EB) for the thing the audience should look at now, plus semantic green #059669, amber #D97706 and red #DC2626 used only for meaning (correct, warning, wrong). Dark-background slides only for title and section breaks.

**Diagrams:** draw them with native shapes (rounded rectangles, arrows, connectors) so each part can be animated. Keep 3-5 boxes per diagram, label them in plain words, and set the reading direction left→right or top→bottom.

**Visual evidence:** prefer real screenshots and charts (python-pptx `add_chart` gives native, editable charts). If you must draw a mock UI from shapes, caption it "Illustration" and mention it in your report.

**Consistency:** make one helper per slide type (title, section, content, diagram, quiz, feedback) and build every slide through them. Same positions on every slide mean less for the eye to search.
