# blastp-uniref90
Create a blast database from uniref90 sequence database with TaxID per sequence

## 1 Download uniref90 and taxonomy database
uniref90 can be downloaded from:
```console
wget "https://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz"
tar -xf taxdump.tar.gz  
```
taxonomy database can be downloaded from: 
```console
wget "https://ftp.uniprot.org/pub/databases/uniprot/uniref/uniref90/uniref90.fasta.gz"
gunzip uniref90.fasta.gz
```

## Create the SeqID-TaxID mapp
the path to uniref90.fasta and taxonomy database (names.dmp) must be specified inside get_taxlist.py
```console
python get_taxlist.py
```

## Create the blast database
```console
makeblastdb -in uniref90.fasta -parse_seqids -title uniref90 -dbtype prot -out uniref90 -taxid_map uniref90.taxlist
```
