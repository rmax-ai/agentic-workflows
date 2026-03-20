# Canonical pattern schema guide

`schema/pattern.schema.json` defines the canonical document shape for workflow pattern entries. The schema is written as JSON Schema, but it is intended to validate YAML entries because YAML is the authoring format for structured ontology artifacts in this repository.

This guide explains what each field means, how much data it should usually contain, and where controlled vocabularies are expected to tighten the model later.

## Schema goals

The Phase 1 schema is designed to be:

- **canonical** enough to keep pattern entries consistent,
- **pragmatic** enough to permit authoring before vocabulary files exist,
- **extensible** enough to support later controlled references without reshaping every document.

In practice, that means many fields are typed as strings, arrays, or small objects today, with descriptions that indicate an eventual vocabulary-backed identifier.

## Document shape

A canonical pattern entry is a single object with required identity, structural, and governance fields.

### Required top-level fields

The schema requires these fields for every pattern:

- `id`
- `slug`
- `name`
- `summary`
- `pattern_family`
- `problem_structure`
- `domain`
- `workflow_goal`
- `inputs`
- `outputs`
- `environment`
- `capability_requirements`
- `execution_architecture`
- `autonomy_profile`
- `risk_governance`
- `why_agentic`
- `failure_modes`
- `evaluation`
- `maturity`
- `tags`

These requirements are intentionally opinionated. A pattern is incomplete if it lacks agentic rationale, governance framing, or an evaluation model.

## Canonical fields

### Identity and description

#### `id`
Stable canonical identifier. Use lower-kebab-case and treat it as the durable key.

Cardinality: exactly one string.

#### `slug`
Human-readable path-safe identifier. In most cases it will match `id`, but keeping both fields allows future path or display needs without changing the primary key.

Cardinality: exactly one string.

#### `name`
Display label for humans.

Cardinality: exactly one string.

#### `summary`
Short paragraph or compact sentence describing the pattern.

Cardinality: exactly one string.

### Classification

#### `pattern_family`
Primary family bucket for browse and coverage purposes.

Cardinality: exactly one string or reference object.

Vocabulary backing: expected later. Do not hardcode large enum lists in Phase 1; prefer stable identifiers that will map cleanly to future family vocabulary entries.

#### `problem_structure`
Primary reusable problem form represented by the pattern.

Cardinality: exactly one string or reference object.

Vocabulary backing: expected later.

#### `domain`
Domains where the pattern commonly appears. This is plural in meaning even though the field name stays singular for continuity with the initial repository plan.

Cardinality: one or more entries.

Vocabulary backing: expected later.

### Workflow semantics

#### `workflow_goal`
What successful execution achieves.

Cardinality: exactly one descriptive string.

#### `inputs`
Material the workflow consumes or inspects.

Cardinality: one or more structured items.

Each input item may include:

- `name`
- `description`
- `kind`
- `required`
- `examples`

#### `outputs`
Artifacts, decisions, updates, or actions produced by the workflow.

Cardinality: one or more structured items with the same general shape as `inputs`.

#### `environment`
Operating context such as systems touched, actors involved, data boundaries, and runtime conditions.

Cardinality: exactly one object.

The schema supports lists for systems, actors, constraints, and assumptions rather than forcing a single text blob.

### Agentic requirements

#### `capability_requirements`
Capabilities the workflow depends on, such as retrieval, planning, tool use, verification, coordination, or memory.

Cardinality: one or more capability entries.

Vocabulary backing: expected later.

#### `execution_architecture`
Architectural styles commonly used to realize the pattern.

Cardinality: one or more architecture entries.

Vocabulary backing: expected later.

#### `autonomy_profile`
How much discretion the agent has, where approvals sit, and what escalation boundaries apply.

Cardinality: exactly one object.

This object should describe autonomy level, human checkpoints, reversibility, and escalation expectations.

#### `risk_governance`
Risk posture and control expectations.

Cardinality: exactly one object.

This object should capture risk level, failure impact, auditability, privacy or security constraints, and approval boundaries.

#### `why_agentic`
Why the workflow benefits from agentic behavior instead of static automation.

Cardinality: one or more strings.

Use concise statements tied to planning, adaptation, exception handling, verification, statefulness, or coordination.

### Quality and evolution

#### `failure_modes`
Ways the workflow can fail, degrade, or cause harm.

Cardinality: one or more structured items.

The schema supports per-failure severity, detectability, and mitigations.

#### `evaluation`
How the pattern should be evaluated.

Cardinality: exactly one object.

Expected contents include success metrics, quality criteria, robustness checks, and optional benchmark notes.

#### `implementation_notes`
Optional implementation-oriented guidance.

Cardinality: zero or one object.

Use this for pragmatic notes about orchestration, integrations, or deployment concerns. Do not overload it with domain-specific examples that belong in instances.

#### `related_patterns`
Canonical links to adjacent, prerequisite, or contrastive patterns.

Cardinality: zero or more entries.

Prefer ids or compact reference objects rather than prose-only mentions.

#### `example_domains`
Optional short examples explaining how the same pattern manifests across domains.

Cardinality: zero or more objects.

This field is illustrative, not authoritative; it should not replace the main `domain` classification.

#### `maturity`
How developed and stable the pattern definition is.

Cardinality: exactly one string or reference object.

Suggested values may later come from a small controlled vocabulary such as draft, emerging, stable, or mature, but the Phase 1 schema leaves the field open.

#### `tags`
Freeform discovery aids.

Cardinality: one or more strings.

Tags should supplement, not replace, canonical fields.

## Vocabulary-backed fields

The schema is intentionally prepared for future controlled vocabularies in these areas:

- `pattern_family`
- `problem_structure`
- `domain`
- `capability_requirements[*]`
- `execution_architecture[*]`
- `autonomy_profile.level`
- `risk_governance.level`
- `maturity`

During Phase 1, these fields accept plain strings or lightweight reference objects. Later phases can tighten them by:

1. publishing vocabulary files with stable ids,
2. updating descriptions and examples,
3. optionally replacing permissive strings with `enum`, `const`, or `$ref` constraints once the vocabularies are mature.

## Reference pattern for future vocabularies

Where a field supports either a string or object, the preferred future object shape is intentionally simple:

```yaml
pattern_family:
  id: investigate-reconcile-verify
  label: Investigate / Reconcile / Verify
```

The schema only requires `id` for these reference objects today. `label`, `source_vocabulary`, and `notes` are optional so the transition to controlled vocabularies stays incremental.

## How to use the JSON schema

Typical workflow:

1. Author a canonical pattern entry in YAML under `data/patterns/` in a later phase.
2. Validate that YAML against `schema/pattern.schema.json` using a JSON Schema-compatible tool.
3. Resolve structural issues first, then vocabulary alignment issues.

Because YAML parsers generally convert YAML to an in-memory JSON-like object model before validation, the JSON Schema can validate the YAML content without requiring JSON as the storage format.

## Authoring guidance

- Prefer stable lower-kebab-case ids in vocabulary-shaped fields.
- Keep `summary` compact; put elaboration in structured fields.
- Use arrays where the workflow genuinely has multiple inputs, outputs, capabilities, or related patterns.
- Capture governance explicitly; do not bury approval gates or audit requirements in freeform prose.
- Keep example domains illustrative and secondary to the canonical pattern definition.

## Non-goals for Phase 1

The schema does **not** yet attempt to:

- hardcode every family, domain, architecture, or capability as enums,
- define separate schemas for views, vocabularies, or instances,
- encode every possible implementation nuance.

Those belong to later phases once the canonical pattern shape is stable.
