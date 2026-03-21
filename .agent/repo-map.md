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
- `data/patterns/gather-retrieve-synthesize/approval-packet-generation.yaml` — canonical gather/synthesize pattern for governed approval-packet assembly that ends at human-reviewed handoff, with explicit provenance, exception visibility, and multi-agent evidence assembly.
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
- `instances/research/approved-human-subjects-ethics-amendment-portal-submission.md` — grounded research execution case for approval-gated browser submission of a human-subjects ethics amendment with protocol-version checks, masked evidence capture, and explicit human takeover on portal or governance ambiguity.
- `instances/research/benchmark-study-artifact-packet-to-research-review-intake-record-handoff.md` — grounded research transform case for turning heterogeneous benchmark-study artifacts into a structured pre-publication review intake record with provenance, uncertainty capture, and exception routing.
- `instances/research/benchmark-study-publication-go-no-go-recommendation.md` — grounded research recommendation case for ranking, narrowing, or escalating publication of a benchmark study against reproducibility, licensing, privacy, and reputational-risk thresholds before any external claim is committed.
- `instances/research/benchmark-study-publication-readiness-review-scheduling.md` — grounded research scheduling case for bounded-delegation coordination of a benchmark-study publication-readiness review inside an embargoed abstract-submission window.
- `instances/research/benchmark-study-disclosure-risk-alert-triage.md` — grounded research monitoring case for collapsing draft-sharing, embargo, reproducibility, and dataset-rights signals into an explainable urgent-review queue before benchmark disclosures drift outside approved boundaries.
- `instances/research/embargoed-benchmark-replication-review-queue-reprioritization.md` — grounded research optimization case for feedback-driven reprioritization of a benchmark replication review backlog under fairness, embargo, reviewer-capacity, and rollback guardrails.
- `instances/research/cross-lab-benchmark-replication-discrepancy-investigation.md` — grounded research investigation case for reconciling experiment lineage, dataset drift, evaluation-harness changes, and serving evidence into a defensible explanation of benchmark divergence before any rerun or claim decision.
- `instances/engineering/payments-api-latency-incident-investigation.md` — grounded engineering incident case for reconciled telemetry and root-cause analysis.
- `instances/engineering/service-mesh-migration-readiness-evidence-synthesis-for-architecture-review.md` — grounded engineering synthesis case for assembling cited architecture, reliability, rollback, and security evidence before service-mesh migration approval.
- `instances/engineering/deprecated-message-broker-client-migration-exception-copilot-loop.md` — grounded engineering collaboration case for mixed-initiative architecture-exception packet drafting around deprecation risk, mitigation commitments, and explicit human approval boundaries.
- `instances/engineering/production-release-regression-alert-triage.md` — grounded engineering monitoring case for collapsing release-linked detector noise into an explainable urgent-review queue without auto-triggering rollback or incident declaration.
- `instances/engineering/release-candidate-evidence-packet-to-deployment-review-staging-record-handoff.md` — grounded engineering transform case for turning heterogeneous release-readiness evidence into a structured deployment-review staging record with provenance, schema fidelity, and exception routing before any approval or rollout decision.
- `instances/engineering/cross-team-release-readiness-review-scheduling.md` — grounded engineering scheduling case for bounded-delegation coordination of a pre-cutover release-readiness review across required technical reviewers and release-policy windows.
- `instances/engineering/approved-production-change-freeze-exception-portal-submission.md` — grounded engineering execution case for approval-gated browser submission of a production change-freeze exception with rollback evidence, freeze-policy checks, and explicit safe halt behavior before authorizing a blackout-period production path.
- `instances/engineering/managed-database-major-version-upgrade-exception-recommendation.md` — grounded engineering recommendation case for ranking, narrowing, or escalating an accelerated managed-database major-version upgrade exception before seasonal freeze commitments are made.
- `instances/engineering/ci-pipeline-failure-review-queue-reprioritization.md` — grounded engineering optimization case for bounded reprioritization of a CI failure review backlog under release-pressure, fairness, blast-radius, security, and rollback guardrails.
- `instances/finance/suspicious-wire-transfer-alert-triage.md` — grounded finance triage case for governed alert prioritization and escalation.
- `instances/compliance/pharmacovigilance-safety-signal-alert-triage.md` — grounded compliance monitoring case for de-duplicating and prioritizing drug-safety signals into human review queues with reporting-clock context.
- `instances/operations/cold-chain-temperature-excursion-alert-triage.md` — grounded operations monitoring case for turning noisy refrigeration telemetry into explainable excursion-response queues without auto-executing downstream interventions.
- `instances/operations/cross-functional-maintenance-review-scheduling.md` — grounded operations scheduling case for bounded-delegation coordination around maintenance review timing.
- `instances/operations/multi-site-service-package-feasibility-recommendation.md` — grounded operations recommendation case for ranking, narrowing, or escalating a multi-site service rollout package against delivery-capacity, subcontractor-spend, inventory, and SLA constraints before customer commitment.
- `instances/compliance/cross-border-deal-exception-review.md` — grounded compliance review case for governed recommendation support on cross-border commercial exceptions.
- `instances/compliance/sanctions-alert-closure-regulator-response-copilot-loop.md` — grounded compliance collaboration case for mixed-initiative regulator response drafting around a closed sanctions alert, with explicit policy citation and human-owned conclusions.
- `instances/compliance/pharmacovigilance-follow-up-packet-to-safety-case-record-handoff.md` — grounded compliance transform case for turning regulated drug-safety follow-up packets into reviewable ICSR staging records with provenance and exception routing.
- `instances/compliance/vendor-data-transfer-safeguard-obligation-synthesis-for-cross-border-review.md` — grounded compliance synthesis case for assembling executed transfer terms, regulator guidance, vendor disclosures, and internal privacy-review artifacts into a cited obligations brief before cross-border vendor review decisions.
- `instances/compliance/control-remediation-sign-off-review-scheduling.md` — grounded compliance scheduling case for bounded-delegation coordination of a regulator-visible remediation sign-off review across control, audit, and technology-risk stakeholders before attestation cutoff.
- `instances/support/deprovisioned-contractor-access-escalation-copilot-loop.md` — grounded support escalation case for mixed-initiative diagnosis, customer messaging, and explicit engineering/security handoff ownership.
- `instances/support/enterprise-admin-entitlement-drift-root-cause-investigation.md` — grounded support investigation case for reconciling entitlement, identity, configuration, and responder evidence into a defensible explanation before remediation or customer-facing root-cause commitments.
- `instances/support/severity-one-service-credit-and-recovery-package-recommendation.md` — grounded support recommendation case for ranking, narrowing, or escalating a service-credit and recovery-package path against entitlement rules, concession thresholds, precedent risk, and stakeholder approvals before any customer-facing commitment.
- `instances/support/suspected-account-takeover-support-alert-triage.md` — grounded support monitoring case for correlating noisy takeover signals into an explainable urgent-review queue without auto-triggering customer or security interventions.
- `instances/support/customer-escalation-bridge-scheduling.md` — grounded support scheduling case for same-day customer escalation bridge coordination across support, engineering, customer success, and incident leadership.
- `instances/support/enterprise-support-obligation-synthesis-for-severity-one-review.md` — grounded support synthesis case for assembling cited premium-support obligations and entitlement evidence before customer-facing Sev1 commitments or concession discussions.
- `instances/support/enterprise-outage-evidence-packet-to-support-escalation-record-handoff.md` — grounded support transform case for turning a multi-channel outage packet into a structured severity-escalation staging record with provenance, privacy flags, and exception routing before any live bridge launch or engineering page.
- `instances/hr/approved-payroll-status-change-submission.md` — grounded HR execution case for approval-gated payroll status changes in a browser-only portal.
- `instances/hr/interview-panel-availability-coordination.md` — grounded HR scheduling case for recruiter-led final-round interview panel coordination under timezone, fairness, and SLA constraints.
- `instances/hr/pay-transparency-posting-obligation-synthesis-for-requisition-launch-review.md` — grounded HR synthesis case for assembling cited multi-jurisdiction pay-transparency posting obligations before requisition launch, compensation exceptions, or template updates.
- `instances/hr/international-relocation-and-sign-on-package-recommendation.md` — grounded HR recommendation case for ranking, narrowing, or escalating an executive-hire relocation and sign-on exception package against compensation-band, mobility-policy, internal-equity, and approval constraints before any offer commitment.
- `instances/hr/workplace-accommodation-exception-memo-copilot-loop.md` — grounded HR collaboration case for mixed-initiative accommodation exception memo drafting with privacy-aware evidence handling, explicit human approval, and escalation to legal or occupational-health review when the record is not yet supportable.
- `instances/hr/medical-leave-certification-packet-to-leave-case-record-handoff.md` — grounded HR transform case for turning a sensitive multi-document leave intake packet into a structured leave-case staging record with provenance, privacy tags, and exception routing before any adjudication or payroll action.
- `instances/hr/protected-leave-case-review-queue-reprioritization.md` — grounded HR optimization case for bounded protected-leave backlog reprioritization under privacy, fairness, workload-balance, service-level, and rollback guardrails.
- `instances/hr/protected-leave-return-to-work-status-drift-root-cause-investigation.md` — grounded HR investigation case for reconciling leave-case, HRIS, payroll, timekeeping, benefits, and document evidence into a defensible explanation before any corrective pay, leave, or employee-communication action.
- `instances/hr/work-authorization-expiry-risk-alert-triage.md` — grounded HR monitoring case for collapsing noisy work-authorization expiry and reverification signals into an explainable human-review queue without automating outreach, filing, or employment-status action.
- `instances/finance/invoice-packet-to-payables-record-handoff.md` — grounded finance transformation case for converting heterogeneous invoice packets into ERP-ready payable records with provenance and exception routing.
- `instances/finance/dual-approved-vendor-bank-account-change-submission.md` — grounded finance execution case for approval-gated browser submission of a sensitive vendor remittance bank-account change.
- `instances/operations/site-inspection-packet-to-corrective-maintenance-work-order-handoff.md` — grounded operations transform case for turning facilities inspection packets into CMMS-ready corrective-maintenance staging records with traceability and exception routing.
- `instances/operations/field-service-dispatch-queue-reprioritization.md` — grounded operations optimization case for storm-affected field-service dispatch reprioritization under safety, fairness, and rollback guardrails.
- `instances/operations/approved-emergency-maintenance-vendor-portal-dispatch-submission.md` — grounded operations execution case for approval-gated browser submission of an emergency contractor mobilization and site-access request under safety, spend, and incident-command controls.
- `instances/operations/distribution-sorter-misroute-root-cause-investigation.md` — grounded operations investigation case for reconciling sorter controls, scanner evidence, maintenance history, and supervisor workarounds into a defensible root-cause narrative before remediation or customer commitments.
- `instances/operations/supplier-labeling-deviation-remediation-brief-copilot-loop.md` — grounded operations collaboration case for mixed-initiative supplier remediation-brief drafting around labeling deviations, evidence lineage, and explicit human approval of outbound commitments.
- `instances/support/post-outage-enterprise-ticket-queue-reprioritization.md` — grounded support optimization case for bounded queue retuning after an outage using reopen feedback, SLA pressure, and fairness guardrails.
- `instances/support/approved-break-glass-admin-access-restoration-submission.md` — grounded support execution case for approval-gated browser submission of a high-impact tenant admin access restoration under incident, security, and customer-account controls.
- `instances/finance/multi-year-renewal-pricing-and-payment-structure-recommendation.md` — grounded finance recommendation case for governed renewal pricing and payment-structure review under margin, credit, and accounting constraints.
- `instances/finance/treasury-cash-position-discrepancy-investigation.md` — grounded finance investigation case for reconciling treasury, bank, and ERP evidence into a close-critical root-cause narrative.
- `instances/finance/debt-covenant-obligation-synthesis-for-quarter-close-review.md` — grounded finance synthesis case for assembling binding debt-agreement obligations, waivers, and close support into a cited quarter-close briefing before disclosure or lender certification work begins.
- `instances/finance/quarter-close-covenant-clarification-package-copilot-loop.md` — grounded finance collaboration case for mixed-initiative lender-response drafting around covenant interpretation support, evidence lineage, and explicit human approval of all outbound commitments.
- `instances/finance/quarter-close-control-review-scheduling.md` — grounded finance scheduling case for bounded-delegation coordination of a quarter-close control review across controllership, treasury accounting, SEC reporting, internal controls, and finance systems before sign-off deadlines.
- `instances/finance/quarter-close-exception-review-queue-reprioritization.md` — grounded finance optimization case for bounded reprioritization of a quarter-close exception backlog under materiality, fairness, auditability, and rollback guardrails.
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
