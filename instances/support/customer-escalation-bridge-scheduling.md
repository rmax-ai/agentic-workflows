# Customer escalation bridge scheduling

## Linked pattern(s)

- `calendar-conflict-coordination`

## Domain

Support.

## Scenario summary

After a severe overnight service disruption affecting a large enterprise customer, a support escalation manager needs to schedule a same-day customer bridge to align internal responders before the customer update call. The bridge has to include the assigned support lead, the incident commander, the engineering service owner for the degraded component, and the customer success manager covering the account, while also respecting the customer team's stated availability in US Eastern time and the internal engineering lead's working hours in Central European time. The workflow is about finding a viable coordination slot, placing reversible holds, and escalating quickly if no in-policy overlap exists within the agreed response window.

## Target systems / source systems

- Support incident ticket with severity, account tier, and required responder roles
- Team calendars for support, engineering, customer success, and incident leadership
- On-call schedule and major-incident roster for current responders
- CRM account record with customer contacts, timezone, and bridge preferences
- Video meeting platform and calendar system that support tentative holds
- Messaging channel for the incident room and escalation updates

## Why this instance matters

This grounds the pattern in a customer-facing coordination problem where delay, missed attendance, or timezone confusion directly affects trust during a live escalation. Unlike the existing operations example, the hard part is not shift-plus-room logistics around a maintenance window; it is reconciling fast-moving responder availability, customer-facing timing commitments, and explicit boundaries on what the scheduling workflow may do without incident leadership approval.

## Likely architecture choices

- A tool-using single agent gathers free-busy data, current on-call assignments, customer timezone metadata, and bridge preferences from approved systems.
- Bounded delegation fits because the agent can rank feasible bridge times, place short-lived tentative holds, and prepare an invite packet, but it should not move executive incident reviews, override protected focus blocks, or commit to an out-of-hours customer call without escalation.
- Human checkpoints remain for cases where the customer requests a time outside internal policy, a required internal responder has no overlap with the customer window, or incident leadership wants to substitute attendees before the bridge is confirmed.

## Governance notes

- Required roles should be explicit: support owner, engineering owner, customer success owner, and incident leadership delegate if severity policy requires one.
- Calendar access should stay limited to free-busy, timezone, and policy metadata rather than exposing private appointment contents from responders or customer contacts.
- Tentative holds should expire automatically if the bridge is not confirmed within the escalation SLA so calendars do not accumulate stale blockers during a fast-moving incident.
- The workflow should escalate instead of guessing when no compliant overlap exists inside the promised customer-update window, when the only slot crosses protected overnight hours, or when a customer-facing invite would be sent without the minimum required internal coverage.

## Evaluation considerations

- Median time from escalation-triggered scheduling request to a viable bridge slot with all required internal roles covered
- Rate of bridge invites sent without later rescheduling due to missed timezone normalization or stale on-call data
- Frequency of escalations caused by no in-policy overlap versus avoidable coordination failures
- Audit usefulness of the coordination log for explaining which slots were rejected, which reversible holds were placed, and why incident leadership approval was required
