
f = open("wordPathZebra","r")
for line in f:
    PATH = line.strip()
    print PATH
    t = open(PATH,"r")
    for i in range(20):
            L = t.readline()
            L = L.strip()
            word = L.split("\t")[0]
            print word
    t.close()
f.close()


