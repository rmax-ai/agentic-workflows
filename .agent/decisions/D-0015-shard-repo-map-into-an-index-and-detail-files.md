# D-0015 — Shard repo-map into an index and detail files

- Status: accepted
- Decision: Keep `.agent/repo-map.md` as a concise read-first repository map index, and store bulky structural detail under a small set of clearly named Markdown files in `.agent/repo-map/`.
- Rationale: Repo-map is part of the read-first execution-memory set, so it should stay fast to scan in the same way the decision index does. Sharding preserves structural orientation while reducing startup reading cost, keeping edits smaller, and letting agents open only the structural detail that matches the task.
