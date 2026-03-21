# Current Plan

## Iteration focus

Iteration `20260321-091136` is now scoped: the highest-leverage next gap is `plan-coordinate-schedule`'s missing `critical` risk slice, and this iteration should close it with one bounded critical planning/coordination pattern plus a few linked grounded instances if the work can stay strictly on critical coordination-state restoration or command-window re-sequencing rather than triage, recommendation, or execution.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement.
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory.
- Phase 4: top-level family overview docs are complete under `docs/patterns/`.
- Phase 5: canonical coverage spans thirty-four patterns across all nine top-level pattern families, and every top-level family now has at least three canonical patterns while `transform-process` sits at five, `gather-retrieve-synthesize`, `monitor-detect-triage`, `recommend-decide-escalate`, and `investigate-reconcile-verify` sit at four, and the remaining families currently sit at three pending this iteration's bounded planning-family refinement.
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains, with one hundred seventeen instance files now committed.
- Phase 7: coverage refinement remains active, and `investigate-reconcile-verify` now joins `gather-retrieve-synthesize`, `transform-process`, `monitor-detect-triage`, and `execute-automate` in spanning the full tracked risk ladder.
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path.

## Ordered tasks

1. Add one `plan-coordinate-schedule` pattern that fills the family's missing `critical` risk cell while remaining bounded at critical coordination-state restoration, emergency re-sequencing, or command-window control rather than triage, recommendation, or execution.
2. Ground that new planning pattern with a small set of representative instances in domains where critical coordination-state freshness materially matters.
3. Synchronize the planning family doc plus only the directly affected derived browse views and coverage memory after the content batch lands.
4. Continue validating repository YAML with `uv run python scripts/python/validate_yaml.py` after the feature batch and again before closing the iteration.

## Iteration checkpoint

- Timestamp: `20260321-091136`
- Starting scope: target a single bounded `plan-coordinate-schedule` refinement that fills the family's missing `critical` risk cell and, if feasible, also fills its empty `human-directed` autonomy slice without changing the ontology spine.
- Planned feature batch: add one critical planning pattern, two to three linked grounded instances, and the directly affected planning-family and derived-view updates in one feature commit.
- Planned orchestrator follow-up: validate the refreshed repository state, record the dated iteration summary, synchronize coverage and status counts, and queue the next narrow uncovered `critical` slice only after this planning-family closure is reflected in `.agent/`.

## Constraints

- Keep the ontology pattern-first: choose the expansion because it fills a structural coverage gap, not because a domain example sounds appealing.
- Ensure every subagent task ends with exactly one git commit and leaves no unrelated file churn behind.
- Prefer a modest, dependency-aware batch that strengthens one family with one new pattern and a few instances rather than reopening broad expansion.
- Keep governance, reversibility, privacy, and auditability explicit in every new pattern and instance.
- Keep this critical-risk planning refinement centered on schedule authority, participant alignment, and bounded command-window coordination rather than alert triage, route recommendation, deep diagnosis, or downstream execution.
- Treat the work as in-family only if the primary output remains a critical coordination artifact such as a re-sequenced command timeline, authoritative checkpoint ledger, or explicitly held coordination packet rather than a brief, verdict, policy choice, or executed system change.
- Prefer one modest batch with one new canonical pattern and a few instances over broad family expansion.

## Expected outcome

This iteration should leave `plan-coordinate-schedule` with representative `critical` risk coverage via one bounded high-consequence coordination anchor and a few grounded examples, while keeping the ontology pattern-first and the completed content batch modest.
