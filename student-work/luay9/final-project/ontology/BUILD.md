# Building and testing the ontology (v0.1)

This folder holds the Meeting & Mandate ontology, the synthetic data I test it with, and the results of every test. One script rebuilds all of it from the CCO release:

```bash
bash build.sh /path/to/CommonCoreOntologiesMerged.ttl
```

**Tested with:** ROBOT 1.9.10 (HermiT is bundled), Java 25, and CCO v2.2 (merged file, 2026-08-13). The script expects ROBOT at `~/tools/robot.jar`; set `ROBOT_JAR` to use another path. A clean rebuild on 2026-10-17 reproduced the module and the reasoned ontology byte for byte.

## Files

| File | What it is | Written or generated |
|---|---|---|
| `cco-terms.txt` | The 15 CCO classes and 14 BFO/CCO relations the pattern uses | written |
| `cco-module.ttl` | The slice of BFO + CCO those terms need: 94 classes, 30 object properties | generated (step 1) |
| `meeting-mandate.ttl` | **The ontology**: 6 new classes, their axioms, SKOS alignment to IAO | written |
| `test-individuals.ttl` | Synthetic Program A: 4 meetings, 7 mandates, minutes, a follow-up letter | written |
| `meeting-mandate-full.ttl` | The three files above, merged, with HermiT's inferences added | generated (step 2) |
| `tests/` | Two probe files used only by the failure tests | written |
| `queries/cq1–cq5.rq` | One SPARQL query per competency question | written |
| `queries/checks/` | Queries that check the reasoner's output | written |
| `queries/qc/`, `report-profile.txt` | Quality-report rules | written |
| `results/` | Every output the tests produce | generated (steps 3–7) |
| `documents/` | Program A again, as 7 separate documents (D01–D07) for the extendability test, with `manifest.tsv` | written |
| `ingest.py` | Ingests the documents one at a time: reason, CQs, regression, counts, named graphs | written |
| `queries/extendability/` | X01, X02, X04, V04: questions that need one named graph per document | written |

The competency questions themselves are in [`../03-competency-questions.md`](../03-competency-questions.md).

## The steps

### 1. Extract the module

```bash
robot extract --input $CCO --method BOT --term-file cco-terms.txt --individuals exclude --output cco-module.ttl
```

I don't import all of CCO. BOT extraction takes each term in `cco-terms.txt`, every class above it up to BFO, and every axiom needed to keep their entailments. That includes BFO's disjointness of independent, specifically dependent and generically dependent continuants, which test 4a depends on. To add a term, add its IRI to `cco-terms.txt` and re-run; `cco-module.ttl` is never edited by hand.

### 2. Merge and reason

```bash
robot merge --input cco-module.ttl --input meeting-mandate.ttl --input test-individuals.ttl \
  reason --reasoner hermit --axiom-generators "SubClass ClassAssertion" --include-indirect true \
  --output meeting-mandate-full.ttl
```

HermiT checks consistency, then writes every inferred class membership into the output. **No meeting in the test data is typed as a decision meeting.** Any `:DecisionMeeting` in `meeting-mandate-full.ttl` was put there by the reasoner.

One thing that matters: each `.ttl` file declares every relation it uses as `owl:ObjectProperty`. ROBOT parses each input file separately, so a relation that a file uses without declaring is read as an annotation, and the reasoner never sees it.

### 3. Check the reasoner's results

| Check | Query | Expected | Result |
|---|---|---|---|
| Which meetings are decision meetings? | `checks/decision-meetings.rq` | 1, 2, 4 yes; 3 (status briefing) no | ✓ `results/step7-decision-meetings.csv` |
| Are mandates placed in CCO and BFO? | `checks/mandate-types.rq` | each one a Process Regulation and a generically dependent continuant | ✓ all 7, `results/step7-mandate-types.csv` |
| Where do the new classes sit? | `checks/class-hierarchy.rq` | under the CCO parents in `meeting-mandate.ttl` | ✓ `results/step7-class-hierarchy.csv` |
| How many decision meetings before and after reasoning? | `checks/cq4-control.rq` | 0 before, 3 after | ✓ `results/cq4-control-asserted.csv`, `cq4-control-reasoned.csv` |

The last row is the cleanest single piece of evidence: the data contains no decision meetings, and the reasoned ontology contains three.

### 4. Failure tests

A test that can't fail proves nothing, so two probes try to break the ontology. They live in `tests/` and are only merged in for these tests.

| Probe | What it adds | Expected | Result |
|---|---|---|---|
| `tests/bad-mandate-person.ttl` | `bad_1`, typed both Mandate and Person | inconsistent | ✓ HermiT: "The ontology is inconsistent" (`results/step8-inconsistency.txt`) |
| `tests/no-authority-probe.ttl` | a directive issued by a person who bears no authority role | its meeting is **not** a decision meeting | ✓ `meeting_x` false (`results/probe-no-authority.csv`) |

ROBOT's explanation of the inconsistency is in `results/step8-explanation.md`. A Person is a material entity, so an independent continuant. A Mandate is a Process Regulation, so an information content entity, so a generically dependent continuant. BFO makes the two disjoint.

### 5. Answer the competency questions

```bash
robot query --input meeting-mandate-full.ttl --query queries/cq1.rq results/cq1.csv   # and so on to cq5
```

The queries run against the **reasoned** file. CQ4 depends on it: on the unreasoned data it returns nothing.

| CQ | Expected | Result |
|---|---|---|
| CQ1: which mandates were issued more than once? | M01, M05, M06; not M02 | ✓ each v1.0 → v1.1 |
| CQ2: who issued each mandate, in virtue of what role? | chair 1, authority role | ✓ all 7 |
| CQ3: which documents carry a mandate? | minutes; M06 v1.1 also in the letter | ✓ 8 rows |
| CQ4: which meetings are decision meetings? | 1, 2, 4 | ✓ with 2, 2 and 3 mandates |
| CQ5: what work does a mandate prescribe, toward which objective? | a planned act and an objective for each | ✓ all 7 |

### 6. Quality report

```bash
robot report --input meeting-mandate.ttl --profile report-profile.txt --fail-on none --output results/report.tsv
```

The report runs on my file only. CCO's own metadata isn't mine to fix.

ROBOT's default `missing_definition` rule looks for `IAO:0000115`, the OBO definition property. CCO and this ontology use `skos:definition`, so the default rule flags every class even though each has a definition. `report-profile.txt` is ROBOT's default profile with that one rule replaced by two of my own:
- `qc/missing_skos_definition.rq`: every class has an English `skos:definition`
- `qc/missing_arabic_preflabel.rq`: every class has an Arabic `skos:prefLabel`

I checked that both rules fire on a copy with one definition and one Arabic label removed.

**Result: 0 errors, 0 warnings, 1 info.** The info is `missing_superclass` on DecisionMeeting. That's expected: it's a defined class with an equivalence and no asserted parent, and HermiT places it under Act of Meeting.

### 7. Sustained extendability: one document at a time

```bash
python ingest.py
```

The one-shot build above loads all of Program A at once. This step loads it the way it would arrive: one document at a time, in meeting order. Each document is a file in [`documents/`](documents/) and becomes one named graph. The idea and the course readings behind it are in [`../../presentation-1/course-reflection/04-sustained-extendability.md`](../../presentation-1/course-reflection/04-sustained-extendability.md).

For each document, `ingest.py`:

1. merges the base (`cco-module.ttl` + `meeting-mandate.ttl`), every document accepted so far, and the new one, and reasons with HermiT. **If the result is inconsistent, the document is rejected and the base stays as it was.**
2. answers CQ1–CQ5 on that snapshot
3. checks that **every earlier answer still holds**. A row with an empty cell (CQ5's objective before the deck arrives) counts as still holding when a new row agrees on every filled cell. Unknown becoming known is depth, not breakage.
4. counts what the document added: new individuals, facts on nodes the base already had, links into the base, classes used for the first time, new OWL classes (must be 0) and new labels.

| Doc | Kind | Classes reused | Classes first used | New labels | CQs answered | Regressions |
|---|---|---|---|---|---|---|
| D01 minutes, meeting 1 | base | 0/11 | 11 | 0 | 4/5 | — |
| D02 minutes, meeting 2 | depth | 8/8 | — | 1 | 4/5 | 0 |
| D03 deck, meeting 3 | breadth | 1/3 | Objective, meeting presentation | 6 (KPI parked) | 4/5 | 0 |
| D04 minutes, meeting 3 | depth (negative case) | 4/5 | Act of Communication | 2 | 4/5 | 0 |
| D05 minutes, meeting 4 | depth | 8/8 | — | 0 | **5/5** (CQ1 now answerable) | 0 |
| D06 follow-up letter | language | 1/2 | official letter | 5 | 5/5 | 0 |
| D07 conflicting status note | — | **rejected**: inconsistent | | | | |

Full log: [`results/extendability/ingest-log.md`](results/extendability/ingest-log.md).

**Three results.**

- **No document minted an OWL class.** The six documents added 56 individuals and 14 labels. The only new term, *KPI*, was parked as a SKOS concept (`:concept_kpi`), because no competency question needs it yet.
- **Nothing broke.** 0 regressions across 6 ingestions. **After D06, CQ1–CQ5 return exactly the answers of the one-shot build in `results/`.** Loading the documents one by one ends in the same place as loading them all at once.
- **The conflict was caught.** D07 types M06 v1.1 as a Planned Act, which confuses the mandate with the work it requires. HermiT finds it inconsistent: the minutes have M06 v1.1 as a continuant part, `has continuant part` has range continuant, and BFO makes continuant and occurrent disjoint. Explanation: [`results/extendability/after-D07/explanation.md`](results/extendability/after-D07/explanation.md).

**Questions only the named graphs can answer.** These run on [`results/extendability/program-a.trig`](results/extendability/program-a.trig): one graph per accepted document, plus a `graph/base` holding the pattern and the CCO module.

| Question | Query | Result |
|---|---|---|
| X01: which documents is each mandate known from? | `queries/extendability/x01-provenance.rq` | M06 v1.1 from D05 and D06; every other mandate from one set of minutes |
| X02: what did document D add to things already known? | `x02-what-changed.rq` (D05) | 6 facts: the three `precedes` links back to D01/D02, and three `prescribes` links from D03's objectives |
| X04: which mandates rest on one source? | `x04-corroboration.rq` | 6 of 7; only M06 v1.1 is corroborated |
| V04: which words did each document add? | `v04-new-terms.rq` | 14 labels across D02, D03, D04, D06 |

**Limits.** The documents are synthetic and small, so the counts show the mechanism rather than a trend. Provenance stops at the document: real minutes would also carry a page and a quote for each assertion. The regression check is only as strong as the five CQs.

## Where v0.1 goes beyond the v2 pattern documents

- **DecisionMeeting** requires the directive to be issued by a person who bears an authority role. The written v2 definition says this. The axiom encodes it, and the no-authority probe tests it.
- **Mandate** must be the output of a directive act that is part of a meeting ("performed in a meeting", in the v2 definition).
- **Labels:** `rdfs:label` is English only; English and Arabic are both in `skos:prefLabel`. Two `rdfs:label`s per class gives 12 `multiple_labels` errors in the ROBOT report.
- **has member part** (BFO_0000115) was added to `cco-terms.txt`, because the v2 triples use it for the group of attendees.
- **Test data:** the synthetic timeline's eight meeting dates are condensed into four meetings. The dates are kept as comments.
