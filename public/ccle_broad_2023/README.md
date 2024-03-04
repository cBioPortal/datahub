
General
	•	Paper: https://www.nature.com/articles/s41586-019-1186-3
	•	Data source: https://depmap.org/portal/download/all/
	•	Reference genome used: GRCh38


Clinical data: 
	•	Data was retrieved from ‘Model.csv’ file from the ‘DepMap Public 23Q4 All Files’.
	•	Samples without a CCLE ID: Cell line name used as Patient/Sample ID 
				
Segmented data: 
	•	Data was retrieved from ‘OmicsCNSegmentsProfile’ file from the ‘DepMap Public 23Q4 All Files’.


Mutation data: 
	•	Data was retrieved from ‘OmicsSomaticMutationsMAFProfile’ file from the ‘DepMap Public 23Q4 All Files’.
	•	Annotation with Genome Nexus pipeline 
		
SV data:
	•	Data was retrieved from ‘OmicsFusionFiltered’ file from the ‘DepMap Public 23Q4 All Files’.

Expression data: 
	•	Expression data was retrieved from ‘OmicsExpressionProteinCodingGenesTPMLogp1’ file from the ‘DepMap Public 23Q4 All Files’.
	•	Data was transformed and used to calculate the Z-scores.

Copy number data:
	•	CNA data was retrieved from ‘OmicsCNGene’ file from the ‘DepMap Public 23Q4 All Files’.
	•	The copy number data is log2 transformed. 
