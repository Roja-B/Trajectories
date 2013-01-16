#!/usr/lib/python3.0
''' This program reads the contingency table and counts total number of votes by each community (K_Ci). The result is needed to compute table of expected values. '''
# 1575232	[0, 0, 1, 0]	1
# 1658496	[0, 0, 1, 0]	1
import sys
PATH = sys.argv[1]
dirname = sys.argv[2]
PATH = PATH+'/'+dirname
M = int(sys.argv[3])
#PATH = raw_input('Enter data path: ')
#M = int(raw_input('Enter the number of communities: '))
f = open(PATH+"/contingencyTable.txt","r")
t = open(PATH+"/communityVoteCounts.txt","w")
comVotes = [0]*M
for line in f:
#    votes_row = line.split('[')[1].split(']')[0]
    for i in range(0,M):
#        votes = votes_row.split(',')[i].strip()
        votes = line.split('\t')[i+1].strip()
        comVotes[i] += int(votes)
for i in range(0,M):
    t.write(str(comVotes[i])+'\n')
t.close()
f.close()
