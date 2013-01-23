#!/usr/lib/python3.0

# This program extracts all the unique words in a text file

# Author: Roja Bandari
# September 2012

import re
PATH = "."
   
f = open(PATH+"top100.txt","r")
t = open(PATH+"uniqueTopWords.txt", "w")
    
UniqueWords = set()
for line in f:
     word = line.split("\t")[1].strip()
     UniqueWords.add(word)

for word in UniqueWords:
     t.write(word+'\n')
print len(UniqueWords)

f.close()
t.close()
