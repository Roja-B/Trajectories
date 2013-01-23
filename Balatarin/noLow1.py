# This program reads top links for each community and excludes any that have less than 10 votes
import sys,string
PATH = sys.argv[1]
dirname = sys.argv[2]
PATH = PATH+'/'+dirname
M = int(sys.argv[3])
print PATH
try:f = open(PATH+"/RelevantLinks/contingencyTable.txt","r")
except: print PATH
linkvotes = dict()
for line in f:
        line = line.strip()
        linkID = line.split("\t")[0]
        line = string.replace(line, linkID,"").strip()
        numvotes = 0
        for element in line.split("\t"): numvotes += int(element)
        linkvotes[linkID] = numvotes
f.close()
for i in range(0,M):
        f1 = open(PATH+"/RelevantLinks/top50Links"+str(i),"r")
        t1 = open(PATH+"/RelevantLinks/NoLowTop10Links"+str(i),"w")
        count = 0
        for line1 in f1:
                if count == 10: break
                line1 = line1.strip()
                linkID = line1.split(" ")[1]
                if linkvotes[linkID] < 10: continue
                else:
                        print "good link:",linkvotes[linkID]
                        t1.write(line1+'\n')
                        count += 1
        f1.close()
        t1.close()

