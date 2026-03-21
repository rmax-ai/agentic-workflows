# Current Plan

## Iteration focus

Iteration `20260321-102507` is now scoped around one family-safe planning refinement: add an approval-gated contingency-activation pattern under `plan-coordinate-schedule`, ground it with a small critical-domain instance batch, and refresh only the derived browse views and `.agent/` memory that follow from the new canonical truth.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement.
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory.
- Phase 4: top-level family overview docs are complete under `docs/patterns/`.
- Phase 5: canonical coverage now spans forty-one patterns across all nine top-level pattern families, and every top-level family still has at least four canonical patterns while `recommend-decide-escalate` now sits at six, `transform-process`, `investigate-reconcile-verify`, and `optimize-adapt` sit at five, and `gather-retrieve-synthesize`, `monitor-detect-triage`, `plan-coordinate-schedule`, `execute-automate`, and `human-agent-collaborative-work` sit at four. Future additions should remain narrow and land only where a remaining autonomy or architecture gap maps to a genuinely reusable workflow shape.
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains, with one hundred thirty-seven instance files now committed.
- Phase 7: coverage refinement remains active, and all nine top-level families now span the full tracked `low` / `moderate` / `high` / `critical` risk ladder.
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path.
- Derived-view baseline: browse artifacts should continue to follow canonical pattern truth, especially when autonomy or architecture classifications change during refinement work.
- Current refinement target: `plan-coordinate-schedule` is the cleanest next family-safe candidate because it can naturally absorb an `approval-gated` / `approval-gated-execution` slice without drifting into downstream execution or upstream recommendation.

## Ordered tasks

1. Add one `plan-coordinate-schedule` pattern for approval-gated contingency activation that stays bounded at readiness gating, explicit holds, and coordination-packet handoff rather than executing the contingency itself.
2. Ground the new planning pattern with a modest critical-domain instance batch, preferably in finance, operations, and compliance where contingency-activation governance is concrete and adjacent-family boundaries are already documented.
3. Refresh only the derived browse views and `.agent/` execution memory implied by the canonical addition, then validate repository YAML with `uv run python scripts/python/validate_yaml.py`.

## Iteration checkpoint

- Timestamp: `20260321-102507`
- Planned scope: add one approval-gated contingency-activation planning pattern, link a small critical-domain instance batch, and refresh the derived index, architecture, autonomy, risk, and domain views plus `.agent/` execution memory if the canonical addition lands cleanly.
- Working hypothesis: the cleanest remaining narrow architecture gap is a planning workflow that prepares and gates contingency activation readiness without choosing the authority lane, verifying truth, or executing the contingency.
- Reflection target: confirm that the new pattern's main artifact remains a human-approved coordination or activation packet so the batch stays within `plan-coordinate-schedule` rather than leaking into recommendation or execution.

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

## Expected outcome

This iteration should leave the repository with one more family-safe planning slice covered: `plan-coordinate-schedule` gains an approval-gated contingency-activation pattern grounded by linked critical-domain instances, and the browse views plus `.agent/` memory remain synchronized with the new canonical truth.
