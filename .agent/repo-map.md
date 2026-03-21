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
- `instances/compliance/pharmacovigilance-safety-signal-alert-triage.md` — grounded compliance monitoring case for de-duplicating and prioritizing drug-safety signals into human review queues with reporting-clock context.
- `instances/operations/cold-chain-temperature-excursion-alert-triage.md` — grounded operations monitoring case for turning noisy refrigeration telemetry into explainable excursion-response queues without auto-executing downstream interventions.
- `instances/operations/cross-functional-maintenance-review-scheduling.md` — grounded operations scheduling case for bounded-delegation coordination around maintenance review timing.
- `instances/compliance/cross-border-deal-exception-review.md` — grounded compliance review case for governed recommendation support on cross-border commercial exceptions.
- `instances/compliance/sanctions-alert-closure-regulator-response-copilot-loop.md` — grounded compliance collaboration case for mixed-initiative regulator response drafting around a closed sanctions alert, with explicit policy citation and human-owned conclusions.
- `instances/compliance/pharmacovigilance-follow-up-packet-to-safety-case-record-handoff.md` — grounded compliance transform case for turning regulated drug-safety follow-up packets into reviewable ICSR staging records with provenance and exception routing.
- `instances/compliance/vendor-data-transfer-safeguard-obligation-synthesis-for-cross-border-review.md` — grounded compliance synthesis case for assembling executed transfer terms, regulator guidance, vendor disclosures, and internal privacy-review artifacts into a cited obligations brief before cross-border vendor review decisions.
- `instances/support/deprovisioned-contractor-access-escalation-copilot-loop.md` — grounded support escalation case for mixed-initiative diagnosis, customer messaging, and explicit engineering/security handoff ownership.
- `instances/support/customer-escalation-bridge-scheduling.md` — grounded support scheduling case for same-day customer escalation bridge coordination across support, engineering, customer success, and incident leadership.
- `instances/support/enterprise-support-obligation-synthesis-for-severity-one-review.md` — grounded support synthesis case for assembling cited premium-support obligations and entitlement evidence before customer-facing Sev1 commitments or concession discussions.
- `instances/hr/approved-payroll-status-change-submission.md` — grounded HR execution case for approval-gated payroll status changes in a browser-only portal.
- `instances/hr/interview-panel-availability-coordination.md` — grounded HR scheduling case for recruiter-led final-round interview panel coordination under timezone, fairness, and SLA constraints.
- `instances/finance/invoice-packet-to-payables-record-handoff.md` — grounded finance transformation case for converting heterogeneous invoice packets into ERP-ready payable records with provenance and exception routing.
- `instances/finance/dual-approved-vendor-bank-account-change-submission.md` — grounded finance execution case for approval-gated browser submission of a sensitive vendor remittance bank-account change.
- `instances/operations/site-inspection-packet-to-corrective-maintenance-work-order-handoff.md` — grounded operations transform case for turning facilities inspection packets into CMMS-ready corrective-maintenance staging records with traceability and exception routing.
- `instances/operations/field-service-dispatch-queue-reprioritization.md` — grounded operations optimization case for storm-affected field-service dispatch reprioritization under safety, fairness, and rollback guardrails.
- `instances/operations/approved-emergency-maintenance-vendor-portal-dispatch-submission.md` — grounded operations execution case for approval-gated browser submission of an emergency contractor mobilization and site-access request under safety, spend, and incident-command controls.
- `instances/support/post-outage-enterprise-ticket-queue-reprioritization.md` — grounded support optimization case for bounded queue retuning after an outage using reopen feedback, SLA pressure, and fairness guardrails.
- `instances/support/approved-break-glass-admin-access-restoration-submission.md` — grounded support execution case for approval-gated browser submission of a high-impact tenant admin access restoration under incident, security, and customer-account controls.
- `instances/finance/multi-year-renewal-pricing-and-payment-structure-recommendation.md` — grounded finance recommendation case for governed renewal pricing and payment-structure review under margin, credit, and accounting constraints.
- `instances/finance/treasury-cash-position-discrepancy-investigation.md` — grounded finance investigation case for reconciling treasury, bank, and ERP evidence into a close-critical root-cause narrative.
- `instances/finance/debt-covenant-obligation-synthesis-for-quarter-close-review.md` — grounded finance synthesis case for assembling binding debt-agreement obligations, waivers, and close support into a cited quarter-close briefing before disclosure or lender certification work begins.
- `instances/compliance/beneficial-ownership-registry-update-submission.md` — grounded compliance execution case for approval-gated browser submission of a regulated beneficial-ownership filing.
- `instances/compliance/regulatory-consumer-complaint-response-queue-reprioritization.md` — grounded compliance optimization case for statutory complaint-review backlog reprioritization under deadline, fairness, supervisory-review, and rollback guardrails.
- `instances/compliance/sanctions-screening-gap-root-cause-investigation.md` — grounded compliance investigation case for reconstructing why governed sanctions-review controls were bypassed during a high-risk payment window.
- `instances/operations/conveyor-safety-bulletin-synthesis-for-network-readiness-review.md` — grounded operations synthesis case for assembling OEM bulletins, inspection records, waivers, and asset context into a cited readiness brief before maintenance planning or site action.

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
