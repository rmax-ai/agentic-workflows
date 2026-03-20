# Proposal: Self-Reflection and Self-Improvement In The Ontology

- Status: proposed
- Date: 2026-03-20
- Scope: ontology modeling proposal
- Related areas: capabilities, problem structures, optimize-adapt patterns, autonomy, governance

## Question

How should the repository represent self-reflection and self-improvement without breaking the pattern-first ontology or encouraging vague, unconstrained agent behavior?

## Proposal Summary

Model self-reflection and self-improvement as different kinds of ontology elements:

1. Self-reflection should be modeled primarily as a capability and control mechanism.
2. Self-improvement should be modeled primarily as a bounded pattern within the `optimize-adapt` family.
3. Persistent changes to agent behavior should be treated as governance-relevant and usually approval-gated.

This keeps the ontology pattern-first while making room for closed-loop agent behavior.

## Why This Split

Self-reflection and self-improvement are related, but they operate at different levels.

### Self-reflection

Self-reflection is usually an in-run activity. The agent inspects its intermediate outputs, evidence quality, uncertainty, policy alignment, or progress against the goal, then revises the next step.

Typical outcomes:

- revise a plan
- request more evidence
- invoke verification
- reduce confidence
- escalate to a human
- stop before an irreversible action

This makes self-reflection a capability and control-loop concern more than a top-level pattern family.

### Self-improvement

Self-improvement is usually a cross-run or persistent activity. The system changes some reusable aspect of future behavior based on feedback, evaluation, or observed failures.

Typical targets of improvement:

- prompt or instruction structure
- routing logic
- retrieval or memory heuristics
- thresholding or scoring policies
- workflow branching rules
- escalation criteria

This makes self-improvement a pattern-level concern, especially when the workflow explicitly performs improvement over time.

## Recommended Ontology Placement

### 1. Capabilities

Add capability terms along these lines in a future controlled vocabulary:

- `self-assessment`
- `uncertainty-estimation`
- `critique-and-revision`
- `replanning`
- `feedback-integration`

These fit naturally under `capability_requirements` in canonical pattern entries.

### 2. Problem structures

Add reusable problem structures along these lines in a future controlled vocabulary:

- `closed-loop-optimization`
- `error-recovery-and-replanning`
- `policy-constrained-adaptation`

These let patterns distinguish between simple execution, bounded adaptation, and persistent improvement loops.

### 3. Pattern family placement

Keep self-improvement under the existing `optimize-adapt` family rather than creating a new top-level family.

Candidate canonical patterns:

- `self-evaluation-and-replanning`
- `feedback-driven-optimization`
- `continuous-improvement-loop`
- `policy-constrained-self-improvement`

This aligns with the repository's existing browse direction and avoids overfitting the ontology to one fashionable label.

### 4. Governance placement

Represent key controls in these existing pattern fields:

- `autonomy_profile`
- `risk_governance`
- `failure_modes`
- `evaluation`
- `why_agentic`

No schema expansion is required to start modeling this cleanly.

## Important Distinction: Within-Run Reflection vs Cross-Run Improvement

The ontology should treat these as different timescales with different governance expectations.

### Within-run reflection

The agent may:

- critique an intermediate result
- revise a plan
- request additional evidence
- invoke a verification step
- escalate when confidence or policy alignment is too low

This can often be autonomous when the action remains reversible and well-bounded.

### Cross-run improvement

The system may:

- modify prompt templates
- update routing or delegation rules
- tune thresholds
- change memory selection behavior
- alter workflow policies for future runs

This should generally be treated as a higher-risk activity requiring stronger evaluation, auditability, rollback, and often human approval.

## Proposed Modeling Rules

1. If the behavior is about thinking better before acting in the current run, model it as reflection.
2. If the behavior is about changing future behavior over time, model it as improvement.
3. If the change persists across runs, model governance and reversibility explicitly.
4. Do not create a top-level `self-improving-agent` family.
5. Do not treat unconstrained self-modification as a default or baseline agentic capability.

## Schema Implications

The current schema already supports this proposal through existing fields:

- `capability_requirements`
- `autonomy_profile`
- `risk_governance`
- `why_agentic`
- `failure_modes`
- `evaluation`
- `related_patterns`

Because of that, the next dependency-safe step is vocabulary and pattern authoring, not schema redesign.

## Example Pattern Sketch

Illustrative canonical pattern:

- `id`: `self-evaluation-and-replanning`
- `pattern_family`: `optimize-adapt`
- `problem_structure`: `error-recovery-and-replanning`
- key capabilities: `self-assessment`, `replanning`
- governance emphasis: bounded autonomy, approval before irreversible change, auditable revision logic

## Recommended Follow-On Work

When the repository reaches the appropriate dependency stage:

1. Add vocabulary entries for the capability and problem-structure terms above.
2. Add an optimize-adapt family doc that distinguishes reflection, adaptation, and improvement.
3. Author one canonical pattern for bounded self-evaluation and replanning.
4. Author one canonical pattern for policy-constrained self-improvement.
5. Ensure any future instance distinguishes ephemeral adaptation from persistent behavior change.

## Decision Request

If accepted later, this proposal should lead to a durable decision stating:

- self-reflection is modeled as a capability/control-loop mechanism
- self-improvement is modeled as a bounded optimize-adapt pattern
- persistent behavioral change requires explicit governance and usually approval gating
