# Field-service dispatch queue reprioritization

## Linked pattern(s)

- `queue-prioritization-optimization`

## Domain

Operations.

## Scenario summary

An operations dispatch supervisor for a regional utility service network needs to retune the live field-service work-order queue after an early-summer storm causes a surge of transformer inspections, downed-line assessments, meter-restoration visits, and routine preventive work. The dispatch platform already tracks outage impact, customer vulnerability flags, crew certifications, travel time, and appointment commitments, but the current ordering no longer fits the day because two line crews are offline, one district is under heat-safety restrictions, and yesterday's rush decisions created repeat visits for partially diagnosed equipment faults. The optimization workflow must reprioritize the queue so urgent restoration and safety work rises appropriately while preserving fairness for stranded low-income neighborhoods, bounded travel assumptions, and non-waivable safety constraints on who can be dispatched where.

## Target systems / source systems

- Field-service dispatch platform with open work orders, outage linkage, customer commitments, and current queue ranking
- Workforce and crew-qualification system showing certifications, shift limits, truck capability, and current location
- Historical dispatch outcome store with repeat-visit rates, missed appointment data, supervisor overrides, and restoration outcomes
- Weather, road-closure, and heat-safety feeds that change travel feasibility and allowable work conditions during the shift
- Dispatch audit dashboard used by supervisors to review tuning changes, freeze automation, and roll back to the last trusted policy

## Why this instance matters

This grounds the optimization pattern in an operations setting where queue order affects safety exposure, restoration speed, and equitable service delivery rather than only ticket throughput. A naive optimizer could keep chasing shortest travel time or fastest closure, leaving medically vulnerable customers waiting, overloading certified crews, or pushing technicians into unsafe heat conditions. The instance makes the adaptation loop concrete: it can learn from repeat visits and override history, but only inside explicit safety, fairness, and rollback boundaries.

## Likely architecture choices

- Event-driven monitoring should trigger queue reevaluation when storm-related work spikes, crews go offline, weather constraints change, or supervisors repeatedly override the current dispatch order.
- A tool-using single agent can recompute bounded prioritization weights, publish a revised ranked dispatch queue with rationale, and simulate the impact on crew utilization and appointment risk before changes go live.
- Exception-gated autonomy fits because in-policy tuning can update dispatch sequencing automatically, but larger shifts that change protected-priority handling, district fairness balance, or safety buffers should require supervisor approval.
- Human dispatch leads should remain able to freeze optimization updates, restore the last trusted ranking policy, and assign work manually when field conditions become too unstable for feedback signals to be trusted.

## Governance notes

- Downed-line hazards, life-safety restoration work, and jobs requiring scarce certifications should remain protected classes that cannot be demoted for efficiency or route-density reasons.
- The optimization log should capture which outcome signals, staffing changes, weather constraints, fairness checks, and supervisor overrides drove each reprioritization so post-shift review can separate justified adaptation from metric chasing.
- Fairness checks should look for repeated deferral of lower-revenue or harder-to-reach neighborhoods during storm recovery instead of silently optimizing toward the easiest service territory.
- Rollback paths should be explicit: if repeat-visit rates rise, crews exceed safe heat exposure assumptions, or supervisors reject the new order at a high rate, the workflow should revert to the prior trusted policy and flag the tuning packet for review.

## Evaluation considerations

- Reduction in unsafe dispatch assignments, repeat truck rolls, and missed restoration commitments after tuned queue ordering is applied
- Change in wait time and completion equity across districts, especially for vulnerable-customer and historically under-served service areas
- Frequency of supervisor overrides that indicate the optimized ranking violated safety, fairness, or field-context expectations
- Speed and clarity of rollback when updated tuning degrades dispatch stability or conflicts with new storm-response guidance
