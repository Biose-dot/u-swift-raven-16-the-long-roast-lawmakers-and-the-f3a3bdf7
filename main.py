#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert - make.fun entry.

Writes one line of text (no trailing newline) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic, stdlib only, no network.
"""
import os

ENTRY = "The committee that regulates AI, crypto, and the entire internet spent three hours debating a bill titled 'The Future of Technology,' then adjourned because nobody in the room could convert the final draft to PDF, so the law now exists only as a screenshot in a group chat."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
