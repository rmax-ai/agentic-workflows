# Execution Memory

## Core `.agent/` files

- `.agent/current-plan.md` — current ordered iteration plan.
- `.agent/mission.md` — stable mission and curation rules for the repository.
- `.agent/backlog.yaml` — dependency-ordered task backlog.
- `.agent/ontology-status.yaml` — status inventory and gap tracking.
- `.agent/coverage-matrix.yaml` — coverage grid for pattern, domain, architecture, and risk combinations.
- `.agent/decisions.md` — concise decision index keyed by D-code.
- `.agent/decisions/` — per-decision detail files keyed by D-code slug.
- `.agent/repo-map.md` — concise repository map index.
- `.agent/repo-map/` — on-demand repository-structure detail files.
- `.agent/glossary.md` — repository terminology guide.

## Supporting `.agent/` subdirectories

- `.agent/iterations/` — one dated Markdown file per iteration, grouped by year.
- `.agent/prompts/mega-prompt.txt` — master orchestration prompt for the repository loop.
- `.agent/prompts/operator-prompt.txt` — per-iteration operator instructions.
- `.agent/prompts/mermaid-illustration-orchestrator-prompt.txt` — specialized orchestrator prompt for adding validated Mermaid workflow diagrams to eligible pattern and instance Markdown files.
- `.agent/proposals/` — bounded improvements that may become durable conventions later.

## Runtime boundaries

- `.agent/runs/`, `.agent/tmp/`, lock files, sockets, and `.agent/stop.txt` are runtime artifacts rather than durable ontology memory.
- Read compact indexes first and open decision or repo-map detail shards only when the current task needs them.
