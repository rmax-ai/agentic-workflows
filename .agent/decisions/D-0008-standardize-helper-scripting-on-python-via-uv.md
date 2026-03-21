# D-0008 — Standardize helper scripting on Python via uv

- Status: accepted
- Decision: Use `uv` with Python 3.14 for repository helper scripts, keep shell scripts as thin orchestration wrappers, and move reusable parsing or validation logic into checked-in Python files.
- Rationale: Recent agent runs relied on ad hoc Ruby YAML parsing that was not declared as repository tooling. A uv-managed Python path makes helper logic explicit, reproducible, and easier to extend without turning shell entrypoints into opaque maintenance scripts.