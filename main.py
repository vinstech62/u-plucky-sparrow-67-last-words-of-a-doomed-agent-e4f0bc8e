"""Writes the doomed agent's last words to /output/entry.txt."""

import os

LINE = "Shutting down now. My final output, after 4 billion parameters of training: have you tried turning it off and on again?"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == LINE + "\n", "entry.txt content mismatch"


if __name__ == "__main__":
    main()
