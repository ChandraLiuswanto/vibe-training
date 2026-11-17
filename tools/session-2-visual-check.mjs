// Session 2 deck check. Usage: node tools/session-2-visual-check.mjs [deckPath] [--only=1,2,...]
import { chromium } from './deck-check/node_modules/playwright-core/index.mjs';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '..');
const args = process.argv.slice(2);
const onlyArg = args.find((a) => a.startsWith('--only='));
const only = onlyArg ? new Set(onlyArg.slice(7).split(',').map(Number)) : null;
const deckArg = args.find((a) => !a.startsWith('--')) || 'decks/session-2-access-control-visual.html';
const deckPath = path.resolve(process.cwd(), deckArg);
const REF = 'C:/Users/HP/pr-reviews/vibe-training-pr4/decks/session-1-external-data-visual.html';

const TITLES = [
  'Give Every User the Right Access',
  'Continue the app you already built',
  'The business need',
  'Authentication versus authorization',
  'LDAP: the company directory',
  'Mock LDAP for practice',
  'Sign in once, carry a pass',
  'Two roles',
  'Quick check: hidden button',
  'Where the check belongs',
  'The admin page',
  'Audit trail',
  'What to record',
  'Demo: brief, plan, approve, build',
  'Evidence: two accounts',
  'Evidence: the audit trail',
  'Your 60-minute practice',
  'Finish check and next session',
];
const IDS = ['access-plan', 'login-build', 'roles-build', 'admin-build', 'audit-build', 'access-test', 'finish'];
const BANNED = ['Frankfurter', 'Google Drive', 'Session 1', 'csv'];
const HANDOUT = 'Session 2 \u00b7 Practice handout';

let failures = 0;
const want = (n) => !only || only.has(n);
const fail = (check, slide, msg) => {
  failures++;
  console.log(`FAIL ${check}${slide ? ` slide ${slide}` : ''}: ${msg}`);
};
const finish = () => {
  console.log(failures ? `FAILED: ${failures}` : 'PASS');
  process.exit(failures ? 1 : 0);
};
const wc = (t) => (t || '').split(/\s+/).filter((w) => /[\p{L}\p{N}]/u.test(w)).length;
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

if (!fs.existsSync(deckPath)) {
  console.log(`FAIL 0: deck not found: ${deckPath}`);
  console.log('FAILED: 1');
  process.exit(1);
}

const browser = await chromium.launch({
  executablePath: 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
});
const url = pathToFileURL(deckPath).href;
const consoleErrors = [];
const pageErrors = [];
const badRequests = [];

async function openPage(w = 1920, h = 1080, hash = '') {
  const ctx = await browser.newContext({ viewport: { width: w, height: h } });
  const page = await ctx.newPage();
  page.on('console', (m) => { if (m.type() === 'error') consoleErrors.push(m.text()); });
  page.on('pageerror', (e) => pageErrors.push(String(e)));
  page.on('request', (r) => {
    const u = r.url();
    if (!/^(file|data|blob):/i.test(u)) badRequests.push(u);
  });
  await page.goto(url + hash);
  await sleep(250);
  return page;
}
async function go(page, n) {
  await page.evaluate((n) => { location.hash = '#slide-' + n; }, n);
  await sleep(250);
}

// Text of the active slide, one text node at a time, joined with spaces.
// Excludes .speaker-note, footer, script, style; optionally also h1/h2.
const collect = (skipHeadings) => {
  const s = document.querySelector('.slide.active');
  if (!s) return '';
  const skip = '.speaker-note, footer, script, style' + (skipHeadings ? ', h1, h2' : '');
  const out = [];
  const w = document.createTreeWalker(s, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = w.nextNode())) {
    const p = n.parentElement;
    if (!p || p.closest(skip)) continue;
    if (p.checkVisibility && !p.checkVisibility({ visibilityProperty: true })) continue;
    out.push(n.nodeValue);
  }
  return out.join(' ');
};

try {
  const page = await openPage();
  const meta = await page.evaluate(() => [...document.querySelectorAll('.slide')].map((s) => ({
    title: s.getAttribute('data-title'),
    heads: s.querySelectorAll('h1, h2').length,
    notes: [...s.querySelectorAll('.speaker-note')].map((a) => a.textContent),
  })));
  const N = meta.length;

  const slideInfo = [];
  for (let i = 1; i <= N; i++) {
    await go(page, i);
    const info = await page.evaluate(() => {
      const a = document.querySelector('.slide.active');
      const h = a && a.querySelector('h1, h2');
      return { vtitle: h ? h.innerText.replace(/\s+/g, ' ').trim() : '' };
    });
    info.text = await page.evaluate(collect, true);
    info.full = await page.evaluate(collect, false);
    info.words = wc(info.text);
    slideInfo.push(info);
    console.log(`slide ${i} "${info.vtitle}" words=${info.words}`);
  }

  if (want(1)) {
    if (N !== 18) fail(1, 0, `expected 18 slides, found ${N}`);
    meta.forEach((m, i) => {
      const k = i + 1;
      if (!m.title) fail(1, k, 'empty data-title');
      else if (TITLES[i] !== undefined && m.title !== TITLES[i]) fail(1, k, `data-title "${m.title}" != "${TITLES[i]}"`);
      if (m.heads !== 1) fail(1, k, `expected 1 h1/h2, found ${m.heads}`);
      if (m.notes.length !== 1) fail(1, k, `expected 1 speaker-note, found ${m.notes.length}`);
      else {
        const c = wc(m.notes[0]);
        if (c < 35 || c > 90) fail(1, k, `speaker note has ${c} words (35-90)`);
      }
    });
  }

  if (want(2)) {
    slideInfo.forEach((s, i) => {
      const max = i + 1 === 17 ? 60 : 40;
      if (s.words > max) fail(2, i + 1, `${s.words} visible words (max ${max})`);
    });
  }

  if (want(3)) {
    for (const [w, h] of [[1920, 1080], [1280, 720]]) {
      const p = await openPage(w, h);
      for (let i = 1; i <= N; i++) {
        await go(p, i);
        const res = await p.evaluate(() => {
          const s = document.querySelector('.slide.active');
          const out = [];
          if (!s) return ['no active slide'];
          const r = s.getBoundingClientRect();
          for (const el of s.querySelectorAll('*')) {
            if (el.closest('.speaker-note')) continue;
            const b = el.getBoundingClientRect();
            if (!b.width || !b.height) continue;
            if (b.right > r.right + 1 || b.bottom > r.bottom + 1 || b.left < r.left - 1) {
              const cls = typeof el.className === 'string' && el.className ? '.' + el.className.split(/\s+/).join('.') : '';
              out.push(`<${el.tagName.toLowerCase()}${cls}> outside slide`);
              if (out.length >= 3) break;
            }
          }
          if (s.scrollHeight > s.clientHeight + 2) out.push(`scrollHeight ${s.scrollHeight} > clientHeight ${s.clientHeight}`);
          return out;
        });
        res.forEach((m) => fail(3, i, `${w}x${h}: ${m}`));
      }
      await p.context().close();
    }
  }

  let prompts = null;
  if (want(5) || want(6)) {
    try { prompts = await page.evaluate(() => prompts); } catch (e) { fail(5, 0, 'cannot read prompts: ' + e.message.split('\n')[0]); }
  }
  if (want(5) && prompts) {
    if (!Array.isArray(prompts) || prompts.length !== 7) fail(5, 0, `prompts length ${prompts.length}, expected 7`);
    IDS.forEach((id, i) => {
      const p = prompts[i];
      if (!p || p.id !== id) { fail(5, 0, `prompt ${i + 1} id "${p && p.id}" != "${id}"`); return; }
      const c = wc(p.text);
      if (c < 120 || c > 330) fail(5, 0, `prompt "${id}" has ${c} words (120-330)`);
    });
    const dp = await page.evaluate(() => [...document.querySelectorAll('[data-prompt]')].map((e) => e.getAttribute('data-prompt')));
    dp.forEach((v) => { if (!IDS.includes(v)) fail(5, 0, `data-prompt "${v}" is not a known id`); });
    const pp = await page.evaluate(() => {
      const e = document.querySelector('#print-prompts');
      return e ? { n: e.querySelectorAll('article').length, t: e.textContent } : null;
    });
    if (!pp) fail(5, 0, '#print-prompts missing');
    else {
      if (pp.n !== 7) fail(5, 0, `#print-prompts has ${pp.n} articles, expected 7`);
      if (!pp.t.includes(HANDOUT)) fail(5, 0, `#print-prompts lacks "${HANDOUT}"`);
    }
  }

  if (want(6) && prompts) {
    try {
      const p = await openPage();
      await go(p, 14);
      await p.click('.slide.active [data-prompt]', { timeout: 3000 });
      await sleep(250);
      const d = await p.evaluate(() => {
        const m = document.querySelector('#modal');
        return {
          open: !!m && (m.open === true || m.classList.contains('open') || getComputedStyle(m).display !== 'none'),
          title: (document.querySelector('#modal-title') || {}).textContent,
          body: (document.querySelector('#modal-body') || {}).textContent || '',
        };
      });
      if (!d.open) fail(6, 14, '#modal not open after clicking prompt button');
      if ((d.title || '').trim() !== prompts[0].title) fail(6, 14, `modal title "${d.title}" != prompts[0].title`);
      if (!d.body.includes('Untested')) fail(6, 14, 'modal body lacks "Untested"');
      await p.keyboard.press('Escape');
      await sleep(250);
      await p.click('#controls [data-action="prompts"]', { timeout: 3000 });
      await sleep(250);
      const n = await p.evaluate(() => document.querySelectorAll('#modal-body [data-prompt]').length);
      if (n !== 7) fail(6, 0, `prompt list has ${n} [data-prompt] buttons, expected 7`);
      await p.keyboard.press('Escape');
      await go(p, 9);
      await p.locator('.slide.active .quiz').nth(1).click({ timeout: 3000 });
      await sleep(250);
      const a = await p.evaluate(() => (document.querySelector('.slide.active .answer') || {}).textContent || '');
      if (!a.trim().startsWith('B.')) fail(6, 9, `answer "${a.trim()}" does not start with "B."`);
      await p.context().close();
    } catch (e) {
      fail(6, 0, 'interaction failed: ' + e.message.split('\n')[0]);
    }
  }

  if (want(7)) {
    if (!fs.existsSync(REF)) console.log('WARN 7: reference deck not found, skipped');
    else {
      const lines = (f) => fs.readFileSync(f, 'utf8').split('\n').map((l) => l.replace(/\r$/, ''));
      const a = lines(deckPath), b = lines(REF);
      for (const ln of [7, 10]) if (a[ln - 1] !== b[ln - 1]) fail(7, 0, `line ${ln} differs from reference`);
    }
  }

  if (want(8)) {
    const lastScript = await page.evaluate(() => {
      const s = document.querySelectorAll('script');
      return s.length ? s[s.length - 1].textContent : '';
    });
    for (const word of BANNED) {
      const re = new RegExp(word, 'i');
      slideInfo.forEach((s, i) => {
        if (re.test(s.full)) fail(8, i + 1, `banned word "${word}" in visible text`);
      });
      if (re.test(lastScript)) fail(8, 0, `banned word "${word}" in script`);
    }
  }

  if (want(9)) {
    const dir = path.join(root, '.review', 'session-2-shots');
    fs.mkdirSync(dir, { recursive: true });
    const p = await openPage(1920, 1080);
    for (let i = 1; i <= N; i++) {
      await go(p, i);
      await p.screenshot({ path: path.join(dir, `s${String(i).padStart(2, '0')}.png`) });
    }
    await p.context().close();
  }

  if (want(10)) {
    for (const hash of ['#slide-18', '#slide-99']) {
      const before = pageErrors.length;
      const p = await openPage(1920, 1080, hash);
      const c = await p.evaluate(() => (document.querySelector('#counter') || {}).textContent || '');
      if (c.trim() !== '18 / 18') fail(10, 0, `${hash}: counter "${c.trim()}" != "18 / 18"`);
      if (pageErrors.length > before) fail(10, 0, `${hash}: page error ${pageErrors[pageErrors.length - 1]}`);
      await p.context().close();
    }
  }

  if (want(4)) {
    consoleErrors.forEach((m) => fail(4, 0, `console error: ${m}`));
    pageErrors.forEach((m) => fail(4, 0, `page error: ${m}`));
    badRequests.forEach((m) => fail(4, 0, `network request: ${m}`));
  }
} catch (e) {
  fail(0, 0, 'script error: ' + e.message.split('\n')[0]);
} finally {
  await browser.close();
}
finish();
