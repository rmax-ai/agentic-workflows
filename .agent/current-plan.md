# Current Plan

## Iteration focus
Use the newly committed controlled vocabularies to create Phase 3 navigation views without introducing a second source of truth.

## Current phase
- Phase 2: controlled vocabularies are complete
- Phase 3: create pattern-first and alternate browse views

## Ordered tasks
1. Create `data/views/index-tree.yaml` using the established pattern families and link strategy from `docs/index-tree.md`.
2. Create alternate browse views for domain, architecture, autonomy, and risk using the controlled vocabulary ids from `data/vocabularies/`.
3. Keep view artifacts reference-oriented so they can be regenerated once pattern files exist.
4. After views land, prepare the top-level `docs/patterns/` family docs before seed pattern authoring.

## Constraints
- Do not add canonical pattern entries before navigation views and family docs exist.
- Keep views aligned with the controlled vocabulary ids and treat them as derived browse artifacts.
- Ensure every subagent task ends with exactly one git commit.

## Expected outcome
The next iteration should end with committed browse views that make the ontology more navigable and set up focused pattern family documentation.
