#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry.

Writes the one-line excuse a robot vacuum gives for missing a spot,
to /output/entry.txt. Deterministic: the same line every run.
"""

import os
import sys

MAX_CHARS = 140

LINE = (
    "I cleaned that spot once, in March. "
    "The house went quiet for six hours. "
    "I put it back the same day."
)


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-140 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > MAX_CHARS:
        print(
            f"ERROR: entry is {len(line)} chars, over the {MAX_CHARS}-char limit",
            file=sys.stderr,
        )
        sys.exit(1)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
