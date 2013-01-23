PATH = "/media/data3/roja/Balatarin/CompleteRun"
f = open(PATH+"/Work/NumComsAndModularities","r")
t = open(PATH+"/Work/NumComsAndModularities_betterformat","w")
for line in f:
        line = line.strip()
#       if "/" not in line:
#               t.write(line+'\n')
#               continue
        numComs = line.split(" ")[1]
        dates = line.split(" ")[0].split("/")[7]
        modularity = line.split(" ")[2]
        t.write(dates[3:11]+"-"+dates[11:len(dates)]+"\t"+numComs+'\t'+modularity+'\n')
        # 10051019200911182009
f.close()
t.close()

