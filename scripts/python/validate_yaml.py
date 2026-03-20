#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

SKIP_PREFIXES = (
    (".git",),
    (".venv",),
    ("venv",),
    ("env",),
    ("ENV",),
    ("node_modules",),
    ("__pycache__",),
    ("dist",),
    ("build",),
    (".agent", "runs"),
    (".agent", "tmp"),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate YAML files in the repository.")
    parser.add_argument(
        "paths",
        nargs="*",
        default=[Path(__file__).resolve().parents[2]],
        type=Path,
        help="Files or directories to validate. Defaults to the repository root.",
    )
    return parser.parse_args()


def should_skip(path: Path, root: Path) -> bool:
    try:
        relative_parts = path.relative_to(root).parts
    except ValueError:
        relative_parts = path.parts

    return any(relative_parts[: len(prefix)] == prefix for prefix in SKIP_PREFIXES)


def iter_yaml_files(base_path: Path, root: Path) -> list[Path]:
    if not base_path.exists():
        raise FileNotFoundError(f"Path does not exist: {base_path}")

    if base_path.is_file():
        return [base_path] if base_path.suffix in {".yaml", ".yml"} else []

    files: list[Path] = []
    for candidate in base_path.rglob("*"):
        if should_skip(candidate, root):
            continue
        if candidate.is_file() and candidate.suffix in {".yaml", ".yml"}:
            files.append(candidate)
    return files


def display_path(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def validate_yaml_file(path: Path) -> None:
    with path.open("r", encoding="utf-8") as handle:
        list(yaml.safe_load_all(handle))


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parents[2]

    yaml_files: list[Path] = []
    for path_arg in args.paths:
        target = path_arg.resolve()
        yaml_files.extend(iter_yaml_files(target, root))

    yaml_files = sorted(set(yaml_files))

    if not yaml_files:
        print("No YAML files found.")
        return 0

    errors: list[tuple[str, str]] = []
    for yaml_file in yaml_files:
        try:
            validate_yaml_file(yaml_file)
        except yaml.YAMLError as error:
            errors.append((display_path(yaml_file, root), str(error).strip()))
        except OSError as error:
            errors.append((display_path(yaml_file, root), str(error)))

    if errors:
        print("YAML validation failed:", file=sys.stderr)
        for file_name, message in errors:
            print(f"- {file_name}: {message}", file=sys.stderr)
        return 1

    print(f"Validated {len(yaml_files)} YAML files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
