# Current Plan

## Iteration focus

Iteration `20260321-104838` is in progress: inspect the remaining family-safe architecture imbalances, choose one narrow `approval-gated-execution` gap only if it cleanly fits the family boundary, and land a single canonical pattern with a few linked instances plus the directly derived browse-view updates.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement.
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory.
- Phase 4: top-level family overview docs are complete under `docs/patterns/`.
- Phase 5: canonical coverage now spans forty-three patterns across all nine top-level pattern families, and every top-level family still has at least four canonical patterns while `recommend-decide-escalate` remains at six; `transform-process`, `investigate-reconcile-verify`, `optimize-adapt`, and `plan-coordinate-schedule` remain at five; `execute-automate` now also sits at five; and `gather-retrieve-synthesize`, `monitor-detect-triage`, and `human-agent-collaborative-work` remain at four. Future additions should remain narrow and land only where a remaining autonomy or architecture gap maps to a genuinely reusable workflow shape.
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains, with one hundred forty-three instance files now committed.
- Phase 7: coverage refinement remains active, and all nine top-level families now span the full tracked `low` / `moderate` / `high` / `critical` risk ladder.
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path.
- Derived-view baseline: browse artifacts should continue to follow canonical pattern truth, especially when autonomy or architecture classifications change during refinement work.
- Current refinement target: inspect the remaining empty `approval-gated-execution` architecture cells and fill at most one more family-safe gap this iteration, only if the pattern can remain tightly bounded within its family's primary artifact and stop point.

## Ordered tasks

1. Select the single safest remaining `approval-gated-execution` architecture gap by re-checking family boundaries, neighboring patterns, and whether the stop point remains pre-execution or approval-gated within-family output.
2. Use one scoped subagent batch to add that one reusable shape, two or three grounded instances, and only the derived browse-view updates that follow directly from canonical truth.
3. Continue updating `.agent/` execution memory and validating repository YAML with `uv run python scripts/python/validate_yaml.py` for each committed refinement batch.

## Iteration checkpoint

- Timestamp: `20260321-103612`
- Completed scope: added `human-directed-task-orchestration` under `execute-automate`, linked engineering, operations, and compliance guided-execution instances, and refreshed the derived index, domain, architecture, autonomy, and risk views.
- Working result: `execute-automate` now spans all six tracked autonomy levels, with the new pattern keeping the family boundary centered on live operational action under explicit human direction rather than delegated routine execution, browser gating, or shared collaboration.
- Reflection: the cleanest way to add human-directed execution was to anchor the pattern on authoritative step ledgers, verified state after each consequential action, and takeover-safe resumption packets instead of letting the family drift into planning or copilot-style artifact work.

## Constraints

- Keep the ontology pattern-first: choose the next expansion because it fills a structural coverage gap, not because a domain example sounds appealing.
- Ensure every subagent task ends with exactly one git commit and leaves no unrelated file churn behind.
- Prefer one modest normalization batch over broader family expansion whenever derived views or execution memory drift from canonical pattern data.
- Keep governance, reversibility, privacy, and auditability explicit in every new pattern and instance.
- Keep future critical-risk refinements centered on each target family's own primary artifact boundary rather than letting severe workflows collapse into adjacent families.
- Treat collaboration-family work as in-family only if the primary output remains a critical shared artifact, explicit approval-readiness collaboration loop, or human-owned joint work surface rather than authority choice, command sequencing, or executed action.
- Treat the new verification-family batch as in-family only if the main output is an inspectable evidence verdict plus approval-gated release boundary, not a recommendation, correction package, or executed downstream change.
- Treat future optimize-family batches as in-family only if the main output remains an adaptive optimization-state change, sampled-policy adjustment, or bounded self-tuning artifact rather than alert triage, recommendation, scheduling, or executed operational change.
- Treat future recommendation-family batches as in-family only if the output remains a bounded recommendation or narrowed option set inside delegated authority limits; anything that resolves the approval itself or commits the downstream change belongs in an adjacent family.
- Treat the new planning-family batch as in-family only if the output remains a contingency-activation readiness ledger, explicit hold state, and approval-gated coordination packet rather than a decision recommendation, verification verdict, or executed contingency step.
- Treat future planning-family additions as in-family only if the primary artifact remains a plan, checkpoint ledger, readiness packet, or coordination-state update; once the workflow crosses into gate adjudication or live fallback action, it belongs elsewhere.
- Treat the new execution-family batch as in-family only if the primary artifact remains real operational completion under explicit human step direction; if the work mainly narrows options, prepares a packet, or maintains a shared collaborative workspace, it belongs in an adjacent family instead.

## Expected outcome

This iteration leaves the repository with one more family-safe execution slice covered: `execute-automate` now includes a human-directed execution pattern grounded by linked engineering, operations, and compliance examples, and the browse views plus `.agent/` memory are synchronized with that canonical truth.
