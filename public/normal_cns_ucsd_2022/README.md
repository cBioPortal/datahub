# **Information on the Curation of this Study**

## General
* Study: [https://aacrjournals.org/cancerres/article/82/8/1492/694359/Colorectal-Cancer-Is-Associated-with-the-Presence](https://aacrjournals.org/cancerres/article/82/8/1492/694359/Colorectal-Cancer-Is-Associated-with-the-Presence)
* Reference genome used: GRCh37
* uploaded data available from original publication

## Clinical Data
* Patient data was retrieved from the paper's method section

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |-			 |PATIENT_ID           |
  |-                     |SEX                  |
  |-                     |AGE                  |
  |-		         |CAUSE_OF_DEATH       |
 
* Sample data was retrieved from Supplementary Data 1 - "Raw mosaic SNV/INDEL calls from the 300× WGS. Raw mosaic SNV/INDEL calls from the 300× WGS. The information includes the genomic position, reference and alternative alleles, as well as caller agreement on the specific variant. The candidate variant list subjected to MPAS and snMPAS panel design and the considered regions are included as separate sheets. Quality control metrics of WGS are also included."
* remapped clinical sample data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |ID	                 |SAMPLE_ID            |
  |ID/TISSUE_DETECTED    |SAMPLE_SITE	       |
  |-	                 |PATIENT_ID           |

## Mutation Data
* Mutation data was retrieved from Supplementary Data 1 - "Raw mosaic SNV/INDEL calls from the 300× WGS. Raw mosaic SNV/INDEL calls from the 300× WGS. The information includes the genomic position, reference and alternative alleles, as well as caller agreement on the specific variant. The candidate variant list subjected to MPAS and snMPAS panel design and the considered regions are included as separate sheets. Quality control metrics of WGS are also included."
* Sample data was only available for bulk sequenced cns tissues. single-cell derived colonies were excluded due to missing sample data.
* Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
* Case list all