# Speaker notes: slides v2

Total about 11 minutes. These notes are also in the .pptx (View → Notes).

## Slide 1: Design Pattern Final Project (0:20)

Hi, I'm Luay Assidmi. This is my design pattern for the final project: meetings, and the mandates they produce.

This is the deck from my first proposal, revised. I kept the original slides so you can see what I proposed, and then show where the course material changed my thinking: the definitions lecture, Document Acts, and IAO-Intel.

## Slide 2: Proposed Final Project Topic (0:20)

The topic is meetings. More precisely, the decisions made in meetings, and the documents that carry those decisions afterwards.

The reason this is an intelligence problem: an executive who sets priorities, a lot of information spread across many committee files, and no analytic layer connecting them. That's a strategic intelligence problem. Often nobody knows to ask what's already been said.

## Slide 3: Why Meetings? (0:45)

Why meetings? Three reasons.

First, there are a lot of them. Presentations and minutes are the most abundant knowledge an organization produces.

Second, they're already engineered, for humans. Someone chose what goes on each slide. That gives us context, provenance and traceability for free.

Third, the minutes carry action. A chair says "do this", and that becomes a mandate somebody is accountable for.

The goal is to engineer those same documents for machines, so that what was said in one committee can be connected to what was said in another, without losing data quality.

## Slide 4: Design process method (0:35)

My method has five steps.

Step 1 is my own definition in plain words, with no BFO or CCO lens. Step 2 is a BPMN process map.

Steps 3 to 5 I co-author with a Design Pattern Assistant. That's an AI agent I built that looks up every BFO and CCO term in an index of the actual CCO release, and lints each pattern. Step 3 sorts entities into the seven rules-of-thumb slots, step 4 maps them to BFO and CCO, and step 5 is the workshop where we draw the pattern in Mermaid.

The revision today mostly hits steps 1, 2 and 5.

## Slide 5: Step 1: My own definition, tested (1:15)

Step 1. Here's my original definition: a meeting is a human gathering, online or in person, for a determined period of time, to address topics and make decisions, which I called mandates.

After the Military Intelligence lecture I ran the test from slide 5. A definition is a pair: the term and the expression. Assume the term is true and look for a case where the expression isn't. Then the reverse.

It fails both ways.

Term true, definition false: a status briefing where nothing gets decided is still a meeting. So "make decisions" is too strong. And two directors who settle something in a five-minute corridor conversation, with nothing scheduled, also had a meeting. So "a determined period of time" is too strong.

Definition true, term false: a family at dinner deciding where to go on holiday. Human gathering, a period of time, a topic, a decision. Nobody calls that a meeting. Nothing in my definition rules it out.

It passes on negative language, because there are no "not" clauses.

But it fails the word-to-world test in a quieter way: "make decisions (mandates)" treats an act and its output as the same thing. Deciding is something the chair does. The mandate is what that act produces.

## Slide 6: Step 1 revised: v2 definitions (1:00)

So here's version 2, as three definitions.

A meeting is an act of association in which two or more persons, sharing a place or connected through a communication artifact, communicate about topics for a common purpose. The genus comes straight from CCO's Act of Meeting.

A decision meeting is a meeting that has, as a part, an act of directive communication by someone with an authority role, whose output is a mandate.

A mandate is the process regulation produced by that act.

Two things to point out. I dropped "determined period": every meeting takes time, but not every meeting is scheduled. And I moved deciding into a subtype instead of the main definition. That splits the class from the inside, "a meeting that…", so I never need a negative class like "non-decision meeting", which the lecture warned is a false bifurcation.

The table re-runs the cases. Briefing: meeting, not a decision meeting, which is correct. Huddle: both. Family dinner: not a meeting.

What's still open: "common purpose" carries a lot of weight. It's CCO's wording, so I've kept it and flagged it.

## Slide 7: Step 2: Build BPMN map (two acts, not one) (1:00)

Step 2, the BPMN. The map itself hasn't changed, but reading Document Acts changed how I read it.

Look at the accountable lane. There are two tasks: Make Decision, and Document Decisions. My original pattern collapsed them into one node. Barry Smith's paper explains why they're two different kinds of act.

Make Decision is a speech act. It creates the obligation, but only if the felicity conditions hold, and the main one is authority. The chair has to bear the role that makes the directive binding. That's pages 9 to 10.

Document Decisions is a document act. Smith's point is that in a large organization, memory can't carry obligations. Documents extend memory, and they let a deontic power reach people who weren't in the room. On page 6 he traces how "to record" shifted from bearing oral witness to producing a document. The minutes are exactly that shift.

## Slide 8: Step 3: Apply rules of Thumb  (0:25)

Step 3, the rules of thumb. The assistant sorts everything from my definition and the BPMN into seven slots: material entity, quality, process, realizable entity, where, when, and information.

The interesting result here was that the topic is information, not a participant. It's drawn as a lane in the BPMN, but nobody performs it.

## Slide 9: Step 4: Lookup BFO/CCO lenses on to build Design pattern  (0:25)

Step 4. Every term was looked up in an index built from CCO version 2.2, which includes BFO 2020. Each one is marked: exact match, near match, or proposed new term.

For the meeting pattern, every term is an existing CCO or BFO term. No new classes.

## Slide 10: Steps 5 the workshop (0:15)

Step 5 is the workshop. The assistant and I take the slot list and the term mapping, and build the pattern together, with a numbered decision log I can challenge.

## Slide 11: Steps 5 Workshop result: Mermaid (v1) (0:30)

This is the version 1 result I presented. Act of Meeting at the top, with its agent, topic, time and place. In the middle, the act of directive communication, "deciding", which realizes the authority role and outputs the mandate, a process regulation, which requires planned work.

The problem is that middle node. It's doing two jobs, and there's nothing here for the minutes at all. So the pattern can't say where a mandate lives after the meeting ends.

## Slide 12: Step 5 revisited: speech act vs. document act (1:15)

Here's the revision.

Deciding stays as an Act of Directive Communication. That's the speech act. It realizes the authority role and outputs the mandate.

Then a second act, Act of Official Documentation. CCO already has this term, and it's exactly a document act: an agent records information for official use by another agent. My own workshop had used it in step 5; version 1 of the diagram just lost it. I considered Act of Reporting and rejected it, because minutes aren't just a true account. Once recorded, they're what people are held to.

That act outputs the minutes file, which carries the minutes, a CCO Report. And the mandate is part of the minutes, not the same thing. That matters, because the same mandate can also appear in a follow-up letter, or next month's deck.

Last, the identifier. "M06 version 1.1" is a Non-Name Identifier that designates the mandate. More on that next.

I ran the linter on this: 0 errors, 3 warnings. The main warning is that CCO prefers outputs to be physical carriers. I kept the mandate as the output anyway, because CCO's own definition of process regulation says it's the output of an act that realizes an authority role.

## Slide 13: Identifiers reveal recurrence (1:00)

Why the identifier matters. Page 10 of Document Acts talks about knowledge by comparison. Tracking numbers and VINs create what Smith calls "virtual attachment" between documents: the same number in many documents ties them to one thing.

Mandate IDs work the same way. M06 appears in the minutes, in a follow-up letter, in a tracker. Three documents, one mandate. No document has to point to another document.

And comparing versions is where the intelligence is. This is synthetic data, but it has the shape of a real file. Three directives were issued twice. M06 version 1.0 asked to see the operating model. Version 1.1 asked for the gaps, the fixes, and a resubmission. The chair had to say it twice, and asked for more the second time.

In the pattern, each version is a separate mandate linked by "precedes". I never overwrite version 1.0, because the fact that it had to be said twice is the signal.

## Slide 14: File Engineering aligned to IAO (1:00)

Last change: File Engineering, the method I use for real files, aligned to IAO.

The decision is that CCO is the import and IAO is an alignment. IAO and CCO cover the same ground, so importing both would give me two competing "document" classes. Instead, each class gets a skos close-match or exact-match to its IAO counterpart, so IAO-based tools can still find the data.

This follows IAO-Intel. Smith and colleagues populate downward from IAO: Intelligence Report under IAO Report, and so on through the Army report types. I do the same with an executive office's own document types. Minutes, محضر, are an exact match to IAO report, which IAO defines as the output of a documenting process. Letters and presentations sit under IAO document. The directive, توجيه, sits under directive information entity.

Two limits. People stay in CCO, because IAO only covers information. And IAO's version number is defined for manufactured products, so versions live in the identifier instead.

## Slide 15: Course material applied in this revision (0:45)

To sum up, three readings changed the proposal.

The definitions lecture took my Step 1 apart and gave me three tighter definitions. Document Acts split one act into two, and added the identifier that makes recurrence visible. And IAO-Intel gave me the method for aligning my document types without importing a second ontology.

Every term is checked against the CCO and IAO source files, and the IRIs are in the write-up in my GitHub folder.

What's next is implementation: the pattern in OWL as a Turtle file, synthetic test data, a reasoner check, and SPARQL queries for the competency questions. For example, "which mandates has the chair had to issue more than once?" That's what turns this design pattern into the final project.

Thank you.
