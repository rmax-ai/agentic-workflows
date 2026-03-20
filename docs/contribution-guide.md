# Contribution guide

This repository is built in strict dependency order. Contributors should add ontology content only when the prerequisite layer is already stable.

## Contribution priorities

Always work in this order:

1. foundational docs
2. canonical schema
3. controlled vocabularies
4. browse views
5. canonical pattern entries
6. grounded instances
7. coverage refinement

Do not skip ahead by authoring lots of patterns or examples before the schema and vocabulary layers are ready.

## File placement rules

### `README.md`

Repository entry point. It should explain the pattern-first mission and point readers to the foundational docs.

### `docs/`

Human-readable guidance for repository structure and ontology rules.

Use this directory for:

- ontology documentation,
- schema guidance,
- browse model documentation,
- contribution rules,
- later pattern-family documentation.

Do **not** use `docs/` as the canonical home for structured pattern data.

### `schema/`

JSON Schema and later supporting schema assets.

Use this directory for contracts that validate canonical structured files.

### Helper tooling

Repository automation that grows beyond simple shell orchestration should live in checked-in Python helpers managed through `uv`.

Use this rule of thumb:

- keep shell scripts for thin orchestration,
- move reusable parsing, validation, or repository logic into Python,
- prefer `uv run python ...` over ad hoc Ruby or one-off interpreter snippets,
- keep dependencies narrow and standard-library-first unless a real need appears.

### `data/vocabularies/`

Controlled vocabulary YAML files for families, domains, architectures, capabilities, autonomy levels, and governance levels.

Vocabulary files should define reusable terms, not individual patterns.

### `data/patterns/`

Canonical YAML entries for workflow patterns.

Each file should represent one canonical pattern and validate against the pattern schema.

### `data/views/`

Derived browse artifacts and generated indexes.

These files should reference canonical patterns; they should not become a second source of truth.

### `instances/`

Grounded Markdown examples, scenarios, or case studies linked to canonical patterns.

Instances should enrich the ontology with context, not replace the canonical pattern definition.

## Naming conventions

### Identifiers

Use lower-kebab-case for stable identifiers, filenames, and vocabulary ids.

Examples:

- `multi-source-synthesis`
- `event-driven-monitoring`
- `approval-gated-execution`

### Filenames

Prefer one canonical entity per file.

- Pattern schema: `schema/pattern.schema.json`
- Pattern family docs: `docs/patterns/<family>.md`
- Canonical patterns: `data/patterns/<pattern-id>.yaml`
- Vocabulary files: plural category names such as `data/vocabularies/domains.yaml`
- Instances: descriptive kebab-case names such as `instances/finance-month-end-reconciliation.md`

### Headings and labels

Use human-readable headings in Markdown, but keep the backing ids stable and machine-friendly.

## Authoring workflow

### 1. Decide the correct layer

Before writing anything, determine whether the content belongs to:

- ontology documentation,
- schema definition,
- controlled vocabulary,
- canonical pattern,
- derived view,
- grounded instance.

If the content mixes multiple layers, split it rather than stuffing everything into one file.

### 2. Reuse before inventing

Before creating a new pattern, check whether the structure already exists and only needs an added domain reference or related instance.

A new domain example does not automatically justify a new canonical pattern.

### 3. Define structure before breadth

It is better to have a smaller number of well-normalized patterns than a large number of shallow, overlapping entries.

### 4. Keep governance explicit

If a workflow has approval gates, privacy constraints, irreversible actions, audit requirements, or high failure cost, capture them directly in the canonical fields instead of burying them in prose.

### 5. Link related artifacts

When later phases add patterns and instances:

- patterns should link to related patterns,
- instances should link to canonical pattern ids,
- views should reference canonical pattern ids,
- vocabulary-backed fields should use stable terms.

## Dependency order in practice

### Foundational phase

Allowed work:

- ontology model docs,
- schema docs,
- contribution rules,
- canonical schema files.

Not yet allowed:

- broad pattern authoring,
- vocabulary sprawl,
- generated browse views,
- large batches of instances.

### Vocabulary phase

Allowed work:

- controlled vocabularies that stabilize high-reuse fields.

Patterns should wait until these vocabularies are coherent enough to prevent naming drift.

### Pattern phase

Allowed work:

- high-quality canonical pattern entries,
- carefully linked related patterns,
- example domains.

Pattern files should validate structurally and align with repository vocabulary choices.

### Instance phase

Allowed work:

- grounded examples,
- realistic scenarios,
- implementation-specific context.

Instances should not silently redefine the canonical pattern.

## Quality bar

A contribution is ready when it is:

- pattern-first,
- internally consistent,
- normalized enough to avoid duplicate concepts,
- explicit about governance and evaluation,
- placed in the right directory,
- compatible with future controlled vocabularies and browse views.
