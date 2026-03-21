# Procurement-card segregation-of-duties attestation recommendation

## Linked pattern(s)

- `control-requirement-attestation-recommendation`

## Domain

Finance.

## Scenario summary

A finance controls analyst is assembling the quarterly internal attestation for the procurement-card program covering cardholder onboarding, manager approval separation, statement-review completion, and unresolved exception aging. The source reports are mostly current, but one business unit still has two overdue manager-review samples, the training evidence for newly delegated approvers was exported before the latest roster change, and a prior-quarter exception allowing one small shared mailbox flow may no longer fit the current policy boundary. The workflow must recommend whether the packet is ready for controller review, should return for targeted remediation, or should escalate to controllership because the requirement fit now depends on exception interpretation before any human signs the internal attestation or changes finance-system settings.

## Target systems / source systems

- ERP and expense-management workflow reports showing cardholder approvals, statement-review completion, and sampled segregation-of-duties evidence
- Procurement-card administration portal with cardholder roster, delegated approver assignments, and training-completion exports
- Finance controls library with the current quarterly attestation checklist, exception rules, and freshness thresholds for supporting evidence
- Internal audit and prior-quarter review archive containing earlier exceptions, remediation commitments, and reviewer comments
- Governed finance review workspace where the attestation packet, requirement mapping, and escalation notes are stored for controller review

## Why this instance matters

This grounds the pattern in finance where the key job is evaluating whether a bounded internal control-attestation packet meets a known requirement set, not planning remediation work, collaborating through multiple drafting rounds, or filing a regulatory report. The value is surfacing requirement gaps and exception dependence clearly enough that a controller can make a deliberate decision without mistaking a neat summary for an already accepted attestation. It also shows why low-risk treatment can still be appropriate: the workflow only advises on an internal review packet and stops before any formal sign-off or system change.

## Likely architecture choices

- A tool-using single agent can reconcile approval-separation reports, training exports, sample evidence, and exception history into one reviewable requirement map.
- Human-in-the-loop review should remain primary because the controller or delegated finance owner must decide whether partial evidence is acceptable or whether remediation is required before sign-off.
- Read-only system access is preferable so the workflow cannot approve transactions, edit approver assignments, or record the attestation automatically.

## Governance notes

- Each attestation requirement should retain direct links to the source report, sample set, training export, or approved exception that supports it for the current quarter.
- Overdue samples, stale training evidence, or exceptions that no longer match current roster design should trigger explicit remediation or escalation rather than being summarized as minor noise.
- Cardholder details, manager assignments, and audit comments should be minimized to what controller reviewers need for the attestation decision and retained under normal finance confidentiality controls.
- The workflow must preserve the handoff boundary clearly: accepting the attestation, granting a renewed exception, or changing finance-control configuration remains fully human-owned.

## Evaluation considerations

- Reviewer agreement with the recommended posture before controller sign-off
- Rate at which stale evidence, overdue reviews, or no-longer-valid exceptions are caught before quarterly attestation completion
- Quality of traceability from each segregation-of-duties requirement to current finance evidence and prior exception history
- Frequency of human overrides caused by weak requirement mapping or hidden ambiguity in the packet
