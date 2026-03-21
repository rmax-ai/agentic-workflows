# D-0006 — Shard iteration history into dated files

- Status: accepted
- Decision: Store iteration history in `.agent/iterations/<year>/<timestamp>.md` rather than appending indefinitely to a single `.agent/iteration-log.md` file.
- Rationale: Iteration history grows without bound, while plan, status, and decisions should stay concise. Per-iteration files keep the root `.agent/` directory readable, make history easier to navigate by date, and reduce edit contention on one long-lived file.