# `.agent/` directory guide

This directory stores committed execution memory for the repository. It helps future agents understand the mission, current plan, durable decisions, ontology status, and where to look next without re-deriving context from scratch.

## Files

- `current-plan.md` — the active iteration plan and next bounded work target.
- `mission.md` — the repository mission, curation rules, and operating constraints.
- `backlog.yaml` — dependency-ordered phases and work items for the ontology roadmap.
- `ontology-status.yaml` — current phase status, inventory counts, coverage summaries, and consistency notes.
- `coverage-matrix.yaml` — the structured coverage grid for families, domains, architectures, and risk levels.
- `decisions.md` — durable design and process decisions that should not be rediscovered each run.
- `repo-map.md` — the current map of committed repository structure and what each major path means.
- `glossary.md` — repository-specific terminology for patterns, domains, instances, views, schema, and execution memory.
- `stop.txt` — a local stop signal used by long-running loop tooling; it is runtime control state, not ontology content.

## Subfolders

- `iterations/` — one Markdown file per iteration, grouped by year. This is the running history of completed work.
  - `iterations/README.md` — the layout and usage rules for iteration history.
- `prompts/` — the orchestration prompts used by the repository automation loop.
  - `mega-prompt.txt` — the master prompt that assembles the full repository context.
  - `operator-prompt.txt` — the per-iteration operator instructions.
- `proposals/` — draft ideas and process improvements that may become durable conventions later.

## How to use this directory

- Read the memory files first when starting a new task.
- Update the plan, status, and decisions when the repository state changes.
- Keep runtime artifacts out of versioned ontology content unless they are intentionally part of execution memory.
