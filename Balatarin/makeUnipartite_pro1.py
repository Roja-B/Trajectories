u = open(PATH+"unipartite/"+ugraphname+"_"+str(voteThreshold)+"_stats.txt","w")
h = open(PATH+"unipartite/"+ugraphname+"_"+str(voteThreshold)+".txt","w")
f = open(PATH+"bipartite/"+bgraphname+".txt","r")
PATH = "/media/data3/allen/"
sigDigit = 4
voteThreshold = 5
coefficient = 100
t1 = time.time()
ugraphname = "unipartite_politics_"+str(sMonth)+"_"+str(sDay)+"_"+str(sYear)+"_"+delta+"_days"
bgraphname = "bipartite_politics_"+str(sMonth)+"_"+str(sDay)+"_"+str(sYear)+"_"+delta+"_days"
#bgraphname = "bipartite_politics_"+str(startMonth)+"_"+str(startYear)+"-"+str(endMonth)+"_"+str(endYear)
#endMonth = int(raw_input("Enter end month: "))
#endYear = int(raw_input("Enter end year: "))
#startMonth = int(raw_input("Enter start month: "))
#startYear =  int(raw_input("Enter start year: "))
endDate = startDate + difference
difference = datetime.timedelta(days=int(delta))
startDate = datetime.date(sYear,sMonth,sDay)
sDay = int(sDate.split('/')[1])
sMonth = int(sDate.split('/')[0])
sYear = int(sDate.split('/')[2])
# start (s) end (e)
delta = sys.argv[2]  # in days
sDate = sys.argv[1]
#endMonth = int(sys.argv[4])
#endYear = int(sys.argv[3])
#startMonth = int(sys.argv[2])
#startYear =  int(sys.argv[1])
	return f(n) / f(r) / f(n-r)
	f = math.factorial
def nCr(n,r):
import datetime
import sys
import os
import time
import math
#a list of tuples
#[(user_id, [links that user voted on])]
#Read lines and fit data into tuple format.
# 	Form: "User Link"
# Input: Bipartite Graph
# Creates Unipartite graph using cosine similarity from a bipartite graph 
# Unipartite Projection 
################################################
################################################
h.close()
u.close()
f.close()
u.write("Runtime of Code: "+str((t2-t1)/60)+" minutes\n")
u.write("Total number of zeros: " + str(int(zeros))+ " | "+str(round(perZeros,2))+" Percent\n")
u.write("Total number of edges: " + str(int(edges))+ " | "+str(round(perEdges,2))+" Percent\n")
u.write("Total possible combinations between each user pair: "+str(combinations)+"\n")
u.write("There are "+str(numUsers)+" valid voters.\n")
u.write("Coefficient multiplier for Jaccard Index: "+str(coefficient)+"\n")
# Unipartite Projection 
# Creates Unipartite graph using cosine similarity from a bipartite graph 
# Input: Bipartite Graph
# 	Form: "User Link"
#Read lines and fit data into tuple format.
#[(user_id, [links that user voted on])]
#a list of tuples
import math
import time
import os
import sys
import datetime
def nCr(n,r):
	f = math.factorial
	return f(n) / f(r) / f(n-r)
#startYear =  int(sys.argv[1])
#startMonth = int(sys.argv[2])
#endYear = int(sys.argv[3])
#endMonth = int(sys.argv[4])
sDate = sys.argv[1]
delta = sys.argv[2]  # in days
# start (s) end (e)
sYear = int(sDate.split('/')[2])
sMonth = int(sDate.split('/')[0])
sDay = int(sDate.split('/')[1])
startDate = datetime.date(sYear,sMonth,sDay)
difference = datetime.timedelta(days=int(delta))
endDate = startDate + difference
#startYear =  int(raw_input("Enter start year: "))
#startMonth = int(raw_input("Enter start month: "))
#endYear = int(raw_input("Enter end year: "))
#endMonth = int(raw_input("Enter end month: "))
#bgraphname = "bipartite_politics_"+str(startMonth)+"_"+str(startYear)+"-"+str(endMonth)+"_"+str(endYear)
bgraphname = "bipartite_politics_"+str(sMonth)+"_"+str(sDay)+"_"+str(sYear)+"_"+delta+"_days"
ugraphname = "unipartite_politics_"+str(sMonth)+"_"+str(sDay)+"_"+str(sYear)+"_"+delta+"_days"
t1 = time.time()
coefficient = 100
voteThreshold = 5
sigDigit = 4
PATH = "/media/data3/allen/"
f = open(PATH+"bipartite/"+bgraphname+".txt","r")
h = open(PATH+"unipartite/"+ugraphname+"_"+str(voteThreshold)+".txt","w")
u = open(PATH+"unipartite/"+ugraphname+"_"+str(voteThreshold)+"_stats.txt","w")
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
sortedKeys = user_links.keys().sort()
print sortedKeys
for i in range(numUsers):
	for j in range(i+1,numUsers):
		u1 = sortedKeys[i]
		u2 = sortedKeys[j]
		denom = float(len(set(user_links[u1]).union(set(user_links[u2]))))
		if denom == 0.0:
			continue
		num = float(len(set(user_links[u1]).intersection(set(user_links[u2]))))
		weight = coefficient*round(num/denom,sigDigit)
		if weight == 0.0:
			zeros = zeros + 1
			continue
		h.write(str(u1)+' '+str(u2)+' '+str(weight)+'\n')
		edges = edges+1
		# print str(i+1)+"/"+str(numUsers)
t2 = time.time()
combinations = nCr(numUsers,2)
perZeros = zeros/combinations*100
perEdges = edges/combinations*100
print "There were "+str(len(eliminations)) +" eliminations with a minimum threshold of "+str(voteThreshold)+" votes."
print "Coefficient multiplier for Jaccard Index: "+str(coefficient)
print "There are "+str(numUsers)+" valid voters."
print "_______________________________"		
print "Total possible combinations between each user pair: "+str(combinations)
print "Total number of edges: " + str(int(edges))+ " | "+str(round(perEdges,2))+" Percent"
print "Total number of zeros: " + str(int(zeros))+ " | "+str(round(perZeros,2))+" Percent"
print "Runtime of Code: "+str((t2-t1)/60)+" minutes"
u.write("There were "+str(len(eliminations)) +" eliminations with a minimum threshold of "+str(voteThreshold)+" votes.\n")
u.write("Coefficient multiplier for Jaccard Index: "+str(coefficient)+"\n")
u.write("There are "+str(numUsers)+" valid voters.\n")
u.write("Total possible combinations between each user pair: "+str(combinations)+"\n")
u.write("Total number of edges: " + str(int(edges))+ " | "+str(round(perEdges,2))+" Percent\n")
u.write("Total number of zeros: " + str(int(zeros))+ " | "+str(round(perZeros,2))+" Percent\n")
u.write("Runtime of Code: "+str((t2-t1)/60)+" minutes\n")
f.close()
u.close()
h.close()
################################################
