input_maf = open ("data_mutations_extended.txt", "r")
header_line = "";

# search for header row
for line in input_maf:
	values = line.split("\t");
	if values[0].upper() == "HUGO_SYMBOL":
		header_line = line;

headers = header_line.rstrip().split("\t");
keep_col_index_arr = []; #Index of columns to keep
input_maf.close();

# iterate through all column headers and record the index of targeted ones
count = 0;
exon_number_index = -1;
exon_index = -1;
intron_index = -1;
oncotator_index_arr = [];
for header_item in headers:
	if header_item.upper() == "EXON_NUMBER":
		exon_number_index = count;
	elif header_item.upper() == "EXON":
		exon_index = count;
	elif header_item.upper() == "INTRON":
		intron_index = count;
	elif header_item[0:len("ONCOTATOR")] == "ONCOTATOR":
		oncotator_index_arr.append(count);
	else:
		keep_col_index_arr.append(count);
	count += 1;

print "INDEX OF COLUMNS TO DROP >>>>>>>>>>>>>>";
print "INTRON: " + str(intron_index);
print "EXON_NUMBER: " + str(exon_number_index);
print "EXON: " + str(exon_index);
print "ONCOTATOR: " + str(oncotator_index_arr)[1:-1] ;
print "DROPPING COLUMNS ....";


#### Start of reconstructing file
input_maf = open ("data_mutations_extended.txt", "r");
output_maf = open ("output_maf.txt", "w");

# write out the original extra header lines (sequences samples, versions, etc.)
for line in input_maf:
	values = line.split("\t");
	if values[0].upper() != "HUGO_SYMBOL":
		output_maf.write(line);
	else:
		break;

# write out header line
for keep_col_index in keep_col_index_arr:
	if headers[keep_col_index].upper() == "HUGO_SYMBOL":
		output_maf.write("Hugo_Symbol");
	elif headers[keep_col_index].upper() == "START_POSITION":
		output_maf.write("\tStart_Position");
	elif headers[keep_col_index].upper() == "END_POSITION":
		output_maf.write("\tEnd_Position");
	else:
		output_maf.write("\t" + headers[keep_col_index]);
output_maf.write("\n");

# write out content
for line in input_maf:
	col_counter = 0;
	cols = line.split("\t");
	for keep_col_index in keep_col_index_arr:
		if col_counter != 0:
			output_maf.write("\t");
			output_maf.write(cols[keep_col_index]);
		else:
			if cols[keep_col_index].upper() == "1-FEB":
				output_maf.write("FEB1");
			elif cols[keep_col_index].upper() == "2-FEB":
				output_maf.write("FEB2");
			elif cols[keep_col_index].upper() == "5-FEB":
				output_maf.write("FEB5");
			elif cols[keep_col_index].upper() == "6-FEB":
				output_maf.write("FEB6");
			elif cols[keep_col_index].upper() == "7-FEB":
				output_maf.write("FEB7");
			elif cols[keep_col_index].upper() == "9-FEB":
				output_maf.write("FEB9");
			elif cols[keep_col_index].upper() == "10-FEB":
				output_maf.write("FEB10");
			elif cols[keep_col_index].upper() == "1-MAR":
				output_maf.write("MARCH1");
			elif cols[keep_col_index].upper() == "2-MAR":
				output_maf.write("MARCH2");
			elif cols[keep_col_index].upper() == "3-MAR":
				output_maf.write("MARCH3");
			elif cols[keep_col_index].upper() == "4-MAR":
				output_maf.write("MARCH4");
			elif cols[keep_col_index].upper() == "5-MAR":
				output_maf.write("MARCH5");
			elif cols[keep_col_index].upper() == "6-MAR":
				output_maf.write("MARCH6");
			elif cols[keep_col_index].upper() == "7-MAR":
				output_maf.write("MARCH7");
			elif cols[keep_col_index].upper() == "8-MAR":
				output_maf.write("MARCH8");
			elif cols[keep_col_index].upper() == "9-MAR":
				output_maf.write("MARCH9");
			elif cols[keep_col_index].upper() == "10-MAR":
				output_maf.write("MARCH10");
			elif cols[keep_col_index].upper() == "11-MAR":
				output_maf.write("MARCH11");
			elif cols[keep_col_index].upper() == "1-APR":
				output_maf.write("MAGEH1");
			elif cols[keep_col_index].upper() == "2-APR":
				output_maf.write("FAM215A");
			elif cols[keep_col_index].upper() == "3-APR":
				output_maf.write("ATRAID");
			elif cols[keep_col_index].upper() == "1-MAY":
				output_maf.write("PRKCD");
			elif cols[keep_col_index].upper() == "1-SEP":
				output_maf.write("SEPT1");
			elif cols[keep_col_index].upper() == "2-SEP":
				output_maf.write("SEPT2");
			elif cols[keep_col_index].upper() == "3-SEP":
				output_maf.write("SEPT3");
			elif cols[keep_col_index].upper() == "4-SEP":
				output_maf.write("SEPT4");
			elif cols[keep_col_index].upper() == "5-SEP":
				output_maf.write("SEPT5");
			elif cols[keep_col_index].upper() == "6-SEP":
				output_maf.write("SEPT6");
			elif cols[keep_col_index].upper() == "7-SEP":
				output_maf.write("SEPT7");
			elif cols[keep_col_index].upper() == "8-SEP":
				output_maf.write("SEPT8");
			elif cols[keep_col_index].upper() == "9-SEP":
				output_maf.write("SEPT9");
			elif cols[keep_col_index].upper() == "10-SEP":
				output_maf.write("SEPT10");
			elif cols[keep_col_index].upper() == "11-SEP":
				output_maf.write("SEPT11");
			elif cols[keep_col_index].upper() == "12-SEP":
				output_maf.write("SEPT12");
			elif cols[keep_col_index].upper() == "13-SEP":
				output_maf.write("SEPT13");
			elif cols[keep_col_index].upper() == "14-SEP":
				output_maf.write("SEPT14");
			elif cols[keep_col_index].upper() == "2-OCT":
				output_maf.write("POU2F2");
			elif cols[keep_col_index].upper() == "2-OCT":
				output_maf.write("SLC22A2");
			elif cols[keep_col_index].upper() == "3-OCT":
				output_maf.write("POU5F1");
			elif cols[keep_col_index].upper() == "4-OCT":
				output_maf.write("POU5F1");
			elif cols[keep_col_index].upper() == "6-OCT":
				output_maf.write("POU3F1");
			elif cols[keep_col_index].upper() == "6-OCT":
				output_maf.write("SLC22A16");
			elif cols[keep_col_index].upper() == "7-OCT":
				output_maf.write("POU3F2");
			elif cols[keep_col_index].upper() == "9-OCT":
				output_maf.write("POU3F4");
			elif cols[keep_col_index].upper() == "11-OCT":
				output_maf.write("POU2F3");
			elif cols[keep_col_index].upper() == "1-NOV":
				output_maf.write("C11orf40");
			elif cols[keep_col_index].upper() == "2-NOV":
				output_maf.write("CTGF");
			elif cols[keep_col_index].upper() == "1-DEC":
				output_maf.write("DEC1");
			else:
				output_maf.write(cols[keep_col_index]);
		col_counter += 1;

input_maf.close();
output_maf.close();
#### End of reconstructing file

