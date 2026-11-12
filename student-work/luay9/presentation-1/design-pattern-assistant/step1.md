# Exercise 3: Meeting · Step 1: Identify

**Inputs:** your definition (narrative) + `Meeting.bpmn` (takes precedence where they disagree)
**Mode:** run straight through with no pauses, as you asked. Where I'd normally ask a question, I've recorded an **assumption (A1–A7)** instead. Override any of them and the pattern updates.
**Scope:** no competency question, so the scope is the BPMN plus the narrative
**Level:** both. A class-level spec for "a type of human gathering…", plus one typed example run of the BPMN
**Parser output:** `skeleton.md` / `skeleton.tsv`, passes lint
**Related:** your Final Presentation mandate pattern (`01-cdp-mandate-pattern.md`), which models the "make decisions (mandates)" half

Source key: **B:** BPMN element · **N:** narrative phrase · **implied**

---

## Slot 1: Material Entity

| Item | Source | Note |
|---|---|---|
| the stakeholders (the attendees) | B: lane *Stakeholder* · N: "human gathering" | a group of persons |
| the responsible person | B: nested lane *Responsible* | prepares and presents |
| the accountable person | B: nested lane *Accountable* | assesses, decides, documents |
| files: material, deck, minutes | implied by B: *Create Presentation*, *Document Decisions* (business-rule tasks) | what the Slot 7 content is carried in |
| ~~Topic~~ | B: lane *Topic* | not something physical; it's **information**, so it moves to Slot 7 (A3) |

## Slot 2: Quality

| Item | Source | Note |
|---|---|---|
| **none** | | Nothing in either source is measured or turns on a property. "A determined period" is **time** (Slot 6), not a quality |

## Slot 3: Process

| Item | Source | Note |
|---|---|---|
| the triggering event | B: start event *Event* (signal) | something happens that raises an issue. Left unspecified |
| preparing meeting material | B: *Prepare Meeting Material* | the responsible person |
| creating the presentation | B: *Create Presentation* | the responsible person |
| **the meeting** | N: "human gathering" · B: pool *Meeting* | presenting, assessing and deciding happen inside it (A1) |
| presenting | B: *Present* | responsible → accountable |
| assessing | B: *Assess* | the accountable person. Outcome: *need more information*, or enough |
| making the decision | B: *Make Decision* · N: "make decisions (mandates)" | the accountable person issues the mandate |
| documenting the decisions | B: *Document Decisions* | produces the minutes |
| the decision cycle | B: pool | the whole. It may contain **several meetings** (A2) |
| ~~Needs Decision~~ | B: task in the *Topic* lane | named as a state, and nobody performs it. It becomes the topic (Slot 7) (A3) |

## Slot 4: Realizable Entity

| Item | Source | Note |
|---|---|---|
| the accountable person's authority | B: lane *Accountable* · N: "make decisions (mandates)" | the authority to issue binding mandates (A4) |
| ~~Responsible / Stakeholder roles~~ | B: lanes | not modelled as roles: what each person does already tells them apart (A4) |

## Slot 5: Where

| Item | Source | Note |
|---|---|---|
| the meeting room | N: "in person" | a place, bounded by walls (A5) |
| (no shared place) | N: "online" | the communication is carried by technology instead (A5) |

## Slot 6: When

| Item | Source | Note |
|---|---|---|
| the meeting's period | N: "a determined period of time" | fixed in advance (A6) |
| cycle start, cycle end | B: *Event*, *End* | instants |

## Slot 7: Information

| Item | Source | Note |
|---|---|---|
| **the topic** | B: lane *Topic*, task *Needs Decision* · N: "address a topic(s)" | the open question the meeting addresses (A3) |
| meeting material | B: *Prepare Meeting Material* | prepared beforehand |
| the presentation | B: *Create Presentation* | the slides |
| the assessment result | B: gateway branch *Need more Information* | enough information, or not |
| **the decision = the mandate** | B: *Make Decision* · N: "(mandates)" | requires others to act (A7) |
| the minutes | B: *Document Decisions* | the record of the meeting. The mandate is part of it |
| the schedule | N: "a determined period of time" | what fixes the period in advance (A6) |

---

## Where the narrative and the BPMN disagree

| # | Narrative | BPMN | Resolution |
|---|---|---|---|
| X1 | "a type of human gathering… for a determined period" | the pool also covers preparation *before* and documentation *after* | **Both.** The meeting is the gathering (present → assess → decide). The pool is the wider decision cycle around it (A1) |
| X2 | "make decisions" | a loop: *Need more Information* → prepare again | **BPMN.** One decision may take several meetings (A2) |
| X3 | "online / in person" | nothing | **Keep, narrative only** (A5) |
| X4 | "for a determined period of time" | no timer | **Keep, narrative only** (A6) |
| X5 | "address a topic(s)" | *Topic* is drawn as a lane, as if it were a participant | **Narrative.** A topic is information, not something that takes part (A3) |

## Assumptions (in place of questions; override any)

- **A1.** The meeting is CCO's `Act of Meeting`, and it contains presenting, assessing and deciding. Preparing happens before it and documenting after, both inside the wider decision cycle.
- **A2.** The *Need more Information* loop means the meeting ends without a decision, the material is prepared again, and a follow-up meeting happens. Panel B's main run shows one meeting that decides; a separate view shows the loop across two meetings.
- **A3.** *Topic* is information (the open question), not a participant. *Needs Decision* is the topic's state rather than an activity, since nobody performs it. It becomes the topic itself, which is *about* the triggering event.
- **A4.** *Accountable* is the person with authority to issue mandates. *Responsible* and *Stakeholder* aren't modelled as roles, because what each person does already identifies them. (Your mandate pattern's `*Mandate Obligation Role` would go here if the pattern followed the mandate into being carried out. It doesn't.)
- **A5.** In person, the meeting happens in a room. Online, there's no shared place, and technology carries the communication. Panel B shows the in-person case; Panel A allows either.
- **A6.** "A determined period" means the meeting takes up a period that a schedule fixed in advance.
- **A7.** The decision is a mandate, issued by an act that uses the accountable person's authority. This is the same spine as your Final Presentation pattern.

### Decided without asking

- The start event *Event* marks the end of the triggering occurrence, which lies outside the cycle (the same pattern as the arrival in Exercise 1 and the request in Exercise 2).
- *Prepare Meeting Material* has two incoming arrows (the first pass and the loop). The parser flags this, but here it's correct: they're alternatives, not parallel arrivals, so the task should run once per arrival.
- The unlabelled branch out of the assessment gateway means "enough information".
