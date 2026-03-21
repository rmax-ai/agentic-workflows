# Executive offer-exception recommendation packet revision approved for compensation committee decision lane

## Linked pattern(s)

- `approval-gated-recommendation-release`

## Domain

HR.

## Scenario summary

An executive recruiting workflow has already prepared one exact recommendation packet revision for a senior-leader offer exception. The packet narrows the bounded options to release a capped sign-on plus relocation exception package, release a narrower in-band compensation mix with deferred equity treatment, or escalate to the chief people officer for broader review, and it keeps blocked requests such as guaranteed severance, an off-cycle level change, or open-ended housing support explicit. Before that exact packet revision can enter the restricted compensation committee decision lane, a named total-rewards release owner must approve the committee scope, validity window, and release manifest so committee members receive the governed recommendation artifact rather than a stale or redistributed copy. The workflow stops at governed release of that packet revision; it does not decide which offer exception is approved, issue the offer letter, or communicate terms to the candidate.

## Target systems / source systems

- Executive offer-exception workspace holding the current recommendation packet revision, bounded option set, blocked-term rationale, and superseded drafts
- Applicant-tracking, compensation-band, internal-equity, relocation-policy, and precedent records already cited by the recommendation packet
- Governance repository defining the named compensation committee lane, authorized recipients, release expiry, and the human owner who may approve packet release
- Approval manifest and committee-routing tooling that records the exact packet hash, committee audience, and any blocked forwarding attempts outside the approved lane
- Audit and supersession ledger used to hold older packet revisions when candidate demands, internal-equity context, or policy scope changes before committee review

## Why this instance matters

This grounds the pattern in HR where the governance problem is not to adjudicate the exception package, but to control release of one bounded recommendation artifact into one human decision lane. Executive-offer packets can shift late as candidate asks change, internal-equity comparisons refresh, or relocation and tax constraints narrow viable terms, so approval must stay tied to one reviewed revision rather than to a vague permission to keep circulating compensation advice. The example keeps the family boundary clear by ending at compensation-committee handoff rather than offer adjudication, candidate communication, or downstream execution in HR systems.

## Likely architecture choices

- Approval-gated execution fits because the recommendation packet remains held until a named total-rewards owner authorizes release into the compensation committee decision lane.
- Human-in-the-loop review remains necessary because only accountable HR and compensation leaders should confirm audience scope, expiry, and blocked-term visibility without collapsing the workflow into offer approval itself.
- A governed agent can compare packet hashes, assemble the manifest, and block broadened distribution, but it should not approve compensation exceptions, issue the offer letter, or update HR systems with candidate terms.

## Governance notes

- Approval should bind to one immutable packet revision, one named compensation committee lane, one bounded validity window, and one exact option set so later edits cannot inherit release authority silently.
- Blocked terms such as guaranteed severance, off-cycle leveling, or open-ended relocation support should remain visible in the released packet rather than being compressed into a cleaner executive-offer summary.
- If candidate asks, internal-equity evidence, or committee scope changes during approval review, the pending packet should be held and superseded rather than routed under stale approval.
- Audit records should preserve the released packet id, option-set hash, approver identity, committee-recipient scope, expiry timing, and any blocked redistribution attempts.

## Evaluation considerations

- Percentage of compensation-committee releases where the offer-exception recommendation packet revision, option-set hash, and manifest metadata align exactly without later correction
- Rate at which superseded or stale executive-offer recommendation packets are blocked before committee review
- Time required to move from packet-ready status to approved bounded committee release when equity, policy, and relocation evidence are complete
- Reviewer correction rate for missing blocked terms, wrong audience scope, or stale-state handling after the committee receives the released recommendation packet
