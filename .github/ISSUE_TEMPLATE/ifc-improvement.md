---
name: IFC Improvement
about: Suggest an improvement to IFC
title: ''
labels: enhancement
assignees: ''

---

This repository has a clearly defined objective. Please read this wiki page first, before starting a new issue: https://github.com/buildingSMART/NextGen-IFC/wiki/Towards-a-technology-independent-IFC

Make sure your issue is fixing one of these issues:
* The geometry kernel is too big to fully implement. There are many specific entities that increase the efficiency of storage, but only have a few use-cases.
* The structure has many dependencies in it. The final representation of entities is depending on the attributes of others (for example positioning of objects). The whole file needs to be analysed, with multiple dependencies, before the result of a single object can be derived.
* The use of advanced data modelling structures like ‘linked lists’, and ‘selects’ have little or no comparable equivalents in broadly used languages like UML and linked data standard RDF. Trying to mimic the IFC data types in languages like XML and JSON creates bespoke solutions that cannot be used with out of the box libraries.
* The many advanced data modelling structures that are available provide a wide range of options for software vendors to build implementations. This creates different implementations in software that are not interoperable. The schema needs to be stricter and eliminate ambiguity.
* Many of the advanced structures in IFC have been proven to be too complex for software vendors to implement. The time that vendors need to implement IFC is too long, and for vendors that have lower commercial interest in supporting IFC the threshold becomes too high. 

Issues that are not focussed on fixing these points will be removed from this repository.
