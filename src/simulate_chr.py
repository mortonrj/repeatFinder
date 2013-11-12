from simulation import go
import re
import Bio
# import biopython libraries


def main():
    # 1) Read in chr22.fa using biopython

    from Bio.seq import SeqIO
    directory = "../genomes"
    directory+"chr22.fa"
    record = SeqIO.read(directory, "FASTA")
    
    # 2) Generate a simulated sequence s using go()
    k = 5
    length = len( str(record))
    go(record, k, length)
    
    # 3) Read in chr22.fa.out  (using re.split("\s+", line))
    repeatRec = SeqIO.read(director, "FASTA")
    repeatRec("\s+", line)
    
    # 4) Start replacing porsions of s with porsions of chr22.fa as dictated by lines of chr22.fa.out  
    newString = record
    # (might combine (3) and (4) into one loop)
    # 5) Write simulated sequence to new file using biopython
    output_handle = open ("example.fasta", "w")
    SeqIO.write(newString, output_handle, "fasta")

if __name__ == "__main__":
    main()
