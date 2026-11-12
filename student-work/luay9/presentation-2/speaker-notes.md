# Speaker notes: Presentation 2 (slides v3)

Slides 1–14 are unchanged from v2. Their notes are in [`../presentation-1/speaker-notes.md`](../presentation-1/speaker-notes.md). Slide 15's close is rewritten, and slides 16–21 are new. Slides 16–21 take about 6.5 minutes, so the whole deck runs about 17 minutes. The notes are also in the .pptx (View → Notes).

## Slide 15: Course material applied in this revision

To sum up, three readings changed the proposal.

The definitions lecture took my Step 1 apart and gave me three tighter definitions. Document Acts split one act into two, and added the identifier that makes recurrence visible. And IAO-Intel gave me the method for aligning my document types without importing a second ontology.

Since then the pattern is implemented: version 0.1 in OWL, on an extracted BFO and CCO module, with HermiT and five SPARQL competency questions passing. But a pattern for one meeting isn't enough. An office has a meeting every week. So the next question is how each new document makes the base stronger instead of starting a new one.

## Slide 16: Next step: sustained extendability (1:00)

The pattern models one meeting. But an executive office produces a meeting every week: a deck before it, minutes after it, letters following up. If I model each document on its own, I get a pile of small graphs that don't know about each other. If I redesign the ontology every time a new kind of document turns up, nothing stays stable.

So the principle I'm adding is sustained extendability: every new presentation or set of minutes makes the base deeper or wider.

There are three ways a document can add. Depth: new facts about things already in the base. Meeting 4 re-issues three mandates, and those new acts link back to acts from the first two sets of minutes, which are never edited. Breadth: a new branch. The first deck brings in the programme objectives. And language: the organization's own words for things the base already has. Mahdar and MoM for minutes, takleef and directive for mandate.

That third one is the point. Every document is evidence of how the organization represents its own knowledge.

## Slide 17: Defined and tested like “meeting” (1:00)

I defined it the same way as meeting, as a pair, term and expression, and looked for counterexamples.

My first attempt said: each new document can be added without changing earlier assertions.

Definition true, term false: a document store. Every file is added and nothing changes, but nothing is integrated either. Adding is not extending.

Term true, definition false: a later set of minutes says M06 was re-issued. The base has to change, because something new is known. What mustn't happen is overwriting.

And 'without changing' is negative language, which the lecture warned about.

So version 2 says what is kept: one fixed loop that links what a document contributes to what's already there, while every earlier assertion and every earlier answer to the competency questions is kept. 'Links' rules out the document store. 'Every earlier answer' is a test I can actually run.

## Slide 18: One loop per document, after JDO (1:15)

Where did the loop come from? Mostly from the Joint Doctrine Ontology reading.

JDO is built incrementally, one joint publication at a time, in three steps. Enrichment: add the terms a publication uses that the glossary doesn't define. Logical regimentation: rewrite the definitions by the rules. Formalization: OWL.

I treat each meeting document as a joint publication. Harvesting and reconciling terms is enrichment. Classifying, with the T-E test, is regimentation. Modelling, only when a question needs it, is formalization. Then four steps JDO doesn't need, because I'm loading facts, not just terms: assert into the document's own named graph, compare, test, and release, which a person decides.

JDO also points out that doctrine stayed consistent because every publication used the same general terms. Minutes have the same property: every set says chair, mandate, minutes.

Underneath are five rules. One named graph per document. A new class only when a question needs it. Never overwrite. Every new class under BFO or CCO. And no IRI carries a project code.

## Slide 19: Implemented: one document at a time (1:15)

This is implemented. The same synthetic Program A as in version 0.1, but now split into seven documents and loaded one at a time, in meeting order. After each one, a script merges it onto everything accepted before, reasons with HermiT, and re-runs the five competency questions.

Read the table top to bottom. The first minutes found the base: 11 classes, all CCO or mine from the pattern. The second minutes reuse 8 of 8: pure depth. The deck is breadth: objectives and presentations appear for the first time, and the word KPI is parked in the vocabulary because no question needs it. Meeting 4's minutes are where CQ1 first returns anything. Recurrence can't be seen in any single document; it only appears when a later document is linked to earlier ones. And the letter is mostly language.

Three results. No document needed a new OWL class. Nothing broke: zero regressions, and after the sixth document the answers are identical to loading everything at once. And document 7 was rejected by the reasoner.

## Slide 20: Named graphs, and a rejected document (1:00)

Keeping one named graph per document gives me questions about the documents themselves.

Provenance: M06 version 1.1 is known from two documents, the minutes and the letter. Every other mandate rests on a single set of minutes, which for an analyst is a confidence signal. What changed: D05 added six facts to things the base already knew, three precedes links and three links from the deck's objectives. Nothing was overwritten. And which words each document brought in.

On the right, the rejection. Document 7 says M06 version 1.1 is a planned act. That's the most common mistake in real minutes: confusing the mandate with the work it requires. HermiT finds it inconsistent: the minutes have M06 as a continuant part, so it's a continuant; a planned act is a process, so an occurrent; and BFO makes those disjoint. The document is rejected and the base stays as it was. The upper ontology is doing quality control.

## Slide 21: Course material applied to extendability (1:00)

To close: where each idea came from. Joint Doctrine Ontology gave the loop: incremental, one publication at a time, enrichment, regimentation, formalization. Ontology for the Intelligence Analyst gave the stability requirement: terms keep their place even when whole new branches are added, and one preferred label per type, which is why new words go into labels and not new classes. IAO-Intel: coverage determined incrementally, from requests and from the terms in the documents. C3O: breadth arrives as modules under CCO. Sikos: one named graph per data source. And Falsehoods About Names: names aren't unique or stable, and neither are an organization's terms.

The limits. The data is synthetic and small, so this shows the mechanism, not a trend. Provenance stops at the document; real minutes need a page and a quote for every assertion. And the regression test protects only what the questions ask.

Next is the final project packet, and running this loop on a real file.

Thank you.
