#!/usr/lib/python3.0

# This program enters Balatarin links in MongoDB database called Balatarin. 

# Author: Roja Bandari
# October 2012

#
# FORM:
# links-summary.txt
# id, user_id, category_id, mediatype_id, points, created_at 
# id: the link id
# Examples:
# 1000001       2       2       1       8       2006-08-14 21:06:19
# 1000002       2       4       4       16      2006-08-14 21:07:10
#
# votes-summary.txt
# id, link_id, user_id, sign, vote_reason_id, created_at
# link_id: the "id" of links-summary.txt
# user_id: will be used to construct bipartite graph
# 1     1000001 2       1       \N      2006-08-14 21:08:55
# 2     1000001 4       1       \N      2006-08-14 21:51:04


from pymongo import Connection
from PARAMETERS import *
import datetime


connection = Connection()
balatarindb = connection.Balatarin
links = balatarindb.link

f = open(DATAPATH+"/links-summary.txt","r")
log = open("mongoError.log","a")

i = 0
for line in f:
     line = line.strip()
     linkID = line.split('\t')[0]
     userID = line.split('\t')[1]
     category = line.split('\t')[2]
     mediatype = line.split('\t')[3]
     votes = int(line.split('\t')[4])
     createdAT = line.split('\t')[5].split(' ')[0]    
     # example: 2006-08-14 21:51:04
     year = int(createdAT.split("-")[0]) 
     month = int(createdAT.split("-")[1]) 
     day = int(createdAT.split("-")[2]) 
     date = datetime.datetime(year,month,day)
	
     new_record = [{ "linkID" : linkID,
                             "userID" :userID,
                             "category" : category,
                             "mediatype" : mediatype,
                             "votes" : votes,
                             "date":date}]
     links.insert(new_record) 
     i+=1

print "Total entries procesed = " + str(i)
f.close()
log.close()
