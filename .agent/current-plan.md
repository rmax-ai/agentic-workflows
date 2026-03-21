# Current Plan

## Iteration focus

Iteration `20260321-032912` is now in progress. The repository is still in Phase 6, and the highest-leverage next step is to deepen `transform-process` with exactly one HR-domain grounding for `document-to-structured-data-handoff`. The chosen slice is a governance-sensitive leave-intake scenario where a multi-document leave packet is transformed into a structured case staging record without making any eligibility, accommodation, payroll, or manager-notification decision.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage spans all nine top-level pattern families
- Phase 6: grounded instances currently cover forty-four scenarios, with `transform-process` grounded across finance, compliance, operations, and support but still missing HR, engineering, and research
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `document-to-structured-data-handoff`, existing transform-process instances, and adjacent HR-domain artifacts before authoring new content.
2. Author exactly one new HR-domain instance linked to `document-to-structured-data-handoff`.
3. Keep the scenario bounded to document-to-record transformation: heterogeneous leave-request documents should become a structured leave-case staging record with provenance, exception routing, privacy-aware handling, and explicit human review boundaries.
4. Avoid drift into recommendation, accommodation adjudication, payroll execution, or employee communication commitments; the workflow stops at a reviewable staged record.
5. Keep the content batch limited to this single instance so coverage improves without widening scope.
6. After the instance commit, refresh `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the dated iteration log.
7. Validate repository YAML with `uv run python scripts/python/validate_yaml.py` before closing the iteration.

## Iteration checkpoint

- Timestamp: `20260321-032912`
- Planned subagent scope: add one HR `document-to-structured-data-handoff` instance centered on a leave-intake packet to structured case-record handoff.
- Planned orchestrator follow-up: refresh execution memory so Phase 6 status and coverage tracking reflect the new HR transform grounding.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing new seed patterns.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.
- Do not widen this iteration into pattern, vocabulary, or schema changes unless a dependency issue makes that unavoidable.

## Expected outcome

This iteration should add one HR-domain `transform-process` example, raise `transform-process` from four grounded domains to five, and leave the repository ready for another small Phase 6 grounding batch after `.agent/` memory refresh.
