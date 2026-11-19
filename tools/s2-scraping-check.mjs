// Checks for decks/session-2-web-scraping-visual.html (Day 4 S2 rebuild).
// node tools/s2-scraping-check.mjs [--shots]   → screenshots in .scratch/s2-rebuild/shots
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { chromium } from './deck-check/node_modules/playwright-core/index.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const deckPath = path.join(root, 'decks/session-2-web-scraping-visual.html');
const copyPath = path.join(root, 'docs/copy/day4-s2-web-scraping.md');
const shots = process.argv.includes('--shots');
const shotDir = path.join(root, '.scratch/s2-rebuild/shots');
const EXPECTED = 23;
const BUDGET = n => (n >= 20 ? 60 : 40);
const BUDGET_EXCEPT = {};

let failures = 0;
const fail = (check, slide, msg) => { failures++; console.log(`FAIL ${check} slide ${slide}: ${msg}`); };
const norm = s => (s || '').replace(/\s+/g, ' ').trim();
const wc = s => (s || '').split(/\s+/).filter(w => /[\p{L}\p{N}]/u.test(w)).length;

const copyTitles = [...fs.readFileSync(copyPath, 'utf8').matchAll(/^## (\d+) · (.+)$/gm)].map(m => m[2].trim());

// Visible text on the active slide (same rules as day4-deck-check.mjs collect()).
function collect(skipHeadings) {
  const s = document.querySelector('.slide.active');
  const skip = '.speaker-note, footer, .foot, script, style' + (skipHeadings ? ', h1, h2' : '');
  const out = [], walker = document.createTreeWalker(s, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = walker.nextNode())) {
    const p = n.parentElement;
    if (!p || p.closest(skip) || !p.checkVisibility({ visibilityProperty: true, opacityProperty: true })) continue;
    const v = n.nodeValue.replace(/\s+/g, ' ').trim();
    if (v) out.push(v);
  }
  return out.join(' ');
}

function bounds() {
  const s = document.querySelector('.slide.active'), r = s.getBoundingClientRect(), out = [];
  const bar = document.getElementById('controls')?.getBoundingClientRect();
  const foot = s.querySelector('.foot')?.getBoundingClientRect();
  for (const el of s.querySelectorAll('*')) {
    if (el.closest('.speaker-note,script,style,.foot') || !el.checkVisibility({ visibilityProperty: true, opacityProperty: true })) continue;
    const b = el.getBoundingClientRect();
    if (!b.width || !b.height) continue;
    const name = el.tagName.toLowerCase() + (typeof el.className === 'string' && el.className ? '.' + el.className.trim().split(/\s+/)[0] : '');
    if (b.left < r.left - 1 || b.top < r.top - 1 || b.right > r.right + 1 || b.bottom > r.bottom + 1) out.push(name + ' outside stage');
    if (foot && b.bottom > foot.top + 1 && !el.closest('.foot')) out.push(name + ' overlaps footer');
    // Clipped inside an overflow box (content cut off without leaving the stage).
    if ((el.scrollHeight > el.clientHeight + 2 || el.scrollWidth > el.clientWidth + 2) && ['hidden', 'clip'].includes(getComputedStyle(el).overflowY) && el.clientHeight > 0) out.push(name + ' clips its content');
    // Text that overflows its own box.
    if (el.childNodes.length && [...el.childNodes].some(c => c.nodeType === 3 && c.textContent.trim()) && el.scrollWidth > el.clientWidth + 2 && getComputedStyle(el).display !== 'inline') out.push(name + ' text wider than its box');
  }
  return out;
}

function smallText() {
  const s = document.querySelector('.slide.active'), out = [];
  const stage = document.getElementById('stage');
  const scale = new DOMMatrix(getComputedStyle(stage).transform).a || 1;
  for (const el of s.querySelectorAll('*')) {
    if (el.closest('.speaker-note, .foot, .s2-illus')) continue;
    const own = [...el.childNodes].filter(c => c.nodeType === 3 && c.textContent.trim()).map(c => c.textContent.trim()).join(' ');
    if (!own || !el.checkVisibility({ visibilityProperty: true })) continue;
    const px = parseFloat(getComputedStyle(el).fontSize);
    if (px < 22) out.push(`${px}px "${own.slice(0, 40)}"`);
  }
  return out;
}

const browser = await chromium.launch({ executablePath: '/usr/bin/google-chrome' });
try {
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, acceptDownloads: true });
  const errors = [];
  page.on('console', m => { if (m.type() === 'error') errors.push('console error: ' + m.text()); });
  page.on('pageerror', e => errors.push('page error: ' + e));
  page.on('request', r => { if (!/^(file|data|blob):/i.test(r.url())) errors.push('network request: ' + r.url()); });
  await page.goto(pathToFileURL(deckPath).href);
  await page.evaluate(() => document.fonts.ready);
  const go = async n => { await page.evaluate(n => { location.hash = '#slide-' + n; }, n); await page.waitForTimeout(350); };
  const key = async k => { await page.keyboard.press(k); await page.waitForTimeout(320); };

  // 1. Structure
  const meta = await page.evaluate(() => {
    const d = JSON.parse(document.getElementById('deck-data').textContent);
    return { data: d.slides.map(s => s.title), slides: [...document.querySelectorAll('.slide')].map(s => ({ title: s.dataset.title, heading: s.querySelector('h1,h2')?.textContent, steps: s.querySelectorAll('[data-step]').length, minutes: +s.dataset.minutes, notes: s.querySelector('.speaker-note')?.textContent.trim() })) };
  });
  if (meta.slides.length !== EXPECTED) fail(1, 0, `expected ${EXPECTED} slides, found ${meta.slides.length}`);
  if (meta.data.length !== meta.slides.length) fail(1, 0, `deck-data has ${meta.data.length} slides`);
  meta.slides.forEach((m, i) => {
    const n = i + 1;
    if (norm(m.heading) !== norm(m.title)) fail(1, n, 'heading differs from data-title');
    if (m.title !== meta.data[i]) fail(1, n, 'data-title differs from deck-data');
    if (norm(m.title) !== norm(copyTitles[i])) fail(1, n, `title differs from copy deck: "${copyTitles[i]}"`);
    if (!/\.$/.test(m.title)) fail(1, n, 'title is not a sentence');
    if (!m.notes) fail(1, n, 'no speaker notes');
  });
  const minutes = meta.slides.reduce((a, m) => a + m.minutes, 0);
  if (minutes < 55 || minutes > 60) fail(7, 0, `talk minutes ${minutes} outside 55–60`);

  // 2–4. Every click state: words, bounds, small text, screenshots
  if (shots) { fs.rmSync(shotDir, { recursive: true, force: true }); fs.mkdirSync(shotDir, { recursive: true }); }
  const report = [];
  for (const [w, h] of [[1920, 1080], [1280, 720]]) {
    await page.setViewportSize({ width: w, height: h });
    await go(1);
    for (let i = 0; i < meta.slides.length; i++) {
      const n = i + 1, steps = meta.slides[i].steps;
      await page.evaluate(() => document.querySelectorAll('.slide.active [data-step]').forEach(e => e.classList.remove('shown')));
      for (let st = 0; st <= steps; st++) {
        if (st > 0) { await key('ArrowRight'); }
        const cur = await page.evaluate(() => [...document.querySelectorAll('.slide')].findIndex(s => s.classList.contains('active')) + 1);
        if (cur !== n) fail(4, n, `step ${st}: → moved to slide ${cur} before all steps were shown`);
        if (w === 1920) {
          const words = wc(await page.evaluate(collect, true));
          if (st === steps) report.push({ n, title: meta.slides[i].title, words, steps });
          if (words > BUDGET(n) && !BUDGET_EXCEPT[n]) fail(2, n, `${words} visible words (max ${BUDGET(n)})`);
          for (const t of await page.evaluate(smallText)) fail(9, n, `small text ${t}`);
        }
        for (const b of [...new Set(await page.evaluate(bounds))]) fail(3, n, `${w}x${h} step ${st}: ${b}`);
        if (shots) await page.screenshot({ path: path.join(shotDir, `${w}-s${String(n).padStart(2, '0')}-${st}.png`) });
      }
      if (steps) {
        for (let st = steps; st > 0; st--) await key('ArrowLeft');
        const left = await page.evaluate(() => document.querySelectorAll('.slide.active [data-step].shown').length);
        const cur = await page.evaluate(() => [...document.querySelectorAll('.slide')].findIndex(s => s.classList.contains('active')) + 1);
        if (left || cur !== n) fail(4, n, `← did not undo steps (shown ${left}, slide ${cur})`);
        for (let st = 0; st < steps; st++) await key('ArrowRight');
      }
      if (n < meta.slides.length) await key('ArrowRight');
    }
  }

  // Phone width (portrait), slide frame only
  await page.setViewportSize({ width: 390, height: 844 });
  for (const n of [1, 5, 10, 13]) { await go(n); if (shots) await page.screenshot({ path: path.join(shotDir, `phone-s${String(n).padStart(2, '0')}.png`) }); }
  await page.setViewportSize({ width: 1920, height: 1080 });

  // 4b. Quizzes write to their own slide
  await go(15);
  if (await page.locator('.slide.active [data-step]').count() !== 3) fail(4, 15, 'expected three recap reveals');
  await go(5);
  if (await page.locator('.slide.active .s2-rung:visible').count() !== 6 || await page.locator('.slide.active [data-step]').count()) fail(4, 5, 'all ladder rungs must be visible on arrival');

  // 5. Prompt modal, copy, downloads, print
  await page.click('#controls [data-action="prompts"]');
  await page.waitForTimeout(200);
  const btns = await page.evaluate(() => [...document.querySelectorAll('#modal [data-download]')].map(b => b.dataset.download));
  for (const k of ['pack', 'rss', 'sample']) if (!btns.includes(k)) fail(5, 0, `prompt menu lacks ${k} download`);
  for (const [k, name] of [['pack', 'session-2-web-scraping-prompt.txt'], ['rss', 'sample-news-feed.xml'], ['sample', 'sample-news-page.html']]) {
    const [dl] = await Promise.all([page.waitForEvent('download'), page.click(`#modal [data-download="${k}"]`)]);
    if (dl.suggestedFilename() !== name) fail(5, 0, `download ${k} named ${dl.suggestedFilename()}`);
    const text = fs.readFileSync(await dl.path(), 'utf8');
    if (k === 'rss' && (text.match(/<item>/g) || []).length !== 3) fail(5, 0, 'sample feed does not have 3 items');
    if (k === 'sample' && (text.match(/BBCA/g) || []).length < 2) fail(5, 0, 'sample page titles do not name BBCA');
    if (k === 'pack' && !/STAGE 2 · READ THE FEED/.test(text)) fail(5, 0, 'prompt pack is not the feed-first prompt');
  }
  await page.click('#modal [data-prompt="news"]');
  await page.waitForTimeout(200);
  const promptText = await page.evaluate(() => document.getElementById('prompt-text')?.textContent || '');
  for (const must of ['FinancialAppTraining/1.0', 'no proxies, no CAPTCHA solving', 'Just a moment', 'sample-news-feed.xml']) if (!promptText.includes(must)) fail(5, 0, `prompt lacks "${must}"`);
  await page.click('#close-modal');
  await go(22);
  await page.click('.slide.active [data-action="help"]');
  const help = await page.evaluate(() => document.getElementById('modal-body').textContent);
  if (/Antara is a candidate/.test(help) || !/Start with a feed/.test(help)) fail(5, 24, 'help dialog still has the old wording');
  await page.click('#close-modal');
  await page.emulateMedia({ media: 'print' });
  const printPre = await page.evaluate(() => document.querySelector('.print-prompts pre')?.textContent || '');
  if (!printPre.includes('STAGE 2 · READ THE FEED')) fail(5, 0, 'print block has the old prompt');
  const hiddenInPrint = await page.evaluate(() => [...document.querySelectorAll('[data-step]')].filter(e => getComputedStyle(e).opacity !== '1').length);
  if (hiddenInPrint) fail(5, 0, `${hiddenInPrint} reveal steps hidden in print`);
  await page.emulateMedia({ media: 'screen' });

  // 6. No external requests, no errors
  errors.forEach(e => fail(6, 0, e));

  console.log('\nSlide | words (final state) | steps | title');
  report.forEach(r => console.log(`${String(r.n).padStart(2)} | ${String(r.words).padStart(3)}${BUDGET_EXCEPT[r.n] ? ' (exception: ' + BUDGET_EXCEPT[r.n] + ')' : ''} | ${r.steps} | ${r.title}`));
  console.log(`\nTalk minutes: ${minutes}`);
} finally {
  await browser.close();
}
console.log(failures ? `\n${failures} FAIL` : '\nPASS');
process.exit(failures ? 1 : 0);
