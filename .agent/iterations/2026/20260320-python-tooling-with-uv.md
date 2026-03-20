# 2026-03-20 — uv-managed Python helper tooling

- Added a minimal uv-managed Python tooling baseline with `pyproject.toml` and a committed `.python-version` targeting Python 3.14.
- Added `scripts/python/validate_yaml.py` as a checked-in YAML validation helper so repository automation no longer needs ad hoc Ruby parsing snippets.
- Updated `scripts/run-agentic-workflows-loop.sh` to require `uv` and run the Python YAML validator before assembling the iteration prompt.
- Updated repository docs, operator guidance, and durable decisions to make Python-via-uv the default path for reusable helper logic.

## What changed

- `pyproject.toml`
- `.python-version`
- `scripts/python/validate_yaml.py`
- `scripts/run-agentic-workflows-loop.sh`
- `README.md`
- `docs/contribution-guide.md`
- `.gitignore`
- `.agent/prompts/operator-prompt.txt`
- `.agent/decisions.md`
- `.agent/repo-map.md`
- `.agent/current-plan.md`
- `.agent/proposals/python-tooling-with-uv.md`

## What was learned

- The Ruby YAML parsing that motivated this change was appearing in prior run logs rather than in committed repository scripts, so the right fix was to add a committed helper and reinforce the workflow through prompts and docs.
- Committing `.python-version` required an explicit exception in `.gitignore` because the repository was already ignoring that file class globally.

## Next step

Resume Phase 3 by authoring `data/views/` browse artifacts against the stabilized vocabulary layer, using the new Python helper path only when reusable repository logic is needed.
