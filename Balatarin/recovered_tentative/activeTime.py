f = open("votes-summary.txt","r")
t = open("LastActivity.txt","a")
lastActive = dict()
for line in f:
	user = line.split("\t")[2]
	date = line.split("\t")[5].split(" ")[0]
	if lastActive[user] < date :
		lastActive[user] =  date
b0VIM 7.3
roja
starsky
/media/data3/roja/Balatarin/activeTime.py
utf-8
U3210
