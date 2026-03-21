# Warehouse slotting reference rollout verification

## Linked pattern(s)

- `claimed-state-verification`

## Domain

Operations.

## Scenario summary

An operations excellence team marks an updated warehouse slotting quick-reference bundle as rolled out for the next shift after publishing new kiosk pages, scanner help cards, and printable supervisor sheets. Site leads want to know whether that claimed rollout state is actually true across the approved reference surfaces before they assume the new guidance is available on the floor. The workflow verifies the rollout claim against authoritative publication evidence and stops at a clear confirmed, disproved, or inconclusive result; it must not assign labor, reprioritize replenishment work, or push new materials itself.

## Target systems / source systems

- Controlled operations content repository containing the approved slotting reference bundle and release metadata
- Warehouse kiosk content service that serves the current quick-reference version to floor supervisors
- Scanner help-card distribution system with bundle version and device-sync timestamps
- Printable supervisor-sheet archive used by site leads for shift binders
- Rollout event feed or workflow tracker that records the original rollout-complete claim
- Verification log storing evidence checks, lag assessments, and follow-up records for stale sites or surfaces

## Why this instance matters

This instance shows low-risk verification in operations without drifting into briefing, planning, or execution. A content owner's rollout claim may be directionally right while one surface still serves an older version or one device channel remains inside its sync delay. The workflow's job is to prove what state actually holds on the approved reference surfaces so supervisors can coordinate confidently without mistaking an intended rollout for a completed one.

## Likely architecture choices

- Event-driven monitoring is appropriate because the workflow begins from the recorded rollout-complete claim and immediately checks whether the expected reference state now exists.
- A tool-using single agent can compare bundle versions across the content repository, kiosk service, scanner help-card system, and printable archive while applying approved lag tolerances.
- Bounded delegation fits because operations owners can define the in-scope surfaces and acceptable sync windows in advance while humans decide whether any stale rollout requires manual republishing or local follow-up.
- Verification history should remain durable so repeated rollout claims or expected sync delays do not generate ambiguous records for the same bundle.

## Governance notes

- Only approved reference surfaces should drive the verdict; supervisor chat confirmations or informal photos of posted sheets should remain supplementary, not authoritative.
- The workflow should preserve version ids, sync timestamps, and affected surface names so regional operations leads can inspect why a rollout was confirmed or held.
- If one site surface is still inside an allowed sync delay, the verdict should remain explicitly inconclusive rather than implying a completed or failed rollout.
- Republishing materials, opening a site exception, or changing floor procedures stays outside the verification scope and under human control.

## Evaluation considerations

- Percentage of slotting-reference rollout claims that produce a verdict with complete surface-by-surface evidence traceability
- Rate at which stale kiosk, scanner, or printable-surface states are detected before supervisors rely on the new reference bundle
- Reviewer correction rate for lag-window handling and authoritative-surface classification
- Clarity of follow-up records when one approved surface remains out of date beyond the allowed rollout window
