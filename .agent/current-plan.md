# Current Plan

## Iteration focus

Iteration `20260321-050550` is complete: it added `critical-signal-corroboration-triage` as a second `monitor-detect-triage` pattern, filling that family's thin `critical` risk cell while broadening `orchestrated-multi-agent` coverage beyond the earlier gather and investigation anchors without crossing into investigation or execution.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical coverage now spans eleven patterns across all nine top-level pattern families
- Phase 6: grounded instances still cover all nine families across all seven currently modeled domains
- Phase 7: coverage refinement remains active, with the highest-leverage gaps now centered on sparse `low` risk cells plus additional multi-agent breadth beyond the current gather, investigation, and monitoring anchors
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `.agent/coverage-matrix.yaml`, the family overview docs, and the canonical pattern set before selecting the next refinement batch.
2. Prefer the next bounded batch to add one second canonical pattern in a family that still has only one entry and can legitimately expand `low` risk coverage outside `plan-coordinate-schedule`, or broaden `orchestrated-multi-agent` into another family.
3. Prioritize patterns that stay cleanly within their family boundary while improving one thin structural cell rather than reopening already-balanced family/domain coverage.
4. Keep terminology aligned with the existing vocabularies, and record any genuinely new concept in `.agent/decisions.md` before it spreads across schema-adjacent files.
5. After the next content commit, refresh `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the dated iteration log so execution memory continues to match repository reality.
6. Validate repository YAML with the existing uv-managed helper before closing the next iteration.

## Iteration checkpoint

- Timestamp: `20260321-050550`
- Completed subagent scope: authored `data/patterns/monitor-detect-triage/critical-signal-corroboration-triage.yaml` and updated the linked browse views in one focused content commit.
- Completed orchestrator follow-up: refreshed execution memory so the new canonical pattern inventory and structural coverage changes are reflected in status, coverage tracking, the repository map, the backlog, and the dated iteration log.

## Constraints

- Keep the ontology pattern-first: choose the next canonical expansion based on coverage gaps rather than domain-first duplication.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest, dependency-aware batches that improve one thin architecture or risk slice rather than forcing a broad cross-family sweep.
- Keep governance, reversibility, privacy, and auditability explicit in both canonical patterns and grounded examples.
- Do not widen the next iteration into vocabulary or schema changes unless a dependency issue makes that unavoidable.

## Expected outcome

The next iteration should likely add one carefully chosen second canonical pattern that improves sparse `low` risk coverage outside `plan-coordinate-schedule`, or extends `orchestrated-multi-agent` into another family without diluting the current ontology boundaries.
