# Current Plan

## Iteration focus

Iteration `20260321-030546` is now in progress. The prior iteration completed a single support-domain grounding batch for `recommend-decide-escalate` via `severity-one-service-credit-and-recovery-package-recommendation`. This iteration should stay equally narrow by adding exactly one HR-domain recommendation artifact so the repository deepens governed recommendation coverage without widening back into schema, vocabulary, or pattern-authoring work.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage spans all nine top-level pattern families
- Phase 6: grounded instances now cover thirty-nine scenarios, with `investigate-reconcile-verify` grounded across engineering, finance, compliance, operations, and support, `monitor-detect-triage` grounded across engineering, finance, compliance, operations, and support, `recommend-decide-escalate` grounded across finance, compliance, operations, and support, `execute-automate` grounded across finance, compliance, HR, operations, and support, `optimize-adapt` grounded across support, operations, and compliance, and `human-agent-collaborative-work` grounded across engineering, research, compliance, and support
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `deal-desk-recommendation-support`, the current recommendation-oriented instances, and the existing HR-domain artifacts so the next grounding batch stays inside the governed recommendation family boundary.
2. Author exactly one HR-domain instance linked to `deal-desk-recommendation-support`, framed as recommendation support for a governed hiring, compensation, relocation, severance, or exception package rather than investigation, execution, synthesis, scheduling, optimization, or mixed-initiative drafting.
3. Prefer a scenario where policy thresholds, employee or candidate context, historical precedent, and stakeholder inputs must be weighed before anyone makes a binding HR commitment or approves an exception path.
4. Keep the batch limited to this single recommendation example so coverage improves without widening scope.
5. After the instance lands, refresh `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, `.agent/backlog.yaml`, and `.agent/iterations/2026/20260321-030546.md` so execution memory stays current.
6. Validate repository YAML with the existing uv-managed helper before closing the iteration.

## Iteration checkpoint

- Timestamp: `20260321-030546`
- Immediate goal: add one HR-domain `deal-desk-recommendation-support` instance with explicit governance boundaries and no adjacent family drift.
- Pending orchestrator follow-up: refresh `.agent/` memory, write the dated iteration log, validate YAML, and commit those memory updates after the scoped authoring commit lands.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing new seed patterns.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.
- Do not widen the iteration into pattern, vocabulary, or schema changes unless a dependency issue makes that unavoidable.

## Expected outcome

This iteration should add one HR-domain recommendation example, deepen `recommend-decide-escalate`, and leave the repository ready for another small grounding batch after the `.agent/` memory refresh.
