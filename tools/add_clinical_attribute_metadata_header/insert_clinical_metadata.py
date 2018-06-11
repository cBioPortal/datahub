import os
import sys
import csv
import optparse

# some file descriptors
ERROR_FILE = sys.stderr
OUTPUT_FILE = sys.stdout

CLINICAL_ATTRIBUTE_METADATA_FILENAME = '/Users/suny1/scripts/curation/header/clinical_attributes_metadata.txt'
CLINICAL_ATTRIBUTE_METADATA = {}
PATIENT_CLINICAL_ATTRIBUTES = {}

CLINICAL_PATIENT_FILENAME = 'data_clinical_patient.txt'
CLINICAL_SAMPLE_FILENAME = 'data_clinical_sample.txt'

NULL_VALUES = ['NA', None]

def process_datum(datum):
	try: 
		dfixed = datum.strip()
	except AttributeError:
		dfixed='NA'

	if dfixed in NULL_VALUES:
		return 'NA'
	else:
		return dfixed

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

		CLINICAL_ATTRIBUTE_METADATA[column] = {'DISPLAY_NAME':display_name, 'DESCRIPTION':description, 'PRIORITY':priority, 'DATATYPE':datatype, 'ATTRIBUTE_TYPE':attribute_type}


def get_clinical_header(clinical_filename):
	""" Returns the new file header by clinical file type. """
	new_header = ['PATIENT_ID']

	# get the file header and filter by attribute type
	clinical_file_header = get_header(clinical_filename)
	if 'SAMPLE_ID' in clinical_file_header:
		new_header.append('SAMPLE_ID')

	filtered_header = [hdr for hdr in clinical_file_header if not hdr in new_header]

	new_header.extend(filtered_header)

	return new_header


def get_clinical_header_metadata(header, clinical_filename):
	""" 
		Returns the clinical header metadata. 
		The order of the clinical header metadata goes:
			1. display name 
			2. descriptions
			3. datatype (STRING, NUMBER, BOOLEAN)
			4. attribute type (PATIENT, SAMPLE)
			5. priority
	"""

	display_names = []
	descriptions = []
	datatypes = []
	attribute_types = []
	priorities = []
    
	is_mixed_attributes = ('data_clinical.txt' == os.path.basename(clinical_filename))
	for column in header:
		if not column in CLINICAL_ATTRIBUTE_METADATA.keys():
			print 'Clinical attribute not known:', column
			print 'Please add clinical attribute metadata before continuing. Exiting...'
			sys.exit(2)
		display_names.append(CLINICAL_ATTRIBUTE_METADATA[column]['DISPLAY_NAME'])
		descriptions.append(CLINICAL_ATTRIBUTE_METADATA[column]['DESCRIPTION'])
		datatypes.append(CLINICAL_ATTRIBUTE_METADATA[column]['DATATYPE'])
		priorities.append(CLINICAL_ATTRIBUTE_METADATA[column]['PRIORITY'])

        # add attribute type only if clinical file contains mixed attributes
        if is_mixed_attributes:
    		attribute_types.append(CLINICAL_ATTRIBUTE_METADATA[column]['ATTRIBUTE_TYPE'])

	display_names = '#' + '\t'.join(display_names)
	descriptions = '#' + '\t'.join(descriptions)
	datatypes = '#' + '\t'.join(datatypes)
	priorities = '#' + '\t'.join(priorities)
	attribute_types = "#" + '\t'.join(attribute_types)

	if is_mixed_attributes:
		metadata = [display_names, descriptions, datatypes, attribute_types, priorities]
	else:
		metadata = [display_names, descriptions, datatypes, priorities]
    
	return metadata	


def write_clinical_metadata(clinical_header, clinical_filename):
	""" Writes the clinical datafile with the metadata filtered by attribute type. """

	# get the clinical metadata
	clinical_metadata = get_clinical_header_metadata(clinical_header, clinical_filename)

	# read the clinical data file and filter data by given header
	clinical_file = open(clinical_filename, 'rU')
	clinical_reader = csv.DictReader(clinical_file, dialect='excel-tab')
	filtered_clinical_data = ['\t'.join(clinical_header)]
	for line in clinical_reader:
		line_data = map(lambda x: process_datum(line.get(x, 'NA')), clinical_header)
		filtered_clinical_data.append('\t'.join(line_data))
	clinical_file.close()

	# resolve the output filename 
	output_directory = os.path.dirname(clinical_filename)
	output_filename = os.path.join(output_directory, clinical_filename + '.metadata')

	# combine metadata and filtered clinical data for output
	output_data = clinical_metadata[:]
	output_data.extend(filtered_clinical_data)

	# create output file and write output data
	output_file = open(output_filename, 'w')
	output_file.write('\n'.join(output_data))
	output_file.close()

	print 'Clinical file with metadata written to:', output_filename


def insert_clinical_metadata_main(directory):
	""" Writes clinical data to separate clinical patient and clinical sample files. """
	clinical_files = find_clinical_files(directory)

	for clinical_filename in clinical_files:
		# get the patient and sample clinical file headers
		clinical_header = get_clinical_header(clinical_filename)
		write_clinical_metadata(clinical_header, clinical_filename)


def find_clinical_files(directory):

	clinical_files = []
	for filename in os.listdir(directory):
		if 'clinical' in filename and not 'meta' in filename: 
			clinical_files.append(os.path.join(directory, filename))

	return clinical_files



def usage():
	print >> OUTPUT_FILE, 'insert_clinical_metadata.py --directory cancer/study/path'
	sys.exit(2)

def main():
	# get command line arguments
	parser = optparse.OptionParser()
	parser.add_option('-d', '--directory', action = 'store', dest = 'directory')

	(options, args) = parser.parse_args()
	directory = options.directory

	# exit if clinical file does not exist
	if not os.path.exists(directory):
		print 'No such directory:', directory
		sys.exit(2)

	# load clinical attribute metadata
	load_clinical_attribute_metadata()
	insert_clinical_metadata_main(directory)


	


if __name__ == '__main__':
	main()
