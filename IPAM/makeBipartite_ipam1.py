# This program creates bipartite graphs of programs and participants using the desired window size and slide amount 
# Roja Bandari
# September 2012
# parameters
WINDOW = 4 # in years
SLIDE = 1 # in years
PATH = "/media/data3/roja/IPAM"
START_YEAR = 2000
END_YEAR = 2013

t = open(PATH+"/myIntermediateFiles/BipartiteNamesAndPaths","w")
# make bipartite graphs using the data from each year
year = START_YEAR
while year < END_YEAR-WINDOW:
	print year
	bgraphname = PATH+"/myIntermediateFiles/Bipartite/Bipartite"+'_'+str(year)+'_'+str(year+WINDOW-1)
	t.write(bgraphname+"\n")
	tt = open(bgraphname,"w")
	for n in range(year,year+WINDOW):
		f = open(PATH+"/myIntermediateFiles/TemporalGraphs/EdgeList"+str(n),"r")
		for line in f: tt.write(line)
		f.close()
	tt.close()
	year += SLIDE
t.close()
