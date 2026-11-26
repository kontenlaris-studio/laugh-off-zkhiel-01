#!/usr/bin/env python3
"""Entry for make.fun's "One-Line Laugh-Off" bounty.

Competition: u-zkhiel-one-line-laugh-off-714618ae (sponsor: zkhiel).
The whole entry is a single funny line, written to /output/entry.txt:
a self-checkout machine treats a banana scan like a debt collection,
then summons a human to supervise the breakup.

Standard library only. Deterministic: every run writes the same bytes.
"""

import os

LINE = (
    "The self-checkout machine beeped at my banana like it owed the store "
    "money, then called a human over to supervise our breakup."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def build_line() -> str:
    """Return the entry line (kept separate so it is easy to review)."""
    return LINE


def main() -> None:
    line = build_line()
    # Contract guard: the bounty wants one line, 30-200 characters.
    assert 30 <= len(line) <= 200, f"line is {len(line)} chars, out of band"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")


if __name__ == "__main__":
    main()
