#!/usr/lib/python3.0

''' This program takes the Diff.txt file and converts it to an edgelist (replaces difference values with weights) '''

f = open("Diff.txt","r")
t = open("Edgelist.txt","w")
for line in f:
	line = line.strip()
	elements = line.split(" ")
	diff = float(elements[2])
	file1 = elements[0]
	file2 = elements[1]
	if diff == 0 or file2 == 'none' : continue
	else : t.write(file1+" "+file2+" "+str(100*1.0/diff)+"\n")
f.close()
t.close()



