# -*- coding: utf-8 -*-
# This program compares two lists of word counts (per community with total counts overall) and writes a score for each word
import operator
stopwords = open("stopwordList").read()
pathfile = open("PATHSplusCOMS","r")
f1 = open("totalWordCounts","r")
totalCount = dict()
maxTotal = 0
while True:
        line = f1.readline()
        line = line.strip()
        try: countTotal = int(line.split("\t")[1])
        except: break
        word = line.split("\t")[0].strip()
        if word in stopwords: continue
        if countTotal > maxTotal : maxTotal = countTotal
        totalCount[word] = countTotal
f1.close()
print len(totalCount)
for p in pathfile:
        p = p.strip().split("\t")
	PATH = p[0]
	M = int(p[1])
	# for each community:
	for i in range(M):
		f2 = open(PATH+"/RelevantLinks/NoLowWordCounts"+str(i),"r")
		f2.readline()
		wordCount = dict()
		maxCount = 0
		while True:
			line = f2.readline()
			line = line.strip()
	        	try:count = int(line.split("\t")[1])
			except: break
        	        word = line.split("\t")[0].strip()
                	if word in stopwords: continue
			if count>maxCount: maxCount = count
			wordCount[word] = count
		f2.close()
		score = dict()
		for word in wordCount:
			if wordCount[word] == 1: continue
			w1 = float(wordCount[word])/float(maxCount)
			w2 = float(totalCount[word])/float(maxTotal)
			wordScore = round(w1-w2,5) 
			score[word] = wordScore
		#except: 
#			print word
		#	continue
#        t = open("testWordScores","w")
#		print PATH
		t = open(PATH+"/RelevantLinks/NoLowWordScores"+str(i),"w")
		sorted_x = sorted(score.iteritems(), key=operator.itemgetter(1),reverse=True)
		for pair in sorted_x[1:100]:
#			print pair[0].decode("utf-8")
			t.write(pair[0]+"\t"+str(pair[1])+'\n')
		t.close()
#"! 
