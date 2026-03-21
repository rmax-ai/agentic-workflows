# Benefits eligibility and deduction drift anomaly review

## Linked pattern(s)

- `anomaly-detection-review`

## Domain

HR.

## Scenario summary

An HR benefits operations team monitors eligibility determinations, dependent-coverage changes, qualifying-life-event updates, payroll deduction feeds, carrier-file acknowledgments, and retro-effective-date edits to detect mid-severity benefits anomalies before they turn into coverage gaps, payroll disputes, or compliance incidents. The workflow must collapse duplicate anomalies tied to the same worker or household, benefit plan, and effective-date window; enrich each case with plan eligibility rules, payroll-calendar context, approved event windows, prior reviewer notes, sensitive dependent-data exposure, and any recent vendor-file rejects; and then prioritize which anomalies deserve restricted human review. A case should enter the review queue when, for example, multiple workers in the same population lose medical-plan eligibility and restart deductions on mismatched dates without corresponding status changes, repeated retro deduction adjustments appear after a qualifying life event without carrier acceptance, or a burst of dependent eligibility flips lands near an enrollment cutoff with missing supporting context. The goal is an explainable anomaly review packet for benefits operations, payroll liaison, or people-compliance reviewers, not to correct deductions, contact employees or carriers, interpret plan law, or open a formal investigation automatically.

## Target systems / source systems

- HRIS and benefits-administration systems with worker eligibility status, dependent coverage, plan elections, effective dates, and qualifying-life-event metadata
- Payroll deduction and interface systems with deduction start-stop history, retro adjustment logs, payroll calendars, and transmission status to downstream vendors
- Carrier-feed, enrollment, and case-management tools with acknowledgment failures, file rejects, approved event windows, and prior reviewer dispositions
- Restricted review queues used by benefits operations leads, payroll liaisons, and people-compliance reviewers
- Audit-grade evidence storage preserving anomaly lineage, suppression decisions, routed packets, reviewer actions, and policy versions

## Why this instance matters

This grounds `anomaly-detection-review` in HR work where the early-warning problem is spotting unusual but not yet catastrophic drift between benefits eligibility state and deduction behavior before workers experience coverage confusion or downstream control failures. A weak workflow would either flood reviewers with every ordinary enrollment correction or miss the one recurring anomaly pattern that signals broken handoffs among HRIS, payroll, and carrier-file processes. The instance stays inside monitor/detect/triage because the agentic work is anomaly detection, bounded context assembly, duplicate suppression, prioritization, and routing into human review rather than eligibility adjudication, payroll correction, carrier outreach, employee communication, or formal investigation.

## Likely architecture choices

- Event-driven monitoring should continuously ingest eligibility updates, deduction changes, carrier-file responses, and qualifying-life-event edits, then reopen or merge anomaly clusters as new evidence arrives.
- A tool-using single agent can correlate worker and plan identifiers across HRIS, payroll, and benefits systems; check approved event windows and sensitive-data rules; attach bounded context; and publish a prioritized review packet with explicit anomaly drivers.
- Bounded delegation fits because routine mid-severity anomaly packets can route into a preapproved restricted benefits review queue without case-by-case authorization, while higher-consequence or protected cases still escalate to accountable humans.
- Deduction correction, carrier resubmission, employee outreach, legal interpretation, or enrollment action should remain outside the workflow and under explicit human control.

## Governance notes

- Review packets should show which anomaly features fired, which raw eligibility and deduction events were merged, what approved-window or carrier-feedback context was checked, and why the case was routed to a particular restricted queue.
- Sensitive personal, dependent, health-plan, and payroll details should be minimized in queue views and retained only in the restricted evidence path necessary for authorized reviewers.
- Reversibility should stay explicit: queue placement and packet contents can be recomputed as late carrier acknowledgments or event documentation arrives, but missed review windows may be only partially recoverable once payroll cycles pass or workers experience coverage disruption.
- Approval boundaries must remain firm: only authorized benefits operations, payroll, or people-compliance owners may decide whether the anomaly becomes a correction task, a vendor escalation, a worker communication, or a closed false positive.
- Auditability should preserve source timestamps, anomaly thresholds, duplicate handling, reviewer overrides, and routing history so later controls review can reconstruct why sensitive benefits-drift anomalies were or were not surfaced promptly.

## Evaluation considerations

- Recall of historically meaningful benefits eligibility and deduction anomalies that should have reached human review before downstream coverage or payroll issues grew
- Reduction in duplicate reviewer work from merged worker-plan anomaly clusters without lowering capture of genuinely important benefits-drift patterns
- Median time from first anomalous eligibility-versus-deduction signal to a review packet containing plan context, approved-window checks, prior notes, and routing rationale
- Reviewer override rate for anomaly packets that were over-ranked because routine enrollment cleanup was misread or under-ranked because cross-system context was not assembled clearly enough
- Auditability of suppression, merge, and routing decisions during benefits-controls review or payroll-interface retrospectives
