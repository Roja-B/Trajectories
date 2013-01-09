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
for line in f:
     word = line.split("\t")[1].strip()
     UniqueWords.add(word)

for word in UniqueWords:
     t.write(word+'\n')
print len(UniqueWords)

f.close()
t.close()
