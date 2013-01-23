#!/usr/lib/python3.0

'''create the table of expected values between links and communities'''
import sys
PATH = sys.argv[1]
dirname = sys.argv[2]
PATH = PATH+'/'+dirname
#PATH = "./ResultsJaccard30day14slide/"+dirname
M = int(sys.argv[3])


#PATH = raw_input('Enter data path: ')
#M = int(raw_input('Enter the number of communities: '))

try:
	r = open(PATH+'/communityVoteCounts.txt',"r")
	s = open(PATH+'/linkVoteCounts.txt',"r")
	t = open(PATH+'/ExpectedVotes.txt',"w")
except:
	print 'error opening file'

ComVotes = []
LinkVotes = []
for line in r:
	ComVotes.append(int(line))
r.close()
for line in s:
	LinkVotes.append(int(line))
s.close()
if sum(ComVotes) != sum(LinkVotes): print "Warning: votes don't add up!\n"
print sum(ComVotes)
print sum(LinkVotes)
N = sum(ComVotes)
for linkvote in LinkVotes:
	for comvote in ComVotes:
		t.write(str(round(float(comvote)*float(linkvote)/float(N),5))+'\t')
	t.write('\n')
	
t.close()
r.close()
s.close()
