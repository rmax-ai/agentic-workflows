# Current Plan

## Iteration focus

The last iteration batch rebalanced `gather-retrieve-synthesize` by adding finance and operations grounding, so the family is no longer concentrated almost entirely in research. The next modest batch should continue broadening that family without over-expanding it, with compliance or support as the preferred next domains if suitable scenarios can stay clearly inside retrieval and synthesis boundaries.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances now cover twenty-eight total scenarios, with `gather-retrieve-synthesize` grounded across research, finance, and operations, `investigate-reconcile-verify` grounded across engineering, finance, and compliance, `monitor-detect-triage` grounded across finance, compliance, and operations, `execute-automate` grounded across finance, compliance, HR, operations, and support, and `optimize-adapt` grounded across support, operations, and compliance
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `research-synthesis-with-citation-verification` plus the current research, finance, and operations gather/synthesis instances so the next examples stay inside evidence retrieval and synthesis boundaries rather than drifting into recommendation, investigation, or collaboration.
2. Keep the next grounding batch modest: prefer one or two `gather-retrieve-synthesize` instances in underrepresented domains, with compliance or support as the leading candidates for the next iteration.
3. Update `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the required iteration log after the next grounding batch so repository memory reflects broader gather/synthesis coverage.
4. Continue validating repository YAML with the existing uv-managed helper before closing each iteration.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve coverage balance inside one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep the next iteration scoped to one modest gather/synthesis grounding batch plus required `.agent/` memory updates; do not expand the canonical pattern set unless dependency order changes.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.

## Expected outcome

The next iteration should deepen `gather-retrieve-synthesize` with one or two grounded, governance-aware compliance or support instances while preserving the repository's pattern-first structure and modest-batch discipline.
