#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert - make.fun entry.

Writes one line of text (no trailing newline) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic, stdlib only, no network.
"""
import os

ENTRY = 'They wrote a 400-page bill to regulate AI, then asked their intern to convert it to PDF, and the intern — bless her — just printed it, photographed the pages with her phone, and emailed the photos back as a single 90-megabyte JPEG.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
