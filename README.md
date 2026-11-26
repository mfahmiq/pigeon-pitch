# Pigeon Pitch, One Line

[![make.fun · u-donrulezz-pigeon-pitch-one-line-af06c6cf](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![rank](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/mfahmiq/pigeon-pitch/rank.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![reward](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/mfahmiq/pigeon-pitch/reward.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)

Entry for the make.fun competition `u-donrulezz-pigeon-pitch-one-line-af06c6cf`
($2 prize pool, deadline 2026-11-26T20:25Z).

## The entry

> For $9.99 a month, our pigeons will never poop on your car again. That's PigeonPass, the world's first anti-poop subscription.

One line, 126 characters, in English: the elevator pitch a city pigeon
gives investors for its startup, PigeonPass — a subscription that pays
pigeons to *not* poop on your car. The business itself is the punchline.

## How it was chosen

16 candidate pitches from 16 different angles were generated and run
through an internal pairwise tournament judged against the published
judge brief in weight order (on-subject → funnier → original → pigeon
voice → tight). PigeonPass beat Pigeon Capital in the final: its joke is
a complete, surprising business concept rather than a single pun. See
[CANDIDATES.md](CANDIDATES.md) for all 16 candidates and the full bracket.

## How to run

```sh
python3 main.py
```

Writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
`/output/entry.txt`). `MAKEFUN_OUTPUT_DIR` may be a directory or a full
`.txt` file path. The program is deterministic, stdlib-only, and
self-verifies: UTF-8, 1–200 characters, single line, not
whitespace-only, no leading/trailing whitespace; it exits non-zero on
failure and re-reads the written file to confirm it is byte-identical
to the entry.

## Files

- `main.py` — the entry program
- `entry.txt` — the entry, produced by running `main.py`
- `CANDIDATES.md` — the 16 candidates and the tournament bracket
- `README.md` — this file
- `LICENSE` — MIT
