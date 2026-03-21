# Current Plan

## Iteration focus

Iteration `20260321-092906` is complete: it closed `optimize-adapt`'s missing `critical` risk slice with `critical-protected-priority-adaptation`, three linked grounded severe-state adaptation instances, and synchronized the optimize family doc plus the directly affected derived browse views. The next highest-leverage gap is now the remaining family-specific `critical` slice in `human-agent-collaborative-work`, provided it can stay centered on critical shared-work and approval ownership rather than authority recommendation, crisis planning, or execution.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement.
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory.
- Phase 4: top-level family overview docs are complete under `docs/patterns/`.
- Phase 5: canonical coverage spans thirty-seven patterns across all nine top-level pattern families, and every top-level family now has at least three canonical patterns while `transform-process` and `recommend-decide-escalate` sit at five; `gather-retrieve-synthesize`, `investigate-reconcile-verify`, `monitor-detect-triage`, `plan-coordinate-schedule`, `execute-automate`, and `optimize-adapt` sit at four; and `human-agent-collaborative-work` sits at three.
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains, with one hundred twenty-six instance files now committed.
- Phase 7: coverage refinement remains active, and `optimize-adapt` now joins `gather-retrieve-synthesize`, `transform-process`, `investigate-reconcile-verify`, `monitor-detect-triage`, `plan-coordinate-schedule`, `recommend-decide-escalate`, and `execute-automate` in spanning the full tracked risk ladder.
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path.

## Ordered tasks

1. Re-evaluate the remaining uncovered `critical` risk cells now that `optimize-adapt` also spans low, moderate, high, and critical coverage.
2. Identify the next family-specific `critical` refinement that can stay bounded at its own family boundary, with `human-agent-collaborative-work` the leading candidate if a severe shared-work or approval-ownership workflow can avoid drifting into authority recommendation, crisis planning, or execution.
3. Keep future Phase 7 batches modest, dependency-aware, and synchronized across canonical patterns, grounded instances, browse views, and `.agent/` execution memory.
4. Continue validating repository YAML with `uv run python scripts/python/validate_yaml.py` after each content batch before closing the iteration.

## Iteration checkpoint

- Timestamp: `20260321-092906`
- Completed scope: added `critical-protected-priority-adaptation`, three linked grounded instances in engineering, finance, and operations, and synchronized the optimize family doc plus the directly affected derived browse views in one feature commit.
- Updated coverage context: `optimize-adapt` now spans low-, moderate-, high-, and critical-risk slices and also adds an explicit critical `human-directed` optimization anchor centered on temporary severe-state retuning, expiry discipline, and rollback preparation.
- Reflection outcome: no new `.agent/proposals/` entry was added because the iteration did not surface a new durable loop, tooling, schema, or ontology improvement beyond already captured guidance.
- Planned orchestrator follow-up: validate the refreshed repository state, keep execution memory synchronized, and queue the remaining narrow uncovered `critical`-risk candidate in `human-agent-collaborative-work`.

## Constraints

- Keep the ontology pattern-first: choose the next expansion because it fills a structural coverage gap, not because a domain example sounds appealing.
- Ensure every subagent task ends with exactly one git commit and leaves no unrelated file churn behind.
- Prefer one modest batch with one new canonical pattern and a few instances over broader family expansion.
- Keep governance, reversibility, privacy, and auditability explicit in every new pattern and instance.
- Keep future critical-risk refinements centered on each target family's own primary artifact boundary rather than letting severe workflows collapse into adjacent families.
- Treat collaboration-family work as in-family only if the primary output remains a critical shared artifact, explicit approval-readiness collaboration loop, or human-owned joint work surface rather than authority choice, command sequencing, or executed action.
- Prefer one modest batch with one new canonical pattern and a few instances over broad family expansion.

## Expected outcome

This repository state now leaves `optimize-adapt` with representative `critical` risk coverage via one bounded severe-state protected-priority adaptation anchor and three grounded examples, while setting up `human-agent-collaborative-work` as the next likely narrow `critical`-risk refinement.
