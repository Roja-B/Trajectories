import operator
import sys
PATH = sys.argv[1]
dirname = sys.argv[2]
PATH = PATH+'/'+dirname
M = int(sys.argv[3])
INFINITY = 10000
#PATH = raw_input('Enter data path: ')
#M = int(raw_input('Enter the number of communities: '))
#tablefilename = raw_input("Enter file name: ")
tablefilename = "H_value.txt" 
f = open(PATH+'/'+tablefilename,"r")
#t = open(PATH+"/repLinks.txt","w")
Communities= []
#for each community we need a hash table
for i in range(M):
    Communities.append(dict())
for line in f:
    L = line.split('\t')
    link = L[0]
    for i in range(0,M):
        try:count = float(L[i+1])
	except ValueError: count = INFINITY
        Communities[i][link] = count
for i in range(0,M):
    tt = open(PATH+"topLinks"+str(M),"w")
    sorted_com = sorted(Communities[i].iteritems(), key=operator.itemgetter(1))
#    t.write("*** Community "+str(i)+'\n')
    for j in range(len(sorted_com)):
	tt.write('link '+sorted_com[j][0]+' '+str(sorted_com[j][1])+'\n')
    tt.close()
#t.close()
f.close()


