# D-0009 — Keep browse views derived and reference-oriented

- Status: accepted
- Decision: Model `data/views/` as derived browse artifacts that reference stable family and vocabulary ids, leaving canonical pattern payloads in `data/patterns/` rather than duplicating them into views.
- Rationale: The repository's organizing spine is pattern-first, so alternate browse paths should help navigation without becoming a second source of truth. Reference-oriented views stay regenerable as patterns accumulate and make it easier to keep domain, architecture, autonomy, and risk indexes consistent with the canonical pattern files.