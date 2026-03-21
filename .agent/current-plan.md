# Current Plan

## Iteration focus

Add the first grounded `transform-process` example, then pair it with one `optimize-adapt` instance so this iteration improves both the last ungrounded family and one other lightly grounded family without expanding scope beyond Phase 6.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances still cover only seven total scenarios, so many family/domain cells remain partial
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read the `document-to-structured-data-handoff` and `queue-prioritization-optimization` canonical patterns plus neighboring instance files to keep the new grounding aligned with established instance structure.
2. Author the first `transform-process` Markdown instance in a finance, compliance, or operations scenario where schema fidelity, provenance, and exception routing are concrete and inspectable.
3. Add one additional `optimize-adapt` instance in support, operations, or compliance so a second newer family gains grounded coverage in the same iteration.
4. Keep both instances tightly linked to existing canonical YAML patterns and focused on specific systems, workflows, governance choices, and evaluation hooks rather than generic domain summaries.
5. Validate repository YAML after the follow-on `.agent/` memory updates that record the new instance coverage.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest instance batches that improve coverage balance across families and domains without forcing a large cross-family sweep.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.

## Expected outcome

This iteration should leave the repository with the first grounded `transform-process` example and one additional grounded `optimize-adapt` example, plus updated memory that records the new coverage state and next Phase 6 target.
