## Changes to the filenames on datahub:

Based on the user questions over time, some of the mRNA expression data filenames we follow were confusing or might not apply to all the studies. Hence we have reviewed all the filenames we use and have updated them to be more clear, self-explanatory.

The decisions behind the renaming are logged in the issue: https://github.com/cBioPortal/datahub/issues/445.

Here is the list of all the old data filenames and the new naming patterns they were updated to for reference: (this list doesn't include the filenames with no updates)

File Category | Old Data Filename | New Data Filename
-- | -- | --
Clinical | data_bcr_clinical_data_patient.txt | data_clinical_patient.txt
Clinical | data_bcr_clinical_data_sample.txt | data_clinical_sample.txt
CNA | data_CNA.txt | data_cna.txt
CNA | data_linear_CNA.txt | data_linear_cna.txt
CNA | data_log2_CNA.txt | data_log2_cna.txt
CNA | data_log2CNA.txt | data_log2_cna.txt
CNA | data_CNA_consensus.txt | data_cna_consensus.txt
CNA | data_CNA_RAE.txt | data_cna_rae.txt
CNA | data_armlevel_CNA.txt | data_armlevel_cna.txt
RPPA | data_rppa_Zscores.txt | data_rppa_zscores.txt
Protein Quantification | data_protein_quantification_Zscores.txt | data_protein_quantification_zscores.txt
MAF | data_mutations_extended.txt | data_mutations_uniprot_canonical_transcripts.txt
MAF | data_mutations_extended_*.txt | data_mutations_uniprot_canonical_transcripts_*.txt
MAF | data_mutations_mskcc.txt | data_mutations_mskimpact_transcripts.txt
Gene Panel | data_gene_matrix.txt | data_gene_panel_matrix.txt
Generic Assay | data_drug_treatment_AUC.txt | data_drug_treatment_auc.txt
Generic Assay | data_drug_treatment_IC50.txt | data_drug_treatment_ic50.txt
Generic Assay | data_drug_treatment_ZSCORE.txt | data_drug_treatment_zscore.txt
mRNA | data_expression.txt | data_mrna_affymetrix_microarray.txt
mRNA | data_expression_Zscores.txt | data_mrna_affymetrix_microarray_zscores_ref_diploid_samples.txt
mRNA | data_expression_all_sample_Zscores.txt | data_mrna_affymetrix_microarray_zscores_ref_all_samples.txt
mRNA | data_expression_median.txt | data_mrna_agilent_microarray.txt
mRNA | data_mRNA_median_Zscores.txt | data_mrna_agilent_microarray_zscores_ref_diploid_samples.txt
mRNA | data_mRNA_median_all_sample_Zscores.txt | data_mrna_agilent_microarray_zscores_ref_all_samples.txt
mRNA | data_RNA_Seq_expression_median.txt | data_mrna_seq_rpkm.txt
mRNA | data_rna_seq_mrna.txt | data_mrna_seq_rpkm.txt
mRNA | data_rna_seq_mrna_median_Zscores.txt | data_mrna_seq_rpkm_zscores_ref_diploid_samples.txt
mRNA | data_RNA_Seq_mRNA_median_Zscores.txt | data_mrna_seq_rpkm_zscores_ref_diploid_samples.txt
mRNA | data_expression_zscores_file.txt | data_mrna_seq_rpkm_zscores_ref_diploid_samples.txt
mRNA | data_RNA_Seq_mRNA_median_all_sample_Zscores.txt | data_mrna_seq_rpkm_zscores_ref_all_samples.txt
mRNA | data_RNA_Seq_v2_expression_median.txt | data_mrna_seq_v2_rsem.txt
mRNA | data_RNA_Seq_v2_expression_RSEM_UQ_Log2.txt | data_mrna_seq_v2_rsem.txt
mRNA | data_RNA_Seq_v2_mRNA_median_Zscores.txt | data_mrna_seq_v2_rsem_zscores_ref_diploid_samples.txt
mRNA | data_RNA_Seq_v2_mRNA_median_all_sample_Zscores.txt | data_mrna_seq_v2_rsem_zscores_ref_all_samples.txt
mRNA | data_mRNA_seq_fpkm_capture.txt | data_mrna_seq_fpkm_capture.txt
mRNA | data_mRNA_seq_fpkm_capture_Zscores.txt | data_mrna_seq_fpkm_capture_zscores_ref_diploid_samples.txt
mRNA | data_mRNA_seq_fpkm_capture_all_sample_Zscores.txt | data_mrna_seq_fpkm_capture_zscores_ref_all_samples.txt
mRNA | data_mRNA_seq_fpkm_polya.txt | data_mrna_seq_fpkm_polya.txt
mRNA | data_mRNA_seq_fpkm_polya_Zscores.txt | data_mrna_seq_fpkm_polya_zscores_ref_diploid_samples.txt
mRNA | data_mRNA_seq_fpkm_polya_all_sample_Zscores.txt | data_mrna_seq_fpkm_polya_zscores_ref_all_samples.txt
mRNA | data_RNA_Seq_expression_cpm.txt | data_mrna_seq_cpm.txt
mRNA | data_RNA_Seq_expression_cpm_Zscores.txt | data_mrna_seq_cpm_zscores_ref_diploid_samples.txt
mRNA | data_RNA_Seq_expression_cpm_all_sample_Zscores.txt | data_mrna_seq_cpm_zscores_ref_all_samples.txt
mRNA | data_RNA_Seq_expression_tpm.txt | data_mrna_seq_tpm.txt
mRNA | data_RNA_Seq_expression_tpm_Zscores.txt | data_mrna_seq_tpm_zscores_ref_diploid_samples.txt
mRNA | data_RNA_Seq_expression_tpm_all_sample_Zscores.txt | data_mrna_seq_tpm_zscores_ref_all_samples.txt
mRNA | data_RNA_Seq_v2_mRNA_median_normals.txt | data_mrna_seq_v2_rsem_normal_samples.txt
mRNA | data_RNA_Seq_v2_mRNA_median_Zscores_normals.txt | data_mrna_seq_v2_rsem_normal_samples_zscores_ref_normal_samples.txt
mRNA | data_RNA_Seq_v2_mRNA_median_all_sample_ref_normal_Zscores.txt | data_mrna_seq_v2_rsem_zscores_ref_normal_samples.txt
mRNA | data_expression_merged.txt | data_mrna_affymetrix_microarray_merged.txt
mRNA | data_expression_merged_Zscores.txt | data_mrna_affymetrix_microarray_merged_zscores_ref_diploid_samples.txt
mRNA | data_expression_merged_median_Zscores.txt | data_mrna_mirna_merged_zscores.txt
mRNA | data_mRNA_outliers.txt | data_mrna_outliers.txt
miRNA | data_expression_miRNA.txt | data_mirna.txt
miRNA | data_miRNA_median_Zscores.txt | data_mirna_zscores.txt
SV | data_SV.txt | data_sv.txt
Methylation | data_methylation_promoters_hmEPIC.txt | data_methylation_promoters_hmepic.txt
Methylation | data_methylation_genebodies_hmEPIC.txt | data_methylation_genebodies_hmepic.txt

Some of the filename updates here are just case changes. All the filenames were lowercased for uniformity.