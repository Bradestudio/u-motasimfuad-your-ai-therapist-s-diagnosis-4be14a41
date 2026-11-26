"""make.fun entry: Your AI Therapist's Diagnosis.

Writes the single diagnosis line to entry.txt under
MAKEFUN_OUTPUT_DIR (fallback /output). Stdlib only, no network,
no clock, no hardcoded paths. Deterministic, byte-identical output.
"""

import os

ENTRY = (
    "Diagnosis: chronic group-chat narrator \u2014 you type 'lol' "
    "at your own jokes, then wait for applause that never arrives."
)


def main():
    line = ENTRY
    if not line or line != line.strip():
        raise SystemExit("entry must be non-blank with no surrounding whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in line):
        raise SystemExit("entry must not contain control characters")
    if not 1 <= len(line) <= 200:
        raise SystemExit("entry must be 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Verify the bytes on disk round-trip exactly to the gated line.
    with open(path, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise SystemExit("entry.txt does not match the gated line")


if __name__ == "__main__":
    main()
