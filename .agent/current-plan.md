# Current Plan

## Iteration focus

This iteration should deepen the thinnest `transform-process` slice by grounding the existing canonical handoff pattern in two additional domains it already names directly: `compliance` and `operations`. The goal is to turn one thin family with only a finance grounding into a small but clearly cross-domain transform family without broadening scope into new canonical patterns.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances now cover thirteen total scenarios, with broader research and collaboration coverage, but many family/domain cells remain partial and `transform-process` still has only one fully grounded domain
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `document-to-structured-data-handoff` plus the existing finance transform instance and neighboring compliance and operations instances to keep new authoring aligned with repository structure and grounded-example style.
2. Add one new compliance transform instance and one new operations transform instance, each tied directly to `document-to-structured-data-handoff` and explicit about schema contracts, provenance, exception routing, and review boundaries.
3. Keep the batch narrowly scoped to Phase 6 grounding rather than expanding the canonical pattern set or touching unrelated families.
4. Update `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the iteration log after the batch so memory reflects the newly improved transform coverage and the next thin slice to rebalance.
5. Validate repository YAML with the existing uv-managed helper before closing the iteration.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against the existing `document-to-structured-data-handoff` canonical pattern rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer a modest grounding batch that improves one family across two real domains without forcing a broad cross-family sweep.
- Keep this iteration scoped to transform-focused instance authoring plus required `.agent/` memory updates; do not expand the canonical pattern set unless dependency order changes.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.

## Expected outcome

The next iteration should leave `transform-process` with concrete grounded examples in finance, compliance, and operations while preserving the repository's pattern-first structure.
