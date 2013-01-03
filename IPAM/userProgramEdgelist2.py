
f = open("IPAM_Data.txt","r")
t = open("EdgeList","w")
for line in f:
	line = line.strip()
	programID = line.split('\t')[0]
	try: userEmail = line.split('\t')[6]
	except:
		print line
		continue
	t.write(programID+'\t'+userEmail+'\n')

f.close()
t.close()

