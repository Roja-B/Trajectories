PATH = "/media/data3/roja/Balatarin/CompleteRun"
f = open(PATH+"/Work/U-pol_J100VT_stats.txt","r")
t = open(PATH+"/Results/CommunitySizes","w")
dates=[]
dirs=[]
for line in f:
    dirs.append("100"+line.split(" ")[0].replace("-",""))
    dates.append(line.split(" ")[0])
f.close()
#Open specific repLinks.txt file for each time folder 
time = 0
for (date,entry) in zip(dates,dirs):
    #Mention the correct path upto time folder name {0} and the following path to repLinks.txt in the line below
    f=open(PATH+"/Results/{0}/communityStats".format(entry),"r")
    f.readline()
    print "========================== C",date
    for line in f:
        line = line.strip()
        density = line.split(' ')[3]
        com = line.split(' ')[0]
        size = line.split(' ')[1]
        if density == "NA": size = "3"
        print com,size,density
        t.write(date+'_'+str(com)+'\t'+entry+'\t'+str(size)+'\n')
    f.close()
    time += 1
t.close()

