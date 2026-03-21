# Proposal: Useful Python Helper Scripts For Repository Automation

- Status: proposed
- Date: 2026-03-20
- Scope: repository automation and helper-script roadmap
- Related areas: uv-managed Python tooling, YAML validation, browse-view generation, execution memory maintenance

## Question

Which Python helper scripts would be useful next, now that the repository has a uv-managed Python 3.14 baseline?

## Proposal Summary

Add a small set of focused Python helpers that improve repository consistency, reduce repeated shell logic, and support the ontology workflow without turning the repo into a heavy application.

The recommendation is to keep the current shell entrypoints thin and only add Python helpers where the logic is reusable, validation-heavy, or easier to maintain in Python than in shell.

## Selection Principles

Candidate scripts should meet at least one of these conditions:

1. They replace repeated ad hoc shell or interpreter snippets.
2. They validate repository invariants that are easy to break manually.
3. They derive or check structured artifacts such as views, indexes, or memory files.
4. They improve consistency across `.agent/`, `data/`, and `docs/` without becoming a second source of truth.
5. They can stay small, explicit, and standard-library-first unless YAML parsing or another clear need requires a dependency.

## Recommended Script Backlog

### 1. `scripts/python/repo_snapshot.py`

- Purpose: Generate the repository snapshot currently assembled inline in the loop shell script.
- Why it is useful: The current shell logic for gathering tree state, recent commits, and `.agent/` files is already substantial. If it grows further, Python will be easier to extend and test than a larger shell block.
- Suggested responsibilities:
- collect branch name and git status
- list top-level repository structure with ignore-aware pruning
- list committed `.agent/` files
- capture recent commits
- write the snapshot to a target file

- Priority: Medium.

Keep it in shell until snapshot logic becomes meaningfully more complex.

### 2. `scripts/python/check_agent_memory.py`

- Purpose: Validate that the core committed `.agent/` files stay internally consistent.
- Why it is useful: The repository relies on `.agent/current-plan.md`, `.agent/backlog.yaml`, `.agent/ontology-status.yaml`, `.agent/repo-map.md`, and `.agent/decisions.md` as durable memory. Those files can drift from actual repo state even when ontology work is otherwise correct.
- Suggested responsibilities:
- verify required `.agent/` files exist
- check that current phase statements match backlog and status files at a coarse level
- detect references to files that do not exist anymore
- flag implemented proposals that were never reflected in decisions or repo memory when appropriate

- Priority: High.

This directly supports the repository's memory-first workflow.

### 3. `scripts/python/validate_views.py`

- Purpose: Validate derived browse views once `data/views/` exists.
- Why it is useful: The repository intends views to be reference-oriented artifacts rather than a second source of truth. That requires checking that view ids map back to real vocabulary ids and later to real pattern ids.
- Suggested responsibilities:
- validate that referenced vocabulary ids exist
- validate that referenced pattern families are allowed
- later validate that referenced pattern ids exist
- flag orphaned or stale references in derived views

- Priority: High once Phase 3 view authoring begins.

### 4. `scripts/python/generate_views.py`

- Purpose: Generate some or all browse-view YAML files from controlled vocabularies and canonical source data.
- Why it is useful: If the repository wants view artifacts to remain derived and regenerable, a generator may eventually be preferable to manual editing.
- Suggested responsibilities:
- read controlled vocabularies
- emit scaffolded view structures
- preserve stable ordering
- optionally update only generated sections

- Priority: Medium.

Validation should come before generation. The repo should understand the desired view shape clearly before automating it.

### 5. `scripts/python/validate_patterns.py`

- Purpose: Validate canonical pattern YAML entries against the schema and vocabulary constraints once `data/patterns/` exists.
- Why it is useful: The schema already defines structural expectations, but real quality also depends on vocabulary-backed fields and cross-file referential integrity.
- Suggested responsibilities:
- run JSON Schema validation against pattern files
- check vocabulary-backed fields against approved ids
- verify links to related patterns
- report coverage-relevant metadata for later aggregation

- Priority: High once Phase 5 pattern authoring begins.

### 6. `scripts/python/coverage_report.py`

- Purpose: Generate or verify a machine-derived summary for `.agent/coverage-matrix.yaml`.
- Why it is useful: Coverage tracking is one of the repository's explicit control mechanisms. As patterns and instances accumulate, manual maintenance of coverage state will become error-prone.
- Suggested responsibilities:
- read patterns and instances
- aggregate counts by family, domain, architecture, autonomy, and risk
- compare derived counts to the tracked matrix
- optionally emit a summary report rather than rewriting the matrix directly

- Priority: Medium to high after canonical patterns exist.

### 7. `scripts/python/check_links.py`

- Purpose: Verify cross-file links in Markdown and structured data.
- Why it is useful: The repository is designed to become navigable through links between docs, patterns, views, instances, and `.agent/` memory. Broken links will accumulate as the structure grows.
- Suggested responsibilities:
- verify Markdown links to local files
- verify linked pattern ids resolve
- verify instance references point back to canonical patterns
- report stale references in docs and memory files

- Priority: Medium.

### 8. `scripts/python/bootstrap_iteration_note.py`

- Purpose: Create a timestamped iteration note scaffold under `.agent/iterations/<year>/`.
- Why it is useful: The repository has a committed iteration-memory discipline. A small helper can reduce formatting drift and ensure notes include the expected sections.
- Suggested responsibilities:
- create the dated file path
- insert standard headings
- optionally prefill changed-file summaries from git

- Priority: Low to medium.

Useful, but less important than validation and referential-integrity tooling.

## Recommended Order

The suggested implementation order is:

1. `check_agent_memory.py`
2. `validate_views.py`
3. `validate_patterns.py`
4. `coverage_report.py`
5. `repo_snapshot.py`
6. `check_links.py`
7. `generate_views.py`
8. `bootstrap_iteration_note.py`

## Why This Order

This order matches the repository's dependency model:

1. protect execution memory first
2. validate derived views before generating more structure
3. validate canonical patterns before automating coverage summaries
4. automate convenience tasks only after core invariants are enforced

## Guardrails

Any future helper script should follow these rules:

1. Do not create a second source of truth.
2. Prefer read-only validation before automated rewriting.
3. Keep file scope explicit.
4. Produce deterministic output when writing files.
5. Fail with actionable messages rather than opaque exceptions.
6. Avoid adding dependencies unless the script clearly benefits.

## Non-Recommendations

The repository should avoid these classes of Python scripts for now:

1. Large autonomous content generators for pattern files.
2. Scripts that rewrite ontology prose aggressively.
3. Automation that bypasses the explicit `.agent/` planning and decision process.
4. Heavy web or external-service integrations not required for repository maintenance.

## Decision Request

If accepted later, this proposal should guide future helper additions toward validation, referential integrity, and lightweight derivation rather than content generation for its own sake.
