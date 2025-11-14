DepMap Data README

Clinical data: 
	•	Data was retrieved from ‘Model.csv’ file from the ‘DepMap Public 25Q2 Files- Primary Files’.
	•	Samples ID: CCLEName
	•	Samples without a CCLEName: CellLineName used as Sample ID 
	•	Depmap ID= ModelID
	•	The cohort is restricted to tumor samples only (all non-cancerous samples (145) were eliminated from the cohort)
	•	Updated Sample IDs:
		VACO 432 --> VACO-432
		YUSEEP-M 16-3517 --> YUSEEP-M-16-3517
	•	Removed Oncotree Primary Disease and Oncotree Lineage as they are redundant to CT and CTD.
	
Mutation data: 
	•	Data was retrieved from ‘OmicsSomaticMutations.csv’ file from the ‘DepMap Public 25Q2 Files- Primary Files’.
	•	Annotation with Genome Nexus pipeline 