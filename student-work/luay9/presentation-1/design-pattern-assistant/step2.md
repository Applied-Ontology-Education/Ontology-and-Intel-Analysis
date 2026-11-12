# Exercise 3: Meeting · Step 2: Map to BFO, then CCO

Every term below was looked up in the index built from CCO v2.2 (2026-08-13), which includes BFO 2020. Your Pause 1 answers are applied. Items marked M1–M7 are new mapping decisions for you to challenge at Pause 2.

**Marks:** ✓ exact CCO match · ~ near match · \* proposed new term · **— stays at BFO** means CCO has nothing and the pattern doesn't need anything more specific

---

## 2.1 BFO

| Slot | Item | BFO class | Why |
|---|---|---|---|
| 1 | the stakeholders | `object aggregate` | separate persons that together form a unit |
| 1 | responsible person · accountable person · files | `object` | single physical things; a file is carried by a physical medium |
| 3 | triggering event · every act · the meeting · the cycle | `process` | |
| 4 | the accountable person's authority | `role` | exists because others accept the person's power to issue binding directives, not because of the person's physical makeup |
| 5 | the meeting room | `site` | an area of space, not made of matter, bounded by walls |
| 6 | the meeting's period | `temporal interval` | |
| 6 | cycle start · cycle end | `temporal instant` | |
| 7 | topic · material · presentation · assessment result · mandate · minutes · schedule | `generically dependent continuant` | copyable content: the same mandate is in the minutes, the follow-up email, and next month's slides |

## 2.2 CCO

### Slot 1: Material Entity

| Item | CCO class | Mark | Why |
|---|---|---|---|
| the stakeholders | `Group of Persons` | ✓ | "a Group of Agents that has only Persons as member parts" |
| responsible · accountable | `Person` | ✓ | |
| material file · deck file · minutes file | `Information Bearing Entity` | ✓ | "an Object upon which an Information Content Entity generically depends". The same class your mandate pattern uses |

### Slot 3: Process

| Item | CCO class | Mark | Why |
|---|---|---|---|
| the triggering event | — stays at BFO | | neither source says what it is |
| preparing material · creating the presentation | `Planned Act` | ✓ | the general class: "at least one Agent plays a causative role and which is prescribed by some Directive Information Content Entity". CCO has no authoring or creation acts |
| **the meeting** | `Act of Meeting` | ✓ | "an Act of Association wherein two or more Persons assemble for some common purpose". That's "human gathering… to address a topic" almost word for word |
| presenting | `Act of Representative Communication` | ✓ | "commits a speaker to the truth of the expressed content". A presenter vouches for their findings |
| assessing | `Act of Appraisal` | ✓ | "evaluating, assessing, estimating, or judging the nature, value, importance, condition, or quality of something" |
| making the decision | `Act of Directive Communication` | ✓ | "intended to cause the hearer to take a particular action". A mandate tells someone to act. This matches your mandate pattern |
| documenting the decisions | `Act of Official Documentation` | ✓ | "records some information for official use by another Agent" |
| the online variant | `Act of Communication Mediated by Artifact` | ✓ | "technology is used to create a new copy of the Information Content Entity in the recipient". Class level only (A5) |
| the decision cycle | — stays at BFO | | the whole, identified by its parts |

### Slot 4: Realizable Entity

| Item | CCO class | Mark | Why |
|---|---|---|---|
| the accountable person's authority | `Authority Role` | ✓ | "realized by Processes which create, modify, transfer, or eliminate Process Regulations". Issuing a mandate creates one, so this is exact |

### Slot 5: Where

| Item | CCO class | Mark | Why |
|---|---|---|---|
| the meeting room | — stays at BFO | | `site`. CCO has no room class; `Facility` is the whole building |

### Slot 6: When

| Item | CCO class | Mark | Why |
|---|---|---|---|
| the meeting's period | `Multi-Minute Temporal Interval` | ✓ | "measured in Minutes and spans at least one Minute". The right size for a meeting |
| cycle start · cycle end | — stays at BFO | | `temporal instant` |

### Slot 7: Information

| Item | CCO class | Mark | Why |
|---|---|---|---|
| the topic | `Information Content Entity` | ✓ | the general class: "stands in relation of aboutness to some Entity". An open question is neither a description nor a prescription |
| meeting material · the presentation | `Document Content Entity` | ✓ | "a series of paragraphs of text or diagrams that are intended to be carried by physical pieces of paper or an electronic document" |
| the assessment result | `Descriptive Information Content Entity` | ✓ | "describes some Entity": whether the material is sufficient |
| **the mandate** | `Process Regulation` | ✓ | "prescribes a Process as required, prohibited, or permitted, and is the output of a Process which realizes some Authority Role". The same as your mandate pattern |
| the minutes | `Report` | ✓ | "conveys an account of some event". The minutes are an account of the meeting |
| the schedule | `Prescriptive Information Content Entity` | ✓ | the general class; CCO has no schedule class |

**Tally:** 18 ✓ · 0 ~ · 0 \* · 4 stay at BFO. **No new terms.**

---

## 2.3 Relations

| Relation | From | Domain → Range | Used for | Why this one, not the similar one |
|---|---|---|---|---|
| `has member part` | BFO | material entity → material entity | stakeholders → the two persons | the stakeholders are an object aggregate |
| `has agent` | CCO | process → `Agent` | every act; the stakeholders as the agent of the meeting | lint check 11 |
| `has recipient` | CCO | `Act of Communication` → `Agent` | presenting → accountable; deciding → responsible | the mandate's recipient is the person who must act on it |
| `has participant` | BFO | process → | meeting → topic ("addresses"); presenting → deck; assessing → material | BFO 2020 lets content take part in processes |
| `has occurrent part` | BFO | occurrent → occurrent | cycle → steps; meeting → presenting, assessing, deciding | |
| `precedes` | BFO | occurrent → occurrent | BPMN order, including meeting → meeting in the loop | **not** `cco:is predecessor of`, which applies only to independent continuants (see the note on your mandate pattern) |
| `has output` | CCO | process → | preparing, creating, documenting → **the files**; assessing → result; deciding → mandate | output the carrier where there is one (lint check 12). The last two have no carrier named |
| `is carrier of` | BFO | → GDC | files → material, deck, minutes | |
| `is about` | CCO | ICE → entity | material, deck → topic; topic → triggering event; minutes → the meeting | |
| `describes` | CCO | Descriptive ICE → entity | assessment result → material | |
| `continuant part of` | BFO | continuant → continuant | mandate → minutes | as in your mandate pattern: the mandate is *part of* the minutes, not the same thing as them |
| `bearer of` · `realizes` | BFO | | accountable → authority; deciding → authority | |
| `requires` | CCO | Process Regulation → process | mandate → the acts it requires (class level) | |
| `prescribes` | CCO | Prescriptive ICE → entity | schedule → the meeting's period | |
| `occupies temporal region` | BFO | process → temporal region | meeting → its period | **not** `occurs at`, whose range is `site` (see the note on your mandate pattern) |
| `occurs at` | CCO | process → site | meeting → the room | the room is a site, so this one is correct |
| `process has first instant` / `process has last instant` | CCO | process → temporal instant | cycle → start / end; triggering event → start | |
