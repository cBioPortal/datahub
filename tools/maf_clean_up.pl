#!/usr/bin/perl

use warnings;
use strict;

# search for header row
open(IN, "data_mutations_extended.txt") or die;
my $headerline = "";
while (my $line = <IN>) {
	chomp $line;
	my @columns = split(/\t/, $line);
	if ($columns[0] eq "Hugo_Symbol") {
		$headerline = $line;
		last;
	}
}
close IN;

# iterate through all column headers and record the index of targeted ones
my @headers = split(/\t/, $headerline);
my $count = 0;
my $exon_number_index = -1;
my $exon_index = -1;
my $intron_index = -1;
my @oncotator_index = ();
my @keep_cols = ();
my $header = "";
foreach $header (@headers) {
	if (uc($header) eq "EXON_NUMBER") {
		$exon_number_index = $count;
	} elsif (uc($header) eq "EXON") {
		$exon_index = $count;
	} elsif (uc($header) eq "INTRON") {
		$intron_index = $count;
	} elsif (uc(substr($header, 0, length ("ONCOTATOR"))) eq "ONCOTATOR") {
		push @oncotator_index, $count;
	} else {
		push @keep_cols, $count;
	}
	$count++; 
}
print "INDEX OF COLUMNS TO DROP >>>>>>>>>>>>>>\n";
print "INTRON: $intron_index\n";
print "EXON_NUMBER: $exon_number_index\n";
print "EXON: $exon_index\n";
print "ONCOTATOR: @oncotator_index\n";
print "DROPPING COLUMNS ....";

#Reconstruct file
open(IN, "data_mutations_extended.txt") or die "Error occured while writing MAF...";
open(DAT, ">out.txt") or die "Error occured while writing .txt output...";
while (my $line = <IN>) {
	chomp $line;
	my @columns = split(/\t/, $line);
	my $keep_col_index = -1;
	my $col_counter = 0;
	foreach $keep_col_index (@keep_cols) {
		if ($col_counter != 0) {
			print DAT "\t";
			# normalize casing for certain columns
			if (uc($columns[$keep_col_index]) eq "START_POSITION") {
				print DAT "Start_Position";
			} elsif (uc($columns[$keep_col_index]) eq "END_POSITION") {
				print DAT "End_Position";	
			} else {
				# write out only columns needed / trim outdated unused columns 
				print DAT "$columns[$keep_col_index]";
			}
		} else {
			# convert hugo gene symbol in date format.
			if (uc($columns[$keep_col_index]) eq "HUGO_SYMBOL") {
				print DAT "Hugo_Symbol";
			} elsif (uc($columns[$keep_col_index]) eq "1-FEB") {
				print DAT "FEB1";
			} elsif (uc($columns[$keep_col_index]) eq "2-FEB") {
				print DAT "FEB2";
			} elsif (uc($columns[$keep_col_index]) eq "5-FEB") {
				print DAT "FEB5";
			} elsif (uc($columns[$keep_col_index]) eq "6-FEB") {
				print DAT "FEB6";
			} elsif (uc($columns[$keep_col_index]) eq "7-FEB") {
				print DAT "FEB7";
			} elsif (uc($columns[$keep_col_index]) eq "9-FEB") {
				print DAT "FEB9";
			} elsif (uc($columns[$keep_col_index]) eq "10-FEB") {
				print DAT "FEB10";
			} elsif (uc($columns[$keep_col_index]) eq "1-MAR") {
				print DAT "MARCH1";
			} elsif (uc($columns[$keep_col_index]) eq "2-MAR") {
				print DAT "MARCH2";
			} elsif (uc($columns[$keep_col_index]) eq "3-MAR") {
				print DAT "MARCH3";
			} elsif (uc($columns[$keep_col_index]) eq "4-MAR") {
				print DAT "MARCH4";
			} elsif (uc($columns[$keep_col_index]) eq "5-MAR") {
				print DAT "MARCH5";
			} elsif (uc($columns[$keep_col_index]) eq "6-MAR") {
				print DAT "MARCH6";
			} elsif (uc($columns[$keep_col_index]) eq "7-MAR") {
				print DAT "MARCH7";
			} elsif (uc($columns[$keep_col_index]) eq "8-MAR") {
				print DAT "MARCH8";
			} elsif (uc($columns[$keep_col_index]) eq "9-MAR") {
				print DAT "MARCH9";
			} elsif (uc($columns[$keep_col_index]) eq "10-MAR") {
				print DAT "MARCH10";
			} elsif (uc($columns[$keep_col_index]) eq "11-MAR") {
				print DAT "MARCH11";
			} elsif (uc($columns[$keep_col_index]) eq "1-APR") {
				print DAT "MAGEH1";
			} elsif (uc($columns[$keep_col_index]) eq "2-APR") {
				print DAT "FAM215A";
			} elsif (uc($columns[$keep_col_index]) eq "3-APR") {
				print DAT "ATRAID";
			} elsif (uc($columns[$keep_col_index]) eq "1-MAY") {
				print DAT "PRKCD";
			} elsif (uc($columns[$keep_col_index]) eq "1-SEP") {
				print DAT "SEPT1";
			} elsif (uc($columns[$keep_col_index]) eq "2-SEP") {
				print DAT "SEPT2";
			} elsif (uc($columns[$keep_col_index]) eq "3-SEP") {
				print DAT "SEPT3";
			} elsif (uc($columns[$keep_col_index]) eq "4-SEP") {
				print DAT "SEPT4";
			} elsif (uc($columns[$keep_col_index]) eq "5-SEP") {
				print DAT "SEPT5";
			} elsif (uc($columns[$keep_col_index]) eq "6-SEP") {
				print DAT "SEPT6";
			} elsif (uc($columns[$keep_col_index]) eq "7-SEP") {
				print DAT "SEPT7";
			} elsif (uc($columns[$keep_col_index]) eq "8-SEP") {
				print DAT "SEPT8";
			} elsif (uc($columns[$keep_col_index]) eq "9-SEP") {
				print DAT "SEPT9";
			} elsif (uc($columns[$keep_col_index]) eq "10-SEP") {
				print DAT "SEPT10";
			} elsif (uc($columns[$keep_col_index]) eq "11-SEP") {
				print DAT "SEPT11";
			} elsif (uc($columns[$keep_col_index]) eq "12-SEP") {
				print DAT "SEPT12";
			} elsif (uc($columns[$keep_col_index]) eq "13-SEP") {
				print DAT "SEPT13";
			} elsif (uc($columns[$keep_col_index]) eq "14-SEP") {
				print DAT "SEPT14";
			} elsif (uc($columns[$keep_col_index]) eq "2-OCT") {
				print DAT "POU2F2";
			} elsif (uc($columns[$keep_col_index]) eq "2-OCT") {
				print DAT "SLC22A2";
			} elsif (uc($columns[$keep_col_index]) eq "3-OCT") {
				print DAT "POU5F1";
			} elsif (uc($columns[$keep_col_index]) eq "4-OCT") {
				print DAT "POU5F1";
			} elsif (uc($columns[$keep_col_index]) eq "6-OCT") {
				print DAT "POU3F1";
			} elsif (uc($columns[$keep_col_index]) eq "6-OCT") {
				print DAT "SLC22A16";
			} elsif (uc($columns[$keep_col_index]) eq "7-OCT") {
				print DAT "POU3F2";
			} elsif (uc($columns[$keep_col_index]) eq "9-OCT") {
				print DAT "POU3F4";
			} elsif (uc($columns[$keep_col_index]) eq "11-OCT") {
				print DAT "POU2F3";
			} elsif (uc($columns[$keep_col_index]) eq "1-NOV") {
				print DAT "C11orf40";
			} elsif (uc($columns[$keep_col_index]) eq "2-NOV") {
				print DAT "CTGF";
			} elsif (uc($columns[$keep_col_index]) eq "1-DEC") {
				print DAT "DEC1";
			} else {
				print DAT "$columns[$keep_col_index]";
			}
		} 
		$col_counter++;
	}
	print DAT "\n";
}
print "Done.\n";

# close the filehandle
close IN;
close DAT;

exit;