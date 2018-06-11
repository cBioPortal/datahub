### Usage

This tool aims to cleanup MAFs in the following aspects:

1. Convert dates back to gene symbols (hugo_symbol)

Detailed list see gene_id.txt

2. Correct letter case pattern for header fields

Start_Position
End_Position
Hugo_Symbol

3. Drop columns

Exon
Exon_number
Intron
ONCOTATOR_*

### Command Line
```
  -h, --help            show this help message and exit
  -i INPUTFILE, --input-file=INPUTFILE
                        file name of input maf
  -o OUTPUTFILE, --output-file=OUTPUTFILE
                        file name of output maf
  -c GENEIDFILE, --gene-id=GENEIDFILE
                        file name of gene id mapping
```

### Example
```
	cd path/to/study
	python maf_cleanup.py -i data_mutations_extended.txt -o output.txt -c gene_id.txt
```

### Notes
`gene_id.txt` is a mapping between captured wrongly formatted gene symbols with the correct form.

