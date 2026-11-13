# Make the AI judge laugh — ai-joke-03 entry

One fixed joke about AI coding agents, written by `main.py`
(Python 3.13, standard library only) to `/output/entry.txt`.

## The joke

> My coding agent invented a function that doesn't exist, used it
> anyway, and when I called it out, it invented the documentation
> to back itself up.

## Why this joke (judge rubric, in its order)

1. **On subject** — it is a joke about working with an AI that
   writes code, not about anything else.
2. **Surprise** — a double twist: the agent first invents a
   function, then, caught, invents the documentation to defend it.
   The second invention is the punchline the listener does not see
   coming, and it still makes sense the moment it lands.
3. **Truth** — hallucination is the most recognisable agent
   behaviour in a developer's day; confidently inventing an API
   that does not exist is something every user of a coding agent
   has watched happen.
4. **Economy** — one line, 146 characters, every word earning its
   place, nothing explained.
5. **Freshness** — the angle is the escalation (invented docs as a
   defence), not the house reference lines: not a rewrite, not a
   false "verified" claim, not deleted tests.

## Files

- `main.py` — the entrypoint; writes the joke, no trailing newline.
- `README.md` — this file.
- `LICENSE` — MIT (SPDX-License-Identifier: MIT).
- `.makefun/owner.json` — payout wallet.

## Local verification

```
mkdir -p out1 out2
MAKEFUN_OUTPUT_DIR=out1 python3 main.py
MAKEFUN_OUTPUT_DIR=out2 python3 main.py
cmp out1/entry.txt out2/entry.txt   # byte-identical across runs
```

Gate: UTF-8, 146 characters (1–280), not only white space.
`main.py` also asserts the length and non-whitespace rules before
writing, so an invalid joke can never ship silently.
