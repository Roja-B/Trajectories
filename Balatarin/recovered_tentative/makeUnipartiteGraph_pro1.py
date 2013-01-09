#"! 
############################################################################
t.close()
h.close()
v.close()
h.close()
# Writes an edge list of users to link_id in a separate text file
print "Time Spent: "+str((t2-t1)/60)+" minutes.\n"
t2 = time.time()
	h.write(graph_list[i][0]+" "+graph_list[i][1]+"\n")
for i in range(N):
N = len(graph_list)
print "Now Writing"
graph_list.sort() 					# sorts by user_id
		t.write(line.split()[5]+"\n")
		graph_list.append((line.split()[2],id))   # (user_id, link_id)
	if id in links_set:
	id = line.split()[1]               # id = link_id
	if date < startDate: continue
	if date > endDate: continue
	date = datetime.date(year,month,day)
	day = int(line.split()[5].split("-")[2])
	month = int((line.split()[5]).split("-")[1])
	year = int((line.split()[5]).split("-")[0]) 
for line in v:
graph_list = []                         # A list of tuples
links_set = set(links) 					
#############################################################
print "Relevant Links Extracted"	
	links.append(linkID)
	linkID = line.split()[0]   
	if date < startDate: continue
	if date > endDate: continue
	date = datetime.date(year,month,day)
	day = int(line.split()[5].split("-")[2])
	month = int((line.split()[5]).split("-")[1])
	year = int((line.split()[5]).split("-")[0]) 
for line in l:
links = []
t1 = time.time()
t = open(PATH+"date_check.txt","w")
h = open(PATH+"bipartite/"+bgraphname+".txt","w")
v = open(PATH+"data/votes-summary.txt","r")
l = open(PATH+"data/links_summary_politics.txt","r")
#"+str(eMonth)+"_"+str(eDay)+"_"+str(eYear)
bgraphname = "bipartite_politics_"+str(sMonth)+"_"+str(sDay)+"_"+str(sYear)+"_"+delta+"_days"
PATH = "/media/data3/roja/"
#endMonth = int(raw_input("Enter end month: "))
#endYear = int(raw_input("Enter end year: "))
#startMonth = int(raw_input("Enter start month: "))
#raw_input("Enter start year: "))
#endMonth = int(sys.argv[4])
#endYear = int(sys.argv[3])
#startMonth = int(sys.argv[2])
#startYear =  int(sys.argv[1])
endDate = startDate + difference
difference = datetime.timedelta(days=int(delta))
startDate = datetime.date(sYear,sMonth,sDay)
sDay = int(sDate.split('/')[1])
sMonth = int(sDate.split('/')[0])
sYear = int(sDate.split('/')[2])
# start (s) end (e)
delta = sys.argv[2]  # in days
sDate = sys.argv[1]
import datetime
import sys
import time
# 2	1000001	4	1	\N	2006-08-14 21:51:04
# 1	1000001	2	1	\N	2006-08-14 21:08:55
# user_id: will be used to construct bipartite graph
# link_id: the "id" of links-summary.txt
# id, link_id, user_id, sign, vote_reason_id, created_at
# votes-summary.txt
# 1000002	2	4	4	16	2006-08-14 21:07:10
# 1000001	2	2	1	8	2006-08-14 21:06:19
# Examples:
# id: the link id
# id, user_id, category_id, mediatype_id, points, created_at 
# links-summary.txt
# FORM:
# votes-summary.txt
# links-summary.txt
# Two files:
 # Program that extracts the users and links of a particular category and writes them to a new file
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
voteThreshold = 0 
sigDigit = 4
PATH = "/media/data3/roja/Balatarin/"
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
for i in range(numUsers):
	for j in range(i+1,numUsers):
		u1 = user_links.keys()[i]
		u2 = user_links.keys()[j]
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
#		print str(i+1)+"/"+str(numUsers)
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
################################################
