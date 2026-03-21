# Current Plan

## Iteration focus

Iteration `20260321-050550` is now scoped as a single Phase 7 canonical-pattern batch. The goal is to add one second `monitor-detect-triage` pattern that fills the thin `critical` risk cell while broadening `orchestrated-multi-agent` coverage beyond the current gather and investigation anchors without crossing into investigation or execution.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical coverage now spans ten patterns across all nine top-level pattern families
- Phase 6: grounded instances still cover all nine families across all seven currently modeled domains
- Phase 7: coverage refinement remains active, with the highest-leverage gaps now centered on sparse `low` and `critical` risk cells plus additional multi-agent breadth beyond the current gather/investigation anchors
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Author a second `monitor-detect-triage` canonical pattern that stays inside triage and routing boundaries while covering a `critical` risk posture.
2. Use the pattern to broaden `orchestrated-multi-agent` coverage into the monitoring family by structuring corroboration, enrichment, and escalation packaging as distinct coordinated roles.
3. Update only the directly derived browse artifacts needed to keep family, domain, autonomy, architecture, and risk navigation aligned with the new pattern.
4. Keep terminology aligned with the existing vocabularies, and record any genuinely new concept in `.agent/decisions.md` before it spreads across schema-adjacent files.
5. After the content commit, refresh `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the dated iteration log so execution memory continues to match repository reality.
6. Validate repository YAML with the existing uv-managed helper before closing the iteration.

## Iteration checkpoint

- Timestamp: `20260321-050550`
- In-flight subagent scope: author one new `monitor-detect-triage` canonical pattern plus the directly derived browse-view updates needed to keep navigation consistent.
- Pending orchestrator follow-up: refresh execution memory so the new canonical pattern inventory and structural coverage changes are reflected in status, coverage tracking, the repository map, the backlog, and the dated iteration log.

## Constraints

- Keep the ontology pattern-first: choose the next canonical expansion based on coverage gaps rather than domain-first duplication.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest, dependency-aware batches that improve one thin architecture or risk slice rather than forcing a broad cross-family sweep.
- Keep governance, reversibility, privacy, and auditability explicit in both canonical patterns and grounded examples.
- Do not widen the next iteration into vocabulary or schema changes unless a dependency issue makes that unavoidable.

## Expected outcome

This iteration should produce one carefully chosen second canonical pattern in `monitor-detect-triage` that improves sparse `critical` risk coverage and extends `orchestrated-multi-agent` into another family without diluting the current ontology boundaries.
