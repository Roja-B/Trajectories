# Unipartite Projection 
#
# Creates Unipartite graph using cosine similarity from a bipartite graph 
# Input: Bipartite Graph
# 	Form: "User Link"
#
#Read lines and fit data into tuple format.
#[(user_id, [links that user voted on])]
#a list of tuples

import math
import time
import os
def intersect(a,b):
	return list(set(a) & set(b))

def union(a,b):
	return list(set(a) | set(b))
	
def nCr(n,r):
	f = math.factorial
	return f(n) / f(r) / f(n-r)


startYear =  int(sys.argv[1])
startMonth = int(sys.argv[2])
endYear = int(sys.argv[3])
endMonth = int(sys.argv[4])



#startYear =  int(raw_input("Enter start year: "))
#startMonth = int(raw_input("Enter start month: "))
#endYear = int(raw_input("Enter end year: "))
#endMonth = int(raw_input("Enter end month: "))

bgraphname = "bipartite_politics_"+str(startMonth)+"_"+str(startYear)+"-"+str(endMonth)+"_"+str(endYear)
ugraphname = "unipartite_politics_"+str(startMonth)+"_"+str(startYear)+"-"+str(endMonth)+"_"+str(endYear)

t1 = time.time()
coefficient = 100
voteThreshold = 5
sigDigit = 4
PATH = "Bipartite/"
f = open(PATH+bgraphname+".txt","r")
h = open(ugraphname+"_"+str(voteThreshold)+".txt","a")
u = open(ugraphname+"_"+str(voteThreshold)+"_stats.txt","a")

user_link = []
seen_users = []
tempLinks = []
t = -1 # Tuple Tracker
numElimination = 0
for line in f:
	uid = int(line.split()[0])
	lid = int(line.split()[1])
	if uid not in set(seen_users):
		if t >= 0:
			if len(tempLinks[1]) > voteThreshold:
				user_link.append((tempLinks[0],tempLinks[1]))
				tempLinks = []
				t = t+1
#				print t
			else:
#				print "Successful Elimination"
				numElimination = numElimination+1
				tempLinks = []
		else:
			t = t+1 # Only for first line of data
		tempLinks.append(uid)
		tempLinks.append([lid])	
		seen_users.append(uid)
	else:
		tempLinks[1].append(lid)

if t >= 0:
	if len(tempLinks[1]) > voteThreshold:
		user_link.append((tempLinks[0],tempLinks[1]))
		tempLinks = []
		t = t+1
		print t
	else:
#		print "Successful Elimination"
		numElimination = numElimination+1
		tempLinks = []
else:
	print "This shouldn't happen"

print "Loading Complete"

seen_users = [] # Clear memory
f.close()

zeros = 0.0
edges = 0.0
totalUsers = len(user_link)

for i in range(t+1):
	for j in range(i+1,t+1):
		try:
			weight = coefficient*round(float(len(intersect(user_link[i][1],user_link[j][1])))/float(len(union(user_link[i][1], user_link[j][1]))),sigDigit)
		except:
			print "weight did not compute"
			break
		if weight == 0.0:
			zeros = zeros+1
#			print "zeroed"
			continue
		h.write(str(user_link[i][0])+' '+str(user_link[j][0])+' '+str(weight)+'\n')
		edges = edges+1
		print str(i) + "/" + str(totalUsers) #Gives rough estimate on progress of code.

t2 = time.time()
combinations = nCr(totalUsers,2)
perZeros = zeros/combinations*100
perEdges = edges/combinations*100
print "There were "+str(numElimination) +" eliminations with a minimum threshold of "+str(voteThreshold)+" votes."
print "Coefficient multiplier for Jaccard Index: "+str(coefficient)
print "There are "+str(totalUsers)+" valid voters."
print "_______________________________"		
print "Total possible combinations between each user pair: "+str(combinations)
print "Total number of edges: " + str(int(edges))+ " | "+str(round(perEdges,2))+" Percent"
print "Total number of zeros: " + str(int(zeros))+ " | "+str(round(perZeros,2))+" Percent"
print "Runtime of Code: "+str((t2-t1)/60)+" minutes"

u.write("There were "+str(numElimination) +" eliminations with a minimum threshold of "+str(voteThreshold)+" votes.\n")
u.write("Coefficient multiplier for Jaccard Index: "+str(coefficient)+"\n")
u.write("There are "+str(totalUsers)+" valid voters.\n")
u.write("Total possible combinations between each user pair: "+str(combinations)+"\n")
u.write("Total number of edges: " + str(int(edges))+ " | "+str(round(perEdges,2))+" Percent\n")
u.write("Total number of zeros: " + str(int(zeros))+ " | "+str(round(perZeros,2))+" Percent\n")
u.write("Runtime of Code: "+str((t2-t1)/60)+" minutes\n")

u.close()
h.close()

################################################
################################################
