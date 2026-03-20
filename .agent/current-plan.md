# Current Plan

## Iteration focus

Shift from initial pattern authoring to grounded expansion by adding the first Markdown instances for the new canonical patterns while planning the next seed-pattern batch.

## Current phase

- Phase 2: controlled vocabularies are complete
- Phase 3: navigation views are complete
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Tooling baseline: uv-managed Python 3.14 helper workflow is in place
- Phase 5: first canonical pattern batch landed in `data/patterns/`
- Phase 6: grounded instances are now the next dependency-safe expansion target for the mature seed patterns already in the repo

## Ordered tasks

1. Author the first grounded Markdown instances under `instances/` for `research-synthesis-with-citation-verification`, `incident-root-cause-analysis`, and `risk-alert-triage`, making sure each instance points back to one or more canonical YAML patterns.
2. Choose concrete but reusable scenarios that deepen domain grounding without collapsing the ontology into vendor-specific documentation.
3. Keep instance authoring aligned with the existing schema, vocabularies, browse views, and the governance posture already established in the canonical pattern files.
4. After the first instances land, resume Phase 5 with a second seed-pattern batch in still-empty families such as planning, recommendation, or execution.
5. Continue to avoid `transform-process` until a concrete pattern is justified despite the current `problem-structures` vocabulary gap, or until that gap is deliberately refined.
6. Validate new YAML and Markdown-adjacent references with the existing `uv`-managed helper tooling and normal repo review discipline after each batch.

## Constraints

- Keep Python tooling narrowly scoped to repository automation and helper scripts.
- Prefer standard-library Python first and add third-party packages only when justified.
- Keep shell entrypoints thin even if helper logic moves into Python.
- Use checked-in Python helpers instead of ad hoc Ruby for reusable validation or parsing tasks.
- Use the family overview docs as narrative constraints, not as alternate canonical data.
- Keep views aligned with the controlled vocabulary ids and treat them as derived browse artifacts.
- Ensure every subagent task ends with exactly one git commit.
- Keep early instance work tightly tied to existing canonical patterns; do not create standalone domain essays.

## Expected outcome

The next iteration should land a modest first set of grounded instances linked to the new canonical patterns, leaving the repository more navigable across both ontology and instance layers.
