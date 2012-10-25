import math
import sys
dirname = sys.argv[1]
PATH = "test/"+dirname

def intersect(a,b):
        return list(set(a) & set(b))

def union(a,b):
        return list(set(a) | set(b))

def nCr(n,r):
        f = math.factorial
        return f(n) / f(r) / f(n-r)

f = open(PATH+"/ComContingencyTable.txt","r")
a = []
b = []
n = []
i = 0
for line in f:
	line = line.strip()
	n.append([])
	n[i] = line.split("\t") 
	i += 1

M1 = len(n) # no. of communities in clustering1
M2 = len(n[0]) # no. of communities in clustering2

index = 0 
for i in range(M1):
	a.append(0)	
	for j in range(M2):
		element = int(n[i][j])
		index += element*(element-1)/2  # this is n choose 2 
		a[i] += int(n[i][j])

for j in range(M2):
	b.append(0)
	for i in range(M1):
		b[j] += int(n[i][j])

#print a
#print b

N = sum(a)

sum_a = 0
sum_b = 0
for i in range(M1): sum_a += a[i]*(a[i]-1)/2
for j in range(M2): sum_b += b[j]*(b[j]-1)/2

expectedIndex = float(sum_a*sum_b)/(N*(N-1)/2)
maxIndex = 1/2.0*(sum_a+sum_b)
adjusted_Rand = (index - expectedIndex)/(maxIndex - expectedIndex)

#print "Index = "+str(index)
#print "Maximum Index = " + str(maxIndex)
#print"Expected Index = " + str(expectedIndex)
#print "Adjusted Rand Index = "+ str(adjusted_Rand)

t = open("RandIndecesOverTime.txt","a")
t.write(str(adjusted_Rand)+'\n')
