# Current Plan

## Iteration focus

Iteration `20260321-030546` is complete: it added a single HR-domain grounding batch for `recommend-decide-escalate` via `international-relocation-and-sign-on-package-recommendation`. The next modest batch should rebalance another thin family/domain slice without widening back into schema, vocabulary, or pattern-authoring work. Operations collaboration coverage is now a strong adjacent target because operations has broad grounding in nearby families but still lacks an explicit `human-agent-collaborative-work` example.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage spans all nine top-level pattern families
- Phase 6: grounded instances now cover forty scenarios, with `investigate-reconcile-verify` grounded across engineering, finance, compliance, operations, and support, `monitor-detect-triage` grounded across engineering, finance, compliance, operations, and support, `recommend-decide-escalate` grounded across finance, compliance, operations, support, and HR, `execute-automate` grounded across finance, compliance, HR, operations, and support, `optimize-adapt` grounded across support, operations, and compliance, and `human-agent-collaborative-work` grounded across engineering, research, compliance, and support
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `analyst-copilot-loop`, the current collaboration-oriented instances, and the existing operations-domain artifacts so the next grounding batch stays inside the mixed-initiative collaboration family boundary.
2. Author exactly one operations-domain instance linked to `analyst-copilot-loop`, framed as shared human-agent artifact production or review with explicit ownership boundaries rather than recommendation, investigation, execution, scheduling, monitoring, or optimization.
3. Prefer a scenario where operations staff and an agent iteratively build or refine a governed artifact such as an exception packet, supplier response, network-readiness memo, or remediation brief before a human makes the binding conclusion.
4. Keep the next batch limited to this single collaboration example so coverage improves without widening scope.
5. Update `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the next dated iteration log after that grounding batch so execution memory stays current.
6. Validate repository YAML with the existing uv-managed helper before closing the next iteration.

## Iteration checkpoint

- Timestamp: `20260321-030546`
- Completed subagent scope: authored `instances/hr/international-relocation-and-sign-on-package-recommendation.md` as one HR-domain `deal-desk-recommendation-support` grounding change and committed it separately.
- Pending orchestrator follow-up for the next iteration: scope the operations collaboration batch before new substantive edits.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing new seed patterns.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.
- Do not widen the next iteration into pattern, vocabulary, or schema changes unless a dependency issue makes that unavoidable.

## Expected outcome

The next iteration should add one operations-domain collaboration example, deepen `human-agent-collaborative-work`, and leave the repository ready for another small grounding batch after the `.agent/` memory refresh.
