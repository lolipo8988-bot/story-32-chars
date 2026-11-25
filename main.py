"""One Wi-Fi network name that tells a whole story in 32 characters.

The program writes exactly one 32-character line to entry.txt and
nothing else. The name is the whole joke: a breakup told in two beats.
"She left" sets up the character and the event; "took WiFi password
too" is the punchline -- the password was the last petty thing she
took on her way out, and the narrator is left offline as well as
alone. No title, no preamble, and no explanation of the joke is
included in the output file.
"""

import os

NAME = "She left, took WiFi password too"  # exactly 32 characters


def write_entry() -> str:
    """Write the network name to the output directory and return its path."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(NAME)
    # Self-check the gate: 1 to 32 characters, no trailing newline added.
    with open(target, encoding="utf-8") as handle:
        written = handle.read()
    assert written == NAME and 1 <= len(written) <= 32, repr(written)
    return target


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
