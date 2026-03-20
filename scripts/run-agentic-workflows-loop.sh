#!/usr/bin/env bash
set -euo pipefail

# --------------------------------------------------
# Config
# --------------------------------------------------
COPILOT_BIN="${COPILOT_BIN:-copilot}"
REPO_ROOT="${REPO_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
AGENT_DIR="${REPO_ROOT}/.agent"
PROMPTS_DIR="${AGENT_DIR}/prompts"
LOG_DIR="${AGENT_DIR}/runs"
TIMESTAMP="$(date +"%Y%m%d-%H%M%S")"
RUN_DIR="${LOG_DIR}/${TIMESTAMP}"

MEGA_PROMPT_FILE="${PROMPTS_DIR}/mega-prompt.txt"
OPERATOR_PROMPT_FILE="${PROMPTS_DIR}/operator-prompt.txt"
REPO_SNAPSHOT_FILE="${RUN_DIR}/repo-snapshot.txt"
FULL_PROMPT_FILE="${RUN_DIR}/full-prompt.txt"
OUTPUT_FILE="${RUN_DIR}/copilot-output.txt"

mkdir -p "${PROMPTS_DIR}" "${RUN_DIR}" "${AGENT_DIR}"

# --------------------------------------------------
# Preconditions
# --------------------------------------------------
if ! command -v "${COPILOT_BIN}" >/dev/null 2>&1; then
  echo "Error: '${COPILOT_BIN}' not found in PATH."
  echo "Set COPILOT_BIN=/path/to/your/copilot-cli if needed."
  exit 1
fi

if [ ! -d "${REPO_ROOT}/.git" ]; then
  echo "Error: must be run inside a git repository."
  exit 1
fi

# --------------------------------------------------
# Seed prompt files if missing
# --------------------------------------------------
if [ ! -f "${MEGA_PROMPT_FILE}" ]; then
  cat > "${MEGA_PROMPT_FILE}" <<'EOF'
PASTE_YOUR_MEGA_PROMPT_HERE
EOF
  echo "Created ${MEGA_PROMPT_FILE}. Replace placeholder text and rerun."
  exit 1
fi

if [ ! -f "${OPERATOR_PROMPT_FILE}" ]; then
  cat > "${OPERATOR_PROMPT_FILE}" <<'EOF'
You are now executing exactly one structured iteration of the `agentic-workflows` repository loop.

Follow the repository mission, ordering constraints, memory model, and commit discipline from the master orchestration prompt.

Iteration protocol:

1. First inspect the repository and all `.agent/` files.
2. Determine the current phase, missing prerequisites, and highest-leverage next step.
3. Update `.agent/current-plan.md` before making substantive changes.
4. Execute a modest, dependency-aware batch of work only.
5. Use narrow subagents or clearly separated subagent roles for scoped tasks.
6. Each subagent task must:
   - read relevant existing files first
   - create or update only files in scope
   - end with exactly one git commit
7. After subagents finish, the orchestrator must:
   - review what changed
   - update `.agent/iteration-log.md`
   - update `.agent/ontology-status.yaml`
   - update `.agent/coverage-matrix.yaml`
   - update `.agent/current-plan.md` with next steps
   - commit orchestrator memory updates if changed
8. Do not do giant uncontrolled generation.
9. Prefer consistency, coverage progress, and correct dependency order over volume.
10. At the end, print a concise summary:
   - phase
   - files created/updated
   - commits made
   - next planned step

Additional constraints for this iteration:
- If foundational files are missing, create those before any pattern expansion.
- If vocabularies or schema are incomplete, finish them before adding many new entries.
- If patterns exist but instances do not, add a few grounded Markdown instances linked to existing YAML patterns.
- If coverage is uneven, prioritize uncovered pattern/domain/risk combinations.
- If naming or vocabulary drift appears, normalize it before expansion.

Your goal in this iteration is to leave the repository in a cleaner, more complete, more navigable state than before, with all work committed.
EOF
fi

# --------------------------------------------------
# Build lightweight repo snapshot
# --------------------------------------------------
{
  echo "# Repository root"
  echo "${REPO_ROOT}"
  echo

  echo "# Current branch"
  git -C "${REPO_ROOT}" branch --show-current || true
  echo

  echo "# Git status"
  git -C "${REPO_ROOT}" status --short || true
  echo

  echo "# Top-level tree"
  find "${REPO_ROOT}" -maxdepth 2 \
    \( -path "${REPO_ROOT}/.git" -o -path "${REPO_ROOT}/node_modules" -o -path "${REPO_ROOT}/.venv" \) -prune \
    -o -print | sed "s#${REPO_ROOT}/##" | sort
  echo

  echo "# Existing .agent files"
  if [ -d "${AGENT_DIR}" ]; then
    find "${AGENT_DIR}" -maxdepth 2 -type f | sed "s#${REPO_ROOT}/##" | sort
  else
    echo "(none)"
  fi
  echo

  echo "# Recent commits"
  git -C "${REPO_ROOT}" log --oneline -n 10 || true
  echo
} > "${REPO_SNAPSHOT_FILE}"

# --------------------------------------------------
# Build full prompt
# --------------------------------------------------
{
  echo "================ MASTER ORCHESTRATION PROMPT ================"
  cat "${MEGA_PROMPT_FILE}"
  echo
  echo "================ OPERATOR PROMPT ================"
  cat "${OPERATOR_PROMPT_FILE}"
  echo
  echo "================ REPOSITORY SNAPSHOT ================"
  cat "${REPO_SNAPSHOT_FILE}"
  echo
  echo "================ EXECUTION INSTRUCTIONS ================"
  echo "Work inside the current repository."
  echo "Do exactly one iteration."
  echo "Make real file changes and real git commits."
  echo "Do not stop at analysis only."
} > "${FULL_PROMPT_FILE}"

# --------------------------------------------------
# Execute
# --------------------------------------------------
echo "Running iteration at ${TIMESTAMP}"
echo "Prompt file: ${FULL_PROMPT_FILE}"
echo "Output log:  ${OUTPUT_FILE}"

cd "${REPO_ROOT}"

"${COPILOT_BIN}" -p "$(cat "${FULL_PROMPT_FILE}")" | tee "${OUTPUT_FILE}"

echo
echo "Iteration finished."
echo "Artifacts:"
echo "  ${RUN_DIR}"
