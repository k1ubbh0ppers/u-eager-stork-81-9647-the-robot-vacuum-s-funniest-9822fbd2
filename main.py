"""The Robot Vacuum's Funniest Excuse — make.fun entry.

A robot vacuum owns up to the spot it skipped, in a single line of
at most 120 characters, and writes that line to entry.txt.
Pure Python standard library; nothing leaves the machine.
"""

import sys
from pathlib import Path

# The vacuum's excuse, exactly as it will be judged (82 characters).
EXCUSE = "That spot is not dirty, it is load-bearing dust. I left it for structural reasons."

LIMIT = 120


def validate(text: str) -> str | None:
    """Return an error message when the line breaks the gate, else None."""
    if len(text) < 1 or len(text) > LIMIT:
        return "entry must be 1-%d characters, got %d" % (LIMIT, len(text))
    if text.strip() == "":
        return "entry must not be only whitespace"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    return None


def emit(text: str) -> int:
    problem = validate(text)
    if problem is not None:
        print("error: " + problem, file=sys.stderr)
        return 1
    folder = Path(__import__("os").environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "entry.txt").write_text(text, encoding="utf-8")
    print(text)
    print("length: %d chars" % len(text))
    return 0


if __name__ == "__main__":
    sys.exit(emit(EXCUSE))
