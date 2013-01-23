####################################################
# This program creates a file (for each time window) including all the users in communities at a time window
# It will be used to find user dropout
import numpy,sys
PATH = sys.argv[1]
f=open(PATH+"/Work/NumComsAndModularities","r")
NumComs=dict()
# Read in directory names (corresponding to window dates) and number of communities per directory
for line in f:
        line = line.strip()
        dirname = line.split("\t")[0]
        NumComs[dirname] = int(line.split("\t")[1])
f.close()
for dirname in NumComs:
        print dirname
        tt = open(dirname+"/AllUsers","w")
        for n in range(NumComs[dirname]):
                try: f1 = open(dirname+"/community"+str(n),"r")
                except: continue
                #f2 = open(dirname+"/pageranks"+str(n),"r")
                #userPageranks = []
                #userIds = []
                for line in f1: tt.write(line)
                f1.close()
        tt.close()

