#!/usr/bin/env bash
# This script detects the studies that were changed and triggers the validation accordingly

STUDIES_DIR="public/"
REPO_DIR="$HOME/repo/"
TEST_REPORTS_LOCATION="$HOME/test-reports"
ERRORS_DIR="$TEST_REPORTS_LOCATION/ERRORS"
VALIDATION_SCRIPT="$HOME/cbioportal-core/scripts/importer/validateStudies.py"
GIT_REMOTE_URL="git@github.com:cbioportal/datahub.git"
MAX_THREADS=7

git remote add upstream "$GIT_REMOTE_URL"
git fetch upstream master

files_changing=$(git diff --name-only --diff-filter=ACMRU upstream/master)
list_of_study_dirs=()

for file_changing in $files_changing; do
    # if file is part of studies_dir, store its directory path (except case_lists)
    if [[ $file_changing = *$STUDIES_DIR* ]] && [[ $file_changing != *".htm"* ]]; then
      echo "study file changing > [$file_changing]"
      dir_name=$(dirname $file_changing)
      # match case_list*, caselist* as a case list dir (actually only case_lists is valid, 
      # but this is up to validation script to flag):
      if [[ $dir_name != *"/case_list"* ]] && [[ $dir_name != *"/caselist"* ]] && [[ $dir_name != *"/archived_files"* ]] && [[ $dir_name != *"/gene_sets"* ]] && [[ $dir_name != *"/normals"* ]]; then
        echo "study dir > [$dir_name]"
      else
        # get parent dir:
        dir_name=`dirname $dir_name`
        echo "study dir > [$dir_name]"
      fi
      if [[ ! " ${list_of_study_dirs[@]} " =~ " $dir_name " ]]; then
        echo "adding to list..."
        list_of_study_dirs+=("$dir_name")
        echo "downloading files from git lfs..."
        git lfs pull -I "$dir_name/*"
        git lfs pull -I "$dir_name/case_lists/*"
      fi
    fi
done
num_studies=${#list_of_study_dirs[@]}
if [[ $num_studies > 0 ]]; then
  echo $'\n====List of studies:====\n'
  list_csv=$(printf "%s," "${list_of_study_dirs[@]}" | sed 's/,$//')
  echo "$list_csv"

  mkdir -p "$ERRORS_DIR"
  validation_command=""
  num=0
  break_num=$((num_studies / MAX_THREADS + 1))
  for study in ${list_csv//,/ }
  do
      # append sleep command between commands
      ((num=num+1))
      mod=$(($num % $break_num))
      # if [ $mod = 0 ] ; then
      #   validation_command="${validation_command} && sleep $((num*2))"
      # fi
      # append the first study
      if [[ -z "$validation_command" ]] ; then
        validation_command="($VALIDATION_SCRIPT -d $REPO_DIR -l $study -p $REPO_DIR/.circleci/portalinfo -html $TEST_REPORTS_LOCATION/$study"
      else
        # run each validation individually in the background
        if [ $mod = 0 ] ; then
          validation_command="${validation_command}) & ($VALIDATION_SCRIPT -d $REPO_DIR -l $study -p $REPO_DIR/.circleci/portalinfo -html $TEST_REPORTS_LOCATION/$study"
        else
          validation_command="${validation_command} ; $VALIDATION_SCRIPT -d $REPO_DIR -l $study -p $REPO_DIR/.circleci/portalinfo -html $TEST_REPORTS_LOCATION/$study"
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
      echo "waiting for all processes to finish..."
      # exit only when all processes finished
      if (( code = 127 )); then
        break
      fi
    }
  done
  
  # Check if there are any files in $test_reports_location
  if [ -z "$(ls -A $TEST_REPORTS_LOCATION)" ]; then
    echo "No files found in $TEST_REPORTS_LOCATION. An error has occurred running the validator."
    exit 1
  fi

  # find all studies with error
  erred_studies=$(grep -rl "$TEST_REPORTS_LOCATION" -e 'Validation status.*Failed')
  if [[ $? -eq 0 ]] && [[ -n "$erred_studies" ]]; then
    echo $'\n====List of error studies:====\n'
    echo "$erred_studies"
    echo "$erred_studies" | xargs -I {} mv {} "$ERRORS_DIR"
    exit 1
  else
    echo "No error studies found."
  fi
else
  echo "No studies were changed"
fi