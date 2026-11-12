"""Replace a deck's notes-data JSON with notes from its copy document.

Usage: python inject_notes.py COPY.md DECK.html
"""
import argparse
import json
import re
from pathlib import Path

from check_deck import parse_copy


def inject_notes(copy_md: str, html: str) -> str:
    notes = {n: entry["notes"] for n, entry in parse_copy(copy_md).items()}
    payload = json.dumps(notes, ensure_ascii=False).replace("</", "<\\/")
    pattern = r'(<script\b[^>]*\bid=[\"\']notes-data[\"\'][^>]*>).*?(</script\s*>)'
    result, count = re.subn(
        pattern, lambda m: m.group(1) + payload + m.group(2), html,
        flags=re.S | re.I,
    )
    if count != 1:
        raise ValueError(f"Expected one notes-data script, found {count}")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("copy_md")
    parser.add_argument("deck_html")
    args = parser.parse_args()
    deck = Path(args.deck_html)
    result = inject_notes(
        Path(args.copy_md).read_text(encoding="utf-8"),
        deck.read_text(encoding="utf-8"),
    )
    deck.write_text(result, encoding="utf-8")


if __name__ == "__main__":
    main()
