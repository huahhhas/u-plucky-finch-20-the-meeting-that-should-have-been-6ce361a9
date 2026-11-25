"""The Meeting That Should Have Been an Email.

Writes one funny line about a meeting that should have been an email
to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).
Gate: UTF-8 text of 1 to 200 characters, not only white space.
"""

import os

LINE = (
    "We held a meeting to decide if this could have been an email, "
    "and the meeting decided it needed a follow-up meeting."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
