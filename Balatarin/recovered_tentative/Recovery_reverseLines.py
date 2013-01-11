''' This programs reads lines from a file and writes them in another one in reverse order'''

import sys

INFILE = sys.argv[1] 
OUTFILE = "corrected_"+INFILE 
f = open(INFILE,"r")
t = open(OUTFILE,"w")

lines = []
for line in f:
	lines.append(line)
lines.reverse()
for line in lines:
	t.write(line)
f.close()
t.close()
