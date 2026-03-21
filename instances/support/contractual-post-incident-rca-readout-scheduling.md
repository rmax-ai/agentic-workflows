# Contractual post-incident RCA readout scheduling

## Linked pattern(s)

- `calendar-conflict-coordination`

## Domain

Support.

## Scenario summary

After a resolved authentication outage for a regulated enterprise customer, a premium support program manager needs to schedule the contractual root-cause readout within five business days of the customer-safe RCA draft being approved. The meeting must include the assigned escalation manager, the reliability engineer who owned the fix, the customer success director, the customer's incident manager, and an approved language interpreter for the customer's Mexico City stakeholder group, while also respecting the customer's CAB blackout blocks, the engineer's follow-the-sun handoff window, and policy that customer-facing readouts cannot be booked outside published support coverage hours without duty-manager approval. The workflow is about finding a viable slot, placing reversible holds, and escalating quickly when no compliant overlap exists rather than improvising attendee substitutions or sending a final invite without human confirmation.

## Target systems / source systems

- Support escalation record with contractual RCA deadline, required attendee roles, and customer-safe readout status
- Team calendars for premium support, site reliability, customer success, and the customer's named incident contacts
- Interpreter scheduling roster with approved language coverage and availability windows
- Customer account record with timezone, CAB blackout periods, and preferred readout modality
- Calendar and meeting tools that support tentative holds, delegate-aware invites, and reversible drafts
- Support leadership channel where exception requests, rejected slots, and final approval status are tracked

## Why this instance matters

This grounds the scheduling pattern in a support workflow that is customer-facing but no longer a live bridge. Unlike the existing same-day escalation bridge example, the hard part here is reconciling contractual follow-up timing, interpreter availability, customer CAB constraints, and support-coverage boundaries for a post-incident readout rather than assembling active responders during a fast-moving outage.

## Likely architecture choices

- A tool-using single agent gathers free-busy availability, the contractual readout deadline, interpreter coverage, customer blackout metadata, and support-hours policy from approved systems.
- Bounded delegation fits because the agent can rank feasible slots, place short-lived tentative holds, and draft a timezone-normalized invite packet, but it should not bypass required customer-facing roles, book outside support coverage hours, or confirm the final readout without the premium support manager's approval.
- Human checkpoints remain necessary when no compliant overlap exists before the contractual deadline, when the only feasible slot crosses the engineer's protected handoff window, or when the interpreter or customer asks for a time that would require an exception to published coverage policy.

## Governance notes

- Required roles should be explicit before any hold is placed: escalation manager, fix owner, customer success director, customer incident manager, and approved interpreter when the customer requests localized delivery.
- Calendar access should stay limited to free-busy, timezone, delegate, and policy metadata rather than exposing private event details from internal staff or customer participants.
- Tentative holds should be reversible, short-lived, and tied to the specific escalation record so stale placeholders do not block other customer commitments.
- The workflow should minimize copied incident details in invites, sharing only the meeting purpose, approved attendee roles, and timing information needed for coordination.
- The workflow should escalate instead of guessing when no in-policy slot exists before the contractual deadline, when the only overlap falls outside published support coverage, or when a substitute attendee would change who is accountable for the RCA readout.
- Final commitment should stay human-owned: the premium support manager or escalation manager confirms the selected slot and any approved exception before the customer-facing invite becomes authoritative.

## Evaluation considerations

- Median time from customer-safe RCA approval to a viable readout slot covering all required roles before the contractual deadline
- Percentage of readout meetings confirmed without manual back-and-forth beyond defined premium-support checkpoints
- Frequency of escalations caused by interpreter availability, customer CAB blackout conflicts, or support-hours policy boundaries
- Audit usefulness of the coordination log for showing which slots were rejected, which reversible holds were placed, and why a human had to approve the final commitment or exception
