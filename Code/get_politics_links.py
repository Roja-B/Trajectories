# This program extracts all the politics links from the data and saves them in links-politics.txt


# links-summary.txt
# id, user_id, category_id, mediatype_id, points, created_at 
# id: the link id
# Examples:
# 1000001       2       2       1       8       2006-08-14 21:06:19
# 1000002       2       4       4       16      2006-08-14 21:07:10

from PARAMETERS import *

f = open(DATAPATH+"/links-summary.txt","r")
t = open(DATAPATH+"/links-politics.txt","w")

for line in f:
	category = line.split("\t")[2]
	if category == "4" : t.write(line) # category 4 is politics

f.close()
t.close()


