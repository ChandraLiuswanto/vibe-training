// Coordinator check: smallest visible text per slide, in on-screen px at a 1600x900 viewport.
import { chromium } from '../tools/deck-check/node_modules/playwright-core/index.mjs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
const EDGE = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe';
const decks = { s1: 'decks/session-1-external-data-visual.html', s2: 'decks/session-2-access-control-visual.html', s3: 'decks/session-3-vps-deployment-visual.html' };
const want = { s1: [1, 3, 6, 10, 12], s2: [6, 14], s3: [3, 9, 11, 12] };
const browser = await chromium.launch({ executablePath: EDGE });
for (const [k, f] of Object.entries(decks)) {
  const page = await browser.newPage({ viewport: { width: 1600, height: 900 } });
  for (const n of want[k]) {
    await page.goto(pathToFileURL(path.resolve(f)).href + '#slide-' + n);
    await page.waitForTimeout(700);
    const rows = await page.evaluate(() => {
      const slide = document.querySelector('.slide.active');
      const out = [];
      for (const el of slide.querySelectorAll('*')) {
        const own = [...el.childNodes].filter(c => c.nodeType === 3 && c.textContent.trim()).map(c => c.textContent.trim()).join(' ');
        if (!own) continue;
        const r = el.getBoundingClientRect();
        if (!r.width || !r.height) continue;
        const cs = getComputedStyle(el);
        if (cs.visibility === 'hidden' || +cs.opacity === 0) continue;
        // rendered glyph height relative to the layout font size
        const fs = parseFloat(cs.fontSize);
        let scale = 1; let p = el;
        const m = new DOMMatrix(getComputedStyle(document.querySelector('.deck-stage, .stage, .deck') || document.body).transform);
        scale = m.a || 1;
        const svg = el.closest('svg');
        let px = fs * scale;
        if (svg && el.getBBox) { const bb = el.getBBox(); if (bb.height) px = fs * (r.height / bb.height); }
        out.push({ px: Math.round(px * 10) / 10, color: cs.color === 'rgba(0, 0, 0, 0)' ? cs.fill : (svg ? cs.fill : cs.color), text: own.slice(0, 48) });
      }
      return out.sort((a, b) => a.px - b.px).slice(0, 5);
    });
    console.log(k + ' slide ' + n + ': ' + rows.map(r => `${r.px}px "${r.text}" ${r.color}`).join(' | '));
  }
  await page.close();
}
await browser.close();
