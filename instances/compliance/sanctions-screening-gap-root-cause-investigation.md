# Sanctions screening gap root-cause investigation

## Linked pattern(s)

- `incident-root-cause-analysis`

## Domain

Compliance.

## Scenario summary

After a regulator inquiry, a financial-crime compliance team must investigate why several cross-border payments involving high-risk counterparties were not queued for manual sanctions review during a two-day window. The likely causes include a watchlist vendor update that changed name-normalization behavior, a screening-rule deployment mismatch across regions, a case-routing configuration error, or analyst-applied suppressions that propagated too broadly. The workflow reconciles alert logs, list-update history, routing decisions, and human case activity into a defensible explanation of the control gap and its contributing conditions.

## Target systems / source systems

- Sanctions-screening engine logs, rule versions, and match-explanation records
- Watchlist vendor update history, list-ingestion validation results, and name-normalization mappings
- Case-management routing logs, queue assignments, and analyst disposition history
- Payment messages, customer and counterparty reference data, and escalation notes
- Change tickets, regional release approvals, and compliance issue-management records

## Why this instance matters

This instance shows how `incident-root-cause-analysis` applies to compliance when the core need is to explain a possible control failure without collapsing the work into alert triage or policy recommendation. The investigation must reconcile machine decisions with governed human actions, preserve uncertainty about scope and causality, and produce an auditable narrative that can stand up to internal review, regulator challenge, and remediation planning.

## Likely architecture choices

- An orchestrated multi-agent design can divide evidence collection across screening telemetry, list-ingestion history, and case-routing traces while sharing one normalized investigation record.
- Shared case memory should track affected transactions, competing causal hypotheses, rejected explanations, and open verification checks across compliance, engineering, and operations participants.
- Human-in-the-loop approval is required before declaring the primary root cause, defining the official incident scope, or using the findings in regulator communications.

## Governance notes

- Preserve evidence provenance for every affected payment, rule version, and analyst action so the final narrative is auditable and reproducible.
- Separate observed control failures from inferred intent; analyst suppressions or overrides should not be treated as misconduct without independent review.
- The workflow should minimize exposure of personal and payment data in working artifacts while retaining enough detail for legal hold, audit, and regulator-response obligations.
- Remediation commitments, retrospective lookback expansion, suspicious activity filing decisions, and external statements must remain human-owned.

## Evaluation considerations

- Completeness of the reconciled timeline linking list updates, rule behavior, routing outcomes, and human review activity
- Accuracy of the ranked hypotheses versus the final compliance-accepted explanation of the screening gap
- Percentage of affected transactions with inspectable evidence showing why they bypassed manual review
- Whether the workflow surfaces residual uncertainty, scope limitations, and competing causes clearly enough for audit and regulator scrutiny
