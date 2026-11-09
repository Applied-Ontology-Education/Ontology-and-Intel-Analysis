OBJECTIVE 

The idea that I intend to model is conflicting reports on a particular event. To keep data moving smoothly, we must first show who is providing it. This topic is of particular interest to intelligence analysis because it can provide background information on the source itself.  
Since there are many ways a report can differ from person to person, the goal will be to identify a source, as well as claims made. These claims can be influenced by occupation, cultural, and age differences. When working with information provided by multiple sources, you may come across inconsistency, so I intend to model a way that will represent the differences that are observed. 
 The information that will be most necessary for the ontology to accomplish this task will be the event that is being reported on, the individuals that are reporting the event, including their occupation and observations, and effects of the event. The ontology is aimed at helping analysts evaluate inconsistency that can be seen in multiple reports given by different people by comparing information.  

 

SCOPE STATEMENT 

The specific things that the ontology will represent will include information about the source of the report, including their occupation, cultural background, and age. Importantly, it will also contain the event itself, and the effects that arise from the event.  
What will remain outside of the scope of this ontology is truthiness, and validity. Since the ontology is aimed at representing metadata, the information itself will be analyzed by an intelligence analyst.  

 

COMPETENCY QUESTIONS 

-Some of the competency questions that will be included are: 
-What is the source of a report? 
-What is the background information we have available on the source?  
-Which sources describe similar details of a particular event? 
-How long did it take for a report to come in?  
-Is there any information missing between reports that another report may have? 



ARTIFACT  

Current Hierarchy:  

Owl:Thing  
-Agent 
  -Occupation 
-Date 
-Event 
  -Reported event 
-EventEffect 
  -PropertyDamage 
  -SustainedInjury 
-InformationContent 
  -Claim 
  -Observation 
-Location 


Current Relations:  
-ContainsClaim 
-HasEffect 
-HasOccupation 
-hasSource 



SOURCES 
	One of my main influences on this ontology will be the PROV-O ontology which aims to represent provenance. Reusing certain information about sources and their relations will help me establish information about the source itself.  

 

 
