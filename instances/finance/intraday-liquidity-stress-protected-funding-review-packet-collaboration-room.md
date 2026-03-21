# Intraday liquidity stress protected funding review packet collaboration room

## Linked pattern(s)

- `critical-protected-artifact-collaboration`

## Domain

Finance.

## Scenario summary

During a declared intraday liquidity stress event, treasury opens a restricted collaboration room around one protected funding review packet that will later support human contingency decisions. An assistant treasurer owns the artifact while agents help merge updated cash-position evidence, controller objections, disputed exposure language, and market-sensitive annex schedules into one shared packet. The collaboration loop keeps the main narrative, contested assumptions, and restricted annex boundaries synchronized as treasury, finance, and risk reviewers argue over funding-window wording, covenant implications, and what can safely leave the room. The human artifact owner remains responsible for deciding whether the packet is ready for the next bounded handoff and whether unresolved disagreement is acceptable to carry forward, while actual authority routing, contingency selection, and funding actions stay outside the workflow.

## Target systems / source systems

- Restricted treasury collaboration room with the funding review packet, disagreement ledger, annex references, and human release-state record
- Intraday liquidity and treasury ledgers with current balances, facility availability, collateral state, and payment timing pressure
- Market-sensitive annex repository with scenario schedules, counterparty exposure tables, and confidential funding assumptions
- Finance-control, risk-policy, and delegation repositories defining what the packet may contain and which human must release it onward
- Audit systems capturing packet revisions, annex access, residual-objection acceptance, and protected distribution events

## Why this instance matters

This grounds the pattern in a finance workflow where the main value is keeping one severe shared packet inspectable despite live objections and highly sensitive annex material. The room is not ranking authorities or choosing a funding strategy; it is maintaining artifact integrity, ownership, and release discipline so later human workflows start from one honest shared record. It highlights why critical collaboration differs from briefing-only synthesis: the packet is jointly rewritten over several turns, with disagreement and access scope preserved instead of compressed away.

## Likely architecture choices

- Human-in-the-loop collaboration should remain primary because only accountable treasury and finance leaders can decide whether disputed language, confidential annex exposure, and release timing are acceptable.
- An orchestrated multi-agent setup fits when separate agent roles refresh liquidity evidence, compare wording changes, track annex sensitivity, and maintain the protected trace across successive updates.
- Agents may update schedules, reconcile comments, and surface held-state causes, but selecting the authority lane, opening market communications, or initiating funding operations should remain explicitly human-gated and external to the room.

## Governance notes

- The packet should clearly separate verified cash-state facts, disputed interpretation, market-sensitive annex content, and human-accepted release conditions so later reviewers can inspect the record honestly.
- Every material statement about funding pressure, covenant headroom, payment timing, or facility prerequisites should link to current treasury evidence or remain marked as contested.
- Market-sensitive schedules and counterparty exposure detail should remain in restricted annexes with tightly logged access and explicit promotion rules.
- The handoff-readiness state should show the named human owner, remaining blockers, accepted residual disagreement, and which downstream workflow may consume the packet next.
- If new evidence changes the stress scope materially or makes the packet audience unsafe, the room should revert to held state rather than quietly broadening distribution.

## Evaluation considerations

- Time to maintain one handoff-ready protected packet while liquidity evidence, objections, and annex content continue to change
- Rate at which downstream finance or risk reviewers identify hidden disagreement, stale treasury data, or over-broad disclosure after packet release
- Consistency between the main packet, annex map, and human readiness state across repeated revisions
- Frequency with which humans reject agent edits because they implied funding choices, authority recommendations, or operational commitments beyond collaboration scope
