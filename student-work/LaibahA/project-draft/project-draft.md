# Undergraduate Final Project Draft

## 1. Project Title and Intelligence-Analysis Topic

Connecting Geospatial Information Across Intelligence Reports Using Ontology

## 2. Project Objective

Intelligence analysts examine intelligence reports that include geospatial information to identify patterns and relationships between events and locations. Geospatial information is not only about one event at one place, it can be about actors, like people or organizations, present at a location, and represent development across locations over time. Connecting this kind of information can help analysts identify relationships between events or actors and location(s) they may be at across time and dates, revealing how reports relate to one another.

However, there's a few different issues an analyst may face trying to connect geospatial information across intelligence reports. For example, different reports might use inconsistent vocabulary when describing the same geographic location, which would make it difficult to recognize that it's referring to the same place. This gets more complicated as reports may describe the same actors or events at specific locations, but the locations are referenced differently, making it even harder to build connections across individual reports. Furthermore, considering date and time just add additional layers of detail that must be represented to connect reports meaningfully.

In order to address these challenges, my ontology will represent intelligence reports, events and actors, and geospatial relationships and information that the reports describe. The ontology is intended to support analysts performing intelligence analysis on reports by identifying reports describing events in the same geographic area, recognizing different references to the same location, identifying actors associated with locations, and representing relationships between events and actors with locations over time or as locations change.

## 3. Scope Statement

Some main classes that will be modelled are intelligence reports, events, people, organizations, locations, and time. People and organizations are types of actors, and locations and time are used to describe where and when events or actors are associated with information in the reports.

Some main relationships that will be represented are reports describing events and/or actors associated with locations at specific dates and times, different terms or descriptions referring to the same location, and geographic relationships between locations. The ontology should be able to model relationships like a location being inside another location, like a city in a country, but not necessarily a distance between every possible location on the globe. Locations can include cities, states, countries, other general regions, but not specific addresses or buildings because that would extend beyond the scope of the project.

Some potential boundaries that describe what is out of scope for my ontology are, determining if reports are factually accurate, drawing conclusions about events or actors activities, and tracking events and actors associations with locations in real time. Route calculation and detailed geographic features or information about locations will also be out of scope since the focus will be on representing locations referenced in reports and relevant relationships between them or with events and actors.

## 4. Competency Questions or Intended Uses

A preliminary set of intelligence-analysis competency questions that the ontology is intended to answer are:

1. Which intelligence reports describe events occurring at the same geographic location?
2. Which intelligence reports reference the same location using different names or descriptions?
3. What locations are referenced by different names or descriptions?
4. Which events described in the reports occurred in the same region?
5. Which events occurred within a certain geographic location?
6. Which people or organizations are associated with a particular location in intelligence reports?
7. What locations are certain people or organizations associated with across intelligence reports?
8. What date and times do reports describe events occurring or actors being associated with certain locations?

The ontology should represent information and relationships to connect information across individual intelligence reports, rather than verify accuracy of reports or determine or predict future event or actor association with locations.

## 5. Preliminary Ontology Artifacts

### Class Hierarchy

- Thing
  - Intelligence Report
  - Event
  - Actor
    - Person
    - Organization
  - Location
    - Country
    - State
    - County
    - City
  - Time
  - Date
  - Reported Association

Reported Association: I want this class to represent a collection of information to connect actors/events with locations, dates/times, and the intelligence reports that describe them. Multiple Reported Association individuals can reference the same intelligence report to represent different pieces of information described in that report.

### Relationships

- `describesEvent`: Intelligence Report → Event
- `referencesActor`: Intelligence Report → Actor
- `occursAt`: Event → Location, to represent a specific location the event is described to occur in
- `occursIn`: Event → Location, to represent the broader area that an event occurs in, can usually be inferred
- `associatedWithLocation`: Actor → Location
- `isWithin`: Location → Location
- `hasAlternateName`: Location → Location
- `occursAtTime`: Event → Time
- `presentAtTime`: Actor → Time
- `occursOnDate`: Event → Date
- `presentAtDate`: Actor → Date
- `involvedWith`: Actor → Event
- `hasEvent`: Reported Association → Event
- `hasActor`: Reported Association → Actor
- `hasLocation`: Reported Association → Location
- `hasDate`: Reported Association → Date
- `hasTime`: Reported Association → Time
- `reportedIn`: Reported Association → Intelligence Report

### Definitions

| Class | Definition |
|---|---|
| Intelligence Report | A report that contains information about events, actors, locations, or other details relevant to intelligence analysis. |
| Event | Something that happens, like a meeting, situation, or other occurrence. |
| Actor | A person or organization involved in an event or associated with a location. |
| Person | An individual human being. |
| Organization | A group of people organized for a particular purpose. |
| Location | A geographic area where an event occurs or an actor is associated with. |
| Country | A location recognized as a country. |
| State | A location recognized as a state. |
| County | A location recognized as a county. |
| City | A location recognized as a city. |
| Time | A specific clock time. |
| Date | A specific calendar day. |
| Reported Association | A collection of information connecting an actor or event with a location and date or time, based on what is described in an intelligence report. |

## 6. Sources and Reused Resources

- For location data and alternate names of locations I will use data from GeoNames.
- For report data I will write synthetic intelligence reports that mention events, actors, locations, and other information. I may use real world reports as reference, from CIA Electronic Reading Room, CREST collection ([cia.gov/readingroom](https://www.cia.gov/readingroom)).
- For event types I can reference [CAMEO event codes](https://gdeltproject.org/data/lookups/CAMEO.eventcodes.txt) to find examples to put in my synthetic intelligence reports.
- I am not reusing or adapting existing ontologies. The class hierarchy, relations, and definitions are original. I might refer to ontologies definitions as I continue the project through.
- Course readings and lectures informed my general understanding of how to use ontologies in intelligence analysis, and what to think about as I model a topic. For example, the Week 3 reading "Ontology of Information Artifacts in the Intelligence Domain" (IAO-Intel, Smith et al.) informed my decision to separate intelligence reports from the events, actors, and locations they describe, since the reports aren't necessarily factual conclusions, they just provide information that can be used by analysts. Therefore, the ontology can represent what a report says about an event, actor, or location without claiming it is true, and the same event, actor, or location can be connected across multiple reports.
