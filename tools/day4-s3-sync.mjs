// Rebuild S3's stored slide copies from its authored sections; never edits prompts.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { chromium } from './deck-check/node_modules/playwright-core/index.mjs';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const file = path.join(root, 'decks/session-3-vps-deployment-visual.html');
const source = fs.readFileSync(file, 'utf8');
const json = /(<script id="deck-data" type="application\/json">)([\s\S]*?)(<\/script>)/;
const match = source.match(json);
if (!match) throw new Error('Missing deck-data');
const data = JSON.parse(match[2]);
const sections = source.match(/<section\b[^>]*class="[^"]*\bslide\b[^"]*"[^>]*>[\s\S]*?<\/section>/g) || [];
if (sections.length !== 16 || data.slides.length !== 16) throw new Error('Expected 16 slides');
function innerDiv(section, cls) {
  const start = new RegExp('<div\\b[^>]*class="' + cls + '"[^>]*>').exec(section);
  if (!start) return '';
  const begin = start.index + start[0].length;
  const tags = /<\/?div\b[^>]*>/g; tags.lastIndex = begin;
  let depth = 1, tag;
  while ((tag = tags.exec(section))) {
    depth += /^<\//.test(tag[0]) ? -1 : 1;
    if (!depth) return section.slice(begin, tag.index);
  }
  throw new Error('Unbalanced div: ' + cls);
}
const browser = await chromium.launch({ executablePath: 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe' });
let changed = 0;
try {
  const page = await browser.newPage({ viewport: { width: 1600, height: 900 } });
  await page.goto(pathToFileURL(file).href);
  await page.evaluate(() => document.fonts.ready);
  const metadata = await page.evaluate(() => [...document.querySelectorAll('.slide')].map(s => ({
    title: s.dataset.title,
    eyebrow: s.querySelector('.eyebrow').textContent.trim(),
    notes: s.querySelector('.speaker-note').textContent.trim(),
    minutes: Number(s.dataset.minutes)
  })));
  for (let i = 0; i < sections.length; i++) {
    await page.evaluate(n => { location.hash = '#slide-' + n; }, i + 1);
    await page.waitForTimeout(550);
    const words = await page.evaluate(() => {
      const s = document.querySelector('.slide.active');
      const out = [], walker = document.createTreeWalker(s, NodeFilter.SHOW_TEXT);
      let n;
      while ((n = walker.nextNode())) {
        const p = n.parentElement;
        if (!p || p.closest('.speaker-note, footer, .foot, script, style, h1, h2') || !p.checkVisibility({ visibilityProperty: true })) continue;
        const v = n.nodeValue.replace(/\s+/g, ' ').trim();
        if (v) out.push(v);
      }
      return out.join(' ').split(/\s+/).filter(w => /[\p{L}\p{N}]/u.test(w)).length;
    });
    const fields = { ...metadata[i], visual: innerDiv(sections[i], 'visual'), actions: innerDiv(sections[i], 'actions'), words };
    for (const [key, value] of Object.entries(fields)) {
      if (data.slides[i][key] === value) continue;
      console.log(`slide ${i + 1}: ${key} differs${key === 'words' ? ` (${data.slides[i][key]} → ${value})` : ''}`);
      data.slides[i][key] = value; changed++;
    }
  }
} finally { await browser.close(); }
if (process.argv.includes('--check')) {
  console.log(changed ? `DIFFERENCES: ${changed} fields` : 'PASS: 0 fields differ');
  process.exitCode = changed ? 1 : 0;
} else {
  fs.writeFileSync(file, source.replace(json, (_, open, old, close) => open + JSON.stringify(data).replace(/<\/script/gi, '<\\/script') + close));
  console.log(`Synced ${changed} fields`);
}
