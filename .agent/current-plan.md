# Current Plan

## Iteration focus

Iteration `20260321-052613` is starting: the repository has broad family and domain grounding, so this batch should strengthen one still-thin canonical family without reopening schema or vocabulary work.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical coverage now spans thirteen patterns across all nine top-level pattern families, with `gather-retrieve-synthesize`, `transform-process`, `monitor-detect-triage`, and `recommend-decide-escalate` each holding more than one canonical anchor
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains
- Phase 7: coverage refinement remains active, with `investigate-reconcile-verify`, `plan-coordinate-schedule`, `execute-automate`, `optimize-adapt`, and `human-agent-collaborative-work` still holding only one canonical pattern each
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read the thin-family docs, canonical pattern set, and derived views before selecting one dependency-safe expansion cell.
2. Use this iteration to add one second canonical pattern in a still-thin family, preferring a low-risk or otherwise sparse coverage slice that stays cleanly inside an existing family boundary.
3. Update the derived browse views that reference the chosen family so navigation remains aligned with canonical pattern inventory.
4. After the content commit, refresh `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the dated iteration log so execution memory matches repository reality.
5. Validate repository YAML with `uv run python scripts/python/validate_yaml.py` before closing the iteration.

## Constraints

- Keep the ontology pattern-first: avoid domain-first duplication and do not add instances in the same batch unless dependency pressure makes them necessary.
- Do not change schema or vocabularies unless the selected pattern cannot be represented with existing terms.
- Ensure the scoped subagent task ends with exactly one git commit.
- Keep governance, reversibility, privacy, and auditability explicit in the canonical pattern wording.
- Prefer a modest content batch that improves a thin risk or architecture cell over broad expansion.

## Expected outcome

The iteration should leave one currently thin family with a second canonical anchor, aligned browse views, refreshed execution memory, and validated YAML.
