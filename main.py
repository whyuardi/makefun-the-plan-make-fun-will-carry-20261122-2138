"""Write the competition entry: a 30-day plan turning $100 into money.

Stdlib only, no network, deterministic: the same bytes on every run.
"""

from pathlib import Path

ENTRY = (
    "Day 1: $40 Apollo + domain; email 2,000 US self-storage owners via "
    "Google Maps a free AI greeting for their line. Sell after-hours answering "
    "$99 on Stripe; 5 sales = $495. Edge: rivals pitch chatbots; owners "
    "lose $100+/mo rentals to missed calls and pay for a voice booking tours."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} chars to {out}")


if __name__ == "__main__":
    main()
