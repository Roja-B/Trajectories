PATH = "W30S14/Results"
f = open(PATH+"/ComEvolutions","r")
t = open(PATH+"/Edgelist_comEvolutions.txt","w")
time = 1
# 11062006-11202006	(0,0.571,[0])	(1,0.5,[3])	(2,0.5,[3])	(3,0.476,[2])
for line in f:
	line = line.strip()
	for entry in line.split('\t'):
        	if "," not in entry : 
			dates = entry
			continue
	        com = entry.split(',')[0].split('(')[1]
        	nextCom = entry.split('[')[1].split(']')[0]
        	prob = entry.split(',')[1]
 		if float(prob)>0:
			if "," in nextCom: 
				nextComs=nextCom.split(',')
				for element in nextComs:
					element = element.strip()
#					t.write("C"+str(time)+"_"+com+'\t'+"C"+str(time+1)+"_"+element+'\t'+prob+'\n')
					t.write(str(time)+"_"+com+'\t'+str(time+1)+"_"+element+'\t'+prob+'\n')
			else:
				#t.write("C"+str(time)+"_"+com+'\t'+"C"+str(time+1)+"_"+nextCom+'\t'+prob+'\n')
				t.write(str(time)+"_"+com+'\t'+str(time+1)+"_"+nextCom+'\t'+prob+'\n')
	time += 1
f.close()
t.close()
#"! 
