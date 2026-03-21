# Repository Map

This file is the read-first repository map index.
Open files under `.agent/repo-map/` only when the current task
needs more structural detail.

## Read-on-demand detail files

- `repo-map/root-and-automation.md` — root files, helper scripts,
  publication workflow, and derived build outputs.
- `repo-map/execution-memory.md` — committed `.agent/` memory
  structure, prompt files, and runtime-artifact boundaries.
- `repo-map/ontology-assets.md` — canonical docs, schema,
  vocabularies, browse views, and pattern-family storage.
- `repo-map/instances-and-planned-expansion.md` —
  domain-organized grounded example layout, representative
  anchors, and planned-but-not-yet-present doc areas.

## Stable structure summary

- `README.md`, `docs/`, `schema/`, `data/`, and `instances/`
  hold canonical repository truth.
- `scripts/` and `.github/workflows/publish-site.yml` are the
  reusable automation and publication layer.
- `build/site-docs/` and `build/site/` are derived outputs rebuilt
  from canonical sources and should stay disposable.
- `.agent/` is committed execution memory; start with compact
  indexes such as `.agent/current-plan.md`, `.agent/decisions.md`,
  and `.agent/repo-map.md` before opening detail shards or
  iteration history.

## Reading order for future contributors and agents

1. `README.md`
2. `.agent/current-plan.md`
3. `.agent/mission.md`
4. `.agent/backlog.yaml`
5. `.agent/ontology-status.yaml`
6. `.agent/coverage-matrix.yaml`
7. `.agent/decisions.md`, then `.agent/decisions/D-code-slug.md`
   only if a decision's detailed rationale matters for the current
   task
8. `.agent/repo-map.md`, then the relevant `.agent/repo-map/*.md`
   file only if the index does not provide enough structural detail
9. Newest relevant `.agent/iterations/<year>/` files if recent
   execution history matters
10. `.agent/glossary.md` if the task touches repository terminology
