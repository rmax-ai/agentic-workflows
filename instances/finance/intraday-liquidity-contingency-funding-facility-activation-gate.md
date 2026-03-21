# Intraday liquidity contingency funding facility activation gate

## Linked pattern(s)

- `contingency-plan-activation-gate`

## Domain

Finance.

## Scenario summary

After a severe payment-rail disruption, treasury leadership has already declared the contingency scope and identified the committed fallback path: a governed intraday funding facility activation that would protect priority payment obligations if the normal liquidity position does not recover before market-open deadlines. Upstream workflows have already restored the trusted cash picture and routed the correct authority lane. The planning workflow now has to assemble one activation-ready packet showing collateral readiness, lender notice windows, dual-control staffing, protected payment-queue holds, and market-open communication constraints. It should keep explicit holds for any missing lender callback, collateral shortfall, or control-coverage gap, and stop at the human approval gate rather than drawing the facility, releasing payments, or re-arguing whether the contingency should exist.

## Target systems / source systems

- Treasury continuity playbook and bridge workspace with the declared fallback scope, prior gate packets, and protected liquidity thresholds
- Trusted cash-state, collateral, and payment-priority systems already designated as authoritative inputs for contingency preparation
- Lender notice trackers, delegate rosters, calendars, and control-review schedules for treasury, risk, controllership, and executive coordination
- Approval-routing and audit systems that record packet versions, open holds, and human sign-off before any funding fallback can begin
- Restricted communication-planning tools for market-open and lender-facing timing windows

## Why this instance matters

This grounds the pattern in finance where the hard problem is not deciding whether to draw the facility or executing the draw mechanics. The hard problem is keeping one approval-gated readiness packet current as collateral, staffing, and lender-window constraints shift under pressure. It shows why contingency planning deserves a separate slice from truth restoration, authority recommendation, and staged execution: treasury leaders need a disciplined activation gate artifact before any liquidity fallback can be approved safely.

## Likely architecture choices

- Approval-gated execution fits because the packet may be technically activation-ready while the facility draw remains concretely blocked until treasury leadership signs off.
- The workflow should preserve one readiness ledger tying collateral checkpoints, lender windows, control coverage, and protected payment holds to the latest packet version.
- Explicit holds should remain visible whenever callback windows, dual-control staffing, or queue protections are incomplete rather than being compressed into a nominally ready packet.
- The workflow should stop at the approval packet and hold register rather than recommending a different funding authority, revalidating the cash-state truth, or initiating the facility draw.

## Governance notes

- Protected prerequisites such as collateral sufficiency, lender-notice timing, dual-control staffing, and payment-priority safeguards should be encoded as non-waivable holds in the packet.
- Broad coordination packets should expose timing, readiness, and hold state without copying sensitive account, counterparty, or strategy detail outside restricted treasury channels.
- Human treasury ownership is required before the packet becomes the authoritative basis for any liquidity fallback activation.
- Repeated packet revisions should preserve append-only lineage so audit and risk teams can reconstruct exactly which upstream references and holds changed before approval.

## Evaluation considerations

- Time from updated liquidity contingency request to a human-reviewable funding-facility activation packet with complete prerequisite and hold state
- Percentage of lender-window, collateral, or staffing blockers kept explicit in the hold register rather than hidden in a green status summary
- Agreement between the workflow's packet and the final human-approved activation gate used for downstream liquidity fallback
- Stability of the readiness packet when lender availability, collateral status, or payment-priority protections change within the same market-open cycle
