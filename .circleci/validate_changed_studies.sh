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
      if [[ $dir_name != *"/case_list"* ]] && [[ $dir_name != *"/caselist"* ]] && [[ $dir_name != *"/archived_files"* ]] && [[ $dir_name != *"/gene_sets"* ]] && [[ $dir_name != *"/normals"* ]]; then
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
  validation_command=""
  num=0
  max_threads=7
  break_num=$(($num_studies / $max_threads + 1))
  for study in ${list_csv//,/ }
  do
      # append sleep command between commands
      ((num=num+1))
      mod=$(($num % $break_num))
      # if [ $mod = 0 ] ; then
      #   validation_command="${validation_command} && sleep $((num*2))"
      # fi
      # append the first study
      if [ "$validation_command" = "" ] ; then
        validation_command="($HOME/cbioportal-core/src/main/resources/scripts/importer/./validateStudies.py -d $HOME/repo/ -l $study -p $HOME/repo/.circleci/portalinfo -html $test_reports_location/$study"
      else
        # run each validation individually in the background
        if [ $mod = 0 ] ; then
          validation_command="${validation_command}) & ($HOME/cbioportal-core/src/main/resources/scripts/importer/./validateStudies.py -d $HOME/repo/ -l $study -p $HOME/repo/.circleci/portalinfo -html $test_reports_location/$study"
        else
          validation_command="${validation_command} ; $HOME/cbioportal-core/src/main/resources/scripts/importer/./validateStudies.py -d $HOME/repo/ -l $study -p $HOME/repo/.circleci/portalinfo -html $test_reports_location/$study"
        fi
      fi
  done
  validation_command="${validation_command})"
  echo $'\nExecuting: '; echo $validation_command
  eval "$validation_command"
  # Waiting for all background processes to finish
  while true; do
    wait -n || {
      code="$?"
      echo "waiting for all processes to finish ...................."
      # exit only when all processes finished
      if ([[ $code = "127" ]] && exit 0) ; then
        break
      fi
    }
  done;

  # find all studies with error
  erred_studies=`grep -rnlz $test_reports_location -e 'Validation status.*Failed' `
  if [[ $? -eq 0 ]]; then
    echo $'\n====List of error studies:====\n'
    echo $erred_studies
    mv $erred_studies $test_reports_location/ERRORS
    exit 1
  else
    echo "All tests passed successfully"
    exit 0
  fi
else
  echo "No studies were changed"
fi
