# Intercompany netting settlement mismatch investigation

## Linked pattern(s)

- `incident-root-cause-analysis`

## Domain

Finance.

## Scenario summary

At monthly close, the corporate netting center for a multinational industrial group reports that three entity pairs in the EMEA–APAC cross-currency netting pool have unresolved settlement mismatches totalling €2.1 million equivalent. Each pair submitted netting confirmations on time, but the netting engine's consolidated settlement instruction does not match the position that one or both entities carry in their ERP subledger. The discrepancy could stem from an FX-rate divergence between the netting center's agreed interday rate and the entity booking rates, a late intercompany payable captured in one entity's final submission but not yet mirrored in the counterparty's system, a duplicate instruction that was re-submitted after a network timeout during the netting window, or a rounding difference introduced when the netting engine applied a cross-currency conversion rule that one entity's ERP applies at a different precision. The investigation reconciles netting-engine output, entity subledger positions, submission logs, and operations notes into an evidence-backed explanation of which entity pair contributed each component of the break, what each candidate cause predicts, and which checks remain open before a human-owned decision on settlement instruction correction or dispute escalation can proceed. Kai Brandt, Head of Intercompany Operations, is the named human owner of this investigation packet.

**Prerequisite state that must be confirmed before narrowing hypotheses:**
- Netting cycle has reached final-submission cutoff and no further entity resubmissions are pending.
- FX reference-rate publication for the netting window is complete and the authoritative interday rate is locked in the netting engine.
- Entity ERP subledger snapshots for the netting date have been extracted and timestamped; no retroactive journal postings to the intercompany accounts are in progress.
- Any prior-cycle carry-over disputes or unmatched credits from the preceding netting run have been documented as in-scope or explicitly excluded.

```mermaid
flowchart TD
    A["Netting engine settlement instruction<br>does not match one or both entity subledger positions<br>for three EMEA–APAC entity pairs"]
    B["Extract netting-engine output, entity subledger positions,<br>submission logs, and operations notes;<br>confirm prerequisite state is satisfied"]
    C["Normalize timestamps and FX-rate<br>references across netting engine,<br>ERP extracts, and submission logs"]
    D{"All entity submissions and<br>subledger snapshots present<br>and timestamped?"}
    E["Hold hypothesis narrowing;<br>document missing or incomplete artifacts<br>with cited entity and system"]
    F["Test hypothesis 1:<br>FX-rate divergence between entity booking<br>rate and netting-center agreed rate"]
    G["Test hypothesis 2:<br>late intercompany payable present in<br>one entity submission but not mirrored<br>by counterparty"]
    H["Test hypothesis 3:<br>duplicate instruction re-submitted after<br>network timeout during netting window"]
    I["Test hypothesis 4:<br>cross-currency rounding rule applied<br>at different precision in netting engine<br>vs. entity ERP"]
    J["Compare supporting and disconfirming evidence<br>across all four hypotheses;<br>attribute each break component to<br>a candidate cause or flag as unresolved"]
    K{"Each break component attributed<br>to one evidence-backed cause with<br>cited supporting artifacts?"}
    L["Document residual uncertainty,<br>unmatched break components,<br>and pending verification checks"]
    M["Produce investigation packet:<br>ranked causal attribution per entity pair,<br>unresolved items, source-precedence register,<br>and recommended follow-up checks"]
    N["Escalate to Kai Brandt (Head of Intercompany Operations)<br>for human-owned settlement correction decision,<br>dispute escalation, or supervised resubmission"]

    A --> B
    B --> C
    C --> D
    D -->|"No"| E
    E --> N
    D -->|"Yes"| F
    D -->|"Yes"| G
    D -->|"Yes"| H
    D -->|"Yes"| I
    F --> J
    G --> J
    H --> J
    I --> J
    J --> K
    K -->|"No"| L
    L --> N
    K -->|"Yes"| M
    M --> N
```

## Target systems / source systems

**Authoritative (highest precedence):**
- Netting engine settlement file and confirmation records for the current cycle, including the locked FX reference rate, netted position per entity pair, and the final settlement instruction
- Entity ERP intercompany subledger snapshots extracted at netting-date cutoff, with posting timestamps and journal-header metadata

**Operational and contextual (secondary precedence):**
- Netting submission logs, including entity submission timestamps, resubmission events, network-timeout acknowledgements, and any override or manual-correction records
- FX rate history from the treasury system for the netting window, including intraday-rate updates and any rate-lock confirmation messages
- Operations desk notes and intercompany team communications documenting late payable notifications, disputed balances, or entity-reported anomalies during the netting window

**Excluded from authoritative use without explicit promotion:**
- Informal email exchanges or chat messages not attached to a submission log or netting-engine event
- Prior-cycle residuals or forecast positions not confirmed as part of the current cycle's scope

## Why this instance matters

Intercompany netting breaks at month-end are high-stakes because an unresolved settlement instruction error can propagate into cash-pool funding, drive incorrect elimination entries in the consolidation ledger, and distort intercompany receivable and payable balances across multiple reporting entities. Unlike a simple cash-position discrepancy, a netting mismatch requires reconciling submissions from independent legal entities that each maintain their own books at potentially different FX rates, precision settings, and cutoff conventions. The investigation must attribute each break component to a specific candidate cause without declaring which entity is wrong or approving any correcting instruction — both of which require human judgment and governance controls that sit outside the agent's authority. This instance grounds `incident-root-cause-analysis` in an audit-sensitive, multi-entity finance workflow where evidence provenance, source precedence, and explicit uncertainty are essential for the downstream decision to be defensible.

## Likely architecture choices

```mermaid
flowchart LR
    netting["Netting engine settlement file,<br>confirmation records, and<br>locked FX reference rate"] -->|"Provides current-cycle netting positions,<br>settlement instruction, and<br>authoritative rate context"| lanes["Multi-agent investigation lanes:<br>evidence retrieval, subledger reconciliation,<br>and hypothesis verification"]
    erp["Entity ERP subledger snapshots<br>with posting timestamps and<br>journal metadata"] -->|"Provides entity-pair subledger positions,<br>cutoff timestamps, and<br>journal lineage"| lanes
    logs["Submission logs, treasury FX history,<br>and operations notes"] -->|"Provides resubmission events,<br>timeout context, and<br>late-payable clues"| lanes
    lanes -->|"Records candidate causes,<br>evidence links, and<br>open checks by entity pair"| memory["Shared case memory for<br>hypotheses, FX normalization,<br>and unresolved break components"]
    memory -->|"Returns prior findings,<br>source precedence, and<br>pending verification state"| lanes
    lanes -->|"Assembles break attribution,<br>supporting evidence, and<br>residual uncertainty"| packet["Investigation packet for<br>intercompany operations and<br>regional finance handoffs"]
    memory -->|"Supplies hypothesis lineage<br>and cited open items"| packet
    packet -->|"Routes the evidence-backed packet to<br>Kai Brandt for adjudication"| review["Kai Brandt human review<br>boundary"]
    review -->|"Stops at human-owned settlement correction,<br>dispute escalation, or<br>supervised resubmission decisions"| stop["Stop boundary:<br>No agent-driven settlement correction,<br>dispute escalation, or journal action"]
```

- An orchestrated multi-agent flow can separate netting-engine evidence retrieval, cross-entity subledger reconciliation, and hypothesis verification so each reasoning step remains attributable and inspectable.
- Shared case memory should preserve candidate causes, confirming and disconfirming evidence per entity pair, FX-rate normalization choices, and open break components across handoffs between intercompany operations, regional finance teams, and the netting center.
- Human-in-the-loop review must remain mandatory before any settlement instruction is corrected, any entity is notified of a disputed balance, or any consolidation journal is adjusted as a result of the investigation's findings.
- Source-precedence rules must be declared explicitly in the investigation record so the netting-engine file and ERP subledger snapshots are treated as authoritative and submission logs are treated as contextual rather than equivalent.

## Governance notes

- Preserve the original netting-engine settlement file, entity subledger snapshots, and submission logs as immutable evidence links; do not overwrite or restate values in the investigation record without citing the source artifact and timestamp.
- Distinguish observed position mismatches from inferred causal attribution; an FX-rate divergence that explains 80 percent of a break is not evidence that the remaining 20 percent has the same root cause.
- Settlement instruction corrections, entity notifications, and consolidation journal adjustments must remain explicitly human-owned; the investigation packet ends at a ranked attribution with cited evidence and open checks, not at an approved corrective action.
- Record revision lineage for the investigation packet, including which hypotheses were added, demoted, or closed as new evidence arrived, so that any later audit or dispute review can trace the reasoning history.
- If submission-log gaps, missing ERP snapshots, or conflicting FX references prevent full attribution for one or more entity pairs, the investigation must surface that uncertainty explicitly rather than forcing a single-cause conclusion; Kai Brandt must be informed before any close deadline is allowed to pass with unresolved components.
- Restrict access to entity-level position detail and intercompany balance data to the intercompany operations team and the consolidation controller; do not share raw subledger extracts outside that group during the investigation.

## Evaluation considerations

- Time to first evidence-backed causal attribution for the largest break component, with cited netting-engine and subledger artifacts
- Proportion of total break volume attributed to a single evidence-backed cause before a human decision on settlement correction is required
- Whether FX-rate divergence, late payable, duplicate submission, and rounding-rule hypotheses are each tested and closed or explicitly held open rather than collapsed into a single undifferentiated explanation
- Rate at which missing subledger snapshots, unacknowledged submission timeouts, or conflicting FX references produce explicit uncertainty flags rather than forced reconciliation
- Whether the final investigation packet allows Kai Brandt to understand which entity pair contributed each break component and which open checks remain before a settlement correction decision can be made
