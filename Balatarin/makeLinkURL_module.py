# this program takes a list of balatarin link ids and creates a list of balatarin URLs.

PATH = raw_input('Enter data path: ')

f1 = open(PATH+"/links.txt","r")
f2 = open("/media/data3/roja/Balatarin/links-summary.txt","r")
t = open(PATH+"LinkURLs.txt","a")

links = dict()
for line in f1:
	line = line.strip()
	linkId = line.split(" ")[0]
	links[linkId] = 1
#	links.append(linkId)
f1.close()

for line in f2:
	link = line.split("\t")[0]
	if link in links:
#		print "link found"
		date = line.split("\t")[5].split(" ")[0]
		year = int(date.split("-")[0])
		month = int(date.split("-")[1])
		day = int(date.split("-")[2])
		t.write("https://balatarin.com/permlink/"+str(year)+"/"+str(month)+"/"+str(day)+"/"+link+'\n')
t.close()
f2.close()


