#This program takes two *.fa.out files and calculate the sensitivity at base-level 
#Typically, the first *.fa.out file is generated from a repeat finder tool and the second
#*.fa.out file is a corresponding output from RepeatMasker using RepBase
import sys

def mergeOverlap(L):
    """
    Input: A list of intervals sorted by start position.
    Output: A copy in which all overlaping intervals have been replaced with a spanning interval"""
    i,j=1,0
    newL=[L[0]]
    while i<len(L):
        if newL[j][1]>=L[i][0]:
            newL[j][1]=max(newL[j][1],L[i][1])
        else :
            newL.append(L[i])
            j += 1            
        i += 1

    return newL
        
def compareList(L1, L2):
    """
    Input: Two interval lists
    Output: A 4-tuple T
    * T[0]: Number of bases covered by L1 but not by L2
    * T[1]: Number of bases covered by L2 but not by L1
    * T[2]: Number of bases covered by L1
    * T[3]: Number of bases covered by L2
    """
    Tp=4*[0]
    L1.sort(key=lambda t: t[0])
    L2.sort(key=lambda t: t[0])

    L1=mergeOverlap(L1)
    L2=mergeOverlap(L2)
    
    Tp[2]=sum( [ T[1] - T[0] for T in L1] )
    Tp[3]=sum( [ T[1] - T[0] for T in L2] )
      
    len1=len(L1)
    len2=len(L2)
    i=0    #index of L1
    j=0    #index of L2
    end1=0 #flag of end of L1
    end2=0 #flag of end of L2

    while (not (end1 or end2)):                         
        
        l1=L1[i][0]
        r1=L1[i][1]
        l2=L2[j][0]
        r2=L2[j][1]        
        
        # if two intervals overlap
        if l1<r2 and l2<r1:
            if l1 > l2:
                Tp[1] += l1-l2
            elif l2 < l1:
                Tp[0] += l2-l1
                
            if r1 > r2 :
                L1[i][0] = r2
            elif r1 < r2:
                L2[j][0] = r1
            
        else: #if two intervals are disjoint
            if l1-r2>=0:
                Tp[1] += r2-l2                
            else:
                Tp[0] += r1-l1
                
        # increase i or j if possible
        if r1 <= r2:
            if i+1<len1:
                i += 1
            else:
                end1=1
        if r1 >= r2:
            if j+1<len2:
                j += 1
            else:
                end2=1   
    #end of while loop            
    # if one of the list ends, read the rest of the other list
    if not(end1 and end2):        
        if end1:
            Tp[1]+=sum([T[1] - T[0] for T in L2[j:]])
        if end2 :
            Tp[0]+=sum([T[1] - T[0] for T in L1[i:]])      
            
    return Tp

def readfile(file):
    List=[]    
    for i,line in enumerate(open(file)):
        if i>2:
            A = line.strip().split() 
            if A[8]!= 'C':
                begin = int(A[5])-1
                end   = int(A[6])
                List.append([begin,end])
    return List   
def main(file1,file2):
    
    L1=readfile(file1)
    L2=readfile(file2)
    T = compareList(L1,L2)
    TP = T[2]-T[0]
    
    print TP/float(T[3])
    
    print T

if __name__=="__main__":
    
    main(sys.argv[1],sys.argv[2])
