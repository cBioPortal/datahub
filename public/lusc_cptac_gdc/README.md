# Comments & assumptions made during curation

## General

- Study is updated once every 3 months with latest data from [ISB-CGC BigQuery tables](https://isb-cgc.appspot.com/bq_meta_search/)
  - The ISB-CGC tables allow easy access to data collected from multiple NCI-CRDC repositories including the GDC, PDC, and others. The CPTAC data in this study comes from the GDC and is accessed through these tables.
- Reference genome used: hg38

- Only tumor sample data is included (no normal samples)

## Clinical data

- Patient data: Retrieved from BigQuery table `isb-cgc-bq.CPTAC.clinical_gdc_current`
- Sample data: Retrieved from BigQuery table `isb-cgc-bq.CPTAC.biospecimen_gdc_current`

- Transformations
  - `AGE` is clipped from 18 to 89.
  - `OS_MONTHS` is converted from `demo__days_to_death` when that value if present. If the patient is still alive, it is converted from `follow__days_to_follow_up`.
  
  - `DFS_MONTHS` is converted from `diag__days_to_recurrence` when that value is present. If there was no recurrence event, it falls back to the value of `OS_MONTHS`.
  
- Remapped columns: **TODO**

## CNA data

- Retrieved from BigQuery table `isb-cgc-bq.CPTAC.copy_number_gene_level_hg38_gdc_current`
- Transformations
  - See [Genomic data transformations](#genomic-data-transformations)
  - Copy number values from the BigQuery tables are converted from [ASCAT](https://www.pnas.org/doi/10.1073/pnas.1009843107https://www.pnas.org/doi/10.1073/pnas.1009843107) to GISTIC 2.0 using the following thresholds:

| ASCAT Value | GISTIC Value |
|---|---|
| X = 0 | -2 |
| X = 1 | -1 |
| X = 2 | 0 |
| 2 &lt; X &le; 8 | 1 |
| 8 &lt; X | 2 |

## Expression data

- Retrieved from BigQuery table `isb-cgc-bq.CPTAC.RNAseq_hg38_gdc_current`
- The `unstranded` and `fpkm_uq_unstranded` columns are pulled and each mapped to their own data file.
  - The regular FPKM values are excluded because [FPKM-UQ provides a more stable metric](https://docs.gdc.cancer.gov/Data/Bioinformatics_Pipelines/Expression_mRNA_Pipeline/#upper-quartile-fpkm).
- Transformations: see [Genomic data transformations](#genomic-data-transformations)

## Segment data

- Retrieved from BigQuery table `isb-cgc-bq.CPTAC.copy_number_segment_masked_hg38_gdc_current`
- Remapped columns:

| Original | cBioPortal |
|---|---|
| sample_barcode | ID |
| chromosome | chrom |
| start_pos | loc.start |
| end_pos | loc.end |
| num_probes | num.mark |
| segment_mean | seg.mean |

## Mutation data

- Retrieved from BigQuery table `isb-cgc-bq.CPTAC.masked_somatic_mutation_hg38_gdc_current`
- Remapped columns:

| Original | cBioPortal |
|---|---|
| sample_barcode_tumor | Tumor_Sample_Barcode |
| sample_barcode_normal | Matched_Norm_Sample_Barcode |

## Genomic data transformations

These rules are applied to multiple genomic data modalities:

- Ensembl gene IDs are mapped to Entrez IDs using the [Genome Nexus hg38 canonical transcript file](https://github.com/genome-nexus/genome-nexus-importer/blob/master/data/grch38_ensembl95/export/ensembl_biomart_canonical_transcripts_per_hgnc.txt). Any genes that cannot be converted using this file are dropped.
  - Prior to conversion, we also filter out a small number of duplicate Ensembl genes. These genes have copies containing data for both the X and the Y chromosomes.
- If a sample has multiple aliquots, it is "reduced" to a single aliquot chosen to represent the entire sample.
  - This is done by choosing the aliquot ID with the highest lexicographical sort value (eg. highest plate number). This follows [the same policy](https://broadinstitute.atlassian.net/wiki/spaces/GDAC/pages/844334036/FAQ#FAQ-replicateFilteringQ%3AWhatdoyoudowhenmultiplealiquotbarcodesexistforagivensample%2Fportion%2Fanalytecombination%3F) used by GDAC used to reduce aliquot data in their studies.