# Sanctions screening manual fallback activation gate

## Linked pattern(s)

- `contingency-plan-activation-gate`

## Domain

Compliance.

## Scenario summary

After a material sanctions-screening outage is declared, compliance leadership has already identified the bounded fallback path and the accountable approval owner: a manual screening contingency for a defined set of payment corridors and protected release holds. Upstream truth-restoration and authority-routing work has already established the trusted outage scope, active payment holds, and decision lane. The planning workflow now has to prepare one activation-ready packet showing reviewer coverage by shift, queue partitioning, legal-notice constraints, protected-channel rules, and the prerequisite controls needed before the manual fallback can be approved. It should preserve explicit holds for any uncovered review cell, unresolved legal hold, or missing queue-control segregation, and stop at the approval gate rather than releasing payments, determining regulator posture, or launching manual screening operations.

## Target systems / source systems

- Compliance continuity playbooks and outage workspace with the declared fallback scope, protected release boundaries, and prior gate packets
- Trusted outage-state, payment-hold, queue-segmentation, and reviewer-coverage systems already accepted as authoritative inputs for fallback preparation
- Legal-hold records, delegate rosters, calendars, and staffing plans for sanctions reviewers, queue supervisors, compliance leadership, and legal responders
- Approval-routing and audit systems that capture packet versions, hold state, and human sign-off before any manual screening contingency may start
- Restricted communications tooling for regulator-response and internal-notice checkpoints that remain downstream of the planning gate

## Why this instance matters

This grounds the pattern in compliance where the hard problem is preparing a governed activation packet for a sensitive fallback path without blurring into authority recommendation, truth verification, or payment action. It stays planning-centered because the output is a readiness packet with explicit holds and staffing commitments, not a release decision or manual-screening execution record. The instance shows how contingency planning can remain useful and bounded even in a regulator-sensitive outage.

## Likely architecture choices

- Approval-gated execution fits because the manual fallback may be operationally prepared but must remain blocked until compliance leadership approves the packet.
- The readiness ledger should tie reviewer staffing, queue segmentation, legal holds, protected-channel rules, and release boundaries to one current packet version.
- Explicit holds should remain visible for missing reviewer coverage, unresolved legal constraints, or absent segregation-of-duties checkpoints instead of being normalized away.
- The workflow should stop at the packet and hold register rather than recommending the authority lane again, re-establishing outage truth, or initiating manual screening.

## Governance notes

- Protected prerequisites such as reviewer coverage, legal-hold visibility, queue segregation, and release-boundary controls should be explicit before the packet can be treated as activation-ready.
- Shared packets should minimize payment, counterparty, jurisdiction, and legal-analysis detail outside restricted compliance and legal channels.
- Human compliance ownership is required before the packet becomes the authoritative basis for any manual-screening fallback activation.
- Audit lineage should preserve which trusted outage references, staffing commitments, and protected holds changed across packet revisions during the outage window.

## Evaluation considerations

- Time from declared manual-fallback preparation request to a human-reviewable activation packet with complete staffing, queue, and hold state
- Percentage of unresolved legal or staffing blockers kept visible in the hold register rather than hidden in a partially prepared fallback packet
- Agreement between the workflow's packet and the final human-approved manual-screening activation gate used downstream
- Stability of the readiness packet as outage scope, reviewer coverage, or protected release boundaries shift during the same critical period
