# Unipartite Projection 
# Creates Unipartite graph using cosine similarity from a bipartite graph 
# Input: Bipartite Graph
# 	Form: "User Link"
#Read lines and fit data into tuple format.
#[(user_id, [links that user voted on])]
#a list of tuples
import math
import time
import sys
import datetime
def nCr(n,r):
	f = math.factorial
	return f(n) / f(r) / f(n-r)
coefficient = 100
voteThreshold = 5
sigDigit = 4
sDelta = sys.argv[1]  # start date from first
eDelta = sys.argv[2]  # in days
#dirName = sys.argv[3] # directory name in unipartite and in bipartite
first = datetime.date(2006,8,14)
startDate = first + datetime.timedelta(days=int(sDelta))
endDate = startDate + datetime.timedelta(days=int(eDelta))
sDate = startDate.isoformat().split('T')[0].split('-')
eDate = endDate.isoformat().split('T')[0].split('-')
bgraphname = "bipartite_politics_"+sDate[1]+sDate[2]+sDate[0]+'-'+eDate[1]+eDate[2]+eDate[0]
ugraphname = "U-pol_J"+str(coefficient)+"VT"+str(voteThreshold)+"_"+sDate[1]+sDate[2]+sDate[0]+'-'+eDate[1]+eDate[2]+eDate[0]
PATH = "/media/data2/roja/Balatarin/CompleteRun"
#f = open(PATH+"/bipartite/"+dirName+"/"+bgraphname+".txt","r")
#h = open(PATH+"/unipartite/"+dirName+"/"+ugraphname+".txt","w")
#u = open(PATH+"/unipartite/"+dirName+"/U-pol_J"+str(coefficient)+"VT"+str(voteThreshold)+"_stats.txt","a")
f = open(PATH+"/bipartite/"+bgraphname+".txt","r")
h = open(PATH+"/unipartite/"+ugraphname+".txt","w")
u = open(PATH+"/unipartite/"+"/U-pol_J"+str(coefficient)+"VT"+str(voteThreshold)+"_stats.txt","a")
seen_users = set()
user_links = {}     # Dictionary of user ids as keys
for line in f:
	uid = line.split()[0]
	lid = line.split()[1]
	if uid in seen_users:
		user_links[uid].append(lid)	
	else:
		user_links[uid] = [lid]
		seen_users.add(uid)
eliminations = []
seen_users.clear()
for i in range(len(user_links.keys())):
	tempID = user_links.keys()[i]
	if len(user_links[tempID]) <= voteThreshold:
		eliminations.append(tempID)
		continue
for i in range(len(eliminations)):
	del user_links[eliminations[i]]
zeros = 0.0
edges = 0.0
numUsers = len(user_links.keys())
for i in range(numUsers):
	for j in range(i+1,numUsers):
		u1 = user_links.keys()[i]
		u2 = user_links.keys()[j]
		denom = float(len(set(user_links[u1]).union(set(user_links[u2]))))
		if denom == 0.0:
			continue
		num = float(len(set(user_links[u1]).intersection(set(user_links[u2]))))
		weight = round(coefficient*(num/denom),sigDigit)
		if weight == 0.0:
			zeros = zeros + 1
			continue
		h.write(str(u1)+' '+str(u2)+' '+str(weight)+'\n')
		edges = edges+1
combinations = nCr(numUsers,2)
eDensity = round(edges/combinations,sigDigit)
print "There were "+str(len(eliminations)) +" eliminations with a minimum threshold of "+str(voteThreshold)+" votes."
#print "Coefficient multiplier for Jaccard Index: "+str(coefficient)
#print "There are "+str(numUsers)+" valid voters."		
#print "Total possible combinations between each user pair: "+str(combinations)
#print "Total number of edges: " + str(int(edges))+ " | "+str(round(perEdges,2))+" Percent"
#print "Total number of zeros: " + str(int(zeros))+ " | "+str(round(perZeros,2))+" Percent"
u.write(sDate[1]+sDate[2]+sDate[0]+'-'+eDate[1]+eDate[2]+eDate[0]+" "+str(int(numUsers))+" "+str(int(edges))+" "+str(eDensity)+"\n")
f.close()
u.close()
h.close()
################################################
################################################
