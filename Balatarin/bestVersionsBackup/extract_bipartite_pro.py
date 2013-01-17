 # Program that extracts the users and links of a particular category and writes them to a new file
# Two files:
# links-summary.txt
# votes-summary.txt
# FORM:
# links-summary.txt
# id, user_id, category_id, mediatype_id, points, created_at 
# id: the link id
# Examples:
# 1000001	2	2	1	8	2006-08-14 21:06:19
# 1000002	2	4	4	16	2006-08-14 21:07:10
# votes-summary.txt
# id, link_id, user_id, sign, vote_reason_id, created_at
# link_id: the "id" of links-summary.txt
# user_id: will be used to construct bipartite graph
# 1	1000001	2	1	\N	2006-08-14 21:08:55
# 2	1000001	4	1	\N	2006-08-14 21:51:04
import time
import sys
import datetime
sDelta = sys.argv[1]  # start date from first
eDelta = sys.argv[2]  # in days
# start (s) end (e)
first = datetime.date(2006,8,14)
startDate = first + datetime.timedelta(days=int(sDelta))
endDate = startDate + datetime.timedelta(days=int(eDelta))

print startDate
PATH = "/media/data2/roja/Balatarin"
sDate = startDate.isoformat().split('T')[0].split('-')
eDate = endDate.isoformat().split('T')[0].split('-')
bgraphname = "bipartite_politics_"+sDate[1]+sDate[2]+sDate[0]+'-'+eDate[1]+eDate[2]+eDate[0]
l = open(PATH+"/data/links-politics.txt","r")
v = open(PATH+"/data/votes-summary.txt","r")
h = open(PATH+"/CompleteRun/bipartite/"+bgraphname+".txt","w")
print "1"
links = []
for line in l:
	year = int((line.split()[5]).split("-")[0]) 
	month = int((line.split()[5]).split("-")[1])
	day = int(line.split()[5].split("-")[2])
	date = datetime.date(year,month,day)
	if date > endDate: continue
	if date < startDate: continue
	linkID = line.split()[0]   
	links.append(linkID)	
print len(links)," articles"
#############################################################
print "2"
links_set = set(links) 					
graph_list = []                         # A list of tuples
for line in v:
	year = int((line.split()[5]).split("-")[0]) 
	month = int((line.split()[5]).split("-")[1])
	day = int(line.split()[5].split("-")[2])
	date = datetime.date(year,month,day)
	if date > endDate: continue
	if date < startDate: continue
	link_id = line.split()[1]               # id = link_id
	if link_id in links_set:
		graph_list.append((line.split()[2],link_id))   # (user_id, link_id)
graph_list.sort() 					# sorts by user_id
N = len(graph_list)
print N," votes"
for i in range(N):
	h.write(graph_list[i][0]+" "+graph_list[i][1]+"\n")
# Writes an edge list of users to link_id in a separate text file
h.close()
v.close()
l.close()
#############################################################
