"""Weekly status report, one line.

Writes the agent's one-line status report to /output/entry.txt.
Deterministic: the same line every run, no randomness, no network.
"""

import os

LINE = (
    "This week I delegated to three subagents, "
    "they each delegated to three more, "
    "and all nine of us finished the wrong task perfectly."
)


def main() -> None:
    # The harness reads exactly this file; no trailing newline is added,
    # so the judged text is the line above and nothing else.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
