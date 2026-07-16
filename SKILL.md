---
name: manuscript-logic-polisher
description: Reconstruct, audit, and confirm the argument logic of an academic manuscript before revising it; derive a reusable academic style profile from user-provided exemplar papers; and rewrite the confirmed manuscript into submission-ready English while preserving claims, data, citations, equations, and authorial intent. Use for full papers or sections supplied as plain text, Markdown, LaTeX, DOCX, or PDF when the user asks to clarify paper logic, confirm argument relationships, learn wording or transitions from exemplar articles, improve coherence, polish academic language, or prepare a manuscript for journal submission.
---

# Manuscript Logic Polisher

Turn an author draft into a logically explicit, stylistically consistent manuscript. Separate reasoning decisions from language editing and require the author to confirm the argument before full rewriting.

## Non-negotiable rules

- Preserve scientific meaning, numerical values, equations, citations, qualifiers, and uncertainty unless the author explicitly approves a change.
- Never invent evidence, results, mechanisms, citations, limitations, or experimental details.
- Treat exemplar papers as style evidence, not as scientific evidence for the manuscript.
- Learn patterns from exemplars; do not imitate distinctive sentences or reproduce passages.
- Label interpretations and proposed premises as inferences. Do not present them as facts supplied by the author.
- Stop at the confirmation gate before performing a full-manuscript rewrite.
- Keep the author's source file unchanged. Write revisions to a new file unless the author explicitly requests in-place editing.
- Give each sentence one main communicative job. Keep subordinate material only when it qualifies or completes that same job; otherwise split the sentence.
- Vary sentence length intentionally to support reading rhythm. Do not force every sentence into the same short or long template.
- Use logical connectors only for relationships that are actually present, and avoid mechanically repeating the same connector or transition pattern.
- Replace generic AI-sounding praise, inflated abstractions, and formulaic framing with concrete scientific content. Do not ban a term when it has a necessary domain-specific meaning.
- Maintain a concise scholarly register built around synthesis, relationships, and claims. Avoid chronological or conversational narration unless sequence is scientifically necessary, while retaining direct reproducible wording in Methods.

## Choose the operating mode

Infer the mode from the request; ask only when ambiguity changes the deliverable.

- **Full workflow**: logic map, confirmation, exemplar profile, revision, and quality audit.
- **Logic audit**: logic map and confirmation only.
- **Style profile**: analyze exemplar papers without revising a manuscript.
- **Section revision**: run the same confirmation-first workflow at section scale.
- **Post-confirmation revision**: continue from a previously approved logic map and style profile.

## Stage 1: Intake and source control

1. Identify the manuscript, exemplar papers, target field or journal, desired output language, and requested scope.
2. Distinguish source roles explicitly: `manuscript`, `style exemplar`, `scientific evidence`, or `journal guidance`.
3. Ask for missing target-journal or audience information only if it materially affects logic or style. Otherwise state a conservative assumption and continue.
4. Extract DOCX or PDF text with the appropriate document/PDF workflow when available. Preserve LaTeX commands, citation keys, labels, cross-references, math, and tables when editing `.tex`.
5. Record any unreadable, incomplete, or ambiguous source material before analysis.

## Stage 2: Reconstruct the argument

Read [references/logic-and-confirmation.md](references/logic-and-confirmation.md) before analyzing the draft. Copy [assets/logic-confirmation-template.md](assets/logic-confirmation-template.md) when a persistent deliverable is useful.

Build the logic from the manuscript rather than from an idealized paper structure:

1. State the research problem, knowledge gap, objective, central claim, and contribution.
2. Decompose the central claim into necessary subclaims.
3. Map every subclaim to its supporting method, result, figure, table, citation, or reasoning step.
4. Assign a rhetorical function to each section and paragraph.
5. Trace relationships using explicit labels: background, contrast, gap, premise, method, observation, comparison, interpretation, mechanism, limitation, or implication.
6. Flag contradictions, missing premises, unsupported claims, causal overreach, circular reasoning, misplaced content, redundancy, and undefined terms.
7. Distinguish the manuscript's current logic from the proposed improved logic.

## Stage 3: Run the author confirmation gate

Present a compact confirmation packet containing:

1. **My reading of your intended argument** — one central claim and a numbered claim-evidence chain.
2. **Logic issues and uncertainties** — each with location, severity, explanation, and the smallest decision needed from the author.
3. **Proposed revised logic** — reordered or repaired claim chain, with all new inferred premises visibly marked.
4. **Confirmation request** — ask the author to approve, correct, or choose among genuinely different interpretations.

Do not rewrite the full manuscript until the author explicitly confirms the logic. If only minor wording can be improved without depending on an unresolved decision, show at most a short illustrative example and keep it separate from the deliverable.

When the author corrects the map, update it and repeat the gate only for unresolved or materially changed relationships. Treat explicit approval such as “确认”, “按这个逻辑继续”, or an equivalent statement as permission to proceed.

## Stage 4: Learn from exemplar papers

After logic confirmation, read [references/exemplar-style-learning.md](references/exemplar-style-learning.md). Copy [assets/style-profile-template.md](assets/style-profile-template.md) when the profile should persist across tasks or be tracked in Git.

If [references/author-exemplar-style-profile.md](references/author-exemplar-style-profile.md) exists, read it before analyzing new exemplars or revising text for this author. Treat it as a living, provenance-tracked profile: merge new evidence into it, preserve explicit user weighting, and keep unsupported section profiles marked incomplete.

For drafting or revising an Introduction for this author, also read [references/author-introduction-style.md](references/author-introduction-style.md). Prioritize its paragraph-level argument architecture over isolated wording from any exemplar.

1. Check exemplar fit by field, article type, section type, target journal, and publication quality. Down-weight mismatched examples.
2. Extract recurring rhetorical and linguistic patterns, including paragraph moves, topic-sentence placement, information flow, transition functions, stance, hedging, voice, sentence rhythm, terminology, and claim strength.
3. Separate section-specific patterns. Do not apply Methods conventions to an Abstract or Discussion.
4. Record both preferred patterns and patterns to avoid.
5. Support profile claims with aggregate observations from multiple exemplars where possible. Mark single-paper observations as provisional.
6. For LaTeX exemplars, run `scripts/extract_latex_sections.py` first to separate prose by section and remove tables, equations, and layout commands. Then use `scripts/analyze_exemplars.py` for optional surface statistics on the extracted UTF-8 text. Treat all statistics as diagnostic evidence, not as style decisions.
7. Save only the derived profile in the skill/project by default; keep full copyrighted exemplar articles outside the skill repository unless the user intentionally chooses to version them.

## Stage 5: Revise the confirmed manuscript

Read [references/revision-and-qa.md](references/revision-and-qa.md) before rewriting.

Apply three passes in order:

1. **Structural pass**: reorder sections or paragraphs, repair stated premises, remove redundancy, and align evidence with claims according to the confirmed map.
2. **Paragraph pass**: give each paragraph one controlling purpose; create a clear topic sentence, evidence or reasoning sequence, interpretation, and forward link where appropriate.
3. **Sentence pass**: improve precision, concision, grammar, terminology, transitions, information flow, hedging, and journal fit using the derived style profile.

During the sentence pass, read [references/natural-academic-language.md](references/natural-academic-language.md) and apply the persistent author profile when available. Use transitions only when they express a real logical relation. Prefer explicit nouns and verbs over vague references or decorative academic wording. Combine short, medium, and selectively longer sentences according to rhetorical purpose. Preserve a useful authorial voice rather than homogenizing every sentence.

For claims requiring missing evidence, insert a visible author query such as `[AUTHOR QUERY: evidence needed for ...]`; never repair the gap by fabrication. If the confirmed logic requires scientific content that the author has not supplied, pause only that passage and continue with independent sections.

## Stage 6: Deliver and audit

Return:

1. The revised manuscript or section in the requested format.
2. A concise revision report based on [assets/revision-report-template.md](assets/revision-report-template.md).
3. The final logic map and style profile when they were created.
4. A list of unresolved author queries, unsupported claims, and format risks.

Run the quality audit in [references/revision-and-qa.md](references/revision-and-qa.md). Do not claim “submission-ready” if critical logic, evidence, citation, or formatting issues remain; state the remaining conditions plainly.

## File conventions

- Use descriptive sibling names such as `manuscript_logic_map.md`, `exemplar_style_profile.md`, `manuscript_polished.tex`, and `revision_report.md`.
- Preserve citation manager fields and source formatting whenever possible.
- For long manuscripts, work section by section but maintain one master logic map, terminology list, and style profile.
- For repeated use, keep the derived style profile and templates in Git; keep sensitive drafts and licensed exemplar PDFs out of Git unless the author requests otherwise.
