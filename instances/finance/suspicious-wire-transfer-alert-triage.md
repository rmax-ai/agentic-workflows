# Suspicious wire transfer alert triage

## Linked pattern(s)

- `risk-alert-triage`

## Domain

Finance.

## Scenario summary

A treasury operations team receives real-time alerts for outgoing corporate wire transfers that deviate from a customer's historical behavior, beneficiary profile, jurisdiction pattern, or sanction-screening context. The workflow must quickly separate likely false positives from alerts that warrant analyst escalation, account-contact review, or temporary payment hold consideration.

## Target systems / source systems

- Transaction-monitoring alert stream and scoring pipeline
- Customer profile, KYC, and historical payment-behavior records
- Beneficiary screening, sanctions, and adverse-media results
- Treasury case-management queue and prior alert dispositions
- Wire-approval workflow logs and analyst review notes

## Why this instance matters

This instance grounds the pattern in a finance setting where speed, explainability, and governance are tightly coupled. Effective triage lowers analyst overload, but missed prioritization can create fraud loss, regulatory exposure, and poorly governed interventions against legitimate customers.

## Likely architecture choices

- Event-driven monitoring ingests alert signals continuously and enriches them with customer, beneficiary, and prior-case context.
- Human-in-the-loop review stays embedded for severe, low-confidence, or policy-conflicted cases that could affect funds movement or regulatory reporting.
- Approval-gated routing keeps automated scoring advisory until an authorized reviewer confirms escalation, suppression, or downstream action.

## Governance notes

- Triage packets should explain which rules fired, what context changed the score, and why the case was routed to a given queue.
- Threshold, suppression, and routing-policy changes need controlled review because they directly affect false-negative and false-positive risk.
- High-severity cases should not trigger irreversible account restrictions, filing decisions, or payment blocking without human approval.
- Sensitive financial and personal data should be minimized in downstream artifacts while preserving enough evidence for audit and case reconstruction.

## Evaluation considerations

- Recall of historically suspicious wire cases that should have been escalated
- Reduction in analyst-handled false positives without harming high-risk recall
- Median time from alert arrival to triage packet ready for review
- Explainability of suppression, merge, and escalation decisions during control testing or audit replay
