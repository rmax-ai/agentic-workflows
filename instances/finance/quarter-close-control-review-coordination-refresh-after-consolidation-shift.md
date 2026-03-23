# Quarter-close control review coordination refresh after consolidation shift

## Linked pattern(s)

- `authoritative-change-coordination-refresh`

## Domain

Finance.

## Scenario summary

A quarter-close control review already has a published coordination packet tying together the locked close calendar, required attendees, tentative meeting hold, and handoff expectations for controllership, treasury accounting, SEC reporting, internal controls, and finance systems. Then an authoritative consolidation timing shift lands late in the cycle: a final entity true-up moves the earliest valid review window, one required attendee changes to an approved delegate because of board-material review overlap, and the close calendar adds a protected blackout interval for lender materials. The workflow should refresh the existing review packet, reissue targeted delta notices, and queue controller adoption for the materially changed state rather than recomputing the full close plan, recommending accounting treatment, or advancing downstream certification work.

```mermaid
flowchart TD
    A["Authoritative consolidation shift<br>updates the close calendar"] --> B["Compare the new timing against the<br>published control review packet"]
    B --> C{"Trigger provenance and current<br>packet lineage verified?"}
    C -- "No" --> H["Hold refresh and route<br>exception review"]
    C -- "Yes" --> D["Refresh only bounded coordination deltas:<br>review window, delegate, blackout impact"]
    D --> E{"Revised slot stays inside locked<br>close guardrails and avoids blackout?"}
    E -- "No" --> H
    E -- "Yes" --> F["Reissue the review packet and send<br>role-targeted delta notices"]
    F --> G{"Material time shift or required<br>delegate substitution present?"}
    G -- "No" --> J["Publish refreshed packet, notices,<br>and lineage as current coordination state"]
    G -- "Yes" --> I["Hold authoritative status and queue<br>controller adoption for the changed state"]
    I -- "Adopted" --> J
```

## Target systems / source systems

- Close-management tracker with the authoritative milestone calendar, required review roles, and prior coordination status
- Team calendars and delegate records for controllership, treasury accounting, SEC reporting, internal controls, and finance systems
- Consolidation and close-status systems publishing approved timing shifts that affect when the control review may occur
- Finance coordination workspace where invite status, acknowledgements, exceptions, and refresh lineage are maintained
- Messaging or meeting tools capable of sending role-targeted change notices without exposing broader close commentary

## Why this instance matters

This grounds the pattern in a finance workflow where participants depend on one current review packet during a compressed close window and cannot afford ambiguous schedule drift. The coordination refresh needs to preserve the link between authoritative close-state changes and the revised review checkpoint, while keeping human ownership over any consequential timing or authority shift. The instance remains in planning scope because it refreshes coordination state only; it does not decide the close outcome, reinterpret accounting policy, or file anything externally.

## Likely architecture choices

```mermaid
flowchart LR
    tracker["Close-management tracker<br>authoritative milestone calendar,<br>required review roles, prior coordination status,<br>and protected blackout interval"]
    calendars["Team calendars and delegate records<br>controllership, treasury accounting,<br>SEC reporting, internal controls,<br>and finance systems"]
    consolidation["Consolidation and close-status systems<br>approved timing shifts affecting<br>when the control review may occur"]
    refresh["Quarter-close control-review refresh<br>event-driven monitoring, guardrail checks,<br>and packet delta preparation"]
    workspace["Finance coordination workspace<br>invite status, acknowledgements,<br>exceptions, and refresh lineage"]
    notices["Messaging or meeting tools<br>role-targeted change notices and<br>review packet reissue delivery"]
    owner["Assistant controller or designated<br>close owner adoption checkpoint"]
    exceptions["Exception review<br>no-feasible-window, delegate-conflict,<br>or blackout-boundary routing"]

    tracker -->|"Provides milestone calendar, required roles,<br>prior coordination state, and blackout constraints"| refresh
    calendars -->|"Provides attendee availability<br>and approved delegate coverage"| refresh
    consolidation -->|"Provides approved timing shifts that move<br>the valid control-review window"| refresh
    workspace -->|"Provides current invite status,<br>acknowledgements, exceptions,<br>and existing lineage"| refresh
    refresh -->|"Writes refreshed packet state,<br>lineage updates, and exception status"| workspace
    refresh -->|"Issues role-targeted delta notices<br>and updated review packet delivery"| notices
    refresh -->|"Presents materially changed timing,<br>delegate, or blackout impact for adoption"| owner
    owner -->|"Returns adoption or hold outcome<br>for the changed coordination state"| refresh
    refresh -->|"Routes no-feasible-window, delegate-conflict,<br>or blackout-boundary cases"| exceptions
```

- Event-driven monitoring should subscribe to approved close-calendar updates, posted consolidation timing shifts, and controlled delegate-state changes that affect the issued review packet.
- Exception-gated autonomy fits because routine packet refresh, targeted notice issuance, and lineage updates can happen automatically when changes remain inside approved close guardrails.
- The assistant controller or designated close owner should adopt any materially changed meeting time, protected-window impact, or required-attendee substitution before the refreshed packet becomes authoritative.
- Exception handling should route no-feasible-window cases, delegate conflicts, or blackout-boundary violations instead of publishing a misleading current state.

## Governance notes

- Required roles and approved delegates should remain explicit and auditable for assistant controller, treasury accounting, SEC reporting, internal controls, and finance systems ownership.
- Refreshed notices should include only role-relevant timing, attendee, and checkpoint deltas rather than detailed ledger commentary or sensitive close narrative.
- The workflow should preserve prior and current schedule versions, recipient lists, and adoption actions so close leadership can reconstruct how the packet changed.
- Automatic refresh should be blocked when the trigger comes from a draft workbook, unofficial calendar note, or unapproved attendee substitution.
- Repeated late-cycle refreshes should be monitored for churn so the workflow does not overwhelm reviewers with conflicting versions near sign-off.

## Evaluation considerations

- Percentage of approved close-state changes reflected in one current control-review packet with complete lineage and clear controller adoption status
- Rate of blackout-boundary conflicts, unsupported delegate substitutions, or ambiguous timing shifts correctly routed to exception review
- Reviewer ability to identify the latest authoritative review packet and understand what changed since the prior version
- Notification-deduplication performance when multiple close updates land within the same narrow review window
