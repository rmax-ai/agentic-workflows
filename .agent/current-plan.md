# Current Plan

## Iteration focus

Use the next Phase 6 batch to deepen the still-thinnest grounded family, `human-agent-collaborative-work`, while keeping an eye on remaining partial domain slices in recommendation, execution, transform, and optimization.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances now cover eleven total scenarios, with stronger finance and compliance coverage, but many family/domain cells remain partial and `human-agent-collaborative-work` still relies on a single grounded example
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `analyst-copilot-loop` plus its existing support instance and related family docs to choose the smallest useful follow-on collaboration grounding batch.
2. Add one new Markdown instance for `human-agent-collaborative-work`, preferably in research or compliance so the matrix gains a materially different collaboration scenario rather than another support escalation.
3. If a second instance still fits the batch cleanly, use it to deepen one remaining partial slice in recommendation, execution, transform, or optimize coverage without creating near-duplicate examples.
4. Keep new instances tightly linked to existing canonical YAML patterns and focused on concrete systems, workflows, accountability boundaries, and evaluation hooks.
5. Validate repository YAML after the follow-on `.agent/` memory updates that record the new instance coverage.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest instance batches that improve coverage balance across families, domains, and governance profiles without forcing a large cross-family sweep.
- Keep the next iteration scoped to instance authoring plus required `.agent/` memory updates; do not expand the canonical pattern set.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.

## Expected outcome

The next iteration should leave the repository with at least one new grounded collaboration example and a more balanced coverage matrix before returning to further canonical pattern expansion.
