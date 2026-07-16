# Logic reconstruction and confirmation

## Purpose

Recover the author's actual argument, expose uncertainty, and obtain approval before language polishing makes an unconfirmed argument sound deceptively certain.

## Build the map

### Manuscript-level fields

- **Problem**: What real or theoretical problem motivates the work?
- **Gap**: What is unknown, inadequate, inconsistent, or unavailable?
- **Objective**: What does this study attempt to establish, create, compare, or explain?
- **Central claim**: What single proposition should a reader accept after reading the paper?
- **Contribution**: What changes for the field if the central claim is accepted?
- **Boundary**: Under what conditions is the claim supported, and where does it stop?

### Claim-evidence record

For each claim, record:

| Field | Meaning |
|---|---|
| ID | Stable identifier such as C1 or C2.1 |
| Claim | The proposition asserted by the manuscript |
| Role | Premise, method validity, result, interpretation, mechanism, comparison, limitation, or implication |
| Evidence | Result, figure, table, equation, citation, method, or reasoning step |
| Relation | Supports, qualifies, contrasts, depends on, explains, or follows from |
| Location | Section/paragraph or source line when available |
| Status | Supported, partially supported, unsupported, ambiguous, or author decision required |

Do not equate temporal sequence or correlation with causation. Do not treat a citation as support without checking what proposition the manuscript assigns to it.

## Diagnose breaks

Use four severities:

- **Critical**: The central conclusion does not follow, contradicts evidence, or requires absent evidence.
- **Major**: A subclaim is unsupported, a necessary premise is missing, or ordering obscures the argument.
- **Moderate**: Paragraph function, transition, definition, or scope is unclear but recoverable.
- **Minor**: Redundancy or local wording masks an otherwise sound relationship.

Name the defect precisely:

- missing premise;
- unsupported generalization;
- causal overreach;
- claim-evidence mismatch;
- contradiction;
- scope drift;
- undefined or shifting term;
- circular justification;
- result/interpretation conflation;
- motivation presented after its dependent claim;
- duplicated function;
- implication stated as observation.

## Propose repairs

Prefer the smallest repair that makes the chain valid:

1. Reorder existing content.
2. Make an implicit but clearly supported premise explicit.
3. Narrow or qualify the claim.
4. Move interpretation away from observation.
5. Request missing evidence or an author decision.

Never add an unprovided mechanism, result, or citation as a repair. Label any reconstructed intent with `Inference:`.

## Confirmation packet format

Keep the packet short enough for a meaningful author decision.

### A. Intended argument

State the central claim in one sentence, followed by a numbered chain:

`C1 evidence -> C2 interpretation -> C3 consequence -> central claim`

### B. Decisions required

List only decisions that change the argument. For each, include the current reading, alternative reading, consequence, and recommended option with rationale.

### C. Proposed logic

Show the revised section order and claim-evidence chain. Mark:

- `[PRESERVED]` for an explicit author claim;
- `[INFERRED]` for a proposed implicit premise;
- `[NARROWED]` for a claim whose scope is reduced;
- `[QUERY]` for information only the author can supply.

### D. Approval request

Ask the author to confirm the central claim, claim order, and all `[INFERRED]` items. Do not ask them to approve grammar or stylistic details at this stage.
