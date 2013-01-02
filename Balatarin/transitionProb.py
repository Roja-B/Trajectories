import math

def intersect(a,b):
        return list(set(a) & set(b))

def union(a,b):
        return list(set(a) | set(b))

def nCr(n,r):
        f = math.factorial
        return f(n) / f(r) / f(n-r)

f = open("work/ComContingencyTable.txt","r")
n_t1 = []
n_t2 = []
n = []
i = 0
for line in f:
	line = line.strip()
	n.append([])
	n[i] = line.split("\t") 
	i += 1

M1 = len(n) # no. of communities in clustering1
M2 = len(n[0]) # no. of communities in clustering2

sum_all = 0 
for i in range(M1):
	n_t1.append(0)	
	for j in range(M2):
		sum_all += int(n[i][j])
		n_t1[i] += int(n[i][j])

for j in range(M2):
	n_t2.append(0)
	for i in range(M1):
		n_t2[j] += int(n[i][j])

#print n_t1
#print n_t2

N = sum(n_t1)

p = []
for i in range(M1):
	p.append([])
	if n_t1[i] == 0 : continue
	for j in range(M2):
		p_t1 = float(n_t1[i])/N
		p_t2 = float(n_t2[j])/N
		joint_p = float(n[i][j])/sum_all
		p[i].append(round(joint_p/p_t1,3))

print p



