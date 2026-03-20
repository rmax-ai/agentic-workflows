# Current Plan

## Iteration focus

Land the first canonical pattern in `human-agent-collaborative-work`, then refresh execution memory so the next iteration can decide between support-domain grounding and a justified `transform-process` refinement from a cleaner baseline.

## Current phase

- Phase 2: controlled vocabularies are complete
- Phase 3: navigation views are complete
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Tooling baseline: uv-managed Python 3.14 helper workflow is in place
- Phase 5: canonical patterns now cover `optimize-adapt` in addition to the initial gather, investigate, monitor, planning, recommendation, and execution anchors
- Phase 6: the repository now has six grounded instances spanning research, engineering, finance, operations, compliance, and HR

## Ordered tasks

1. Add the first canonical pattern in `human-agent-collaborative-work`, using the existing `human-agent-collaboration` problem-structure term and keeping the pattern centered on mixed initiative, explicit handoffs, and shared responsibility rather than a thin approval wrapper.
2. Re-read the relevant family overview doc, schema, vocabularies, neighboring patterns, and coverage matrix before authoring the pattern and the minimum required derived-view updates.
3. Validate repository YAML after the canonical pattern lands so the new family anchor does not break the existing schema-aligned corpus.
4. After the empty-family pattern lands, reassess the next highest-leverage gap between support-domain grounding and a justified `transform-process` vocabulary refinement.
5. Continue using grounded instances only as domain evidence and cross-link context rather than as substitutes for canonical YAML pattern structure.

## Constraints

- Keep Python tooling narrowly scoped to repository automation and helper scripts.
- Prefer standard-library Python first and add third-party packages only when justified.
- Keep shell entrypoints thin even if helper logic moves into Python.
- Use checked-in Python helpers instead of ad hoc Ruby for reusable validation or parsing tasks.
- Use the family overview docs as narrative constraints, not as alternate canonical data.
- Keep views aligned with the controlled vocabulary ids and treat them as derived browse artifacts.
- Ensure every subagent task ends with exactly one git commit.
- Keep canonical pattern work tightly aligned with the existing schema, vocabularies, and family boundaries.
- Prefer tasks that improve coverage in still-empty families before adding more instances to already-grounded families.
- Favor next steps that make the coverage matrix more balanced across families, domains, architectures, autonomy levels, and risk levels.

## Expected outcome

The next iteration should leave the repository with the first canonical pattern in `human-agent-collaborative-work`, updated browse linkage for that family, validated YAML, and refreshed execution memory that points cleanly to the next coverage move.
