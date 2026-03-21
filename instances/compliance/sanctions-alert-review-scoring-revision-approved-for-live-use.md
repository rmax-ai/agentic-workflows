# Sanctions alert-review scoring revision approved for live use

## Linked pattern(s)

- `approval-gated-optimization-state-release`

## Domain

Compliance.

## Scenario summary

A sanctions governance lead has prepared one exact alert-review scoring revision after replay shows that the current live profile underweights nested beneficial-ownership signals, corridor-specific evasion patterns, and regulator-sensitive customer segments when alert volumes surge. The candidate revision raises sensitivity for those protected screening factors, tightens cooldown handling on low-yield alert clusters, and names a restore target if analyst overrides or missed-escalation risk rise. The workflow must release that exact scoring revision into bounded live use only after a human approver confirms the manifest, validity window, and rollback packet, while staying centered on governed optimization-state release rather than clearing alerts, adjudicating true matches, filing regulator reports, or launching remediation work.

## Target systems / source systems

- Versioned sanctions alert-scoring registry with the current live profile, candidate revision hash, protected screening floors, and prior trusted revisions
- Replay and shadow-analysis workspace with analyst overrides, false-positive burden, missed-escalation checks, corridor-specific alert history, and exam findings
- Compliance approval and manifest tooling used by sanctions governance leadership to authorize one bounded live scoring revision for the named screening program scope
- Audit, rollback, and restoration controls that can restore the prior profile if protected-segment handling, analyst trust, or missed-escalation metrics worsen
- Screening-review dashboards, analyst queues, and governance oversight surfaces that consume the active alert-review scoring policy

## Why this instance matters

This grounds the pattern in compliance where the released artifact is a versioned screening-tuning revision, not a sanctions disposition or escalation decision. The reusable challenge is governing one exact live scoring revision with explicit approval, validity timing, and restore readiness in a regulator-visible workflow. That keeps the instance family-safe by ending at bounded optimization-state release rather than alert adjudication, investigator assignment, or downstream reporting execution.

## Likely architecture choices

- Approval-gated execution fits because the scoring revision can be technically ready in the screening registry while activation remains blocked until a named sanctions owner approves that exact version and live scope.
- Human-in-the-loop review remains necessary because accountable compliance leaders must accept the trade-offs among protected screening coverage, false-positive burden, and analyst capacity before the revision becomes live.
- A governed release agent can compare revision hashes, verify replay evidence, arm rollback triggers, and write the audit trace, but it should not clear alerts, decide sanctions matches, or trigger regulator outreach.

## Governance notes

- Approval should bind to one exact scoring revision, one named screening-program scope, and one validity window so later tuning edits cannot inherit stale authority.
- Protected screening floors for regulator-sensitive customer segments, nested ownership signals, and corridor-specific evasion patterns should remain explicit release conditions.
- Expiry should restore the prior trusted profile automatically unless sanctions governance leadership explicitly renews the revision after reviewing live alert outcomes.
- Rollback triggers should include unusual analyst override spikes, worsening missed-escalation indicators, or degraded handling of protected screening segments.
- Audit records should preserve the approved and prior revision ids, replay evidence windows, approver identity, validity timing, rollback criteria, and any extension or restore action.
- The workflow must not adjudicate alerts, freeze accounts, file suspicious-activity narratives, or launch remediation tasks; it only governs release of the scoring revision used by human screening-review surfaces.

## Evaluation considerations

- Reduction in missed-escalation risk, analyst override churn, and regulator-visible review defects after the approved scoring revision becomes live
- Accuracy of manifest binding among the approved revision hash, protected screening floors, and activated program scope
- Reliability of automatic expiry or rollback when false-positive burden, override behavior, or protected-segment handling breaches the approved guardrails
- Time required for compliance leaders to inspect one revision, approve bounded live use, and verify safe restoration to the prior trusted profile
