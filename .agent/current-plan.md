# Current Plan

## Iteration focus

Iteration `20260321-101259` is now scoped: the highest-leverage remaining family-safe gap is the missing `bounded-delegation` autonomy slice in `recommend-decide-escalate`. This iteration should add one canonical recommendation pattern that operates within delegated authority guardrails, plus a small set of grounded instances that show the shape without drifting into approval adjudication or execution.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement.
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory.
- Phase 4: top-level family overview docs are complete under `docs/patterns/`.
- Phase 5: canonical coverage spans forty patterns across all nine top-level pattern families, and every top-level family now has at least four canonical patterns while `transform-process`, `investigate-reconcile-verify`, `recommend-decide-escalate`, and `optimize-adapt` sit at five; `gather-retrieve-synthesize`, `monitor-detect-triage`, `plan-coordinate-schedule`, `execute-automate`, and `human-agent-collaborative-work` sit at four. The next canonical addition should stay narrow and only land where a remaining autonomy or architecture gap maps to a genuinely reusable workflow shape.
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains, with one hundred thirty-five instance files now committed.
- Phase 7: coverage refinement remains active, and all nine top-level families now span the full tracked `low` / `moderate` / `high` / `critical` risk ladder.
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path.
- Derived-view baseline: browse artifacts should continue to follow canonical pattern truth, especially when autonomy or architecture classifications change during refinement work.
- Current refinement target: `recommend-decide-escalate` is the only family still missing a natural `bounded-delegation` pattern, making it the cleanest next autonomy-balancing batch.

## Ordered tasks

1. Add one `recommend-decide-escalate` canonical pattern for bounded delegated option ranking or route recommendation inside preapproved authority guardrails, keeping the output in-family as a recommendation rather than an adjudicated approval or executed action.
2. Add a small linked instance batch that grounds the new recommendation shape in concrete delegated-authority scenarios without duplicating existing recommendation patterns.
3. Update derived architecture and autonomy browse views immediately after the canonical pattern lands so the new autonomy/architecture coverage remains reference-correct.
4. Refresh `.agent/` execution memory and validate repository YAML with `uv run python scripts/python/validate_yaml.py` before closing the iteration.

## Iteration checkpoint

- Timestamp: `20260321-101259`
- In-progress scope: add a family-safe `bounded-delegation` recommendation pattern plus a modest set of linked grounded examples, then update derived views and `.agent/` memory to reflect the new autonomy balance.
- Working hypothesis: `recommend-decide-escalate` can absorb a delegated-authority option-ranking pattern cleanly because the primary output remains a constrained recommendation packet with explicit escalation when requests exceed delegated bounds.
- Reflection placeholder: assess after the content batch whether the addition surfaces any new durable guidance about autonomy balancing or delegated-authority recommendation boundaries.

## Constraints

- Keep the ontology pattern-first: choose the next expansion because it fills a structural coverage gap, not because a domain example sounds appealing.
- Ensure every subagent task ends with exactly one git commit and leaves no unrelated file churn behind.
- Prefer one modest normalization batch over broader family expansion whenever derived views or execution memory drift from canonical pattern data.
- Keep governance, reversibility, privacy, and auditability explicit in every new pattern and instance.
- Keep future critical-risk refinements centered on each target family's own primary artifact boundary rather than letting severe workflows collapse into adjacent families.
- Treat collaboration-family work as in-family only if the primary output remains a critical shared artifact, explicit approval-readiness collaboration loop, or human-owned joint work surface rather than authority choice, command sequencing, or executed action.
- Treat the new verification-family batch as in-family only if the main output is an inspectable evidence verdict plus approval-gated release boundary, not a recommendation, correction package, or executed downstream change.
- Treat future optimize-family batches as in-family only if the main output remains an adaptive optimization-state change, sampled-policy adjustment, or bounded self-tuning artifact rather than alert triage, recommendation, scheduling, or executed operational change.
- Treat the new recommendation-family batch as in-family only if the output remains a bounded recommendation or narrowed option set inside delegated authority limits; anything that resolves the approval itself or commits the downstream change belongs in an adjacent family.

## Expected outcome

This iteration should leave the repository with one more family-safe autonomy slice covered: `recommend-decide-escalate` should gain a delegated-authority pattern grounded by linked instances, while browse views and `.agent/` memory remain synchronized with the new canonical truth.
