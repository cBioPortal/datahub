## Recommended Staging Filenames:

This document provides recommendations for staging filenames the cancer study data should assume in order for the study to be successfully added to datahub.

cBioPortal provides a set of [staging files formats](https://docs.cbioportal.org/5.1-data-loading/data-loading/file-formats) for the various data types.

Datatype | Data Level | Recommended Data Filename | Recommended Meta Filename | Meta Stable_id | Meta Genetic_alteration_type| Meta Datatype
-- | -- | -- | -- | -- | -- | -- 
Clinical | clinical | data_clinical.txt | meta_clinical.txt | clinical | CLINICAL | CLINICAL
Clinical | clinical-sample | data_clinical_sample.txt | meta_clinical_sample.txt | clinical_sample | CLINICAL | SAMPLE_ATTRIBUTES
Clinical | clinical-patient | data_clinical_patient.txt | meta_clinical_patient.txt | clinical_patient | CLINICAL | PATIENT_ATTRIBUTES
Clinical | clinical-supp | data_clinical_supp.txt | meta_clinical.txt | clinical | CLINICAL | CLINICAL
Timeline | time-line-data | data_timeline.txt | meta_timeline.txt | | CLINICAL | TIMELINE
Timeline | time-line-data-other | data_timeline_*.txt | meta_timeline.txt | | CLINICAL | TIMELINE
CNA | cna-gistic | data_cna.txt | meta_cna.txt | gistic | COPY_NUMBER_ALTERATION | DISCRETE
CNA | cna-rae | data_cna_rae.txt | meta_cna_rae.txt | cna_rae | COPY_NUMBER_ALTERATION | DISCRETE
CNA | cna-consensus | data_cna_consensus.txt | meta_cna_consensus.txt | cna_consensus | COPY_NUMBER_ALTERATION | DISCRETE
CNA | linear-cna-gistic | data_linear_cna.txt | meta_linear_cna.txt | linear_CNA | COPY_NUMBER_ALTERATION | CONTINUOUS
CNA | log2-cna | data_log2_cna.txt | meta_log2_cna.txt | log2CNA | COPY_NUMBER_ALTERATION | LOG2-VALUE
CNA | armlevel-cna | data_armlevel_cna.txt | meta_armlevel_cna.txt | armlevel_cna | GENERIC_ASSAY | CATEGORICAL
CNA | gistic-genes-amp | data_gistic_genes_amp.txt | meta_gistic_genes_amp.txt | gistic_genes_amp | GISTIC_GENES_AMP | Q-VALUE
CNA | gistic-genes-del | data_gistic_genes_del.txt | meta_gistic_genes_del.txt | gistic_genes_del | GISTIC_GENES_DEL | Q-VALUE
Segment | cna-hg19-seg-std | data_cna_hg19.seg | meta_cna_hg19_seg.txt | | COPY_NUMBER_ALTERATION | SEG
Segment | cna-hg18-seg-std | data_cna_hg18.seg | meta_cna_hg18_seg.txt | | COPY_NUMBER_ALTERATION | SEG
Mutation | mutation | data_mutations.txt | meta_mutations.txt | mutations | MUTATION_EXTENDED | MAF
Mutation | mutation-uncalled | data_mutations_uncalled.txt | meta_mutations_uncalled.txt | mutations_uncalled | MUTATION_UNCALLED | MAF
MutSig | mutation-significance-v2 | data_mutsig.txt | meta_mutsig.txt | mutsig | MUTSIG | Q-VALUE
Gene Panel | gene-panel | data_gene_panel.txt | | |
Gene Panel | gene-panel | data_gene_panel_*.txt | | |
Gene Panel Matrix | gene-panel-matrix | data_gene_panel_matrix.txt | meta_gene_panel_matrix.txt | | GENE_PANEL_MATRIX | GENE_PANEL_MATRIX
Fusion | fusion | data_fusions.txt | meta_fusions.txt | mutations | FUSION | FUSION
RPPA | rppa | data_rppa.txt | meta_rppa.txt | rppa | PROTEIN_LEVEL | LOG2-VALUE
RPPA | rppa-zscores | data_rppa_zscores.txt | meta_rppa_zscores.txt | rppa_Zscores | PROTEIN_LEVEL | Z-SCORE
Protein Quantification | protein-quantification | data_protein_quantification.txt | meta_protein_quantification.txt | protein_quantification | PROTEIN_LEVEL | CONTINUOUS
Protein Quantification | protein-quantification-zscores | data_protein_quantification_zscores.txt | meta_protein_quantification_zscores.txt | protein_quantification_zscores | PROTEIN_LEVEL | Z-SCORE
Phosphoprotein Quantification | phosphoprotein_quantification | data_phosphoprotein_quantification.txt | meta_phosphoprotein_quantification.txt | phosphoprotein_quantification | GENERIC_ASSAY | LIMIT-VALUE
Acetylphoprotein Quantification | acetylprotein-quantification | data_acetylprotein_quantification.txt | meta_acetylprotein_quantification.txt | acetylprotein_quantification | GENERIC_ASSAY | CONTINUOUS
Lipidome Quantification | lipidome-positive-quantification | data_lipidome_positive_quantification.txt | meta_lipidome_positive_quantification.txt | lipidome_positive_quantification | GENERIC_ASSAY | CONTINUOUS
Lipidome Quantification | lipidome-negative-quantification | data_lipidome_negative_quantification.txt | meta_lipidome_negative_quantification.txt | lipidome_negative_quantification | GENERIC_ASSAY | CONTINUOUS
Methylation | methylation-hm27 | data_methylation_hm27.txt | meta_methylation_hm27.txt | methylation_hm27 | METHYLATION | CONTINUOUS
Methylation | methylation-hm450 | data_methylation_hm450.txt | meta_methylation_hm450.txt | methylation_hm450 | METHYLATION | CONTINUOUS
Methylation | methylation-promoters-hmepic | data_methylation_promoters_hmepic.txt | meta_methylation_promoters_hmepic.txt | methylation_promoters_hmEPIC | METHYLATION | CONTINUOUS
Methylation | methylation-promoters-wgbs | data_methylation_promoters_wgbs.txt | meta_methylation_promoters_wgbs.txt | methylation_promoters_wgbs | METHYLATION | CONTINUOUS
Methylation | methylation-genebodies-hmepic | data_methylation_genebodies_hmepic.txt | meta_methylation_genebodies_hmepic.txt | methylation_genebodies_hmEPIC | METHYLATION | CONTINUOUS
Methylation | methylation-genebodies-wgbs | data_methylation_genebodies_wgbs.txt | meta_methylation_genebodies_wgbs.txt | methylation_genebodies_wgbs | METHYLATION | CONTINUOUS
mRNA | affymetrix-gene-expression | data_mrna_affymetrix_microarray.txt | meta_mrna_affymetrix_microarray.txt | mrna_U133 | MRNA_EXPRESSION | CONTINUOUS
mRNA | affymetrix-gene-expression-diploid-zscores | data_mrna_affymetrix_microarray_zscores_ref_diploid_samples.txt | meta_mrna_affymetrix_microarray_zscores_ref_diploid_samples.txt | mrna_U133_Zscores | MRNA_EXPRESSION | Z-SCORE
mRNA | affymetrix-gene-expression-all-sample-zscores | data_mrna_affymetrix_microarray_zscores_ref_all_samples.txt | meta_mrna_affymetrix_microarray_zscores_ref_all_samples.txt | mrna_U133_all_sample_Zscores | MRNA_EXPRESSION | Z-SCORE
mRNA | agilent-gene-expression | data_mrna_agilent_microarray.txt | meta_mrna_agilent_microarray.txt | mrna | MRNA_EXPRESSION | CONTINUOUS
mRNA | agilent-gene-expression-diploid-zscores | data_mrna_agilent_microarray_zscores_ref_diploid_samples.txt | meta_mrna_agilent_microarray_zscores_ref_diploid_samples.txt | mrna_median_Zscores | MRNA_EXPRESSION | Z-SCORE
mRNA | agilent-gene-expression-all-sample-zscores | data_mrna_agilent_microarray_zscores_ref_all_samples.txt | meta_mrna_agilent_microarray_zscores_ref_all_samples.txt | mrna_median_all_sample_Zscores | MRNA_EXPRESSION | Z-SCORE
mRNA | rnaseq-gene-expression-rpkm | data_mrna_seq_rpkm.txt | meta_mrna_seq_rpkm.txt | rna_seq_mrna | MRNA_EXPRESSION | CONTINUOUS
mRNA | rnaseq-gene-expression-rpkm-diploid-zscores | data_mrna_seq_rpkm_zscores_ref_diploid_samples.txt | meta_mrna_seq_rpkm_zscores_ref_diploid_samples.txt | rna_seq_mrna_median_Zscores | MRNA_EXPRESSION | Z-SCORE
mRNA | rnaseq-gene-expression-rpkm-all-sample-zscores | data_mrna_seq_rpkm_zscores_ref_all_samples.txt | meta_mrna_seq_rpkm_zscores_ref_all_samples.txt | rna_seq_mrna_median_all_sample_Zscores | MRNA_EXPRESSION | Z-SCORE
mRNA | rnaseq-gene-expression-rsem | data_mrna_seq_v2_rsem.txt | meta_mrna_seq_v2_rsem.txt | rna_seq_v2_mrna | MRNA_EXPRESSION | CONTINUOUS
mRNA | rnaseq-gene-expression-rsem-diploid-zscores | data_mrna_seq_v2_rsem_zscores_ref_diploid_samples.txt | meta_mrna_seq_v2_rsem_zscores_ref_diploid_samples.txt | rna_seq_v2_mrna_median_Zscores | MRNA_EXPRESSION | Z-SCORE
mRNA | rnaseq-gene-expression-rsem-all-sample-zscores | data_mrna_seq_v2_rsem_zscores_ref_all_samples.txt | meta_mrna_seq_v2_rsem_zscores_ref_all_samples.txt | rna_seq_v2_mrna_median_all_sample_Zscores | MRNA_EXPRESSION | Z-SCORE
mRNA | rnaseq-gene-expression-rsem-normal | data_mrna_seq_v2_rsem_normal_samples.txt | meta_mrna_seq_v2_rsem_normal_samples.txt | rna_seq_v2_mrna_median_normals | MRNA_EXPRESSION | CONTINUOUS
mRNA | rnaseq-gene-expression-rsem-normal-zscores | data_mrna_seq_v2_rsem_normal_samples_zscores_ref_normal_samples.txt | meta_mrna_seq_v2_rsem_normal_samples_zscores_ref_normal_samples.txt | rna_seq_v2_mrna_median_normals_Zscores | MRNA_EXPRESSION | Z-SCORE
mRNA | rnaseq-gene-expression-rsem-all-sample-ref-normal-zscores | data_mrna_seq_v2_rsem_zscores_ref_normal_samples.txt | meta_mrna_seq_v2_rsem_zscores_ref_normal_samples.txt | rna_seq_v2_mrna_median_all_sample_ref_normal_Zscores | MRNA_EXPRESSION | Z-SCORE
mRNA | rnaseq-gene-expression-cpm | data_mrna_seq_cpm.txt | meta_mrna_seq_cpm.txt | mrna_seq_cpm | MRNA_EXPRESSION | CONTINUOUS
mRNA | rnaseq-gene-expression-cpm-diploid-zscores | data_mrna_seq_cpm_zscores_ref_diploid_samples.txt | meta_mrna_seq_cpm_zscores_ref_diploid_samples.txt | mrna_seq_cpm_Zscores | MRNA_EXPRESSION | Z-SCORE
mRNA | rnaseq-gene-expression-cpm-all-sample-zscores | data_mrna_seq_cpm_zscores_ref_all_samples.txt | meta_mrna_seq_cpm_zscores_ref_all_samples.txt | mrna_seq_cpm_all_sample_Zscores | MRNA_EXPRESSION | Z-SCORE
mRNA | rnaseq-gene-expression-tpm | data_mrna_seq_tpm.txt | meta_mrna_seq_tpm.txt | mrna_seq_tpm | MRNA_EXPRESSION | CONTINUOUS
mRNA | rnaseq-gene-expression-tpm-diploid-zscores | data_mrna_seq_tpm_zscores_ref_diploid_samples.txt | meta_mrna_seq_tpm_zscores_ref_diploid_samples.txt | mrna_seq_tpm_Zscores | MRNA_EXPRESSION | Z-SCORE
mRNA | rnaseq-gene-expression-tpm-all-sample-zscores | data_mrna_seq_tpm_zscores_ref_all_samples.txt | meta_mrna_seq_tpm_zscores_ref_all_samples.txt | mrna_seq_tpm_all_sample_Zscores | MRNA_EXPRESSION | Z-SCORE
mRNA | mrna-seq-fpkm | data_mrna_seq_fpkm.txt | meta_mrna_seq_fpkm.txt | mrna_seq_fpkm | MRNA_EXPRESSION | CONTINUOUS
mRNA | mrna-seq-fpkm-diploid-zscores | data_mrna_seq_fpkm_zscores_ref_diploid_samples.txt | meta_mrna_seq_fpkm_zscores_ref_diploid_samples.txt | mrna_seq_fpkm_Zscores | MRNA_EXPRESSION | Z-SCORE
mRNA | mrna-seq-fpkm-all-sample-zscores | data_mrna_seq_fpkm_zscores_ref_all_samples.txt | meta_mrna_seq_fpkm_zscores_ref_all_samples.txt | mrna_seq_fpkm_all_sample_Zscores | MRNA_EXPRESSION | Z-SCORE
mRNA | mrna-outliers | data_mrna_outliers.txt | meta_mrna_outliers.txt | mrna_outliers | MRNA_EXPRESSION | DISCRETE
cRNA | crna-quantification | data_circular_rna.txt | meta_circular_rna.txt | crna_quantification | GENERIC_ASSAY | CONTINUOUS
miRNA | mirna-expression | data_mirna.txt | meta_mirna.txt | mirna | MRNA_EXPRESSION | CONTINUOUS
miRNA | mirna-expression-zscores | data_mirna_zscores.txt | meta_mirna_zscores.txt | mirna_median_Zscores | MRNA_EXPRESSION | Z-SCORE
Microbiome | microbiome-signatures | data_microbiome.txt | meta_microbiome.txt | microbiome_signature | GENERIC_ASSAY | LIMIT-VALUE
GSVA | gsva-scores | data_gsva_scores.txt | meta_gsva_scores.txt | gsva_scores | GENESET_SCORE | GSVA-SCORE
GSVA | gsva-pvalues | data_gsva_pvalues.txt | meta_gsva_pvalues.txt | gsva_pvalues | GENESET_SCORE | P-VALUE
Generic Assay | drug-treatment-ic50 | data_drug_treatment_ic50.txt | meta_drug_treatment_ic50.txt | CCLE_drug_treatment_IC50 | GENERIC_ASSAY | LIMIT-VALUE
Generic Assay | drug-treatment-ic50-zscores | data_drug_treatment_zscore.txt | meta_drug_treatment_zscore.txt | CCLE_drug_treatment_zscore | GENERIC_ASSAY | LIMIT-VALUE
Generic Assay | drug-treatment-auc | data_drug_treatment_auc.txt | meta_drug_treatment_auc.txt | CCLE_drug_treatment_AUC | GENERIC_ASSAY | LIMIT-VALUE
Resource Data | resource-definition | data_resource_definition.txt | meta_resource_definition.txt | | |
Resource Data | resource-study | data_resource_study.txt | meta_resource_study.txt | | |
Resource Data | resource-sample | data_resource_sample.txt | meta_resource_sample.txt | | |
Structural Variant | sv | data_sv.txt | meta_sv.txt | structural_variants | STRUCTURAL_VARIANT | SV
