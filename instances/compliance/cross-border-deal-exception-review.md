# Cross-border deal exception review

## Linked pattern(s)

- `deal-desk-recommendation-support`

## Domain

Compliance.

## Scenario summary

A regional account team proposes a renewal for a multinational distributor that wants nonstandard pricing, extended payment terms through a reseller, and a contractual exception allowing customer data support from an additional jurisdiction. Compliance must review whether the combined commercial package should be recommended as-is, narrowed to a safer structure, or escalated because pricing concessions, contract language, and cross-border exposure interact in ways that exceed ordinary approval thresholds.

## Target systems / source systems

- CRM opportunity record, quote drafts, and reseller structure details
- Pricing policy, approval matrix, and prior exception register
- Standard contract templates, requested redlines, and legal fallback clauses
- Export-control, sanctions, privacy, and cross-border data-transfer guidance
- Margin analysis, revenue-recognition notes, and implementation-risk commentary

## Why this instance matters

This instance shows why deal support in compliance is not a generic contract summary task. Reviewers need a recommendation that keeps the commercial trade-offs visible while making policy limits, legal uncertainty, and required escalation paths explicit before anyone signals approval to the field.

## Likely architecture choices

- A recommendation-only workflow retrieves pricing guardrails, precedent exceptions, contractual deviations, and jurisdiction-specific compliance constraints into one review packet.
- Human-in-the-loop review is mandatory because the workflow should advise on option ranking and escalation triggers, not approve the exception or alter deal records.
- Write access to quoting, approval, or contracting systems should remain disabled so the agent cannot convert a recommendation into an operational commitment.

## Governance notes

- The packet should clearly separate viable options, blocked options, and unresolved legal or compliance questions instead of presenting one blended answer.
- Any recommendation that depends on precedent should note whether the older case matched the same jurisdictions, reseller model, and contract deviations.
- Non-waivable constraints such as sanctions, export, privacy, or revenue-recognition limits should trigger explicit escalation rather than risk-weighted downgrading.
- Sensitive pricing, customer, and contract data should be shared only with authorized reviewers and retained under commercial-confidentiality controls.

## Evaluation considerations

- Reviewer agreement with the recommended path and required escalation route
- Rate at which hidden compliance blockers are surfaced before customer-facing commitment
- Quality of evidence linking pricing, contract, and jurisdictional exposure to the recommendation
- Frequency of stale or mismatched precedent use detected during governed review
