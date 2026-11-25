#!/usr/bin/env python3
"""Last Text at One Percent — make.fun entry.

Writes the dying phone's final text message to /output/entry.txt.
Stdlib only, no network. Enforces the 1-200 character gate in code.
"""

import os

ENTRY_TEXT = (
    "Before I go: I deleted your 4,000 unread emails. You're welcome. "
    "I also read your search history. I take that to the grave. Bye."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY_TEXT.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry text must be 1-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry text must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip check: what the grader reads must be exactly what we wrote.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("round-trip mismatch: file content differs from entry text")
    if not (1 <= len(written) <= MAX_CHARS):
        raise SystemExit(f"written file fails gate: {len(written)} chars")
    print(f"wrote /output/entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()
