# `.agent/` directory guide

This directory stores committed execution memory for the repository.
It helps future agents understand the mission, current plan,
durable decisions, ontology status, and where to look next
without re-deriving context from scratch.

## Files

- `current-plan.md` — the active iteration plan and next bounded work target.
- `mission.md` — the repository mission, curation rules, and operating constraints.
- `backlog.yaml` — dependency-ordered phases and work items for the ontology roadmap.
- `ontology-status.yaml` — current phase status, inventory counts,
  coverage summaries, and consistency notes.
- `coverage-matrix.yaml` — the structured coverage grid for
  families, domains, architectures, and risk levels.
- `decisions.md` — durable decision index with one-line summaries
  keyed by D-code; open a detail file only when the rationale
  matters.
- `repo-map.md` — concise repository map index; open a detail file
  only when the task needs more structural detail.
- `glossary.md` — repository-specific terminology for patterns,
  domains, instances, views, schema, and execution memory.
- `stop.txt` — a local stop signal used by long-running loop
  tooling; it is runtime control state, not ontology content.

## Subfolders

- `iterations/` — one Markdown file per iteration, grouped by year.
  This is the running history of completed work.
  - `iterations/README.md` — the layout and usage rules for iteration history.
- `decisions/` — one Markdown file per durable decision, keyed by D-code slug.
- `repo-map/` — a small set of clearly named repository-structure
  detail files opened on demand from `repo-map.md`.
- `prompts/` — the orchestration prompts used by the repository automation loop.
  - `mega-prompt.txt` — the master prompt that assembles the full repository context.
  - `operator-prompt.txt` — the per-iteration operator instructions.
- `proposals/` — draft ideas and process improvements that may
  become durable conventions later.

## How to use this directory

- Read the compact memory indexes first when starting a new task,
  then open decision or repo-map detail shards only when needed.
- Update the plan, status, and decisions when the repository state changes.
- Keep runtime artifacts out of versioned ontology content unless
  they are intentionally part of execution memory.
