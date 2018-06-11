### Usage
Add meta data for clinical attributes as header lines to data clinical files. 

### Command Line
insert_clinical_metadata.py -d DIRECTORY, --directory=DIRECTORY

### Example
```
cd path/to/brca_tcga
python insert_clinical_metadata.py -d .
rm data_clinical_patient.txt
rm data_clinical_sample.txt
mv data_clinical_patient.txt.metadata data_clinical_patient.txt
mv data_clinical_sample.txt.metadata data_clinical_sample.txt
```

### Notes
`data_clinical_patient.txt` and `data_clinical_sample.txt` need to be presented under the existing study.
`clinical_attributes_metadata.txt` needed under the same path. 
`clinical_attributes_metadata.txt` shall be synced with corresponding clinical data dictionary in `topbraid`