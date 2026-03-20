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
