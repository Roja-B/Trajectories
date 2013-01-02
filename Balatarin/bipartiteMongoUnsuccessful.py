#!/usr/lib/python3.0

# This program extracts bipartite edgelist of users and links belonging to a specific time window (both the link and the votes should come from that time window) 

# Author: Roja Bandari
# October 2012



from pymongo import Connection
from PARAMETERS import *
import datetime
import time
import sys

n_slide = 14
n_delta = 30
difference = datetime.timedelta(days=n_delta)
slide = datetime.timedelta(days=n_slide)
#sDate = sys.argv[1]
#delta = sys.argv[2]  # in days
#sYear = int(sDate.split('/')[2])
#sMonth = int(sDate.split('/')[0])
#sDay = int(sDate.split('/')[1])

#startDate = datetime.datetime(sYear,sMonth,sDay)
#difference = datetime.timedelta(days=int(delta))
#endDate = startDate + difference
#print startDate
#print endDate
t1 = time.time()

connection = Connection()
balatarindb = connection.Balatarin
links = balatarindb.links
votes = balatarindb.votes

log = open("mongoError.log","a")
f = open(PATH+"/bipartite/edgelistSortedPolitics.txt","w")


startDateList = []



for vote in votes.find().sort({"date"}):
     v_date = vote["date"]
     if v_date in startDateList :
          endDate = v_date + difference
          flag = False
          bgraphname = str.join(["bipartite_politics_",str(startDate.month),"_",str(startDate.day),"_",str(startDate.year),"_",delta,"_days\n"])
          f.write(bgraphname)


     link = links.find_one({"linkID":linkID})
     if link["date"] < startDate : continue
     if link["category"] == "4":
          f.write(vote["userID"]+'\t'+vote["linkID"]+'\n')

     
     if v_date >= endDate : 
          f.close()
          flag = True




#for vote in votes.find({"date":{"$gte":startDate,"$lt":endDate}}):
#     print vote["linkID"] 
#     linkID = vote["linkID"]
#     link = links.find_one({"linkID":linkID})
#     if link["date"] < startDate : continue
#     if link["category"] == "4":
#          f.write(vote["userID"]+'\t'+vote["linkID"]+'\n')
          
f.close()
log.close()

t2 = time.time()

print "Time Spent: "+str((t2-t1)/60)+" minutes.\n"

