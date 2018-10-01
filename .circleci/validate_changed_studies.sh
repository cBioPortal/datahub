#!/usr/bin/env bash
# This script detects the studies that were changed and triggers the validation accordingly

STUDIES_DIR="public/"

git remote add upstream git@github.com:cbioportal/datahub.git
git fetch upstream master

files_changing=`git diff --name-only --diff-filter=ACMRU upstream/master`
list_of_study_dirs=()

for file_changing in $files_changing
do
    #echo "file > [$file_changing]"
    # if file is part of studies_dir, store its directory path (except case_lists)
    if [[ $file_changing = *$STUDIES_DIR* ]] && [[ $file_changing != *".htm"* ]]; then
      echo "study file changing > [$file_changing]"
      dir_name=`dirname $file_changing`
      # match case_list*, caselist* as a case list dir (actually only case_lists is valid, 
      # but this is up to validation script to flag):
      if [[ $dir_name != *"/case_list"* ]] && [[ $dir_name != *"/caselist"* ]] && [[ $dir_name != *"/archived_files"* ]]; then
        echo "study dir > [$dir_name]"
      else
        # get parent dir:
        dir_name=`dirname $dir_name`
        echo "study dir > [$dir_name]"
      fi
      found_in_list=`echo ${list_of_study_dirs[@]} | grep $dir_name`
      if [[ $found_in_list = "" ]]; then
        echo "adding to list..."
        list_of_study_dirs+=($dir_name)
        echo "downloading files from git lfs..."
        git lfs pull -I "$dir_name/*"
        git lfs pull -I "$dir_name/case_lists/*"
      fi
    fi
done
num_studies=${#list_of_study_dirs[@]}
if [[ $num_studies > 0 ]]; then
  echo $'\n====List of studies:====\n'
  list_csv=`echo ${list_of_study_dirs[@]} | tr ' ' ','`
  echo $list_csv

  test_reports_location="$HOME/test-reports"
  validation_command="$HOME/cbioportal/core/src/main/scripts/importer/./validateStudies.py -d $HOME/repo/ -l $list_csv -p $HOME/repo/.circleci/portalinfo -html $test_reports_location"
  echo $'\nExecuting: '; echo $validation_command
  if sh -c "$validation_command" ; then
    echo "Tests passed successfully"
    exit 0
  else
    echo "Errors found"
    # move errors to ERRORS/ folder:
    erred_studies=`grep -rnlz $test_reports_location -e 'Validation status.*Failed' `
    mv $erred_studies $test_reports_location/ERRORS
    exit 1
  fi
else
  echo "No studies were changed"
fi
