#!/usr/bin/env bash
# This script runs validation on all public studies.

set -o pipefail

STUDIES_DIRS=("public" "crdc/gdc")
REPO_DIR="$HOME/repo"
TEST_REPORTS_LOCATION="$HOME/test-reports"
ERRORS_DIR="$TEST_REPORTS_LOCATION/ERRORS"
LOG_DIR="$TEST_REPORTS_LOCATION/logs"
VALIDATION_SCRIPT="$HOME/cbioportal-core/scripts/importer/validateStudies.py"
GIT_REMOTE_URL="git@github.com:cbioportal/datahub.git"
MAX_THREADS=7
EXIT_STATUS=0

git remote add upstream "$GIT_REMOTE_URL"
git fetch upstream master

mkdir -p "$LOG_DIR"
mkdir -p "$ERRORS_DIR"

# Collect all study directories
list_of_study_dirs=()
for STUDIES_DIR in "${STUDIES_DIRS[@]}"; do
  for study in "$REPO_DIR/$STUDIES_DIR"/*/; do
    if [[ -d "$study" ]]; then
      list_of_study_dirs+=("$study")
    fi
  done
done

num_studies=${#list_of_study_dirs[@]}
echo $'\n====List of studies:====\n'
echo "${list_of_study_dirs[@]}"
echo ""

pids=()
log_files=()

for study in "${list_of_study_dirs[@]}"; do
  log_file="$LOG_DIR/$(basename "$study").log"
  log_files+=("$log_file")
  echo "Pulling LFS data for: $study"
  git -c lfs.fetchexclude="" lfs pull -I "$study*"
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
  EXIT_STATUS=1
else
  echo "No error studies found."
fi

exit "$EXIT_STATUS"
