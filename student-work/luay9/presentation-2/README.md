# Presentation 2: Meeting & Mandate, implemented and made extendable

| File | What it is |
|---|---|
| [`Assidmi_Luay_Presentation_2_slides_v3.pdf`](Assidmi_Luay_Presentation_2_slides_v3.pdf) | **The deck, 2026-11-11.** Slides 1–15 are the Presentation 1 revision (v2), with the close of slide 15 updated. Slides 16–21 are new. (`.pptx` alongside) |
| [`speaker-notes.md`](speaker-notes.md) | Script for slides 15–21. The notes for slides 1–14 are in [`../presentation-1/speaker-notes.md`](../presentation-1/speaker-notes.md) |
| [`../presentation-1/course-reflection/04-sustained-extendability.md`](../presentation-1/course-reflection/04-sustained-extendability.md) | The write-up: the definition and its tests, depth / breadth / language, the loop, the five rules, the course readings, the results and the limits |
| [`../final-project/ontology/BUILD.md` §7](../final-project/ontology/BUILD.md) | How it was implemented and tested: `documents/` D01–D07, `ingest.py`, and `results/extendability/` |

## What Presentation 2 adds, against the brief

| The brief asks for | Where |
|---|---|
| What changed since Presentation 1 | Slide 15: the pattern is implemented (v0.1, 17 Oct). Slides 16–17: a new principle, *sustained extendability*, defined and tested like *meeting* |
| What motivated the change | One meeting is not the problem; a meeting every week is. Without the principle, each document becomes its own graph, or the ontology has to be redesigned each time (slide 16) |
| What ontology content is implemented | Slide 19: Program A split into 7 synthetic documents, each one a named graph |
| How the model was evaluated | Slides 19–20: HermiT and CQ1–CQ5 after every document; 0 regressions; the final answers equal the one-shot build; D07 rejected; X01/X02/X04/V04 on the named graphs |
| What remains uncertain | Slide 21: synthetic and small; provenance stops at the document; the regression test covers only what the CQs ask |
| How it becomes the Final Project | Slide 21: the packet, plus the same loop run on a real file |

All the data is synthetic. No real organization, people or documents appear here.
