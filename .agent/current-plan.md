# Current Plan

## Iteration focus

Iteration `20260321-103612` is now scoped: close the remaining `execute-automate` autonomy gap by adding one human-directed execution pattern, grounding it with a modest cross-domain instance batch, and refreshing only the derived browse views and execution memory that should follow from that canonical addition.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement.
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory.
- Phase 4: top-level family overview docs are complete under `docs/patterns/`.
- Phase 5: canonical coverage now spans forty-two patterns across all nine top-level pattern families, and every top-level family still has at least four canonical patterns while `recommend-decide-escalate` now sits at six; `transform-process`, `investigate-reconcile-verify`, `optimize-adapt`, and `plan-coordinate-schedule` sit at five; and `gather-retrieve-synthesize`, `monitor-detect-triage`, `execute-automate`, and `human-agent-collaborative-work` sit at four. Future additions should remain narrow and land only where a remaining autonomy or architecture gap maps to a genuinely reusable workflow shape.
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains, with one hundred forty instance files now committed.
- Phase 7: coverage refinement remains active, and all nine top-level families now span the full tracked `low` / `moderate` / `high` / `critical` risk ladder.
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path.
- Derived-view baseline: browse artifacts should continue to follow canonical pattern truth, especially when autonomy or architecture classifications change during refinement work.
- Current refinement target: `execute-automate` still lacks a clean `human-directed` autonomy slice even though the family already spans approval-gated, bounded-delegation, exception-gated autonomy, and autonomous-with-audit execution. The next batch should close that gap with an action-first pattern whose main artifact is completed operational work under explicit human step direction rather than a recommendation, plan, or shared collaboration surface.

## Ordered tasks

1. Add one new `execute-automate` canonical pattern for human-directed multi-step execution under explicit operator control, keeping the family boundary centered on completed operational action rather than planning, recommendation, or collaboration.
2. Ground the new pattern with 2-3 linked instances in domains where guided execution is structurally natural, starting with engineering, operations, and compliance.
3. Refresh only the derived browse views (`index-tree`, `by-domain`, `by-architecture`, `by-autonomy`, `by-risk`) and `.agent/` execution memory that change as a direct consequence of the new canonical truth.
4. Validate repository YAML with `uv run python scripts/python/validate_yaml.py` after the content batch and again after the final memory refresh if those files change.

## Iteration checkpoint

- Timestamp: `20260321-103612`
- Ready scope: add a human-directed execution pattern under `execute-automate`, link a small engineering/operations/compliance instance batch, and refresh the derived browse views that consume canonical pattern metadata.
- Intended result: `execute-automate` should no longer have an empty `human-directed` autonomy bucket, while still preserving its family boundary at controlled operational action rather than recommendation, planning, or shared collaborative authorship.
- Design guardrail: keep the new pattern centered on operator-directed step execution with durable state, explicit takeover points, and bounded agent assistance, not on approval gating, generic copilot work, or event-triggered closure.

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

This iteration should leave the repository with one more family-safe execution slice covered: `execute-automate` gains a human-directed execution pattern grounded by linked engineering, operations, and compliance examples, and the browse views plus `.agent/` memory stay synchronized with that canonical truth.
