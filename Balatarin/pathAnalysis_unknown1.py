import sys
from counter import *
from noPunct import *
TrajectoryNames = ["A","B","Bprime","B1","B1prime","E","Eprime","C","C0","D2","D2prime","D","F"]
OPTION = "H_Value"
#OPTION = "NoLowVotes"
f = open("/media/data3/roja/Balatarin/data/politics_linkTexts")
linkText = dict()
for line in f:
        link_id = line.split("_")[0].strip()
        linkText[link_id] = line
f.close()





#PATH = sys.argv[1]
#dirname = sys.argv[2]
#PATH = PATH+'/'+dirname
#M = int(sys.argv[3]) # number of communities
#PATH = "./test/RepLinkDomains"
PATH = "/media/data3/roja/Balatarin/CompleteRun/TrajectoryAnalysis/Links/"+OPTION
for name in TrajectoryNames:
        f = open(PATH+"/Links"+name+"Path","r")
        t = open(PATH+"/linkTextsPath"+name,"w")
        for line in f:
                linkID = line.strip()
                try: t.write(linkText[linkID])
                except: print linkID
        f.close()
        t.close()

