# Current Plan

## Iteration focus

This iteration should rebalance the still-thin engineering domain by grounding `human-agent-collaborative-work` with exactly one engineering-domain instance linked to `analyst-copilot-loop`. The instance should stay centered on mixed-initiative co-production around a shared artifact, with explicit handoffs and human-owned judgment, rather than drifting into pure synthesis, recommendation, investigation, or execution.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances now cover thirty-three total scenarios, with `gather-retrieve-synthesize` grounded across research, engineering, finance, compliance, operations, support, and HR, `investigate-reconcile-verify` grounded across engineering, finance, and compliance, `monitor-detect-triage` grounded across finance, compliance, and operations, `recommend-decide-escalate` grounded across finance, compliance, and operations, `execute-automate` grounded across finance, compliance, HR, operations, and support, and `optimize-adapt` grounded across support, operations, and compliance
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `analyst-copilot-loop`, the current collaboration-oriented instances, and at least one engineering instance so the next grounding batch stays inside the mixed-initiative family boundary.
2. Author exactly one engineering-domain instance linked to `analyst-copilot-loop`, framed as shared human-agent work around an engineering artifact rather than pure evidence synthesis, recommendation ranking, incident investigation, or browser execution.
3. Prefer a governance-aware engineering scenario where the shared artifact evolves across visible turns and the human retains responsibility for consequential interpretations, approvals, or external commitments.
4. Keep the batch limited to this single collaboration example so engineering-domain balance improves without widening the scope into multiple families.
5. Update `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the iteration log after that grounding batch so execution memory stays current.
6. Validate repository YAML with the existing uv-managed helper before closing the iteration.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer a modest grounding batch that improves one thin family/domain slice instead of forcing a broad cross-family sweep.
- Keep governance, reversibility, privacy, and auditability explicit in the new grounded example.
- Do not leave uncommitted changes before handing off to the authoring subagent.

## Expected outcome

The iteration should add one engineering-domain mixed-initiative collaboration example, improve `human-agent-collaborative-work` coverage, and leave the repository ready for another small grounding batch after the `.agent/` memory refresh.
