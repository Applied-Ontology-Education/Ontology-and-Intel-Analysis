# Luay Assidmi (luay9): graduate track

**Pattern:** Meeting & Mandate. An ontology design pattern for executive meetings, the directives (mandates) they produce, and the documents that carry them. It's built so that a directive the chair has had to issue twice becomes a signal derivable from the graph.

**Why it's intelligence analysis:** an executive who sets priorities, collection fragmented across many committee files, and no analytic layer between them is a strategic intelligence problem. The pattern is the structure for that analytic layer.

## Contents

| Folder | What's in it | Status |
|---|---|---|
| [`presentation-1/`](presentation-1/) | Proposal deck (v2, revised with course material), design pattern, BPMN, Design Pattern Assistant workings | Presentation 1 recorded 2026-09-29; revision 2026-10-17 |
| [`presentation-1/course-reflection/`](presentation-1/course-reflection/) | How course readings changed the proposal: definition tests, Document Acts, IAO alignment | Done |
| [`final-project/`](final-project/) | Ontology (`.ttl`) and the 7-part final project packet | Ontology v0.1 built and tested 2026-10-17; packet documents next |

## Plan

| When | What | Where it's submitted |
|---|---|---|
| 2026-10-17 (Week 8) | Proposal revised with course material; v2 deck + speaker notes | this folder |
| Week 9 (Oct 19–25) | `.ttl` v0.1: pattern classes, synthetic data, reasoner + CQ queries (done early, 2026-10-17) | this folder |
| Week 10 (Oct 26–Nov 1) | **Presentation 2**: v2 deck + implementation and testing slides | recording link in GitHub Discussions |
| Weeks 11–14 | Final project packet (7 parts), revisions from feedback | this folder |
| Week 15 (Nov 30–Dec 6) | **Final Project** submitted | pull request |

## Method

1. My own definition in words, with no BFO/CCO lens
2. BPMN process map
3. Sort entities into the seven rules-of-thumb slots
4. Look up BFO/CCO terms for each item
5. Design pattern workshop in Mermaid

Steps 3–5 are co-authored with a Design Pattern Assistant: an AI agent that looks up every term in an index built from CCO v2.2 and lints each pattern for term existence and domain/range. Its workings are in `presentation-1/design-pattern-assistant/`.

## Data

All instance data here is **synthetic**. The pattern was developed against real internal files, which are not published, in line with the course's sensitive-information policy.
