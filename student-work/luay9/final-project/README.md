# Final Project: Meeting & Mandate ontology (in progress)

**Ontology v0.1 is built and tested** (2026-10-17). How it was built, how to rebuild it, and every test result: [`ontology/BUILD.md`](ontology/BUILD.md).

This folder holds the packet required by [`assignments/final-project.md`](../../../assignments/final-project.md):

| # | Item | File | Status |
|---|---|---|---|
| 1 | Ontology artifact | [`ontology/meeting-mandate.ttl`](ontology/meeting-mandate.ttl) (uses an extracted BFO + CCO module; IAO aligned with SKOS mappings) | v0.1 |
| 2 | Problem statement | `01-problem.md` | to write |
| 3 | Scope statement | `02-scope.md` | to write |
| 4 | Competency questions | [`03-competency-questions.md`](03-competency-questions.md) + SPARQL in [`ontology/queries/`](ontology/queries/) | done |
| 5 | Modeling documentation | `04-modeling.md` | to write |
| 6 | Sources and reused content | `05-sources.md` | to write |
| 7 | Analytic value and limitations | `06-value-and-limitations.md` | to write |
| — | Validation | HermiT via ROBOT, two failure tests, CQ results, ROBOT report: [`ontology/BUILD.md`](ontology/BUILD.md) and [`ontology/results/`](ontology/results/) | done for v0.1 |
| — | Sustained extendability | The same data ingested one document at a time: 6 accepted, 1 rejected by HermiT, 0 regressions, same final answers as the one-shot build: [`ontology/BUILD.md` §7](ontology/BUILD.md) | done 2026-11-11 |
