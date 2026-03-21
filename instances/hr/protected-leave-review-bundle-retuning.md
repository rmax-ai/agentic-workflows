# Protected leave review bundle retuning

## Linked pattern(s)

- `governed-optimization-bundle-retuning`

## Domain

HR.

## Scenario summary

A people operations governance lead is responsible for a shared leave-and-accommodation tuning bundle that affects several coupled surfaces: intake urgency scoring, document-sufficiency weighting, follow-up timing buffers, and specialist-review prioritization for protected leave and workplace accommodation cases. Recent outcome history shows that the active bundle has improved average closure time for straightforward cases, but escalations, reopen events, and supervisor overrides are increasing for intermittent-leave renewals, accommodation requests with sensitive medical documentation, and cases involving lower-visibility worker populations that require more careful review. The workflow must recommend a governed retuning package that adjusts the shared bundle across those surfaces so protected-worker fairness, documentation quality, and review timeliness improve together, without letting the system adjudicate leave eligibility, rewrite HR policy, or execute case actions without human adoption.

## Target systems / source systems

- Leave and accommodation case-management system with active case states, current urgency scores, follow-up timers, and specialist-review routing outputs
- HRIS, absence-management, and policy repositories with worker context, protected-leave rules, accommodation guidance, and case-type metadata
- Outcome and override history showing supervisor overrides, reopened cases, missed follow-up windows, escalations, and prior rollback events
- Shared parameter registry containing the active leave-review bundle, protected-worker fairness caps, evidence-sufficiency floors, and prior version history
- Replay workspace used to test candidate bundle versions against prior case cohorts before people-operations leaders adopt them
- Governance dashboard used by HR and employee-relations leads to inspect bundle trade-offs, defer policy-linked changes, and restore the last trusted version

## Why this instance matters

This grounds the pattern in an HR workflow where several coupled review surfaces share one optimization bundle and isolated local tuning would create unfair or unstable handling. A naive optimizer could keep reducing average cycle time by favoring simpler document patterns while pushing sensitive accommodation cases, intermittent-leave renewals, or lower-visibility worker groups into repeated reopen and escalation loops. The example remains firmly in optimize/adapt territory because the workflow ends at a human-adopted retuning package and candidate bundle version rather than leave determinations, policy adjudication, scheduling, or case execution.

## Likely architecture choices

- Orchestrated multi-agent coordination fits because separate roles can analyze outcome drift, test protected-worker fairness constraints, replay candidate bundles, and assemble one auditable retuning packet over shared state.
- Human-in-the-loop review should be standard because HR governance owners must explicitly accept or reject bundle changes before any live optimization state is updated.
- Recommendation-only autonomy keeps the workflow bounded: it can recommend how urgency weights, evidence floors, and follow-up buffers should move together, but it must not activate those changes or decide individual cases.
- HR leaders should remain able to freeze retuning, defer policy-adjacent parameter moves for legal or employee-relations review, and revert immediately if a newly adopted bundle harms protected-worker treatment.

## Governance notes

- Parameters affecting protected-worker fairness, medical-document sensitivity, statutory timing floors, and specialist-review protection should remain protected components that ordinary retuning cannot cross.
- Every retuning package should show cross-surface effects on reopen risk, escalation volume, follow-up timeliness, and lower-visibility worker populations so throughput gains cannot hide people-risk regression.
- Auditability should retain the current and proposed bundle versions, replay cohorts, supervisor overrides, deferred changes, adoption decisions, and rollback triggers for each retuning cycle.
- Optimization packets should minimize exposure of personal and medical details and preserve only the authorized evidence needed for HR governance review.
- Reversibility should be explicit: if escalations rise, follow-up windows are missed, or fairness checks degrade after adoption, the workflow should restore the last trusted bundle and surface the failed trade-off.
- The workflow must not determine eligibility, authorize accommodations, or send worker-facing actions; it only recommends changes to shared optimization state across existing review surfaces.

## Evaluation considerations

- Reduction in reopen events, supervisor overrides, and missed protected-leave follow-up windows after a retuned bundle is adopted
- Change in treatment of intermittent-leave renewals, accommodation cases with sensitive documentation, and lower-visibility worker populations across the coupled surfaces
- Frequency with which policy-adjacent parameter moves are correctly deferred instead of being smuggled into ordinary optimization
- Speed and clarity of rollback when a bundle improves closure speed but weakens fairness, documentation quality, or protected-case stability
