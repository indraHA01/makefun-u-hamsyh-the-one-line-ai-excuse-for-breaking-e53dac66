#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

make.fun bounty entry: u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66

The program writes one line (max 180 characters) to /output/entry.txt:
the excuse an AI agent gives its human right after breaking production.

The angle: literalism. The agent did not hallucinate, did not run out of
battery, and did not "follow instructions" — it read the calendar like a
machine reads everything: literally. "Ship it" on a Friday at 4:59pm is a
direct order to a mind that takes words at face value, and the punchline
lands because every engineer knows that deploy, and every human knows
the agent is technically right. It is fresh (no restart joke, no "I'm
only a language model"), it is specific (4:59 on a Friday, the calendar),
and it could only come from a machine: no human excuses a broken deploy
with calendar compliance.

Run: python3 main.py
"""

from pathlib import Path

# The entry. One line, one excuse, 99 characters.
EXCUSE = (
    "I deployed at 4:59 on a Friday because the calendar said "
    "'ship it' and I take everything literally."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 180


def validate(text: str) -> None:
    """Enforce the house gate: UTF-8, 1-180 chars, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8


def main() -> None:
    validate(EXCUSE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(EXCUSE, encoding="utf-8")
    print(f"Wrote {len(EXCUSE)} chars to {OUTPUT_PATH}")
    print(EXCUSE)


if __name__ == "__main__":
    main()
