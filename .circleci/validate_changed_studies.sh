#!/usr/bin/env bash
# This script detects the studies that were changed and triggers the validation accordingly

set -o pipefail

STUDIES_DIRS=("public/" "crdc/gdc/")
REPO_DIR="$HOME/repo"
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
    # if file is part of studies_dir, store its directory path (except case_lists)
    for STUDIES_DIR in "${STUDIES_DIRS[@]}"; do
      if [[ $file_changing = *$STUDIES_DIR* ]] && [[ $file_changing != *".htm"* ]]; then
        echo "study file changing > [$file_changing]"
        dir_name=$(dirname "$file_changing")
        # match case_list*, caselist* as a case list dir (actually only case_lists is valid,
        # but this is up to validation script to flag):
        if [[ $dir_name != *"/case_list"* ]] && [[ $dir_name != *"/caselist"* ]] && [[ $dir_name != *"/archived_files"* ]] && [[ $dir_name != *"/gene_sets"* ]] && [[ $dir_name != *"/normals"* ]] && [[ $dir_name != *"/validation_reports"* ]]; then
          echo "study dir > [$dir_name]"
        else
          # get parent dir:
          dir_name=$(dirname "$dir_name")
          echo "study dir > [$dir_name]"
        fi
        if [[ ! " ${list_of_study_dirs[@]} " =~ " $dir_name " ]]; then
          echo "adding to list..."
          list_of_study_dirs+=("$dir_name")
          echo "downloading files from git lfs..."
          git -c lfs.fetchexclude="" lfs pull -I "$dir_name/*"
          git -c lfs.fetchexclude="" lfs pull -I "$dir_name/case_lists/*"
        fi
      fi
    done
done

num_studies=${#list_of_study_dirs[@]}
if [[ $num_studies -gt 0 ]]; then
  echo $'\n====List of studies:====\n'
  echo "${list_of_study_dirs[@]}"

  mkdir -p "$ERRORS_DIR"
  pids=()
  log_files=()

  for study in "${list_of_study_dirs[@]}"; do
    log_file="$LOG_DIR/$(basename "$study").log"
    log_files+=("$log_file")
    echo "Starting validation for: $study"
    python "$VALIDATION_SCRIPT" \
      -d "$REPO_DIR" \
      -l "$study" \
      -p "$REPO_DIR/.circleci/portalinfo" \
      -html "$TEST_REPORTS_LOCATION/$study" \
      > "$log_file" 2>&1 &
    pids+=($!)

    # Throttle to MAX_THREADS parallel jobs
    while [[ ${#pids[@]} -ge $MAX_THREADS ]]; do
      for i in "${!pids[@]}"; do
        if ! kill -0 "${pids[$i]}" 2>/dev/null; then
          unset "pids[$i]"
        fi
      done
      pids=("${pids[@]}")
      sleep 1
    done
  done

  # Wait for all remaining background jobs to finish
  for pid in "${pids[@]}"; do
    wait "$pid" || true
  done

  # Print all logs cleanly after all jobs finish
  echo $'\n====Validation Results:====\n'
  for i in "${!log_files[@]}"; do
    log="${log_files[$i]}"
    study="${list_of_study_dirs[$i]}"
    if [[ -f "$log" ]]; then
      echo "============================================================"
      echo " Study: $study"
      echo "============================================================"
      cat "$log"
      echo ""
    fi
  done

  # Remove the log directory
  if [[ -d "$LOG_DIR" ]]; then
    rm -rf "$LOG_DIR"
  fi

  # Find all studies with errors
  erred_studies=$(grep -rl -e 'Failed' "$TEST_REPORTS_LOCATION" || true)
  if [[ -n "$erred_studies" ]]; then
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
