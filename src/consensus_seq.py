#!/usr/bin/python2.7
############################################################################
# consensus_seq.py
# program for generating consensus sequences
# Written by: Rachael Morton

import argparse
import random
import argparse
import unittest
import sys
import Bio
from Bio import SeqIO
from collections import defaultdict

def main():
    
    # 1) Read in sequence using biopython
    directory = "../genomes"
    genomeFile = directory+"/"+seq
    record = SeqIO.read(genomeFile, "fasta")
    
    # Opening elements file
    elementFile = "../repeatFinder/raider/raider output/elements"
    f = open(elementFile, 'r')
    lines = repeatRec.readlines()
    t = dict()
    
    for i in range(1,len(lines)):
        
        repeatList
        line = lines[i]
        line = line.rstrip()
        toks = re.split("\s",line)
        number = toks[0]
        
        #Finding repeat section from chr22.fa based on elements coordinates
        start,end = int(toks[6]), int(toks[7])
        repeat = list(record)[start:end]
        
        #logging repeat in dictionary
        t[number] = repeat
        consensus(t)

def consensus(t):
    consensusList = dict()
    
    firstNumber = t[dict.keys()[0]]
    consensusList[firstNumber] = t[0]
    for number in t:
        if number == firstNumber:
            
        else:
            firstNumber == number
            consensusList[number] = t[number]



if __name__ == "__main__":

    main()

