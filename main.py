#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun entry.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Concrete debugging images (logs, a print statement, a typo) with the last line turning the poem: the bug was one letter all along.
"""
import os

ENTRY = 'Logs scroll past midnight\none print statement left to try\nit was a typo'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
