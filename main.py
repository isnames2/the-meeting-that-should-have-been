#!/usr/bin/env python3
"""Entry for make.fun: The Meeting That Should Have Been an Email.

Writes one line, at most 200 characters: one joke about a meeting that
should have been an email. Pure standard library; output is byte-identical
on every run.
"""

import os
from pathlib import Path

LINE = (
    # 111 characters: the turn is the irony — the meeting's only output
    # is the very email it should have been in the first place.
    "I spent an hour taking notes so I could email everyone a summary "
    "of the meeting that should have been an email."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
