# Current Plan

## Iteration focus

Iteration `20260321-051222` is complete: it added `policy-constrained-escalation-routing` as a second `recommend-decide-escalate` pattern, broadening `orchestrated-multi-agent` coverage into that family while keeping the boundary at governed routing and escalation packaging. A follow-up fix aligned `data/views/by-domain.yaml` with the canonical pattern's domain list.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical coverage now spans twelve patterns across all nine top-level pattern families, with `recommend-decide-escalate` now holding a second canonical anchor
- Phase 6: grounded instances still cover all nine families across all seven currently modeled domains
- Phase 7: coverage refinement remains active, with the highest-leverage gaps now centered on sparse `low` risk cells outside `plan-coordinate-schedule` now that multi-agent breadth reaches gather, investigation, monitoring, and recommendation families
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `.agent/coverage-matrix.yaml`, the family overview docs, and the canonical pattern set before selecting the next low-risk refinement target.
2. Prefer the next bounded batch to add one second canonical pattern in a family that still has only one entry and can legitimately expand `low` risk coverage outside `plan-coordinate-schedule`.
3. Prioritize patterns that stay cleanly within their family boundary while improving one thin structural cell rather than reopening already-balanced family/domain coverage.
4. Keep terminology aligned with the existing vocabularies, and record any genuinely new concept in `.agent/decisions.md` before it spreads across schema-adjacent files.
5. After the next content commit, refresh `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the dated iteration log so execution memory continues to match repository reality.
6. Validate repository YAML with the existing uv-managed helper before closing the next iteration.

## Iteration checkpoint

- Timestamp: `20260321-051222`
- Completed subagent scope: authored `data/patterns/recommend-decide-escalate/policy-constrained-escalation-routing.yaml` and updated the linked browse views in one focused content commit.
- Completed orchestrator follow-up: corrected the derived domain view to match the canonical pattern domains, validated repository YAML, and refreshed execution memory so the new canonical pattern inventory and structural coverage changes are reflected in status, coverage tracking, the repository map, the backlog, and the dated iteration log.

## Constraints

- Keep the ontology pattern-first: choose the next canonical expansion based on coverage gaps rather than domain-first duplication.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer a modest, dependency-aware batch that improves one thin low-risk slice without forcing new instances in the same iteration.
- Keep governance, reversibility, privacy, and auditability explicit in the canonical pattern wording.
- Do not widen this iteration into vocabulary or schema changes unless a dependency issue makes that unavoidable.

## Expected outcome

The next iteration should likely add one carefully chosen low-risk canonical pattern outside `plan-coordinate-schedule`, ideally in a family that still has only one canonical entry and can expand coverage without diluting current ontology boundaries.
