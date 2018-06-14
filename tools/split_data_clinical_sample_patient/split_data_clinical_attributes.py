import os
import sys
import csv
import optparse

# some file descriptors
ERROR_FILE = sys.stderr
OUTPUT_FILE = sys.stdout

CLINICAL_ATTRIBUTE_METADATA_FILENAME = '/Users/suny1/scripts/curation/separate/clinical_attributes_metadata.txt'
CLINICAL_ATTRIBUTE_METADATA = {}
PATIENT_CLINICAL_ATTRIBUTES = {}

CLINICAL_PATIENT_FILENAME = 'data_clinical_patient.txt'
CLINICAL_SAMPLE_FILENAME = 'data_clinical_sample.txt'

def get_header(filename):
	""" Returns the file header. """
	filedata = [x for x in open(filename).read().split('\n') if not x.startswith('#')]
	header = map(str.strip, filedata[0].split('\t'))
	return header


def load_clinical_attribute_metadata():
	""" Loads clinical attribute metadata. """
	metadata_header = get_header(CLINICAL_ATTRIBUTE_METADATA_FILENAME)
	
	# read file and load clinical attribute metadata
	metadata_file = open(CLINICAL_ATTRIBUTE_METADATA_FILENAME, 'rU')
	metadata_reader = csv.DictReader(metadata_file, dialect='excel-tab')
	for line in metadata_reader:
		column = line['NORMALIZED_COLUMN_HEADER']
		attribute_type = line['ATTRIBUTE_TYPE']
		display_name = line['DISPLAY_NAME']
		description = line['DESCRIPTIONS']
		priority = line['PRIORITY']
		datatype = line['DATATYPE']

		if attribute_type == 'PATIENT':
			PATIENT_CLINICAL_ATTRIBUTES[column] = True
		else:
			PATIENT_CLINICAL_ATTRIBUTES[column] = False

		CLINICAL_ATTRIBUTE_METADATA[column] = {'DISPLAY_NAME':display_name, 'DESCRIPTION':description, 'PRIORITY':priority, 'DATATYPE':datatype}


def get_clinical_header(clinical_filename, is_patient_file):
	""" Returns the new file header by clinical file type. """
	new_header = ['PATIENT_ID']
	# sample clinical header needs SAMPLE_ID
	if not is_patient_file:
		new_header.append('SAMPLE_ID')

	# get the file header and filter by attribute type
	clinical_file_header = get_header(clinical_filename)
	attribute_type_header = [hdr for hdr in clinical_file_header if PATIENT_CLINICAL_ATTRIBUTES[hdr] == is_patient_file]
	filtered_header = [hdr for hdr in attribute_type_header if not hdr in new_header]

	new_header.extend(filtered_header)

	return new_header


def get_clinical_header_metadata(header):
	""" 
		Returns the clinical header metadata. 
		The order of the clinical header metadata goes:
			1. display name 
			2. descriptions
			3. datatype (STRING, NUMBER, BOOLEAN)
			4. priority
	"""

	display_names = []
	descriptions = []
	datatypes = []
	priorities = []

	for column in header:
		if not column in CLINICAL_ATTRIBUTE_METADATA.keys():
			print 'Clinical attribute not known:', column
			print 'Please add clinical attribute metadata before continuing. Exiting...'
			sys.exit(2)
		display_names.append(CLINICAL_ATTRIBUTE_METADATA[column]['DISPLAY_NAME'])
		descriptions.append(CLINICAL_ATTRIBUTE_METADATA[column]['DESCRIPTION'])
		datatypes.append(CLINICAL_ATTRIBUTE_METADATA[column]['DATATYPE'])
		priorities.append(CLINICAL_ATTRIBUTE_METADATA[column]['PRIORITY'])

	display_names = '#' + '\t'.join(display_names)
	descriptions = '#' + '\t'.join(descriptions)
	datatypes = '#' + '\t'.join(datatypes)
	priorities = '#' + '\t'.join(priorities)

	metadata = [display_names, descriptions, datatypes, priorities]
	return metadata	


def write_clinical_datafile(clinical_header, is_patient_file, clinical_filename):
	""" Writes the clinical datafile with the metadata filtered by attribute type. """

	# get the clinical metadata
	clinical_metadata = get_clinical_header_metadata(clinical_header)

	# read the clinical data file and filter data by given header
	clinical_file = open(clinical_filename, 'rU')
	clinical_reader = csv.DictReader(clinical_file, dialect='excel-tab')
	filtered_clinical_data = ['\t'.join(clinical_header)]
	for line in clinical_reader:
		line_data = map(lambda x: line.get(x, 'NA'), clinical_header)
		filtered_clinical_data.append('\t'.join(line_data))

	# resolve the output filename 
	output_directory = os.path.dirname(os.path.abspath(clinical_filename))
	if is_patient_file:
		output_filename = os.path.join(output_directory, CLINICAL_PATIENT_FILENAME)
	else: 
		output_filename = os.path.join(output_directory, CLINICAL_SAMPLE_FILENAME)
	clinical_file.close()

	# combine metadata and filtered clinical data for output
	output_data = clinical_metadata[:]
	output_data.extend(filtered_clinical_data)

	# create output file and write output data
	output_file = open(output_filename, 'w')
	output_file.write('\n'.join(output_data))
	output_file.close()

	if is_patient_file:
		print 'Patient clinical data written to:', output_filename
	else :
		print 'Sample clinical data written to:', output_filename


def split_data_clinical_attributes_main(clinical_filename):
	""" Writes clinical data to separate clinical patient and clinical sample files. """

	# get the patient and sample clinical file headers
	patient_clinical_header = get_clinical_header(clinical_filename, True)
	sample_clinical_header = get_clinical_header(clinical_filename, False)

	write_clinical_datafile(patient_clinical_header, True, clinical_filename)
	write_clinical_datafile(sample_clinical_header, False, clinical_filename)


def usage():
	print >> OUTPUT_FILE, 'split_data_clinical_attributes.py --clinical-file path/to/clinical/file'
	sys.exit(2)


def main():
	# get command line arguments
	parser = optparse.OptionParser()
	parser.add_option('-c', '--clinical-file', action = 'store', dest = 'clinfile')

	(options, args) = parser.parse_args()
	clinical_filename = options.clinfile

	if not clinical_filename:
		usage()

	# exit if clinical file does not exist
	if not os.path.exists(clinical_filename):
		print 'No such file:', clinical_filename
		sys.exit(2)

	# load clinical attribute metadata
	load_clinical_attribute_metadata()
	split_data_clinical_attributes_main(clinical_filename)


if __name__ == '__main__':
	main()