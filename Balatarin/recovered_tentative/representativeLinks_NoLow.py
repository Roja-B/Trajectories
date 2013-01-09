import sys
PATH = sys.argv[1]
dirname = sys.argv[2]
PATH = PATH+'/'+dirname
M = int(sys.argv[3])

#f1 = open(PATH+"/repLinks.txt","r")
f2 = open("/media/data3/roja/Balatarin/Domains/id_domains.txt","r")

chi2 = [dict() for i in range(M)]  
links = [[] for i in range(M)]

for com in range(M):
	f1 = open(PATH+"/","r")
	for line in f1:
		line = line.strip()
#		if line.split(" ")[0] == "***": 
#			com = int(line.split(" ")[2])
#			print com
#			continue
		linkId = line
		links[com].append(linkId)
		chi2[com][linkId]=line.split(" ")[2]
	f1.close()

for line in f2:
	link = line.split(" ")[0]
	for i in range(M):
		# print links[i]
		if link in links[i]:
#			print "link found"
			t = open(PATH+"/NoLowLinkDomains"+str(i),"a")
			domain = line.split(" ")[1].strip()
			t.write(domain+' '+chi2[i][link]+'\n')
			t.close()
			continue
f2.close()

