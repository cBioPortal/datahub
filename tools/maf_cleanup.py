#!/usr/bin/env python2.7

import argparse

### start of parsing parameters
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input-file', action = 'store', dest = 'inputfile', help = "file name of input maf", required=True)
parser.add_argument('-o', '--output-file', action= 'store', dest = "outputfile", default=False, help = "file name of output maf", required=True)
parser.add_argument('-c', '--gene-id', action= 'store', dest = "geneidfile", default=False, help = "file name of gene id mapping", required=True)

args = parser.parse_args()
input_file = args.inputfile
output_file = args.outputfile
gene_id_file = args.geneidfile

#if not input_file:
#	print 'ERROR: missing input MAF name.'
#	parser.print_help()
#elif not output_file:
#	print 'ERROR: missing output MAF name.'
#	parser.print_help()

### end of parsing parameters

### start of searching for header row
header_line = ""
with open(input_file, "r") as f:
	for line in f:
		values = line.split("\t")
		if values[0].upper() == "HUGO_SYMBOL":
			header_line = line
			break;
headers = header_line.rstrip().split("\t")
keep_col_index_arr = [] #Index of columns to keep
### end of searching for header row

### start of filtering out unwanted columns
count = 0
exon_number_index = -1
exon_index = -1
intron_index = -1
oncotator_index_arr = []
for header_item in headers:
	if header_item.upper() == "EXON_NUMBER":
		exon_number_index = count
	elif header_item.upper() == "EXON":
		exon_index = count
	elif header_item.upper() == "INTRON":
		intron_index = count
	elif header_item[0:len("ONCOTATOR")].upper() == "ONCOTATOR":
		oncotator_index_arr.append(count)
	else:
		keep_col_index_arr.append(count)
	count += 1

if exon_number_index != -1 or exon_index != -1 or intron_index != -1 or len(oncotator_index_arr) != 0:
	print "Dropping columns >>>>>>>>>>>>>>"
if exon_number_index != -1:
	print "EXON_NUMBER: " + str(exon_number_index)
if exon_index != -1:
	print "EXON: " + str(exon_index)
if intron_index != -1:
	print "INTRON: " + str(intron_index)
if len(oncotator_index_arr) != 0:
	print "ONCOTATOR: " + ' '.join(str(index) for index in oncotator_index_arr)
### end of filtering out unwated columns

### Start of reconstructing file
print "Reconstructing file ........"
input_maf = open(input_file, "r")
output_maf = open(output_file, "w")

# write out the original extra header lines (sequences samples, versions, etc.)
for line in input_maf:
	values = line.split("\t")
	if values[0].upper() != "HUGO_SYMBOL":
		output_maf.write(line)
	else:
		break

# write out header line
header_item_arr = []
for keep_col_index in keep_col_index_arr:
	if headers[keep_col_index].upper() == "HUGO_SYMBOL":
		header_item_arr.append("Hugo_Symbol")
	elif headers[keep_col_index].upper() == "START_POSITION":
		header_item_arr.append("Start_Position")
	elif headers[keep_col_index].upper() == "END_POSITION":
		header_item_arr.append("End_Position")
	else:
		header_item_arr.append(headers[keep_col_index])
output_maf.write("\t".join(header_item_arr) + "\n");

#creating dictionary of gene id mapping
id_mapping = {}
with open(gene_id_file, "r") as f:
	for line in f:
		cols = line.rstrip("\n").split("\t")
		id_mapping[cols[1]]=cols[0]

# write out content
row_count = 0;
for line in input_maf:
	cols = line.rstrip("\n").split("\t")
	content_item_arr = []
	for keep_col_index in keep_col_index_arr:
		if cols[keep_col_index].upper() in id_mapping:
			content_item_arr.append(id_mapping[cols[keep_col_index].upper()])
			print "ROW " + str(row_count) + " converting gene symbol: " + cols[keep_col_index] + " --> " + id_mapping[cols[keep_col_index].upper()]
		else:
			content_item_arr.append(cols[keep_col_index])			
	row_count = row_count + 1
	output_maf.write("\t".join(content_item_arr) + "\n")

input_maf.close()
output_maf.close()
#### End of reconstructing file
