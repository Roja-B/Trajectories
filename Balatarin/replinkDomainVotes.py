
#import sys
#PATH = sys.argv[1]
#dirname = sys.argv[2]
#PATH = PATH+'/'+dirname
pathsFile = open("Work/NumComsAndModularities","r")
# read all links and their domains into a dictionary
f = open("/media/data3/roja/Balatarin/Domains/id_domains.txt","r")
linkDomains = dict()
for line in f:
	line = line.strip()
	try:
		linkID = line.split(" ")[0]
		domain = line.split(" ")[1]
	except: print line
	linkDomains[linkID] = domain
f.close()
for p in pathsFile:
	p = p.strip()
	PATH = p.split('\t')[0]
	M = int(p.split('\t')[1])
	# find the total number of votes for each link in one time slot
	f = open(PATH+"/RelevantLinks/contingencyTable.txt","r")
	domainVotes = dict()
	linkVotes = dict()
	for line in f:
		line = line.strip()
		linkID = line.split('\t')[0]
		votes = line.split('\t')
		linkVotes[linkID] = 0
		for i in range(1,len(votes)):
			linkVotes[linkID] += int(votes[i])
	f.close()
	# find total number of votes for each domain in one time slot
	for link in linkVotes:
		domain = linkDomains[link]
		if domain in domainVotes: domainVotes[domain] += linkVotes[linkID]
		else: domainVotes[domain] = linkVotes[linkID]
	# find votes of representative links
	print M
	for i in range(M):
		try: f = open(PATH+"/RelevantLinks/RepLinkDomains"+str(i),"r")
		except: 
			print "no community "+str(i)
			continue
		t = open(PATH+"/RelevantLinks/RepLinkDomainVotes"+str(i),"w")
		for line in f:
			domain = line.strip().split(' ')[0]
			t.write(domain+"\t"+str(domainVotes[domain])+'\n')
		f.close()


