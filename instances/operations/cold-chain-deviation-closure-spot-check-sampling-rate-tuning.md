# Cold-chain deviation closure spot-check sampling-rate tuning

## Linked pattern(s)

- `adaptive-review-sampling-rate-tuning`

## Domain

Operations.

## Scenario summary

A regulated distribution quality team performs spot checks on cold-chain deviation closure packets — the governed artifacts that formally close temperature excursions, humidity breaches, and transport delay events affecting pharmaceutical or perishable goods. Each packet bundles the root-cause investigation record, corrective-action evidence, product-impact assessment, and sign-off trail required for regulatory submission and customer audit. The current fixed sampling policy treats all closed deviation packets equally, under-covering high-escape cohorts such as multi-leg carrier events, out-of-specification edge cases with product released under exception, and sites where prior regulatory findings were clustered. The workflow must autonomously retune bounded spot-check sampling rates so closure-packet cohorts with higher escape risk or greater quality-finding yield receive more oversight, while keeping protected floors for submission-visible deviations, respecting auditor and quality-specialist capacity, minimizing copied patient-adjacent or proprietary logistics detail, and preserving a fast rollback path when the loop risks overreacting to a short spike in findings after a seasonal disruption.

## Target systems / source systems

- Quality policy store with active closure-packet sampling rates, protected deviation classes, prior policy versions, and rollback snapshots
- Deviation management system with closed-packet metadata: deviation type, severity tier, carrier identifier, site, product class, release disposition, and exception flags
- Quality-review findings history covering documentation gaps, corrective-action deficiencies, investigator override decisions, and regulatory-observation linkages discovered during later inspections
- Auditor and quality-specialist capacity register covering available spot-check reviewers, restricted-product annexes, and current backlog
- Governance and change-control workspace used by the qualified person or quality director to inspect sampled tuning runs, freeze autonomous adjustments, and restore the last trusted sampling policy

## Why this instance matters

This grounds the pattern in a regulated operations context that is materially different from the existing maintenance-documentation example. The surface being tuned is the closure-packet spot-check coverage policy, not work-order documentation. The hard boundary stays clear: the workflow does not reopen deviations, alter release dispositions, schedule auditor visits, or communicate with regulators; it only determines how much future quality-review coverage different closure-packet cohorts should receive. That keeps the main deliverable a bounded, reversible sampling-policy revision with its change record and freeze-or-rollback packet — the correct artifact family for optimize/adapt.

## Prerequisite policy and operating state

- A current approved sampling policy with per-cohort base rates and protected-class floors must exist in the quality policy store before the tuning loop is activated.
- The loop operates only in steady-state regulatory periods; it is frozen by default whenever a site is under active regulatory inspection or a triggered recall investigation is open.
- Review-findings data must cover at least the most recent full audit cycle to produce statistically stable cohort yield estimates before any autonomous rate change is committed.
- The qualified person or quality director has explicitly delegated bounded in-policy adjustments and has reviewed the initial tuning parameters.

## Source precedence

1. Quality policy store (active rates, protected floors, rollback snapshots) — primary authority
2. Deviation management system (closed-packet cohort metadata and disposition flags) — population data
3. Quality-review findings history (yield signals, override records, regulatory linkages) — signal data
4. Auditor capacity register (reviewer availability and backlog pressure) — constraint data
5. Governance workspace audit trail (prior tuning decisions, freeze events) — lineage and accountability record

Conflicts between the quality policy store and the findings history are resolved by human review; the loop surfaces the discrepancy and holds the affected cohort at its current rate until the qualified person or quality director approves a resolution.

## Accountable human owner

**Quality Director, Distribution Operations** — holds delegated authority to approve sampling-policy changes, freeze or unfreeze the autonomous loop, order backfill review sweeps, and restore the prior trusted policy from a rollback snapshot. No rate change below a protected floor may be committed without a recorded override from this role.

## Visible blockers and unresolved items

- Cohorts containing closed deviations with product released under an active exception hold are flagged and held at their current rate until the exception is cleared or a supervisor override is recorded.
- Sites with fewer than the minimum qualifying closure packets in the evaluation window are excluded from autonomous rate changes; their rates remain at the protected floor pending a manual review.
- Any cohort where the tuning signal is dominated by a single high-severity event is quarantined with a cooldown flag; the loop notes the instability and defers the move until the next stable window.
- Carrier-specific cohorts where a new logistics partner has fewer than two audit cycles of closure-packet history remain locked at the protected onboarding floor.

## Revision lineage

Each committed sampling-policy revision is recorded as a versioned snapshot in the quality policy store with the following fields: evaluation window dates, cohort-level yield signals, capacity assumptions, moves proposed, moves blocked with reasons, moves committed, prior rates, new rates, and the identity of any human overrides. The governance workspace displays the full lineage from the initial approved policy through each tuning cycle so any auditor can reconstruct the rationale for current coverage levels.

## Likely architecture choices

- Event-driven monitoring should trigger reevaluation when quality-review findings cluster around a carrier, deviation type, or site, when seasonal disruption events inflate short-term finding rates, or when auditor capacity drops materially due to scheduled inspection commitments.
- A tool-using single agent can compute bounded sampling moves, enforce protected-class floors and reviewer-load ceilings, write the versioned policy update, and append the structured change record.
- Autonomous-with-audit fits because in-policy spot-check coverage changes can apply automatically, while the quality director reviews sampled tuning cycles and freezes the loop when regulatory inspection periods or regime changes make recent signals unreliable.
- Human owners must remain able to roll back to any prior policy snapshot, order a temporary backfill sweep for an under-reviewed cohort, and record override justifications for audit submission.

## Governance notes

- Submission-visible deviations, product classes subject to expedited regulatory reporting, and onboarding-period carrier cohorts must maintain protected minimum coverage that autonomous tuning cannot reduce below the approved floor.
- Audit records must capture cohort-level yield signals, reviewer-capacity assumptions, blocked moves with reasons, cooldown flags, and the identity and justification of any human override — all in a form suitable for regulatory inspection.
- Closed-packet metadata used in tuning must remain at aggregated cohort level; patient-adjacent product detail, proprietary carrier routing, and investigation narratives must not be copied into general tuning logs unless a restricted annex is required by the quality director.
- The workflow must not reopen deviation records, alter product release dispositions, schedule auditor or inspector visits, or send external communications; it only updates the governed spot-check coverage policy for future closure-packet reviews.

## Evaluation considerations

- Change in meaningful quality-finding yield per auditor review hour after tuned sampling rates are applied to closed closure-packet cohorts
- Rate of escaped documentation gaps or corrective-action deficiencies discovered in later regulatory inspections or customer audits following a cohort coverage decrease
- Frequency of quality-director freezes, backfill sweeps, or rollbacks indicating the loop is misreading seasonal disruption spikes or sparse-data cohorts
- Reviewer-load stability across protected deviation classes, carrier cohorts, and sites during high-volume seasonal disruption periods
- Absence of unauthorized rate reductions below protected floors for submission-visible or exception-released deviation cohorts
