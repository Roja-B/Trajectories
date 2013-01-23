f = open("domainPathVotesGreen","r")
for line in f:
    PATH = line.strip()
    print PATH
    t = open(PATH,"r")
    for i in range(10):
            L = t.readline()
            L = L.strip()
            domain = L.split(" ")[0]
            print domain
    t.close()
f.close()


