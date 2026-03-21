# Cold-chain temperature excursion alert triage

## Linked pattern(s)

- `risk-alert-triage`

## Domain

Operations.

## Scenario summary

A cold-chain operations center monitors live temperature, door-open, location, and power-status telemetry from refrigerated trailers, depots, and pharmacy storage units carrying temperature-sensitive products. The workflow must separate sensor chatter and transient blips from excursions that may threaten product quality, enrich alerts with route stage, shipment criticality, equipment service history, and prior exception context, and then route the most consequential cases to the right response queue. The emphasis is on continuous watching, explainable severity ranking, and human-gated escalation into quarantine, maintenance, or customer-notification decisions rather than on executing those downstream actions automatically.

## Target systems / source systems

- IoT telemetry pipeline for temperature probes, door sensors, compressor status, battery health, and connectivity-loss events
- Transportation-management or warehouse-management system with shipment contents, lane milestones, facility ownership, and customer commitments
- Equipment-maintenance history showing recent sensor calibrations, refrigeration faults, prior excursion incidents, and open service tickets
- Product master and quality rules defining allowable excursion ranges, hold times, product sensitivity tiers, and site-specific handling requirements
- Incident or exception-management queue used by cold-chain operations, quality assurance, depot supervisors, and field maintenance teams
- Audit log and evidence store preserving raw telemetry windows, deduplication decisions, routing rationale, and human escalation approvals

## Why this instance matters

This grounds the pattern in an operations environment where a large share of incoming alerts are noisy, correlated, or short-lived, yet a real missed excursion can create spoilage, patient risk, or contractual loss. Static thresholds are not enough because severity depends on context such as whether the excursion happened during loading, how long connectivity was lost, whether the same unit is already under watch, and what products are on board. The instance cleanly fits monitor/detect/triage because it stops at making a defensible response queue and evidence packet, leaving quarantine releases, shipment diversion, maintenance dispatch, and customer communications to later human-controlled workflows.

## Likely architecture choices

- Event-driven monitoring should continuously evaluate telemetry streams, reopening or merging cases as sensor conditions change and as the same asset emits repeated threshold breaches.
- Human-in-the-loop review should remain embedded for high-severity excursions, disputed sensor-health situations, and any recommendation that could trigger product hold, disposal, or customer-facing escalation.
- A tool-using single agent can correlate signals across sensors on the same asset, suppress obvious duplicate chatter, attach shipment and maintenance context, and publish a prioritized queue with explainable severity bands and routing suggestions.
- Approval-gated escalation should keep the agent from independently placing inventory on hold, rerouting vehicles, or notifying external parties; it can prepare the case packet and recommended queue destination, but a supervisor or quality reviewer should authorize consequential next steps.

## Governance notes

- Deduplication should preserve lineage from raw sensor events to the merged alert so reviewers can see whether repeated threshold breaches were treated as one unfolding excursion or several separate incidents.
- Calibration state, connectivity gaps, and known hardware faults should be explicit in the triage packet so the workflow does not over-trust a noisy probe or hide a true excursion behind presumed sensor error.
- Privacy and commercial sensitivity controls should limit exposure of customer names, product SKUs, and exact shipment locations in broad routing views while retaining detailed evidence in restricted audit stores.
- Reversibility should be designed into the queueing layer: severity scores, merge decisions, and routing recommendations can be recomputed as telemetry stabilizes, but once a shipment sits too long in an unreviewed excursion state the product-loss window may close, so ambiguous cases should escalate quickly to human review.
- Override, suppression, and escalation actions should be immutably logged so post-incident review can distinguish justified noise suppression from control failures that delayed response to a genuine cold-chain breach.

## Evaluation considerations

- Recall of materially significant temperature excursions or equipment failures that should have reached rapid human review
- Reduction in duplicate-alert load and reviewer interruptions from transient telemetry noise without increasing missed true excursions
- Median time from first relevant signal to a prioritized alert packet containing telemetry evidence, shipment context, and routing rationale
- Reviewer override rate for cases where the triage workflow misread sensor-health context, over-merged distinct incidents, or under-ranked product-critical shipments
- Ability to reconstruct every suppression, merge, and escalation decision during quality audits, spoilage investigations, or customer-claim review
