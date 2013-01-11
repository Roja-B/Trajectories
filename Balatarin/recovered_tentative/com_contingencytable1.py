#!/usr/lib/python3.0
''' This program creates matrices of transition probabilities between communities at different times.
The sorted timeline (also names of directories) of graphs is in U-pol_J100VT5_stats_combined.txt, the number of communities in each is in NumComsAndModularities'''
import string
import math
def intersect(a,b):
        return list(set(a) & set(b))
def union(a,b):
        return list(set(a) | set(b))
PATH = "./myResults"
prefix = ""
def contingency(dirname1,dirname2,numComs1,numComs2):
	PATH1 = PATH + '/' + dirname1
	PATH2 = PATH + '/' + dirname2
	filename = PATH+'/ComContingencyTable'+dirname1+'.txt'
	t = open(filename,"w")
	Cluster1 = [set() for i in range(numComs1+1)] # sets of programs in communities at time 1
	Cluster2 = [set() for i in range(numComs2+1)]
	X1 = set() # all the programs at time 1
	X2 = set()
	for i in range(numComs1):
		try: f = open(PATH1+'/community'+str(i),"r")
		except: 
			print PATH1,'/community',str(i)," does not exist (community too small)."
			continue
		for line in f: # populate set with uprograms
			program = line.strip()
			Cluster1[i].add(program)
		X1 = X1 | Cluster1[i] 
		f.close()
	for i in range(numComs2):
       		try: f = open(PATH2+'/community'+str(i),"r")
                except:
                        print PATH2,'/community',str(i)," does not exist (community too small)."
                        continue
	        for line in f:
        	        program = line.strip()
                	Cluster2[i].add(program)
		X2 = X2 | Cluster2[i]
		f.close()
#	Cluster1[numComs1] = X2-X1
#	Cluster2[numComs2] = X1-X2
#	for i in range(numComs1+1):
#                for j in range(numComs2+1):
	# create contingency table
	for i in range(numComs1):
		for j in range(numComs2):
			index = len(intersect(Cluster1[i],Cluster2[j]))
			t.write(str(index)+'\t')
		t.write('\n')
#	print len(X1-X2)
#	print len(X2-X1)
	t.close()
	return filename
def transitionProb(date,contingencyfilename):
	f = open(contingencyfilename,"r")
	n_t1 = []
	n_t2 = []
	n = []
	i = 0
	for line in f:
       		line = line.strip()
	        n.append([])
        	n[i] = line.split("\t")
        	i += 1
	M1 = len(n) # no. of communities in clustering1
	M2 = len(n[0]) # no. of communities in clustering2
	sum_all = 0
	for i in range(M1):
	        n_t1.append(0)
	        for j in range(M2):
                	sum_all += int(n[i][j])
        	        n_t1[i] += int(n[i][j])
	for j in range(M2):
        	n_t2.append(0)
	        for i in range(M1):
        	        n_t2[j] += int(n[i][j])
#print n_t1
#print n_t2
	N = sum(n_t1)
	p = []
	for i in range(M1):
        	p.append([])
        	if n_t1[i] == 0 : 
			for j in range(M2):
				p[i].append(0)
			continue
	        for j in range(M2):
        	        p_t1 = float(n_t1[i])/N
	                p_t2 = float(n_t2[j])/N
                	joint_p = float(n[i][j])/sum_all
        	        p[i].append(round(joint_p/p_t1,3))
	print p
        t = open(PATH+"/TrProbs"+date,"w")
	for i in range(M1):
		for j in range(M2):
        		t.write(str(p[i][j])+'\t')
		t.write('\n')
        t.close()
#----------- main() ---------------
graphDates = []
f = open("Work/U-pol_J100VT_stats.txt","r")
for line in f:
        graphDate = line.split(" ")[0]
        numNodes = int(line.split(" ")[1])
        if numNodes <= 3 :continue # this is because com-finding fails for a graph with 3 nodes or less
        graphDates.append(graphDate)
f.close()
print graphDates
graphs = dict()
f = open("Work/NumComsAndModularities_betterformat","r")
for line in f:
        graphDate = line.split("\t")[0]
	print graphDate
        numComs = line.split("\t")[1]
        graphs[graphDate] = numComs
f.close()
for year in range(2000,2013-SLIDE):
#	print date1, date2
        dirname1 = ''.join([PATH,"/",str(year),str(year+SLIDE)])
	dirname2 = ''.join([PATH,"/",str(year+1),str(year+1+SLIDE)])
	num1 = int(graphs[graphDates[i]])
	num2 = int(graphs[graphDates[i+1]])
	print date1,num1
	print date2,num2 
	contingencyfilename = contingency(dirname1,dirname2,num1,num2)
	#rand(date1,contingencyfilename)
	transitionProb(date1,contingencyfilename)
