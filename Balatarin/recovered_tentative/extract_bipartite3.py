# Program that extracts the users and links of a particular category and writes them to a new file
# Two files:
# links-summary.txt
# votes-summary.txt
# FORM:
# links-summary.txt
# id, user_id, category_id, mediatype_id, points, created_at 
# id: the link id
# Examples:
# 1000001       2       2       1       8       2006-08-14 21:06:19
# 1000002       2       4       4       16      2006-08-14 21:07:10
# votes-summary.txt
# id, link_id, user_id, sign, vote_reason_id, created_at
# link_id: the "id" of links-summary.txt
# user_id: will be used to construct bipartite graph
# 1     1000001 2       1       \N      2006-08-14 21:08:55
# 2     1000001 4       1       \N      2006-08-14 21:51:04
import time
import sys
import datetime
sDate = sys.argv[1]
eDate = sys.argv[2]
# start (s) end (e)
sYear = int(sDate.split('/')[2])
sMonth = int(sDate.split('/')[0])
sDay = int(sDate.split('/')[1])
eYear = int(eDate.split('/')[2])
eMonth = int(eDate.split('/')[0])
eDay = int(eDate.split('/')[1])
#startYear =  int(sys.argv[1])
#startMonth = int(sys.argv[2])
#endYear = int(sys.argv[3])
#endMonth = int(sys.argv[4])
#raw_input("Enter start year: "))
#startMonth = int(raw_input("Enter start month: "))
#endYear = int(raw_input("Enter end year: "))
#endMonth = int(raw_input("Enter end month: "))
PATH = "/media/data3/allen/"
bgraphname = "bipartite_politics_"+str(sMonth)+"_"+str(sDay)+"_"+str(sYear)+"-"+str(eMonth)+"_"+str(eDay)+"_"+str(eYear)
l = open(PATH+"processed_data/links_summary_politics.txt","r")
v = open(PATH+"raw_data/votes-summary.txt","r")
h = open(PATH+"bipartite/"+bgraphname+".txt","w")
t = open(PATH+"date_check.txt","w")
t1 = time.time()
links = []
for line in l:
        year = int((line.split()[5]).split("-")[0])
        if year < sYear: continue
        if year > eYear: continue
        month = int((line.split()[5]).split("-")[1])
        if year == sYear and month < sMonth: continue
        if year == eYear and month > eMonth: continue
        day = int(line.split()[5].split("-")[2])
        if year == eYear and month == eMonth and day > eDay: continue
        if year == sYear and month == sMonth and day < sDay: continue
        linkID = line.split()[0]
        links.append(linkID)
print "Relevant Links Extracted"
#############################################################
links_set = set(links)
graph_list = []                         # A list of tuples
for line in v:
        id = line.split()[1]               # id = link_id
        year = int((line.split()[5]).split("-")[0])
        if year < sYear: continue
        if year > eYear: continue
        month = int((line.split()[5]).split("-")[1])
        if year == sYear and month < sMonth: continue
        if year == eYear and month > eMonth: continue
        day = int(line.split()[5].split("-")[2])
        if year == eYear and month == eMonth and day > eDay: continue
        if year == sYear and month == sMonth and day < sDay: continue
        if id in links_set:
                graph_list.append((line.split()[2],id))   # (user_id, link_id)
                t.write(line.split()[5]+"\n")
graph_list.sort()
print "Now Writing"
N = len(graph_list)
for i in range(N):
        h.write(graph_list[i][0]+" "+graph_list[i][1]+"\n")
t2 = time.time()
print "Time Spent: "+str((t2-t1)/60)+" minutes.\n"
# Writes an edge list of users to link_id in a separate text file
h.close()
v.close()
h.close()
t.close()

