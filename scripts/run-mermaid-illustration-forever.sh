#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="${REPO_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
ITERATION_SCRIPT="${REPO_ROOT}/scripts/run-mermaid-illustration-loop.sh"
SLEEP_SECONDS="${SLEEP_SECONDS:-2}"

if [ ! -x "${ITERATION_SCRIPT}" ]; then
  echo "Error: ${ITERATION_SCRIPT} is not executable."
  exit 1
fi

while true; do
  echo
  echo "========================================"
  echo "Starting new Mermaid illustration batch"
  echo "========================================"
  "${ITERATION_SCRIPT}"

  if [ -f "${REPO_ROOT}/.agent/stop.txt" ]; then
    echo "Stop file detected. Exiting."
    exit 0
  fi

  echo
  read -r -p "Run another Mermaid batch? [y/N] " answer
  case "${answer}" in
    y|Y|yes|YES)
      sleep "${SLEEP_SECONDS}"
      ;;
    *)
      echo "Stopping."
      exit 0
      ;;
  esac
done
