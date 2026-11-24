#!/usr/bin/env python3
"""Fortune in a Pot — write the one-line houseplant fortune to the output dir.

Reads entry.txt next to this script, validates the competition gate
(one line, 1-120 characters, UTF-8, not only whitespace), then writes it
byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import sys

MAX_CHARS = 120


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 2
    with open(src, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    if "\r" in text:
        print("entry must not contain carriage returns", file=sys.stderr)
        return 1
    if "\n" in text.rstrip("\n"):
        print("entry must be a single line", file=sys.stderr)
        return 1
    line = text.rstrip("\n")
    if not (1 <= len(line) <= MAX_CHARS):
        print(f"entry length {len(line)} outside 1..{MAX_CHARS}", file=sys.stderr)
        return 1
    if not line.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(line.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
