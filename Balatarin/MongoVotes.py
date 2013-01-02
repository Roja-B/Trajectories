#!/usr/lib/python3.0

# This program enters Balatarin votes in MongoDB database called Balatarin. 

# Author: Roja Bandari
# October 2012

#
# FORM:
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
votes = balatarindb.votes

f = open(DATAPATH+"/votes-summary.txt","r")
log = open("mongoError.log","a")

i = 0
for line in f:
     line = line.strip()
     voteID = line.split('\t')[0]
     linkID = line.split('\t')[1]
     userID = line.split('\t')[2]
     sign = line.split('\t')[3]
#     reason = line.split('\t')[4]
     createdAT = line.split('\t')[5].split(' ')[0]    
     # example: 2006-08-14 21:51:04
     year = int(createdAT.split("-")[0]) 
     month = int(createdAT.split("-")[1]) 
     day = int(createdAT.split("-")[2]) 
     date = datetime.datetime(year,month,day)
	
     new_record = [{ "voteID" : voteID,
     "linkID" : linkID,
     "userID" :userID,
     "sign" : sign,
     "date":date}]
     votes.insert(new_record) 
     i+=1

print "Total entries procesed = " + str(i)
f.close()
log.close()
