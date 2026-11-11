# Sustained extendability: every document makes the base stronger

**Course material applied:** *Joint Doctrine Ontology* (week 07), *Ontology for the Intelligence Analyst* (week 01), *IAO-Intel* (week 03), *Document Acts* (week 03), *A Common Core-Based Cyber Ontology in Support of Cross-Domain Situational Awareness* (week 11), Sikos, *Cybersecurity Knowledge Graphs* (week 11), *Falsehoods Programmers Believe About Names* (week 13), and the definitions method from *Military Intelligence Part 1*.

**Implemented and tested:** `final-project/ontology/` ([`BUILD.md` §7](../../final-project/ontology/BUILD.md)). All the data is synthetic (Program A).

## The problem

The pattern models one meeting. An executive office, though, produces a meeting every week: a deck before it, minutes after it, letters following up. If each document is modelled on its own, the result is a pile of small graphs that don't know about each other. If the ontology is redesigned every time a new kind of document turns up, nothing stays stable long enough for an analyst to rely on it.

What I want is the opposite. **Every new presentation or set of minutes should make the base deeper or wider, and in doing so show how the organization itself talks about what it knows.**

## Step 1: the definition, tested the same way as *meeting*

I wrote the definition as a pair ⟨T, E⟩ and looked for counterexamples, as in the *meeting* definition on slide 5.

**First attempt.** *Sustained extendability* =def a property of a knowledge base built from an organization's documents, such that each new document can be added without changing earlier assertions.

| Test | Case | Result |
|---|---|---|
| Definition true, term false | A document store or search index. Every file is added and nothing earlier changes, but nothing is integrated with anything else. | **Fails.** Adding is not the same as extending. |
| Term true, definition false | A new document legitimately says M06 was re-issued. The base must change: something is now known that wasn't before. | **Fails.** "Without changing" is too strong. What must not happen is *overwriting*. |
| Negative language | "without changing" | The lecture's warning applies. The constraint is better stated as what is kept. |

**Version 2.** *Sustained extendability* =def a property of a knowledge base built from an organization's documents, such that each new document passes through one fixed loop that **links** what it contributes to what the base already holds, as depth, breadth or language, **while every earlier assertion and every earlier answer to the competency questions is kept.**

- "Links" rules out the document store. The demo measures it as *links into the base*.
- "Keeps every earlier answer" is a test that can be run: the regression check.
- "One fixed loop" is what makes it *sustained*. The tenth document goes through the same steps as the first.

## Three ways a document can add to the base

| Kind | What it adds | In the pattern | Program A (synthetic) |
|---|---|---|---|
| **Depth** | new facts about things the base already holds | new individuals of existing classes; new links to old nodes | D05 re-issues M01, M05 and M06. The new deciding acts are preceded by acts from D01 and D02, which are never edited. |
| **Breadth** | a new branch: a kind of thing not seen before | the first use of a class, or a new module under BFO/CCO, when a question needs it | D03, the first deck, brings in the objectives and links them to work the minutes already hold |
| **Language** | the organization's own words for things the base already holds | `skos:altLabel` on existing classes, or a parked `skos:Concept` | محضر and *MoM* for minutes; تكليف and *directive* for mandate; *KPI* parked |

The third kind is what makes this more than bookkeeping. Every document is evidence of **how the organization represents its knowledge**: which words it uses, which distinctions it draws (a mandate and a decision are not the same thing), and which things it treats as worth tracking. Over many documents, the label layer becomes a record of the organization's language, and the class layer shows which of those words carry a real distinction.

## The loop for each document

The same nine steps for every document:

| # | Step | Adds to | Check |
|---|---|---|---|
| 1 | **Register**: ID, type, date, version | metadata | the document has its own named graph IRI |
| 2 | **Harvest**: list the terms the questions need, with page and quote | candidate vocabulary | every term has a source |
| 3 | **Reconcile**: existing concept (add a label), new concept, or reject | vocabulary, thesaurus | no two accepted terms mean the same |
| 4 | **Classify**: place a new concept in a scheme. Does it need a class at all? | taxonomy | each broader link passes "every X is a Y" |
| 5 | **Model**: only if a question needs it, add a class under its BFO/CCO parent | ontology | the reasoner accepts it |
| 6 | **Assert**: write this document's facts | one named graph | the document's facts are in its own graph |
| 7 | **Compare**: what did it add, change or contradict? (X02) | change note | nothing earlier was overwritten |
| 8 | **Test**: run every competency question | test report | **every earlier answer still holds** |
| 9 | **Release**: accept, or reject and keep the base as it was | new version | the gate is passed by a person |

## Five rules that keep it extendable

1. **One named graph per document.** Nothing is merged in a way that loses its source. (Sikos: a knowledge graph as named graphs, one per data source.)
2. **A new class only when a competency question needs it.** Otherwise the term stays a SKOS concept. *KPI* in D03 is the worked case.
3. **Never overwrite; add a dated record.** M06 v1.0 stays when v1.1 arrives, because the fact that it had to be said twice is the signal (*Document Acts*, p. 10).
4. **Every new class goes under a BFO or CCO parent, defined by genus and differentia.** This is downward population, as in IAO-Intel.
5. **No IRI carries a project or file code.** A class minted for one file must still fit the next one.

## Where the course material comes in

| Reading | What it gives this argument |
|---|---|
| ***Joint Doctrine Ontology*** (section IX.C) | **The model for the whole idea.** JDO is built "incremental[ly]", one joint publication at a time, in three steps: **enrichment** (add the terms a publication uses but the glossary doesn't define), **logical regimentation** (rewrite definitions by the rules) and **formalization** (OWL). Here, each meeting document plays the part of a joint publication. Enrichment is loop steps 2–3, regimentation is step 4 plus the ⟨T, E⟩ test, and formalization is step 5. JDO also observes that doctrine was consistent because every publication used the same general terms. Minutes have the same property: every set uses *chair*, *mandate*, *minutes*. |
| ***Ontology for the Intelligence Analyst*** (Semantic Enhancement) | Each term keeps its place in the hierarchy "even when new terms or even whole new branches are added". That is breadth without disruption. It also asks for one preferred label and one definition per type, which is why language goes into `altLabel` and never into a second class. And its aim is a single *evolving* suite rather than ad hoc local ontologies. |
| ***IAO-Intel*** (section V) | Coverage "will be determined incrementally", from analysts' requests and the terms in doctrinal publications. That is rule 2 (a class when a question asks for it) and the harvest step. It also populates downward from IAO (rule 4), as on slide 14. |
| ***Document Acts*** | Documents extend memory, and identifiers create "virtual attachment" between documents. This is how depth arrives: D06 attaches to M06 v1.1 through its identifier, without ever pointing at D05. |
| ***C3O*** (section 2) | Domain modules extend CCO and so stay interoperable with other CCO-based modules. Breadth beyond the meeting (KPIs, initiatives) arrives as modules under CCO, never as a parallel hierarchy. |
| **Sikos, *Cybersecurity Knowledge Graphs*** | A knowledge graph written as named graphs, one per data source. This is rule 1, and what makes X01, X02 and X04 answerable. |
| ***Falsehoods Programmers Believe About Names*** | Names are not unique, stable or single. The same holds for an organization's terms: محضر, محضر اجتماع and *MoM* name one thing. Labels go in their own layer, and a new label never forces a new class. |

## What the test shows

`python ingest.py` loads Program A one document at a time. After each document it reasons with HermiT and re-runs CQ1–CQ5.

| Doc | Kind | Classes reused | First used | New labels | CQs answered | Regressions |
|---|---|---|---|---|---|---|
| D01 minutes, meeting 1 | base | 0/11 | 11 | 0 | 4/5 | — |
| D02 minutes, meeting 2 | depth | **8/8** | — | 1 | 4/5 | 0 |
| D03 deck, meeting 3 | breadth | 1/3 | Objective, meeting presentation | 6 (KPI parked) | 4/5 | 0 |
| D04 minutes, meeting 3 | depth (no decision) | 4/5 | Act of Communication | 2 | 4/5 | 0 |
| D05 minutes, meeting 4 | depth | **8/8** | — | 0 | **5/5** | 0 |
| D06 follow-up letter | language | 1/2 | official letter | 5 | 5/5 | 0 |
| D07 conflicting note | — | **rejected by HermiT** | | | | |

- **0 new OWL classes in six documents.** The pattern held. The one new term was parked in the vocabulary.
- **0 regressions.** After D06, the answers are identical to those of the one-shot v0.1 build.
- **CQ1 only becomes answerable at D05.** Recurrence can't be seen in any single document. It appears only when a later document is linked to earlier ones, which is the point of the whole exercise.
- **D07 is rejected.** It calls M06 v1.1 a planned act, confusing the mandate with the work. BFO's continuant/occurrent disjointness catches it, and the base stays at D06.
- **The named graphs answer new questions.** X01: M06 v1.1 is known from two documents. X04: 6 of the 7 mandates rest on one source. V04: which words each document added.

## Limits

- **Small, synthetic data.** Seven documents show the mechanism, not a trend. A real file is needed to see the rate of new terms per document fall.
- **Provenance stops at the document.** Real minutes need a page and a quote for each assertion.
- **The regression test is only as good as the questions.** An answer no CQ asks for is not protected.
- **Language is captured but not yet governed.** Who decides that تكليف and توجيه are one concept, not two, is a person's call (the release gate). It is not something the reasoner can decide.
