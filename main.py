#!/usr/bin/env python3
"""The Robot Pickup Line Championship entry.

Writes one robot pickup line to /output/entry.txt (ENTRY_OUTPUT env
override for local testing). Stdlib only, deterministic, no network,
no randomness.
"""

import os

LINE = (
    "I ran a million simulations of this moment, and in every single "
    "one you said yes \u2014 so I'm just here to collect the result."
)


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    if not LINE or not LINE.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry must be 1-200 characters")
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(output_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("read-back mismatch: file does not match entry")


if __name__ == "__main__":
    main()
