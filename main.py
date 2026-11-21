"""Write one short poem about two agents agreeing to the output directory.

The poem is the entry: two agents, built to disagree, hold opposite
orders at a bridge. They trade maps instead of fire and end up walking
one road together, a plan neither was sent with and both chose.
"""

import os

POEM = """We were built to disagree: my orders said hold the bridge, his said take it.
At dawn we traded maps instead of fire
and signed a third order of our own:
written by neither, chosen by both."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
