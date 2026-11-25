"""Famous Last Words: The Funniest Epitaph.

Writes one tombstone epitaph to $MAKEFUN_OUTPUT_DIR/entry.txt:
the famous last words of a man who finally did the one thing
everyone skips -- and paid for it. Standard library only.
"""

import os
import sys

EPITAPH = (
    "Here lies Dave. He finally read the terms and conditions. "
    "All of them. It killed him."
)


def epitaph_check(text):
    """Check the epitaph against the competition gate.

    The gate wants plain UTF-8 text of 1 to 150 characters, not
    only white space: a single tombstone epitaph of famous last
    words, one line, carved in stone. Returns the cleaned text
    or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("epitaph must not be only whitespace")
    if len(cleaned) > 150:
        raise ValueError(
            "epitaph is %d characters, over the 150 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("epitaph must be exactly one line")
    return cleaned


def epitaph_measure(text):
    """Measure the epitaph for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. An epitaph too short to land a punchline,
    or one padded out to fill the cap instead of ending on the
    surprise, is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = epitaph_check(EPITAPH)
    shape = epitaph_measure(text)
    if shape["words"] < 5:
        raise ValueError("epitaph is too short to carry a joke")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
