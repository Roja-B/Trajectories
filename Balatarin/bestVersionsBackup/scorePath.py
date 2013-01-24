# makes the file paths for word scores for a given "path" or "trajectory"
TrajectoryNames = ["E","Pink","B1","B1prime","F","C0","D2","D2prime","Eprime"]
for name in TrajectoryNames:
        print name
        f = open("Path"+name,"r")
        t = open("userPath"+name,"w")
        for line in f:
                line = line.strip()
                date = line.split("\t")[0]
                date = date.replace("-","")
                try: com = line.split("\t")[1]
                except: 
                        print line
                        break
                date = "Results/1005"+date+"/community"+com
                t.write(date+'\n')
        f.close()
        t.close()
