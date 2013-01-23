#!/usr/lib/python3.0
# This program extracts all the unique words in a text file
# Author: Roja Bandari
# September 2012
OPTION = "H_Value"
import re
PATH = "/media/data3/roja/Balatarin/CompleteRun/TrajectoryAnalysis/Links/"+OPTION   
f = open(PATH+"/top100Words"+OPTION,"r")
t = open(PATH+"/uniqueTopWords"+OPTION, "w")
    
UniqueWords = set()
for i in range(1300):
     line = f.readline()
     if "WordScoresPath" in line: continue
     print line.split("\t")
     word = line.split("\t")[0].strip()
     UniqueWords.add(word)     
for word in UniqueWords:
     t.write(word+'\n')
print len(UniqueWords)
f.close()
t.close()
b0VIM 7.3
SPS{
roja
starsky
/media/data3/roja/Balatarin/CompleteRun/TrajectoryAnalysis/uniqifyWords.py
utf-8
