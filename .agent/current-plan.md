# Current Plan

## Iteration focus

Iteration `20260321-114951` is now complete: `recommend-decide-escalate` gained the new `approval-gated-recommendation-release` slice plus linked engineering, finance, and compliance examples. The family boundary held because approval governs release of one exact recommendation packet revision into one bounded human decision lane, while the actual choice remains explicitly human-owned.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement.
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory.
- Phase 4: top-level family overview docs are complete under `docs/patterns/`.
- Phase 5: canonical coverage now spans forty-nine patterns across all nine top-level pattern families. `recommend-decide-escalate` now sits at seven canonical patterns; `transform-process` and `optimize-adapt` each sit at six; `gather-retrieve-synthesize` now sits at five; and `monitor-detect-triage`, `investigate-reconcile-verify`, `plan-coordinate-schedule`, `execute-automate`, and `human-agent-collaborative-work` each remain at five. Future additions should remain narrow and land only where a genuinely reusable workflow shape deepens uneven grounded coverage rather than duplicating already-covered matrix cells.
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains, with one hundred sixty-one instance files now committed.
- Phase 7: coverage refinement remains active, all nine top-level families now span the full tracked `low` / `moderate` / `high` / `critical` risk ladder and all tracked architecture types. The next refinement target should shift from matrix closure to balancing grounded depth across underrepresented domains and governance-heavy approval-bound slices.
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path.
- Derived-view baseline: browse artifacts should continue to follow canonical pattern truth, especially when autonomy or architecture classifications change during refinement work.
- Current refinement target: rebalance grounded coverage in thinner domains such as HR, research, and compliance, especially where newly completed approval-bound pattern slices still have only one or two representative instance clusters.

## Ordered tasks

1. Rebalance grounded depth in underrepresented domains, starting with a modest batch in one or two families where approval-bound or high-governance slices still have thin instance coverage.
2. Prefer new instances or small normalization passes over new canonical patterns unless a genuinely missing structural shape appears.
3. Keep future batches at the same scale as this one: one bounded family target, a few grounded examples, and only directly dependent memory or view updates.
4. Continue validating repository YAML with `uv run python scripts/python/validate_yaml.py` after each bounded batch.

## Iteration checkpoint

- Timestamp: `20260321-114951`
- Previous completed scope: added `approval-gated-briefing-release`, linked engineering, operations, and finance approval-bound briefing-release instances, updated the gather/retrieve/synthesize family doc, refreshed the derived index, domain, architecture, autonomy, and risk views, and confirmed YAML validation still passes.
- Completed scope: added `approval-gated-recommendation-release`, linked engineering, finance, and compliance approval-bound recommendation-packet release instances, updated the recommend/decide/escalate family doc, refreshed the derived index, domain, architecture, autonomy, and risk views, and confirmed YAML validation still passes.
- Current working hypothesis: approval-gated refinement is family-safe only when the governed object is one exact artifact revision and one bounded downstream lane; for the recommend family, that means packet release must stay distinct from the actual human decision.
- Boundary reminder: future approval-gated work should remain tied to one exact artifact revision and one bounded handoff lane rather than broad permission to keep recommending, coordinating, or executing.

## Constraints

- Keep the ontology pattern-first: choose the next expansion because it fills a structural coverage gap, not because a domain example sounds appealing.
- Ensure every subagent task ends with exactly one git commit and leaves no unrelated file churn behind.
- Prefer one modest normalization batch over broader family expansion whenever derived views or execution memory drift from canonical pattern data.
- Keep governance, reversibility, privacy, and auditability explicit in every new pattern and instance.
- Keep future critical-risk refinements centered on each target family's own primary artifact boundary rather than letting severe workflows collapse into adjacent families.
- Treat the completed gather-family refinement as valid only because approval governs one exact synthesized briefing or context-package revision, with audience scope, freshness, and hold/release state explicit, rather than vague permission to brief, recommend, or act.
- Treat future transform-family additions as in-family only if the primary artifact remains a transformed package, lineage trace, explicit hold state, or approval/release manifest rather than a crisis brief, evidence verdict, recommendation, or downstream execution step.
- Treat collaboration-family work as in-family only if the primary output remains a critical shared artifact, explicit approval-readiness collaboration loop, or human-owned joint work surface rather than authority choice, command sequencing, or executed action.
- Treat future recommendation-family additions as in-family only if the output remains a bounded recommendation or narrowed option set inside delegated authority limits; anything that resolves the approval itself or commits the downstream change belongs in an adjacent family.
- Treat future optimize-family batches as in-family only if the main output remains an adaptive optimization-state change, sampled-policy adjustment, or bounded self-tuning artifact rather than alert triage, recommendation, scheduling, or executed operational change.
- Treat the current optimize-family approval-gated slice as valid only if approval governs one exact tuning or optimization-state revision, with expiry and rollback readiness explicit, rather than a vague permission to keep optimizing.
- Treat future monitor-family additions as in-family only if the output remains watchlisting, anomaly packet assembly, or triage routing; anything that binds approval to downstream action or settles truth should stay in an adjacent family.
- Treat future collaboration-family additions as valid only if approval or release control governs a protected shared artifact or joint work surface while leaving authority choice, command sequencing, recommendation adjudication, and operational action to adjacent patterns.

## Expected outcome

The next iteration should pivot from family-by-architecture closure to depth balancing: add a small number of grounded examples or normalization updates where underrepresented domains and approval-bound governance slices are still comparatively thin.
