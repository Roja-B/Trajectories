# -*- coding: utf-8 -*-
# This program compares two lists of word counts (per community with total counts overall) and writes a score for each word. Note: It only writes to file the scores for top 100 words in each community
import operator
stopwords = open("stopwordList").read()
f1 = open("totalWordCounts","r")
totalCount = dict()
maxTotal = 0
while True:
        line = f1.readline() # we do this because it avoids encoding problems
        line = line.strip()
        try: countTotal = int(line.split("\t")[1])
        except:	break
        word = line.split("\t")[0].strip()
#	print word
        if word in stopwords: continue
        if countTotal > maxTotal : maxTotal = countTotal
        totalCount[word] = countTotal
f1.close()
print len(totalCount)
TrajectoryNames = ["A","B","Bprime","B1","B1prime","E","Eprime","C","C0","D2","D2prime","D","F"]
PATH = "/media/data3/roja/Balatarin/CompleteRun/TrajectoryAnalysis/Links/NoLowVotes"
for name in TrajectoryNames:
	filename = PATH+"/WordCountsPath"+name
	f2 = open(filename,"r")
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
	t = open(PATH+"/NoLowWordScoresPath"+name,"w")
	sorted_x = sorted(score.iteritems(), key=operator.itemgetter(1),reverse=True)
	for pair in sorted_x[1:100]:
		t.write(pair[0]+"\t"+str(pair[1])+'\n')
	t.close()
#"! 
