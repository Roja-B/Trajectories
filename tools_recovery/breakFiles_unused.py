
filename = "string_py_file-00543.py"
n = 1
f = open(filename,"r")
t = open(filename+str(n),"w")
for line in f:
	line = line.strip()
	if line ==: "": continue
	if "/usr/lib/python" in line: 
		n += 1
		t.close()
		t = open(filename+str(n),"w")
		t.write(line)
	else: t.write(line)
f.close()
t.close()

