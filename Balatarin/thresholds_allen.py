PATH = "."
MIN_USER_VOTES = 20 
MAX_USER_VOTES = 30000
MAX_LINK_VOTES = 175 
f1 = open(PATH+"/data/links-summary.txt","r")
f2 = open(PATH+"/data/votes-summary.txt","r")
t1 = open(PATH+"/data/threshold_max"+str(MAX_LINK_VOTES)+"-links.txt","w")
t2 = open(PATH+"/data/threshold_min"+str(MIN_USER_VOTES)+"_max"+str(MAX_USER_VOTES)+"-users.txt","w")
# id, user_id, category_id, mediatype_id, points, created_at
for line in f1:
	line = line.strip()
	linkVotes = int(line.split('\t')[4])
	if linkVotes > MAX_LINK_VOTES or linkVotes < 0: continue
	else: t1.write(line+'\n')
f1.close()
t1.close()
userVotes = dict()
#id, link_id, user_id, sign, vote_reason_id, created_at
for line in f2:
        line = line.strip()
        userID = int(line.split('\t')[2])
	if userID not in userVotes: userVotes[userID] = 1
	else: userVotes[userID] += 1
f2.close()
print "hash table completed"
userPassFail = dict()
for user in userVotes.keys(userVotes):
        if userVotes[user] > MAX_USER_VOTES or userVotes[user] < MIN_USER_VOTES:
		userPassFail[user] = "Fail" 
		print user
        else: userPassFail = "Pass"
print "pass fail hash table completed"
f2 = open(PATH+"/data/votes-summary.txt","r")
for line in f2:
        line = line.strip()
        userID = int(line.split('\t')[2])       
	if userPassFail[userID] == "Fail" : continue
	else: t2.write(line+'\n')
f2.close()
t2.close()
#"! 
