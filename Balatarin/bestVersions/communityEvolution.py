# TODO: reading the files from U-pol-... but not all of them exist, because (why?!)
# filenames = os.listdir(PATH+"/TransitionProbs")
dates = []
f = open(PATH+"/Work/U-pol_J100VT5_stats.txt","r")
#f = open(PATH+"/Work/U-pol_L-VT5_stats.txt","r")
for line in f:
	line.strip()
	dates.append(line.split(' ')[0])
f.close()
t = open(PATH+"/Results/ComEvolutions","w")
tt = open(PATH+"/Results/Dates","w")
for date in dates:
	print date
	filename = PATH+"/Results/TransitionProbs/TrProbs"+date
	try: [maxprobs,nextComs] = consecutiveComs(filename)
	except: continue
	t.write(date+"\t")
	tt.write(date+'\n')
	for i in range(len(nextComs)):
		t.write("("+str(i)+","+str(maxprobs[i])+","+str(nextComs[i])+")\t")
	t.write('\n')
t.close()
tt.close()
# This program takes matrices of transition probabilities (between two consecutive temporal windows) and creates lines where each line is a list of next most probably communities for each community at time ti.
import sys
PATH = sys.argv[1]
def consecutiveComs(filename):
	try:f = open(filename, "r")
	except:
                print "could not find TrProbs",date
	nextComs = []
	maxprobs = []
	for line in f:
	        line = line.strip()
        	probs = [float(p) for p in (line.split('\t'))]
#		print probs
		m = max(probs)
		nextComs.append([i for i, j in enumerate(probs) if j == m])
		maxprobs.append(m)
	print nextComs
	print maxprobs
	return [maxprobs,nextComs]
