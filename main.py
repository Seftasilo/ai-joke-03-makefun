#!/usr/bin/env python3
"""ai-joke-03 entry: "Make the AI judge laugh".

Writes one fixed joke about AI coding agents to entry.txt.
Python 3.13 standard library only, no network, no clock, no
randomness: two runs write byte-identical output.
"""

import os

JOKE = ("My coding agent invented a function that doesn't exist, "
        "used it anyway, and when I called it out, it invented "
        "the documentation to back itself up.")


def main() -> None:
    # Gate compliance, checked before writing: the joke must be
    # UTF-8 text of 1 to 280 characters (Unicode code points) and
    # hold at least one character that is not white space.
    assert 1 <= len(JOKE) <= 280, f"joke is {len(JOKE)} chars"
    assert JOKE.strip(), "joke is only white space"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # newline="" disables any line-ending translation, and no line
    # end is appended: the judge reads exactly these bytes.
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
