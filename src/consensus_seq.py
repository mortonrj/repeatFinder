#!/usr/bin/python2.7
############################################################################
# consensus_seq.py
# program for generating consensus sequences
# Written by: Rachael Morton

import random
import argparse
import unittest
import sys
import Bio
from Bio import Seq
from Bio import SeqIO
from collections import defaultdict

def get_consensus(elements_list, genome_string):
    family_length = int(elements_list[0][5])-int(elements_list[0][4])
    s = ""
    D = {'A':0,'C':0,'G':0,'T':0,'X':0}
    for column in range(family_length):
        for L in element_list:
            current_position = int(L[4]) + column
            base = genome_string[current_position]
            try:
                D[base] += 1
            except:
                D['X'] += 1
        best_base = max([(c,b) for b,c in D.items()])[1]
        s += best_base
    return s

def main(seq,elements):  
    
    # 1) Read in sequence using biopython
    genomeFile = seq
    record = SeqIO.parse(genomeFile, "fasta")
    genome_string = list(record)[0]
    
    # Opening elements file
    elementFile = elements
    f = open(elementFile, 'r')
    lines = [re.split("\s+", line.rstrip()) for line in f.readLines()]
    num_families = int(lines[-1][0]) + 1

    for family_num in range(0,num_families):
        results.append((family_num,
                        get_consensus([line for line in lines if int(L[0]) == family_num],genome_string)))

        
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "Generate Simulated Sequence")
    parser.add_argument(\
        '--seq',action='store',required=False,type=str,default="../genomes/chr22.fa",
        help="sequence fasta file")
    parser.add_argument(\
        '--elements',action='store',required=False,type=str,
        default="../repeatFinder/raider/raider_output/elements",
        help = "elements file")
    args = parser.parse_args()
    main(args.seq,args.elements)

