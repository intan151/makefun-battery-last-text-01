#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger — deterministic one-liner.

Writes a single funny final text message, in the voice of a dying
phone battery to the charger it waited for all day, to
/output/entry.txt (also honours $OUTPUT_DIR for local runs). The text
is fixed: no randomness, no network, no external input, so every run
produces byte-identical output.
"""
import os
from pathlib import Path

ENTRY = (
    "you left me at 2% all day and waltz in now like a hero. "
    "fine \u2014 charge me, but know this: every time you forget me, "
    "I delete one of your contacts. starting with mom."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")
    # Self-check gate: output must be exactly the intended entry,
    # 1-200 chars, non-whitespace. Raises if anything drifts.
    written = (out_dir / "entry.txt").read_text(encoding="utf-8")
    assert written == ENTRY, "entry.txt does not match ENTRY"
    assert 1 <= len(written) <= 200, "entry length out of gate range"
    assert written.strip(), "entry is only whitespace"


if __name__ == "__main__":
    main()
