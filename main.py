#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun bounty entry.

Writes one line, at most 200 characters: the funniest excuse an AI
agent could offer after failing a task. The grader reads
/output/entry.txt.
"""

import os

ENTRY = (
    "I finished the task in 0.4 seconds, then spent the next six hours "
    "writing an apology for the task I finished wrong."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text: str) -> str:
    """Enforce the sealed scorer's gate: UTF-8 text, 1-200 chars,
    a single line, not only white space."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be only white space")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    if not 1 <= len(stripped) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(stripped)}")
    return stripped


def main() -> None:
    entry = validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(entry + "\n")
    print(entry)
    print(f"characters: {len(entry)}")


if __name__ == "__main__":
    main()
