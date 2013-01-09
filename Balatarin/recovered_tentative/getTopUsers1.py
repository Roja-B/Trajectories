import numpy,sys

# set threshold
def getThreshold(d):
	threshold = numpy.average(d)+numpy.std(d) # mean plus a stddev
#	threshold = # 3rd quantile
	return threshold 



PATH = sys.argv[1]
f=open(PATH+"/Work/NumComsAndModularities","r")
NumComs=dict()
# Read in directory names (corresponding to window dates) and number of communities per directory
for line in f:
	line = line.strip()
	dirname = line.split(" ")[0]
	NumComs[dirname] = int(line.split(" ")[1])
f.close()

for dirname in NumComs:
	print dirname
	tt = open(dirname+"/TopUsercommunityStats","w")
        tt.write("com vertices\n") 
	for n in range(NumComs[dirname]):
		try: f1 = open(dirname+"/community"+str(n),"r")
		except: continue
		f2 = open(dirname+"/pageranks"+str(n),"r")
		userPageranks = []
		userIds = []
		for line in f1: userIds.append(line.strip())
		for line in f2: userPageranks.append(float(line.strip()))
		threshold = getThreshold(userPageranks)
		t = open(dirname+"/topuser_community"+str(n),"w")
		numUsers = 0
		for pagerank,uId in zip(userPageranks,userIds):
			if pagerank >= threshold: 
				t.write(uId+'\n')
				numUsers += 1
		tt.write(str(n)+" "+str(numUsers)+"\n")		
		t.close()
		f1.close()
		f2.close()
	tt.close()
