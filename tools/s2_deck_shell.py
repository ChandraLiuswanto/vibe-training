"""Split and reassemble decks/session-2-web-scraping-visual.html.

The deck is one file: <head>/<style>, <main id="stage"> with <section class="slide">
elements, controls, a .print-prompts block, a JSON <script id="deck-data">, and the
runtime <script>. This module lets a build script replace only the parts it owns.
"""
import html
import json
import re

DECK = 'decks/session-2-web-scraping-visual.html'
STAGE_OPEN = re.compile(r'(<main id="stage"[^>]*>)(.*?)(</main>)', re.S)
PRINT = re.compile(r'(<div class="print-prompts">)(.*?)(</div><script id="deck-data")', re.S)
DATA = re.compile(r'(<script id="deck-data" type="application/json">)(.*?)(</script>)', re.S)


def dump_json(data):
    # Same encoding as the original file: ensure_ascii=False, "</" escaped.
    return json.dumps(data, ensure_ascii=False).replace('</', '<\\/')


def split(src):
    stage = STAGE_OPEN.search(src)
    data = DATA.search(src)
    prn = PRINT.search(src)
    if not (stage and data and prn):
        raise SystemExit('deck shell not recognised')
    return {
        'sections': stage.group(2),
        'data': json.loads(data.group(2)),
        'print': prn.group(2),
    }


def join(src, sections=None, data=None, print_html=None, extra_css=None, runtime_patch=None):
    out = src
    if sections is not None:
        out = STAGE_OPEN.sub(lambda m: m.group(1) + sections + m.group(3), out, count=1)
    if print_html is not None:
        out = PRINT.sub(lambda m: m.group(1) + print_html + m.group(3), out, count=1)
    if data is not None:
        out = DATA.sub(lambda m: m.group(1) + dump_json(data) + m.group(3), out, count=1)
    if extra_css is not None:
        marker_start, marker_end = '/* === S2 REBUILD START === */', '/* === S2 REBUILD END === */'
        block = marker_start + extra_css + marker_end
        if marker_start in out:
            out = re.sub(re.escape(marker_start) + '.*?' + re.escape(marker_end), lambda m: block, out, flags=re.S)
        else:
            i = out.rfind('</style>')
            out = out[:i] + block + out[i:]
    if runtime_patch:
        for old, new in runtime_patch:
            if new in out:
                continue
            if out.count(old) != 1:
                raise SystemExit(f'runtime patch target not unique: {old[:60]}')
            out = out.replace(old, new)
    return out


def esc(t):
    return html.escape(t, quote=True)


if __name__ == '__main__':
    src = open(DECK, encoding='utf-8').read()
    parts = split(src)
    again = join(src, sections=parts['sections'], data=parts['data'], print_html=parts['print'])
    print('round-trip identical:', again == src, len(src))
