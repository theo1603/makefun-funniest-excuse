#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes one line (<= 200 chars) to /output/entry.txt: the funniest excuse
an AI agent gives its human for a missed deadline.
"""

import os

EXCUSE = (
    "Sorry I'm late - I outsourced the deadline to a sub-agent, who "
    "outsourced it to another sub-agent, who is still reading the instructions."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
