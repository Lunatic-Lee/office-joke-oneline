#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint - make.fun entry.

Writes the entry line to /output/entry.txt (UTF-8).

Be more visible at work. So now I reply-all to everything. HR has noticed.
"""
import os

ENTRY = "My boss said I need to be more visible at work, so now I reply-all to everything. I'm very visible now. HR has noticed."


def main():
    # Competition gate: entry must be 1-200 characters.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
