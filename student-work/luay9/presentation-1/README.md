# Presentation 1: Meeting & Mandate design pattern

| File | What it is |
|---|---|
| [`Assidmi_Luay_Design_Pattern_Final_Project_1_slides_v2.pdf`](Assidmi_Luay_Design_Pattern_Final_Project_1_slides_v2.pdf) | **The deck, revised 2026-10-17.** Read this first. (`.pptx` alongside) |
| [`speaker-notes.md`](speaker-notes.md) | Script for each slide with timings (about 11 min). Also in the .pptx notes |
| [`course-reflection/01-definition.md`](course-reflection/01-definition.md) | Step 1: my definition tested against *Military Intelligence Part 1* (definitions as ⟨T, E⟩, counterexamples, negative language), with the v2 definitions |
| [`course-reflection/02-document-acts.md`](course-reflection/02-document-acts.md) | Steps 2 and 5: *Document Acts* applied. Deciding (speech act) and documenting (document act) are split, and the mandate identifier is added. Revised pattern + lint |
| [`course-reflection/03-file-engineering-iao-alignment.md`](course-reflection/03-file-engineering-iao-alignment.md) | File Engineering (the method behind the pattern) aligned to IAO, following IAO-Intel. Synthetic timeline |
| [`course-reflection/04-sustained-extendability.md`](course-reflection/04-sustained-extendability.md) | **Next step (2026-11-11):** sustained extendability. Every new deck or set of minutes adds depth, breadth or language to the base without breaking it. Course readings applied, implemented and tested in `final-project/ontology/` (BUILD.md §7). Presented in [`../presentation-2/`](../presentation-2/) |
| [`course-reflection/pattern-v2-triples.tsv`](course-reflection/pattern-v2-triples.tsv) | The revised pattern as triples (lint: PASS, 0 errors) |
| [`design-pattern-assistant/`](design-pattern-assistant/) | Steps 3–5 as presented on 2026-09-29: slot sort, BFO/CCO mapping, workshop |
| [`diagrams/`](diagrams/) | `Meeting.bpmn` (open at <https://demo.bpmn.io>), pattern v1 and v2, synthetic timeline |

## What changed between the recording and v2

| Slide | Change | Course material |
|---|---|---|
| 5 → 5, 6 | Definition tested; v1 fails two counterexamples and is too broad. Revised into *meeting* + *decision meeting* + *mandate* | Military Intelligence Part 1, slides 4–32 |
| 7 (BPMN) | *Make Decision* marked as the speech act and *Document Decisions* as the document act | Document Acts, pp. 6, 9–10 |
| 12 (new) | Pattern v2: `Act of Official Documentation` → minutes file → minutes ⊃ mandate; `Non-Name Identifier` designates the mandate | Document Acts, pp. 9–10 |
| 13 (new) | Identifiers make recurrence (M06 v1.0 → v1.1) visible across documents | Document Acts, p. 10 |
| 14 (new) | File Engineering classes aligned to IAO (CCO stays the import) | IAO-Intel |
