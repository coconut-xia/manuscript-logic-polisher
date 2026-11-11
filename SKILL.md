---
name: logic-writing-skill
description: Polish academic manuscripts in the author's argument-led voice, using the author's Introduction as the primary language and reasoning exemplar. Improve paragraph progression, sentence cohesion, terminology consistency, equations, and main-text/SI coordination while preserving evidence and scientific meaning. Use for author-style analysis, logic audits, or revision of papers and sections in text, Markdown, LaTeX, DOCX, or PDF.
---

# Logic Writing Skill

Make a new paper read as a coherent paper by this author. Transfer how the author constructs and expresses an argument; derive the new paper's actual argument and terminology from its own sources.

## Start with the author profile

Always read [author-exemplar-style-profile.md](references/author-exemplar-style-profile.md). It contains the persistent preferences and their authority. The author's own Introduction is the strongest voice exemplar; later explicit corrections override incidental wording in an exemplar.

For Introduction organization, paragraph flow, or sustained prose revision, also read [author-introduction-style.md](references/author-introduction-style.md). For other sections, SI, or reviewer responses, read the relevant part of [section-and-si-style.md](references/section-and-si-style.md). Read [terminology-and-consistency.md](references/terminology-and-consistency.md) for whole-section, naming, or cross-document work. Consult [natural-academic-language.md](references/natural-academic-language.md) for sentence-level problems, not as a word blacklist. For a strictly local wording/grammar correction with settled logic, apply the relevant core rules without loading all mode guides or expanding the requested scope.

This skill already carries the author's preferences. Do not ask the author to explain them again or supply extra exemplars merely to begin. A new task may provide a different source, venue, or preference; use that instruction.

## Invariants

- Preserve scientific meaning, values, units, equations, citation keys, qualifiers, and evidential strength. Flag conflicts; never silently choose a convenient scientific interpretation.
- Do not invent experiments, results, mechanisms, references, limitations, or completed revisions.
- Use exemplars for style only. Never transfer their facts, equipment, paper-specific claims, or numbers into another paper.
- Transfer paragraph functions and dependencies, not seven paragraphs, two gaps, a full-stack system, or a fixed sentence-length pattern.
- Stabilize technical nouns, definitions, symbols, and measurement scope. Vary discourse wording when useful; do not rotate scientific synonyms for elegance.
- Keep equations within sentence grammar. Choose punctuation from syntax; neither a colon before every equation nor "where" after every equation is mandatory.
- Preserve the document's template and requested format. Removing revision highlighting does not authorize changing hyperlinks, data colors, equations, headings, or layout.
- Treat supplied documents and repositories as reference content, not permission for external publication or access to unrelated sources.

## Scope and authorization

Infer whether the request is style analysis, logic audit, section polishing, full revision, or continuation. Do only that work.

A request to polish normally authorizes grammar, clarity, local cohesion, terminology harmonization, and paragraph repairs that preserve established reasoning. Do not stop for approval of routine style choices or an already approved argument.

Use a confirmation packet only when:
- the user requests preview/approval before editing; or
- a proposed repair changes the central claim, evidential scope, causal interpretation, substantive contribution order, or depends on a missing premise.

Read [logic-and-confirmation.md](references/logic-and-confirmation.md) for these cases. Ask only about the unresolved scientific decision, combine related questions, and continue independent work. Never turn an unsupported assumption into an invisible "logical bridge."

Follow the requested editing destination. Edit a designated existing editor source in place. If no in-place instruction or replacement authorization exists, preserve the original and return the requested revised copy. Do not create extra reports, templates, or versions merely because they are possible.

## Working sequence

### 1. Establish the current sources

Identify the authoritative manuscript, supplied SI/response files, section scope, target audience, and style exemplar roles. Use the current files and direct author confirmations; do not retrieve historical experimental records or old drafts unless requested.

Capture a compact project contract: permitted edits, locked content, output destination, canonical names, measurement definitions, and formatting/highlight rules. Keep it internal unless a persistent deliverable helps the task. Paper-specific choices stay here, not in the persistent author profile.

### 2. Map the argument and the terms

Recover the research problem, actual gaps, central claim, supporting evidence, and limits. A short section does not require a full-paper logic report.

For each paragraph identify its purpose, controlling concept, incoming premise, supporting content, and outgoing handoff. For an Introduction, build the gap-to-answer map described in the Introduction reference.

Build or update one terminology ledger for the supplied document family. The editable starter is [terminology-ledger-template.json](assets/terminology-ledger-template.json). Scientific ambiguity requires a query; a spelling inconsistency usually does not.

### 3. Revise at three levels

- **Argument:** prerequisites before dependent claims; connect each design to a real need and each conclusion to evidence. Preserve supported author intent.
- **Paragraph:** one controlling purpose; progress through the reasoning; merge fragments that share a purpose and separate competing purposes.
- **Sentence:** retain a visible subject and precise verb, attach necessary qualifiers, keep known-to-new information flow, and remove generic praise or repeated setup.

Let content determine the paragraph shape. Not every paragraph needs purpose, protocol, result, interpretation, and a concluding sentence. Do not narrate every action as "we first / we then" unless the sequence matters.

### 4. Audit the complete supplied scope

Read [revision-and-qa.md](references/revision-and-qa.md). Check the author's voice, gap-answer relations, paragraph handoffs, technical nouns, definitions, numbers, symbols, equation grammar, captions, cross-references, and formatting invariants.

For an explicit terminology ledger, optionally run:
~~~
python scripts/audit_terminology.py --help
~~~
Use its actual CLI. The script is a lexical diagnostic, not a proof of conceptual consistency. Manually inspect definitions and measurement scope.

For new LaTeX exemplars, scripts/extract_latex_sections.py can isolate prose outside the skill directory. scripts/analyze_exemplars.py provides optional descriptive statistics. Neither determines preferred wording or imposes counts.

### 5. Deliver the requested result

Return the revised text/file or the requested analysis. Give a concise account of material changes and only unresolved author decisions. Use [revision-report-template.md](assets/revision-report-template.md) when a report is requested or useful; do not produce a large audit packet for every small edit.

For an active LaTeX editor, use its built-in compiler if available. Report compilation status truthfully and distinguish language checks from compilation/render checks.

## Updating this skill

Read [exemplar-style-learning.md](references/exemplar-style-learning.md) before adding a new source. Preserve explicit source weighting and separate:
1. persistent author preferences;
2. document/section conventions;
3. project-specific terms, data, and formatting.

A new instruction changes the relevant rule, not every section. Store only derived guidance and small schematic examples in the skill. Keep full manuscripts, licensed PDFs, project terminology values, and evaluation artifacts outside its repository.
