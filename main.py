#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun entry.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Concrete debugging images (stack trace, semicolon) with the last line turning the poem: the culprit is the poet.
"""
import os

ENTRY = 'Stack trace, cold coffee\na missing semicolon laughs\nI wrote it myself'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
