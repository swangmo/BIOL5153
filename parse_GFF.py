#! /usr/bin/python

import argparse
	
parser = argparse.ArgumentParser(description = "parse files")

parser.add_argument( "--gff", help="the name of the gff file", default= "watermelon.gff")
parser.add_argument( "--fasta", help="the name of the fasta file", default= "watermelon.fsa")

args = parser.parse_args()

gff_file = open(args.gff, "r")
gff_output = open("gff_output.file", "w")

for line in gff_file:

    fields = line.split("\t")
    start = int(fields[3])
    stop = int(fields[4])
    
    gff_substring = (fields[3], fields[4])

    gff_output.write(str(start) + "\t" + str(stop) + "\n")

    print(str(start) + "\t" + str(stop) + "\n")

gff_file.close()

fasta_file = open(args.fasta, "r")
fasta_output = open("gff_output.file")


substring = open("substring.file", "w")

for lines in fasta_file:

    positions = lines.split('\t')
    start = int(positions[0])
    stop =  int(positions[1])
    substring_sequence = fasta[start:stop]
    print(substring_sequence)
    fasta_out.write(substring_sequence)

fasta_file.close()
   





