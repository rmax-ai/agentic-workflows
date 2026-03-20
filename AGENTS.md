# AGENTS.md

Guidance for coding agents working in this repository.

## Purpose

This repository is a pattern-first knowledge base for agentic workflows.

The goal is to build a coherent ontology of agentic work where:

- patterns are the primary organizing unit
- domains provide context, not the top-level structure
- implementations and grounded examples come after the ontology is stable

Use YAML for canonical structured artifacts and Markdown for documentation, examples, and repository working memory.

## Read First

Before making substantive changes, read these files in order:

1. `README.md`
2. `.agent/current-plan.md`
3. `.agent/mission.md`
4. `.agent/backlog.yaml`
5. `.agent/ontology-status.yaml`
6. `.agent/coverage-matrix.yaml`
7. `.agent/decisions.md`
8. `.agent/repo-map.md`

If your work touches terminology, also read `.agent/glossary.md`.

## Repository Rules

1. Keep the ontology pattern-first.
2. Work in dependency order: execution memory -> foundations/schema -> vocabularies -> views -> patterns -> instances.
3. Do not add shallow pattern files before schema and controlled vocabularies are stable.
4. Record durable ontology decisions in `.agent/decisions.md` before letting them spread across multiple files.
5. Prefer modest, dependency-aware batches over large uncontrolled generation.
6. Treat governance, autonomy boundaries, reversibility, failure cost, privacy, and auditability as first-class concerns.

## Source Of Truth By File Type

- `schema/` holds canonical structural definitions.
- `data/vocabularies/` holds controlled vocabularies.
- `data/views/` holds browse and navigation structures.
- `data/patterns/` holds canonical workflow-pattern entries.
- `instances/` holds grounded Markdown examples linked back to canonical patterns.
- `docs/` holds human-readable documentation.
- `.agent/` holds durable execution memory for the repository.

## Working In .agent

The `.agent/` directory is committed repository state, not disposable scratch space, except for ignored runtime artifacts.

Maintain these files when your work changes repository state:

- `.agent/current-plan.md` for the current next steps
- `.agent/decisions.md` for durable decisions
- `.agent/iteration-log.md` for a concise record of what changed
- `.agent/ontology-status.yaml` for current phase and gaps
- `.agent/coverage-matrix.yaml` for coverage progress
- `.agent/repo-map.md` when the repository structure changes materially
- `.agent/glossary.md` when repository terminology changes

Do not commit transient runtime output from `.agent/runs/`, `.agent/tmp/`, lock files, sockets, or `.agent/stop.txt`.

## Expected Change Workflow

For substantive work:

1. Read the required context files.
2. Identify the current phase and the highest-leverage next dependency-safe step.
3. Update `.agent/current-plan.md` before major edits if the plan is outdated.
4. Make a focused batch of changes.
5. Update the relevant `.agent/` memory files to reflect reality.
6. Verify consistency across docs, schema, vocabularies, and status tracking.

## Commit Guidance

When running inside the repository's autonomous loop, follow the loop contract in `.agent/prompts/operator-prompt.txt` and keep subagent work scoped and commit-sized.

When working interactively with a user, do not create commits unless the user explicitly asks for them.

## What To Avoid

- Do not reorganize the repo around industries or implementation stacks.
- Do not create many weak pattern entries to simulate progress.
- Do not let naming drift across schema, vocabularies, patterns, and docs.
- Do not treat `.agent/` files as optional notes.
- Do not add generated artifacts or runtime logs to version control.

## Success Criteria

Your work is aligned with this repository when it leaves the ontology:

- more coherent
- more navigable
- better grounded in controlled terminology
- more explicit about governance and autonomy constraints
- easier for the next agent iteration to continue safely
