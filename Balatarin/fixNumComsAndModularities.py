PATH = "./W42S14"
f= open(PATH+"/Work/NumComsAndModularities","r")
t = open("NumComsAndModularities","w")
for line in f:
	line = line.strip()
	if "/" in line:
		line = string.replace(line," ","\t")
		line = string.replace(line,"Results","W42S14/Results")
		print line.split("\t")
		t.write(line+'\t')
	else: t.write(line+'\n')
#	t.write(line+'\n')

f.close()
t.close()
