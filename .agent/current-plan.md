# Current Plan

## Iteration focus

Begin Phase 4 pattern-family documentation now that Phase 3 browse views are committed and validated.

## Current phase

- Phase 2: controlled vocabularies are complete
- Phase 3: navigation views are complete
- Tooling baseline: uv-managed Python 3.14 helper workflow is in place
- Phase 4: create top-level pattern family docs in `docs/patterns/`

## Ordered tasks

1. Create `docs/patterns/` family overview files for the nine top-level pattern families in the established browse order.
2. Keep the family docs aligned with `docs/index-tree.md`, `data/views/index-tree.yaml`, and the existing controlled vocabularies so later pattern files inherit stable naming.
3. Note the temporary ontology gap where `transform-process` lacks a direct `problem-structures` mapping, but do not block family-doc authoring on that refinement.
4. Validate any new YAML changes with the existing `uv`-managed helper tooling.
5. After family docs land, move to a small batch of seed pattern YAML entries rather than broad generation.

## Constraints

- Keep Python tooling narrowly scoped to repository automation and helper scripts.
- Prefer standard-library Python first and add third-party packages only when justified.
- Keep shell entrypoints thin even if helper logic moves into Python.
- Use checked-in Python helpers instead of ad hoc Ruby for reusable validation or parsing tasks.
- Do not add canonical pattern entries before navigation views and family docs exist.
- Keep views aligned with the controlled vocabulary ids and treat them as derived browse artifacts.
- Ensure every subagent task ends with exactly one git commit.

## Expected outcome

The next iteration should land committed pattern-family docs that make the browse tree explainable to human readers and leave the repository ready for the first seed pattern batch.
