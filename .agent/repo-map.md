# Repository Map

## Current committed structure

### Root files

- `README.md` — repository mission, pattern-first framing, and intended target structure.
- `.python-version` — pinned local interpreter target for uv-managed Python helper scripts.
- `pyproject.toml` — Python helper-tool metadata and dependency declarations for uv.
- `uv.lock` — locked Python helper dependencies for reproducible local execution.
- `.gitattributes` — text normalization and Linguist hints for planned YAML and Markdown content.
- `.gitignore` — ignore rules that preserve committed `.agent/` memory while excluding runtime artifacts.
- `LICENSE` — repository license.

### Current automation

- `scripts/run-agentic-workflows-loop.sh` — runs one repository iteration by assembling prompt context and invoking Copilot.
- `scripts/run-agentic-workflows-forever.sh` — optional wrapper for repeated iterations with a stop-file check.
- `scripts/python/validate_yaml.py` — uv-managed Python helper that validates repository YAML files without relying on ad hoc Ruby.

### Current execution-memory assets

- `.agent/current-plan.md` — current ordered iteration plan.
- `.agent/prompts/mega-prompt.txt` — master orchestration prompt for the repo-building loop.
- `.agent/prompts/operator-prompt.txt` — per-iteration operator instructions.
- `.agent/mission.md` — stable mission and curation rules for the repository.
- `.agent/backlog.yaml` — dependency-ordered task backlog.
- `.agent/iterations/` — one dated Markdown file per iteration, grouped by year.
- `.agent/decisions.md` — durable architectural and process decisions.
- `.agent/ontology-status.yaml` — status inventory and gap tracking.
- `.agent/coverage-matrix.yaml` — coverage grid for planned pattern/domain/architecture/risk combinations.
- `.agent/glossary.md` — repository terminology guide.

### Current foundational ontology assets

- `docs/ontology.md` — canonical explanation of ontology layers, relationships, and normalization rules.
- `docs/schema.md` — field-by-field guide to the canonical pattern schema.
- `docs/index-tree.md` — proposed pattern-first browse tree and derived view strategy.
- `docs/contribution-guide.md` — dependency-aware authoring and placement rules.
- `docs/patterns/README.md` — directory-level guide for the top-level pattern family overviews.
- `docs/patterns/*.md` — nine family overview docs that define family boundaries, neighboring links, governance concerns, and seed-pattern guidance before canonical YAML authoring.
- `schema/pattern.schema.json` — canonical JSON Schema for YAML pattern entries.

### Current controlled vocabularies

- `data/vocabularies/problem-structures.yaml` — reusable workflow problem forms for `problem_structure`.
- `data/vocabularies/domains.yaml` — approved contextual domain ids for `domain`.
- `data/vocabularies/architectures.yaml` — execution architecture ids for `execution_architecture`.
- `data/vocabularies/capabilities.yaml` — reusable capability ids for `capability_requirements`.
- `data/vocabularies/autonomy-levels.yaml` — autonomy ladder for `autonomy_profile.level`.
- `data/vocabularies/risk-levels.yaml` — governance-sensitive levels for `risk_governance.level`.

### Current navigation views

- `data/views/index-tree.yaml` — canonical family-ordered browse tree scaffold that keeps the default navigation pattern-first.
- `data/views/by-domain.yaml` — derived domain view that groups future canonical patterns by domain while preserving family order.
- `data/views/by-architecture.yaml` — derived architecture view that organizes future canonical patterns by execution style.
- `data/views/by-autonomy.yaml` — derived autonomy view that organizes future canonical patterns by discretion and control boundary.
- `data/views/by-risk.yaml` — derived risk view that organizes future canonical patterns by governance posture.

### Current canonical pattern data

- `data/patterns/gather-retrieve-synthesize/research-synthesis-with-citation-verification.yaml` — canonical gather/synthesize pattern for evidence-grounded synthesis with citation verification.
- `data/patterns/transform-process/document-to-structured-data-handoff.yaml` — canonical transform/process pattern for turning heterogeneous documents into schema-aligned structured records with provenance, lossiness, and exception-aware handoff.
- `data/patterns/investigate-reconcile-verify/incident-root-cause-analysis.yaml` — canonical investigation pattern for evidence-backed incident diagnosis and reconciled timelines.
- `data/patterns/monitor-detect-triage/risk-alert-triage.yaml` — canonical monitoring pattern for governed alert prioritization and escalation packaging.
- `data/patterns/plan-coordinate-schedule/calendar-conflict-coordination.yaml` — canonical planning and coordination pattern for low-risk multi-party scheduling under bounded delegation.
- `data/patterns/recommend-decide-escalate/deal-desk-recommendation-support.yaml` — canonical recommendation pattern for governed commercial option ranking, approval guidance, and escalation packaging.
- `data/patterns/execute-automate/browser-based-form-completion-with-approval-gates.yaml` — canonical execution pattern for sensitive browser-based submissions under explicit approval gates and exception handling.
- `data/patterns/optimize-adapt/queue-prioritization-optimization.yaml` — canonical optimization pattern for tuning queue ordering from outcome feedback under explicit service, fairness, and policy guardrails.
- `data/patterns/human-agent-collaborative-work/analyst-copilot-loop.yaml` — canonical human-agent collaboration pattern for mixed-initiative co-working around a shared artifact, explicit handoffs, and visible responsibility boundaries.

### Current grounded examples

- `instances/research/regulatory-obligation-synthesis-for-data-retention-review.md` — grounded research/compliance-adjacent instance for evidence-backed policy synthesis and citation review.
- `instances/research/model-serving-platform-benchmark-briefing-copilot-loop.md` — grounded research collaboration case for mixed-initiative benchmark preparation with traceable experiment evidence and explicit analyst sign-off.
- `instances/engineering/payments-api-latency-incident-investigation.md` — grounded engineering incident case for reconciled telemetry and root-cause analysis.
- `instances/finance/suspicious-wire-transfer-alert-triage.md` — grounded finance triage case for governed alert prioritization and escalation.
- `instances/operations/cross-functional-maintenance-review-scheduling.md` — grounded operations scheduling case for bounded-delegation coordination around maintenance review timing.
- `instances/compliance/cross-border-deal-exception-review.md` — grounded compliance review case for governed recommendation support on cross-border commercial exceptions.
- `instances/support/deprovisioned-contractor-access-escalation-copilot-loop.md` — grounded support escalation case for mixed-initiative diagnosis, customer messaging, and explicit engineering/security handoff ownership.
- `instances/hr/approved-payroll-status-change-submission.md` — grounded HR execution case for approval-gated payroll status changes in a browser-only portal.
- `instances/finance/invoice-packet-to-payables-record-handoff.md` — grounded finance transformation case for converting heterogeneous invoice packets into ERP-ready payable records with provenance and exception routing.
- `instances/support/post-outage-enterprise-ticket-queue-reprioritization.md` — grounded support optimization case for bounded queue retuning after an outage using reopen feedback, SLA pressure, and fairness guardrails.
- `instances/finance/multi-year-renewal-pricing-and-payment-structure-recommendation.md` — grounded finance recommendation case for governed renewal pricing and payment-structure review under margin, credit, and accounting constraints.
- `instances/compliance/beneficial-ownership-registry-update-submission.md` — grounded compliance execution case for approval-gated browser submission of a regulated beneficial-ownership filing.

## Not yet present but planned

### Additional documentation

- `docs/domains/`
- `docs/architectures/`

## Reading order for future contributors and agents

1. `README.md`
2. `.agent/current-plan.md`
3. `.agent/mission.md`
4. `.agent/backlog.yaml`
5. `.agent/ontology-status.yaml`
6. `.agent/coverage-matrix.yaml`
7. `.agent/decisions.md`
8. `data/vocabularies/`
9. `docs/patterns/`
10. `schema/pattern.schema.json`
11. `instances/`
