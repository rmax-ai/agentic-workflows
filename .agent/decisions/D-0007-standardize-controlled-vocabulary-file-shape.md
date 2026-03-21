# D-0007 — Standardize controlled vocabulary file shape

- Status: accepted
- Decision: Represent each controlled vocabulary as a versioned YAML document with top-level metadata (`version`, `vocabulary`, `title`, `summary`, `source_fields`, `usage_notes`) plus a `terms` list whose entries use stable ids and concise author guidance.
- Rationale: Vocabulary files will be read by both humans and future agents, so a consistent document shape makes them easier to browse, validate, and reference from pattern entries and derived views without inventing a new format for each concept class.
