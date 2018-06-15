### Usage

This tool is intended to fix some common seen issues with MAFs during curation and importing. 
This tool shall be ran on MAF as the last step before importing. 
Below listed the issues this scripts targets: 

#### Convert dates back to gene symbols (hugo_symbol)

Detailed list see gene_id.txt

#### Correct letter case pattern for header fields

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
python maf_cleanup.py -i <old_maf> -o <new_maf> -c gene_id.txt
```

### Notes
`gene_id.txt` is a mapping between captured wrongly formatted gene symbols with the correct form.

