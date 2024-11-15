# Comments & assumptions made during curation

## General
- Paper: https://www.cell.com/cancer-cell/fulltext/S1535-6108(22)00312-9
- Reference genome used: GRCh37
- Entrez IDs were mapped to existing Hugo symbols in file using the genes API (http://www.cbioportal.org/api/genes)
- Most data is stored on [biodev](https://biodev.github.io/BeatAML2/)
- Remapped patient ids to 'aml_ohsu_2022_PATIENTID'
- Remapped sample ids to 'aml_ohsu_2022_PATIENTID_SAMPLEID', removing the trailing 'R'/'D' on samples to combine WES/RNAseq in one sample

## Clinical data
- Supplementary Table 1 
  - Filename: mmc2.xlsx
- For clinical data remapping, look at [Remapped clinical columns](#clinical-data-remapping)
- Annotated as many attributes as possible with the MSK API

## Timeline data
- Not created. There is no data that is relative to time of first diagnosis.

## Mutation data
- Retrieved from [biodev](https://biodev.github.io/BeatAML2/). 
  - Filename: beataml_wes_wv1to4_mutations_dbgap.txt
<br><br>
- All samples with `tumor_only == 0` have matched normal samples
- Protein change already present in MAF, wrapper script not used
- Remapped MAF columns:

| Original | cBioPortal |
|---|---|
|dbgap_sample_id|Tumor_Sample_Barcode|
|seqnames|Start_Position|
|pos_start|End_Position|
|pos_end|Chromosome|
|ref|Reference_Allele|
|alt|Tumor_Seq_Allele2|
|hgvsp_short|HGVSp_Short|
|allele_reads|t_alt_count|
|normal_allele_reads|n_alt_count|
|variant_classification|Variant_Classification|
|symbol|Hugo_Symbol|

- Calculated t_ref_count by `total_reads - t_alt_count`
- Calculated n_ref_count by `normal_total_reads - n_alt_count`
- Remapped Variant_Classification column to cBioPortal standard:

| Original value           | cBioPortal value       |
|--------------------------|------------------------|
| frameshift_variant       | Nonsense_Mutation      |
| missense_variant         | Missense_Mutations     |
| stop_gained              | Nonsense_Mutation      |
| inframe_deletion         | In_Frame_Del           |
| protein_altering_variant | Missense_Mutation      |
| splice_acceptor_variant  | Splice_Site            |
| splice_donor_variant     | Splice_Site            |
| start_lost               | Translation_Start_Site |
| inframe_insertion        | In_Frame_Ins           |
| stop_lost                | Nonstop_Mutation       |

## Expression data
- Retrieved from [biodev](https://biodev.github.io/BeatAML2/). 
  - Filename: beataml_waves1to4_norm_exp_dbgap.txt
- Column `display_label` is `hugo_symbol`
- Raw file is log2 normalized RPKM values
- zscores calculated using  [this script](https://github.com/cBioPortal/datahub-study-curation-tools/tree/master/zscores/zscores_relative_allsamples)
  - option -e used as input was log transformed

# Generic assay data
- Supplementary Table 1 
  - Filename: mmc2.xlsx
- Multiple columns containing blood measurements taken
- For columns `PERC_BLASTS_IN_BM` & `PERC_BLASTS_IN_PB`, replaced non-floating values ('rare', 'occasional', 'N/A ', 
 'predominant', '75 (by flow)') by NA

# Structural variants
- Supplementary Table 1 
  - Filename: mmc2.xlsx
- Column `consensusAMLFusions` taken as fusion column
- Value `KMT2A_re` interpreted as `KMT2A rearranged`

# Case lists
- Case lists generated:
  - Case list all
  - Case list sequenced
  - Case list expression

-----

## Clinical data remapping
| Original Column                           | Renamed column                                  | Patient/Sample      | Comment                                                                                   | 
|-------------------------------------------|-------------------------------------------------|---------------------|-------------------------------------------------------------------------------------------|
| dbgap_subject_id                          | PATIENT_ID                                      | both                |                                                                                           |
| dbgap_dnaseq_sample                       | SAMPLE_ID_DNA                                   | sample              | Combined with SAMPLE_ID_RNA to create SAMPLE ID                                           |
| dbgap_rnaseq_sample                       | SAMPLE_ID_RNA                                   | sample              | Combined with SAMPLE_ID_DNA to create SAMPLE ID                                           |
| cohort                                    | COHORT                                          | sample              |                                                                                           |
| used_manuscript_analyses                  | USED_IN_MANUSCRIPT                              | sample              |                                                                                           |
| manuscript_dnaseq                         | nan                                             | nan                 | Already captured by USED_IN_MANUSCRIPT                                                    |
| manuscript_rnaseq                         | nan                                             | nan                 | Already captured by USED_IN_MANUSCRIPT                                                    |
| manuscript_inhibitor                      | nan                                             | nan                 | Already captured by USED_IN_MANUSCRIPT                                                    |
| consensus_sex                             | SEX                                             | patient             |                                                                                           |
| inferred_sex                              | nan                                             | nan                 | Value can differ per sample (for the same patient), already captured by consesnsus_sex    |
| reportedRace                              | RACE                                            | patient             |                                                                                           |
| reportedEthnicity                         | ETHNICITY                                       | patient             |                                                                                           |
| inferred_ethnicity                        | nan                                             | nan                 | Value can differ per sample (for the same patient), already captured by reportedEthnicity |
| centerID                                  | CENTER_ID                                       | sample              |                                                                                           |
| CEBPA_Biallelic                           | CEBPA_BIALLELIC                                 | sample              |                                                                                           |
| consensusAMLFusions                       | CONSENSUS_AML_FUSIONS                           | structural_variants |                                                                                           |
| ageAtDiagnosis                            | AGE_AT_DIAGNOSIS                                | sample              |                                                                                           |
| isRelapse                                 | IS_RELAPSE                                      | sample              |                                                                                           |
| isDenovo                                  | IS_DENOVO                                       | sample              |                                                                                           |
| isTransformed                             | IS_TRANSFORMED                                  | sample              |                                                                                           |
| specificDxAtAcquisition_MDSMPN            | SPECIFIC_DX_AT_ACQUISITION_MDSMPN               | sample              |                                                                                           |
| nonAML_MDSMPN_specificDxAtAcquisition     | NON_AML_MDSMPN_SPECIFIC_DX_AT_ACQUISITION       | sample              |                                                                                           |
| priorMalignancyNonMyeloid                 | PRIOR_MALIGNANCY_NON_MYELOID                    | patient             |                                                                                           |
| priorMalignancyType                       | PRIOR_MALIGNANCY_TYPE                           | patient             |                                                                                           |
| cumulativeChemo                           | CUMULATIVE_CHEMO                                | patient             |                                                                                           |
| priorMalignancyRadiationTx                | PRIOR_MALIGNANCY_RADIATION_TX                   | patient             |                                                                                           |
| priorMDS                                  | PRIOR_MDS                                       | patient             |                                                                                           |
| priorMDSMoreThanTwoMths                   | PRIOR_MDS_MORE_THAN_TWO_MTHS                    | patient             |                                                                                           |
| priorMDSMPN                               | PRIOR_MDS_MPN                                   | patient             |                                                                                           |
| priorMDSMPNMoreThanTwoMths                | PRIOR_MDS_MPN_MORE_THAN_TWO_MTHS                | patient             |                                                                                           |
| priorMPN                                  | PRIOR_MPN                                       | patient             |                                                                                           |
| priorMPNMoreThanTwoMths                   | PRIOR_MPN_MORE_THAN_TWO_MONTHS                  | patient             |                                                                                           |
| dxAtInclusion                             | DX_AT_INCLUSION                                 | patient             |                                                                                           |
| specificDxAtInclusion                     | SPECIFIC_DX_AT_INCLUSION                        | patient             |                                                                                           |
| ELN2017                                   | ELN2017                                         | sample              |                                                                                           |
| dxAtSpecimenAcquisition                   | CANCER_TYPE                                     | sample              |                                                                                           |
| specificDxAtAcquisition                   | CANCER_TYPE_DETAILED                            | sample              |                                                                                           |
| ageAtSpecimenAcquisition                  | AGE_AT_SPECIMEN_ACQUISITION                     | sample              |                                                                                           |
| timeOfSampleCollectionRelativeToInclusion | TIME_OF_SAMPLE_COLLECTION_RELATIVE_TO_INCLUSION | sample              |                                                                                           |
| specimenGroups                            | SPECIMEN_GROUPS                                 | sample              |                                                                                           |
| diseaseStageAtSpecimenCollection          | DISEASE_STAGE_AT_SPECIMEN_COLLECTION            | sample              |                                                                                           |
| specimenType                              | SPECIMEN_TYPE                                   | sample              |                                                                                           |
| rnaSeq                                    | nan                                             | nan                 | Already captured by case-lists                                                            |
| exomeSeq                                  | nan                                             | nan                 | Already captured by case-lists                                                            |
| totalDrug                                 | nan                                             | nan                 |                                                                                       |
| analysisRnaSeq                            | nan                                             | nan                 | Already captured by USED_IN_MANUSCRIPT                                                    |
| analysisExomeSeq                          | nan                                             | nan                 | Already captured by USED_IN_MANUSCRIPT                                                    |
| analysisDrug                              | nan                                             | nan                 |                                                                                       |
| cumulativeTreatmentTypeCount              | CUMULATIVE_TREATMENT_TYPE_COUNT                 | patient             |                                                                                           |
| cumulativeTreatmentTypes                  | CUMULATIVE_TREATMENT_TYPES                      | patient             |                                                                                           |
| cumulativeTreatmentRegimenCount           | CUMULATIVE_TREATMENT_REGIMEN_COUNT              | sample              |                                                                                           |
| cumulativeTreatmentRegimens               | CUMULATIVE_TREATMENT_REGIMENS                   | sample              |                                                                                           |
| cumulativeTreatmentStageCount             | CUMULATIVE_TREATMENT_STAGE_COUNT                | sample              |                                                                                           |
| cumulativeTreatmentStages                 | CUMULATIVE_TREATMENT_STAGES                     | sample              |                                                                                           |
| responseToInductionTx                     | RESPONSE_TO_INDUCTION_TX                        | sample              |                                                                                           |
| typeInductionTx                           | TYPE_INDUCTION_TX                               | patient             |                                                                                           |
| responseDurationToInductionTx             | RESPONSE_DURATION_TO_INDUCTION_TX               | patient             |                                                                                           |
| mostRecentTreatmentType                   | MOST_RECENT_TREATMENT_TYPE                      | patient             |                                                                                           |
| currentRegimen                            | CURRENT_REGIMEN                                 | sample              |                                                                                           |
| currentStage                              | CURRENT_STAGE                                   | sample              |                                                                                           |
| mostRecentTreatmentDuration               | MOST_RECENT_TREATMENT_DURATION                  | sample              |                                                                                           |
| vitalStatus                               | OS_STATUS                                       | patient             |                                                                                           |
| overallSurvival                           | OS_MONTHS                                       | patient             |                                                                                           |
| causeOfDeath                              | CAUSE_OF_DEATH                                  | patient             |                                                                                           |
| %.Basophils.in.PB                         | PERC_BASOPHILS_IN_PB                            | generic_assay       |                                                                                           |
| %.Blasts.in.BM                            | PERC_BLASTS_IN_BM                               | generic_assay       |                                                                                           |
| %.Blasts.in.PB                            | PERC_BLASTS_IN_PB                               | generic_assay       |                                                                                           |
| %.Eosinophils.in.PB                       | PERC_EOSINOPHILS_IN_PB                          | generic_assay       |                                                                                           |
| %.Immature.Granulocytes.in.PB             | PERC_IMMATURE_GRANULOCYTES_IN_PB                | generic_assay       |                                                                                           |
| %.Lymphocytes.in.PB                       | PERC_LYMPHOCYTES_IN_PB                          | generic_assay       |                                                                                           |
| %.Monocytes.in.PB                         | PERC_MONOCYTES_IN_PB                            | generic_assay       |                                                                                           |
| %.Neutrophils.in.PB                       | PERC_NEUTROPHILS_IN_PB                          | generic_assay       |                                                                                           |
| %.Nucleated.RBCs.in.PB                    | PERC_NUCLEATED_RBCS_IN_PB                       | generic_assay       |                                                                                           |
| ALT                                       | ALT                                             | generic_assay       |                                                                                           |
| AST                                       | AST                                             | generic_assay       |                                                                                           |
| albumin                                   | ALBUMIN                                         | generic_assay       |                                                                                           |
| creatinine                                | CREATININE                                      | generic_assay       |                                                                                           |
| fabBlastMorphology                        | FAB_BLAST_MORPHOLOGY                            | sample              |                                                                                           |
| hematocrit                                | HEMATOCRIT                                      | generic_assay       |                                                                                           |
| hemoglobin                                | HEMOGLOBIN                                      | generic_assay       |                                                                                           |
| karyotype                                 | KARYOTYPE                                       | generic_assay       |                                                                                           |
| LDH                                       | LDH                                             | generic_assay       |                                                                                           |
| MCV                                       | MCV                                             | generic_assay       |                                                                                           |
| otherCytogenetics                         | OTHER_CYTOGENETICS                              | sample              |                                                                                           |
| plateletCount                             | PLATELET_COUNT                                  | generic_assay       |                                                                                           |
| surfaceAntigensImmunohistochemicalStains  | SURFACE_ANTIGENS_IMMUNOHISTOCHEMICAL_STAINS     | sample              |                                                                                           |
| totalProtein                              | TOTAL_PROTEIN                                   | generic_assay       |                                                                                           |
| wbcCount                                  | WBC_COUNT                                       | generic_assay       |                                                                                           |
| FLT3-ITD                                  | FLT3_ITD                                        | sample              |                                                                                           |
| allelic_ratio                             | ALLELIC_RATIO                                   | sample              |                                                                                           |
| NPM1                                      | NPM1                                            | sample              |                                                                                           |
| RUNX1                                     | RUNX1                                           | sample              |                                                                                           |
| ASXL1                                     | ASXL1                                           | sample              |                                                                                           |
| TP53                                      | TP53                                            | sample              |                                                                                           |
| variantSummary                            | VARIANT_SUMMARY                                 | sample              |                                                                                           |
