#!/usr/lib/python3.0
''' (uses hash table) This program groups together all the users who voted (positive) for a specific link and lists them in front of the link_id. Output looks like this:
link_id user1_id user2_id user3_id ... etc.
later addition: remove high-degree users (high degree users ids are given in a file "high_deg_users.txt")'''
import sys
PATH = sys.argv[1]
dirname = sys.argv[2]
PATH = PATH+'/'+dirname
#PATH = "./ResultsJaccard30day14slide/"+dirname
#PATH = "./test/"+dirname
#PATH = raw_input('Enter data path: ')	
from collections import defaultdict
try:
	f = open(PATH+"/bipartite.txt","r")
	# h = open("high_deg_users.txt","r").read()
	t = open(PATH+'/links.txt',"w")
except:
	print 'error opening file'
k = 0
Links = defaultdict(list)
link = 0
for line in f:
	k +=1
	user = line.split(' ')[0]
	if int(user)>1000000 : print user
	link = line.split(' ')[1].strip()
	# vote = line.split('\t')[2]
	# for negative votes:
	# if int(vote)>0: continue	
	# for positive votes:
#	if int(vote)<1:	continue
	# if ' '+user+' ' in h: continue
        Links[link].append(user)
for key in Links:
	t.write(key+' ')
	users = Links[key]
	for u in users:
		t.write(u+' ')
	t.write('\n')
#	print k
#	if k>= 10000:
#		break
t.close()
f.close()

