from simulation import go
import re
import Bio
# import biopython libraries


def main():
    # 1) Read in chr22.fa using biopython

    from Bio.seq import SeqIO
    directory = "../genomes"
    genomeFile=directory+"/chr22.fa"
    record = SeqIO.read(genomeFile, "FASTA")
    
    # 2) Generate a simulated sequence s using go()
    k = 5
    length = len( str(record))
    practice = list()
    genome = list(record.seq)
    # go(record, k, length)
    for l in length:
        practice.append(random.sample(['A','G','C','T'], 1))

    
    # 3) Read in chr22.fa.out  (using re.split("\s+", line))
    repeatFile =directory+"/chr22.fa.out"
    with open(repeatFile,'w') as repeatRec:
        for line in repeatRec:
            line = line.rstrip()
            toks = re.split("\s+", line)
            start,end = int(toks[5]), int(toks[6])
            practice[start:end] = genome[start:end]
    practice = Seq("".join(practice))
            
    # 4) Start replacing portions of s with portions of chr22.fa as dictated by lines of chr22.fa.out  
    
    # (might combine (3) and (4) into one loop)
    # 5) Write simulated sequence to new file using biopython
    output_handle = open ("exampleFasta.fasta", "w")
    SeqIO.write(newString, output_handle, "fasta")

if __name__ == "__main__":
    main()
