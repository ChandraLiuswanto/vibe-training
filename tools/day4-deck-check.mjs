// Day 4 regression checks. No practice prompt is executed.
// node tools/day4-deck-check.mjs [--only=s1|s2|s3|sheets] [--shots]
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { chromium } from './deck-check/node_modules/playwright-core/index.mjs';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const only = process.argv.find(a => a.startsWith('--only='))?.slice(7);
if (only && !['s1','s2','s3','sheets'].includes(only)) throw new Error('Invalid --only');
const shots = process.argv.includes('--shots');
const ASK = 'The prompt asks. Settings enforce.';
const DATA = 'What the agent reads goes to the AI provider. Made-up files only, never customer or bank data.';
const UNTESTED = 'Untested — rehearse before class.';
const names = ['external-data','access-control','vps-deployment'];
let failures = 0;
const fail = (check, deck, slide, reason) => { failures++; console.log(`FAIL ${check} ${deck} slide ${slide}: ${reason}`); };
const read = p => fs.readFileSync(path.join(root,p),'utf8');
const norm = s => (s || '').replace(/\s+/g,' ').trim();
const wc = s => (s || '').split(/\s+/).filter(w => /[\p{L}\p{N}]/u.test(w)).length;
// Same text-node visibility and exclusions as day4-render.mjs collect().
function collect(skipHeadings) {
  const s = document.querySelector('.slide.active');
  const skip = '.speaker-note, footer, .foot, script, style' + (skipHeadings ? ', h1, h2' : '');
  const out = [], walker = document.createTreeWalker(s, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = walker.nextNode())) {
    const p = n.parentElement;
    if (!p || p.closest(skip) || !p.checkVisibility({visibilityProperty:true})) continue;
    const v = n.nodeValue.replace(/\s+/g,' ').trim();
    if (v) out.push(v);
  }
  return out.join(' ');
}
// Extract source inner HTML, preserving bytes and matching nested divs.
function innerDiv(source, cls) {
  const start = new RegExp('<div\\b[^>]*class="'+cls+'"[^>]*>').exec(source);
  if (!start) return null;
  const begin = start.index + start[0].length;
  const tags = /<\/?div\b[^>]*>/g; tags.lastIndex = begin;
  let depth = 1, m;
  while ((m = tags.exec(source))) {
    depth += /^<\//.test(m[0]) ? -1 : 1;
    if (!depth) return source.slice(begin,m.index);
  }
  return null;
}
const browser = await chromium.launch({executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'});
try {
for (let k = 0; k < 3; k++) {
  const deck = `s${k+1}`;
  if (only && only !== deck) continue;
  const base = `session-${k+1}-${names[k]}-visual`;
  const source = read(`decks/${base}.html`), expected = k === 2 ? 16 : 18;
  const titles = [...read(`docs/outlines/${base}.md`).matchAll(/^\d+\. (.+)\r?$/gm)].map(m=>m[1].trim());
  const sections = source.match(/<section\b[^>]*class="[^"]*\bslide\b[^\"]*"[^>]*>[\s\S]*?<\/section>/g) || [];
  const page = await browser.newPage({viewport:{width:1600,height:900}});
  const errors = [], pageErrors = [];
  page.on('console',m=>{if(m.type()==='error') errors.push('console error: '+m.text());});
  page.on('pageerror',e=>{pageErrors.push(String(e)); errors.push('page error: '+e);});
  page.on('request',r=>{if(!/^(file|data|blob):/i.test(r.url())) errors.push('network request: '+r.url());});
  await page.goto(pathToFileURL(path.join(root,`decks/${base}.html`)).href);
  await page.evaluate(()=>document.fonts.ready);
  const go = async n => { await page.evaluate(n=>{location.hash='#slide-'+n;},n); await page.waitForTimeout(550); };
  const meta = await page.evaluate(()=>[...document.querySelectorAll('.slide')].map(s=>({title:s.dataset.title,heading:s.querySelector('h1,h2')?.textContent,heads:s.querySelectorAll('h1,h2').length,notes:[...s.querySelectorAll('.speaker-note')].map(e=>e.textContent.trim()),minutes:s.dataset.minutes,scope:s.textContent+' '+[...s.querySelectorAll('[aria-label]')].map(e=>e.getAttribute('aria-label')).join(' ')})));
  if(meta.length!==expected) fail(1,deck,0,`expected ${expected} slides, found ${meta.length}`);
  const counts=[];
  const outDir=path.join(root,'.review/day4-fix-shots',deck);
  if(shots){fs.rmSync(outDir,{recursive:true,force:true});fs.mkdirSync(outDir,{recursive:true});}
  for(let i=0;i<meta.length;i++) {
    const n=i+1,m=meta[i]; await go(n);
    if(m.heads!==1) fail(1,deck,n,`expected one title heading, found ${m.heads}`);
    if(m.notes.length!==1) fail(1,deck,n,`expected one speaker note, found ${m.notes.length}`);
    if(norm(m.heading)!==norm(m.title)) fail(1,deck,n,'heading differs from data-title');
    if(m.title!==titles[i]) fail(1,deck,n,`title differs from outline: expected "${titles[i]}"`);
    const body=await page.evaluate(collect,true), full=await page.evaluate(collect,false);
    const words=wc(body); counts.push(words);
    const limit=n===(k===2?15:17)?60:40;
    if(words>limit) fail(2,deck,n,`${words} visible words (max ${limit})`);
    const askSlides={s1:[10,16],s2:[14],s3:[8]};
    if(askSlides[deck].includes(n)&&!full.includes(ASK)) fail(6,deck,n,'ASK is not visible');
    if(deck==='s1'&&n===13&&!full.includes(DATA)) fail(6,deck,n,'DATA is not visible');
    for(const phrase of ['only after you approve','one-time','never edited']) if(full.toLowerCase().includes(phrase)) fail(7,deck,n,`banned visible wording: ${phrase}`);
    for(const phrase of ['test password',...(k===2?['backend','frontend']:[])]) if(new RegExp('\\b'+phrase+'\\b','i').test(m.scope)) fail(7,deck,n,`banned slide/notes/label wording: ${phrase}`);
    const small=await page.evaluate(()=>{
      const s=document.querySelector('.slide.active'),out=[];
      const stage=document.querySelector('.deck-stage, .stage, .deck')||document.body;
      const scale=new DOMMatrix(getComputedStyle(stage).transform).a||1;
      for(const el of s.querySelectorAll('*')) {
        if(el.closest('.speaker-note, footer, .foot, #controls')) continue;
        const own=[...el.childNodes].filter(c=>c.nodeType===3&&c.textContent.trim()).map(c=>c.textContent.trim()).join(' ');
        if(!own||!el.checkVisibility({visibilityProperty:true,opacityProperty:true})) continue;
        const r=el.getBoundingClientRect(),cs=getComputedStyle(el);
        if(!r.width||!r.height) continue;
        const size=parseFloat(cs.fontSize);let px=size*scale;
        if(el.closest('svg')&&el.getBBox){const b=el.getBBox();if(b.height)px=size*r.height/b.height;}
        if(px<16-0.01)out.push({px:Math.round(px*10)/10,text:own});
      } return out;
    });
    small.forEach(r=>fail(9,deck,n,`${r.px}px "${norm(r.text)}" (min 16px)`));
    if(shots) await page.screenshot({path:path.join(outDir,`s${String(n).padStart(2,'0')}.png`)});
  }
  // Bounds are on-screen stage coordinates (including SVG descendants).
  for(const [width,height] of [[1600,900],[1280,720]]) {
    await page.setViewportSize({width,height});
    for(let n=1;n<=meta.length;n++) {
      await go(n);
      const outside=await page.evaluate(()=>{
        const s=document.querySelector('.slide.active'),r=s.getBoundingClientRect(),out=[];
        for(const el of s.querySelectorAll('*')) {
          if(el.closest('.speaker-note,script,style')||!el.checkVisibility({visibilityProperty:true,opacityProperty:true}))continue;
          const b=el.getBoundingClientRect();if(!b.width||!b.height)continue;
          if(b.left<r.left-1||b.top<r.top-1||b.right>r.right+1||b.bottom>r.bottom+1)out.push(el.tagName.toLowerCase()+(typeof el.className==='string'?'.'+el.className.trim().replace(/\s+/g,'.'):''));
        }return out;
      });
      outside.forEach(s=>fail(3,deck,n,`${width}x${height}: ${s} outside stage`));
    }
  }
  await page.setViewportSize({width:1600,height:900});
  const prompts=await page.evaluate(()=>typeof prompts!=='undefined'?prompts:data.prompts);
  if(prompts.length!==7) fail(5,deck,0,`expected seven prompts, found ${prompts.length}`);
  if(k<2){const n=await page.locator('#print-prompts article').count();if(n!==7)fail(5,deck,0,`#print-prompts has ${n} articles, expected seven`);}
  for(const p of prompts) {
    await page.evaluate(id=>promptDialog(id),p.id);
    const text=await page.locator('#modal-body').innerText();
    if(!text.includes(UNTESTED)) fail(5,deck,0,`prompt ${p.id} lacks UNTESTED`);
    if(k===2) {
      const displayed=await page.evaluate(summary=>{
        if(!summary?.trim())return false;
        const body=document.querySelector('#modal-body'),pre=body.querySelector('#prompt-text');
        return [...body.querySelectorAll('*')].some(e=>!e.contains(pre)&&!pre?.contains(e)&&e.textContent.trim()===summary.trim()&&e.checkVisibility({visibilityProperty:true,opacityProperty:true})&&!!(e.compareDocumentPosition(pre)&Node.DOCUMENT_POSITION_FOLLOWING));
      },p.summary);
      if(!displayed)fail(5,deck,0,`prompt ${p.id} lacks a displayed summary above its text`);
    }
    await page.evaluate(()=>document.querySelector('#modal').close());
    if(k===0&&/reviewed package/i.test(p.text)) fail(7,deck,0,`prompt ${p.id} contains reviewed package`);
  }
  if(k===2) {
    let data;
    try {data=JSON.parse(source.match(/<script\b[^>]*id="deck-data"[^>]*>([\s\S]*?)<\/script>/)[1]);}
    catch(e){fail(8,deck,0,'deck-data does not parse: '+e.message);}
    if(data) {
      if(data.slides?.length!==16)fail(8,deck,0,'JSON must have sixteen slides');
      if(data.prompts?.length!==7)fail(8,deck,0,'JSON must have seven prompts');
      for(let i=0;i<meta.length;i++) {
        const s=data.slides?.[i],m=meta[i],n=i+1;
        if(!s){fail(8,deck,n,'JSON slide missing');continue;}
        if(s.title!==m.title)fail(8,deck,n,'JSON title differs from section');
        if(s.notes!==m.notes[0])fail(8,deck,n,'JSON notes differ from section');
        if(String(s.minutes)!==m.minutes)fail(8,deck,n,'JSON minutes differ from section');
        if(s.visual!==innerDiv(sections[i]||'','visual'))fail(8,deck,n,'JSON visual differs from section source');
        // Actions are a separate nested div; preserve their source just like visual.
        if(s.actions!==(innerDiv(sections[i]||'','actions')||''))fail(8,deck,n,'JSON actions differ from section source');
        if(s.words!==counts[i])fail(8,deck,n,`JSON words ${s.words} != rendered ${counts[i]}`);
      }
      if(data.slides.reduce((n,s)=>n+Number(s.minutes),0)!==60)fail(8,deck,0,'minutes do not total sixty');
      for(const p of data.prompts){if(!norm(p.summary))fail(8,deck,0,`prompt ${p.id} summary missing`);if(!data.pack?.includes(p.text))fail(8,deck,0,`pack lacks full prompt ${p.id}`);}
      if(!data.pack?.includes(UNTESTED))fail(8,deck,0,'pack lacks UNTESTED');
      for(const field of ['notice','ssh_host','ssh_user','ssh_host_key_fingerprint','https_url','url_base_path','loopback_port','private_release_root','private_data_dir','private_config_path','public_static_dir','user_service_name'])if(!Object.hasOwn(data.card||{},field))fail(8,deck,0,`card lacks ${field}`);
      // Include the stored slide copy in the spelling scope, not prompts/pack.
      for(const [i,s] of data.slides.entries()) {
        const text=await page.evaluate(s=>{const t=document.createElement('template');t.innerHTML=s.visual;return [s.title,s.notes,t.content.textContent,...[...t.content.querySelectorAll('[aria-label]')].map(e=>e.getAttribute('aria-label'))].join(' ');},s);
        for(const phrase of ['test password','backend','frontend'])if(new RegExp('\\b'+phrase+'\\b','i').test(text)&&!new RegExp('\\b'+phrase+'\\b','i').test(meta[i]?.scope||''))fail(7,deck,i+1,`banned JSON wording: ${phrase}`);
      }
    }
    if(/@keyframes|animation/i.test(source))fail(12,deck,0,'file contains @keyframes or animation');
    const feet=await page.locator('.slide footer, .slide .foot').allTextContents();
    if(feet.length!==16)fail(12,deck,0,`expected sixteen footers, found ${feet.length}`);
    feet.forEach((s,i)=>{if(!s.includes('Financial App · Session 3'))fail(12,deck,i+1,'footer lacks Financial App · Session 3');});
  }
  const quizSlide=[7,9,4][k];
  await go(quizSlide);
  const answer=page.locator('.slide.active .answer');
  if(norm(await answer.textContent()))fail(10,deck,quizSlide,'answer is not empty before a click');
  const hidden=page.locator('.slide.active [data-quiz-hidden]');
  let missingHooksReported=false;
  const checkHidden=async visible=>{if(k!==0)return;if(await hidden.count()!==2){if(!missingHooksReported)fail(10,deck,quizSlide,'expected two data-quiz-hidden hooks');missingHooksReported=true;return;}for(let i=0;i<2;i++){const shown=await hidden.nth(i).evaluate(e=>e.checkVisibility({visibilityProperty:true,opacityProperty:true}));if(shown!==visible)fail(10,deck,quizSlide,`quiz-hidden element ${i+1} should be ${visible?'visible':'hidden'}`);}};
  await checkHidden(false);
  const wrong=page.locator('.slide.active .quiz[data-correct="false"], .slide.active .quiz[data-answer="wrong"]').first();
  const correct=page.locator('.slide.active .quiz[data-correct="true"], .slide.active .quiz[data-answer="right"]').first();
  if(!await wrong.count()||!await correct.count())fail(10,deck,quizSlide,'wrong/correct quiz options missing');
  else {await wrong.click();await checkHidden(false);await correct.click();if(!norm(await answer.textContent()))fail(10,deck,quizSlide,'correct click produced no answer');await checkHidden(true);}
  await go(1);
  for(let n=1;n<expected;n++)await page.keyboard.press('ArrowRight');
  const counter=(await page.locator('#counter').textContent()).match(/\d+/g)?.map(Number);
  if(!counter||counter[0]!==expected||counter[1]!==expected)fail(14,deck,0,'ArrowRight navigation did not reach last counter');
  const active=await page.locator('.slide.active').evaluate(e=>[...document.querySelectorAll('.slide')].indexOf(e)+1);
  if(active!==expected)fail(14,deck,0,'last slide is not active');
  await page.locator('#notes-toggle').click();
  if(!await page.locator('#notes').isVisible()||!norm(await page.locator('#note-text').textContent()))fail(14,deck,expected,'Notes control did not show a nonempty note');
  if(pageErrors.length)fail(14,deck,0,'page error during navigation');
  [...new Set(errors)].forEach(e=>fail(4,deck,0,e));
  await page.close();
}
if(!only) {
  const a=read('decks/session-1-external-data-visual.html').split(/\r?\n/),b=read('decks/session-2-access-control-visual.html').split(/\r?\n/);
  for(const n of [7,10])if(a[n-1]!==b[n-1])fail(11,'s1',0,`shared line ${n} differs from s2`);
}
if(!only||only==='sheets')for(let n=1;n<=3;n++) {
  const file=path.join(root,`handouts/session-${n}-participant-sheet.html`),deck='sheets';
  if(!fs.existsSync(file)){fail(13,deck,n,`missing ${path.relative(root,file)}`);continue;}
  const page=await browser.newPage();
  page.on('request',r=>{if(!/^(file|data|blob):/i.test(r.url()))fail(13,deck,n,'network request: '+r.url());});
  await page.goto(pathToFileURL(file).href);await page.evaluate(()=>document.fonts.ready);
  const text=await page.locator('body').innerText();
  if(!/untested/i.test(text))fail(13,deck,n,'missing untested notice');
  if(!norm(text).includes(DATA))fail(13,deck,n,'missing DATA');
  const rows=await page.locator('[data-prompt-row]').count();if(rows!==7)fail(13,deck,n,`${rows} prompt rows (expected seven)`);
  const pdf=await page.pdf({format:'A4'});
  // Chromium PDFs expose one /Type /Page object per printed page; /Pages is excluded.
  const pages=(pdf.toString('latin1').match(/\/Type\s*\/Page\b/g)||[]).length;
  if(pages<1||pages>2)fail(13,deck,n,`${pages} A4 pages (expected one or two)`);
  await page.close();
}
} finally {await browser.close();}
console.log(failures?`FAILED: ${failures}`:'PASS');
process.exitCode=failures?1:0;
