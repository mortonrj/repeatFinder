#!/usr/bin/python2.7

############################################################################
# redhawk.py
# Class for running raider on genome, creating consensus sequence for each family, 
# and running RepeatMasker with set of consensus sequences as library

import re, string, sys
import subprocess
import os
import argparse

def main(seqFile,outputDir):

    directory = "../genomes"
   
    #1) Running Raider
    subprocess.call(["./../raider/raider", "-v", "1110110111", directory + "/" + seqFile, 
                 outputDir])
    raiderResults = outputDir

    #2) Running RepeatMasker
    subprocess.call("module load RepeatMasker")
    subprocess.call(["RepeatMasker", "-el", "raiderResults"])
    

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Generate Simulated Sequence")
    parser.add_argument(\
        '--seqFile',action='store',required=False,type = str,default = "test.fa",
        help="sequence fasta file")
    parser.add_argument(\
        '-outputDir',action='store',type=str,default=5,
        help="output directory for raider results")
    args = parser.parse_args()
    main(args.seqFile,args.outputDir)
