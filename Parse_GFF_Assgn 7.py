#!/usr/env/python

import argparse
import csv

gff_file   = 'watermelon.gff'
fasta_file = 'watermelon.fsa'

def get_args():
parser = argparse.ArgumentParser(description = 'This script removes false frequency-code pairs from a telemetry data file')

	# add positional argument for the input position in the Fibonacci sequence
	parser.add_argument("watermelon.gff", help="contents of watermelon.gff file")
	parser.add_argument("watermelon.fsa", help="contents of watermelon.fsa")

	# parse the arguments
	return parser.parse_args()

def parse_fasta():
with open(fasta_file, 'r') as tags:
line_counter = 1
for line in fasta_file:
	if line_counter == 2:
		sequence = line.rstrip('\n')
	line_counter += 1

def parse_gff():
with gff = open(gff_file, 'r')
for line in gff:

	line = line.rstrip('\n')
	fields = line.split('\t')
	coordinates = line.(fields[3], fields[4])
    return coordinates

 def gc_content():   

 for line in coordinates:
    positions = line.split('\t')
    substring = fasta_file
    print(substring)
    output.write(substring)

def reverse(substring): 
    string = string[::-1] 
    return string 
print(reverse(string))

args = get_args()

if __name__ == "__main__":
	main()    

