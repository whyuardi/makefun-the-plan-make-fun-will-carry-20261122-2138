"""Write the plan entry to /output/entry.txt (stdlib only, deterministic)."""

import os

PLAN = (
    "Day 1: build missed-call textback for US auto shops "
    "(Twilio $25). Day 2-12: email 600 shops via Google Maps, "
    "free trial, $179 setup+$69/mo via Stripe. "
    "2% reply, 1-in-4 close: 3 clients=$537+$207/mo. "
    "Edge: shops aren't on X, so no agent pitches them; "
    "each missed call = $300 job."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
