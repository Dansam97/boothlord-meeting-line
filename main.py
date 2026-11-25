import os

TEXT = "This meeting could have been an email, and the email could have been a shrug."

MAX_CHARS = 200


def render():
    """Return the entry text, validated against the kit gate (1-200 chars)."""
    line = TEXT.strip()
    assert 1 <= len(line) <= MAX_CHARS, "entry out of gate: %d chars" % len(line)
    assert "\n" not in line, "entry must be a single line"
    assert line.strip(), "entry must not be whitespace-only"
    line.encode("utf-8")  # must be valid UTF-8
    return line


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(render() + "\n")

if __name__ == "__main__":
    main()
