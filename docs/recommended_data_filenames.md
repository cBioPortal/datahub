## Recommended Data Filenames:

This document provides recommendations for staging filenames the cancer study data should assume in order for the study to be successfully added to datahub.

cBioPortal provides a set of [staging files formats](https://docs.cbioportal.org/5.1-data-loading/data-loading/file-formats) for the various data types.

Datatype | Data Level | Recommended Data Filename | Recommended Meta Filename
-- | -- | -- | --
Clinical | clinical | data_clinical.txt | meta_clinical.txt
Clinical | clinical-sample | data_clinical_sample.txt | meta_clinical_sample.txt
Clinical | clinical-patient | data_clinical_patient.txt | meta_clinical_patient.txt
Clinical | clinical-supp | data_clinical_supp.txt | meta_clinical.txt
Timeline | time-line-data | data_timeline.txt | meta_timeline.txt
Timeline | time-line-data-other | data_timeline_*.txt | meta_timeline.txt
CNA | cna-gistic | data_cna.txt | meta_cna.txt
CNA | cna-rae | data_cna_rae.txt | meta_cna_rae.txt
CNA | cna-consensus | data_cna_consensus.txt | meta_cna_consensus.txt
CNA | linear-cna-gistic | data_linear_cna.txt | meta_linear_cna.txt
CNA | log2-cna | data_log2_cna.txt | meta_log2_cna.txt
CNA | armlevel-cna | data_armlevel_cna.txt | meta_armlevel_cna.txt
CNA | gistic-genes-amp | data_gistic_genes_amp.txt | meta_gistic_genes_amp.txt
CNA | gistic-genes-del | data_gistic_genes_del.txt | meta_gistic_genes_del.txt
Segment | cna-hg19-seg-std | data_cna_hg19.seg | meta_cna_hg19_seg.txt
Segment | cna-hg18-seg-std | data_cna_hg18.seg | meta_cna_hg18_seg.txt
Mutation | mutation | data_mutations.txt | meta_mutations.txt
Mutation | mutation-uncalled | data_mutations_uncalled.txt | meta_mutations_uncalled.txt
MutSig | mutation-significance-v2 | data_mutsig.txt | meta_mutsig.txt
Gene Panel | gene-panel | data_gene_panel.txt
Gene Panel | gene-panel | data_gene_panel_*.txt
Gene Panel Matrix | gene-panel-matrix | data_gene_panel_matrix.txt | meta_gene_panel_matrix.txt
Fusion | fusion | data_fusions.txt | meta_fusions.txt
RPPA | rppa | data_rppa.txt | meta_rppa.txt
RPPA | rppa-zscores | data_rppa_zscores.txt | meta_rppa_zscores.txt
Protein Quantification | protein-quantification | data_protein_quantification.txt | meta_protein_quantification.txt
Protein Quantification | protein-quantification-zscores | data_protein_quantification_zscores.txt | meta_protein_quantification_zscores.txt
Phosphoprotein Quantification | phosphoprotein_quantification | data_phosphoprotein_quantification.txt | meta_phosphoprotein_quantification.txt
Acetylphoprotein Quantification | acetylprotein-quantification | data_acetylprotein_quantification.txt | meta_acetylprotein_quantification.txt
Lipidome Quantification | lipidome-positive-quantification | data_lipidome_positive_quantification.txt | meta_lipidome_positive_quantification.txt
Lipidome Quantification | lipidome-negative-quantification | data_lipidome_negative_quantification.txt | meta_lipidome_negative_quantification.txt
Methylation | methylation-hm27 | data_methylation_hm27.txt | meta_methylation_hm27.txt
Methylation | methylation-hm450 | data_methylation_hm450.txt | meta_methylation_hm450.txt
Methylation | methylation-promoters-hmepic | data_methylation_promoters_hmepic.txt | meta_methylation_promoters_hmepic.txt
Methylation | methylation-promoters-wgbs | data_methylation_promoters_wgbs.txt | meta_methylation_promoters_wgbs.txt
Methylation | methylation-genebodies-hmepic | data_methylation_genebodies_hmepic.txt | meta_methylation_genebodies_hmepic.txt
Methylation | methylation-genebodies-wgbs | data_methylation_genebodies_wgbs.txt | meta_methylation_genebodies_wgbs.txt
mRNA | affymetrix-gene-expression | data_mrna_affymetrix_microarray.txt | meta_mrna_affymetrix_microarray.txt
mRNA | affymetrix-gene-expression-diploid-zscores | data_mrna_affymetrix_microarray_zscores_ref_diploid_samples.txt | meta_mrna_affymetrix_microarray_zscores_ref_diploid_samples.txt
mRNA | affymetrix-gene-expression-all-sample-zscores | data_mrna_affymetrix_microarray_zscores_ref_all_samples.txt | meta_mrna_affymetrix_microarray_zscores_ref_all_samples.txt
mRNA | agilent-gene-expression | data_mrna_agilent_microarray.txt | meta_mrna_agilent_microarray.txt
mRNA | agilent-gene-expression-diploid-zscores | data_mrna_agilent_microarray_zscores_ref_diploid_samples.txt | meta_mrna_agilent_microarray_zscores_ref_diploid_samples.txt
mRNA | agilent-gene-expression-all-sample-zscores | data_mrna_agilent_microarray_zscores_ref_all_samples.txt | meta_mrna_agilent_microarray_zscores_ref_all_samples.txt
mRNA | rnaseq-gene-expression-rpkm | data_mrna_seq_rpkm.txt | meta_mrna_seq_rpkm.txt
mRNA | rnaseq-gene-expression-rpkm-diploid-zscores | data_mrna_seq_rpkm_zscores_ref_diploid_samples.txt | meta_mrna_seq_rpkm_zscores_ref_diploid_samples.txt
mRNA | rnaseq-gene-expression-rpkm-all-sample-zscores | data_mrna_seq_rpkm_zscores_ref_all_samples.txt | meta_mrna_seq_rpkm_zscores_ref_all_samples.txt
mRNA | rnaseq-gene-expression-rsem | data_mrna_seq_v2_rsem.txt | meta_mrna_seq_v2_rsem.txt
mRNA | rnaseq-gene-expression-rsem-diploid-zscores | data_mrna_seq_v2_rsem_zscores_ref_diploid_samples.txt | meta_mrna_seq_v2_rsem_zscores_ref_diploid_samples.txt
mRNA | rnaseq-gene-expression-rsem-all-sample-zscores | data_mrna_seq_v2_rsem_zscores_ref_all_samples.txt | meta_mrna_seq_v2_rsem_zscores_ref_all_samples.txt
mRNA | rnaseq-gene-expression-rsem-normal | data_mrna_seq_v2_rsem_normal_samples.txt | meta_mrna_seq_v2_rsem_normal_samples.txt
mRNA | rnaseq-gene-expression-rsem-normal-zscores | data_mrna_seq_v2_rsem_normal_samples_zscores_ref_normal_samples.txt | meta_mrna_seq_v2_rsem_normal_samples_zscores_ref_normal_samples.txt
mRNA | rnaseq-gene-expression-rsem-all-sample-ref-normal-zscores | data_mrna_seq_v2_rsem_zscores_ref_normal_samples.txt | meta_mrna_seq_v2_rsem_zscores_ref_normal_samples.txt
mRNA | rnaseq-gene-expression-cpm | data_mrna_seq_cpm.txt | meta_mrna_seq_cpm.txt
mRNA | rnaseq-gene-expression-cpm-diploid-zscores | data_mrna_seq_cpm_zscores_ref_diploid_samples.txt | meta_mrna_seq_cpm_zscores_ref_diploid_samples.txt
mRNA | rnaseq-gene-expression-cpm-all-sample-zscores | data_mrna_seq_cpm_zscores_ref_all_samples.txt | meta_mrna_seq_cpm_zscores_ref_all_samples.txt
mRNA | rnaseq-gene-expression-tpm | data_mrna_seq_tpm.txt | meta_mrna_seq_tpm.txt
mRNA | rnaseq-gene-expression-tpm-diploid-zscores | data_mrna_seq_tpm_zscores_ref_diploid_samples.txt | meta_mrna_seq_tpm_zscores_ref_diploid_samples.txt
mRNA | rnaseq-gene-expression-tpm-all-sample-zscores | data_mrna_seq_tpm_zscores_ref_all_samples.txt | meta_mrna_seq_tpm_zscores_ref_all_samples.txt
mRNA | mrna-seq-fpkm | data_mrna_seq_fpkm.txt | meta_mrna_seq_fpkm.txt
mRNA | mrna-seq-fpkm-diploid-zscores | data_mrna_seq_fpkm_zscores_ref_diploid_samples.txt | meta_mrna_seq_fpkm_zscores_ref_diploid_samples.txt
mRNA | mrna-seq-fpkm-all-sample-zscores | data_mrna_seq_fpkm_zscores_ref_all_samples.txt | meta_mrna_seq_fpkm_zscores_ref_all_samples.txt
mRNA | mrna-outliers | data_mrna_outliers.txt | meta_mrna_outliers.txt
cRNA | crna-quantification | data_circular_rna.txt | meta_circular_rna.txt
miRNA | mirna-expression | data_mirna.txt | meta_mirna.txt
miRNA | mirna-expression-zscores | data_mirna_zscores.txt | meta_mirna_zscores.txt
Microbiome | microbiome-signatures | data_microbiome.txt | meta_microbiome.txt
GSVA | gsva-scores | data_gsva_scores.txt | meta_gsva_scores.txt
GSVA | gsva-pvalues | data_gsva_pvalues.txt | meta_gsva_pvalues.txt
Generic Assay | drug-treatment-ic50 | data_drug_treatment_ic50.txt | meta_drug_treatment_ic50.txt
Generic Assay | drug-treatment-ic50-zscores | data_drug_treatment_zscore.txt | meta_drug_treatment_zscore.txt
Generic Assay | drug-treatment-auc | data_drug_treatment_auc.txt | meta_drug_treatment_auc.txt
Resource Data | resource-definition | data_resource_definition.txt | meta_resource_definition.txt
Resource Data | resource-study | data_resource_study.txt | meta_resource_study.txt
Resource Data | resource-sample | data_resource_sample.txt | meta_resource_sample.txt
Structural Variant | sv | data_sv.txt | meta_sv.txt