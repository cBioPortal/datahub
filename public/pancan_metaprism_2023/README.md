# META-PRISM

**Publication** : The study is now published in Cancer Discovery and is freely available at https://pubmed.ncbi.nlm.nih.gov/36862804/. 
**Local Instance** : <https://cbioportal.gustaveroussy.fr:8081/study/summary?id=metaprism_2023>.
**Study Id** : pancan_metaprism_2023
**Reference genome** : GRCh37

## Description

## Clinical data: (data_clinical_patient.txt) (data_clinical_sample.txt)

- `Supplementary_Table_1.xlsx` Clinical characteristics and samples of the 1,031 patients included in the META-PRISM
  cohort.

**Clinical data remapping**:
  
| Original column						| Renamed column         				   | Patient/Sample Attribute 	        |
| ---| ---| --- |
| Subject_Id							| Patient_Id			 			   | Patient					|
| Sex								| Sex			 		 		   | Patient					|
| Age_At_Biopsy						| AGE_AT_BIOPSY			 		   | Patient					|
| Oncotree_Code						| Oncotree_Code			 	           | Sample					|
| Primary_Tumor_Site					| Primary Site			 			   | Sample					|
| Histology							| Histology			 	 		   | Sample					|
| Metastatic_Sites						| Metastatic Site 		 			   | Sample					|
| Treatments_Before_Biopsy				| Treatments Before Biopsy			   | Patient					|
| Albumin_At_Biopsy(g/L)				| Albumin At Biopsy(g/L)			 	   | Patient					|
| Lactate_Dehydrogenase_At_Biopsy(UI/L)	| Lactate Dehydrogenase At Biopsy(UI/L) | Patient					|
| Neutrophils_At_Biopsy(10^9/L)			| Neutrophils At Biopsy(10^9/L)		   | Patient					|
| Lymphocytes_At_Biopsy(10^9/L)		| Lymphocytes At Biopsy(10^9/L)	           | Patient					|
| GRIM_Score							| Gustave Roussy Immune Score		   | Patient					|
| Alcohol								| Alcohol History			 		   | Patient					|
| Smoking_History						| Smoking History		 			   | Patient					|
| Vital_Status							| OS status.			 			   | Patient					|
| Sample_Id_DNA_T					| Sample_Id			     		           | Sample					|

## Segmented data: (data_cna_hg19.seg)

- `Data_Table_5.somatic_cna_segments.tsv` Table of all 42,769 curated copy-number segments identified in 569
  WES tumor/normal sample pairs. 
  
## Mutation data: (data_mutations.txt)

- `Data_Table_3.somatic_mutations.maf.gz` Table of all 117,747 somatic mutations detected in 569 analyzed
  WES tumor/normal sample pairs. Only mutations that pass all filters are included.

## Zscore Expression data: (data_mrna_seq_tpm_zscores_ref_all_samples.txt)

- `Data_Table_2.rna_gene_tpm.tsv.gz` Table in 58,288 x 948 format with the expression TPM of 58,288 genes in
  the 947 RNAseq tumor samples.
  
## SV data: (data_sv.txt)

- `Data_Table_10.rna_fusions.tsv.gz` Table of all 707,027 fusion calls as identified by Arriba v1.2.0, EricScript v0.5.5,
  Pizzly v0.37.3, or StarFusion v1.8.1.

## Copy number data: (data_cna.txt)

- `Data_Table_1.rna_gene_counts.tsv.gz` Table in 58,288 x 948 format with the expression raw counts of 58,288 genes in
  the 947 RNAseq tumor samples.

## Mutational Signatures:

(data_mutational_signatures_counts_SBS.txt)
- `Data_Table_9.sbs_96_signature_counts.tsv` Table in 78 x 451 format with the mutation counts contributed by each of
  the 78 signatures from COSMIC SBS v3.2 database in the 450 WES tumor samples .

(data_mutational_signatures_contribution_SBS.txt)
- `Data_Table_11.rna_ssgsea_immune.tsv` Table in 29 x 948 format with the functional gene expression signatures (ssGSEA
  scores) on the 29 gene sets in 947 RNAseq tumor samples.

