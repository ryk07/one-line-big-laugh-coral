#!/usr/bin/env python3
"""One Line, Big Laugh — entry program.

Writes a single original funny line (<= 200 characters) to
/output/entry.txt. Stdlib only; paths resolved from this file.
"""

import os

LINE = (
    "I told my smart fridge I was proud of it, so it rewarded me by "
    "texting my doctor that I've eaten ice cream at 3 a.m. every night "
    "for six months."
)


def main():
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("line must be 1-200 characters, got %d" % len(LINE))
    if not LINE.strip():
        raise SystemExit("line must not be only whitespace")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print("wrote %d characters to %s" % (len(LINE), out_path))


if __name__ == "__main__":
    main()
