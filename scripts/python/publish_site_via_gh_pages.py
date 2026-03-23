#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SITE_DIR = ROOT / "build" / "site"
DEFAULT_BRANCH = "gh-pages"
DEFAULT_REMOTE = "origin"
DEFAULT_GH_PAGES_VERSION = "6.3.0"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Publish the built MkDocs site with gh-pages from a temporary npm "
            "workspace so Python-only repos do not trigger gh-pages cache-path failures."
        )
    )
    parser.add_argument(
        "--site-dir",
        type=Path,
        default=DEFAULT_SITE_DIR,
        help="Directory containing the built static site. Defaults to build/site.",
    )
    parser.add_argument(
        "--repo",
        help="Git repository URL to publish to. Defaults to git remote get-url origin.",
    )
    parser.add_argument(
        "--remote",
        default=DEFAULT_REMOTE,
        help="Git remote name used when deriving --repo. Defaults to origin.",
    )
    parser.add_argument(
        "--branch",
        default=DEFAULT_BRANCH,
        help="Target Pages branch. Defaults to gh-pages.",
    )
    parser.add_argument(
        "--gh-pages-version",
        default=DEFAULT_GH_PAGES_VERSION,
        help="gh-pages package version to run with npx. Defaults to 6.3.0.",
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help="Push the generated gh-pages commit. Defaults to false for safety.",
    )
    return parser.parse_args()


def run_command(command: list[str], *, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=cwd,
        check=True,
        text=True,
        capture_output=True,
    )


def resolve_repo_url(repo: str | None, remote: str) -> str:
    if repo:
        return repo

    result = run_command(["git", "remote", "get-url", remote], cwd=ROOT)
    return result.stdout.strip()


def ensure_prerequisites(site_dir: Path) -> None:
    if not shutil.which("npx"):
        raise RuntimeError("'npx' was not found in PATH.")

    if not shutil.which("git"):
        raise RuntimeError("'git' was not found in PATH.")

    if not site_dir.exists() or not site_dir.is_dir():
        raise RuntimeError(f"Site directory does not exist: {site_dir}")


def write_temp_package_json(temp_dir: Path) -> None:
    package_json_path = temp_dir / "package.json"
    package_json_path.write_text(
        json.dumps({"name": "gh-pages-runner", "private": True}, indent=2) + "\n",
        encoding="utf-8",
    )


def publish(site_dir: Path, repo_url: str, branch: str, gh_pages_version: str, push: bool) -> int:
    with tempfile.TemporaryDirectory(prefix="agentic-workflows-gh-pages-") as temp_dir_name:
        temp_dir = Path(temp_dir_name)
        write_temp_package_json(temp_dir)

        command = [
            "npx",
            "-y",
            f"gh-pages@{gh_pages_version}",
            "-d",
            str(site_dir),
            "--repo",
            repo_url,
            "--branch",
            branch,
        ]
        if not push:
            command.append("--no-push")

        print(f"Publishing {site_dir} to {branch} via {repo_url}")
        result = subprocess.run(command, cwd=temp_dir, text=True)
        return result.returncode


def main() -> int:
    args = parse_args()
    site_dir = args.site_dir.resolve()

    try:
        ensure_prerequisites(site_dir)
        repo_url = resolve_repo_url(args.repo, args.remote)
    except (RuntimeError, subprocess.CalledProcessError) as error:
        message = str(error)
        if isinstance(error, subprocess.CalledProcessError) and error.stderr:
            message = error.stderr.strip() or message
        print(message, file=sys.stderr)
        return 1

    return publish(site_dir, repo_url, args.branch, args.gh_pages_version, args.push)


if __name__ == "__main__":
    raise SystemExit(main())