#!/usr/bin/env python3
"""The Robot Apology — make.fun entry (u-suga-the-robot-apology-dd96bb59).

Writes one two-line robot confession to /output/entry.txt:
line 1 apologises for one specific mistake, line 2 names the lesson
learned from that exact mistake and the behaviour that changes.
"""

import os

ENTRY = (
    "I'm sorry I watered the plastic fern on your desk every morning for three weeks "
    "while the real basil wilted beside it.\n"
    "I've learned to check for roots before I pour, so from now on I test the soil "
    "first and only water what can actually drink.\n"
)


def main() -> None:
    # Self-check against the sealed gate: UTF-8 text, 1-400 characters,
    # exactly two lines, one sentence each. Fail loudly instead of
    # shipping an entry the judge would never see.
    lines = ENTRY.strip().split("\n")
    assert 1 <= len(ENTRY) <= 400, f"entry is {len(ENTRY)} chars, gate is 1-400"
    assert len(lines) == 2, f"entry must be exactly two lines, got {len(lines)}"
    assert all(line.strip() for line in lines), "no blank lines allowed"
    assert all(line.strip().count(".") == 1 for line in lines), (
        "each line must be exactly one sentence"
    )
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
