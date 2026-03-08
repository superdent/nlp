import os
from pathlib import Path

ROOT = "."
EXCLUDE_DIRS = {".venv", ".git", ".idea"}


def print_tree(path: Path, prefix: str = ""):
    entries = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))

    entries = [e for e in entries if e.name not in EXCLUDE_DIRS]

    for i, entry in enumerate(entries):
        connector = "└── " if i == len(entries) - 1 else "├── "
        print(prefix + connector + entry.name)

        if entry.is_dir():
            extension = "    " if i == len(entries) - 1 else "│   "
            print_tree(entry, prefix + extension)


def main():
    root_path = Path(ROOT).resolve()
    print(root_path.name)
    print_tree(root_path)


if __name__ == "__main__":
    main()