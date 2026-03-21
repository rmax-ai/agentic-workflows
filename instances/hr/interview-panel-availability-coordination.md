# Interview panel availability coordination

## Linked pattern(s)

- `calendar-conflict-coordination`

## Domain

HR.

## Scenario summary

A recruiter needs to schedule a final-round interview panel for a senior data-platform candidate within a five-business-day hiring SLA. The panel must include the hiring manager, a peer engineer from the target team, a cross-functional partner interviewer, and a recruiter closeout conversation, while respecting the candidate's provided availability in India Standard Time, interviewer working-hour rules in Pacific and Eastern time, and fairness constraints that avoid repeatedly assigning the same interviewer to off-hours loops. The workflow should reconcile calendars, sequence interview blocks into a coherent panel, place reversible holds, and escalate only when no policy-compliant panel can be assembled in time.

## Target systems / source systems

- Applicant tracking system with stage, SLA clock, interview plan, and required panel roles
- Recruiter scheduling request with candidate availability, modality, and accommodation notes
- Interviewer and hiring-manager calendars with working hours and existing holds
- Interviewer pool roster showing load-balancing or fairness metadata
- Calendar and video-meeting tools that support tentative scheduling holds
- Recruiting communication templates and internal coordination channel

## Why this instance matters

This example shows the scheduling pattern in a people-sensitive workflow where coordination quality affects candidate experience, interviewer load, and hiring velocity. It is materially different from both the operations review and the support bridge because the workflow must reconcile multi-block panel structure, candidate-facing timezone clarity, and fairness constraints across interviewers without drifting into candidate evaluation or hiring recommendation.

## Likely architecture choices

- A tool-using single agent reads candidate availability, interviewer calendars, timezone rules, and panel-role requirements, then proposes viable interview sequences.
- Bounded delegation fits because the agent can reserve tentative interviewer blocks, hold a recruiting closeout slot, and draft timezone-normalized invites, but it should not bypass accommodation requirements, assign an interviewer outside approved load-balancing rules, or confirm an out-of-hours loop without recruiter or hiring-manager approval.
- Human review remains necessary when only unfair or out-of-policy slots are available, when a required interviewer needs substitution, or when the candidate asks for changes that would breach the recruiting SLA unless an exception is approved.

## Governance notes

- Candidate availability and accommodation details should be used only for scheduling decisions and should not be copied broadly into interviewer invites beyond what is necessary.
- Required panel roles, maximum acceptable local-time windows, and interviewer fairness guardrails should be explicit before tentative booking begins.
- Reversible holds should be time-bounded and released automatically when another panel sequence is chosen so interviewer calendars stay trustworthy.
- The workflow should escalate rather than improvising when the only feasible schedule creates repeated off-hours burden for the same interviewer, misses the stated hiring SLA, or conflicts with protected candidate availability boundaries.

## Evaluation considerations

- Median time from final-round request to a complete panel proposal that satisfies all required roles and timezone constraints
- Percentage of interview loops confirmed without manual back-and-forth beyond defined recruiter checkpoints
- Rate of scheduling outcomes that meet interviewer fairness rules and avoid repeated off-hours assignments
- Candidate and recruiter reschedule rate attributable to stale calendar data, sequencing errors, or unclear timezone communication
