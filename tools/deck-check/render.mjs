// Render check for the slide deck. Usage:
//   node tools/deck-check/render.mjs DECK.html [--slides 1-4] [--out DIR] [--reduced-motion]
// Checks per slide, per step, at 1920x1080 and 1280x720: (a) bounds, (b) font size,
// (c) word count, (d) step PNG differs from previous step, (e) prev() restores the previous step's .in set,
// (f) at step 0: controls in not-yet-shown [data-step] are inert, and Space on a visible .prompt button does not advance.
import { chromium } from 'playwright-core';
import { mkdirSync, writeFileSync } from 'node:fs';
import { resolve, join } from 'node:path';
import { pathToFileURL } from 'node:url';

const EDGE = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe';
const SIZES = [[1920, 1080], [1280, 720]];
const WAIT = 2200;

const args = process.argv.slice(2);
const flag = (n) => args.includes(n);
const opt = (n, d) => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : d; };
const deckPath = args.find((a, i) => !a.startsWith('--') && (i === 0 || !['--slides', '--out'].includes(args[i - 1])));
if (!deckPath) { console.error('usage: render.mjs DECK.html [--slides a-b] [--out DIR] [--reduced-motion]'); process.exit(2); }
const out = resolve(opt('--out', '.review/shots'));
const range = opt('--slides', null);
mkdirSync(out, { recursive: true });

// Runs in the page. Returns problems for the active slide at the current step.
function inspect() {
  const stage = document.querySelector('.deck-stage');
  const sr = stage.getBoundingClientRect();
  const slide = document.querySelector('.slide.active');
  const probs = [];
  const vis = (el) => el.checkVisibility({ checkOpacity: true, checkVisibilityCSS: true });
  const scale = sr.width / 1920;
  const tol = 2;
  const lab = (el) => el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/)[0] : '');
  for (const el of [slide, ...slide.querySelectorAll('*')]) {
    if (!vis(el)) continue;
    const r = el.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) continue;
    if (r.left < sr.left - tol || r.top < sr.top - tol || r.right > sr.right + tol || r.bottom > sr.bottom + tol)
      probs.push(`bounds ${lab(el)}`);
  }
  // (b) font size on elements with own visible text
  const small = new Set();
  for (const el of slide.querySelectorAll('*')) {
    if (!vis(el) || el.closest('.prompt, .chip, .pg, .steps-ind, script, style')) continue;
    if (![...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim())) continue;
    const fs = parseFloat(getComputedStyle(el).fontSize);
    if (fs < 28) small.add(`${lab(el)}=${fs}px`);
  }
  for (const s of small) probs.push(`font ${s}`);
  // (c) word count of visible non-title text
  let words = 0;
  const w = document.createTreeWalker(slide, NodeFilter.SHOW_TEXT);
  for (let n; (n = w.nextNode());) {
    const p = n.parentElement;
    if (!p || !n.textContent.trim() || !vis(p)) continue;
    if (p.closest('h1, h2, .prompt, .choices, .pg, .steps-ind, script, style, button')) continue;
    words += n.textContent.trim().split(/\s+/).length;
  }
  const attr = slide.getAttribute('data-words-max');
  const limit = attr ? +attr : (slide.querySelector('.ho, .choices') ? 60 : 40);
  if (words > limit) probs.push(`words ${words}>${limit}`);
  // (f) focusable controls in hidden steps must be unreachable (inert)
  for (const st of slide.querySelectorAll('[data-step]:not(.in)'))
    for (const el of st.querySelectorAll('button, a, [tabindex]'))
      if (!el.closest('[inert]')) probs.push(`focus-hidden ${lab(el)}`);
  const inSet = [...slide.querySelectorAll('.in')].map((e) => e.outerHTML.slice(0, 80) + '#' + [...e.parentNode.children].indexOf(e)).join('|');
  return { probs, inSet, n: slide.dataset.n, steps: window.__deck.maxStep(), hasChoices: !!slide.querySelector('.choices') };
}

const browser = await chromium.launch({ executablePath: EDGE, headless: true });
let failed = 0, pngs = 0;
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
for (const [W, H] of SIZES) {
  const ctx = await browser.newContext({ viewport: { width: W, height: H }, reducedMotion: flag('--reduced-motion') ? 'reduce' : 'no-preference' });
  const page = await ctx.newPage();
  page.on('pageerror', (e) => console.error('pageerror', e.message));
  await page.goto(pathToFileURL(resolve(deckPath)).href);
  await page.waitForFunction(() => window.__deck);
  const total = await page.evaluate(() => document.querySelectorAll('.slide').length);
  let [a, b] = range ? range.split('-').map(Number) : [1, total];
  if (b === undefined || Number.isNaN(b)) b = a;
  for (let pos = a; pos <= Math.min(b, total); pos++) {
    await page.evaluate((p) => window.__deck.go(p), pos - 1);
    await sleep(WAIT);
    let prevPng = null, prevSet = null;
    const meta0 = await page.evaluate(inspect);
    const lastStep = meta0.steps + (meta0.hasChoices ? 1 : 0);
    for (let k = 0; k <= lastStep; k++) {
      if (k > 0) { await page.evaluate(() => window.__deck.next()); await sleep(WAIT); }
      const r = await page.evaluate(inspect);
      const probs = [...r.probs];
      if (k === 0) {
        const hasBtn = await page.evaluate(() => {
          const b = [...document.querySelectorAll('.slide.active .prompt button')].find((x) => x.checkVisibility({ checkOpacity: true, checkVisibilityCSS: true }));
          if (!b) return false;
          b.focus();
          return document.activeElement === b;
        });
        if (hasBtn) {
          const before = await page.evaluate(() => window.__deck.step);
          await page.keyboard.press('Space');
          await sleep(300);
          const after = await page.evaluate(() => window.__deck.step);
          if (after !== before) {
            probs.push('space-advances');
            await page.evaluate(([p]) => window.__deck.go(p), [pos - 1]);
            await sleep(WAIT);
          }
          await page.evaluate(() => document.activeElement && document.activeElement.blur());
        }
      }
      const png = await page.screenshot({ path: join(out, `s${String(pos).padStart(2, '0')}-${r.n}-step${k}-${W}.png`) });
      pngs++;
      if (prevPng && Buffer.compare(png, prevPng) === 0) probs.push('same-png-as-previous-step');
      if (k > 0 && k <= r.steps) {
        await page.evaluate(() => window.__deck.prev());
        await sleep(150);
        const back = await page.evaluate(inspect);
        if (back.inSet !== prevSet) probs.push('prev-does-not-restore');
        await page.evaluate(() => window.__deck.next());
        await sleep(150);
      }
      prevPng = png; prevSet = r.inSet;
      const ok = probs.length === 0;
      if (!ok) failed++;
      console.log(`slide ${pos} (n=${r.n}) step ${k} ${W}x${H} ${ok ? 'PASS' : 'FAIL ' + [...new Set(probs)].join('; ')}`);
    }
  }
  await ctx.close();
}
await browser.close();
console.log(`${pngs} PNGs written to ${out}; ${failed} failing result(s)`);
process.exit(failed ? 1 : 0);
