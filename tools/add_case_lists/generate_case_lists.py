#! /usr/bin/env python

#
# Copyright (c) 2018 Memorial Sloan Kettering Cancer Center.
# This library is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.  The software and
# documentation provided hereunder is on an "as is" basis, and
# Memorial Sloan Kettering Cancer Center
# has no obligations to provide maintenance, support,
# updates, enhancements or modifications.  In no event shall
# Memorial Sloan Kettering Cancer Center
# be liable to any party for direct, indirect, special,
# incidental or consequential damages, including lost profits, arising
# out of the use of this software and its documentation, even if
# Memorial Sloan Kettering Cancer Center
# has been advised of the possibility of such damage.
#
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

# ------------------------------------------------------------------------------
# Script which generates case lists given a cBioPortal study directory containing
# genomic files, a directory to write the case list files to, a cancer study stable id, 
# and a tab delimited case lists configuration file with the following columns:
#   CASE_LIST_FILENAME
#   STAGING_FILENAME
#   META_STABLE_ID - should contain placeholder <CANCER_STUDY> to be replaced with the study id
#   META_CASE_LIST_CATEGORY
#   META_CANCER_STUDY_ID
#   META_CASE_LIST_NAME
#   META_CASE_LIST_DESCRIPTION - may contain placeholder <NUM_CASES> which will be
#     replaced with the number of cases
#
# To get usage:
#   python generate_case_lists.py -h
#
# Authors: Avery Wang and Manda Wilson
# ------------------------------------------------------------------------------
import os
import os.path
import sys
import argparse

CASE_LIST_CONFIG_HEADER_COLUMNS = ["CASE_LIST_FILENAME", "STAGING_FILENAME", "META_STABLE_ID", "META_CASE_LIST_CATEGORY", "META_CANCER_STUDY_ID", "META_CASE_LIST_NAME", "META_CASE_LIST_DESCRIPTION"]
CASE_LIST_UNION_DELIMITER = "|"
CASE_LIST_INTERSECTION_DELIMITER = "&"
MUTATION_STAGING_GENERAL_PREFIX = "data_mutations"
SEQUENCED_SAMPLES_FILENAME = "sequenced_samples.txt"
MUTATION_CASE_LIST_META_HEADER = "sequenced_samples"
MUTATION_CASE_ID_COLUMN_HEADER = "Tumor_Sample_Barcode"
SAMPLE_ID_COLUMN_HEADER = "SAMPLE_ID"
NON_CASE_IDS = frozenset(["MIRNA", "LOCUS", "ID", "GENE SYMBOL", "ENTREZ_GENE_ID", "HUGO_SYMBOL", "LOCUS ID", "CYTOBAND", "COMPOSITE.ELEMENT.REF", "HYBRIDIZATION REF"])
CANCER_STUDY_TAG = "<CANCER_STUDY>"
NUM_CASES_TAG = "<NUM_CASES>"

def generate_case_lists(case_list_config_filename, case_list_dir, study_dir, study_id, overwrite=False, verbose=False):
    header = []
    with open(case_list_config_filename, 'r') as case_list_config_file:
        # get header and validate
        header = case_list_config_file.readline().rstrip('\n').rstrip('\r').split('\t')
        # check full header matches what we expect
        for column in CASE_LIST_CONFIG_HEADER_COLUMNS:
            if column not in header:
                print >> sys.stderr, "ERROR: column '%s' is not in '%s'" % (column, case_list_config_filename)
                sys.exit(2)

        for line in case_list_config_file:
            line = line.rstrip('\n').rstrip('\r')
            config_fields = line.split('\t')
            case_list_filename = config_fields[header.index("CASE_LIST_FILENAME")]
            staging_filename_list = config_fields[header.index("STAGING_FILENAME")]
            case_list_file_full_path = os.path.join(case_list_dir, case_list_filename)
            if os.path.isfile(case_list_file_full_path) and not overwrite:
                if verbose:
                    print "LOG: generate_case_lists(), '%s' exists and overwrite is false, skipping caselist..." % (case_list_filename)
                continue

            # might be single staging file
            staging_filenames = []
            # union (like all cases)
            union_case_list = CASE_LIST_UNION_DELIMITER in staging_filename_list
            # intersection (like complete or cna-seq)
            intersection_case_list = CASE_LIST_INTERSECTION_DELIMITER in staging_filename_list
            delimiter = CASE_LIST_UNION_DELIMITER if union_case_list else CASE_LIST_INTERSECTION_DELIMITER
            staging_filenames = staging_filename_list.split(delimiter)
            if verbose:
                print "LOG: generate_case_lists(), staging filenames: %s" % (",".join(staging_filenames))

            # if this is intersection all staging files must exist
            if intersection_case_list and \
                    not all([os.path.isfile(os.path.join(study_dir, intersection_filename)) for intersection_filename in staging_filenames]):
                continue

            # this is the set we will pass to write_case_list_file
            case_set = set([])
            # this indicates the number of staging files processed -
            # used to verify that an intersection should be written
            num_staging_files_processed = 0
            for staging_filename in staging_filenames:
                if verbose:
                    print "LOG: generate_case_lists(), processing staging file '%s'" % (staging_filename)
                # compute the case set
                case_list = []
                case_list = get_case_list_from_staging_file(study_dir, staging_filename, verbose)

                if len(case_list) == 0:
                    if verbose:
                        print "LOG: generate_case_lists(), no cases in '%s', skipping..." % (staging_filename)
                    continue

                if intersection_case_list:
                    if len(case_set) == 0:
                        # it is empty so initialize it
                        case_set = set(case_list)
                    else:
                        case_set = case_set.intersection(case_list)
                else:
                    # union of files or single file
                    case_set = case_set.union(case_list)

                num_staging_files_processed += 1

            # write case list file (don't make empty case lists)
            if len(case_set) > 0:
                if verbose:
                    print "LOG: generate_case_lists(), calling write_case_list_file()..."

                # do not write out complete cases file unless we've processed all the files required
                if intersection_case_list and num_staging_files_processed != len(staging_filenames):
                    if verbose:
                        print "LOG: generate_case_lists(), number of staging files processed (%d) != number of staging files required (%d) for '%s', skipping call to write_case_list_file()..." % (num_staging_files_processed, len(staging_filenames), case_list_filename)
                else:
                    write_case_list_file(header, config_fields, study_id, case_list_file_full_path, case_set, verbose)
            elif verbose:
                print "LOG: generate_case_lists(), case_set.size() == 0, skipping call to write_case_list_file()..."

def get_case_list_from_staging_file(study_dir, staging_filename, verbose):
    if verbose:
        print "LOG: get_case_list_from_staging_file(), '%s'" % (staging_filename)

    case_set = set([])

    # if we are processing mutations data and a SEQUENCED_SAMPLES_FILENAME exists, use it
    if MUTATION_STAGING_GENERAL_PREFIX in staging_filename:
        sequenced_samples_full_path = os.path.join(study_dir, SEQUENCED_SAMPLES_FILENAME)
        if os.path.isfile(sequenced_samples_full_path):
            if verbose:
                print "LOG: get_case_list_from_staging_file(), '%s' exists, calling get_case_list_from_sequenced_samples_file()" % (SEQUENCED_SAMPLES_FILENAME)
            return get_case_list_from_sequenced_samples_file(sequenced_samples_full_path, verbose)

    staging_file_full_path = os.path.join(study_dir, staging_filename)
    if not os.path.isfile(staging_file_full_path):
        return []

    # staging file
    with open(staging_file_full_path, 'r') as staging_file:
        id_column_index = 0
        process_header = True
        for line in staging_file:
            line = line.rstrip('\n')
            if line.startswith('#'):
                if line.startswith('#' + MUTATION_CASE_LIST_META_HEADER + ':'):
                    # split will split on any whitespace, tabs or any number of consecutive spaces
                    return line[len(MUTATION_CASE_LIST_META_HEADER)+2:].strip().split()
                continue # this is a comment line, skip it
            values = line.split('\t')

            # is this the header line?
            if process_header:
                # look for MAF file case id column header
                # if this is not a MAF file and header contains the case ids, return here
                # we are assuming the header contains the case ids because SAMPLE_ID_COLUMN_HEADER is missing
                if MUTATION_CASE_ID_COLUMN_HEADER not in values and SAMPLE_ID_COLUMN_HEADER not in values:
                    if verbose:
                        print "LOG: get_case_list_from_staging_file(), this is not a MAF header but has no '%s' column, we assume it contains sample ids..." % (SAMPLE_ID_COLUMN_HEADER)
                    for potential_case_id in values:
                        # check to filter out column headers other than sample ids
                        if potential_case_id.upper() in NON_CASE_IDS:
                            continue
                        case_set.add(potential_case_id)
                    break # got case ids from header, don't read the rest of the file
                else:
                    # we know at this point one of these columns exists, so no fear of ValueError from index method
                    id_column_index = values.index(MUTATION_CASE_ID_COLUMN_HEADER) if MUTATION_CASE_ID_COLUMN_HEADER in values else values.index(SAMPLE_ID_COLUMN_HEADER)
                    if verbose:
                        print "LOG: get_case_list_from_staging_file(), this is a MAF or clinical file, samples ids in column with index: %d" % (id_column_index)
                process_header = False
                continue # done with header, move on to next line
            case_set.add(values[id_column_index])

    return list(case_set)

def get_case_list_from_sequenced_samples_file(sequenced_samples_full_path, verbose):
    if verbose:
        print "LOG: get_case_list_from_sequenced_samples_file, '%s'", sequenced_samples_full_path

    case_set = set([])
    with open(sequenced_samples_full_path, 'r') as sequenced_samples_file:
        for line in sequenced_samples_file:
            case_set.add(line.rstrip('\n'))

    if verbose:
        print "LOG: get_case_list_from_sequenced_samples_file, case set size: %d" % (len(case_set))

    return list(case_set)

def write_case_list_file(case_list_config_header, case_list_config_fields, study_id, case_list_full_path, case_set, verbose):
    if verbose:
        print "LOG: write_case_list_file(), '%s'" % (case_list_full_path)
    with open(case_list_full_path, 'w') as case_list_file:
        case_list_file.write("cancer_study_identifier: " + study_id + "\n")
        stable_id = case_list_config_fields[case_list_config_header.index("META_STABLE_ID")].replace(CANCER_STUDY_TAG, study_id)
        case_list_file.write("stable_id: " + stable_id + "\n")
        case_list_file.write("case_list_name: " + case_list_config_fields[case_list_config_header.index("META_CASE_LIST_NAME")] + "\n")
        case_list_description = case_list_config_fields[case_list_config_header.index("META_CASE_LIST_DESCRIPTION")].replace(NUM_CASES_TAG, str(len(case_set)))
        case_list_file.write("case_list_description: " + case_list_description + "\n")
        case_list_file.write("case_list_category: " + case_list_config_fields[case_list_config_header.index("META_CASE_LIST_CATEGORY")] + "\n")
        case_list_file.write("case_list_ids: " + '\t'.join(case_set) + "\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--case-list-config-file', action = 'store', dest = 'case_list_config_file', required = True, help = 'Path to the case list configuration file.  An example can be found in "test/resources/generate_case_lists/case_list_config.tsv"')
    parser.add_argument('-d', '--case-list-dir', action = 'store', dest = 'case_list_dir', required = True, help = 'Path to the directory in which the case list files should be written')
    parser.add_argument('-s', '--study-dir', action = 'store', dest = 'study_dir', required = True, help = 'The directory that contains the cancer study genomic files')
    parser.add_argument('-i', '--study-id', action = 'store', dest = 'study_id', required = True, help = 'The cancer study stable id')
    parser.add_argument('-o', '--overwrite', action = 'store_true', dest = 'overwrite', required = False, help = 'When given, overwrite the case list files')
    parser.add_argument('-v', '--verbose', action = 'store_true', dest = 'verbose', required = False, help = 'When given, be verbose')
    args = parser.parse_args()

    case_list_config_filename = args.case_list_config_file
    case_list_dir = args.case_list_dir
    study_dir = args.study_dir
    study_id = args.study_id
    overwrite = args.overwrite
    verbose = args.verbose

    if verbose:
        print "LOG: case_list_config_file='%s'" % (case_list_config_filename)
        print "LOG: case_list_dir='%s'" % (case_list_dir)
        print "LOG: study_dir='%s'" % (study_dir)
        print "LOG: study_id='%s'" % (study_id)
        print "LOG: overwrite='%s'" % (overwrite)
        print "LOG: verbose='%s'" % (verbose)

    if not os.path.isfile(case_list_config_filename):
        print >> sys.stderr, "ERROR: case list configuration file '%s' does not exist or is not a file" % (case_list_config_filename)
        parser.print_help()
        sys.exit(2)

    if not os.path.isdir(case_list_dir):
        print >> sys.stderr, "ERROR: case list file directory '%s' does not exist or is not a directory" % (case_list_dir)
        parser.print_help()
        sys.exit(2)

    if not os.path.isdir(study_dir):
        print >> sys.stderr, "ERROR: study directory '%s' does not exist or is not a directory" % (study_dir)
        parser.print_help()
        sys.exit(2)

    generate_case_lists(case_list_config_filename, case_list_dir, study_dir, study_id, overwrite, verbose)

if __name__ == '__main__':
    main()
