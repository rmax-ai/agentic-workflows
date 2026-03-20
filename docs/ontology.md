# Ontology model

This repository models **agentic workflows as reusable patterns**. The ontology is deliberately organized in dependency order:

1. **Patterns** describe recurring workflow structure.
2. **Domains** contextualize where a pattern appears.
3. **Instances and implementations** ground a pattern in a specific environment.

That ordering is not cosmetic. It prevents the repository from turning into a grab bag of industry examples that duplicate the same underlying workflow.

## Ontology layers

### 1. Pattern layer (canonical)
The pattern layer is the repository's primary spine. A pattern captures the reusable structure of work that benefits from agentic behavior, independent of any single industry or tool stack.

A canonical pattern should answer:

- What class of problem is being solved?
- What workflow goal defines success?
- What inputs are transformed into what outputs?
- What capabilities, execution architecture, autonomy, and governance constraints shape the work?
- Why is the workflow meaningfully agentic rather than simple automation?

This layer is represented by canonical YAML entries validated by `schema/pattern.schema.json`.

### 2. Vocabulary layer (controlled terms)
Controlled vocabularies stabilize high-reuse fields such as pattern family, problem structure, domains, architectures, capability names, autonomy levels, and risk levels.

In Phase 1, the schema permits pragmatic string values so authoring can start cleanly. Later vocabulary files will narrow those fields to approved identifiers without changing the overall document shape.

### 3. View layer (browse and navigation)
Views are derived structures for browsing the ontology, such as pattern-first trees and alternate indexes by domain, architecture, autonomy, or risk.

Views should never redefine the canonical meaning of a pattern. They reorganize canonical pattern data for discovery.

### 4. Instance layer (grounded examples)
Instances are concrete scenarios that link one or more canonical patterns to a real environment, workflow, or target system.

Instances are intentionally downstream from patterns. They demonstrate the ontology; they do not define it.

## Core entities

### Pattern
A reusable unit of workflow structure.

Required identity:

- `id`: stable canonical identifier
- `slug`: human-readable path-safe identifier
- `name`: display name
- `summary`: short explanation of the pattern

Structural fields usually include:

- `pattern_family`
- `problem_structure`
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

Relational fields usually include:

- `domain`
- `related_patterns`
- `example_domains`
- `tags`

### Domain
A contextual label describing where a pattern appears, such as engineering, finance, compliance, or operations.

Domains are **not** the primary organizing unit. A pattern may apply to multiple domains, and a domain may reuse many patterns.

### Pattern family
A broad organizing bucket for structurally related patterns, such as gather/retrieve/synthesize or monitor/detect/triage. Pattern families are useful for browsing and coverage tracking, but they are more general than individual patterns.

### Instance
A concrete scenario or example that demonstrates a pattern in a specific context.

An instance should reference a canonical pattern rather than restating pattern logic from scratch.

### View
A browse-oriented artifact that reorganizes canonical data for discovery. A view may group patterns by family, domain, architecture, autonomy profile, or risk, but it should not introduce new semantics.

## Relationship model

The ontology uses a small number of intentionally simple relationships:

- **pattern -> belongs to -> pattern family**
- **pattern -> exhibits -> problem structure**
- **pattern -> appears in -> domain(s)**
- **pattern -> requires -> capability/capabilities**
- **pattern -> is commonly implemented with -> execution architecture(s)**
- **pattern -> operates under -> autonomy profile**
- **pattern -> is governed by -> risk and governance profile**
- **pattern -> relates to -> other patterns**
- **instance -> instantiates -> pattern**
- **view -> indexes -> patterns through a chosen perspective**

Key cardinality assumptions:

- A pattern belongs to exactly one primary `pattern_family`.
- A pattern has exactly one primary `problem_structure`.
- A pattern may map to one or many `domain` values.
- A pattern may require many capabilities and may support multiple architectures.
- An instance may reference one or many patterns, but one primary pattern should usually lead.

## Normalization rules

Normalization exists to keep the ontology stable as content volume grows.

### Stable identifiers first
- `id` is the canonical durable key.
- `slug` is the path-safe, human-readable label.
- Names may evolve for clarity; identifiers should not drift casually.

### Separate reusable structure from context
- Put reusable workflow logic in the pattern.
- Put sector-specific framing in domain references and example domains.
- Put concrete operating details in instances or implementation notes.

### Prefer references over duplicated prose
When a field will later be backed by a controlled vocabulary, author it in a way that can cleanly become a vocabulary reference. For example, prefer a stable lower-kebab-case token or an object with an `id` over long ad hoc phrases.

### Keep canonical and derived artifacts distinct
- Canonical pattern data belongs in pattern YAML.
- Browse trees, cross-indexes, and summaries belong in views or documentation.
- Documentation explains the model but should not become an alternate source of record for pattern data.

### Model the primary thing once
If two entries differ only by domain framing, they should probably be one pattern with multiple domain associations, not two separate patterns.

## How patterns relate to domains and instances

### Patterns to domains
Patterns are reusable across domains. Domain fields answer **where a pattern commonly appears**, not **what the pattern fundamentally is**.

For example, a reconcile-and-verify workflow may appear in finance, compliance, and operations. That should remain one canonical pattern unless the workflow structure truly changes.

### Patterns to instances
Instances are downstream exemplars. They should:

- reference a canonical pattern id or slug,
- add concrete systems, actors, constraints, and evaluation context,
- preserve the canonical pattern semantics rather than redefining them.

### Patterns to implementations
Implementation notes may mention typical tooling, orchestration approaches, or integration styles, but implementation detail is tertiary. A pattern should remain understandable even when specific model providers, frameworks, or APIs change.

## Pattern-first curation test

Before adding or editing ontology content, ask:

1. Is this a reusable workflow pattern or only a domain example?
2. If the domain changes, does the structure still hold?
3. Is the agentic value coming from planning, adaptation, tool use, verification, coordination, or governance-aware execution?
4. Should this information live in the canonical pattern, a controlled vocabulary, a browse view, or a grounded instance?

If those answers are unclear, the content is probably not yet normalized enough for canonical inclusion.
