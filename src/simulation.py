#!/usr/bin/python2.7
############################################################################
# simulation.py
# program for genertating simulated sequence using a kth order markov chain
# Written by: Jiajun Wang
# Date: Aug. 21, 2013
# Email: wangj29@miamioh.edu

import random
import argparse
from Bio import SeqIO

def ProbTuple(Mark,kmo):
    total = 0
    tlist=[0]*4
    for t in range(4):
        total += Mark[(kmo<<2)|t]
    if total == 0 :
        return [0,0,0,0]     
    probsum = 0
    for t in range(4):
        tlist[t] = probsum + Mark[(kmo<<2)|t]/float(total)
        probsum = tlist[t]
    return tlist
    
#return the index of the first base without 'N' in following it for k length 
def NextIndex(i,k):
    while i<len(inSeq) and inSeq[i]=='N':
        i+=1
    if i+k>=len(inSeq):
        return i
    
    if 'N' in inSeq[i:i+k+1]:
        while inSeq[i]!='N':
            i+=1
        return NextIndex(i,k)
    return i  
   
def Markov(k):
    Mark= [0]*(4**(k+1))   
    mask=(1<<((k+1)*2))-1
    t=0
    #get first k+1 subsequence
    i=NextIndex(0,k)
    for j in range(k+1):
        t=(t<<2) | fn[inSeq[i+j]]
    Mark[t] = 1
    #go through the whole seq
    i += k+1     
    while i<len(inSeq) : 
        if inSeq[i]=='N':
             i=NextIndex(i,k)
             if (i+k)>=len(inSeq):
                 break
             t=0
             for j in range(k+1):
                 t=(t<<2) | fn[inSeq[i+j]]
	     i += k+1 
        else:
             t = ((t<<2) | fn[inSeq[i]])& mask     
	     i += 1	     
        Mark[t] += 1   
        
    
    Klist=[[0,0,0,0]]*(4**k)  
    for KMOne in range(4**k):         
        Klist[KMOne] = ProbTuple(Mark,KMOne)
    return Klist       

fn={
    'A':0, 'a':0,
    'C':1, 'c':1,
    'G':2, 'g':2,
    'T':3, 't':3,
    'N':-1, 'n':-1
}
gn={
   0:'A',
   1:'C',
   2:'G',
   3:'T'
}


if __name__=='__main__':
    parser = argparse.ArgumentParser(description="Generate Simulated Sequence")
    parser.add_argument('seq',action='store',help="sequence fasta file")     
    parser.add_argument('-k',action='store',dest='k',type=int,default=5,help="order of Markov chain, default is 5")     
    parser.add_argument('-l','--length',action='store',dest='length',type=int,help="length of sequence, same as the orginal sequence by default") 
    parser.add_argument('-n','--name',action='store',dest='name',help="name of simulated sequence")
    args = parser.parse_args()
    k=args.k
    handle = open(args.seq)
    seq_record = SeqIO.read(handle,"fasta")
  
    inSeq=str(seq_record.seq).upper()
    if args.length:
        n = args.length
    else:
        n = len(inSeq)
    #Zero Marcov probabilities list
    total=0
    base_count={}
    for i in range(4):   
        base_count[i]=inSeq.count(gn[i])
        total += base_count[i]        
    plist_zero=ProbTuple(base_count,0)
    
    #generate #0 to #k-1 bases AND kth markov prob list
    sublist = plist_zero
    plist=[]
    key=0
    simSeqStr=''
    for i in range(1,k+1):          
          r,newBase = random.random(),0
          if sublist == [0,0,0,0]:
              sublist = plist_zero        
          while r > sublist[newBase]:
              newBase += 1      
          simSeqStr += gn[newBase]
          key = (key<<2) | newBase     
          plist = Markov(i)
          sublist=plist[key]

    #generate the rest sequence using kth Markov prob         
    mask=(1<<(k*2))-1
    for j in range(k,n):
        sublist=plist[key]
        r,newBase = random.random(),0
        if sublist == [0,0,0,0]:
            sublist = plist_zero        
        while r > sublist[newBase]:
            newBase+=1         
        simSeqStr += gn[newBase]       
        key = ((key<<2) | newBase)& mask 
    
    if args.name:
        seqName = args.name
    else :
        seqName = "SimSeq.fa" 
    fo=open(seqName,"w+");
    fo.write(">"+seqName[:seqName.find('.')]+"\n")        
    fo.write(simSeqStr)
    fo.close()
