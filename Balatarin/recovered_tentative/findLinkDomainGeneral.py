f= open("/media/data3/roja/Balatarin/Domains/id_domains.txt","r")

domains = dict()
for line in f:
	if "*" in line: break
        link = line.split(" ")[0]
        d = line.split(" ")[1].strip()
	domains[link] = d
f.close()

