#!/usr/lib/python3.0
''' This program reads from the Diff.txt file and removes all duplicate files'''

import os
f = open("Diff.txt","r")
removefilelist = set()
for line in f:
	line = line.strip()
	elements = line.split(" ")
	diff = int(elements[2])
	file1 = elements[0]
	file2 = elements[1]
	if file1 in removefilelist or file2 in removefilelist: continue
	if diff == 0: removefilelist.add(file1)

print len(removefilelist)
for repfile in removefilelist:
	try:
		os.remove(repfile) 
	except: 
		print repfile
f.close()




