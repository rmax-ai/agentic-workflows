# Release-readiness review coordination refresh after approver window change

## Linked pattern(s)

- `authoritative-change-coordination-refresh`

## Domain

Engineering.

## Scenario summary

A release-readiness review for a customer-facing identity service already has a coordination packet, tentative hold, required-attendee list, and evidence-ready checkpoint linked to the governing change record. After that package is issued, authoritative schedule conditions shift: the security reviewer’s approved delegate mapping changes, the database migration owner loses the original review window because of an incident bridge, and updated test-evidence timing pushes the earliest valid review start later in the same day. The workflow should refresh the existing coordination package, issue participant-specific delta notices, and hold the changed schedule state at an explicit release-owner adoption checkpoint rather than rebuilding the whole cutover plan, deciding go/no-go, or touching the deployment itself.

```mermaid
flowchart TD
    A["Authoritative delegate, availability,<br>or evidence-ready change arrives"]
    B["Verify the updated delegate mapping,<br>migration-owner window loss, and latest<br>evidence-ready timestamp against the<br>governing change record"]
    C{"A viable refreshed review slot and<br>required-role coverage still stay inside the<br>approved cutover window?"}
    D["Refresh the existing coordination packet,<br>tentative hold, attendee state, and lineage"]
    E["Send participant-specific delta notices to<br>affected reviewers, delegates, and release<br>coordination owners"]
    F{"Release owner adopts the materially<br>changed review timing or attendee state?"}
    G["Publish the refreshed packet as the<br>current authoritative review coordination state"]
    H["Keep the refreshed packet tentative at<br>the release-owner adoption checkpoint"]
    I["Route a bounded exception for freeze-window<br>risk, missing approved delegate coverage,<br>or other out-of-policy refresh conditions"]

    A -->|"Detect authoritative change"| B
    B -->|"Check schedule and role constraints"| C
    C -->|"Yes"| D
    C -->|"No"| I
    D -->|"Reissue current package"| E
    E -->|"Present changed state for adoption"| F
    F -->|"Yes"| G
    F -->|"No"| H
```

## Target systems / source systems

- Change-management record with the approved cutover window, required review roles, and current owner confirmation state
- Team calendars, delegate mappings, and on-call scheduling metadata for release engineering, security review, database migration, and site reliability
- CI and readiness systems publishing authoritative evidence-ready timestamps that constrain when the review can occur
- Release coordination workspace where tentative holds, acknowledgements, and refresh lineage are tracked
- Notification channel or meeting system that can reissue targeted attendee updates without silently replacing the authoritative invite

## Why this instance matters

This grounds the pattern in engineering work where the main need is not initial slot-finding but keeping an existing review checkpoint synchronized with authoritative availability and readiness changes. The value comes from preserving one current coordination artifact, one clear delta history, and explicit human adoption of consequential changes so required reviewers stay aligned during a narrow release window. It stays out of recommendation and execution scope because the workflow does not judge whether the release is safe, replan the whole cutover sequence, or launch production changes.

## Likely architecture choices

```mermaid
flowchart LR
    change["Change-management record<br>approved cutover window, required review roles,<br>and current owner confirmation state"]
    calendars["Team calendars, delegate mappings,<br>and on-call scheduling metadata for<br>release engineering, security review,<br>database migration, and site reliability"]
    readiness["CI and readiness systems<br>authoritative evidence-ready timestamps"]
    refresh["Release-readiness coordination refresh<br>event-driven monitoring, role checks,<br>and schedule validation"]
    workspace["Release coordination workspace<br>tentative holds, acknowledgements,<br>refresh lineage, and current packet state"]
    notices["Notification channel or meeting system<br>targeted attendee updates and<br>authoritative invite history"]
    owner["Release owner<br>adoption checkpoint"]
    exceptions["Bounded exception routing<br>freeze-window risk, missing approved delegate<br>coverage, and out-of-policy refresh cases"]

    change -->|"Provides approved cutover window,<br>required roles, and current owner state"| refresh
    calendars -->|"Provides attendee availability,<br>delegate eligibility, and on-call coverage"| refresh
    readiness -->|"Provides authoritative evidence-ready<br>timing constraints"| refresh
    workspace -->|"Provides tentative hold state,<br>acknowledgements, and lineage"| refresh
    refresh -->|"Writes refreshed packet state,<br>tentative hold updates, and lineage"| workspace
    refresh -->|"Issues participant-specific timing,<br>delegate, and readiness deltas"| notices
    refresh -->|"Presents materially changed timing<br>or attendee state for adoption"| owner
    owner -->|"Returns adoption or tentative-hold<br>outcome for the refreshed packet"| refresh
    refresh -->|"Routes freeze-window conflicts,<br>delegate-coverage gaps, or other<br>out-of-policy refresh conditions"| exceptions
```

- Event-driven monitoring should react only to approved delegate-state updates, authoritative evidence-ready changes, and governed calendar updates that affect the issued review checkpoint.
- Exception-gated autonomy fits because the workflow can refresh the packet, revise the tentative hold, and notify affected participants automatically when changes stay inside the approved cutover window and role boundaries.
- The release owner should adopt any changed meeting time, required-attendee substitution, or freeze-window edge case before the refreshed packet becomes authoritative.
- The workflow should preserve append-only lineage showing which event changed the packet, who received notices, and whether acknowledgements remain outstanding.

## Governance notes

- Required roles and allowable delegates should be explicit before any automatic refresh occurs: release manager, service owner, security reviewer, database migration owner, and site reliability lead.
- Calendar and role access should stay limited to free-busy, delegate eligibility, and schedule-policy metadata rather than private event contents or unrelated incident details.
- Refresh should not silently convert a tentative change into a final meeting commitment; consequential updates stay pending until the release owner adopts them.
- Notification logic should target only affected participants and reviewers rather than rebroadcasting sensitive release context to broad channels.
- The workflow should escalate instead of refreshing authoritatively when the only viable updated slot crosses a protected freeze boundary or a required role loses all approved delegate coverage.

## Evaluation considerations

- Time from authoritative availability or evidence-ready change to a refreshed coordination packet with clear adoption status
- Rate of required-attendee or timing changes correctly held for release-owner adoption before the invite becomes authoritative
- Participant ability to tell what changed between the prior and current review packet without reconstructing the full release thread manually
- Stability of the refresh loop during clustered release-day updates, delegate changes, or repeated evidence timestamp corrections
