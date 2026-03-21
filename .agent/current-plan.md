# Current Plan

## Iteration focus

Iteration `20260321-051941` is in progress: target a bounded Phase 7 refinement by adding `normalization-and-enrichment` as a second `transform-process` pattern so low-risk coverage expands outside `plan-coordinate-schedule` without introducing a vocabulary or schema change.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical coverage now spans twelve patterns across all nine top-level pattern families, with `recommend-decide-escalate` now holding a second canonical anchor and `transform-process` remaining a strong candidate for a second low-risk canonical entry
- Phase 6: grounded instances still cover all nine families across all seven currently modeled domains
- Phase 7: coverage refinement remains active, with the highest-leverage gaps now centered on sparse `low` risk cells outside `plan-coordinate-schedule`; the cleanest current target is `transform-process`
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Use `transform-process` as the next bounded refinement target because its family doc already names `normalization-and-enrichment` as a valid second anchor and the current risk matrix shows no low-risk coverage in that family.
2. Keep the new canonical pattern tightly bounded at representation cleanup, normalization, and safe enrichment for downstream reuse, stopping before verification, recommendation, or execution.
3. Update the derived browse views in the same content batch so family, domain, autonomy, architecture, and risk navigation stay aligned with the new canonical pattern.
4. Keep terminology aligned with the existing vocabularies, and avoid schema or vocabulary edits unless a dependency issue is discovered.
5. After the content commit, refresh `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the dated iteration log so execution memory matches repository reality.
6. Validate repository YAML with the existing uv-managed helper before closing the iteration.

## Iteration checkpoint

- Timestamp: `20260321-051941`
- In-progress scope: author `data/patterns/transform-process/normalization-and-enrichment.yaml` plus the required derived view updates in one focused content commit.
- Pending orchestrator follow-up: validate repository YAML and refresh execution memory so pattern inventory, coverage tracking, the repository map, and the dated iteration log reflect the new low-risk transform anchor.

## Constraints

- Keep the ontology pattern-first: choose the next canonical expansion based on coverage gaps rather than domain-first duplication.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer a modest, dependency-aware batch that improves one thin low-risk slice without forcing new instances in the same iteration.
- Keep governance, reversibility, privacy, and auditability explicit in the canonical pattern wording.
- Do not widen this iteration into vocabulary or schema changes unless a dependency issue makes that unavoidable.

## Expected outcome

This iteration should add one carefully chosen low-risk canonical pattern outside `plan-coordinate-schedule`, specifically a second `transform-process` anchor centered on normalization and enrichment, while keeping the family boundary at representation change rather than downstream judgment or action.
