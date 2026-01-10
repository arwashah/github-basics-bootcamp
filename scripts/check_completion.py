import argparse
import re
from pathlib import Path


def is_complete(content):
    for code in range(ord("A"), ord("L") + 1):
        task = chr(code)
        pattern = rf"^- \[x\] {task}\."
        if not re.search(pattern, content, flags=re.MULTILINE):
            return False
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--progress", default="PROGRESS.md")
    parser.add_argument("--output")
    args = parser.parse_args()

    progress_path = Path(args.progress)
    content = progress_path.read_text(encoding="utf-8")
    complete = is_complete(content)

    if args.output:
        output_path = Path(args.output)
        with output_path.open("a", encoding="utf-8") as handle:
            handle.write(f"complete={'true' if complete else 'false'}\n")
    else:
        print("complete=true" if complete else "complete=false")


if __name__ == "__main__":
    main()
