# Persistent author style profile

## Authority and provenance

Updated 2026-11-10 from explicit author corrections and the current author manuscript family, titled *Full-Stack UAV Detection Pipeline from Precise RGB-Event Sensing to Efficient Edge Processing*.

The author explicitly identifies the Introduction as the section they wrote most intensively and the highest-value source for their own language and progressive reasoning. Use this as the primary author-voice anchor across future papers. The rest of the main text and SI provide section-specific technical-exposition evidence; they are not a reason to overwrite that voice.

The repository's earlier Nature Sensors exemplar remains secondary journal/field context. Its paper-specific facts and earlier equal-weight wording do not override the author's current explicit Introduction priority. No new scientific evidence is established by this profile.

Authority order:
1. Current task instructions and explicit author corrections.
2. The author's deliberate Introduction language and argument habits.
3. Approved section-specific practices from main text, SI, and responses.
4. Compatible journal/field examples.
5. Incidental constructions and automated surface statistics.

Do not learn an acknowledged error as a preference. Examples include accidentally blackening normal hyperlinks during clean-version generation, a remaining formulaic opener, and unresolved numbering. The profile records the intended style, not a certification that every source sentence already complies.

## The portable signature

The most characteristic pattern is **concept-anchored progression**:
- name a specific task difficulty or unresolved issue;
- unpack its cause, observable consequence, or scientific cost;
- use the same concept to organize the relevant comparison;
- derive a requirement;
- answer that requirement with a design or contribution;
- keep the resulting conclusion within its evidence.

This can span several paragraphs. It is not a compulsory sequence inside every paragraph. A new paper can have one gap, several linked gaps, no dataset contribution, no device deployment, or a different section order.

## Operational voice rules

| Rule | What to do | Avoid |
|---|---|---|
| Specificity at entry | Start with the concrete problem, result, object, or relation relevant to the paragraph. | A detachable sentence saying why careful study or fair comparison matters. |
| Concept continuity | Reuse the stable scientific noun when a sentence or paragraph develops it. | Synonym rotation that makes one object appear to become several. |
| Visible reasoning | State the relation between observations, constraints, requirements, and design. | Adding "therefore" to conceal a missing premise. |
| Synthesis | Group prior work by the criterion needed for the argument. | A list of papers followed by an unsupported global dismissal. |
| Controlled contrast | Explain both what an approach preserves and what remains unresolved under specified conditions. | Describing all earlier work as uniformly inadequate. |
| Evidence adjacency | Put a key comparison or evidence pointer close to its claim. | A broad claim separated from its support by unrelated detail. |
| Selective detail | Retain what a reader needs to assess the point; route full protocols to the appropriate section. | Removing conditions to make a paragraph shorter, or reproducing an entire table in prose. |
| Functional endings | End with the consequence, requirement, bounded inference, or bridge that the paragraph has earned. | An automatic importance/novelty slogan at the end of every paragraph. |
| Directness with restraint | State real findings firmly and mechanisms at their supported strength. | Promotional certainty or repeated unnecessary disclaimers. |
| Varied expression | Vary clause construction and reporting verbs where their meaning permits it. | The same sentence frame and connective in every paragraph. |

## Sentence construction

Give each sentence one controlling scientific job. Linked conditions, a justified contrast, or tightly coupled qualifications may remain in the sentence. Split when it introduces an independent result, changes the referent, or starts a second reasoning step.

Prefer an identifiable scientific subject:
- an evaluated model or material;
- a measurement or representation;
- a configuration or experimental condition;
- a named result or interpretation;
- "we" when describing a design choice or action.

Do not ban passive voice. Use it when the controlled operation or object is the focus. Do not replace readable verbs with stacked abstract nouns to sound scholarly. Check the verb-object collocation, not just the verb list: a representation may retain information, while a device remains limited by slow recovery. Do not create unnatural phrases such as a device retaining limitations merely to use a favored operation verb.

Maintain known-to-new flow. Carry a named object or established result forward, then introduce the new property, comparison, limitation, or design consequence. A bare "this" is acceptable when its antecedent is unmistakable; name the result when several antecedents compete.

Vary length by purpose. Short sentences establish direction, a result, or a boundary; medium sentences carry most explanations; longer sentences retain one relationship with necessary conditions. There is no sentence-length quota and no short-long alternation rule.

## Vocabulary and cohesion

Scientific nouns and definitions are invariants; discourse wording is flexible. A model's official name, a measured quantity, and its definition should remain stable. "reports", "compares", "quantifies", "measures", "retains", "reduces", and "remains" can vary with the actual action.

Choose a connector after identifying the relation:
- contrast/concession;
- consequence;
- specification;
- complementary evidence;
- prerequisite/dependency;
- extension of scope.

A repeated technical noun or parallel sentence structure can express the relation without an explicit connector. Do not replace every "together" with "collectively", or every "therefore" with "thus"; remove or reconstruct the weak relation.

Do not preserve generic phrases merely because they occur in the exemplar. Expressions equivalent to unspecified great potential, seamless integration, impressive improvement, or an importance-only conclusion need concrete content. Necessary technical terms are not forbidden words.

## Evidence and numerical detail

Keep observation, comparison, interpretation, and causal mechanism distinguishable. Do not turn a diagnostic into a direct error measurement, a stabilized learning curve into proof of optimal training, or a multi-component comparison into an isolated causal attribution.

Retain useful limitations once, where they affect interpretation. Avoid repeatedly defining the contribution through what it does not establish.

Preserve the direction, reference, metric, units, and uncertainty of each result. Main text needs decisive numbers; SI needs complete relevant values and aggregation definitions. The author's preference to avoid tiny percentage-point gains in a cover letter is not a ban on numerical results in papers.

## Equations are grammatical components

A displayed equation belongs to the surrounding sentence. Introduce the quantity or relation; choose punctuation according to how the sentence continues.

Schematic patterns:
~~~
The residual is defined as
r_i = x_i - x_hat_i,
where x_i and x_hat_i denote ...

The two quantities satisfy
a = b + c.
The second term accounts for ...
~~~

Both patterns are legitimate. A colon is optional when warranted by the actual introduction, not a default before every display. "Here" after a completed sentence is valid; "where" is not mandatory. Define symbols, indices, units, and interpretation nearby. Preserve the paper's numbering and actual source correspondence; never print an empty source tag.

## Section-specific scope

- Introduction: prioritize the author's gap-development and answer-mapping habits. Read the dedicated guide.
- Results: lead readers through comparisons and their meaning, not a chronological inventory of author actions.
- Methods: retain operational order, concrete settings, and the actual implementation.
- Discussion: integrate results and design implications without repeating the full Results section.
- SI: reader-facing technical exposition with reproducible boundaries and full statistical meaning.
- Rebuttal: direct answer, necessary evidence, calibrated interpretation, actual revision location; polite but varied openings.

Read section-and-si-style.md when working outside the Introduction.

## Project settings that must not become universal style rules

Keep the following in a paper's own contract or ledger:
- the number of gaps, paragraphs, modules, datasets, or contributions;
- official system/model/device names and acronym expansions;
- whether a section is called main text, manuscript, appendix, or Supplementary Information;
- numerical settings, labels, source equation numbers, and selected precision;
- journal fonts, caption details, numbering, and highlight colors;
- how much detail one particular reviewer needs;
- submission-letter page limits or selection of headline metrics.

Persistent formatting preferences include preserving the requested template, meaningful equation punctuation, readable captions and table headers, and removing only revision marks when producing a clean version. Respect venue or user overrides.

## Update discipline

Do not ask for these preferences again on each paper. Apply them, report material deviations when relevant, and ask only about a new scientific ambiguity or a changed instruction.

Record each new source's role, section, and explicit author weight. Add a reusable rule only when an explicit instruction or recurring pattern supports it. Keep a one-paper observation provisional; an approved correction is stronger evidence than an uncorrected artifact.
