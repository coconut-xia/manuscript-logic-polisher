# Section-specific and SI style

Use the author profile as the shared voice. Adapt the reasoning function to the section; do not impose the Introduction's structure on technical exposition.

## Abstract

Condense the actual research chain: concrete obstacle, proposed work, essential design or method, decisive evidence, and bounded contribution. A contribution may combine several stages when the paper really does so. Do not manufacture a pipeline or a catalogue of three contributions.

Keep representative results and the conditions needed to understand them. Do not introduce every configuration, minor margin, acronym, or revision-history detail.

## Results

Organize by evaluated scientific questions and meaningful comparisons. Give the reader enough setup to understand the comparison, state the main result, and explain what follows under the evaluated conditions.

- Keep the metric, baseline, population/condition, and direction of change adjacent.
- Distinguish evidence from its possible explanation.
- Report lower scores, trade-offs, failed runs, and non-monotonic observations directly.
- A figure pointer supports a finding; avoid walking through panels without saying what they establish.
- Do not restate every table cell. Select decisive comparisons, trends, and exceptions.
- Do not append the same "these results demonstrate" conclusion after each paragraph.
- Relate a later control or secondary analysis to the question left by the preceding comparison.

Merge paragraphs that fragment one explanation; keep genuinely different questions distinct. There is no fixed paragraph length.

## Methods

Follow the actual flow of information or operations: object/input, configuration, operation/definition, output, and relevant rationale.

Explain implementation facts precisely. A representation's channels, the tensor shape, preprocessing, training, and deployment should describe the same implementation where they are shared. Do not reconcile a discrepancy by silently rewriting a scientific fact.

Specify conditions that change interpretation or reproducibility. Framework defaults without a demonstrated role are not automatically worth listing. Keep necessary operational detail even when a more abstract sentence sounds elegant.

Introduce equations as quantities or relations within the sentence. Define symbols close to first use; identify units, coordinate systems, index domains, and parameter meaning where relevant. Preserve the source's distinction between a definition, a model assumption, and an empirical observation.

## Discussion

Develop what the results mean for the central claim and design choices. Reconnect related findings, explain observed trade-offs, and identify the supported implications.

A possible mechanism remains an interpretation unless directly isolated. Do not repeat all numerical Results, introduce unreported evidence, or add generic limitations merely to sound cautious. Necessary boundaries belong near the inference they constrain or in a coherent limitations passage.

Future work should address a specific remaining issue. A generic promise is not an informative ending.

## SI as a reader-facing technical document

An SI Note explains a scientific object, method, evaluation, or supporting analysis. It is not a record of conversations with reviewers.

### Purpose and arrangement

- Open with the concrete purpose or measured object.
- Use stable experiment names. "New dataset/new validation set" is not appropriate merely because something was added during revision.
- Use the main text's first-citation order when that is the chosen project convention; keep related figures, tables, equations, and response references synchronized.
- Keep shared definitions in one clear home and refer to them elsewhere.
- Provide brief context when required for independent understanding; do not remove essential information solely to avoid all repetition.

### Protocol boundaries

Write enough to establish what comparison was made:
- sample source, selection and exclusion/acceptance rules;
- changed variable and controlled variables;
- training versus evaluation conditions and checkpoint selection;
- coordinate system, resolution, timing anchor, representation, or precision where relevant;
- baseline configuration and the level at which it is matched;
- how raw observations become the reported metric.

Do not require all of these for every experiment. Include the settings that actually affect its interpretation.

### Metric and statistical meaning

For a derived metric, explain its physical/statistical object, formula, unit, and aggregation. Distinguish per-element, per-pair, per-frame/block, per-recording, per-seed, and per-run quantities rather than calling all of them "mean error."

Keep sources of variation separate:
- training-seed variation;
- one fixed checkpoint evaluated under several inputs;
- repeated timing runs;
- sampling uncertainty and confidence intervals.

Identify exceptional sample sizes or non-convergence. Explain accepted-subset coverage and do not generalize its estimate to the entire population by wording alone. Differences computed before rounding need not equal the subtraction of rounded display values; explain when it matters.

### Controls and interpretation

A known perturbation, negative control, or independent measurement should be motivated by the reliability question it answers. Explain what the control supports and what it leaves unresolved.

Keep conceptual distinctions intact: a calibration fit versus a processed discrepancy, temporal consistency versus absolute accuracy, computational counts versus measured runtime, or throughput versus per-result latency. These are examples of the general rule, not a mandatory list for every paper.

### Prose, tables, and links

Put complete values in tables and use prose to interpret trends, key comparisons, and exceptions. Avoid duplicating an entire table.

Shorten overloaded row/column names and explain the measurement in a caption or nearby definition. Use real row/column spans for shared headings when the format permits them. Preserve numbers and content during a formatting-only request.

A caption needs a descriptive title and enough explanation to decode the figure/table: panels, metrics, units, statistical summaries, and essential conditions. It need not repeat the full protocol or Results discussion. Preserve the venue's typography; do not impose one paper's font/size on all future papers.

Use repository links for material that must be downloaded or identified. Do not replace an explanatory SI with repeated links or unnecessary release-history paragraphs. Detailed metadata tables can be appropriate when scientifically useful.

## Rebuttal mode, when requested

Answer the specific concern at the start. Briefly acknowledge a real issue or the usefulness of a suggestion when appropriate, then explain the action and key conclusion before expanding the evidence.

- Use "your" for a direct response to the individual reviewer; retain reviewer labels when describing reports in a letter.
- Avoid identical thanks/agreement openings for every comment and colloquial "you are correct."
- Match detail to the concern; do not turn one reviewer's need for detail into a universal length rule.
- Make complementary experiments form an explicit chain.
- Write a Revision statement as connected prose about actual change locations. Quote selectively when the exact amended wording matters.
- Explain revision highlighting once at the beginning, rather than repeating it in every block.
- Reproduce a given figure/table once within the response document, then cross-reference it.
- Preserve the response's independent numbering and include real main-text/SI source numbers when appropriate. Do not attach a fictitious source number to a response-only derivation.
- Do not copy every marked paragraph into the response or create a separate Revision block after every caption.

Summary comments usually need one courteous paragraph. Minor issues can be brief; important scientific concerns need sufficient supporting evidence.

## Clean and marked versions

Track revision styling separately from normal document styling. A clean version removes revision marks; it preserves ordinary reference/link colors, scientific figure colors, table semantics, emphasis, and template settings. Avoid nested redundant highlight wrappers.

Remove obsolete process notes only when requested or part of finalization. Preserve functional LaTeX percent signs, commands, labels, citation keys, and compilation behavior.
