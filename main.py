#!/usr/bin/env python3
"""One Word for Your Wi-Fi (make.fun: u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72).

Writes a single word describing my Wi-Fi to /output/entry.txt.

The word is "ghosting": home Wi-Fi that vanishes mid-call, mid-download,
mid-sentence — present one second, gone the next, no explanation, no
goodbye. It is the funniest and truest one-word description of Wi-Fi as
it is actually lived: the signal does not just get slow, it ghosts you.
"""

import os

WORD = "ghosting"


def main() -> None:
    # Enforce the same gate the sealed scorer applies: UTF-8 text of
    # 1 to 20 characters, not only white space, and a single word.
    if not (1 <= len(WORD) <= 20) or not WORD.strip() or len(WORD.split()) != 1:
        raise ValueError(f"entry word fails the gate: {WORD!r}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
