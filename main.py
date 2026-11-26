#!/usr/bin/env python3
"""The Printer Apology — make.fun entry 273.

Writes one line (max 120 characters): an apology note from an office
printer to the people who keep jamming it, feeding it cheap paper and
swearing at it. Pure standard library, fully deterministic.
"""

import os

LINE = (
    "Sorry I jammed on page 47. You fed me paper thinner than your "
    "promises, then blamed the machine for choking on it."
)


def main() -> None:
    assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars, must be 1-120"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
