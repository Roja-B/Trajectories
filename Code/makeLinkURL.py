import sys
PATH = sys.argv[1]
dirname = sys.argv[2]
PATH = PATH+'/'+dirname
#PATH = "test/"+dirname
#PATH = "./ResultsJaccard30day14slide/"+dirname
M = int(sys.argv[3])

#PATH = raw_input('Enter data path: ')
#M = int(raw_input('Enter the number of communities: '))

f1 = open(PATH+"/repLinks.txt","r")
f2 = open("/media/data3/roja/Balatarin/data/links-summary.txt","r")
#t = open(PATH+"/RepLinkURLs.txt","a")

chi2 = [dict() for i in range(M)]

links = [[] for i in range(M)]
for line in f1:
	line = line.strip()
	if line.split(" ")[0] == "***": 
		com = int(line.split(" ")[2])
		print com
		continue
	linkId = line.split(" ")[1]
	links[com].append(linkId)
	chi2[com][linkId]=line.split(" ")[2]
f1.close()

#print links

# 1593763	8154	4	1	293	2009-05-20 15:22:50
for line in f2:
	link = line.split("\t")[0]
	for i in range(M):
		# print links[i]
		if link in links[i]:
			print "link found"
			t = open(PATH+"/RepLinkURLs"+str(i),"a")
			date = line.split("\t")[5].split(" ")[0]
			year = int(date.split("-")[0])
			month = int(date.split("-")[1])
			day = int(date.split("-")[2])
			t.write("https://balatarin.com/permlink/"+str(year)+"/"+str(month)+"/"+str(day)+"/"+link+' ')
			t.write(chi2[i][link]+'\n')
			t.close()
			continue
f2.close()


