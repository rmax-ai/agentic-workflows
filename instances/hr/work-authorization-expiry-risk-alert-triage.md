# Work authorization expiry risk alert triage

## Linked pattern(s)

- `risk-alert-triage`

## Domain

HR.

## Scenario summary

An HR compliance operations team monitors a continuous stream of work-authorization expiry signals across visa records, employment-eligibility reverification dates, immigration-vendor case updates, manager-submitted job changes, and HRIS worker-status events. The workflow must collapse duplicate reminders tied to the same worker and authorization window, enrich each alert with employer entity, work location, job-change context, dependent filing status, prior outreach history, and any in-flight renewal case, and then prioritize which cases need immediate human review. The goal is to produce an evidence-backed triage queue for HR compliance specialists, immigration counsel coordinators, or employee-relations leads before an authorization lapse, but not to contact the worker, submit filings, change employment status, or decide legal strategy automatically.

## Target systems / source systems

- HRIS worker master, employment-status history, employer-entity records, work location data, and effective-dated job-change events
- Immigration case-management or vendor portal with visa category, expiration dates, filing milestones, receipt notices, reverification status, and counsel notes
- Document and identity repositories holding employment authorization documents, reverification evidence, and restricted case attachments
- Manager or HR intake channels for transfers, promotions, location changes, leave returns, and other events that may alter work-authorization assumptions
- HR compliance case queue used by immigration specialists, HR compliance reviewers, employee-relations partners, and designated legal liaisons
- Audit-grade evidence store preserving raw alert lineage, deduplication decisions, routing rationale, threshold versions, and human escalation approvals

## Why this instance matters

This grounds `risk-alert-triage` in HR work where the risk is not only missing a calendar deadline, but failing to recognize when a job change, worksite move, leave return, or stalled renewal case turns an apparently routine expiration reminder into a materially urgent compliance issue. A weak workflow would either flood HR specialists with repetitive date-based reminders for already-covered cases or under-rank the one worker whose authorization posture is genuinely at risk because source systems disagree. The instance stays inside monitor/detect/triage because the agentic work is continuous watching, context assembly, noise suppression, priority scoring, and governed routing into human review rather than employee outreach, filing preparation, work suspension, or retrospective legal analysis.

## Likely architecture choices

- Event-driven monitoring should continuously ingest date-based expiry signals, job and location changes, vendor case updates, and reverification status changes, then reopen or merge alert clusters as new evidence arrives.
- A tool-using single agent can correlate worker records across HRIS and immigration systems, suppress duplicate reminder chatter for cases already under active review, attach policy-relevant context, and publish a prioritized queue with explicit urgency drivers.
- Human-in-the-loop review should remain mandatory for any alert involving potential work interruption, conflicting eligibility evidence, protected leave overlap, missing identity documentation, or uncertainty about the lawful path forward.
- Approval-gated escalation is the right boundary because the workflow can recommend urgent routing to HR compliance, legal, or employee-relations reviewers, but it should not independently notify managers, pause work eligibility, or trigger employee-facing compliance actions.

## Governance notes

- Triage packets should show which expiry, reverification, job-change, or vendor-status rules fired; which raw alerts were merged; what supporting records were consulted; and why the case entered a given urgency tier.
- Privacy controls should minimize immigration category details, passport or document identifiers, personal contact data, medical-leave overlap information, and other sensitive worker information in broad queue views while retaining traceable evidence in restricted systems for authorized reviewers.
- Reversibility should be explicit: queue order, duplicate-linkage decisions, and urgency scores can be recomputed as receipt notices arrive or worker records are corrected, but a missed human review window near authorization expiry may be only partially recoverable, so low-confidence high-consequence cases should bias toward human review rather than silent suppression.
- Approval boundaries must remain firm: only authorized HR compliance staff, designated immigration partners, legal reviewers, or employee-relations owners may decide whether outreach is needed, whether work restrictions apply, whether a case is escalated externally, or whether a record can be closed as resolved.
- Auditability should preserve source timestamps, policy versions, suppression rationale, reviewer overrides, and escalation history so internal audit, labor-compliance review, or external counsel support can reconstruct exactly how a case was triaged.

## Evaluation considerations

- Recall of historically high-risk work-authorization or reverification cases that should have reached urgent human review before a lapse window
- Reduction in duplicate reviewer work from merged reminder and vendor-status alerts without lowering capture of genuinely urgent authorization-risk cases
- Median time from first relevant expiry or status-change signal to a triage packet containing worker context, policy basis, and routing rationale
- Reviewer override rate for alerts that were over-ranked because active renewal evidence was missed or under-ranked because conflicting HRIS and vendor records were not surfaced
- Auditability of suppression, merge, policy-version, and escalation decisions during internal compliance testing, immigration-program review, or dispute reconstruction
