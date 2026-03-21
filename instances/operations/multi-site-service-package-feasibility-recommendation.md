# Multi-site service package feasibility recommendation

## Linked pattern(s)

- `deal-desk-recommendation-support`

## Domain

Operations.

## Scenario summary

An operations services desk is reviewing a proposed support package for a retail chain that wants accelerated rollout across forty locations, weekend installation windows, tighter onsite response SLAs for its busiest sites, and dedicated spare-parts staging before quarter end. The workflow must recommend whether operations should support the package as scoped, counter with a phased or narrower service mix, or escalate because field capacity, subcontractor spend, inventory commitments, and exception thresholds move outside normal approval bands.

## Target systems / source systems

- CRM opportunity record, draft services package, and customer rollout assumptions
- Capacity-planning model, technician skill matrix, and regional coverage forecasts
- Field-service history, subcontractor rate cards, and overtime or travel policy thresholds
- Spare-parts inventory position, supplier lead-time data, and staging-cost estimates
- Approval matrix, prior exception register, and implementation-risk notes from operations leadership

## Why this instance matters

This instance grounds the recommendation pattern in operations where the decision is not about quoting alone. The hard part is turning delivery capacity, spend exposure, and rollout risk into a defensible recommendation before the business commits to a package that operations may not be able to deliver safely or predictably.

## Likely architecture choices

- A recommendation-only workflow can retrieve demand assumptions, staffing coverage, subcontractor cost exposure, inventory readiness, and precedent exceptions into one ranked option set for operations review.
- Human-in-the-loop review is mandatory because the workflow should advise on feasible package shapes and escalation paths, not approve service commitments or launch the rollout.
- Read-only integration with CRM, workforce-planning, inventory, and approval systems is preferable so the agent cannot convert a recommendation into booked work, purchase commitments, or customer-facing promises.

## Governance notes

- The output should distinguish in-band options, conditional options that depend on staffing or inventory assumptions, and blocked options that breach service, spend, or risk thresholds.
- Any recommendation that relies on precedent should show whether the earlier case matched site count, geography, peak-season timing, subcontractor dependence, and SLA commitments.
- Requests that would exceed delegated approval for overtime, subcontractor spend, inventory prebuild, or rollout compression should trigger explicit escalation rather than weighted scoring alone.
- Customer rollout plans, margin-sensitive cost assumptions, and vendor pricing should remain visible only to authorized commercial and operations reviewers under normal confidentiality controls.
- Recommendation packets should preserve the assumptions, thresholds, and reviewer comments used so leaders can audit why a package was supported, narrowed, or escalated.

## Evaluation considerations

- Reviewer agreement with the recommended package shape and escalation route before any service commitment is approved
- Rate at which staffing, inventory, or subcontractor blockers are surfaced before launch promises reach the customer
- Quality of evidence linking capacity forecasts, spend thresholds, and prior exceptions to the recommendation
- Stability of recommendations when site count, go-live timing, or SLA expectations change late in review
