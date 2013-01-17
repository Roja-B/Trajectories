#import sys
#PATH = sys.argv[1]
#dirname = sys.argv[2]
#PATH = PATH+'/'+dirname
#M = int(sys.argv[3])
PATH = "/media/data3/roja/Balatarin/CompleteRun"
f = open("DirNamesAndComs","r")
# Read all directory names and number of communities into a dictionary
numcoms = dict()
for line in f:
	line = line.strip()
	dirname = line.split(' ')[0]
	M = line.split(' ')[1]
	numcoms[dirname] = int(M)
f.close()
# Created a dictionary of linkIds and domains
f1 = open("/media/data3/roja/Balatarin/Domains/id_domains.txt","r")
Domains = dict()
for line in f1:
	parsed = line.strip().split(" ")
	try:
		link = parsed[0]
		domain = parsed[1]
		Domains[link] = domain
	except: print line
f1.close()
# Iterate through the directories and extract domains
for dirname in numcoms.keys():
	dirPATH = PATH+'/'+dirname
	for com in range(numcoms[dirname]):
		filename = "%(dirPATH)s/NoLowTop10Links%(com)%s" %locals()
		try: f2 = open(filename,"r")
		except: 
			print "No such file: ",filename
			continue
		filename = "%(dirPATH)s/NoLowLinkDomains%(com)%s" %locals()
		t = open(filename,"w")
		for line in f2:
			linkId = line.strip()
			t.write(Domains[linkID]+'\n')
		f2.close()
		t.close()
