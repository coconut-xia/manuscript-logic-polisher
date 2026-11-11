# Terminology and cross-document consistency

## Purpose and boundary

Preserve the author's scientific nouns and definitions while improving how sentences relate. Repetition of a precise technical term is often useful cohesion. Vary discourse wording when needed; do not rotate a scientific object through attractive synonyms.

Build one project ledger from the current manuscript and any supplied SI, captions, tables, and rebuttal. The ledger belongs to that paper. Do not import model names, measurement values, dataset conventions, hardware, or claims from the author's style exemplar.

The Introduction is the primary author-voice exemplar. It supplies information flow and phrasing tendencies, not authoritative definitions for a different paper.

## Build a small ledger before revising

Use `assets/terminology-ledger-template.json` when a persistent record is useful. Capture only concepts that could drift or have already drifted.

| Category | Record | Inspect across the supplied documents |
|---|---|---|
| Named method or component | Canonical spelling; permitted full and short forms; version or size suffix | Title, abstract, introduction, methods, captions, tables, SI |
| Scientific concept | Definition and referent; deliberately distinct neighboring concepts | Is the same noun naming the same object throughout? |
| Inputs and outputs | Representation, dimensions, channels, coordinate system, units | Does the prose agree with the implemented and evaluated form? |
| Data partitions | Names, allocation unit, role in selection and reporting | Are validation and independent test still distinct? |
| Metric | Quantity, unit, range, averaging basis, threshold | Does a short metric label conceal a different definition? |
| Statistical summary | Experimental unit, repeats, aggregation level, exclusions | Are run means, seed variation, pooled samples, and confidence intervals identified correctly? |
| Symbol or abbreviation | Meaning, full form, subscripts, dimensions, first definition | Is one symbol reused for a different quantity, or one quantity renamed? |
| System stage | Beginning and end; included and excluded work | Do equal names imply equal measurement boundaries? |

A permitted abbreviation is not an error. Do not expand every mention or mechanically insist on the full name. Define abbreviations where the document needs to stand alone; preserve the journal's conventions.

## Separate three kinds of changes

1. **Orthographic consistency.** A hyphen, spelling, capitalization, or an omitted model suffix is wrong for an already unambiguous referent. Correct within the authorized scope and check all supplied uses.
2. **Permitted variation.** The established full name and abbreviation refer to the same entity, or a general description is intentionally broader. Retain both when appropriate.
3. **Semantic disagreement.** The same label means different things, or different labels may hide different protocols. Inspect the source before editing. A terminology substitution cannot resolve a disagreement in science.

Examples of semantic distinctions, not interchangeable synonyms:

- calibration fit and residual displacement after processing;
- relative timing consistency and absolute timing accuracy;
- model execution time and end-to-end response latency;
- throughput and latency;
- sample-level dispersion and dispersion across independent runs;
- a validation result and a held-out test result;
- observed association and a separately isolated mechanism.

These are illustrative distinctions. Apply them only when relevant to the current paper; create the equivalents needed by another field.

## Canonical nouns and flexible discourse

Keep the named subject stable while improving sentence progression:

- A prior sentence introduces a quantity; the next sentence may use that quantity as its subject.
- A paragraph introduces a limitation; the next paragraph can reclaim its name instead of opening with a generic addition marker.
- A concrete noun phrase is useful when `this`, `it`, or `these results` could refer to several objects.
- `Shows`, `indicates`, `suggests`, and `supports` are not decorative synonyms. Choose them by evidence strength.
- Do not replace `accuracy` with `precision`, `robustness` with `generalization`, or `efficiency` with `latency` merely to avoid repetition.
- Do not impose a generic term such as `main text`, a model family suffix, or one table style on another project unless its own contract establishes it.

## Cross-document pass

After revising a section, inspect its shared concepts in the other supplied materials. After a full revision, perform a final cross-document pass.

1. Compare each canonical name and its permitted aliases.
2. Compare definitions, conditions, measurement endpoints, units, and averaging populations.
3. Match numerical statements to the same condition and metric. Do not silently replace one condition's value with another's.
4. Check that Methods describe the configuration actually reported in Results, captions, and SI.
5. Resolve symbols and abbreviations by meaning, not visual similarity.
6. Check figure, table, equation, and section references against their actual subjects and current numbering.
7. Verify that any claimed revision in a supplied response letter exists in the manuscript or SI.
8. Record meaningful conflicts with location and the smallest author decision required. Continue unrelated edits.

When the source is ambiguous, present the conflicting uses. Do not invent a canonical definition, infer an undocumented experiment, or normalize an unresolved disagreement into fluent prose.

## Optional lexical diagnostic

Run only after filling active `terms` in the ledger:

    python scripts/audit_terminology.py --ledger paper_terms.json manuscript.tex SI.tex --format json

Use `--fail-on-match` only when lexical findings should return exit status 1. Invalid input or ledger syntax returns 2. The default audit returns 0 even when variants need review.

The script:

- reads explicitly selected UTF-8 `.tex`, `.md`, and `.txt` sources;
- reports configured watch variants with file, original source line, column, and reason;
- protects configured allowed full and short forms;
- excludes ordinary TeX comments, common macro bodies, reference/citation keys, graphics paths, URL targets, math, and code blocks;
- keeps caption/table prose and the visible label of common links;
- never edits the source, rewrites aliases, changes labels, or changes formatting;
- echoes `concept_checks` as manual-review items rather than claiming to verify their semantics.

`terms[].scope` can limit a rule to file-name/path globs through `files` and `exclude_files`. `case_sensitive` defaults to true. Watch forms may be strings or objects with `form`, `suggestion`, and `reason`. A watch variant is a review finding, not proof that every occurrence is wrong.

## Parser limits and final judgment

This is a lexical aid, not a TeX engine, terminology ontology, or scientific consistency validator. It does not expand custom macros, resolve included files automatically, evaluate mathematical notation, interpret images, or understand units and protocol definitions. Supply included files explicitly. Extract DOCX/PDF through the appropriate workflow before using its text.

Nested custom commands, unusual math delimiters, and document-specific syntax can produce missed or extra matches. Review each finding in context. A report with no lexical matches means only that the configured variants were not found in the scanned text. It does not establish semantic consistency, correct statistics, accurate references, or complete coverage.

Complete the manual definition, metric, symbol, and cross-document pass even when the lexical audit is empty.
