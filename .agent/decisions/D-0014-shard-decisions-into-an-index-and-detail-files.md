# D-0014 — Shard decisions into an index and detail files

- Status: accepted
- Decision: Keep `.agent/decisions.md` as a concise decision index with one-line `D-code — title` summaries, and store detailed decision records under `.agent/decisions/D-code-slug.md`.
- Rationale: Decisions are part of the read-first set for substantive work, so the index should stay fast to scan. Sharding the details preserves stable decision IDs and full rationale while reducing startup reading overhead and making individual decision edits smaller and less conflict-prone.