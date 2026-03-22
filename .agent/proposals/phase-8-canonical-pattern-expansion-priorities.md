# Proposal: Phase 8 Canonical Pattern Expansion Priorities

- Status: proposed
- Date: 2026-03-22
- Scope: ontology modeling proposal
- Related areas: canonical patterns, pattern families, problem structures, Phase 8 breadth expansion

## Question

As the repository moves from Phase 7 coverage refinement into Phase 8 breadth expansion, which new canonical patterns would add real ontology value without weakening the existing family boundaries?

## Proposal Summary

Treat Phase 8 pattern expansion as a narrow shape-expansion exercise rather than another coverage-balancing pass.

The repository should add new canonical patterns only where the current pattern inventory still compresses materially different workflow structures into adjacent patterns.

The highest-value additions currently appear to be:

1. `schema-migration-and-field-remapping`
2. `provenance-and-chain-of-custody-verification`
3. `controlled-submission-and-acknowledgement-tracking`
4. `co-drafting-with-tracked-disagreement`
5. `conflict-aware-source-briefing`

These candidates expand ontology breadth without reopening the current family map, problem-structure vocabulary, or coverage matrix.

## Current State

The repository is not missing family, domain, architecture, or risk coverage.

Current tracked state shows:

1. all nine top-level families have canonical patterns
2. all seven modeled domains have canonical and grounded coverage
3. all tracked architecture types are represented across families
4. all tracked risk levels are represented across families
5. the canonical layer currently contains forty-nine patterns

That means the next ontology step should focus on missing reusable workflow shapes rather than empty matrix cells.

## Why A Phase 8 Proposal Is Needed

The current ontology is mature enough that undisciplined expansion would likely create near-duplicate patterns.

The main risk is not under-modeling. The main risk is adding thin variants that merely rephrase existing patterns by domain, governance level, or artifact name.

Phase 8 therefore needs an explicit selection rule:

1. prefer structurally missing workflow forms
2. reject additions that only restate an existing pattern with narrower subject matter
3. keep family boundaries stable unless multiple candidates repeatedly fail to fit the current family map

## Structural Observations

### Families that look broad but still have room

#### `transform-process`

This family already covers:

- document handoff
- normalization and enrichment
- batch transformation
- change-triggered refresh
- critical channel-safe packaging
- approval-gated transformation release

The remaining gap is a structured-to-structured migration shape where the hard problem is preserving semantic equivalence across field remapping, schema drift, and controlled target-state conversion.

#### `investigate-reconcile-verify`

This family already covers:

- root-cause analysis
- record reconciliation
- claimed-state verification
- approval-bound verification for release
- critical authoritative state restoration

The remaining gap is explicit lineage and custody verification. Provenance continuity is not the same as claim verification, record reconciliation, or release gating.

#### `execute-automate`

This family already covers:

- browser approval-gated execution
- exception-aware task execution
- human-directed task orchestration
- staged execution with rollback holds
- workflow handoff and completion

The missing general shape is controlled submission into an external or downstream lane with acknowledgement tracking, durable receipt handling, retry safety, and completion proof.

#### `human-agent-collaborative-work`

This family already covers:

- analyst copilot loops
- approval-centered collaboration
- shared workbench upkeep
- approval-gated collaborative artifact release
- critical protected artifact collaboration

The remaining gap is true co-authoring of a shared artifact where disagreement stays attached during drafting rather than only at upkeep or release boundaries.

#### `gather-retrieve-synthesize`

This family already covers:

- citation-verified synthesis
- approval packet generation
- change-triggered briefing refresh
- crisis briefing synthesis
- approval-gated briefing release

The remaining gap is a conflict-preserving briefing pattern whose purpose is to surface contradictory source claims and unresolved uncertainty without resolving them.

### Families that currently look saturated

#### `monitor-detect-triage`

This family already has distinct low-, moderate-, approval-bound, and critical shapes. Additional patterns here are likely to become thin variants of watchlisting, anomaly review, risk triage, or critical corroboration.

#### `optimize-adapt`

This family already spans threshold tuning, sampling tuning, queue optimization, governed bundle retuning, approval-bound optimization release, and critical protected adaptation. Additional proposals here should be treated with skepticism unless they introduce a materially different adaptation lifecycle.

#### `plan-coordinate-schedule`

This family already spans scheduling, replanning, coordination refresh, contingency activation gating, and critical command-window resequencing. New additions need unusually clear boundaries to avoid duplication.

#### `recommend-decide-escalate`

This family is the broadest current family by canonical count. It can absorb more patterns, but it is also the easiest place to create duplicates that are really route selection, option ranking, waiver framing, or packet-release variants of existing structures.

## Recommended Candidate Patterns

### 1. `schema-migration-and-field-remapping`

- Target family: `transform-process`
- Suggested `problem_structure`: `structured-representation-transformation`

This pattern would cover workflows whose main challenge is migrating one structured representation into another while preserving operational meaning, handling one-to-many and many-to-one field mapping, recording semantic loss or approximation, and producing a downstream-usable target representation.

This is not already cleanly covered by:

- `document-to-structured-data-handoff`, which begins from heterogeneous or document-like source material
- `normalization-and-enrichment`, which standardizes fields inside a largely stable representation
- `change-triggered-representation-refresh`, which refreshes an already-issued representation after source changes
- `approval-gated-transformation-release`, which governs release of a finished transformed package rather than the transformation logic itself

### 2. `provenance-and-chain-of-custody-verification`

- Target family: `investigate-reconcile-verify`
- Suggested `problem_structure`: `evidence-backed-verification`

This pattern would cover workflows whose main challenge is proving continuity of custody, provenance, or lineage across artifacts, handoffs, evidence packets, samples, records, or operational payloads.

This is not already cleanly covered by:

- `claimed-state-verification`, which asks whether a claimed condition is true
- `authoritative-record-reconciliation`, which restores consistent state across records
- `evidence-gated-verification-for-release`, which verifies whether a packet is ready for bounded release or reliance
- `critical-authoritative-state-restoration`, which reconstructs trusted current state under severe consequences

### 3. `controlled-submission-and-acknowledgement-tracking`

- Target family: `execute-automate`
- Suggested `problem_structure`: `approval-gated-execution`

This pattern would cover workflows that submit approved material into an external or downstream system, track receipts or acknowledgements, handle missing or delayed confirmations, and close the execution loop only when submission state is durably confirmed.

This is not already cleanly covered by:

- `browser-based-form-completion-with-approval-gates`, which is channel-specific and UI-oriented
- `exception-aware-task-execution`, which focuses on resilient execution of routine steps rather than explicit receipt confirmation
- `staged-change-execution-with-rollback-holds`, which governs progressive live-state rollout rather than submission acknowledgement
- `workflow-hand-off-and-completion`, which starts after the decisive action is already accepted or completed

### 4. `co-drafting-with-tracked-disagreement`

- Target family: `human-agent-collaborative-work`
- Suggested `problem_structure`: `human-agent-collaboration`

This pattern would cover workflows where a human and agent jointly author one artifact through visible iterative turns while keeping unresolved objections, alternate phrasings, or contested evidence attached to the draft.

This is not already cleanly covered by:

- `analyst-copilot-loop`, which is a broader copilot interaction shape
- `shared-workbench-orchestration`, which is about upkeep of a shared internal working surface
- `approval-centered-collaboration`, which is centered on approval readiness and reviewer alignment
- `approval-gated-collaborative-artifact-release`, which starts from an already jointly prepared artifact and governs release of one exact revision

### 5. `conflict-aware-source-briefing`

- Target family: `gather-retrieve-synthesize`
- Suggested `problem_structure`: `context-gathering-and-synthesis`

This pattern would cover workflows where the deliverable is an inspectable briefing that deliberately preserves contradictory source claims, confidence differences, source precedence, and unresolved questions rather than normalizing them into a single synthesized conclusion.

This is not already cleanly covered by:

- `research-synthesis-with-citation-verification`, which aims for grounded synthesis
- `change-triggered-context-briefing`, which refreshes context after authoritative source changes
- `crisis-briefing-evidence-synthesis`, which compresses critical context for severe handoff
- `authoritative-record-reconciliation`, which resolves discrepancies rather than preserving them for briefing

## Secondary Candidates Worth Considering Later

### `redaction-and-minimization-transformation`

- Likely family: `transform-process`
- Likely `problem_structure`: `structured-representation-transformation`

This is only worth adding if it stays broader than critical channel packaging and focuses on deliberate lossy transformation for safe downstream reuse.

### `freeze-window-milestone-coordination`

- Likely family: `plan-coordinate-schedule`
- Likely `problem_structure`: `multi-party-coordination`

This is only worth adding if it remains narrowly centered on fixed freeze windows, dependency locks, and non-movable external milestones rather than general scheduling or replanning.

### `policy-waiver-recommendation`

- Likely family: `recommend-decide-escalate`
- Likely `problem_structure`: `recommendation-and-decision-support`

This is only worth adding if it stays focused on exception framing, waiver rationale, and bounded escalation rather than route selection, attestation fit, or generic recommendation support.

## Recommended Addition Order

If Phase 8 begins with a small bounded canonical batch, the suggested order is:

1. `schema-migration-and-field-remapping`
2. `provenance-and-chain-of-custody-verification`
3. `controlled-submission-and-acknowledgement-tracking`

This order is preferred because it spreads additions across three different families and introduces three clearly different reusable shapes:

1. structure-preserving transformation
2. lineage verification
3. receipt-bound execution

That produces more ontology breadth than adding several candidates inside the same family.

## Pattern Addition Rules

Any future Phase 8 canonical pattern added from this proposal should satisfy all of the following:

1. it must describe a reusable workflow shape that appears across multiple domains
2. it must remain cleanly inside one primary family
3. it must not be only a higher-risk or lower-risk restatement of an existing pattern
4. it must not be only a release-gated, approval-gated, or critical variant of an existing pattern unless the reusable structure changes materially
5. it must be distinguishable from neighboring patterns by stop condition, core artifact, and control boundary

## Risks And Tradeoffs

### Risk: over-expansion creates shallow duplicates

Mitigation:

1. add no more than one to three new canonical patterns in the first Phase 8 batch
2. require explicit contrast notes against neighboring patterns before acceptance
3. prefer additions that reveal a clearly different stop condition or reusable artifact shape

### Risk: family boundaries blur under new pattern names

Mitigation:

1. keep the current family map stable unless repeated evidence shows it cannot absorb the new structures
2. add boundary notes to each new canonical pattern explaining why it does not belong in adjacent families

### Risk: recommendations drift back into matrix balancing

Mitigation:

1. do not justify new canonical patterns by uncovered cells alone
2. require an ontology argument before a coverage argument

## Acceptance Criteria

This proposal should be considered implemented when:

1. at least one Phase 8 canonical pattern is added because it fills a genuine missing reusable workflow shape rather than a coverage-only gap
2. each accepted new pattern includes explicit contrast against neighboring canonical patterns
3. Phase 8 additions remain small, dependency-aware, and family-stable
4. the repository avoids adding thin domain-specific restatements of existing canonical patterns

## Decision Request

If accepted later, this proposal should guide Phase 8 canonical expansion toward a small number of structurally distinct additions, starting with transformation, verification, execution, collaboration, and synthesis shapes that are not yet represented cleanly in the current forty-nine-pattern ontology.
