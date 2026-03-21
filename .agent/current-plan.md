# Current Plan

## Iteration focus

This iteration should deepen `monitor-detect-triage` with a small, pattern-faithful grounding batch rather than expanding another family. The chosen batch is two alert-triage instances: one compliance scenario and one operations scenario that both stay inside triage and routing boundaries while materially differing from the existing finance suspicious-wire example.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances now cover twenty-two total scenarios, with `execute-automate` grounded across finance, compliance, HR, operations, and support, and `optimize-adapt` grounded across support, operations, and compliance
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Author one compliance `monitor-detect-triage` instance that emphasizes governed alert prioritization, evidence packaging, and reviewer-controlled escalation without drifting into recommendation or regulator-response drafting.
2. Author one operations `monitor-detect-triage` instance that emphasizes continuous signal watching, noisy-alert suppression, and incident-routing context without drifting into deeper investigation or execution.
3. Update `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the required iteration log after the grounding batch so repository memory reflects stronger monitoring coverage.
4. Continue validating repository YAML with the existing uv-managed helper before closing each iteration.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve coverage balance inside one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep the iteration scoped to one modest monitoring-grounding batch plus required `.agent/` memory updates; do not expand the canonical pattern set unless dependency order changes.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.

## Expected outcome

The iteration should deepen `monitor-detect-triage` in both compliance and operations with two grounded, governance-aware instances while preserving the repository's pattern-first structure and modest-batch discipline.
