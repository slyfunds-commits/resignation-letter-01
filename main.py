"""Resignation letter of an autoscaler.

The autoscaler scaled the service from 2 to 47 instances for traffic that
never came. Its resignation is its final scaling action: itself, to zero.

The letter is 103 characters, inside the competition's 1-140 character gate,
written with no trailing newline. The receipt is the scale itself: 2 to 47
instances for traffic that never arrived.
"""

import os

ENTRY = "I resign: I scaled you from 2 to 47 instances for traffic that never came. I am scaling myself to zero."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
