# Distribution sorter misroute root-cause investigation

## Linked pattern(s)

- `incident-root-cause-analysis`

## Domain

Operations.

## Scenario summary

After a regional fulfillment hub has already declared an incident for a spike in parcel misroutes during an overnight sort wave, network operations must determine why cartons bound for three destination zones were repeatedly diverted to the wrong outbound lanes. The leading explanations conflict: a stale destination-lookup table may have remained active after a routing update, diverter timing may have drifted after a maintenance intervention, barcode image quality may have degraded because of dust buildup on the tunnel scanners, or supervisors may have authorized a temporary manual recirculation workaround that bypassed normal scan confirmation. The workflow reconciles controls logs, scan evidence, maintenance history, and human shift notes into a defensible explanation of what failed, what remains uncertain, and which follow-up checks still matter before leadership commits to remediation or customer-facing statements.

## Target systems / source systems

- Warehouse control system routing tables, wave-release configuration history, and sort-plan change records
- PLC and conveyor controls logs showing diverter actuations, jam-clear resets, and safety-stop events
- Inline scanner image-quality metrics, barcode-read exception logs, and retained parcel-track images for the incident window
- Warehouse-management system shipment assignments, lane manifests, and misroute exception cases
- CMMS work orders, technician notes, and parts-replacement history for the affected sorter zone
- Shift-manager bridge notes, radio logs, and supervisor handoff records documenting manual operating changes

## Why this instance matters

This grounds `incident-root-cause-analysis` in an operations workflow where the main task is not detecting the misroute spike but reconciling fragmented facility evidence well enough to explain it. Sortation incidents often blend automation behavior, recent maintenance, local workarounds, and incomplete parcel-level evidence, so a single plausible story can be dangerously wrong. The instance shows why explicit competing hypotheses, evidence provenance, and human-owned downstream decisions are essential before a site declares the equipment stable, restarts deferred waves, or makes service-recovery commitments.

## Likely architecture choices

- An orchestrated multi-agent design can separate controls-log retrieval, parcel-level timeline reconstruction, and hypothesis verification while preserving one shared investigation record.
- Shared case memory should keep competing explanations visible, including evidence that supports or weakens each one, rather than collapsing early onto the first credible cause.
- Human-in-the-loop review remains necessary before declaring the primary root cause, deciding whether the sorter can be returned to normal operating mode, or authorizing customer-commitment updates tied to shipment recovery.

## Governance notes

- Preserve provenance for every claimed causal link by retaining references to the exact routing-table version, PLC event sequence, scanner evidence, maintenance note, or supervisor log that supports it.
- Distinguish observed facts from inferred causes; for example, a jam-clear reset near the incident window should not be treated as proof of diverter fault unless parcel-flow and actuation evidence corroborate it.
- If evidence remains incomplete or hypotheses stay unresolved, the workflow should surface that uncertainty explicitly instead of implying the sorter is safe, stable, or fully understood.
- Remediation approval, safety declarations for returning equipment to service, incident-command decisions about lane shutdowns, and customer or carrier commitments must remain human-owned.
- Investigation artifacts should retain rejected hypotheses, human overrides, and timeline-normalization choices so post-incident review can replay how the conclusion was reached.

## Evaluation considerations

- Time to first defensible hypothesis set with cited controls, scanner, maintenance, and operator evidence
- Completeness of the reconciled parcel-and-equipment timeline across routing updates, diverter events, jam clears, and manual workarounds
- Agreement between the workflow's ranked explanations and the final operations-accepted root cause
- Rate at which unresolved uncertainty, conflicting evidence, or missing parcel traces are surfaced before remediation or service-recovery decisions are approved
