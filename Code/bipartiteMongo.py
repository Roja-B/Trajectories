#!/usr/lib/python3.0

# This program extracts bipartite edgelist of users and links belonging to a specific time window (both the link and the votes should come from that time window) 

# Author: Roja Bandari
# October 2012

from pymongo import Connection
from PARAMETERS import *
import datetime
import time
import sys
#sDate = sys.argv[1]
#delta = sys.argv[2]  # in days

#sYear = int(sDate.split('/')[2])
#sMonth = int(sDate.split('/')[0])
#sDay = int(sDate.split('/')[1])

begin = datetime.datetime(2006,9,1)
end = datetime.datetime(2010,11,25)
startDate = begin
difference = datetime.timedelta(days=WINDOW)
slidingWindow =  datetime.timedelta(days=SLIDE)
t1 = time.time()

connection = Connection()
balatarindb = connection.Balatarin
links = balatarindb.links
votes = balatarindb.votes
log = open("mongoError.log","a")
     
while startDate < end:
     endDate = startDate + difference
     bgraphname = "".join(["bipartite_politics_",str(startDate.month),"_"+str(startDate.day),"_"+str(startDate.year),"_"+str(WINDOW),"_days"])
     print bgraphname
     f = open(PATH+"/bipartite/"+bgraphname+".txt","w")

     for vote in votes.find({"date":{"$gte":startDate,"$lt":endDate}}):
     #     print vote["linkID"] 
          linkID = vote["linkID"]
          link = links.find_one({"linkID":linkID}) 
          try: 
               if link["date"] < startDate : continue
          except:
               log.write(linkID+'\n')
               continue 
          if link["category"] == "4":
               f.write(vote["userID"]+'\t'+vote["linkID"]+'\n')
               
     f.close()
     startDate += slidingWindow

t2 = time.time()
print "Time Spent: "+str((t2-t1)/60)+" minutes.\n"
log.close()
