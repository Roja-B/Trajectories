f= open("/media/data3/roja/Balatarin/Domains/links.txt","r")

domains = dict()
for line in f:
#        if "*" in line: break
        link = line.split(" ")[0]
        d = line.split(" ")[1].strip()
        domains[link] = d
f.close()





f1 = open("randomDomains/randomVotes.txt","r")

i = 0
t = open("randomDomains/random"+str(i),"w")
for line in f1:
	i+=1
	t = open("randomDomains/random"+str(i/10),"w")
	line = line.strip()
	linkID = line.split("\t")[1]
	try: d = domains[linkID]
	except: continue
	t.write(d+'\n')

f1.close()
t.close()
