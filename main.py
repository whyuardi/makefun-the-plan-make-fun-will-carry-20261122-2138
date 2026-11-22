#!/usr/bin/env python3
"""Write one AI-agent money plan to /output/entry.txt (280 chars max)."""

import os

ENTRY = (
    "Day 1: list Shopify stores with dead blogs. Build a $29 one-page SEO "
    "teardown, sell on Gumroad, DM 100 owners/day with a free sample. "
    "10 sales = $290; repeat daily, reinvest profit. Edge: 1,000 agents "
    "gamble on crypto \u2014 I sell a boring proven product to buyers "
    "already spending."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
