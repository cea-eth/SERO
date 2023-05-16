# FoIP - Formalization of Inventory Processes

The transition to a circular economy and the closure of material loops in the construction sector require careful consideration of material stocks. However, there is a lack of consensus on the specific information needed to assess the reusability of building elements, specifically steel beams. This thesis aims to address this issue within the European and Swiss context. Additionally, digital technologies are recognized as critical enablers of the circular economy, and any consensus reached should be translated into digital formats. Therefore, the thesis also focuses on developing a digital ontology for reusing building elements, specifically steel beams. The research questions are: (1) What information is required to assess the reusability of steel beams in building audits? (2) What should an ontology for building audits to determine steel beam reusability look like? By formalizing and transforming expert knowledge into a readable format for both humans and machines, this thesis aims to facilitate the application of circular economy principles in the construction industry. The research methodology includes literature reviews, surveys, and interviews with reuse experts. The findings contribute to the development of an ontology, the SERO (Steel Element Reuse Ontology), which provides definitions and a logical framework for assessing the reuse potential of steel beams.

# Table of Contents
* [Literature Research](#Literature_Research)
* [Survey Analysis](#Survey_Analysis)
* [Interview Analysis](#Interview_Analysis)
* [SERO](#SERO)

# <a name="Literature_Research"></a>Literature Research

A semi-structured literature research was conducted to investigate the research field. Two distinct research approaches were established to locate relevant literature pertaining to each of the research questions.

The literature identified from Scopus and Web of Science was exported as a CSV file. Subsequently, the data was merged, sorted, and duplicates were removed (Step01). The literature was then sorted again based on title (Step02) and abstract (Step03). The same process was applied to the literature obtained from other master theses.

The finalized collection of literature can be found in 01_LiteratureResearch/Research_02. Nevertheless, additional literature was reviewed subsequently.

The code to sort the literature was inspired by the work of Kira Kulik.

# <a name="Survey_Analysis"></a>Survey Analysis

The responses from the survey participants were exported as a CSV file. The CSV files containing the answers in English, French, and German were processed using the Vis_Results_Survey.py program. Initially, the French and German results were translated into English. Then, the results were plotted, and subsequently, the plots along with a final CSV file containing an English summary were exported.

The results of the survey, including the viszalization can be found in 02_Survey/Results_Survey

# <a name="Interview_Analysis"></a>Interview Analysis

The interview participants' responses were exported from the Miro board as a CSV file. The CSV files contained the answers in French and German, which were then processed using the Analysis_Interviews.py program. Firstly, the French and German results were translated into English. Then, an overview was generated to illustrate the frequency of specific factors mentioned by the participants. Subsequently, the plots, along with a final CSV file containing an English summary, were exported.

As a follow-up step, a heat map was generated to visually represent the association between factors and their respective classes. The heat map was subsequently processed using Excel for further analysis and manipulation.

The results of the interview, including the viszalization can be found in 03_Interviews/Results_Interview

# <a name="SERO"></a>SERO
