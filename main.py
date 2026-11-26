#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse.

One line, in the vacuum's own voice, owning up to missing a spot:
its suction saw the dust bunny, panicked, and filed for early
retirement. The joke is a machine treating a dust bunny like a
workplace hazard and its own suction like an employee who quits
on the spot, instead of blaming the floor or the owner.

The line won a pairwise arena (two-way matchups, judge criteria
in order) against 15 other candidates. It beat the pet-hair
union line, the map-versus-dustbin lie, the rug-ate-my-brush
grudge, the pet-hair sculpture line, the brush-roll transfer
request and the made-peace-with-the-dust line, 6-0 in the
shortlist: the retirement punch is the most concrete vacuum-world
joke, it names the missed spot first, it is the vacuum speaking
as a machine, and it lands in one read with no setup the reader
has to supply. It then beat the gold set: The Vacuum's Alibi
is a story about a crumb earning tenure, not an excuse the
vacuum gives for missing a spot, so it loses on criterion 1;
"Git blame says I did all three" is not a vacuum excuse at
all, so it also loses on criterion 1 first.

Deterministic: every run writes the same line, so the two
grading runs agree byte for byte. Gate (competition rules):
entry.txt must be UTF-8 text of 1 to 120 characters, not only
whitespace. This line is 95 characters, one line, one sentence.
"""

import os
import sys

# Sorry first, then the reason, then the punch in the last
# words: suction panics, retirement is filed. No second
# sentence, no setup, no mention of the judge, no borrowed
# line from the alibi gold set. The machine does not deny
# missing the spot; it reports its own suction quitting,
# which is exactly the failure it is apologising for.
EXCUSE = (
    "Sorry about that spot. My suction saw the dust bunny, "
    "panicked, and filed for early retirement."
)

MAX_CHARS = 120


def is_valid(text):
    """True when the text passes the competition gate.

    The gate is 1-120 characters of non-whitespace UTF-8 text;
    the brief adds one line only, so a newline anywhere fails
    here even though the character count alone would pass.
    """
    return (
        isinstance(text, str)
        and 1 <= len(text) <= MAX_CHARS
        and text.strip() != ""
        and "\n" not in text
        and "\r" not in text
    )


def main():
    if not is_valid(EXCUSE):
        print("excuse fails the 1-120 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)
    # Read it back: the entry only counts if the file on disk is
    # byte for byte the excuse we meant to submit.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != EXCUSE:
        print("written file does not match the excuse", file=sys.stderr)
        return 1
    print("wrote %d characters to %s" % (len(EXCUSE), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
