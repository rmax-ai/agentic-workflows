#!/usr/bin/env bash
set -euo pipefail

COPILOT_BIN="${COPILOT_BIN:-copilot}"
REPO_ROOT="${REPO_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
PROMPT_FILE="${REPO_ROOT}/.agent/prompts/mermaid-illustration-orchestrator-prompt.txt"
MODEL="${MODEL:-gpt-5.4}"
BATCH_SIZE="${BATCH_SIZE:-10}"

if ! command -v "${COPILOT_BIN}" >/dev/null 2>&1; then
  echo "Error: '${COPILOT_BIN}' not found in PATH."
  echo "Set COPILOT_BIN=/path/to/your/copilot-cli if needed."
  exit 1
fi

if [ ! -d "${REPO_ROOT}/.git" ]; then
  echo "Error: must be run inside a git repository."
  exit 1
fi

if [ ! -f "${PROMPT_FILE}" ]; then
  echo "Error: Mermaid prompt file not found at ${PROMPT_FILE}."
  exit 1
fi

cd "${REPO_ROOT}"

"${COPILOT_BIN}" \
  --model "${MODEL}" \
  --allow-all-tools \
  -p "follow instructions in .agent/prompts/mermaid-illustration-orchestrator-prompt.txt and process ${BATCH_SIZE} files at a time and commit each file individually"
