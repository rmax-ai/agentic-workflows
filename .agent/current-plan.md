# Current Plan

## Iteration focus

Iteration `20260321-101259` is now complete: `recommend-decide-escalate` gained `delegated-authority-option-ranking` to close the remaining family-safe `bounded-delegation` autonomy gap, along with two linked instances and the derived browse-view updates required by the new canonical pattern.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement.
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory.
- Phase 4: top-level family overview docs are complete under `docs/patterns/`.
- Phase 5: canonical coverage now spans forty-one patterns across all nine top-level pattern families, and every top-level family still has at least four canonical patterns while `recommend-decide-escalate` now sits at six, `transform-process`, `investigate-reconcile-verify`, and `optimize-adapt` sit at five, and `gather-retrieve-synthesize`, `monitor-detect-triage`, `plan-coordinate-schedule`, `execute-automate`, and `human-agent-collaborative-work` sit at four. Future additions should remain narrow and land only where a remaining autonomy or architecture gap maps to a genuinely reusable workflow shape.
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains, with one hundred thirty-seven instance files now committed.
- Phase 7: coverage refinement remains active, and all nine top-level families now span the full tracked `low` / `moderate` / `high` / `critical` risk ladder.
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path.
- Derived-view baseline: browse artifacts should continue to follow canonical pattern truth, especially when autonomy or architecture classifications change during refinement work.
- Current refinement target: the recommendation-family `bounded-delegation` gap is now closed, so the next refinement step should inspect the remaining family-safe autonomy or architecture concentrations rather than reopening recommendation-family scope.

## Ordered tasks

1. Inspect the remaining autonomy and architecture concentrations for another genuinely family-safe refinement opportunity before adding more canonical content.
2. Prefer the next batch to stay similarly narrow: one reusable shape, modest grounded examples, and only the derived browse-view updates that follow directly from canonical truth.
3. Continue updating `.agent/` execution memory and validating repository YAML with `uv run python scripts/python/validate_yaml.py` for each committed refinement batch.

## Iteration checkpoint

- Timestamp: `20260321-101259`
- Completed scope: added `delegated-authority-option-ranking`, linked finance and operations instances, and refreshed the derived index, architecture, autonomy, risk, and domain views plus `.agent/` execution memory.
- Working result: the family now covers delegated-authority recommendation cleanly by keeping the output to a bounded in-band option set, boundary register, and escalation packet rather than approval adjudication, scheduling, or execution.
- Reflection: this batch confirmed that the cleanest way to add `bounded-delegation` to `recommend-decide-escalate` is a guardrail-constrained option-ranking shape rather than escalation routing, collaboration, or delegated action.

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

## Expected outcome

This iteration leaves the repository with one more family-safe autonomy slice covered: `recommend-decide-escalate` now includes a delegated-authority recommendation pattern grounded by linked instances, and the browse views plus `.agent/` memory are synchronized with the new canonical truth.
