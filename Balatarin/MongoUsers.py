#!/usr/lib/python3.0

# This program enters Balatarin users in MongoDB database called Balatarin. 

# Author: Roja Bandari
# October 2012

#
# FORM:
# users-summary.txt
# SELECT id, login, karma, created_at FROM users INTO OUTFILE 'users-summary.txt';

# user_id: will be used to construct bipartite graph
# 1	admin	110	2006-08-14 21:04:50



from pymongo import Connection
from PARAMETERS import *
import datetime


connection = Connection()
balatarindb = connection.Balatarin
users = balatarindb.users

f = open(DATAPATH+"/users-summary.txt","r")
log = open("mongoError.log","a")

i = 0
for line in f:
     line = line.strip()
     userID = line.split('\t')[0]
     userName = line.split('\t')[1]
     karma = line.split('\t')[2]
     createdAT = line.split('\t')[3].split(' ')[0]    
     # example: 2006-08-14 21:51:04
     year = int(createdAT.split("-")[0]) 
     month = int(createdAT.split("-")[1]) 
     day = int(createdAT.split("-")[2]) 
     date = datetime.datetime(year,month,day)
	
     new_record = [{ "userID" :userID,
     "userName" : userName,
     "karma" : karma,
     "date":date}]
     users.insert(new_record) 
     i+=1

print "Total entries procesed = " + str(i)
f.close()
log.close()
