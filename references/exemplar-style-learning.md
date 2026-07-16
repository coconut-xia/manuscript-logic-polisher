# Exemplar-based academic style learning

## Principle

Build a project-specific style specification from observable patterns. This is analysis and guided transfer, not model fine-tuning. Transfer rhetorical functions and aggregate language tendencies, not distinctive wording.

## Select and weight exemplars

Rank each exemplar on:

1. Same research field and audience.
2. Same article type: research article, methods paper, review, perspective, or letter.
3. Same section type as the text being revised.
4. Same target journal or a closely comparable journal.
5. Similar methodological and evidential culture.

Use at least three comparable exemplars when available. If only one is supplied, describe the profile as provisional and avoid treating idiosyncrasies as journal rules.

## Extract patterns by dimension

### Rhetorical organization

- order of moves within Abstract, Introduction, Results, Discussion, and Conclusion;
- location and directness of the research gap;
- how objectives, contributions, limitations, and implications are introduced;
- whether paragraphs move general-to-specific, evidence-to-interpretation, or comparison-to-explanation.

### Cohesion and transitions

Classify transitions by function rather than word list:

- addition;
- contrast or concession;
- cause or consequence;
- evidence or example;
- comparison;
- temporal or procedural sequence;
- reformulation;
- limitation;
- implication.

Record where an explicit connector is typical and where lexical continuity or sentence structure carries the relation. Avoid inserting connectors into relationships that are not logically present.

### Stance and claim calibration

Record how exemplars distinguish observation, interpretation, mechanism, and speculation. Track hedging, confidence, attribution, limitations, and the treatment of negative or non-significant findings.

### Syntax and information flow

Record approximate sentence-length range, clause density, active/passive balance, subject choice, old-to-new information flow, paragraph length, and variation in sentence openings.

### Lexis and terminology

Record preferred domain terms, reporting verbs, comparison verbs, evidence verbs, evaluative adjectives, nominalization density, abbreviations, and phrases to avoid. Prefer stable terminology over superficial variation.

## Derive the profile

For every profile rule, record:

- the pattern;
- section scope;
- strength: strong, moderate, or tentative;
- aggregate basis: number of exemplars or corpus statistic;
- application guidance;
- exception or misuse risk.

Separate three categories:

1. **Journal/field convention** — repeated across comparable exemplars.
2. **Author-compatible preference** — improves fit without erasing the author's voice.
3. **Single-exemplar feature** — provisional and not automatically transferred.

## Copyright and provenance

- Do not store full exemplar text in the skill by default.
- Do not reproduce memorable sentences or extended passages.
- Quote only short fragments when necessary to explain a pattern, identify the source, and prefer paraphrase.
- Generic academic collocations may be recorded, but never assemble a revision by patchwriting source phrases.
- Keep a list of exemplar filenames or citations used to derive the profile so the analysis is auditable.

## Optional corpus analysis

Run:

```bash
python3 scripts/analyze_exemplars.py article1.txt article2.md article3.tex --format markdown
```

The script measures surface features such as sentence length, paragraph size, transition categories, hedges, boosters, first-person usage, and a rough passive-voice proxy. Manually interpret every result in context; small corpora and formula-heavy LaTeX can distort counts.
