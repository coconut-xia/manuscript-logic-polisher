# Author exemplar style profile

## Status and weighting

Treat this as a living profile, last updated 2026-07-16. Give both current exemplars equal, strong source-level weight. Section-specific application does not reduce either source's status; it prevents Methods or Supplementary conventions from being imposed mechanically on an Abstract or Discussion.

Current evidence:

1. *Brain-inspired visual sensing–perception for open-world environments*, Nature Sensors (2026), DOI 10.1038/s44460-026-00095-3. Analyze the full main-article argument and prose.
2. *Full-Stack UAV Detection Pipeline from Precise RGB-Event Sensing to Efficient Edge Processing*, author-polished main-text LaTeX. Treat its complete Abstract, Introduction, Results, Discussion, Methods, and captions as the primary author-voice exemplar.
3. The corresponding author-polished Supplementary Information. Treat it as equally strong evidence for technical exposition, quantitative analysis, equations, captions, and implementation detail.

Give the Nature Sensors work and the author's full manuscript family equal, strong work-level weight. Within Introduction tasks, follow the user's explicit instruction to use the author-polished main-text Introduction as the author-voice anchor; this section-specific priority does not reduce how fully the other exemplars are learned.

Do not store the source PDF or full LaTeX corpus in Git. Keep only this derived profile and source provenance.

## Transfer principle

Transfer argument architecture, sentence function, evidence calibration, and cohesion before isolated wording. The author's own polished sentences define voice, but generic phrases in any source must still pass the anti-template and evidence-specificity checks.

## Core voice

- Maintain high information density. Center each sentence on a scientific relation, operation, observation, or bounded inference.
- Give each sentence one primary communicative job. Retain linked conditions or qualifiers in the same sentence only when they define that job.
- Prefer purpose-led, finding-led, or object-led openings over conversational chronology.
- Preserve stable technical nouns across adjacent sentences. Do not substitute synonyms merely for variety.
- State boundaries explicitly. Distinguish what the data establish from what a simulation, metric, or comparison cannot establish.
- Use concrete mechanisms, measurements, and comparison targets instead of generic importance or novelty claims.

## Sentence rhythm

Clean diagnostic statistics, used only as descriptive evidence:

| Exemplar | Median | Mean | P90 | Paragraph mean |
|---|---:|---:|---:|---:|
| Nature Sensors main-text blocks | 18 words | 19 words | 29 words | 4.0 sentences |
| Author main-text Introduction | 21 words | 20 words | 27 words | 7.3 sentences |
| Author main-text Results | 18 words | 19 words | 27 words | 6.9 sentences |
| Author main-text Discussion | 18 words | 19 words | 26 words | 5.2 sentences |
| Author main-text Methods | 17 words | 18 words | 27 words | 4.3 sentences |
| Author-polished Supplementary Notes | 22 words | 23 words | 35 words | 2.5 sentences |

Do not target these values mechanically. Use shorter sentences for a decisive result, boundary, or pivot; medium sentences for most claims and explanations; and longer sentences for one relationship with necessary conditions, variables, or contrasts. Never enforce alternating lengths.

## Rhetorical organization

### Abstract

Prefer the compact move sequence: problem -> contrast or motivating principle -> proposed framework -> internal stages -> concrete instantiation -> principal results -> bounded contribution. Keep each move distinct and omit discovery chronology.

### Introduction

Read `author-introduction-style.md` and follow its seven-paragraph progressive narrowing. Use the Nature Sensors exemplar as a compatible high-impact journal reference, but preserve the author's own problem decomposition, paired limitation structure, contribution ordering, and system-level closure.

### Technical and supplementary exposition

- Open a section or paragraph by naming its purpose, evaluated object, figure/table function, or technical problem.
- Explain the conceptual reason for a metric or formulation before presenting the equation.
- After an equation, define variables and then state what the quantity isolates, measures, or permits.
- Describe a multi-stage procedure in true operational order; use `First`, `Second`, and `Third` only when the order matters.
- For hardware or deployment details, report configuration -> measured outcome -> scope of the reported system-level quantity.
- For synthetic experiments, state which physical behaviors are modeled, which non-idealities are omitted, and what claim the simulation is allowed to support.

### Results and ablations

Organize Results as a system evidence chain: benchmark and sensing fidelity -> coverage and modality characteristics -> model design -> cross-dataset and scenario performance -> controlled alignment sensitivity -> model- and system-level deployment. Within each block use evaluation purpose -> comparison setup -> quantitative result -> condition-specific interpretation. Report negative or qualified findings directly, including cases where one metric or modality does not improve. When several modules are compared, keep each metric and attributed function adjacent; reserve complementarity claims for joint evidence.

### Discussion and limitations

Follow the author's six-part Discussion logic when relevant: integrated system contribution -> alignment as a prerequisite -> modality-specific fusion mechanisms -> synthetic-data boundary -> system-level runtime bottleneck -> limitations and future work. Reconnect engineering evidence to the conceptual framework, then state external-validity boundaries separately. Use `may`, `suggest`, or explicit future-work language when generalization has not been tested.

### Methods

Open each subsection with the object or procedure, then provide configuration, operation, and rationale. Define equations conceptually before or immediately after presentation; keep symbols, dimensions, and parameter choices adjacent. Use passive voice when the procedure or controlled condition is the focus, but use an explicit actor when a design decision or interpretation would otherwise be ambiguous.

### Figure and table captions

Begin with a compact descriptive title. Follow with panel-specific statements in visual order. State what is plotted or measured before interpretation. Avoid reproducing the full Results discussion in the caption.

## Cohesion and connectors

- Prefer explicit conceptual subjects and lexical continuity; a connector is optional when the relation is already clear.
- Use purpose clauses such as `To evaluate...` or `To isolate...` to motivate a method or analysis.
- Use figure/table anchors such as `As reported in...` only when the cited object directly supports the sentence.
- Use `however`, `while`, `whereas`, and `although` for genuine contrast, boundary, or concession.
- Use cause/consequence markers only for justified dependencies, not temporal succession or correlation.
- Avoid repetitive paragraph openings with `Furthermore`, `Moreover`, `Additionally`, `Notably`, `Crucially`, or `Ultimately`.

## Claim verbs and lexical discipline

- Prefer precise functional verbs such as `reports`, `presents`, `quantifies`, `compares`, `preserves`, `suppresses`, `mitigates`, `isolates`, `yields`, `enables`, `remains`, and `reflects` when their objects make the action verifiable.
- Use `demonstrates`, `validates`, or `confirms` only when the stated evidence directly tests the claim and its scope.
- Use `suggests`, `indicates`, `is consistent with`, or a narrower factual statement for interpretations and mechanisms not directly isolated.
- Avoid detachable AI-style claims such as `paves the way`, `holds great promise`, `underscores the importance`, `intricate interplay`, or unqualified `groundbreaking` and `transformative`.

## Update protocol

For every new exemplar, record its title or stable identifier, source role, section coverage, and user-specified weight. Compare it against this profile before modifying a rule. Increase confidence only when the new source supports the same pattern; retain section-specific disagreement rather than averaging incompatible conventions. Never overwrite the explicit equal-weight instruction for the two current exemplars without the user's approval.
