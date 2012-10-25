 # Program that extracts the users and links of a particular category and writes them to a new file
# Two files:
# links-summary.txt
# votes-summary.txt
#
# FORM:
# links-summary.txt
# id, user_id, category_id, mediatype_id, points, created_at 
# id: the link id
# Examples:
# 1000001	2	2	1	8	2006-08-14 21:06:19
# 1000002	2	4	4	16	2006-08-14 21:07:10
#
# votes-summary.txt
# id, link_id, user_id, sign, vote_reason_id, created_at
# link_id: the "id" of links-summary.txt
# user_id: will be used to construct bipartite graph
# 1	1000001	2	1	\N	2006-08-14 21:08:55
# 2	1000001	4	1	\N	2006-08-14 21:51:04

import time
import sys

startYear =  int(sys.argv[1])
startMonth = int(sys.argv[2])
endYear = int(sys.argv[3])
endMonth = int(sys.argv[4])
#raw_input("Enter start year: "))
#startMonth = int(raw_input("Enter start month: "))
#endYear = int(raw_input("Enter end year: "))
#endMonth = int(raw_input("Enter end month: "))

PATH = ""
bgraphname = "bipartite_politics_"+str(startMonth)+"_"+str(startYear)+"-"+str(endMonth)+"_"+str(endYear)
l = open(PATH+"links-politics.txt","r")
v = open(PATH+"votes-summary.txt","r")
h = open(PATH+bgraphname+".txt","a")

t1 = time.time()

links = []
for line in l:
	year = int((line.split()[5]).split("-")[0]) 
	if year < startYear: continue
	if year > endYear: continue
	month = int((line.split()[5]).split("-")[1])
	if year == startYear and month < startMonth: continue
	if year == endYear and month > endMonth: continue
#	if line.split()[2]!= categoryID: continue	
	linkID = line.split()[0]   
	#if linkID in links: continue
	links.append(linkID)

print "Links Extraction Complete"	

#############################################################

links_set = set(links) 					# Just in case...
graph_list = []                         # A list of tuples

n = len(links)
for line in v:
	id = line.split()[1]
	if id in links_set:
		graph_list.append((line.split()[2],id))

# Sorts by user ID			
graph_list.sort()

print "Now Writing"

N = len(graph_list)
for i in range(N):
	h.write(graph_list[i][0]+" "+graph_list[i][1]+"\n")

t2 = time.time()

print str(t2-t1)

# Writes an edge list of users to link_id in a separate text file
h.close()
v.close()
h.close()

#############################################################
