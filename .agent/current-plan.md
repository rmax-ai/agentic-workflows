# Current Plan

## Iteration focus

The engineering evidence-synthesis instance is now in place, so `gather-retrieve-synthesize` is grounded across every currently modeled domain. The next modest batch should pivot to another thin family, with `recommend-decide-escalate` looking like the best adjacent target because it already has finance and compliance anchors and an operations-adjacent partial slice that can be strengthened cleanly.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances now cover thirty-two total scenarios, with `gather-retrieve-synthesize` grounded across research, engineering, finance, compliance, operations, support, and HR, `investigate-reconcile-verify` grounded across engineering, finance, and compliance, `monitor-detect-triage` grounded across finance, compliance, and operations, `execute-automate` grounded across finance, compliance, HR, operations, and support, and `optimize-adapt` grounded across support, operations, and compliance
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `deal-desk-recommendation-support` plus the current recommendation instances and decide whether an operations-domain governed recommendation example is the cleanest next coverage move.
2. If that family remains the best target, author exactly one operations instance linked to `deal-desk-recommendation-support`, framed as option ranking and escalation packaging upstream of execution.
3. Keep the next batch scoped to one small grounding move so family balancing stays more important than raw instance volume.
4. Update `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the required iteration log after the next grounding batch so repository memory reflects the new target.
5. Validate repository YAML with the existing uv-managed helper before closing the next iteration.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve coverage balance inside one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep the next iteration scoped to one small grounding batch plus required `.agent/` memory updates; do not expand the canonical pattern set unless dependency order changes.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.

## Expected outcome

The next iteration should pivot from now-complete gather/synthesis grounding to one similarly disciplined family-balancing move, most likely in `recommend-decide-escalate`.
