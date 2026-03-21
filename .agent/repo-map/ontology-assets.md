# Ontology Assets

## Foundational docs and schema

- `docs/ontology.md` — canonical explanation of ontology layers, relationships, and normalization rules.
- `docs/schema.md` — field-by-field guide to the canonical pattern schema.
- `docs/index-tree.md` — pattern-first browse tree and derived-view strategy.
- `docs/contribution-guide.md` — dependency-aware authoring and placement rules.
- `docs/patterns/README.md` and `docs/patterns/*.md` — nine family overview docs that define family boundaries, neighboring links, governance concerns, and seed-pattern guidance before canonical YAML authoring.
- `schema/pattern.schema.json` — canonical JSON Schema for YAML pattern entries.

## Controlled vocabularies

- `data/vocabularies/problem-structures.yaml` — reusable workflow problem forms for `problem_structure`.
- `data/vocabularies/domains.yaml` — approved contextual domain ids for `domain`.
- `data/vocabularies/architectures.yaml` — execution architecture ids for `execution_architecture`.
- `data/vocabularies/capabilities.yaml` — reusable capability ids for `capability_requirements`.
- `data/vocabularies/autonomy-levels.yaml` — autonomy ladder for `autonomy_profile.level`.
- `data/vocabularies/risk-levels.yaml` — governance-sensitive levels for `risk_governance.level`.

## Derived navigation views

- `data/views/index-tree.yaml` — canonical family-ordered browse tree scaffold.
- `data/views/by-domain.yaml` — derived domain view that preserves family order.
- `data/views/by-architecture.yaml` — derived architecture view.
- `data/views/by-autonomy.yaml` — derived autonomy view.
- `data/views/by-risk.yaml` — derived risk view.

## Canonical pattern storage

- `data/patterns/` stores canonical YAML entries grouped by the nine top-level families.
- Family directories currently are `gather-retrieve-synthesize/`, `transform-process/`, `investigate-reconcile-verify/`, `monitor-detect-triage/`, `plan-coordinate-schedule/`, `recommend-decide-escalate/`, `execute-automate/`, `optimize-adapt/`, and `human-agent-collaborative-work/`.
- Current family counts are tracked in `.agent/ontology-status.yaml`; use that index for counts first and open family directories only when the task needs file-level detail.
