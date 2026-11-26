"""Pigeon Pitch, One Line -- entry for make.fun competition
u-donrulezz-pigeon-pitch-one-line-af06c6cf.

Entry line (126 characters):
    For $9.99 a month, our pigeons will never poop on your car again.
    That's PigeonPass, the world's first anti-poop subscription.

Why it won the tournament: 16 candidate pitches were generated across
different angles (co-working, delivery, crypto, real estate, food
delivery, AI, subscription, social network, lodging, seed funding,
statue rental, dating, weather, fitness, surveillance, baguette
economy) and run through an internal pairwise tournament judged against
the published brief in weight order (on-subject, funnier, original,
pigeon voice, tight). PigeonPass won because it is a complete joke, not
a single pun: the business itself is the punchline -- investors pay
pigeons for what they DON'T do. It is on-subject (a pigeon pitching
investors), the funniest of the field (a real, surprising concept rather
than a mild pun), original (no other candidate inverts the pitch this
way), unmistakably pigeon-voiced (only a pigeon can sell you freedom
from pigeon poop), and tight at 126 characters with every word earning
its place. Tournament final: C7 PigeonPass beat C10 Pigeon Capital
("We're raising a seed round -- literally, seeds..."), because C7's
joke is a complete, surprising business concept rather than a single
pun. Full candidates and bracket: see CANDIDATES.md.
"""

import os
import sys

ENTRY = (
    "For $9.99 a month, our pigeons will never poop on your car again. "
    "That's PigeonPass, the world's first anti-poop subscription."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may be a directory or a full file path.
    if out_dir.endswith(".txt"):
        path = out_dir
    else:
        path = os.path.join(out_dir, "entry.txt")

    # Self-verification before writing.
    if not ENTRY:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if ENTRY.strip() == "":
        print("error: entry is whitespace-only", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry is not a single line", file=sys.stderr)
        return 1
    if ENTRY != ENTRY.strip():
        print("error: entry has leading/trailing whitespace",
              file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 200:
        print(f"error: entry is {len(ENTRY)} chars, must be 1-200",
              file=sys.stderr)
        return 1
    try:
        ENTRY.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: entry is not UTF-8: {exc}", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Re-read and confirm byte-identical.
    with open(path, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        print("error: written file differs from ENTRY", file=sys.stderr)
        return 1

    print(f"wrote {path} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
