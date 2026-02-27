DepMap Data README
25Q3 Release Update 

** Disclamer: The CCLE data in cBioPortal is provisional and will continue to be updated based on Depmap dataset releases. 

Clinical data: 
	•	Data was retrieved from ‘Model.csv’ file from the ‘DepMap Public 25Q3 Files- Primary Files’.
	•	Samples ID: CCLEName
	•	Samples without a CCLEName: CellLineName used as Sample ID 
	•	Depmap ID= ModelID
	•	The cohort is restricted to tumor samples only (all non-cancerous samples (151) were eliminated from the cohort)
		Complete cohort (cancerous+non-cancerous) is 2132 samples, and non-cancerous samples are identified from the "Oncotree Primary Disease" attribute and eliminated for a total cohort of 1981 samples
	•	Updated Sample IDs:
		VACO 432 --> VACO-432
		YUSEEP-M 16-3517 --> YUSEEP-M-16-3517
	
	
Mutation data: 
	•	Data was retrieved from ‘OmicsSomaticMutations.csv’ file from the ‘DepMap Public 25Q3 Files- Primary Files’.
	•	Annotation with Genome Nexus pipeline
	
Expression data: 
 	•	Data was retrieved from ‘OmicsExpressionTPMLogp1HumanProteinCodingGenes.csv’ file from the ‘DepMap Public 25Q3 Files- Primary Files’.
	•	Z-scores were computed using the z-score calculator (NormalizeExpressionLevels_allsampleref.py) from the datahub study curation tools 
	
Copy number data: 
 	•	Data was retrieved from ‘OmicsCNGeneWGS.csv’ file from the ‘DepMap Public 25Q3 Files- Primary Files’.
 	•	Segmented data was retrieved from (OmicsCNSegmentsWGS.csv) file from the ‘DepMap Public 25Q3 Files- Supplemental Files'.
 	
 * ModelID used in data files has been mapped to the CCLEName to maintain consistency with previous Depmap releases in cBioPortal.
