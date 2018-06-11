### Usage
Generate case lists for existing study.

### Command Line
```
generate_case_lists.py [-h] -c CASE_LIST_CONFIG_FILE -d CASE_LIST_DIR -s STUDY_DIR -i STUDY_ID [-o] [-v]
```

### Example
```
cd path/to/brca_tcga
rm -rf case_lists #remove current case lists folder (if existed)
mkdir case_lists
python path/to/generate_case_lists.py -c path/to/case_list_conf.txt -s case_lists -s . -i brca_tcga
```

### Notes
`case_list_conf.txt` and `clinicalfile_utils.py` are needed under the sample path. 
`case_list_conf.txt` should be synced with the corresponding google config sheet.
