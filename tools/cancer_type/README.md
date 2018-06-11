### Usage
Add additional columns `CANCER_TYPE` and `CANCER_TYPE_DETAILS` according to values `ONCOTREE_CODE` column into data clinical files.

### Command Line
```
oncotree_code_converter.py [-h] -o ONCOTREE_URL -c CLINICAL_FILE
```

### Example
```
python oncotree_code_converter.py --oncotree-url "http://oncotree.mskcc.org/oncotree/api/tumor_types.txt?oncotree_version=oncotree_development_release" --clinical-file data_clinical_samples.txt
```

### Notes
`clinicalfile_utils.py` and `clinicalfile_utils.pyc` are needed under the sample path. 
