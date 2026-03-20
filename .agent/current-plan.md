# Current Plan

## Iteration focus

Use the newly expanded canonical pattern layer to resume Phase 6 with a three-instance batch for compliance, operations, and HR grounded in the planning, recommendation, and execution patterns before returning to the remaining empty families.

## Current phase

- Phase 2: controlled vocabularies are complete
- Phase 3: navigation views are complete
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Tooling baseline: uv-managed Python 3.14 helper workflow is in place
- Phase 5: a second canonical pattern batch now covers planning, recommendation, and execution families in addition to the initial gather, investigate, and monitor anchors
- Phase 6: the repository has first grounded instances plus several newly stable patterns that now justify another targeted instance batch

## Ordered tasks

1. Add a three-instance follow-on batch tied to `calendar-conflict-coordination`, `deal-desk-recommendation-support`, and `browser-based-form-completion-with-approval-gates`.
2. Prioritize uncovered instance domains by landing one concrete compliance instance, one operations instance, and one HR instance so grounded coverage catches up with the canonical layer.
3. Keep each instance tightly linked to one or more canonical YAML patterns and focused on a real operational scenario rather than a generic domain essay.
4. After the instance batch lands, reassess whether the next highest-leverage step is an `optimize-adapt` or `human-agent-collaborative-work` pattern batch.
5. Continue to avoid `transform-process` until a concrete pattern is justified despite the current `problem-structures` vocabulary gap, or until that gap is deliberately refined.

## Constraints

- Keep Python tooling narrowly scoped to repository automation and helper scripts.
- Prefer standard-library Python first and add third-party packages only when justified.
- Keep shell entrypoints thin even if helper logic moves into Python.
- Use checked-in Python helpers instead of ad hoc Ruby for reusable validation or parsing tasks.
- Use the family overview docs as narrative constraints, not as alternate canonical data.
- Keep views aligned with the controlled vocabulary ids and treat them as derived browse artifacts.
- Ensure every subagent task ends with exactly one git commit.
- Keep instance work tightly tied to existing canonical patterns; do not create standalone domain essays.
- Prefer tasks that improve domain grounding and governance coverage rather than duplicating already-grounded examples.
- Favor next steps that make the coverage matrix more balanced across domains, architectures, autonomy levels, and risk levels.

## Expected outcome

The next iteration should leave the repository with broader grounded coverage for the newly added patterns, explicit compliance/operations/HR scenario support, and a better-informed basis for the next family-expansion decision.
