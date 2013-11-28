import simulation
import re
import Bio
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import random



def main(seq,k,length,n):
    # 1) Read in chr22.fa using biopython

    #  directory = "../genomes"
    #  genomeFile=directory+"/chr22.fa"
    #  record = SeqIO.read(genomeFile, "fasta")
    directory = "../genomes"
    genomeFile = directory+seq
    record = SeqIO.read(genomeFile, "fasta")

    # 2) Generate a simulated sequence s using go()
    # k = 5
    length = len( str(record))
    # newSeq = simulation.go(genomeFile,"chr22Snip.fa",k,length)
    # newSeq = simulation.go(genomeFile, "chr22.fa",k,length)
    newSeq = simulation.go(genomeFile, name, k, length)
    newSeq = list(newSeq)
    # 3) Read in chr22.fa.out  (using re.split("\s+", line))
    repeatFile =directory+"/chr22.fa.out"

    repeatRec = open(repeatFile,'r')
    repeatRec.readline()
    repeatRec.readline()
    repeatRec.readline()
    line = repeatRec.readline()
    line = line.rstrip()
    toks = re.split("\s+", line)
    print toks
    print line
    start,end = int(toks[6]), int(toks[7])
    newSeq[start:end] = list(record)[start:end]
    newSeq = Seq("".join(newSeq))
    print newSeq
    # 4) Start replacing portions of s with portions of chr22.fa as dictated by lines of chr22.fa.out  
    
    # (might combine (3) and (4) into one loop)
    # 5) Write simulated sequence to new file using biopython
   
    output_handle = open("newSeq.fasta", "w")
    record = SeqRecord(newSeq)
    SeqIO.write(record, output_handle, "fasta")

if __name__ == "__main__":
    # main()
   
    parser = argparse.ArgumentParser(description="Generate Simulated Sequence")
    parser.add_argument(\
        '--seq',action='store',required=False,
        help="sequence fasta file")     
    parser.add_argument(\
        '-k',action='store',dest='k',type=int,default=5,
        help="order of Markov chain, default is 5")     
    parser.add_argument(\
        '-l','--length',action='store',dest='length',type=int,
        help="length of sequence, same as the orginal sequence by default") 
    parser.add_argument(\
        '-n','--name',action='store',dest='name',
        help="name of simulated sequence

  main(seq,k,l,n)
   
