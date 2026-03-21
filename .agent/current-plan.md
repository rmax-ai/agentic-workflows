# Current Plan

## Iteration focus

Iteration `20260321-100858` is complete: it normalized a derived-view drift by moving `adaptive-review-sampling-rate-tuning` into the `autonomous-with-audit` bucket in `data/views/by-autonomy.yaml`, then refreshed the directly affected `.agent/` memory so the repository state and execution memory agree again. The next highest-leverage step is to resume inspecting the remaining narrow autonomy and architecture concentrations only after this normalization baseline is secure.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement.
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory.
- Phase 4: top-level family overview docs are complete under `docs/patterns/`.
- Phase 5: canonical coverage spans forty patterns across all nine top-level pattern families, and every top-level family now has at least four canonical patterns while `transform-process`, `investigate-reconcile-verify`, `recommend-decide-escalate`, and `optimize-adapt` sit at five; `gather-retrieve-synthesize`, `monitor-detect-triage`, `plan-coordinate-schedule`, `execute-automate`, and `human-agent-collaborative-work` sit at four.
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains, with one hundred thirty-five instance files now committed.
- Phase 7: coverage refinement remains active, and all nine top-level families now span the full tracked `low` / `moderate` / `high` / `critical` risk ladder.
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path.
- Derived-view baseline: browse artifacts should continue to follow canonical pattern truth, especially when autonomy or architecture classifications change during refinement work.

## Ordered tasks

1. Reassess the remaining narrow autonomy and architecture concentrations now that `autonomous-with-audit` is correctly represented in both `execute-automate` and `optimize-adapt`.
2. Favor another family-clean refinement only if it represents a real reusable workflow shape rather than a coverage exercise; likely candidates remain a natural approval-gated-execution or autonomous-with-audit variant outside the currently covered families.
3. Keep future batches modest and synchronized across canonical patterns, grounded instances, browse views, and `.agent/` execution memory.
4. Continue validating repository YAML with `uv run python scripts/python/validate_yaml.py` after each content batch before closing the iteration.

## Iteration checkpoint

- Timestamp: `20260321-100858`
- Completed scope: corrected the stale autonomy placement in `data/views/by-autonomy.yaml`, revalidated repository YAML, and refreshed `.agent/current-plan.md`, `.agent/ontology-status.yaml`, and `.agent/coverage-matrix.yaml` so the normalization is recorded explicitly.
- Working conclusion: the canonical pattern file remains authoritative for autonomy classification, and derived browse artifacts should be normalized immediately whenever refinement work changes a pattern's modeled control boundary.
- Reflection outcome: no new `.agent/proposals/` entry is needed because this iteration surfaced a local derivation drift, not a new durable process or tooling gap beyond the existing guidance to keep views derived and reference-oriented.

## Constraints

- Keep the ontology pattern-first: choose the next expansion because it fills a structural coverage gap, not because a domain example sounds appealing.
- Ensure every subagent task ends with exactly one git commit and leaves no unrelated file churn behind.
- Prefer one modest normalization batch over broader family expansion whenever derived views or execution memory drift from canonical pattern data.
- Keep governance, reversibility, privacy, and auditability explicit in every new pattern and instance.
- Keep future critical-risk refinements centered on each target family's own primary artifact boundary rather than letting severe workflows collapse into adjacent families.
- Treat collaboration-family work as in-family only if the primary output remains a critical shared artifact, explicit approval-readiness collaboration loop, or human-owned joint work surface rather than authority choice, command sequencing, or executed action.
- Treat the new verification-family batch as in-family only if the main output is an inspectable evidence verdict plus approval-gated release boundary, not a recommendation, correction package, or executed downstream change.
- Treat future optimize-family batches as in-family only if the main output remains an adaptive optimization-state change, sampled-policy adjustment, or bounded self-tuning artifact rather than alert triage, recommendation, scheduling, or executed operational change.

## Expected outcome

This repository state now leaves `autonomous-with-audit` correctly represented in both `execute-automate` and `optimize-adapt` across canonical pattern data, derived browse views, and `.agent/` memory. The next iteration should return to another narrow autonomy or architecture refinement only if it remains equally family-safe.
