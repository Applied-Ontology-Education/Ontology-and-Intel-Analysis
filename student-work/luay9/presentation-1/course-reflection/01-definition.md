# Step 1 revisited: testing my own definition

**Course material applied:** *Intelligence Analysis: Military Intelligence Part 1*, "Definitions Revisited" (slides 4–32).

## v1: the definition as proposed

> **Meeting** =def a type of human gathering (online/in person) for a determined period of time to address a topic(s) and make decisions (mandates).

## The tests

A definition is a pair ⟨T, E⟩. T should be true of exactly what E is true of (slide 4). Each half gets tested by looking for a counterexample (slide 5).

| Test | Counterexample | Result |
|---|---|---|
| **T true, E false**: a meeting the definition misses | A weekly status briefing where people only report progress and nothing is decided | **Fails.** "Make decisions" is not true of every meeting |
| | Two directors meet in a corridor and settle an issue in five minutes, with nothing scheduled | **Fails.** "A determined period of time" is not true of every meeting |
| **E true, T false**: the definition fits, but it isn't a meeting | A family at dinner deciding where to go on holiday | **Fails.** A human gathering for a period, on a topic, that decides. Nobody calls this a meeting, because nothing in E requires the gathering to be planned or to serve a common purpose |
| **Negative language** (slides 12–27) | — | **Passes.** v1 has no "not" clauses. v2 keeps it that way: it defines a *decision meeting* as a subtype of meeting, and does not define a "non-decision meeting" (that would be a false bifurcation, slides 21–24) |
| **Useful vs. true of the world** (slides 8–11) | — | v1 is useful for my corpus but describes the meetings I *want*, not all meetings. That's a world-to-word fit (slide 30) |
| **Word-to-world** (slides 30–32) | "make decisions (mandates)" | **Conflates an act with its output.** Deciding is an act; the mandate is the information it produces (see `02-document-acts.md`) |

## v2: revised definitions

> **Meeting** =def an act of association in which two or more persons, sharing a place or connected through a communication artifact, communicate about one or more topics for a common purpose.

> **Decision meeting** =def a meeting that has as part at least one act of directive communication, performed by a person who bears an authority role, whose output is a mandate.

> **Mandate** =def a process regulation that is the output of an act of directive communication performed in a meeting.

### What changed, and why

| v1 | v2 | Why |
|---|---|---|
| "human gathering" | "act of association … for a common purpose" | Rules out the family dinner. Matches CCO `Act of Meeting` (cco:ont00000144): *"An Act of Association wherein two or more Persons assemble for some common purpose."* |
| "(online/in person)" | "sharing a place or connected through a communication artifact" | Says what makes an online meeting a meeting: `Act of Communication Mediated by Artifact` (cco:ont00002076) |
| "for a determined period of time" | removed | Every meeting occupies some period. Whether a schedule fixed it in advance is a fact about *some* meetings, not part of what a meeting is |
| "make decisions (mandates)" | moved to the subtype **decision meeting** | Not every meeting decides. The subtype splits the class from the inside ("a meeting that…"), so no negative definition is needed |
| decision = mandate | the act of deciding **outputs** the mandate | Act and output are different kinds of thing (process vs. information content entity) |

### Re-running the tests on v2

| Case | Meeting? | Decision meeting? |
|---|---|---|
| Status briefing, nothing decided | ✓ | ✗ (correct) |
| Unscheduled corridor huddle that settles an issue | ✓ | ✓ |
| Family dinner deciding a holiday | ✗: the family isn't uniting "in a Planned Act, enterprise or business" (CCO `Act of Association`, cco:ont00000433) | — |
| Board meeting where the chair issues a directive | ✓ | ✓ |

**One remaining weakness:** "common purpose" carries a lot of weight, and the family-dinner case depends on reading it strictly. This is CCO's wording, so I'm keeping it and flagging it as a known limitation.
