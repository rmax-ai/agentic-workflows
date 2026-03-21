# Current Plan

## Iteration focus

The last iteration added a second grounded `human-agent-collaborative-work` example in `research`, so the next Phase 6 batch should either close the remaining collaboration gap in `compliance` or, if a cleaner opportunity appears, deepen another thin partial slice in `transform-process`, `execute-automate`, or `optimize-adapt`.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances now cover twelve total scenarios, with broader research coverage and a stronger `human-agent-collaborative-work` family footprint, but many family/domain cells remain partial
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `analyst-copilot-loop`, the new research collaboration instance, and existing compliance examples to decide whether the cleanest next gain is a compliance copilot-loop scenario or another thin family/domain slice.
2. Prefer one new `instances/compliance/` collaboration example if it can materially differ from the support and research copilot cases while keeping explicit accountability boundaries.
3. If collaboration/compliance would be too duplicative, choose one small grounded instance in `transform-process`, `execute-automate`, or `optimize-adapt` that closes a partial cell with a clearly distinct workflow.
4. Keep new instances tightly linked to existing canonical YAML patterns and focused on concrete systems, governance checkpoints, provenance, and evaluation hooks.
5. Update `.agent/` memory after the batch and validate repository YAML.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve coverage balance across families and domains without forcing a broad cross-family sweep.
- Keep the next iteration scoped to instance authoring plus required `.agent/` memory updates; do not expand the canonical pattern set unless dependency order changes.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.

## Expected outcome

The next iteration should either close the compliance gap for `human-agent-collaborative-work` or visibly improve another thin partial coverage cell while preserving the repository's pattern-first structure.
