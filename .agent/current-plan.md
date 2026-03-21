# Current Plan

## Iteration focus

Iteration `20260321-102507` is now complete: `plan-coordinate-schedule` gained `contingency-plan-activation-gate` to cover a clean approval-gated contingency-planning slice, along with three linked critical-domain instances and the derived browse-view updates required by the new canonical pattern.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement.
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory.
- Phase 4: top-level family overview docs are complete under `docs/patterns/`.
- Phase 5: canonical coverage now spans forty-two patterns across all nine top-level pattern families, and every top-level family still has at least four canonical patterns while `recommend-decide-escalate` now sits at six; `transform-process`, `investigate-reconcile-verify`, `optimize-adapt`, and `plan-coordinate-schedule` sit at five; and `gather-retrieve-synthesize`, `monitor-detect-triage`, `execute-automate`, and `human-agent-collaborative-work` sit at four. Future additions should remain narrow and land only where a remaining autonomy or architecture gap maps to a genuinely reusable workflow shape.
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains, with one hundred forty instance files now committed.
- Phase 7: coverage refinement remains active, and all nine top-level families now span the full tracked `low` / `moderate` / `high` / `critical` risk ladder.
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path.
- Derived-view baseline: browse artifacts should continue to follow canonical pattern truth, especially when autonomy or architecture classifications change during refinement work.
- Current refinement target: the planning-family approval-gated gap is now closed, so the next refinement step should inspect the remaining family-safe autonomy or architecture concentrations rather than reopening planning-family scope immediately.

## Ordered tasks

1. Inspect the remaining autonomy and architecture concentrations for another genuinely family-safe refinement opportunity before adding more canonical content.
2. Prefer the next batch to stay similarly narrow: one reusable shape, modest grounded examples, and only the derived browse-view updates that follow directly from canonical truth.
3. Continue updating `.agent/` execution memory and validating repository YAML with `uv run python scripts/python/validate_yaml.py` for each committed refinement batch.

## Iteration checkpoint

- Timestamp: `20260321-102507`
- Completed scope: added `contingency-plan-activation-gate`, linked finance, operations, and compliance instances, and refreshed the derived index, architecture, autonomy, risk, and domain views plus `.agent/` execution memory.
- Working result: `plan-coordinate-schedule` now covers approval-gated contingency readiness cleanly by ending at a human-approved activation packet, readiness ledger, and hold register rather than authority recommendation, truth verification, or fallback execution.
- Reflection: the cleanest way to extend planning into `approval-gated-execution` was to treat the gate as a coordination-readiness artifact for a declared contingency, not as a disguised decision or action workflow.

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

## Expected outcome

This iteration leaves the repository with one more family-safe planning slice covered: `plan-coordinate-schedule` now includes an approval-gated contingency-activation pattern grounded by linked critical-domain instances, and the browse views plus `.agent/` memory are synchronized with the new canonical truth.
