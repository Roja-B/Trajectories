# this program creates a list of all balatarin URLs.


f = open("/media/data3/roja/Balatarin/links-summary.txt","r")
t = open("AllLinkURLs.txt","a")

for line in f:
	link = line.split("\t")[0]
	date = line.split("\t")[5].split(" ")[0]
	year = int(date.split("-")[0])
	month = int(date.split("-")[1])
	day = int(date.split("-")[2])
	t.write("https://balatarin.com/permlink/"+str(year)+"/"+str(month)+"/"+str(day)+"/"+link+'\n')
t.close()
f.close()


