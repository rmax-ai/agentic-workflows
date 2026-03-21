# D-0013 — Keep current-plan as a rolling control document

- Status: accepted
- Decision: Keep `.agent/current-plan.md` limited to the active bounded batch, current phase signals, a short ordered task list, and only the most recent checkpoints. Archive superseded execution detail in `.agent/iterations/<year>/<timestamp>.md` instead of carrying it forward in the current plan.
- Rationale: The current plan is read at the start of substantive work and must stay fast to scan. Detailed iteration history already has a dedicated sharded archive, so duplicating it in the current plan increases staleness risk and makes active guidance harder to find.
