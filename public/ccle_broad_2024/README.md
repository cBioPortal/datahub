DepMap Data 
24Q2 Data Release

General
	•	Paper: https://www.nature.com/articles/s41586-019-1186-3
	•	Data source: https://depmap.org/portal/data_page/?tab=allData
	•	Reference genome used: GRCh38


Clinical data:
	•	Data was retrieved from ‘Model.csv’ file from the ‘DepMap Public 24Q2 All Files’.
				
Segmented data:
	•	Data was retrieved from ‘OmicsCNSegmentsProfile’ file from the ‘DepMap Public 24Q2 All Files’.


Mutation data:
	•	Data was retrieved from ‘OmicsSomaticMutationsMAFProfile’ file from the ‘DepMap Public 24Q2 All Files’.
	•	MAF file containing information on all the somatic point mutations and indels called in the DepMap cell lines. The calls are generated from Mutect2.
	•	Annotation with Genome Nexus pipeline.
		
SV data: 
	•	Data was retrieved from ‘OmicsFusionFiltered’ file from the ‘DepMap Public 24Q2 All Files’.
	•	Gene fusion data derived from RNAseq data. Data is filtered using by performing the following:
			- Removing fusion involving mitochondrial chromosomes or HLA genes
			- Removed common false positive fusions (red herring annotations as described in the STAR-Fusion docs)
			- Recurrent fusions observed in CCLE across cell lines (in 10% or more of the samples)
			- Removed fusions where SpliceType='INCL_NON_REF_SPLICE' and LargeAnchorSupport='NO_LDAS' and FFPM < 0.1
			- FFPM < 0.05
	•	Fusion to SV converter tool was used to convert fusion data to structural variant data.

Expression data: 
	•	Expression data was retrieved from ‘OmicsExpressionProteinCodingGenesTPMLogp1’ file from the ‘DepMap Public 24Q2 All Files’.
	•	Data was transformed and used to calculate the Z-scores.