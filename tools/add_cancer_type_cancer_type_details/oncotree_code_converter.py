import os
import sys
import fileinput
import argparse
import urllib2
import re
from clinicalfile_utils import *
# globals

PATTERN = re.compile('([A-Za-z\' ,-/]*) \\(([A-Za-z_]*)\\)')
SPREADSHEET_FIELDS = ['quinternary', 'quaternary', 'tertiary', 'secondary', 'primary']
MAIN_TYPE_FIELD = 'metamaintype'

CANCER_TYPE = 'CANCER_TYPE'
CANCER_TYPE_DETAILED = 'CANCER_TYPE_DETAILED'
ONCOTREE_CODE = 'ONCOTREE_CODE'
SAMPLE_ID = 'SAMPLE_ID'
NA = 'NA'

no_matches = []

# functions

def get_oncotree(oncotree_url):
    """ Gets the oncotree data from the specified url """

    return urllib2.urlopen(oncotree_url).read().split('\n')

def get_cancer_types(oncotree, code):
    """
    Maps a code to an entry on the oncotree
    It returns a dictionary containing the cancer type and cancer type cancer_type_detailed
    based on the oncotree.

    """

    first = True
    header = []
    cancer_type = NA
    cancer_type_detailed = NA
    for line in oncotree:
        if first:
            header = line.split('\t')
            first = False
            continue
        for field in SPREADSHEET_FIELDS:
            data = line.split('\t')
            # If there is an index error, we didn't get a match. Move along..
            try:
                match = PATTERN.match(data[header.index(field)])
            except IndexError:
                continue
            if match:
                if match.group(2) == code:
                    cancer_type_detailed = match.group(1)
                    # This is in case the main cancer type field doesn't exist - problem with oncotree
                    try:
                        cancer_type = data[header.index(MAIN_TYPE_FIELD)]
                    except IndexError:
                        cancer_type = NA
                    # Found it, return to not keep processing more lines.
                    return {CANCER_TYPE: cancer_type, CANCER_TYPE_DETAILED: cancer_type_detailed}
    # Nothing was found, return NAs
    return {CANCER_TYPE: cancer_type, CANCER_TYPE_DETAILED: cancer_type_detailed}

def process_clinical_file(oncotree, clinical_filename):
    """ Insert cancer type/cancer type detailed in the clinical file """

    first = True
    metadata_headers_processed = False
    header = []
    file_has_metadata_headers = has_metadata_headers(clinical_filename)

    # same logic checking for Cancer Type/ Cancer Type Detailed but applied to metadata headers
    if file_has_metadata_headers:
        metadata_lines = get_all_metadata_lines(clinical_filename)
        if CANCER_TYPE not in get_header(clinical_filename):
            add_metadata_for_attribute(CANCER_TYPE, metadata_lines)
        if CANCER_TYPE_DETAILED not in get_header(clinical_filename):
            add_metadata_for_attribute(CANCER_TYPE_DETAILED, metadata_lines)

    # Python docs: "if the keyword argument inplace=1 is passed to fileinput.input()
    # or to the FileInput constructor, the file is moved to a backup
    # file and standard output is directed to the input file"
    f = fileinput.input(clinical_filename, inplace = 1)
    try:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith('#'):
                if file_has_metadata_headers and not metadata_headers_processed:
                    metadata_headers_processed = True
                    write_metadata_headers(metadata_lines, clinical_filename)
                continue
            if first:
                first = False
                header = line.split('\t')
                if CANCER_TYPE not in header:
                    header.append(CANCER_TYPE)
                if CANCER_TYPE_DETAILED not in header:
                    header.append(CANCER_TYPE_DETAILED)
                print '\t'.join(header)
                continue
            data = line.split('\t')
            oncotree_code = data[header.index(ONCOTREE_CODE)]
            cancer_types = get_cancer_types(oncotree, oncotree_code)
            if cancer_types[CANCER_TYPE_DETAILED] == NA:
                no_matches.append(data[header.index(SAMPLE_ID)])
            # Handle the case if CANCER_TYPE or CANCER_TYPE_DETAILED has to be appended to the header.
            # Separate try-except in case one of the fields exists and the other doesn't
            try:
                data[header.index(CANCER_TYPE)] = cancer_types[CANCER_TYPE]
            except IndexError:
                data.append(cancer_types[CANCER_TYPE])
            try:
                data[header.index(CANCER_TYPE_DETAILED)] = cancer_types[CANCER_TYPE_DETAILED]
            except IndexError:
                data.append(cancer_types[CANCER_TYPE_DETAILED])
            print '\t'.join(data)
    finally:
        f.close()

def report_failed_matches():
    """ Reports any samples from the file that could not match its oncotree code """

    if len(no_matches) > 0:
        print 'Could not find a match for the following samples:'
        for sample_id in no_matches:
            print sample_id

def main():
    """
    Parses a clinical file with a ONCOTREE_CODE column and add/update the CANCER_TYPE and CANCER_TYPE_DETAILED columns inplace
    with values from an oncotree instance.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--oncotree-url', action = 'store', dest = 'oncotree_url', required = True, help = 'The url of the raw oncotree text file')
    parser.add_argument('-c', '--clinical-file', action = 'store', dest = 'clinical_file', required = True, help = 'Path to the clinical file')

    args = parser.parse_args()

    oncotree_url = args.oncotree_url
    clinical_filename = args.clinical_file

    if not os.path.exists(clinical_filename):
        print 'clinical file cannot be found ' + clinical_filename
        sys.exit(2)

    oncotree = get_oncotree(oncotree_url)
    process_clinical_file(oncotree, clinical_filename)
    report_failed_matches()

if __name__ == '__main__':
    main()
