#!/usr/bin/env bash
# This script detects the studies that were changed and triggers the validation accordingly

STUDIES_DIRS=("public/" "crdc/gdc/")
REPO_DIR="$HOME/repo/"
TEST_REPORTS_LOCATION="$HOME/test-reports"
ERRORS_DIR="$TEST_REPORTS_LOCATION/ERRORS"
LOG_DIR="$TEST_REPORTS_LOCATION/logs"
VALIDATION_SCRIPT="$HOME/cbioportal-core/scripts/importer/validateStudies.py"
GIT_REMOTE_URL="git@github.com:cbioportal/datahub.git"
MAX_THREADS=7

git remote add upstream "$GIT_REMOTE_URL"
git fetch upstream master

mkdir -p "$LOG_DIR"

files_changing=$(git diff --name-only --diff-filter=ACMRU upstream/master)
list_of_study_dirs=()

for file_changing in $files_changing; do
    echo "study file changing > [$file_changing]"
    # if file is part of studies_dir, store its directory path (except case_lists)
    for STUDIES_DIR in "${STUDIES_DIRS[@]}"; do
      if [[ $file_changing = *$STUDIES_DIR* ]] && [[ $file_changing != *".htm"* ]]; then
        echo "study file changing > [$file_changing]"
        dir_name=$(dirname $file_changing)
        # match case_list*, caselist* as a case list dir (actually only case_lists is valid, 
        # but this is up to validation script to flag):
        if [[ $dir_name != *"/case_list"* ]] && [[ $dir_name != *"/caselist"* ]] && [[ $dir_name != *"/archived_files"* ]] && [[ $dir_name != *"/gene_sets"* ]] && [[ $dir_name != *"/normals"* ]] && [[ $dir_name != *"/validation_reports"* ]]; then
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
      log_file="$LOG_DIR/$(basename $study).log"
      # if [ $mod = 0 ] ; then
      #   validation_command="${validation_command} && sleep $((num*2))"
      # fi
      # append the first study
      if [[ -z "$validation_command" ]] ; then
        validation_command="($VALIDATION_SCRIPT -d $REPO_DIR -l $study -p $REPO_DIR/.circleci/portalinfo -html $TEST_REPORTS_LOCATION/$study  > $log_file 2>&1"
      else
        # run each validation individually in the background
        if [ $mod = 0 ] ; then
          validation_command="${validation_command}) & ($VALIDATION_SCRIPT -d $REPO_DIR -l $study -p $REPO_DIR/.circleci/portalinfo -html $TEST_REPORTS_LOCATION/$study > $log_file 2>&1"
        else
          validation_command="${validation_command} ; $VALIDATION_SCRIPT -d $REPO_DIR -l $study -p $REPO_DIR/.circleci/portalinfo -html $TEST_REPORTS_LOCATION/$study > $log_file 2>&1"
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
      echo -e "waiting for all processes to finish...\n\n"
      # exit only when all processes finished
      if (( code = 127 )); then
        break
      fi
    }
  done
  
  for log in "$LOG_DIR"/*.log; do
    if [[ -f "$log" ]]; then
      cat "$log"
      echo -e "\n----------------------------------------------------\n"
    fi
  done
  
  # find all studies with error
  erred_studies=$(pcregrep -rMl 'Validation status:\n\s*<strong>\s*Failed' "$TEST_REPORTS_LOCATION")
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