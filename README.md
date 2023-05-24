# FoIP - Formalization of Inventory Processes

The construction sector's transition to a circular economy necessitates meticulous consideration of material stocks and the closure of material loops. To facilitate circular economy practices in the construction industry, digital tools, and technologies rely on accurate information regarding material stocks. However, there needs to be more consensus regarding the specific information required to assess the reusability of building elements, particularly steel beams. This master thesis addresses this issue within the European and Swiss contexts. Recognizing the critical role of digital technologies as enablers of the circular economy, any consensus achieved needs to be translated into digital formats. Therefore, this thesis focuses on developing a digital ontology for assessing the reusability of steel beams in building audits. It aims to determine the necessary information for evaluating steel beam reusability and explore the structure and content of an ontology dedicated to conducting such audits. This thesis aims to facilitate the practical application of circular economy principles in the construction industry by formalizing and transforming expert knowledge into a readable format for humans and machines. The research methodology involves comprehensive literature reviews, surveys, and interviews conducted with experts in building element reuse. The findings contribute to the development of the Steel Element Reuse Ontology (SERO), which establishes definitions and a logical framework for assessing the reuse potential of steel beams. Through this thesis, a step towards enhancing circular economy practices in construction is taken by providing a robust foundation to evaluate the reusability of steel beams using digital tools and technologies.

In order to examine the findings from the Literature Research, Survey, and Interview, small sections of code were developed. These code snippets are designed to be easily incorporated and utilized. The purpose of these applications is to analyze the provided data, and they are presented solely for the purposes of evaluation and review.

## Table of Contents
* [Literature Research](#Literature_Research)
* [Survey Analysis](#Survey_Analysis)
* [Interview Analysis](#Interview_Analysis)
* [SERO](#SERO)

## <a name="Literature_Research"></a>Literature Research

A semi-structured literature research was conducted to investigate the research field. Two distinct research approaches were established to locate relevant literature pertaining to each of the research questions.

The literature identified from Scopus and Web of Science was exported as a CSV file. Subsequently, the data was merged, sorted, and duplicates were removed (Step01). The literature was then sorted again based on title (Step02) and abstract (Step03). The same process was applied to the literature obtained from other master theses.

The finalized collection of literature can be found in 01_LiteratureResearch/Research_02. Nevertheless, additional literature was reviewed subsequently.

The code to sort the literature was inspired by the work of Kira Kulik.

## <a name="Survey_Analysis"></a>Survey Analysis

The responses from the survey participants were exported as a CSV file. The CSV files containing the answers in English, French, and German were processed using the Vis_Results_Survey.py program. Initially, the French and German results were translated into English. Then, the results were plotted, and subsequently, the plots along with a final CSV file containing an English summary were exported.

The results of the survey, including the viszalization can be found in 02_Survey/Results_Survey

## <a name="Interview_Analysis"></a>Interview Analysis

The interview participants' responses were exported from the Miro board as a CSV file. The CSV files contained the answers in French and German, which were then processed using the Analysis_Interviews.py program. Firstly, the French and German results were translated into English. Then, an overview was generated to illustrate the frequency of specific factors mentioned by the participants. Subsequently, the plots, along with a final CSV file containing an English summary, were exported.

As a follow-up step, a heat map was generated to visually represent the association between factors and their respective classes. The heat map was subsequently processed using Excel for further analysis and manipulation.

The results of the interview, including the viszalization can be found in 03_Interviews/Results_Interview

## <a name="SERO"></a>SERO

The development of SERO involved utilizing the ontology editor [Protégé](https://protege.stanford.edu/). The front-end was built using the python library [flask](https://palletsprojects.com/p/flask/), while [Jotform](https://www.jotform.com/) was employed to design the questionnaire. Additionally, [nicepage.com](https://nicepage.com/) was utilized to create the results page.

However, the front-end application for populating and testing SERO can be tested using any python developer tool, such as PyCharm. To begin, obtain the git repository and import the libraries mentioned in the *requirements.txt* file if they are not imported automatically. Follow the steps below:

**Setup**:

1. Open the file *reasoner.py*. </br>
2. Provide the path to your local java.exe file by assigning it to the variable `owlready2.JAVA_EXE`, or refer to the instructions provided within *reasoner.py*.

**Test SERO**:

1. Launch *app.py*. </br>
2. Copy the displayed URL, append "/userinput" to it, and paste the modified URL into the command bar of your browser.</br>
3. The front-end interface should appear. Enter all the required information and click *send*. </br>
5. The reasoner executes in the background. Once the reasoning process is complete, the results will be shown. </br>
