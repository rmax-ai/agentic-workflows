# Proposal: Standardize Python Script Development With uv

- Status: implemented
- Date: 2026-03-20
- Scope: repository automation and helper-script tooling
- Decision drivers: remove ad hoc Ruby YAML parsing from agent runs, establish one scripting language for helpers, pin a modern Python runtime, and make dependency management reproducible

## Problem

The committed loop scripts are shell-based and currently do not require an application runtime beyond the Copilot CLI and standard Unix tools. However, recent run logs under `.agent/runs/` show agents reaching for one-off Ruby commands to validate or inspect YAML.

That creates three problems:

1. The repository does not declare Ruby as a supported development dependency.
2. Validation and helper logic can drift into transient shell snippets instead of reusable scripts.
3. There is no standard dependency-management path for future helper tooling.

## Proposal Summary

Adopt `uv` as the repository standard for Python-based helper scripts and target Python 3.14 for local development and CI-like validation flows.

The intent is not to rewrite the current shell entrypoints immediately. The intent is to create a clean path for all non-trivial helper logic so future agents and contributors stop inventing ad hoc Ruby or inline shell parsers.

## Goals

1. Standardize on Python for repository helper scripts.
2. Standardize on `uv` for interpreter management, environment creation, dependency locking, and command execution.
3. Pin the development target to Python 3.14.
4. Replace one-off YAML parsing commands with checked-in Python helpers.
5. Keep the current shell wrappers thin and delegate non-trivial logic to Python entrypoints.

## Non-Goals

1. Do not migrate the ontology data model or repository structure.
2. Do not rewrite every shell script into Python if shell remains the simplest orchestration layer.
3. Do not add heavy runtime dependencies unless a helper script genuinely needs them.

## Proposed End State

The repository should eventually include:

1. A `pyproject.toml` declaring Python 3.14 and the helper-script project metadata.
2. A committed `uv.lock` once dependencies exist.
3. A `.python-version` file set to `3.14` if the team wants local version-manager alignment.
4. One or more Python helper scripts under a stable location such as `scripts/python/` or a small package directory.
5. Shell entrypoints in `scripts/` that call `uv run ...` for reusable validation or maintenance tasks.
6. Prompt or contribution guidance that explicitly prefers checked-in Python helpers over inline Ruby for YAML or repository automation.

## Recommended File Layout

Preferred minimal layout:

```text
pyproject.toml
uv.lock
.python-version
scripts/
  run-agentic-workflows-loop.sh
  run-agentic-workflows-forever.sh
  python/
    validate_yaml.py
    repo_snapshot.py
```

If helper scope grows, move from loose scripts to a small package such as `python/agentic_workflows/` with console entrypoints exposed through `pyproject.toml`.

## Dependency Strategy

Use the standard library wherever practical.

Expected dependency tiers:

1. Baseline: no third-party dependencies if helpers only need filesystem work, subprocess calls, JSON, and basic text processing.
2. First likely dependency: `PyYAML` if helpers need robust YAML parsing and validation beyond what shell tools can provide.
3. Optional later dependencies: linting or task tooling only if the helper surface grows enough to justify them.

The plan should prefer a narrow dependency footprint because this repository is primarily a knowledge base, not a Python application.

## Migration Plan

### Phase A: Establish Python tooling baseline

1. Add `pyproject.toml` with a Python requirement targeting `>=3.14,<3.15`.
2. Add `.python-version` with `3.14`.
3. Document `uv` as the standard workflow in contributor guidance.
4. Add a short bootstrap section describing `uv python install 3.14` and `uv sync`.

### Phase B: Create first checked-in helpers

1. Add a Python YAML-validation helper to replace ad hoc Ruby parsing from agent runs.
2. Add a Python repository-snapshot helper if the shell snapshot logic becomes harder to maintain.
3. Keep shell scripts as thin wrappers that call `uv run python ...` or a `uv run` console script.

### Phase C: Tighten workflow guardrails

1. Update prompts or agent guidance to prefer Python helpers for reusable automation.
2. Update any validation instructions that currently rely on transient interpreter snippets.
3. Optionally add a single task or documented command for validation such as `uv run python scripts/python/validate_yaml.py`.

### Phase D: Clean up legacy habits

1. Remove any remaining documented Ruby-based validation flow.
2. Treat new inline Ruby helper commands as a process smell unless there is a strong justification.
3. Keep future repository automation in Python unless shell is clearly simpler and dependency-free.

## Design Principles

1. Shell for orchestration, Python for logic.
2. Checked-in helpers over transient one-liners.
3. Standard library first, dependencies second.
4. Reproducible developer workflow through `uv`.
5. Keep the repository lightweight and avoid turning tooling into a second project.

## Risks And Tradeoffs

### Python 3.14 availability

Python 3.14 is appropriate if the team explicitly wants to target it, but it raises compatibility risk versus 3.12 or 3.13 because some tools may lag.

Mitigation:

1. Keep dependencies minimal.
2. Prefer standard-library helpers first.
3. Validate that any chosen package supports 3.14 before adding it.

### Extra project metadata in a content repository

Adding `pyproject.toml` and `uv.lock` introduces application-style tooling into a knowledge repository.

Mitigation:

1. Keep the Python scope narrowly limited to repository automation.
2. Avoid adding packaging complexity unless helper count grows.

### Partial migration confusion

If some helpers remain shell snippets and others move to Python, contributors may be unsure what to use.

Mitigation:

1. Document the rule clearly.
2. Move any repeated non-trivial logic into Python quickly.
3. Keep shell wrappers thin and obvious.

## Acceptance Criteria

This proposal should be considered implemented when:

1. `uv` is the documented and actual path for Python helper execution.
2. The repository declares Python 3.14 explicitly.
3. YAML validation no longer depends on ad hoc Ruby commands.
4. At least one checked-in Python helper replaces transient run-log scripting.
5. The shell loop continues to work without requiring contributors to understand the helper internals.

## Recommended Next Steps

1. Accept a durable decision to standardize helper scripting on Python via `uv`.
2. Add the baseline Python project files.
3. Implement the first YAML-validation helper.
4. Update contributor and agent guidance to prefer checked-in Python helpers.
