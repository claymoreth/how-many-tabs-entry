"""Entry for "How Many Tabs Do You Have Open?" (make.fun).

Writes the answer to entry.txt inside MAKEFUN_OUTPUT_DIR
(default "output" when the variable is unset). The output path
comes only from the environment variable, never from the
process working directory, so this runs from anywhere.
"""

import os
from pathlib import Path


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    # Exactly two ASCII digits, no trailing newline or whitespace.
    target.write_text("47", encoding="utf-8")


if __name__ == "__main__":
    main()
