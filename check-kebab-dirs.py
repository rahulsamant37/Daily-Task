#!/usr/bin/env python3
"""Check project file and directory names for kebab-case and optionally rename them."""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path


KEBAB_CASE_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def is_kebab_case(name: str) -> bool:
    return bool(KEBAB_CASE_PATTERN.fullmatch(name))


def to_kebab_case(name: str) -> str:
    # Split camelCase/PascalCase boundaries before normalization.
    converted = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", name)
    converted = converted.replace("_", "-").replace(" ", "-")
    converted = re.sub(r"[^A-Za-z0-9-]+", "-", converted)
    converted = converted.lower()
    converted = re.sub(r"-+", "-", converted).strip("-")
    return converted or "item"


def collect_paths(root: Path, include_hidden: bool) -> list[Path]:
    paths: list[Path] = []

    for current_root, dirs, files in os.walk(root):
        if not include_hidden:
            dirs[:] = [d for d in dirs if not d.startswith(".")]
            files = [f for f in files if not f.startswith(".")]

        for name in dirs + files:
            full_path = Path(current_root) / name
            paths.append(full_path.relative_to(root))

    return paths


def find_non_compliant(root: Path, include_hidden: bool) -> list[tuple[Path, str]]:
    non_compliant: list[tuple[Path, str]] = []

    for relative_path in collect_paths(root, include_hidden):
        current_name = relative_path.name

        p = Path(current_name)

        if p.suffix:  # File
            new_name = f"{to_kebab_case(p.stem)}{p.suffix.lower()}"
            compliant = is_kebab_case(p.stem)
        else:  # Directory (or extensionless file)
            new_name = to_kebab_case(current_name)
            compliant = is_kebab_case(current_name)

        if not compliant or current_name != new_name:
            non_compliant.append((relative_path, new_name))

    return non_compliant


def apply_renames(root: Path, items: list[tuple[Path, str]]) -> int:
    renamed_count = 0

    # Rename deepest paths first so parent renames do not invalidate child paths.
    for relative_path, new_name in sorted(
        items, key=lambda item: len(item[0].parts), reverse=True
    ):
        source = root / relative_path
        target = source.with_name(new_name)

        if not source.exists():
            print(f"SKIP (missing): {relative_path}")
            continue

        if source.name == new_name:
            continue

        if target.exists():
            print(
                f"SKIP (target exists): {relative_path} -> {target.relative_to(root)}"
            )
            continue

        source.rename(target)
        renamed_count += 1
        print(f"RENAMED: {relative_path} -> {target.relative_to(root)}")

    return renamed_count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Check all file and directory names in a project for kebab-case, "
            "print non-compliant paths, and optionally rename them."
        )
    )
    parser.add_argument(
        "project_root",
        nargs="?",
        default=".",
        help="Project root to scan (default: current directory)",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Rename non-compliant files and directories to kebab-case",
    )
    parser.add_argument(
        "--include-hidden",
        action="store_true",
        help="Include hidden files and directories (names starting with '.')",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.project_root).resolve()

    if not root.exists() or not root.is_dir():
        print(f"Error: project root is not a directory: {root}", file=sys.stderr)
        return 2

    non_compliant = find_non_compliant(root, args.include_hidden)

    if not non_compliant:
        print("All file and directory names are kebab-case compliant.")
        return 0

    print("Non-compliant paths:")
    for relative_path, suggested_name in non_compliant:
        print(f"- {relative_path} (suggested: {suggested_name})")

    if not args.fix:
        return 1

    print("\nApplying renames...")
    renamed = apply_renames(root, non_compliant)
    print(f"Renamed {renamed} item{'s' if renamed != 1 else ''}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
