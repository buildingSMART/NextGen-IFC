# IFC_UML

Schema management and versioning repository for IFC. It is manages by the buildingSMART International Model Support Group under the technical services group.

This repository is to setup the UML/XMI structure to maintain IFC. As new commits to the XMI come in, the Continuous Integration pipeline will be triggered and create two artifacts (a) an EXPRESS serialization of the XMI schema (b) a collection of UML diagrams generated from the defined entities (ignoring explicit diagrams serialized in the XMI).

Note that this is currently still work in progress.

## Diagram aims

For the diagrams the following aims were taking into consideration (in decreasing order of priority).

- Up to date (automatically generate labels such as `introduced in ...`)
- Easy to generate and actualize (no dependency on installed software on client machines)
- Customizable (option to embed additional graphics [e.g.](https://standards.buildingsmart.org/IFC/RELEASE/IFC4_1/FINAL/HTML/schema/ifcgeometricmodelresource/lexical/ifcadvancedbrep.htm)))
- Consistent (no different output from different tools)
- Idiomatic and readable (According to conventions of UML, EXPRESS-G, ...)
- Accessibility (SEO, visually impaired, the images in the current HTML docs are now virtually impossible to find using a search engine)

For these reasons an approach has been built using LaTeX Tikz-UML, superseding a previous implementation using GraphViz, which provided a nice automated lay-out but ultimately was not customizable and idiomatic enough (no ortho edges and UML edge ends for example).

The generated images can be browsed using the following URL:

[https://buildingsmartifcuml.s3.us-east-2.amazonaws.com/output/IFC_4X2.xml/index.html](https://buildingsmartifcuml.s3.us-east-2.amazonaws.com/output/IFC_4X2.xml/index.html)

## EXPRESS serialization

The current conversion procedure already takes some measures to generate idiomatic IFC names. For example, the following 

~~~
ENTITY IfcRail
 SUPERTYPE OF (ONEOF
	(IfcRail
	,IfcGuardRail
	,IfcStockRail
	,IfcCheckRail
	,IfcBlade
	,IfcRackRail))
 SUBTYPE OF (IfcBuildingElement);
END_ENTITY;
~~~

is generated from an XMI definition named "Guard rail"

~~~
<element xmi:idref="EAID_C8E4F29C_B6DA_4d90_A315_9D587B7C32D1" xmi:type="uml:Class" name="Guard rail" scope="public">
~~~

There are still some open issues in the EXPRESS conversion, such as multiple inheritance, untyped attributes, one-ended associations, unordered express associations and more.

The current version can be found at the following URL:

[https://buildingsmartifcuml.s3.us-east-2.amazonaws.com/output/IFC_4X2.exp](https://buildingsmartifcuml.s3.us-east-2.amazonaws.com/output/IFC_4X2.exp)
