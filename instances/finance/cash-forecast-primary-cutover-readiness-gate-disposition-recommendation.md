# Cash forecast primary cutover readiness gate disposition recommendation

## Linked pattern(s)

- `readiness-gate-disposition-recommendation`

## Domain

Finance.

## Scenario summary

A treasury transformation steering group is reassessing whether a new cash-forecast workflow can pass its shadow-to-primary cutover gate before quarter-close liquidity planning begins. Since the prior review, one business unit's reconciliation variance remains above tolerance, a control-attestation packet aged past the freshness limit set by policy, and a narrower regional rollout path became feasible if the organization defers two lower-volume entities. The workflow must recommend whether finance should proceed with the primary cutover as scoped, hold for refreshed evidence, narrow the go-live to the validated regional subset, or escalate because variance, control-completeness, and delegated cutover thresholds no longer fit local authority before any system-of-record switch occurs.

## Target systems / source systems

- Treasury program tracker, cutover gate checklist, and delegated finance authority matrix
- Cash-forecast shadow run history, reconciliation dashboards, and model validation evidence store
- Control-attestation repository, segregation-of-duties policy references, and exception register
- Quarter-close calendar, liquidity planning deadlines, and prior cutover review records
- Regional entity onboarding status, data-quality issue tracker, and downstream reporting dependency map

## Why this instance matters

This instance grounds the pattern in finance where the main challenge is not executing the cutover or drafting an approval memo. The value is refreshing a governed readiness disposition as reconciliation evidence, control attestations, and deadline pressure evolve, so treasury leaders see whether a full go-live, narrower launch, hold, or escalation is defensible.

## Likely architecture choices

- Event-driven monitoring fits because reconciliation variance movements, attestation expiry, and quarter-close timing changes should trigger a refreshed readiness recommendation instead of relying on static gate packets.
- Human-in-the-loop review is mandatory because the workflow should advise on the cutover disposition, not change the primary system of record, finalize treasury reporting, or waive control requirements.
- Read-only integration with treasury planning, validation, control, and policy systems is preferable so the agent cannot silently convert a recommendation into a live finance process change.

## Governance notes

- The output should distinguish full-cutover paths, narrower regional go-live paths, hold conditions tied to stale or incomplete evidence, and escalation triggers linked to authority or control thresholds.
- Any narrow recommendation should show which entities remain out of scope, what residual variance or control risk remains, and what evidence would be required to expand later.
- Freshness breaches on control attestations, unresolved reconciliation tolerances, or cutover timing that would compress quarter-close governance should trigger explicit escalation rather than deadline-weighted scoring alone.
- Treasury assumptions, control evidence, and entity-level variance detail should remain visible only to authorized finance, controllership, risk, and audit reviewers under normal confidentiality controls.
- Recommendation packets should preserve evidence versions, blocker deltas, and reviewer comments used so steering-group members can later audit why the cutover was advanced, narrowed, held, or escalated.

## Evaluation considerations

- Reviewer agreement with the recommended cutover disposition before any primary-system switch is authorized
- Rate at which stale attestation evidence, unresolved variances, or authority-threshold breaches are surfaced before quarter-close commitments are made
- Quality of evidence linking reconciliation state, control completeness, and deadline pressure to the readiness recommendation
- Stability of recommendations when shadow-run accuracy, attestation freshness, or entity onboarding status changes during the final gate window
