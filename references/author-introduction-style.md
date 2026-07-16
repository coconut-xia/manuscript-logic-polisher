# Author Introduction style

## Provenance and priority

Derive this profile from the author-polished Introduction of *Full-Stack UAV Detection Pipeline from Precise RGB-Event Sensing to Efficient Edge Processing*. Use it as the primary author-voice anchor for future Introduction work. Use other high-quality exemplars to test journal fit, not to overwrite this architecture.

## Seven-paragraph argument architecture

### 1. Establish the real problem and motivate complementarity

Open with the task-level difficulty, then specify the physical and observational causes. Narrow from general UAV detection to the more difficult air-to-air setting. Introduce RGB and event sensing through complementary failure modes: state what each modality preserves, where each fails, and why fusion follows logically. End with the system capability that complementarity should enable.

### 2. State the paired research gaps

Compress the field-level gaps into two explicit limitations: data/sensing quality and accuracy/efficiency on edge hardware. Give each one a short explanation, then synthesize them into the need for a unified hardware-to-deployment paradigm. Do not introduce contributions yet.

### 3. Establish the dataset and alignment gap

Review prior datasets chronologically only when the chronology shows a research shift. Move from event-only resources to RGB-Event resources, then from general autonomous-driving datasets to UAV-specific benchmarks. Evaluate the closest benchmarks against exact criteria: spatial alignment, temporal synchronization, viewpoint coverage, and controlled perturbations. End with the scientific consequence of those deficits for small, fast targets.

### 4. Establish the model and deployment gap

Frame the second gap as a trade-off. Contrast expressive but expensive architectures with efficient but single-modality designs. Add the representation and preprocessing cost that model-only comparisons omit. Review hardware-aware systems, then explain why their task settings do not solve standard multimodal UAV detection. End with the required design property: accurate, modality-aware, and edge-deployable fusion.

### 5. Present the sensing and dataset contribution

Return to the two gaps in the same order. Introduce the full-stack pipeline, then detail the dataset contribution first. State scale, sensor configuration, alignment mechanisms, viewpoint coverage, real/synthetic composition, and the distinct purpose of the synthetic subset. Use numbers as evidence, not decoration.

### 6. Present the model contribution

Connect the model to the dataset with an explicit dependency such as `Building upon this dataset`. Name the model and its edge objective. Present components in functional order, giving each component one failure mode and one role. End with the evaluation scope and the combined accuracy-efficiency claim.

### 7. Close the system loop

Move beyond benchmark performance to hardware implementation. State the complete sensing-to-processing integration, acceleration setting, and system-level throughput. End by returning to the full-stack thesis: practical performance requires joint optimization across sensing, fusion, and processing.

## Paragraph-internal progression

- Begin with a strong topic sentence that defines the paragraph's argumentative role.
- Move from claim to concrete mechanism, benchmark class, or system constraint.
- Use contrast to expose a trade-off or complementary failure mode, not merely to vary rhythm.
- End each gap paragraph with a requirement and each contribution paragraph with evidence or scope.
- Preserve the same order between gaps and contributions so the solution visibly answers the problem statement.

## Sentence rhythm and density

The current Introduction contains 51 sentences across 7 paragraphs, with a median of about 21 words and a 90th percentile near 27 words after LaTeX cleanup. Treat these as observations, not targets. Most sentences express one claim or relation; longer sentences carry one comparison with tightly linked qualifications. Short sentences establish paragraph direction or isolate one limitation. Do not create mechanical length alternation.

## Cohesion pattern

Use functional transitions sparingly and consistently:

- contrast or boundary: `Although`, `however`, `while`, `in contrast`, `nevertheless`;
- paired structure: `First` / `Second`, followed by paragraphs explicitly developing the first and second limitation;
- solution response: `To address these challenges`;
- dependency: `Building upon this dataset`;
- system extension: a direct deployment-led topic sentence rather than a generic addition marker;
- closure: `Overall` only for the final full-stack synthesis.

Prefer repeated technical concepts such as alignment, modality complementarity, edge constraints, and full-stack integration over synonym rotation. Do not begin successive paragraphs with generic `Moreover`, `Furthermore`, or `Additionally`.

## Claim calibration

- Tie dataset claims to measured scale, coverage, alignment, or controlled variation.
- Tie model claims to named components and cross-dataset experiments.
- Tie deployment claims to model-only and end-to-end throughput separately.
- Use broad practical claims only after the complete sensing-to-processing evidence chain is stated.
- Preserve limitations and trade-offs; do not make every reviewed method sound uniformly inadequate.

## Anti-template filter

Learn the architecture and voice, not every isolated phrase. Replace generic formulations such as unspecified `great potential`, `seamlessly integrates`, or importance-only conclusions when the same point can be expressed through a concrete capability, dependency, or measured outcome. Retain such wording only when the surrounding evidence makes it precise and non-detachable.

## Introduction audit

Confirm that the Introduction:

1. defines the physical problem before presenting methods;
2. explains why RGB and event sensing are complementary;
3. separates dataset/alignment and model/deployment limitations;
4. reviews the nearest work against explicit criteria;
5. mirrors each limitation with a corresponding contribution;
6. distinguishes benchmark, model, and system-level evidence;
7. ends with the full-stack thesis rather than a generic novelty claim.
