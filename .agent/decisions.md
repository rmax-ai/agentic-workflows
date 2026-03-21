# Decisions

## D-0001 — Keep the ontology pattern-first

- **Status:** accepted
- **Decision:** Organize future ontology assets around reusable workflow patterns first, domains second, and concrete implementations or examples third.
- **Rationale:** This matches the repository mission in `README.md` and avoids duplicating structurally similar workflows across industries.

## D-0002 — Enforce strict phase ordering

- **Status:** accepted
- **Decision:** Do not author vocabularies, views, pattern entries, or instances before the foundational docs and canonical schema exist.
- **Rationale:** Early scaffolding decisions must stabilize names and fields before higher-volume authoring begins.

## D-0003 — Commit execution memory as durable repository state

- **Status:** accepted
- **Decision:** Treat `.agent/mission.md`, `.agent/backlog.yaml`, `.agent/iterations/`, `.agent/decisions.md`, `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and `.agent/glossary.md` as committed working memory rather than temporary notes.
- **Rationale:** Future iterations need a stable, machine-readable source of truth for sequencing, status, and terminology.

## D-0004 — Start coverage tracking before content authoring

- **Status:** accepted
- **Decision:** Define the coverage matrix now, even though every coverage cell is currently `none`.
- **Rationale:** The matrix should guide what gets added next instead of being reconstructed after patterns accumulate.

## D-0005 — Establish a glossary during bootstrap

- **Status:** accepted
- **Decision:** Create `.agent/glossary.md` in Phase 0 to anchor repository-specific meanings for pattern, domain, instance, vocabulary, and view.
- **Rationale:** Controlled terminology reduces drift once schema and vocabulary work begins.

## D-0006 — Shard iteration history into dated files

- **Status:** accepted
- **Decision:** Store iteration history in `.agent/iterations/<year>/<timestamp>.md` rather than appending indefinitely to a single `.agent/iteration-log.md` file.
- **Rationale:** Iteration history grows without bound, while plan, status, and decisions should stay concise. Per-iteration files keep the root `.agent/` directory readable, make history easier to navigate by date, and reduce edit contention on one long-lived file.

## D-0007 — Standardize controlled vocabulary file shape

- **Status:** accepted
- **Decision:** Represent each controlled vocabulary as a versioned YAML document with top-level metadata (`version`, `vocabulary`, `title`, `summary`, `source_fields`, `usage_notes`) plus a `terms` list whose entries use stable ids and concise author guidance.
- **Rationale:** Vocabulary files will be read by both humans and future agents, so a consistent document shape makes them easier to browse, validate, and reference from pattern entries and derived views without inventing a new format for each concept class.

## D-0008 — Standardize helper scripting on Python via uv

- **Status:** accepted
- **Decision:** Use `uv` with Python 3.14 for repository helper scripts, keep shell scripts as thin orchestration wrappers, and move reusable parsing or validation logic into checked-in Python files.
- **Rationale:** Recent agent runs relied on ad hoc Ruby YAML parsing that was not declared as repository tooling. A uv-managed Python path makes helper logic explicit, reproducible, and easier to extend without turning shell entrypoints into opaque maintenance scripts.

## D-0009 — Keep browse views derived and reference-oriented

- **Status:** accepted
- **Decision:** Model `data/views/` as derived browse artifacts that reference stable family and vocabulary ids, leaving canonical pattern payloads in `data/patterns/` rather than duplicating them into views.
- **Rationale:** The repository's organizing spine is pattern-first, so alternate browse paths should help navigation without becoming a second source of truth. Reference-oriented views stay regenerable as patterns accumulate and make it easier to keep domain, architecture, autonomy, and risk indexes consistent with the canonical pattern files.

## D-0010 — Map transform-process to structured representation transformation

- **Status:** accepted
- **Decision:** Use `structured-representation-transformation` as the controlled `problem_structure` term for the `transform-process` family and its first canonical seed pattern.
- **Rationale:** The family needed a direct vocabulary mapping to close the last empty top-level pattern gap, but the term also had to preserve the family boundary. Framing the structure around representation change keeps transformation-first workflows distinct from evidence synthesis, verification, or operational execution while remaining broad enough for future normalization, enrichment, and batch reshaping patterns.

## D-0011 — Publish through a derived MkDocs site

- **Status:** accepted
- **Decision:** Publish the repository through a derived MkDocs site that generates presentation-oriented Markdown into `build/site-docs` from the canonical Markdown, YAML, and schema sources, then renders static HTML into `build/site`.
- **Rationale:** This keeps Markdown and YAML as the only authoring surfaces, preserves the repository's pattern-first ontology and source tree, stays aligned with the existing Python and `uv` helper-tooling baseline, and avoids creating a second source of truth for website content.

## D-0012 — Deploy the derived site with GitHub Pages actions

- **Status:** accepted
- **Decision:** Deploy the generated MkDocs site through a GitHub Actions workflow that runs the repository validation and site-generation pipeline on `main`, uploads `build/site` as a Pages artifact, and publishes through GitHub Pages.
- **Rationale:** This keeps deployment automation derived from the same canonical build path used locally, avoids committing generated HTML, and makes publication reproducible without adding a second hosting-specific authoring flow.

## D-0013 — Keep current-plan as a rolling control document

- **Status:** accepted
- **Decision:** Keep `.agent/current-plan.md` limited to the active bounded batch, current phase signals, a short ordered task list, and only the most recent checkpoints. Archive superseded execution detail in `.agent/iterations/<year>/<timestamp>.md` instead of carrying it forward in the current plan.
- **Rationale:** The current plan is read at the start of substantive work and must stay fast to scan. Detailed iteration history already has a dedicated sharded archive, so duplicating it in the current plan increases staleness risk and makes active guidance harder to find.
