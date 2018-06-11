import sys
import os
import optparse
import re
import shutil

ERROR_FILE = sys.stderr
OUTPUT_FILE = sys.stdout

TCGA_BARCODE_PREFIX = 'TCGA'
TCGA_SAMPLE_BARCODE_PATTERN = '(TCGA-\w*-\w*-\d*).*$'
TCGA_PATIENT_BARCODE_PATTERN = '(TCGA-\w*-\w*).*$'
TCGA_SAMPLE_TYPE_CODE_PATTERN = 'TCGA-\w*-\w*-(\d*).*$'

TCGA_SAMPLE_TYPE_CODES = {
	'01':'Primary Solid Tumor',
	'02':'Recurrent Solid Tumor',
	'03':'Primary Blood Tumor',
	'04':'Recurrent Blood Tumor',
	'06':'Metastatic',
	'10':'Blood Derived Normal',
	'11':'Solid Tissues Normal'
}

META_STUDY_FILENAME = 'meta_study.txt'

GENERAL_CLINICAL_META_FILE_PATTERN = 'meta_clinical.txt'
GENERAL_CLINICAL_DATA_FILE_PATTERN = 'data_clinical.txt'
GENERAL_CLINICAL_DATATYPE = 'CLINICAL'
CLINICAL_PATIENT_META_FILE_KEYWORD = 'patient'
CLINICAL_PATIENT_DATATYPE = 'PATIENT_ATTRIBUTES'
CLINICAL_SAMPLE_META_FILE_KEYWORD = 'sample'
CLINICAL_SAMPLE_DATATYPE = 'SAMPLE_ATTRIBUTES'

MAF_GENERAL_FILE_PATTERN = 'data_mutations_extended.txt'
MAF_UNIPROT_FILE_PATTERN = 'data_mutations_uniprot.txt'
MAF_MSKCC_FILE_PATTERN = 'data_mutations_mskcc.txt'
MAF_DATATYPE = 'MAF'

SEG_DATATYPE = 'SEG'

CASE_LIST_DIRNAME = 'case_lists'
CASES_ALL_FILENAME = 'cases_all.txt'
CASE_LIST_DATATYPE = 'CASE_LIST'

STUDY_SAMPLES = {}
EXISTING_CLINICAL_SAMPLES_LIST = set()
EXISTING_CLINICAL_PATIENTS_LIST = set()

MISSING_CLINICAL_SAMPLES_REPORT_FILENAME = 'samples_missing_clinical_info.txt'

GENETIC_ALTERATION_TYPES = {
	'PROFILE':['COPY_NUMBER_ALTERATION', 'PROTEIN_LEVEL', 'MRNA_EXPRESSION', 'METHYLATION'], 
	'NORMAL':['MUTATION_EXTENDED', 'FUSION', 'CLINICAL'],
	'CASE_INDEPENDENT':['MUTSIG', 'GISTIC_GENES_AMP', 'GISTIC_GENES_DEL']
}

NON_CASE_IDS = [
    'MIRNA',
    'LOCUS',
    'ID',
    'GENE SYMBOL',
    'ENTREZ_GENE_ID',
    'HUGO_SYMBOL',
    'LOCUS ID',
    'CYTOBAND',
    'COMPOSITE.ELEMENT.REF',
    'HYBRIDIZATION REF',
]

def report_missing_clinical_records(study_directory, remove_normal_records, add_missing_records, output_data_directory):
	study_files = load_all_samples_for_study(study_directory)
	# get list in clinical file(s) and compare to what's in genomic files - report any that are not in genomic file lists
	samples_missing_clinical_info = {'compiled_missing_clincal_sample_list':set()}
	normal_samples_found = False
	non_normal_samples_missing_clinical_info_found = False
	print >> OUTPUT_FILE, '\nComparing sample lists from genomic files to samples found in clinical files...'	
	for meta_file,properties in study_files.items():
		# we already know what samples are in clinical files so these can be ignored along w/case independent data files
		if properties['genetic_alteration_type'] == 'CLINICAL' or properties['genetic_alteration_type'] in GENETIC_ALTERATION_TYPES['CASE_INDEPENDENT']:
			continue	
		is_patient_id = (properties['datatype'] == CLINICAL_PATIENT_DATATYPE)	
		missing_samples = [sample_id for sample_id in properties['sample_set'] if not sample_id in EXISTING_CLINICAL_SAMPLES_LIST]		
		if len(missing_samples) > 0:
			normal_samples = [sample_id for sample_id in missing_samples if is_normal_sample(sample_id, is_patient_id)]
			non_normal_missing_samples = [sample_id for sample_id in missing_samples if not is_normal_sample(sample_id, is_patient_id)]
			if len(non_normal_missing_samples) == 0:
				print >> OUTPUT_FILE, '\tWARN: All samples missing clinical info in', properties['data_filename'], 'are NORMAL sample types! These samples will NOT be added to clinical files even if --add-missing-records mode is enabled.'
			else:
				print >> OUTPUT_FILE, '\tFound', len(non_normal_missing_samples), 'samples missing clinical info in:', properties['data_filename']
				samples_missing_clinical_info[meta_file] = set(non_normal_missing_samples)
				samples_missing_clinical_info['compiled_missing_clincal_sample_list'].update(non_normal_missing_samples)
				study_files[meta_file]['missing_samples'] = set(non_normal_missing_samples)
				non_normal_samples_missing_clinical_info_found = True
			if len(normal_samples) > 0:
				study_files[meta_file]['normal_sample_set'] = set(normal_samples)
				normal_samples_found = True

	if len(samples_missing_clinical_info['compiled_missing_clincal_sample_list']) > 0:
		generate_samples_missing_clinical_info_report(study_directory, samples_missing_clinical_info)
	else:
		print >> OUTPUT_FILE, 'No samples missing clinical data to report.'

	if normal_samples_found:
		if remove_normal_records:
			find_and_remove_normal_samples(study_directory, study_files, output_data_directory)
		else:
			print >> OUTPUT_FILE, 'WARN: Normal samples found but --remove-normal-records mode is not enabled. Data files will retain normal data.'

	if non_normal_samples_missing_clinical_info_found:
		if add_missing_records:
			add_missing_clinical_records(study_files, output_data_directory, samples_missing_clinical_info['compiled_missing_clincal_sample_list'])
		else:
			if normal_samples_found:
				print >> OUTPUT_FILE, 'WARN: No missing samples to add since only normal samples were found to be missing from clinical data and thus will not be added to clinical file(s).'
				if not remove_normal_records:
					print >> OUTPUT_FILE, '* NOTE *: Consider running script with the --remove-normal-records mode enabled to cleanup the data'
	else:
		print >> OUTPUT_FILE, '\nClinical data files are not missing any samples. No changes to make.'



def add_missing_clinical_records(study_files, output_data_directory, compiled_missing_clincal_sample_list):
	print >> OUTPUT_FILE, '\nAdding patients/samples missing from clinical data files...'
	new_case_list_dir = os.path.join(output_data_directory, CASE_LIST_DIRNAME)
	if not os.path.exists(new_case_list_dir):
		os.mkdir(new_case_list_dir)

	for meta_file,properties in study_files.items():
		# if new meta or data file does not already exist then that means that no attempt to remove normals from data was made
		# and we can go ahead and copy over the data and meta files to the new output directory
		new_meta_filename = os.path.join(output_data_directory, os.path.basename(meta_file))
		if not os.path.exists(new_meta_filename) and not GENERAL_CLINICAL_META_FILE_PATTERN in meta_file and properties['datatype'] != CASE_LIST_DATATYPE:
			shutil.copy(meta_file, new_meta_filename)

		if properties['datatype'] == CASE_LIST_DATATYPE:
			new_data_filename = os.path.join(new_case_list_dir, os.path.basename(properties['data_filename']))
		else:
			new_data_filename = os.path.join(output_data_directory, os.path.basename(properties['data_filename']))
		if not os.path.exists(new_data_filename):
			shutil.copy(properties['data_filename'], new_data_filename)

		# we are not making any modifications to non-clinical files
		if properties['genetic_alteration_type'] != 'CLINICAL':
			continue

		print >> OUTPUT_FILE, '\tAdding missing patient/sample records to:', new_data_filename
		header = get_file_header(new_data_filename)
		data_file = open(new_data_filename, 'rU')
		filedata = [line for line in data_file.readlines()]
		data_file.close()

		data_file = open(new_data_filename, 'w')
		data_file.write(''.join(filedata))

		for sample_id in compiled_missing_clincal_sample_list:
			data = dict(zip(header, ['' for column in header]))
			patient_id = get_stable_id(sample_id, True)

			# do not want to add duplicate patient records if patient already exists in file - this could potentially happen if a patient
			# has multiple samples but only one sample exists in the clinical data			
			if patient_id in EXISTING_CLINICAL_PATIENTS_LIST and properties['datatype'] == CLINICAL_PATIENT_DATATYPE:
				continue
			if sample_id in EXISTING_CLINICAL_SAMPLES_LIST:
				continue

			data['PATIENT_ID'] = patient_id
			if 'SAMPLE_ID' in header:
				data['SAMPLE_ID'] = sample_id # sample id is already in standardized format by now - don't need to get the stable id again

			sample_data = map(lambda x: data.get(x,''), header)
			data_file.write('\n' + '\t'.join(sample_data))
		data_file.close()


def find_and_remove_normal_samples(study_directory, study_files, output_data_directory):
	print >> OUTPUT_FILE, '\nRemoving normals from data files in:', study_directory, '- processed files will be written to:', output_data_directory
	new_case_list_dir = os.path.join(output_data_directory, CASE_LIST_DIRNAME)
	if not os.path.exists(new_case_list_dir):
		os.mkdir(new_case_list_dir)

	for meta_file,properties in study_files.items():
		normal_samples = properties.get('normal_sample_set', set())
		if properties['datatype'] == CASE_LIST_DATATYPE:
			new_data_filename = os.path.join(new_case_list_dir, os.path.basename(properties['data_filename']))
		else:
			new_data_filename = os.path.join(output_data_directory, os.path.basename(properties['data_filename']))

		# always copy over the meta file unless it's generic clinical meta file (meta_clinical.txt) or a case list
		if not GENERAL_CLINICAL_META_FILE_PATTERN in meta_file and properties['datatype'] != CASE_LIST_DATATYPE:
			shutil.copy(meta_file, os.path.join(output_data_directory, os.path.basename(meta_file)))

		if len(normal_samples) == 0 or properties['datatype'] == CLINICAL_PATIENT_DATATYPE:
			# simply copy data file to new output directory if no changes needed
			print >> OUTPUT_FILE, '\tNothing to remove from:', properties['data_filename']
			if properties['datatype'] == CASE_LIST_DATATYPE:
				shutil.copy(properties['data_filename'], new_data_filename)
			else:
				shutil.copy(properties['data_filename'], new_data_filename)
		else:			
			if properties['datatype'] == CASE_LIST_DATATYPE:
				# subset case list data
				remove_normal_samples_from_case_list(new_data_filename, properties)
			else:
				remove_normal_samples_from_data_file(new_data_filename, properties)


def remove_normal_samples_from_case_list(new_data_filename, properties):
	print >> OUTPUT_FILE, '\tRemoving normals from:', properties['data_filename']
	
	data_file = open(properties['data_filename'], 'rU')
	new_data_file = open(new_data_filename, 'w')
	for line in data_file.readlines():
		if not line.startswith('case_list_ids'):
			new_data_file.write(line)
		else:
			filtered_sample_list = [sample_id for sample_id in properties['sample_set'] if not sample_id in properties['normal_sample_set']]
			new_data_file.write('case_list_ids: ' + '\t'.join(filtered_sample_list))
	new_data_file.close()
	data_file.close()


def remove_normal_samples_from_data_file(new_data_filename, properties):
	print >> OUTPUT_FILE, '\tRemoving normals from:', properties['data_filename']

	data_file = open(properties['data_filename'], 'rU')
	new_data_file = open(new_data_filename, 'w')	
	if properties['genetic_alteration_type'] in GENETIC_ALTERATION_TYPES['NORMAL'] or properties['datatype'] == SEG_DATATYPE:
		header_added = False
		for line in data_file.readlines():
			# keep comments
			if line.startswith('#'):
				new_data_file.write(line)
				continue
			# add header if not already added
			if not header_added:
				new_data_file.write(line)
				header_added = True
				continue
			# add data row if row does not contain a normal sample id
			data = map(str.strip, line.split('\t'))
			if len([value for value in data if value in properties['normal_sample_set']]) > 0:
				continue
			new_data_file.write(line)
	else:
		header = get_file_header(properties['data_filename'])
		filtered_header = [column for column in header if not column in properties['normal_sample_set']]
		new_data_file.write('\t'.join(filtered_header))
		for line in data_file.readlines()[1:]:
			data = dict(zip(header, map(str.strip, line.split('\t'))))
			filtered_data = map(lambda x: data.get(x, ''), filtered_header)
			new_data_file.write('\n' + '\t'.join(filtered_data))
	new_data_file.close()
	data_file.close()


def generate_samples_missing_clinical_info_report(study_directory, samples_missing_clinical_info):
	output_filename = os.path.join(study_directory, MISSING_CLINICAL_SAMPLES_REPORT_FILENAME)
	output_file = open(output_filename, 'w')
	output_file.write('compiled_missing_clincal_sample_list\t' + ','.join(list(samples_missing_clinical_info['compiled_missing_clincal_sample_list'])) + '\n')
	for meta_file,missing_samples in samples_missing_clinical_info.items():
		if meta_file != 'compiled_missing_clincal_sample_list':
			output_file.write(meta_file + '\t' + ','.join(list(missing_samples)))
	output_file.close()
	print >> OUTPUT_FILE, '\nSaved missing clinical records report to:', output_filename


def load_all_samples_for_study(study_directory):
	"""
		Loads all samples/patients and stores them in STUDY_SAMPLES.
	"""
	print >> OUTPUT_FILE, 'Processing data files in cancer study path:', study_directory
	study_files = organize_study_files(study_directory)	
	for meta_file,properties in study_files.items():
		if properties['genetic_alteration_type'] in GENETIC_ALTERATION_TYPES['CASE_INDEPENDENT']:
			print >> OUTPUT_FILE, '\tWARN: Data file is not dependent on samples - file will be skipped:', meta_file
			continue

		if properties['datatype'] == CASE_LIST_DATATYPE:
			samples = load_samples_from_case_list(properties)
		else:
			samples = load_samples_from_data_file(study_directory, properties)			
			if properties['datatype'] in [GENERAL_CLINICAL_DATATYPE, CLINICAL_SAMPLE_DATATYPE]:
				EXISTING_CLINICAL_SAMPLES_LIST.update(samples)

		study_files[meta_file]['sample_set'] = samples
	return study_files


def load_samples_from_data_file(study_directory, properties):
	"""
		Loads samples from data file.
	"""
	print >> OUTPUT_FILE, '\tLoading samples from data file:', properties['data_filename']
	is_patient_id = False
	samples = set()
	header = get_file_header(properties['data_filename'])	
	if properties['genetic_alteration_type'] in GENETIC_ALTERATION_TYPES['NORMAL'] or properties['datatype'] == SEG_DATATYPE:
		if properties['genetic_alteration_type'] == 'CLINICAL':
			# keep track of patient ids seen in clinical data files
			update_clinical_patients_seen(properties['data_filename'], header)
			if not 'SAMPLE_ID' in header:
				case_id_column = 'PATIENT_ID'
				is_patient_id = True
			else:
				case_id_column = 'SAMPLE_ID'
		elif 'Tumor_Sample_Barcode' in header:
			case_id_column = 'Tumor_Sample_Barcode'
		elif properties['datatype'] == SEG_DATATYPE:
			case_id_column = 'ID'
		else:
			print >> ERROR_FILE, 'ERROR: Do not know how to extract samples from file:', properties['data_filename']
			print >> ERROR_FILE, 'ERROR: File does not contain key column for clinical files (PATIENT_ID and/or SAMPLE_ID) or mutation/fusion file (Tumor_Sample_Barcode)'
			sys.exit(2)
		data_file = open(properties['data_filename'], 'rU')
		data_reader = [l for l in data_file.readlines() if not l.startswith('#')][1:]
		for line in data_reader:
			data = dict(zip(header, map(str.strip, line.split('\t'))))
			samples.add(data[case_id_column])
		data_file.close()
	else:
		samples.update([column for column in header if not column.upper() in NON_CASE_IDS])
	sample_set = set(map(lambda x: get_stable_id(x.strip(), is_patient_id), samples))
	return sample_set


def update_clinical_patients_seen(data_filename, header):
	data_file = open(data_filename, 'rU')
	data_reader = [l for l in data_file.readlines() if not l.startswith('#')][1:]
	for line in data_reader:
		data = dict(zip(header, map(str.strip, line.split('\t'))))
		EXISTING_CLINICAL_PATIENTS_LIST.add(get_stable_id(data['PATIENT_ID'], True))
	data_file.close()


def load_samples_from_case_list(properties):
	"""
		Loads samples from case list file.
	"""
	print >> OUTPUT_FILE, '\tLoading samples from case list:', properties['data_filename']
	samples = map(lambda x: get_stable_id(x.strip(), False), properties['case_list_ids'].split('\t'))
	return set(samples)


def organize_study_files(study_directory):
	"""
		Organizes meta and data files by genetic alteration type
	"""
	study_files = {}
	for f in os.listdir(study_directory):
		# skip data files and meta_study.txt file
		if META_STUDY_FILENAME in f:
			continue
		if not 'meta' in f and not CASE_LIST_DIRNAME in f:
			continue
		# load properties from meta file and case lists
		full_filepath = os.path.join(study_directory, f)
		if 'meta' in f:
			study_files[full_filepath] = load_properties(study_directory, full_filepath, False)
		elif CASE_LIST_DIRNAME in f:
			for clf in os.listdir(full_filepath):
				case_list_filename = os.path.join(full_filepath, clf)
				study_files[case_list_filename] = load_properties(study_directory, case_list_filename, True)
	if GENERAL_CLINICAL_DATA_FILE_PATTERN in os.listdir(study_directory):
		study_files[GENERAL_CLINICAL_META_FILE_PATTERN] = {'datatype':'CLINICAL', 'genetic_alteration_type':'CLINICAL', 'data_filename':GENERAL_CLINICAL_DATA_FILE_PATTERN}
	return study_files


def load_properties(study_directory, filename, is_case_list):
	"""
		Loads properties as dictionary. 
	"""
	properties = {}
	data_file = open(filename, 'rU')
	for line in data_file:
		prop_name = line.split(':')[0]
		prop_value = line.split(':')[1].strip()
		properties[prop_name] = prop_value
	data_file.close()	

	if is_case_list:
		properties['datatype'] = CASE_LIST_DATATYPE
		properties['genetic_alteration_type'] = CASE_LIST_DATATYPE
		properties['data_filename'] = filename
	else:
		properties['data_filename'] = os.path.join(study_directory, properties['data_filename'])

	# if MAF meta file then choose uniprot or mskcc maf if exists if regular MAF file does not exist
	# both mskcc and uniprot MAFs should contain the same samples so the selection is arbitrary
	if properties['datatype'] == 'MAF':
		if not os.path.exists(properties['data_filename']):
			for maf_filename in [MAF_GENERAL_FILE_PATTERN, MAF_MSKCC_FILE_PATTERN, MAF_UNIPROT_FILE_PATTERN]:
				if os.path.exists(os.path.join(study_directory, maf_filename)):
					properties['data_filename'] = os.path.join(study_directory, maf_filename)
					break

	return properties

def get_patient_id(case_id):
	if case_id.startswith(TCGA_BARCODE_PREFIX):
		m = re.search(TCGA_PATIENT_BARCODE_PATTERN, case_id)
		return m.group(1)
	return case_id

def get_sample_id(case_id):
	if case_id.startswith(TCGA_BARCODE_PREFIX):
		try:
			m = re.search(TCGA_SAMPLE_BARCODE_PATTERN, case_id)
			return m.group(1)
		except AttributeError:
			return case_id + '-01'
	return case_id

def get_stable_id(case_id, is_patient_id):
	if is_patient_id:
		return get_patient_id(case_id)
	return get_sample_id(case_id)

def is_normal_sample(case_id, is_patient_id):
	if is_patient_id or not case_id.startswith(TCGA_BARCODE_PREFIX):
		return False
	m = re.search(TCGA_SAMPLE_TYPE_CODE_PATTERN, case_id)
	sample_type = TCGA_SAMPLE_TYPE_CODES.get(m.group(1), 'Primary Solid Tumor')
	if 'NORMAL' in sample_type.upper():
		return True
	return False

def get_file_header(filename):
	"""
		Returns the file header.
	"""
	data_file = open(filename, 'rU')
	filedata = [l for l in data_file.readlines() if not l.startswith('#')]
	data_file.close()
	header = map(str.strip, filedata[0].split('\t'))
	return header
	
def usage(parser):
	parser.print_help()
	sys.exit(2)

def main():
	# get command line stuff
	parser = optparse.OptionParser()
	parser.add_option('-d', '--study-directory', action = 'store', dest = 'studydir', help = "path to study directory")
	parser.add_option('-a', '--add-missing-records', action="store_true", dest = "addmissing", default=False, help = "flag for adding missing records to clinical files")
	parser.add_option('-r', '--remove-normal-records', action="store_true", dest = "removenorms", default=False, help = "flag for removing normal records from data files")
	parser.add_option('-o', '--output-data-directory', action = 'store', dest = 'outputdir', help = "output directory used after removing normal records from data")

	(options, args) = parser.parse_args()
	study_directory = options.studydir
	add_missing_records = options.addmissing
	remove_normal_records = options.removenorms
	output_data_directory = options.outputdir

	if not study_directory:
		print >> ERROR_FILE, 'ERROR: Study directory must be provided!\n'
		usage(parser)
	if not output_data_directory and (add_missing_records or remove_normal_records):
		print >> ERROR_FILE, 'ERROR: Output data directory must be provided when --add-missing-records and/or --remove-normal-records are enabled.\n'
		usage(parser)

	if not os.path.exists(study_directory):
		print >> ERROR_FILE, 'No such directory: ' + study_directory, '\n'
		usage(parser)
	
	report_missing_clinical_records(study_directory, remove_normal_records, add_missing_records, output_data_directory)


if __name__ == '__main__':
	main()