# Current Plan

## Iteration focus

Iteration `20260321-114951` is now complete: `recommend-decide-escalate` gained the new `approval-gated-recommendation-release` slice plus linked engineering, finance, and compliance examples. The family boundary held because approval governs release of one exact recommendation packet revision into one bounded human decision lane, while the actual choice remains explicitly human-owned.

Iteration `20260321-115928` is now complete: `approval-gated-recommendation-release` gained new research, support, and HR grounding, and the canonical pattern metadata plus derived domain view now expose that slice across six domains without drifting past packet release into decision adjudication or execution.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement.
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory.
- Phase 4: top-level family overview docs are complete under `docs/patterns/`.
- Phase 5: canonical coverage now spans forty-nine patterns across all nine top-level pattern families. `recommend-decide-escalate` now sits at seven canonical patterns; `transform-process` and `optimize-adapt` each sit at six; `gather-retrieve-synthesize` now sits at five; and `monitor-detect-triage`, `investigate-reconcile-verify`, `plan-coordinate-schedule`, `execute-automate`, and `human-agent-collaborative-work` each remain at five. Future additions should remain narrow and land only where a genuinely reusable workflow shape deepens uneven grounded coverage rather than duplicating already-covered matrix cells.
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains, with one hundred sixty-four instance files now committed.
- Phase 7: coverage refinement remains active, all nine top-level families now span the full tracked `low` / `moderate` / `high` / `critical` risk ladder and all tracked architecture types. The next refinement target should stay on balancing grounded depth across underrepresented domains and governance-heavy approval-bound slices rather than adding fresh structural inventory.
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path.
- Derived-view baseline: browse artifacts should continue to follow canonical pattern truth, especially when autonomy or architecture classifications change during refinement work.
- Current refinement target: continue approval-bound depth balancing after the latest recommend-family expansion, starting with either the remaining operations grounding gap for `approval-gated-recommendation-release` or another comparably thin approval-bound slice in a neighboring family.

## Ordered tasks

1. Choose the next approval-bound depth-balancing batch by comparing the remaining operations gap in `approval-gated-recommendation-release` against other thin approval-gated slices in adjacent families.
2. Prefer new instances or small normalization passes over new canonical patterns unless a genuinely missing structural shape appears.
3. Keep future batches at the same scale as this one: one bounded family target, a few grounded examples, and only directly dependent memory or view updates.
4. Continue validating repository YAML with `uv run python scripts/python/validate_yaml.py` after each bounded batch.

## Iteration checkpoint

- Timestamp: `20260321-115928`
- Previous completed scope: added `approval-gated-briefing-release`, linked engineering, operations, and finance approval-bound briefing-release instances, updated the gather/retrieve/synthesize family doc, refreshed the derived index, domain, architecture, autonomy, and risk views, and confirmed YAML validation still passes.
- Completed scope: added research, support, and HR approval-bound recommendation-packet release instances for `approval-gated-recommendation-release`, expanded the canonical pattern's domain and example metadata, refreshed the derived domain view, and confirmed YAML validation still passes.
- Current working hypothesis: approval-gated refinement is family-safe only when the governed object is one exact artifact revision and one bounded downstream lane; for the recommend family, that means packet release must stay distinct from the actual human decision.
- Current scoped follow-on: use the newly broadened recommend-family approval-gated slice as the reference shape for evaluating the next thin approval-bound family/domain combination without reopening schema or view-wide changes.
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

The next iteration should stay in depth-balancing mode: add a small number of grounded examples or normalization updates where underrepresented domains and approval-bound governance slices are still comparatively thin, with a bias toward finishing near-complete family/domain slices before opening broader new batches.
