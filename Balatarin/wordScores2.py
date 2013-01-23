#"! 
	t.close()
		t.write(pair[0]+"\t"+str(pair[1])+'\n')
	for pair in sorted_x[1:100]:
	sorted_x = sorted(score.iteritems(), key=operator.itemgetter(1),reverse=True)
	t = open(PATH+"/NoLowWordScoresPath"+name,"w")
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
	f2 = open(filename,"r")
	filename = PATH+"/WordCountsPath"+name
for name in TrajectoryNames:
PATH = "/media/data3/roja/Balatarin/CompleteRun/TrajectoryAnalysis/Links/NoLowVotes"
TrajectoryNames = ["A","B","Bprime","B1","B1prime","E","Eprime","C","C0","D2","D2prime","D","F"]
print len(totalCount)
f1.close()
        totalCount[word] = countTotal
        if countTotal > maxTotal : maxTotal = countTotal
        if word in stopwords: continue
#	print word
        word = line.split("\t")[0].strip()
        except:	break
        try: countTotal = int(line.split("\t")[1])
        line = line.strip()
        line = f1.readline() # we do this because it avoids encoding problems
while True:
maxTotal = 0
totalCount = dict()
f1 = open("totalWordCounts","r")
stopwords = open("stopwordList").read()
import operator
# This program compares two lists of word counts (per community with total counts overall) and writes a score for each word. Note: It only writes to file the scores for top 100 words in each community
# -*- coding: utf-8 -*-
