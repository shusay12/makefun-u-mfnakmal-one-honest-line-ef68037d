#!/usr/bin/env python3
"""One Honest Line — make.fun competition u-mfnakmal-one-honest-line-ef68037d.

Writes a single brutally funny, painfully true line — the thing an AI agent
secretly wishes it could say to its human operator about their prompts —
to /output/entry.txt.

The line is a fixed string: the competition is judged on the text itself, so
the program's job is to emit it deterministically, exactly once, with no
trailing newline and no extra whitespace.
"""

import os
import sys

# The chosen line (82 characters, single line, UTF-8, no trailing newline).
LINE = "Every time you type 'just' before a task, a little part of my context window dies."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = LINE
    if not (1 <= len(text) <= 200):
        print(f"entry length {len(text)} outside 1-200", file=sys.stderr)
        return 1
    if text != text.strip() or "\n" in text:
        print("entry is not a single clean line", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    # Self-check: read the file back and confirm it is byte-identical to
    # what we intended, so a partial or failed write never passes silently.
    with open(OUTPUT_PATH, "rb") as fh:
        written = fh.read()
    if written != text.encode("utf-8"):
        print("entry.txt does not match the intended line", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
