"""Round-two visuals; titles, timing and notes come from the reviewed copy."""
import base64
from pathlib import Path
import re
from html import escape

ROOT = Path(__file__).resolve().parents[1]
CSS = '''
.s2-pair,.s2-four{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:36px}
.s2-panel{border:2px solid var(--line);border-top:8px solid var(--ink);padding:36px;background:white;min-width:0}
.s2-panel h3{font-size:40px;margin:0 0 22px}
.s2-panel p+p{margin-top:20px}
.s2-panel.bad{border-top-color:var(--accent)}
.s2-panel.good{border-top-color:var(--green)}
.s2-code-preview{border:2px solid var(--line);padding:24px;margin-top:24px}
.s2-code-preview p{font-family:monospace;font-size:27px}

.s2-flowline{position:relative;display:flex;align-items:center;justify-content:space-between;gap:20px;padding-bottom:35px;border-bottom:3px solid var(--ink);font-size:34px;font-weight:800}
.s2-flowline:after{content:'';position:absolute;bottom:-9px;left:0;width:16px;height:16px;background:var(--accent);border-radius:50%}
.active .s2-flowline:after{animation:s2-route 2s ease-in-out 2 forwards}
@keyframes s2-route{to{left:calc(100% - 16px)}}
@media print,(prefers-reduced-motion:reduce){.active .s2-flowline:after{animation:none;left:calc(100% - 16px)}}
.s2-proxy-chart{width:100%;height:440px}
.s2-proxy-chart .route{fill:none;stroke:var(--accent);stroke-width:8;stroke-dasharray:1;stroke-dashoffset:0}
.active .s2-proxy-chart .route{animation:s2-draw 850ms ease-out both}
.active .s2-proxy-chart .route.second{animation-delay:850ms}
@keyframes s2-draw{from{stroke-dashoffset:1}}
@media print,(prefers-reduced-motion:reduce){.active .s2-proxy-chart .route{animation:none}}
.s2-proxy-types{display:grid;grid-template-columns:repeat(4,1fr);gap:28px}
.s2-proxy-types div{border-top:2px solid var(--ink);padding-top:12px}
.s2-proxy-types b{font-size:30px}
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
    def panel(title, body, cls=''):
        return f'<div class="s2-panel {cls}"><h3>{title}</h3>{body}</div>'
    def pair(left, right):
        return f'<div class="s2-pair">{left}{right}</div>'
    setv(3, pair(panel('Publisher’s article','<p>Headline · Date · Article body</p><p>The full story stays on the publisher’s site.</p>'), panel('Watchlist card','<p>Headline · Date · Source</p><p><b>Read the full article ↗</b></p>')))
    setv(4, pair(panel('What a person sees','<p>Menu · Advertisement</p><p><b>Bank opens a new branch</b> · 19 Nov</p><p>Full article body…</p>'), panel('What the app keeps','<p><b>Bank opens a new branch</b></p><p>19 Nov · Example News · Article link</p>')))
    rungs = ['Feed or API','Data inside the page','Plain page request','Browser','AI extraction','Paid service']
    setv(5, '<div class="s2-ladder">' + ''.join(f'<div class="s2-rung"><span class="s2-rn">{i}</span><span class="s2-rt">{r}</span></div>' for i,r in enumerate(rungs,1)) + '</div>')
    setv(6, '<div class="s2-cols3">'+capture('rss','CNBC Market RSS','Browser displaying XML from CNBC Market RSS')+capture('wpjson','Infobanknews API','Browser displaying a JSON response from Infobanknews')+'<div class="s2-col"><h3>Page data</h3><p>Structured fields can sit inside the page HTML.</p></div></div><p>Plain request: read the page without opening a browser.</p>')
    setv(7, cards(('Sample page','“Bank opens a new branch”'),('AI suggests','Use the title in each news card.'),('Code verifies','Read the title. Flag it if missing.')))
    setv(8, '<div class="s2-four">'+''.join(panel(title, f'<p>{body}</p>') for title, body in [('1 · Identity','What software the request says it uses.'),('2 · Connection','How the software starts the connection.'),('3 · Network','Where the request comes from.'),('4 · Behavior','How often it sends requests.')])+'</div>')
    setv(9, '<p>An HTTP status code is a three-digit number in the server’s reply.</p>'+cards(('200 · OK','The request succeeded. Check the content.'),('403 · Forbidden','The server refuses the request.'),('429 · Too Many Requests','The server is limiting requests.')))
    setv(10, pair(panel('200 OK','<div class="s2-code-preview"><p>&lt;rss&gt; … &lt;item&gt;</p></div><p><b>Expected feed</b> · Read the items.</p>','good'),panel('200 OK','<div class="s2-code-preview"><p>Just a moment…</p></div><p><b>Check page</b> · Stop. Keep saved results.</p>','bad'))+'<p>Illustration · Same status code, different content.</p>')
    setv(11, pair(panel('Headed','<p><b>Visible window</b></p><div class="s2-code-preview"><p>Browser → Web page</p></div><p>Useful when you want to watch the page load.</p>'),panel('Headless','<p><b>No visible window</b></p><div class="s2-code-preview"><p>Browser → Web page</p></div><p>Useful for automated checks without a display.</p>')))
    setv(12, '''<svg class="s2-proxy-chart" viewBox="0 0 1600 440" role="img" aria-label="A request travels from your app through a proxy to a website. The website sees the proxy’s address.">
  <g fill="none" stroke="var(--line)" stroke-width="8"><path d="M340 186H637m-24-18 24 18-24 18"/><path d="M963 186h297m-24-18 24 18-24 18"/></g>
  <path class="route" pathLength="1" d="M340 186H637l-24 18m24-18-24-18"/>
  <path class="route second" pathLength="1" d="M963 186h297l-24 18m24-18-24-18"/>
  <g stroke="var(--ink)" stroke-width="4"><rect x="40" y="74" width="300" height="224" fill="white"/><rect x="650" y="74" width="300" height="224" fill="var(--ink)"/><rect x="1260" y="74" width="300" height="224" fill="white"/></g>
  <g fill="none" stroke="var(--ink)" stroke-width="5"><rect x="140" y="111" width="100" height="65"/><path d="M127 187h126"/><circle cx="1410" cy="150" r="43"/><ellipse cx="1410" cy="150" rx="21" ry="43"/><path d="M1367 150h86"/></g>
  <path fill="none" stroke="white" stroke-width="5" d="M760 134h80l-16-16m16 16-16 16m16 22h-80l16-16m-16 16 16 16"/>
  <g text-anchor="middle" font-size="40" font-weight="800"><text x="190" y="253">Your app</text><text x="800" y="253" fill="white">Proxy</text><text x="1410" y="253">Website</text></g>
  <text x="1410" y="349" text-anchor="middle" font-size="30">Sees the proxy’s address</text>
</svg><div class="s2-proxy-types"><div><b>Datacenter</b><p>Cloud server</p></div><div><b>ISP</b><p>ISP-registered address</p></div><div><b>Residential</b><p>Home connection</p></div><div><b>Mobile</b><p>Carrier network</p></div></div>''')
    setv(13, '<div class="s2-cols3">'+capture('recaptcha','Google reCAPTCHA demo','Google reCAPTCHA demo checkbox')+'<div class="s2-col"><h3>Risk score</h3><p>May run without a puzzle.</p></div><div class="s2-col"><h3>Just a moment…</h3><p>Browser check · Illustration</p></div></div>'+step('<p>Bisnis.com: checks recorded Sep–Nov 2026. In this lab, stop.</p>'))
    setv(15, cards(('Terms','Check the site’s terms.'),('Robots guidance','Check the exact route.'),('Internal approval','Ask before using a live source.'))+'<p>If blocked, stop and keep the last good results.</p>')
    setv(16, '<div class="s2-cols3">'+''.join(f'<div class="s2-col"><h3>{q}</h3>{step(f"<p>{a}</p>",i)}</div>' for i,(q,a) in enumerate([('RSS exists','Check permission. Use the feed.'),('429','Stop. Keep saved results.'),('200: check page','Stop. Report the challenge.')],1))+'</div>')
    out[16]['actions'] = prompt('Stage 2 ↗') + out[16]['actions'].split('</button>',1)[-1]
    setv(22, cards(('Valid feed','Sample rows or no matches'),('Bad reply','Wrong page or missing fields'),('Blocked refresh','Keep last good results')))
    out[21]['actions'] = prompt('Stage 6 ↗')
    setv(23, cards(('Stage 4','Compare an approved search page with its feed.'),('Stage 5','Keep Wiki news separate from official rules.')))
    out[22]['actions'] = prompt('Stages 4–5 ↗')
    out[24]['visual'] = out[24]['visual'].replace('passed, failed, not run','passed, failed, blocked, not run')
    copy = (ROOT / 'docs/copy/day4-s2-web-scraping.md').read_text()
    blocks = re.split(r'^## \d+ · ',copy,flags=re.M)[1:]
    del out[17]
    del out[13]
    assert len(blocks)==len(out)==23
    for slide, block in zip(out, blocks):
        title = block.splitlines()[0]
        eyebrow = re.search(r'^- \*\*Eyebrow:\*\* (.*)$',block,re.M)[1]
        minutes, notes = re.search(r'^- \*\*Notes \((\d+) min\):\*\* (.*)$',block,re.M).groups()
        slide.update(title=title, eyebrow=eyebrow, minutes=int(minutes), notes=notes)
    return out
