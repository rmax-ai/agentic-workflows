# Proposed browse tree

This repository should browse **patterns first**, then expose alternate views once canonical patterns and vocabularies exist.

The browse design below is intentionally compatible with later `data/views/` work. It proposes stable conceptual groupings without prematurely freezing every generated file shape.

## Primary browse tree: pattern-first

The default browse experience should start from pattern families, because families let readers move from broad workflow structure to specific reusable patterns.

```text
patterns/
├── gather-retrieve-synthesize/
│   ├── retrieve-and-assemble-context
│   ├── multi-source-synthesis
│   └── evidence-grounded-briefing
├── transform-process/
│   ├── document-to-structured-data
│   ├── normalization-and-enrichment
│   └── batch-content-transformation
├── investigate-reconcile-verify/
│   ├── discrepancy-investigation
│   ├── record-reconciliation
│   └── evidence-backed-verification
├── monitor-detect-triage/
│   ├── event-monitoring-and-alert-triage
│   ├── anomaly-detection-review
│   └── issue-intake-triage
├── plan-coordinate-schedule/
│   ├── constraint-aware-planning
│   ├── multi-party-coordination
│   └── schedule-adjustment-and-replanning
├── recommend-decide-escalate/
│   ├── decision-support-recommendation
│   ├── policy-aware-escalation
│   └── option-ranking-with-rationale
├── execute-automate/
│   ├── approval-gated-action-execution
│   ├── exception-aware-task-execution
│   └── workflow-hand-off-and-completion
├── optimize-adapt/
│   ├── feedback-driven-optimization
│   ├── policy-constrained-adaptation
│   └── continuous-improvement-loop
└── human-agent-collaborative-work/
    ├── analyst-copilot-loop
    ├── approval-centered-collaboration
    └── shared-workbench-orchestration
```

## Intended semantics of the tree

### Family node
A family node is the highest-level browse grouping for reusable workflow structure. It should map cleanly to `pattern_family` in canonical pattern data.

### Pattern node
A pattern node is the canonical reusable unit. It should resolve to a single pattern entry in `data/patterns/` once that directory exists.

### Domain examples under a pattern, not above it
When domain context is shown in the tree, it should appear beneath or beside a pattern as examples, not as a parallel top-level spine.

That keeps the primary tree aligned with the repository mission.

## Alternate browse views

Alternate views should be derived indexes, not competing canonical structures.

### 1. By domain
Purpose: help a reader in a specific sector discover which patterns recur there.

Conceptual shape:

```text
domains/
├── engineering/
├── finance/
├── compliance/
├── operations/
├── research/
├── support/
└── hr/
```

Each domain page or generated view should list linked patterns grouped by family where possible, so the pattern-first structure remains visible.

### 2. By architecture
Purpose: show which patterns are commonly implemented as single-agent, orchestrated multi-agent, human-in-the-loop, event-driven, or approval-gated systems.

Conceptual shape:

```text
architectures/
├── tool-using-single-agent/
├── orchestrated-multi-agent/
├── human-in-the-loop/
├── event-driven-monitoring/
└── approval-gated-execution/
```

### 3. By autonomy
Purpose: help readers discover patterns by level of discretion and required human oversight.

This view should likely group patterns by autonomy level with summaries of approval boundaries and escalation expectations.

### 4. By risk / governance
Purpose: surface high-control workflows, critical failure cost patterns, and audit-sensitive use cases.

This view is especially important for enterprise adoption and should remain compatible with later governance vocabularies.

### 5. By capability requirement
Purpose: make it easy to find patterns requiring retrieval, planning, tool execution, verification, memory, coordination, or optimization.

This should be a secondary view because capabilities are enabling properties, not the canonical organizing spine.

## Compatibility with later `data/views/` work

This document is a design proposal, not a data contract for generated view files. To stay compatible with later phases:

- the **family names** should line up with future controlled vocabulary ids,
- the **pattern nodes** should correspond one-to-one with canonical pattern entries,
- alternate view artifacts should reference canonical pattern ids rather than copy full pattern payloads,
- views should be regenerable from canonical data.

## Browse design rules

1. The top-level default view is always pattern-family-first.
2. Domains are browse aids, not the canonical root taxonomy.
3. A pattern can appear in multiple alternate views without becoming multiple canonical patterns.
4. View files should be safe to regenerate as vocabularies and pattern coverage expand.
5. Documentation may show illustrative tree nodes before the repository has concrete pattern data, but later generated views must stay consistent with canonical ids.
