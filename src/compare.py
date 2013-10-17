import glob
import os
import subprocess
import argparse
import shutil
#add tool name to toollist...
toollist=('piler','repeatscout')
parser = argparse.ArgumentParser(description="Run tools and compare results")
parser.add_argument('-piler',action='store_true',dest='piler',help='run piler')
parser.add_argument('-rs','--repeatscout',action='store_true',dest='repeatscout',help='run repeatscout')
parser.add_argument('-seq',action='store',dest='sequence',required=True,help='sequence file')
#parser.add_argument('-rmrb',action='store',dest='rmrb',required=True,help='*.fa.out file, RepeatMasker using Repbase')
#add tool options here ...

args= parser.parse_args()
args.tool=[x for x in toollist if getattr(args,x)==True]

if len(args.tool)==0:
    parser.error('No tool requested')
    parser.print_help()
    sys.exit(2)

    
#Tools running script
if args.piler:
    exe = "module load piler;"
    #stage one
    exe += "pals -self "+args.sequence+" -out hit.gff;"
    #stage two
    exe += "piler -trs hit.gff -out trs.gff;" 
    
    subprocess.call(exe,shell = True)
    
    #stage three
    exe = "module load piler;"
    os.mkdir("fams")
    exe += "piler -trs2fasta trs.gff -seq "+args.sequence+" -path fams"
    subprocess.call(exe,shell = True)
    os.mkdir("aligned_fams")
    os.chdir('fams')    
    for fam in glob.glob('*'):
        exe = "module load piler;"
        exe += "muscle -in "+fam+" -out ../aligned_fams/"+fam+" -maxiters 1 -diags1"
        subprocess.call(exe,shell = True)
    os.chdir(os.pardir)
    os.mkdir("cons")
    os.chdir("aligned_fams")    
    for fam in glob.glob('*'):
        exe = "module load piler;"
        exe += "piler -cons "+fam+" -out ../cons/"+fam+" -label "+fam
        subprocess.call(exe,shell = True)
    os.chdir(os.pardir)
    os.chdir("cons") 
    exe = "cat * > ../piler_library.fa;"
    subprocess.call(exe,shell = True)
    os.chdir(os.pardir)    
    shutil.rmtree('fams')
    shutil.rmtree('cons')
    shutil.rmtree('aligned_fams')
    
    
if args.repeatscout:
    exe = "module load repeatscout;"
    exe += "build_lmer_table -sequence "+args.sequence+" -freq freq_table;"
    exe += "RepeatScout -sequence "+args.sequence+"  -freq freq_table -output repscout.fa;"
    exe += "filter-stage-1.prl repscout.fa > filtered_repscout.fa;"
    subprocess.call(exe,shell = True)
    exe = "module load RepeatMasker;"
    exe += "RepeatMasker "+args.sequence+" -lib filtered_repscout.fa -pa 4;"
    subprocess.call(exe,shell = True)
    exe = "module load repeatscout;"
    exe += "cat filtered_repscout.fa | perl filter-stage-2.prl --cat="+args.sequence+".out  > repeatscout_library.fa;"
    subprocess.call(exe,shell = True)


#Run RepeatMasker on the libraries built by the tools
for tool in args.tool:
    exe = "module load RepeatMasker;"
    library = tool+"_library.fa"
    folder=tool+"_rmsk"
    os.mkdir(folder)
    exe += "RepeatMasker "+args.sequence+" -lib "+library+" -dir "+folder+" -pa 4;"
    subprocess.call(exe,shell = True)

#Compare the output from RepeatMasker(*.fa.out) to RMRB fa.out files. 'CompareResult.py' does this