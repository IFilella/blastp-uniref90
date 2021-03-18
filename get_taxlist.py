#https://gist.github.com/sujaikumar/9ad04e62449a2d7025b17144de67038b
import gzip
from Bio import SeqIO


taxdmp={}
with open("names.dmp", "r") as dmpfile:
    for line in dmpfile:
        taxdmp[(str(line.split("\t")[2]))] = str(line.split("\t")[0])
        
with open("uniref90_2021_01.fasta", "r") as uniprot, open("uniref90.taxlist", "w") as outfile:
    for  record in SeqIO.parse(uniprot, "fasta"):
        if "Tax=" in str(record.description):
            tax = record.description.split("Tax=")[1].split("RepID=")[0].split("TaxID=")[0].rstrip()
            taxid = record.description.split("Tax=")[1].split("RepID=")[0].split("TaxID=")[1].rstrip()
            if taxid == "" or taxid == "N/A": continue
            #print(str(record.description))
            #print(tax)
            #print(taxid)
            #print(taxdmp[tax])
            outfile.write(str(record.id + "\t" +str(taxid)+ "\n"))
            #outfile.write(str(record.id + "\t" +str(taxdmp[tax])+ "\n"))
            #outfile.write(str(record.id + "\t" +str(taxdmp.get(record.description.split("Tax=")[1].split("RepID=")[0].rstrip()))+ "\n"))
