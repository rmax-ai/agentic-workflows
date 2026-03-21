# Current Plan

## Iteration focus

Iteration `20260321-025122` is now scoped as a single-instance operations grounding batch for `investigate-reconcile-verify`. The goal is to add one operations-domain example linked to `incident-root-cause-analysis`, because operations already has monitoring, scheduling, recommendation, execution, optimization, transformation, and synthesis grounding but still lacks a direct investigation anchor. Keep the work tightly bounded to evidence reconciliation, competing hypotheses, and human-gated remediation or escalation decisions.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances now cover thirty-six total scenarios, with `gather-retrieve-synthesize` grounded across research, engineering, finance, compliance, operations, support, and HR, `investigate-reconcile-verify` grounded across engineering, finance, and compliance, `monitor-detect-triage` grounded across engineering, finance, compliance, operations, and support, `recommend-decide-escalate` grounded across finance, compliance, and operations, `execute-automate` grounded across finance, compliance, HR, operations, and support, `optimize-adapt` grounded across support, operations, and compliance, and `human-agent-collaborative-work` grounded across engineering, research, compliance, and support
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `incident-root-cause-analysis`, the current investigation-oriented instances, and the existing operations-domain artifacts so the new grounding stays inside the investigation family boundary.
2. Author exactly one operations-domain instance linked to `incident-root-cause-analysis`, framed as governed discrepancy or failure investigation rather than triage, execution, optimization, synthesis, or collaboration.
3. Prefer an operations scenario where evidence reconciliation, competing hypotheses, and escalation thresholds are explicit, with human control over remediation, customer, safety, or incident-command commitments.
4. Keep the batch limited to this single investigation example so coverage improves without widening the scope into multiple families.
5. After the subagent commit, update `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and `.agent/iterations/2026/20260321-025122.md` so execution memory reflects the new grounding and the next gap.
6. Validate repository YAML with the existing uv-managed helper before closing the iteration.

## Iteration checkpoint

- Timestamp: `20260321-025122`
- Planned subagent scope: author one operations-domain `incident-root-cause-analysis` grounding file and commit it separately.
- Planned orchestrator follow-up: refresh `.agent/` memory, write the dated iteration log, and re-run YAML validation before the closing memory commit.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve coverage balance inside one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.
- Do not widen the next iteration into pattern, vocabulary, or schema changes unless dependency order clearly demands it.

## Expected outcome

This iteration should add one operations-domain investigation example, improve `investigate-reconcile-verify` coverage, and leave the repository ready for another small grounding batch after the `.agent/` memory refresh.
