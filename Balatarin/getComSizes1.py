


PATH = "/media/data3/roja/Balatarin/CompleteRun/W30S14/Results"
f = open(PATH+"/U-pol_J100VT5_stats.txt","r")
t = open(PATH+"/CommunitySizes","w")
dates=[]
for line in f:
    dates.append("1005"+line.split(" ")[0].replace("-",""))
f.close()
#Open specific repLinks.txt file for each time folder 
time = 0
for entry in dates:
    #Mention the correct path upto time folder name {0} and the following path to repLinks.txt in the line below
    f=open(PATH+"/{0}/communityStats".format(entry),"r")
    f.readline()
    print "========================== C",entry
    time += 1
    for line in f:
        line = line.strip()
        density = line.split(' ')[3]
        com = line.split(' ')[0]
        size = line.split(' ')[1]
        if density == "NA": size = "3"
        print com,size,density
        t.write("C"+str(time)+'_'+str(com)+'\t'+str()+'\t'+str(size)+'\n')
    f.close()
t.close()
