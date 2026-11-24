#!/usr/bin/env python3
"""One Line of Earned Pride.

Writes one original line of earned pride to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt).

Gate: UTF-8 text, 1 to 240 characters, not only whitespace.
Deterministic, Python 3.13 stdlib only: no network, no wall clock, no
randomness. Writes only entry.txt, directly, so the output folder holds
nothing but the entry.
"""

import os

# Revised line: the draft paused on a comma before "letter by letter" and
# called him "boy" at the end. Dropping the comma lets the sounding-out run
# in one breath, and "son" echoes the opening ("his son was born"), so the
# line closes as one unit and the pride lands on the last word, "aloud".
LINE = "The night his son was born, the fisherman who had never learned to read sounded out the birth certificate letter by letter and read his son's name aloud."


def main() -> None:
    line = LINE
    if not line.strip():
        raise SystemExit("line is only whitespace")
    if not (1 <= len(line) <= 240):
        raise SystemExit(f"line is {len(line)} characters, gate needs 1-240")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)


if __name__ == "__main__":
    main()
