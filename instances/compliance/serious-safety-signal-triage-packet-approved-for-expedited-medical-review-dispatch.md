# Serious safety signal triage packet approved for expedited medical-review dispatch

## Linked pattern(s)

- `approval-gated-triage-dispatch`

## Domain

Compliance.

## Scenario summary

A pharmacovigilance operations team has already triaged a serious safety-signal packet that groups related adverse-event alerts, seriousness coding, product context, reporting-clock references, and unresolved questions about expectedness. Before the packet may enter the expedited medical-review lane, a qualified safety reviewer must confirm that the exact packet revision, protected routing scope, and open holds are acceptable for downstream intake. The dispatch workflow therefore monitors packet freshness, follow-up completeness, reviewer sign-off, and protected lane metadata, then releases the packet into expedited medical review only when those approval conditions are satisfied. It stops at the governed handoff boundary rather than deciding causality, drafting regulator communication, or executing case-processing actions.

## Target systems / source systems

- Pharmacovigilance case and signal-triage systems storing the already-triaged safety packet, duplicate linkage, seriousness coding, and reporting-clock context
- Follow-up intake, expectedness reference, and product-label systems that provide freshness and hold-state inputs already cited by the packet
- Expedited medical-review queue and dispatch-manifest tooling used to release one approved packet revision into the protected downstream lane
- Safety-review approval systems recording qualified reviewer identity, route scope, sign-off time, and blocked dispatch attempts
- Audit and hold-tracking services preserving packet supersession, missing-follow-up holds, protected-routing decisions, and override history

## Why this instance matters

This instance shows how severe compliance monitoring can require an explicit approval-bound dispatch step that still belongs in `monitor-detect-triage`. The difficult work here is not medical judgment or regulator-facing action; it is governing whether an already-triaged serious-signal packet may cross into a protected expedited-review lane without losing hold state, packet version control, or routing discipline. The example keeps the family boundary strict by stopping at the approved review-lane release rather than safety assessment, report submission, or broader response coordination.

## Likely architecture choices

- Event-driven monitoring fits because follow-up narratives, duplicate links, and reporting-clock state can change while the packet is waiting for dispatch approval.
- Approval-gated execution fits because the packet is technically ready for expedited review but must remain blocked until a qualified safety reviewer authorizes the precise dispatch boundary.
- Human-in-the-loop review should remain mandatory because releasing the packet into expedited medical review changes who can act next, even though the workflow still does not decide the medical or regulatory response.
- The workflow should emit only the dispatched review-lane entry, dispatch manifest, hold register, and audit trail rather than a causality conclusion, filing recommendation, or communication draft.

## Governance notes

- The dispatch manifest should bind the approved packet version, protected review lane, reviewer identity, and any still-visible holds so downstream teams do not inherit stale or broadened authority.
- Dispatch should remain blocked when follow-up freshness expires, duplicate merges remain unresolved, or the packet would expose more patient detail than the approved expedited lane permits.
- Queue views should minimize patient identifiers, reporter details, and site-sensitive information while preserving traceable references in controlled safety systems.
- Safety-governance owners must approve changes to qualified reviewer roles, lane definitions, reporting-clock handling, and dispatch-hold criteria; the workflow ends before causality review, regulatory submission, or case closure.

## Evaluation considerations

- Median time from serious-signal packet readiness to approved expedited-review dispatch or explicit hold
- Rate of post-dispatch corrections caused by stale follow-up state, wrong packet revision, or protected-routing mismatch
- Completeness of audit lineage linking packet version, reviewer sign-off, and expedited lane release
- Reliability of blocked-dispatch behavior when medically significant follow-up information arrives during the approval window
