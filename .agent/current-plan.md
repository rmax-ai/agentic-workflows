# Current Plan

## Iteration focus

Iteration `20260321-100858` is reserved for consistency normalization after a drift check found that `adaptive-review-sampling-rate-tuning` is modeled as `autonomous-with-audit` in canonical pattern data and `.agent/` memory, while `data/views/by-autonomy.yaml` still places it under `approval-gated`. The highest-leverage next step is to repair the derived autonomy view and any directly affected metadata before adding more coverage.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement.
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory.
- Phase 4: top-level family overview docs are complete under `docs/patterns/`.
- Phase 5: canonical coverage spans forty patterns across all nine top-level pattern families, and every top-level family now has at least four canonical patterns while `transform-process`, `investigate-reconcile-verify`, `recommend-decide-escalate`, and `optimize-adapt` sit at five; `gather-retrieve-synthesize`, `monitor-detect-triage`, `plan-coordinate-schedule`, `execute-automate`, and `human-agent-collaborative-work` sit at four.
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains, with one hundred thirty-five instance files now committed.
- Phase 7: coverage refinement remains active, and all nine top-level families now span the full tracked `low` / `moderate` / `high` / `critical` risk ladder.
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path.
- Immediate normalization target: the browse-by-autonomy view must stay derived from canonical `autonomy_profile.level` values and should not lag behind recent pattern changes.

## Ordered tasks

1. Normalize the derived autonomy browse view so `adaptive-review-sampling-rate-tuning` appears under `autonomous-with-audit` rather than `approval-gated`, and inspect directly adjacent metadata for the same drift.
2. Revalidate the affected coverage and status artifacts after the browse-view correction so the repository memory and derived navigation stay mutually consistent.
3. Only resume autonomy or architecture expansion after the normalization batch is complete and validated.
4. Continue validating repository YAML with `uv run python scripts/python/validate_yaml.py` after each content batch before closing the iteration.

## Iteration checkpoint

- Timestamp: `20260321-100858`
- Planned scope: correct the derived autonomy-view classification drift around `adaptive-review-sampling-rate-tuning`, validate the repaired browse artifact, and update `.agent/` memory so the iteration history records the normalization.
- Working assumption: the canonical pattern file is authoritative for autonomy classification, so derived browse artifacts and memory should follow it rather than reclassifying the pattern ad hoc.
- Planned orchestrator follow-up: validate the refreshed repository state, record the iteration in `.agent/iterations/2026/20260321-100858.md`, and then reassess whether the next batch should return to autonomy/architecture expansion or stay focused on additional derivation consistency checks.

## Constraints

- Keep the ontology pattern-first: choose the next expansion because it fills a structural coverage gap, not because a domain example sounds appealing.
- Ensure every subagent task ends with exactly one git commit and leaves no unrelated file churn behind.
- Prefer one modest normalization batch over broader family expansion when derived views or execution memory drift from canonical pattern data.
- Keep governance, reversibility, privacy, and auditability explicit in every new pattern and instance.
- Keep future critical-risk refinements centered on each target family's own primary artifact boundary rather than letting severe workflows collapse into adjacent families.
- Treat collaboration-family work as in-family only if the primary output remains a critical shared artifact, explicit approval-readiness collaboration loop, or human-owned joint work surface rather than authority choice, command sequencing, or executed action.
- Treat the new verification-family batch as in-family only if the main output is an inspectable evidence verdict plus approval-gated release boundary, not a recommendation, correction package, or executed downstream change.
- Treat future optimize-family batches as in-family only if the main output remains an adaptive optimization-state change, sampled-policy adjustment, or bounded self-tuning artifact rather than alert triage, recommendation, scheduling, or executed operational change.

## Expected outcome

This repository state now leaves `autonomous-with-audit` represented in both `execute-automate` and `optimize-adapt` while preserving clean family boundaries. The next iteration should continue with another narrow autonomy or architecture refinement only if it remains equally family-safe.
