#!/usr/lib/python3.0
''' This program creates rows of the contingency table of links vs. communities.'''
import sys
PATH = sys.argv[1]
dirname = sys.argv[2]
PATH = PATH+'/'+dirname
#PATH = "./ResultsJaccard30day14slide/"+dirname
M = int(sys.argv[3])
#PATH = raw_input('Enter data path: ')
#M = int(raw_input('Enter the number of communities: '))
try:
	f = open(PATH+'/links.txt',"r")
	t = open(PATH+'/contingencyTable.txt',"w")
	w = open(PATH+'/linkVoteCounts.txt',"w")
except:
	print 'error opening file'
# read all users into a hash table and save their memberships
Membership = {}
for i in range(0,M):
#	c = open(PATH+'/VertexCommemberships'+str(i),"r")
	try:
       		c = open(PATH+'/community'+str(i),"r")
	except: 
		print "could not find community"+str(i)
		continue
	for line in c:
		user = line.strip()
		Membership[user] = i
for line in f:
	community = [0]*M
	link = line.split(' ')[0]
	users = line.split(' ')
	users.remove('\n')
	users.remove(link)
	for user in users:
		try:
			memb = int(Membership[user])
			community[memb] += 1
		except:
			continue
	if sum(community) == 0: continue 
	w.write(str(sum(community))+'\n')
	t.write(link)
	for i in range(0,M):
		t.write('\t'+str(community[i]))
	t.write('\n')
t.close()
f.close()
w.close()
