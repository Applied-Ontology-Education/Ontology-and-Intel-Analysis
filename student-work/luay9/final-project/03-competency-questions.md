# Competency questions

The competency questions decide what goes into the ontology. A class or relation that no question needs stays out. Each question below names the terms that answer it and the SPARQL file that runs it against the reasoned ontology (`ontology/meeting-mandate-full.ttl`).

New terms use the prefix `:` (`https://github.com/luay9/meeting-mandate#`). Everything else is a CCO or BFO term, extracted into `ontology/cco-module.ttl`.

| # | Competency question | Classes | Relations | Query |
|---|---|---|---|---|
| CQ1 | Which mandates has the chair had to issue more than once? | `:Mandate`, `:MandateIdentifier`, `cco:Act of Directive Communication` | `cco:has output`, `bfo:precedes`, `cco:designates` | `queries/cq1.rq` |
| CQ2 | Who issued a given mandate, and in virtue of what role? | `cco:Person`, `cco:Authority Role`, `cco:Act of Directive Communication` | `cco:has output`, `cco:has agent`, `bfo:realizes`, `bfo:bearer of` | `queries/cq2.rq` |
| CQ3 | Which documents carry a given mandate? | `:MeetingMinutes`, `:OfficialLetter`, `cco:Information Bearing Entity`, `:MandateIdentifier` | `bfo:has continuant part`, `bfo:is carrier of`, `cco:designates` | `queries/cq3.rq` |
| CQ4 | Which meetings are decision meetings? | `cco:Act of Meeting`, `:DecisionMeeting` (defined) | inferred `rdf:type` | `queries/cq4.rq` |
| CQ5 | What work does a mandate prescribe, and which objective does it serve? | `:Mandate`, `cco:Planned Act`, `cco:Objective` | `cco:prescribes` | `queries/cq5.rq` |

## Extendability questions (added 2026-11-11)

These ask about the documents themselves rather than about the meetings. They need one named graph per document, so they run on `results/extendability/program-a.trig`, not on the reasoned file. See `ontology/BUILD.md` §7.

| # | Question | How it is answered | Query |
|---|---|---|---|
| X01 | Which documents is each mandate known from? | the graphs that hold a fact about it | `queries/extendability/x01-provenance.rq` |
| X02 | What did document D add to things the base already knew? | triples in D whose subject appears in an earlier graph | `queries/extendability/x02-what-changed.rq` |
| X04 | Which mandates rest on one source, and which on several? | the number of documents that have the mandate as a part | `queries/extendability/x04-corroboration.rq` |
| V04 | Which words did each document add to the vocabulary? | labels first seen in that graph | `queries/extendability/v04-new-terms.rq` |

## What each question tests

**CQ1: recurrence.** This is the signal the pattern exists to catch. A version bump (M06 v1.0 → v1.1) is a new mandate, output by a later act of deciding that the earlier one `precedes`. The identifiers carry the human-readable ID. Expected answer on the synthetic data: M01, M05 and M06, and not M02.

**CQ2: the felicity condition.** A directive only succeeds if the person issuing it has the authority to (Smith, *Document Acts*, pp. 9–10). The query walks from the mandate to the act that output it, to its agent, and to the authority role that act realizes and the agent bears.

**CQ3: documents as carriers.** The minutes have the mandate as a continuant part, and the minutes file is the carrier. A follow-up letter that cites the same identifier is linked to the same mandate without pointing at the minutes (Smith's "knowledge by comparison", p. 10). This is asserted per individual, not as an axiom: not every set of minutes contains a mandate.

**CQ4: the v2 definition, checked by the reasoner.** No meeting is asserted to be a `:DecisionMeeting`. HermiT has to infer it from the equivalence axiom: an act of meeting that has as occurrent part an act of directive communication whose output is a mandate. The status briefing (`meeting_3`) must not be classified.

**CQ5: from mandate to purpose.** The mandate `prescribes` a planned act (the required work). The executive's objective also `prescribes` that act. CCO's `prescribes` ranges over any entity and both `Process Regulation` and `Objective` are prescriptive information content entities, so no new relation is needed. *Modeling choice, open to challenge:* the link to the objective runs through the shared planned act, not directly from mandate to objective.

## Left out on purpose

| Not modeled | Why |
|---|---|
| Meeting dates and temporal regions | No CQ asks "when". The synthetic timeline is kept in the test data as `rdfs:comment` only |
| Topics (`has participant` an ICE) | In the v2 pattern, but no CQ needs it |
| Online vs. in-person (`Act of Communication Mediated by Artifact`) | In the v2 definition of *meeting*, but CCO's `Act of Meeting` already covers it; no CQ distinguishes the two |
| Priority file (the dossier) | Belongs to the File Engineering layers above the programme; out of scope for v0.1 |
