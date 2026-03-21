# Current Plan

## Iteration focus

Ground the newly seeded `transform-process` family with its first linked instance, then use a small instance batch to reduce partial coverage in other lightly grounded families.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances still cover only seven total scenarios, so many family/domain cells remain partial
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read the new `data/patterns/transform-process/document-to-structured-data-handoff.yaml` pattern plus neighboring weakly grounded pattern files to choose a modest instance batch.
2. Author the first `transform-process` Markdown instance in either finance, compliance, or operations so the new family is grounded before further pattern expansion.
3. Add one or two additional grounded instances for families that still have only one example, prioritizing partial cells in `optimize-adapt`, `recommend-decide-escalate`, `execute-automate`, or `human-agent-collaborative-work`.
4. Keep new instances tightly linked to existing canonical YAML patterns and focused on concrete target systems, workflows, and governance choices rather than generic domain overviews.
5. Validate repository YAML after any memory or canonical-data updates that accompany the instance batch.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest instance batches that improve coverage balance across families, domains, architectures, and risk levels.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.

## Expected outcome

The next iteration should leave the repository with the first grounded `transform-process` example and a more balanced coverage matrix across the newer families that currently have only one instance each.
