# Current Plan

## Iteration focus

Use the next Phase 6 batch to deepen still-thin grounded coverage in lightly represented families, especially recommendation, execution, and human-agent collaboration, now that `transform-process` and `optimize-adapt` each have their first linked example.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances now cover nine total scenarios, but many family/domain cells remain partial and several families still rely on a single grounded example
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read the lightly grounded recommendation, execution, and collaboration patterns plus their existing instances to choose the smallest useful follow-on grounding batch.
2. Add one or two new Markdown instances for families that still have only one example, prioritizing `recommend-decide-escalate`, `execute-automate`, or `human-agent-collaborative-work`.
3. Prefer domains and governance contexts not yet grounded for those families so the matrix gains genuinely new representative coverage rather than near-duplicates.
4. Keep new instances tightly linked to existing canonical YAML patterns and focused on concrete systems, workflows, accountability boundaries, and evaluation hooks.
5. Validate repository YAML after the follow-on `.agent/` memory updates that record the new instance coverage.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest instance batches that improve coverage balance across families, domains, and governance profiles without forcing a large cross-family sweep.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.

## Expected outcome

The next iteration should leave the repository with one or two new grounded examples in still-thin families and a more balanced coverage matrix before returning to further canonical pattern expansion.
