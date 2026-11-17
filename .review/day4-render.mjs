// Day 4 decks: render slides + prompt panels to PNG, extract text/notes/prompts to Markdown.
// Usage: node .review/day4-render.mjs            (render)
//        node .review/day4-render.mjs --check    (verify outputs only)
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '..');
const shots = path.join(here, 'day4-shots');
const texts = path.join(here, 'day4-text');
const DECKS = {
  s1: { file: 'decks/session-1-external-data-visual.html', slides: 18 },
  s2: { file: 'decks/session-2-access-control-visual.html', slides: 18 },
  s3: { file: 'decks/session-3-vps-deployment-visual.html', slides: 16 },
};
const pad = (n) => String(n).padStart(2, '0');
const NL = String.fromCharCode(10);

if (process.argv.includes('--check')) {
  let fails = 0;
  const fail = (m) => { fails++; console.log(`FAIL ${m}`); };
  for (const [key, d] of Object.entries(DECKS)) {
    const dir = path.join(shots, key);
    const files = fs.existsSync(dir) ? fs.readdirSync(dir) : [];
    for (let i = 1; i <= d.slides; i++) if (!files.includes(`s${pad(i)}.png`)) fail(`${key} missing s${pad(i)}.png`);
    for (const f of files.filter((f) => /\.png$/.test(f))) {
      if (fs.statSync(path.join(dir, f)).size < 15 * 1024) fail(`${key}/${f} is under 15 KB`);
    }
    if (!files.some((f) => /^p\d\d\.png$/.test(f))) fail(`${key} has no pNN.png`);
    const md = path.join(texts, `${key}.md`);
    if (!fs.existsSync(md)) { fail(`${key} text file missing`); continue; }
    const t = fs.readFileSync(md, 'utf8');
    for (let i = 1; i <= d.slides; i++) {
      const n = t.split(NL).filter((l) => l.trim().startsWith(`## Slide ${i}:`)).length;
      if (n !== 1) fail(`${key}.md has ${n} headings for Slide ${i}`);
    }
    if (!/^## Practice prompts\s*$/m.test(t)) fail(`${key}.md lacks "## Practice prompts"`);
  }
  console.log(fails ? `FAILED: ${fails}` : 'PASS');
  process.exit(fails ? 1 : 0);
}

const { chromium } = await import(pathToFileURL(path.join(root, 'tools/deck-check/node_modules/playwright-core/index.mjs')).href);
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const wc = (t) => (t || '').split(/\s+/).filter((w) => /[\p{L}\p{N}]/u.test(w)).length;

// Visible text of the active slide; skips notes, footer, scripts, hidden elements.
const collect = (skipHeadings) => {
  const s = document.querySelector('.slide.active');
  if (!s) return '';
  const skip = '.speaker-note, footer, .foot, script, style' + (skipHeadings ? ', h1, h2' : '');
  const out = [];
  const w = document.createTreeWalker(s, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = w.nextNode())) {
    const p = n.parentElement;
    if (!p || p.closest(skip)) continue;
    if (!p.checkVisibility({ visibilityProperty: true })) continue;
    const v = n.nodeValue.replace(/\s+/g, ' ').trim();
    if (v) out.push(v);
  }
  return out.join(' ');
};

const browser = await chromium.launch({ executablePath: 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe' });
const fence = (t) => '````text\n' + t + '\n````';

for (const [key, d] of Object.entries(DECKS)) {
  const outDir = path.join(shots, key);
  fs.rmSync(outDir, { recursive: true, force: true });
  fs.mkdirSync(outDir, { recursive: true });
  fs.mkdirSync(texts, { recursive: true });
  const ctx = await browser.newContext({ viewport: { width: 1600, height: 900 } });
  const page = await ctx.newPage();
  page.on('request', (r) => { if (!/^(file|data):/i.test(r.url())) console.log(`NETWORK ${r.url()}`); });
  page.on('pageerror', (e) => console.log(`PAGEERROR ${key}: ${e}`));
  await page.goto(pathToFileURL(path.join(root, d.file)).href);
  await sleep(400);

  const meta = await page.evaluate(() => {
    const slides = [...document.querySelectorAll('.slide')];
    const promptsSrc = typeof prompts !== 'undefined' ? prompts : data.prompts;
    return {
      n: slides.length,
      notes: slides.map((s) => [...s.querySelectorAll('.speaker-note')].map((e) => e.textContent.trim()).join('\n\n')),
      prompts: promptsSrc.map((p) => ({ id: p.id, title: p.title, text: p.text })),
      opens: slides.map((s) => [...s.querySelectorAll('[data-prompt]')].map((e) => e.dataset.prompt)),
    };
  });
  if (meta.n !== d.slides) console.log(`WARN ${key}: expected ${d.slides} slides, found ${meta.n}`);

  let md = `# ${key} — ${d.file}\n\n`;
  for (let i = 1; i <= meta.n; i++) {
    await page.evaluate((n) => { location.hash = '#slide-' + n; }, i);
    await sleep(900); // 0.45s arrive animation plus margin
    // Reveal steps: the decks have no in-slide reveal mechanism; advance any element
    // marked as a reveal that is still hidden, and count them.
    let steps = 0;
    for (let guard = 0; guard < 20; guard++) {
      const hidden = await page.evaluate(() => [...document.querySelectorAll('.slide.active [data-reveal], .slide.active [data-step], .slide.active .reveal, .slide.active .fragment')]
        .filter((e) => !e.checkVisibility({ visibilityProperty: true, opacityProperty: true })).length);
      if (!hidden) break;
      await page.keyboard.press('ArrowRight'); steps++; await sleep(500);
    }
    const info = await page.evaluate(() => {
      const a = document.querySelector('.slide.active');
      const h = a.querySelector('h1, h2');
      return { title: h ? h.innerText.replace(/\s+/g, ' ').trim() : '', dt: a.dataset.title || '', idx: [...document.querySelectorAll('.slide')].indexOf(a) + 1 };
    });
    if (info.idx !== i) console.log(`WARN ${key}: asked for slide ${i}, active is ${info.idx}`);
    const text = await page.evaluate(collect, false);
    const body = await page.evaluate(collect, true);
    const overflow = await page.evaluate(() => { const a = document.querySelector('.slide.active'); return a.scrollHeight > a.clientHeight + 2 || a.scrollWidth > a.clientWidth + 2; });
    await page.screenshot({ path: path.join(outDir, `s${pad(i)}.png`) });
    console.log(`${key} slide ${pad(i)} reveal-steps=${steps}${overflow ? ' OVERFLOW' : ''} "${info.title}"`);
    md += `## Slide ${i}: ${info.title || info.dt}\n\n- data-title: ${info.dt}\n- Visible word count (excluding title and footer): ${wc(body)}\n- Reveal steps advanced: ${steps}\n- Screenshot: s${pad(i)}.png\n\n**Visible text**\n\n${fence(text)}\n\n**Speaker notes**\n\n${meta.notes[i - 1] || data_notes_fallback(i)}\n\n`;
  }
  function data_notes_fallback() { return '(none)'; }

  md += `## Practice prompts\n\n`;
  for (let k = 0; k < meta.prompts.length; k++) {
    const p = meta.prompts[k];
    await page.evaluate((id) => { promptDialog(id); }, p.id);
    await sleep(500);
    const shown = await page.evaluate(() => document.getElementById('prompt-text')?.textContent || '');
    if (shown.trim() !== p.text.trim()) console.log(`WARN ${key}: #prompt-text differs from source for ${p.id}`);
    await page.screenshot({ path: path.join(outDir, `p${pad(k + 1)}.png`) });
    await page.evaluate(() => document.getElementById('modal').close());
    const from = meta.opens.map((o, i) => (o.includes(p.id) ? i + 1 : 0)).filter(Boolean);
    md += `### p${pad(k + 1)} — ${p.title}\n\n- id: ${p.id}\n- Opens from slide: ${from.length ? from.join(', ') : 'none (prompt pack only)'}\n- Screenshot: p${pad(k + 1)}.png (panel is scrollable; the text below is complete)\n\n${fence(p.text)}\n\n`;
  }
  fs.writeFileSync(path.join(texts, `${key}.md`), md);
  await ctx.close();
  console.log(`${key}: ${meta.n} slides, ${meta.prompts.length} prompts`);
}
await browser.close();
