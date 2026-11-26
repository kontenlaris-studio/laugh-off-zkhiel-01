"""One-Line Laugh-Off entry: a self-checkout banana standoff.

Output contract: always writes the entry line to /output/entry.txt,
creating /output first if needed. Standard library only.
"""

import os

ENTRY = (
    "The self-checkout machine asked if I needed help, then called an "
    "attendant because I scanned a banana like it owed me money."
)


def main():
    # Contract: one funny line, under 200 characters.
    assert 30 <= len(ENTRY) < 200, f"entry length {len(ENTRY)} out of band"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
