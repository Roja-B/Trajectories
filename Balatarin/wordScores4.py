t.close()
f.close()
	t.write(line)
	line = ''.join([programID,'\t',ProgramDescriptions[programID],'\t',ProgramParticipants[programID],'\n')
for programID in ProgramDescriptions:
		ProgramParticipants[programID].add(participant)
		ProgramParticipants[programID] = set()
	except KeyError: 
	try: ProgramParticipants[programID].add(participant)
	ProgramDescriptions[programID] = description
	participant = L[3]+L[4]
		continue
		print "misformed line in data:", line
	except: 
	try: description = L[1]
	programID = L[0]
	L = line.strip().split('\t')
for line in f:
ProgramParticipants = dict()
ProgramDescriptions = dict()
t = open(PATH+"/myRawData/ProgramInformation","w")
f = open(PATH+"/myRawData/IPAM_Data.txt","r")
from PARAMETERS import PATH
# This program creates a hash table of programs and their descriptions and participants
tttt.close()
f.close()
	t.write(line)
	line = ''.join([programID,'\t',ProgramDescriptions[programID],'\t',participants,'\n'])
	participants = ','.join(ProgramParticipants[programID]) 
for programID in ProgramDescriptions:
		ProgramParticipants[programID].add(participant)
		ProgramParticipants[programID] = set()
	except KeyError: 
	try: ProgramParticipants[programID].add(participant)
	ProgramDescriptions[programID] = description
	participant = ''.join(L[3],L[4])
		continue
		print "misformed line in data:", line
	except: 
	try: description = L[1]
	programID = L[0]
	L = line.strip().split('\t')
for line in f:
ProgramParticipants = dict()
ProgramDescriptions = dict()
t = open(PATH+"/myRawData/ProgramInformation","w")
f = open(PATH+"/myRawData/IPAM_Data.txt","r")
from PARAMETERS import PATH
# This program creates a hash table of programs and their descriptions and participants
		t.close()
			t.write(pair[0]+"\t"+str(pair[1])+'\n')
#			print pair[0].decode("utf-8")
		for pair in sorted_x[1:100]:
		sorted_x = sorted(score.iteritems(), key=operator.itemgetter(1),reverse=True)
		t = open(PATH+"/RelevantLinks/NoLowWordScores"+str(i),"w")
#		print PATH
#        t = open("testWordScores","w")
		#	continue
#			print word
		#except: 
			score[word] = wordScore
			wordScore = round(w1-w2,5) 
			w2 = float(totalCount[word])/float(maxTotal)
			w1 = float(wordCount[word])/float(maxCount)
			if wordCount[word] == 1: continue
		for word in wordCount:
		score = dict()
		f2.close()
			wordCount[word] = count
			if count>maxCount: maxCount = count
                	if word in stopwords: continue
        	        word = line.split("\t")[0].strip()
			except: break
	        	try:count = int(line.split("\t")[1])
			line = line.strip()
			line = f2.readline()
		while True:
		maxCount = 0
		wordCount = dict()
		f2.readline()
		f2 = open(PATH+"/RelevantLinks/NoLowWordCounts"+str(i),"r")
	for i in range(M):
	# for each community:
	print len(totalCount)
	f1.close()
        	totalCount[word] = countTotal
        	if countTotal > maxTotal : maxTotal = countTotal
       		if word in stopwords: continue
	        word = L[0].strip()
        	except: break
	        try: countTotal = int(L[1])
		L = line.split("\t")
	        line = line.strip()
        	line = f1.readline()
	while True:
	f1.readline()
	maxTotal = 0
	totalCount = dict()
	f1 = open(PATH+"/RelevantLinks/normalizedWordCounts","r")
	M = int(p[1])
	PATH = p[0]
        p = p.strip().split("\t")
for p in pathfile:
pathfile = open("PATHSplusCOMS","r")
stopwords = open("stopwordList").read()
import operator
# the scores are only saved for the top 100 words
# stop words are removed
# This program compares word counts per community to total word counts in a window and writes a score for each word
# -*- coding: utf-8 -*-
