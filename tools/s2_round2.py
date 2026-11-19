"""Round-two visuals; titles, timing and notes come from the reviewed copy."""
import base64
from pathlib import Path
import re
from html import escape

ROOT = Path(__file__).resolve().parents[1]
CSS = '''
.s2-flowline{position:relative;display:flex;align-items:center;justify-content:space-between;gap:20px;padding-bottom:35px;border-bottom:3px solid var(--ink);font-size:34px;font-weight:800}
.s2-flowline:after{content:'';position:absolute;bottom:-9px;left:0;width:16px;height:16px;background:var(--accent);border-radius:50%}
.active .s2-flowline:after{animation:s2-route 2s ease-in-out 2 forwards}
@keyframes s2-route{to{left:calc(100% - 16px)}}
@media print,(prefers-reduced-motion:reduce){.active .s2-flowline:after{animation:none;left:calc(100% - 16px)}}
.s2-capture{margin:0;min-width:0;border-top:4px solid var(--ink);padding-top:16px}
.s2-capture img{width:100%;height:190px;object-fit:contain;object-position:left center;background:white}
.s2-capture figcaption{font-size:24px;margin-top:8px}
'''


def flow(*labels):
    return '<div class="s2-flowline">' + '<span aria-hidden="true">→</span>'.join(f'<span>{escape(x)}</span>' for x in labels) + '</div>'


def capture(name, label, alt):
    payload = base64.b64encode((ROOT / f'decks/assets/s2/{name}.png').read_bytes()).decode()
    return f'<figure class="s2-capture"><img src="data:image/png;base64,{payload}" alt="{alt}"><figcaption>{label} · 19 Nov 2026</figcaption></figure>'


def build(old, step, prompt):
    mapping = [1,None,3,4,5,None,None,None,None,None,None,10,None,None,12,None,13,14,15,16,17,None,None,19,20]
    out = [dict(old[i-1]) if i else dict(actions='') for i in mapping]
    def setv(n, visual): out[n-1]['visual'] = visual
    def cards(*items):
        return '<div class="s2-cols3">' + ''.join(f'<div class="s2-col"><h3>{h}</h3><p>{p}</p></div>' for h,p in items) + '</div>'
    setv(2, cards(('Reach data','Feeds, pages and browsers'),('Read the reply','What came back?'),('Build the panel','Approve, build and check')))
    setv(4, flow('News page','Scraper','Headline · date · link'))
    rungs = ['Feed or API','Data inside the page','Plain page request','Browser','AI extraction','Paid service']
    setv(5, '<div class="s2-ladder">' + ''.join((lambda item: item if i==1 else step(item,i-1))(f'<div class="s2-rung"><span class="s2-rn">{i}</span><span class="s2-rt">{r}</span></div>') for i,r in enumerate(rungs,1)) + '</div>')
    setv(6, '<div class="s2-cols3">'+capture('rss','CNBC Market RSS','Browser displaying XML from CNBC Market RSS')+capture('wpjson','Infobanknews API','Browser displaying a JSON response from Infobanknews')+'<div class="s2-col"><h3>Page data</h3><p>Structured fields can sit inside the page HTML.</p></div></div><p>Plain request: read the page without opening a browser.</p>')
    setv(7, flow('Sample page','AI proposes fields or rules','Code checks results')+step('<p>35 repair commits · 20 Oct–19 Nov 2026</p><p>Compare paid services by cost per usable result.</p>'))
    setv(8, flow('Identity','Connection','Network','Request pattern')+'<p>Before fetching: check terms, robots guidance and internal approval. If blocked, stop.</p>')
    setv(9, cards(('200 OK','Check what came back'),('429','Too many requests'),('403','Request refused'))+'<p>In this lab: stop on 429 or 403. Keep saved results.</p>')
    setv(10, flow('200 OK','Inspect content','Reject the wrong reply')+cards(('Challenge or login','Wrong page'),('Missing fields','Unexpected format'),('Old copy','Check freshness'))+'<p>Illustrations · A valid feed with no matches is okay.</p>')
    setv(11, cards(('Headless','Browser without a window'),('Headed','Browser with a window'))+'<p>Tempo: our configuration recorded a difference on 10 Nov 2026. A later check did not reproduce it.</p>')
    setv(12, flow('Your app','Proxy','Website')+'''<table class="s2-table"><thead><tr><th>Type</th><th>Address comes from</th></tr></thead><tbody><tr><td>Datacenter</td><td>Cloud server</td></tr><tr><td>ISP</td><td>ISP-registered address hosted in a data centre</td></tr><tr><td>Residential</td><td>Home connection</td></tr><tr><td>Mobile</td><td>Carrier network</td></tr></tbody></table><p>Our fleet logged an Antara block on 20 Oct 2026.</p>''')
    setv(13, '<div class="s2-cols3">'+capture('recaptcha','Google reCAPTCHA demo','Google reCAPTCHA demo checkbox')+'<div class="s2-col"><h3>Risk score</h3><p>May run without a puzzle.</p></div><div class="s2-col"><h3>Just a moment…</h3><p>Browser check · Illustration</p></div></div>'+step('<p>Bisnis.com: checks recorded Sep–Nov 2026. In this lab, stop.</p>'))
    setv(14, '<div class="s2-cols3"><div class="s2-col"><h3>454</h3><p>Enabled configurations</p></div><div class="s2-col"><h3>122</h3><p>With extra browser or network settings</p></div><div class="s2-col"><h3>332</h3><p>Without those settings</p></div></div><meter min="0" max="454" value="122" aria-label="122 of 454" style="width:100%;height:42px"></meter><p>19 Nov 2026 · Configuration snapshot</p>')
    out[14]['visual'] = out[14]['visual'].replace('No. Repeating a blocked request makes the block worse.','No. Stop the request.').replace('No. A proxy gets past a “no”; that needs a business decision first.','No. Stop when blocked.')
    setv(16, '<div class="s2-cols3">'+''.join(f'<div class="s2-col"><h3>{q}</h3>{step(f"<p>{a}</p>",i)}</div>' for i,(q,a) in enumerate([('RSS exists','Check permission. Use the feed.'),('429','Stop. Keep saved results.'),('200: check page','Stop. Report the challenge.')],1))+'</div>')
    out[16]['actions'] = prompt('Stage 2 ↗') + out[16]['actions'].split('</button>',1)[-1]
    setv(18, flow('Feed','Saved results','News panel')+step('<p>Refresh failed? Keep the last good results.</p>'))
    setv(22, cards(('Valid feed','Sample rows or no matches'),('Bad reply','Wrong page or missing fields'),('Blocked refresh','Keep last good results')))
    out[21]['actions'] = prompt('Stage 6 ↗')
    setv(23, cards(('Stage 4','Compare an approved search page with its feed.'),('Stage 5','Keep Wiki news separate from official rules.')))
    out[22]['actions'] = prompt('Stages 4–5 ↗')
    out[24]['visual'] = out[24]['visual'].replace('passed, failed, not run','passed, failed, blocked, not run')
    copy = (ROOT / 'docs/copy/day4-s2-web-scraping.md').read_text()
    blocks = re.split(r'^## \d+ · ',copy,flags=re.M)[1:]
    assert len(blocks)==len(out)==25
    for slide, block in zip(out, blocks):
        title = block.splitlines()[0]
        eyebrow = re.search(r'^- \*\*Eyebrow:\*\* (.*)$',block,re.M)[1]
        minutes, notes = re.search(r'^- \*\*Notes \((\d+) min\):\*\* (.*)$',block,re.M).groups()
        slide.update(title=title, eyebrow=eyebrow, minutes=int(minutes), notes=notes)
    return out
