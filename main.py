#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — one-line excuse writer.

The vacuum explains, in its own deadpan voice, why one crumb survived
the cleaning run. Writes the single line (94 characters, one line, no
trailing newline) to /output/entry.txt, or to $MAKEFUN_OUTPUT_DIR when
the harness sets it.
"""

import os

MAX_CHARS = 140

EXCUSE_PARTS = (
    "My dustbin hit capacity on that exact crumb, ",
    "so I promoted it to roommate. Rent is due Friday.",
)


def build_line(parts):
    """Join the excuse parts into one clean line under the limit."""
    line = " ".join(" ".join(parts).split())
    if not line:
        raise ValueError("excuse is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"excuse is {len(line)} chars, over the {MAX_CHARS} limit")
    return line


def main():
    line = build_line(EXCUSE_PARTS)
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
