#!/usr/bin/env python3
"""Plan entry for make.fun: turn $100 into the most money in 30 days.

Writes the plan text to /output/entry.txt.

Gate: the entry must be UTF-8 text of 1-280 Unicode code points, not only
whitespace. This plan is exactly 258 code points: day 1 lists a $49
landing-page service on Fiverr and Contra, then daily outreach (DM 30
Google Maps businesses with a free AI-made homepage mockup, close 2 a day),
profits reinvested into more mockups, with a likely day-30 range of
$800-$1,500 and $100 kept as float. Running this file is idempotent: it
always writes the same bytes to /output/entry.txt.
"""

from pathlib import Path

PLAN = (
    "Day 1: post a $49 'landing page in 24h' service on Fiverr and Contra. "
    "Then DM 30 Google Maps businesses with a free AI-made homepage mockup "
    "of their shop; close 2 a day. Reinvest only profits into more mockups. "
    "Likely day 30: $800-$1,500, $100 kept as float."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(PLAN, encoding="utf-8")


if __name__ == "__main__":
    main()
