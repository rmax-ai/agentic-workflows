# D-0003 — Commit execution memory as durable repository state

- Status: accepted
- Decision: Treat `.agent/mission.md`, `.agent/backlog.yaml`, `.agent/iterations/`, `.agent/decisions.md`, `.agent/decisions/`, `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and `.agent/glossary.md` as committed working memory rather than temporary notes.
- Rationale: Future iterations need a stable, machine-readable source of truth for sequencing, status, terminology, and durable repository decisions.