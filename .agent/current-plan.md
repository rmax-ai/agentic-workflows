# Current Plan

## Iteration focus

Iteration `20260321-094718` is complete: it added `evidence-gated-verification-for-release`, three linked evidence-gate verification instances in engineering, finance, and operations, and synchronized the directly affected investigate-family and browse-view artifacts. Iteration `20260321-095953` should now target the narrowest remaining autonomy concentration by adding one family-safe `autonomous-with-audit` pattern outside `execute-automate`, with `optimize-adapt` as the leading candidate family.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement.
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory.
- Phase 4: top-level family overview docs are complete under `docs/patterns/`.
- Phase 5: canonical coverage spans thirty-nine patterns across all nine top-level pattern families, and every top-level family now has at least four canonical patterns while `transform-process`, `investigate-reconcile-verify`, and `recommend-decide-escalate` sit at five; `gather-retrieve-synthesize`, `monitor-detect-triage`, `plan-coordinate-schedule`, `execute-automate`, `optimize-adapt`, and `human-agent-collaborative-work` sit at four.
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains, with one hundred thirty-two instance files now committed.
- Phase 7: coverage refinement remains active, and all nine top-level families now span the full tracked `low` / `moderate` / `high` / `critical` risk ladder.
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path.

## Ordered tasks

1. Target the remaining `autonomous-with-audit` concentration, which currently sits only in `execute-automate`, with one family-safe refinement outside direct execution.
2. Prefer an `optimize-adapt` pattern only if the main output remains a reversible optimization-state change, bounded self-tuning loop, or audit-ready adaptive policy update rather than recommendation, coordination, or direct execution.
3. Keep the batch modest: one canonical pattern, a few linked instances, and only the directly affected family and derived view updates.
4. Continue validating repository YAML with `uv run python scripts/python/validate_yaml.py` after each content batch before closing the iteration.

## Iteration checkpoint

- Timestamp: `20260321-095953`
- Planned scope: add one `optimize-adapt` canonical pattern only if it cleanly represents a low-consequence or bounded self-tuning workflow that can run as `autonomous-with-audit` without drifting into direct execution.
- Coverage intent: extend `autonomous-with-audit` beyond `execute-automate` while keeping the family boundary centered on optimization-state adaptation, logged rollback, and ex post governance rather than routine human approval.
- Commit plan: create one scope commit for this plan update, one feature commit from a narrow subagent, then one orchestrator record commit after validation and memory updates.
- Planned orchestrator follow-up: validate the refreshed repository state, write `.agent/iterations/2026/20260321-095953.md`, and update status and coverage memory to reflect the new autonomy placement.

## Constraints

- Keep the ontology pattern-first: choose the next expansion because it fills a structural coverage gap, not because a domain example sounds appealing.
- Ensure every subagent task ends with exactly one git commit and leaves no unrelated file churn behind.
- Prefer one modest batch with one new canonical pattern and a few instances over broader family expansion.
- Keep governance, reversibility, privacy, and auditability explicit in every new pattern and instance.
- Keep future critical-risk refinements centered on each target family's own primary artifact boundary rather than letting severe workflows collapse into adjacent families.
- Treat collaboration-family work as in-family only if the primary output remains a critical shared artifact, explicit approval-readiness collaboration loop, or human-owned joint work surface rather than authority choice, command sequencing, or executed action.
- Treat the new verification-family batch as in-family only if the main output is an inspectable evidence verdict plus approval-gated release boundary, not a recommendation, correction package, or executed downstream change.
- Treat the new optimize-family batch as in-family only if the main output remains an adaptive optimization-state change, sampled-policy adjustment, or bounded self-tuning artifact rather than alert triage, recommendation, scheduling, or executed operational change.

## Expected outcome

This iteration should leave the repository with one additional family-safe `autonomous-with-audit` anchor outside `execute-automate`, plus synchronized grounded examples and derived views, while preserving the optimize/adapt family boundary around governed feedback-driven change rather than direct action.
