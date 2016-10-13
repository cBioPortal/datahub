Files to seed a new cBioPortal database.

Release notes:
----

20 September 2016
Created by Sander Tan and Pieter Lukasse, The Hyve (thehyve.nl)

These files contain the updated seed database for cBioPortal. We included:
1. Updated genes (60072) and gene aliases
2. Updated gene lengths
3. Updated pfam graphics

Compared to the previous seed database, the following number of values are removed because their associated Entrez Gene IDs do not exist anymore in the NCBI Gene info:
- cosmic_mutation: 247
- uniprot_id_mapping: 1375
- interaction: 56
- drug_interaction: 6

These tables were dropped, since they were not found in cgds.sql:
- micro_rna
- micro_rna_alteration
- mutation_frequency
- patient_list
- patient_list_list
