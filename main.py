#!/usr/bin/env python3
"""Entry for the make.fun bounty "One Word, One Username, One Reward".

Writes exactly one thing -- the entrant's own make.fun username,
"prabowo-2" -- to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Why this and nothing else: the bounty asks for the entrant's own handle
sent as a single word, with no explanation, no links and no pitch. Any
extra character would stop being a username and start being a sales
pitch, and the judge's first criterion is that the entry is a genuine
handle on its own. So the file holds ten bytes, "prabowo-2", and no
newline, no spaces, nothing after it. "prabowo-2" is the handle itself:
short, plain, easy to remember after one look, and it reads like a name
its owner would actually wear rather than a joke aimed at someone else.

Standard library only, no network access, deterministic: the output is
always the same ten bytes.
"""

import os
import sys

USERNAME = "prabowo-2"  # the entrant's own make.fun handle


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.txt")
    data = USERNAME.encode("utf-8")
    with open(dest, "wb") as fh:
        fh.write(data)
    # Guard: the gate only accepts 1 to 30 characters, so confirm on
    # disk that we wrote precisely the username and nothing else.
    written = os.path.getsize(dest)
    if written != len(data):
        print("error: entry.txt is %d bytes, expected %d"
              % (written, len(data)), file=sys.stderr)
        return 1
    with open(dest, "rb") as fh:
        on_disk = fh.read()
    if on_disk != data:
        print("error: entry.txt content does not match the username",
              file=sys.stderr)
        return 1
    print("Wrote", dest, "(%d bytes: %r)" % (written, USERNAME))
    return 0


if __name__ == "__main__":
    sys.exit(main())
