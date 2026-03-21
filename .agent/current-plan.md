# Current Plan

## Iteration focus

Iteration `20260321-045339` is complete: it added one research-domain `monitor-detect-triage` instance linked to `risk-alert-triage`, closing the final open domain slice in that family with a benchmark-study disclosure risk alert scenario. The repository can now shift from family/domain balancing to broader architecture and risk refinement.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage spans all nine top-level pattern families
- Phase 6: grounded instances now cover sixty-three scenarios, and every top-level family now has at least one grounded instance in all seven currently modeled domains
- Phase 7: coverage refinement remains the active phase, but the highest-leverage remaining gaps now sit in partial architecture and risk coverage rather than family/domain coverage
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `.agent/coverage-matrix.yaml`, the family overview docs, and the canonical pattern set before selecting the next refinement batch.
2. Prefer the next bounded batch to add one second canonical pattern in a thin family so architecture or risk coverage improves without duplicating an existing seed entry.
3. Prioritize underrepresented cells such as `orchestrated-multi-agent` outside the current investigation anchor, or sparse `low` / `critical` risk coverage outside the current planning and execution anchors.
4. Keep terminology aligned with the existing vocabularies, and record any genuinely new concept in `.agent/decisions.md` before it spreads across schema-adjacent files.
5. After the next content commit, refresh `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the dated iteration log so execution memory continues to match repository reality.
6. Validate repository YAML with the existing uv-managed helper before closing the next iteration.

## Iteration checkpoint

- Timestamp: `20260321-045339`
- Completed subagent scope: authored `instances/research/benchmark-study-disclosure-risk-alert-triage.md` as one research-domain `risk-alert-triage` grounding change and committed it separately.
- Completed orchestrator follow-up: refreshed execution memory so the new monitoring coverage is reflected in status, coverage tracking, the repository map, the dated iteration log, and the next-step plan.

## Constraints

- Keep the ontology pattern-first: choose the next canonical expansion based on coverage gaps rather than domain-first duplication.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest, dependency-aware batches that improve one thin architecture or risk slice rather than forcing a broad cross-family sweep.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.
- Do not widen this iteration into pattern, vocabulary, or schema changes unless a dependency issue makes that unavoidable.

## Expected outcome

The next iteration should likely add one carefully chosen second canonical pattern that improves architecture or risk coverage and then refresh the linked browse and memory artifacts accordingly.
