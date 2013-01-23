import sys
PATH = "/media/data3/roja/Balatarin/CompleteRun/Results"
START_TIME =sys.argv[1]
f1 = open(PATH+"/EvolutionPaths"+str(START_TIME),"r")
#f1 = open(PATH+"/Results/EvolutionPaths4","r")
lines2 = open("../../forAnsuya/CommunityTopicBalatarin.txt").readlines()
t = open(PATH+"/EvolutionPaths_Topics"+START_TIME,"w")
for line in f1:
	if line.strip() =="" or "*" in line: 
		t.write(line)
		continue
	line = line.strip()
	dates = line.split("\t")[0].split("-")[0]
#	print dates
	community = line.split('\t')[1]
	for line2 in lines2:
		line2 = line2.strip()
		if line2 == "":continue
#		print line2.split("\t")
#		print community, line2.split('\t')[1]
		dates2 = line2.split('\t')[0]
		if dates2[4:12] == dates:
			print dates,dates2[4:12]
			print community, line2.split('\t')[1]
			if line2.split('\t')[1] == community:
				try:print line2.split('\t')[2]
				except:continue
				t.write(line+"\t" + line2.split('\t')[2]+'\n')
f1.close()
t.close()
# This program takes matrices of transition probabilities (between two consecutive temporal windows) and creates lines where each line is a list of next most probably communities for each community at time ti.
import os
PATH = "./Results"
def consecutiveComs(filename):
	f = open(filename, "r")
	nextComs = []
	maxprobs = []
	for line in f:
	        line = line.strip()
        	probs = [float(p) for p in (line.split('\t'))]
#		print probs
		m = max(probs)
		nextComs.append([i for i, j in enumerate(probs) if j == m])
		maxprobs.append(m)
	print nextComs
	print maxprobs
	return [maxprobs,nextComs]
