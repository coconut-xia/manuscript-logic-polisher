# Author Introduction style

## Provenance, priority, and transfer boundary

This guide derives from the author-designated Introduction of *Full-Stack UAV Detection Pipeline from Precise RGB-Event Sensing to Efficient Edge Processing*, read in the current author-provided main-text LaTeX, and from the author's explicit editing preferences. Profile revision: 2026-11-10.

The author states that the Introduction is primarily self-written and carries greater evidence of their intended language and logical progression than other co-edited sections. Give it the highest author-voice weight for Introduction work. Use other exemplars for compatible disciplinary or journal conventions without overriding that priority. Treat organizational patterns inferred from the manuscript as transferable preferences, not as statements that the author explicitly prescribed every detail.

Transfer the way the argument is built and information is connected. Do not transfer this paper's field, measurements, device names, number of gaps, paragraph count, or sequence of technical contributions. Earlier descriptions of a seven-paragraph Introduction or paired data/model limitations describe one manuscript; they are not the required architecture of future papers. Keep complete source articles outside this skill repository.

The signature to preserve is a progressive, noun-anchored argument: a concrete task exposes a constraint; the constraint has a stated consequence; relevant prior work is assessed against that need; the unresolved requirement motivates a matching design; each contribution then answers a previously established problem.

## Working representation before editing

Use the current or already confirmed argument map. Do not reopen settled scientific decisions for routine wording edits. Maintain the following short records internally; return them only when they resolve an ambiguity, explain a substantive restructuring, or the user requests them.

### Gap-answer ledger

For each material gap, record:

| Field | What to record |
|---|---|
| Gap | The precise unresolved property, scope, or question stated in the draft. |
| Consequence | Why this gap affects the target task, using supplied reasoning or evidence. |
| Prior-work basis | The supported literature comparison or existing observation establishing the gap. |
| Answer | The proposed method, resource, analysis, or theoretical step that responds to it. |
| Support | Where the paper evaluates or justifies this response. |
| Scope | Conditions and qualifications that must remain attached to the claim. |

One contribution may answer several linked gaps, and one gap may require several contributions. Make that relationship explicit rather than forcing a one-to-one count. Order contributions so the reader can connect them to the established needs. An attractive contribution without a motivating gap, or a prominent gap without a response, is a logic question; do not repair it by inventing a premise or result.

### Paragraph contract

Before rewriting a paragraph, identify its reader question, controlling purpose, incoming concept, supporting material, and outgoing concept. A topic label such as "related work" is insufficient; a useful purpose is "show that existing evaluation resources do not cover the stated operating condition."

The contract is a diagnostic aid, not a fixed five-part paragraph template. A short transition paragraph may only frame unresolved needs. A literature paragraph may supply the support for a gap introduced earlier. Keep connected reasoning together and split when the argumentative task genuinely changes.

## Operational author-voice decisions

### 1. Make the topic sentence promise a specific argumentative task

Open with the task difficulty, limitation, comparison axis, design response, or object that the paragraph will develop. Let the next sentences fulfill that promise through concrete content.

A topic sentence can be brief and broad enough to govern the paragraph. It does not need to contain the complete finding, every qualification, or an explanation of why the general topic is important. In an Introduction, problem-led openings are appropriate; do not impose rebuttal-style "we changed" or Results-style finding-first openings everywhere.

Check: can the paragraph's purpose be described without its heading? Does each subsequent sentence develop that purpose or a necessary qualification? If the paragraph opens with an abstract importance claim and the second sentence begins the actual argument, remove or replace the opening.

### 2. Connect paragraphs through a named handoff object

Choose the concept the next paragraph needs from the current paragraph: a requirement, limitation, resource, trade-off, unresolved question, or established capability. Name it clearly before crossing the paragraph boundary, then reclaim it in the next topic sentence.

Use the logical relationship that exists:

- For elaboration, repeat the limitation or criterion being developed.
- For narrowing, identify the subset or operating condition now in focus.
- For dependence, state how the preceding resource or result supports the next step.
- For contrast, retain a common comparison axis across the two objects.
- For extension, state the additional requirement that the existing result leaves open.

A connector is optional when the nouns already expose the relationship. Use a demonstrative such as "this limitation" only when its antecedent is unique. Do not begin every paragraph with "This," and do not add "Building upon" unless a real dependency is supplied.

Check the last sentence and next first sentence as a pair. If the next paragraph changes object without a discernible relationship, repair the handoff using existing content. If the relationship itself is missing, flag the logic question rather than concealing it with a transition.

### 3. Move from given information to the new assertion within sentences

Use an established object or a clearly introduced member of an established category as the subject or early anchor. Put the new operation, consequence, contrast, or requirement in the predicate. Where useful, let the new concept become an explicit subject in the following sentence.

For parallel comparisons, the shared comparison criterion provides continuity; the subjects need not literally repeat. For a new paragraph, a clear reorientation can introduce a new object. Old-to-new flow is not a rule that every sentence must start with the preceding sentence's final noun.

Prefer "these features" over a vague "this" when features are the actual referent. Keep conditions close to the assertion they restrict. Do not insert a citation-heavy detour between a concept and the explanation that makes it intelligible.

Check: can the reader identify what each "it," "this," "they," and "these" denotes without rereading? Does a new term appear before its role is established? Are two consecutive sentences connected only by "Furthermore"?

### 4. Establish the consequence of a problem before presenting its design response

Where the supplied argument permits, develop a dependency such as:

`property or operating condition -> stated failure mechanism -> consequence for the task -> required capability`.

Then introduce the design as a response to that required capability. Use only the links actually supported. An observed association does not automatically supply a mechanism, and a plausible mechanism does not establish universal causality.

Do not explain every engineering choice through a newly invented theoretical need. An already established constraint can motivate several choices without being reintroduced each time. A compact passage may combine the condition and consequence in one sentence.

Check: before "we propose" or a named component appears, does the reader know which problem it addresses? Can the need be stated with a concrete property rather than "better performance" or "improved effectiveness"?

### 5. Synthesize the closest literature by task-relevant criteria

Derive the comparison criteria from the paper's actual research question. Group prior work only when the grouping helps assess those criteria. Move toward the closest task, operating condition, or methodological alternative before making the gap claim.

A citation group should do work: establish a capability, expose an unaddressed condition, distinguish task definitions, or explain a trade-off. Chronology is useful when a change in research direction matters; it is not the default organizing principle.

Retain the strengths of the nearest alternatives. State the specific unmet criterion without describing all prior work as uniformly inadequate. Do not group citations under a broader claim than their supplied evidence supports.

Check: if author names and years are removed, does the paragraph still contain an intelligible comparison? Is the stated gap the outcome of that comparison? Would a different set of papers materially change the paragraph, or is the prose detachable boilerplate?

### 6. Introduce contributions in the order in which the argument needs them

Use the gap-answer ledger to decide contribution order. Explain the dependency or division of labor among contributions when it matters; a resource may support a method, an analysis may explain a design, or a deployment study may test an application requirement.

For a component or stage, give the reader its name, action, object, and relevant role. Choose specific supplied operations such as retaining, aligning, aggregating, selecting, or estimating. Avoid giving every component the interchangeable role "improves feature quality."

Do not require every paper to contain a dataset, multiple modules, and hardware deployment. A single-method paper, theory paper, observational study, and resource paper can preserve the same problem-response discipline with different moves.

Check: is each claimed contribution motivated earlier? Is a component's functional role being described, or is an untested causal performance attribution being added? Are contribution claims supported later under their stated scope?

### 7. Expand from the controlling concept to the details that make it credible

Within a paragraph, move through the levels the reader actually needs: a governing point, a category or comparison, concrete operations or examples, and their relevance. Keep a set of details under a shared purpose rather than appending an unrelated inventory.

In a contribution overview, describe the capability or role before lower-level configuration details. Include a number only when it establishes scale, coverage, evidence, or an important outcome at this stage of the argument. Put protocol detail in the appropriate Methods or supplementary location.

Do not require every paragraph to contain all of these levels. Do not remove a necessary premise merely to shorten the paragraph.

Check: can a reader tell why each example or number is included? Are several sentences restating the same role with different abstractions? Has a paragraph begun a second background discussion instead of advancing the established point?

### 8. Assign sentence length by communicative function

Use short sentences to orient, state one limitation, mark a pivot, or make a decisive bounded assertion. Use medium sentences for most explanations, operations, and comparisons. Allow a longer sentence when linked conditions, a tightly controlled contrast, or a coherent list belong to the same scientific assertion.

Split when a sentence starts doing another job, changes comparison axis, or hides a new premise inside a subordinate clause. Preserve a necessary qualification in the same sentence when separating it would broaden the claim.

Do not impose word-count thresholds, fixed short/long alternation, or a rule that every sentence has only one clause. Descriptive sentence statistics from an exemplar are observations, not targets.

Check: does the passage have purposeful changes in rhythm? Is a long sentence scientifically dense or merely clause-stacked? Have several short sentences fragmented a single continuous explanation?

### 9. End paragraphs with information the argument can use

Useful endings identify an unresolved requirement, the consequence of a supported comparison, a bounded capability, a result with its relevant scope, or an object the next paragraph develops. A precise factual statement can be a sufficient ending; no summarizing phrase is required.

Remove detachable endorsements such as "these advantages show great potential" when the paragraph already states the actual capability. Do not attach "Together," "Overall," or "This highlights" to every ending. Use a synthesis only when it adds a relationship that was not already expressed.

The final Introduction paragraph should leave the paper's central response and evaluation scope clear. It need not repeat all contributions or end in a universal application claim.

Check: after reading the final sentence, does the reader know more about the research question, requirement, or answer? Could that sentence be pasted unchanged into an unrelated paper? Does it prepare the next move without announcing the writing process?

### 10. Keep scientific names stable while allowing discourse to vary

Maintain a paper-specific terminology record with canonical term, definition, accepted abbreviation, and nearby non-equivalent terms. Preserve the canonical noun across paragraphs, sections, figures, captions, and supplementary material. Introduce a full name and abbreviation where needed, then follow the paper's chosen form consistently.

Do not substitute "precision" for "accuracy," "test" for "validation," or "robustness" for "stability" merely to avoid repetition. Such terms can denote different measurements or claims. Likewise, component aliases may be consolidated only when they truly denote the same object.

Vary discourse where useful: sentence shape, a precise operation verb, or the way an existing logical relation is expressed. Do not rotate synonyms for a scientific referent, and do not repeatedly replace one overused connector with another.

Check: would a reader infer two different quantities or modules from the names used? Are result and method descriptions using the same term with the same definition? Does lexical variety preserve every distinction the paper relies on?

## Adapt the architecture to the paper

Select the argument moves needed by the new manuscript rather than matching the exemplar's paragraph layout.

| New paper's emphasis | Useful dependency to expose |
|---|---|
| A method | Target failure or limitation -> required property -> method operation -> relevant evaluation. |
| A resource or benchmark | Missing evidence or coverage -> resource design criteria -> provided scope -> supported uses. |
| A theory or analysis | Unresolved question -> assumptions or setting -> analytical step -> warranted conclusion. |
| A system | Interacting constraints -> responsibilities of the stages -> integration -> system-level evaluation. |

These are options for exposing relationships, not required section contents. Preserve the paper's actual scope. Read the section-specific profile before transferring this voice to Results, Methods, Discussion, or SI; those sections should not all become miniature Introductions.

## Schematic revision examples

The placeholders below must be filled only with facts, relationships, or author-approved interpretations supplied for the new paper. They are examples of editorial decisions, not scientific claims or reusable sentences. Keep original citations attached to the propositions they support.

### Example 1: Make a stated problem motivate the design

**Before**

> Under [condition], [failure mode] weakens [task outcome]. We propose [method]. The method retains [relevant information] under that condition.

**After**

> Under [condition], [failure mode] weakens [task outcome]. We develop [method] to retain [relevant information] under this condition.

**Decision:** connect the stated operation to the stated problem without an importance-only opening. Do not imply that retaining the information fully solves the failure unless the supplied evidence establishes that stronger claim.

### Example 2: Replace an addition marker with an actual dependency

**Before**

> We provide [resource]. Moreover, we introduce [method].

**After, when the draft also supplies the dependence**

> We provide [resource] for [stated purpose]. The proposed [method] uses this resource to [stated operation].

**Decision:** name what carries the argument forward. If the method does not use the resource, this revision is invalid; retain an appropriate parallel relationship instead of manufacturing a dependency.

### Example 3: Turn a literature list into a criterion-based comparison

**Before**

> [Study A] provides [capability 1], but does not cover [condition 2]. [Study B] covers [condition 2], but does not provide [capability 3]. [The study's objective] requires [the stated combination].

**After**

> Existing approaches cover different parts of [the stated objective]. [Study A] provides [capability 1] without covering [condition 2], whereas [Study B] covers that condition but lacks [capability 3]. The stated combination therefore remains unresolved.

**Decision:** retain the individual strengths and limits while exposing the comparison axis. The final inference is appropriate only if the supplied literature scope supports it; two examples alone do not establish that the entire field lacks the combination.

### Example 4: Preserve useful content and remove an empty endorsement

**Before**

> [Method] improves [metric] under [evaluated condition]. These impressive findings demonstrate the great potential of the proposed approach.

**After**

> [Method] improves [metric] under [evaluated condition].

**Decision:** a concrete bounded result can close the paragraph. If a further implication is necessary, state the specific supplied implication; do not replace the deleted endorsement with another generic synthesis.

### Example 5: Keep one component name and chain through its output

**Before, with verified aliases**

> The encoder produces [features]. This feature extractor is optimized using [objective]. Its embeddings are passed to [next stage].

**After**

> The encoder is optimized using [objective] and produces [features]. These features are passed to [next stage].

**Decision:** use one canonical name for the verified component, keep the output name stable, and make the output the next sentence's subject. If "encoder," "feature extractor," or "embeddings" denote different objects in the manuscript, preserve those distinctions and explain the relationship instead.

### Example 6: Keep a qualification with the claim it limits

**Before**

> [Method] is accurate. It is evaluated on [specified data] under [specified condition].

**After, when accuracy is supported only in that setting**

> [Method] achieves [reported metric] on [specified data] under [specified condition].

**Decision:** express the supported outcome with its measurement and scope. Do not invent a metric or strengthen "evaluated" to "achieves" when the result has not been supplied.

## Misuse checks

- **Fixed-layout imitation:** Do not reproduce seven paragraphs, two limitations, or a sensing-to-deployment story when the new paper has a different argument.
- **Vocabulary imitation:** Do not carry domain nouns, device descriptions, dataset facts, or distinctive exemplar phrases into another field.
- **Connector substitution:** Changing every "Together" to "Collectively" preserves the repetition. Repair the relation or remove the marker.
- **False dependence:** "Therefore," "consequently," and "building on" require an actual supported link, not adjacency or a desire for smoother prose.
- **Uniformly negative prior work:** Preserve a relevant alternative's strengths. A contribution need not depend on claiming all previous work failed.
- **Compulsory synthesis:** A paragraph need not finish with an endorsement or all-purpose contribution claim.
- **Term flattening:** Similar words can denote different quantities or protocols. Consistency means stable definitions, not forced unification.
- **Sentence statistics as targets:** Do not optimize sentence or paragraph counts to match the exemplar.
- **Section flattening:** Reuse clarity and referential continuity in Methods or SI, but retain their procedural and reader-facing purposes.
- **Scope loss through shortening:** Removing conditions or a comparison target is not a stylistic improvement.
- **Invented gap repair:** If the problem-consequence-design chain lacks scientific support, surface that passage as a focused author question; continue editing independent material.
- **Recreating the author's corrections as universal prohibitions:** Prefer fewer unnecessary colons and formulaic transitions, but retain a colon, contrast, or technical term when its grammatical or scientific role is needed.

## Final Introduction self-audit

Assess the actual prose, not just keyword presence:

1. Does the opening establish a concrete problem and its consequential conditions before the solution appears?
2. Does each paragraph have a controlling job that its following sentences fulfill?
3. Can each paragraph boundary be explained through a shared object or an explicit logical relationship?
4. Do sentence subjects and references allow the reader to follow old information into the new assertion?
5. Are the closest studies synthesized against the criteria relevant to the stated gap?
6. Does every prominent gap have a matching response or an explicitly acknowledged scope boundary?
7. Does every contribution answer a previously motivated need without acquiring invented support?
8. Are component roles and evaluation claims distinct, with the necessary evidence scope preserved?
9. Are details and numbers earning their space at the current level of the argument?
10. Does sentence length vary by function without fragmented or clause-stacked reasoning?
11. Do paragraph endings add a precise consequence, scope, requirement, or forward object rather than generic praise?
12. Are canonical terms, abbreviations, comparison targets, and metric names consistent across the manuscript family?
13. Has the rewrite avoided importing the exemplar's topic, fixed layout, old facts, or unsupported causal claims?

Repair routine language and cohesion issues directly within the authorized scope. Report unresolved scientific relationships concisely with their locations and the smallest author decision required; do not turn the entire checklist into a repeated approval questionnaire.
