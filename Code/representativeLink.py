import operator
import sys
PATH = sys.argv[1]
dirname = sys.argv[2]
PATH = PATH+'/'+dirname
#PATH = "./ResultsJaccard30day14slide/"+dirname
#PATH = "test/"+dirname
M = int(sys.argv[3])

#PATH = raw_input('Enter data path: ')
#M = int(raw_input('Enter the number of communities: '))
#tablefilename = raw_input("Enter file name: ")
tablefilename = "Chi2.txt"
f = open(PATH+'/'+tablefilename,"r")
t = open(PATH+"/repLinks.txt","a")

Communities= []
#for each community we need a hash table
for i in range(M):
    Communities.append(dict())


for line in f:
    link = line.split('\t')[0]
    for i in range(0,M):
        count = float(line.split('\t')[i+1])
        Communities[i][link] = count



for i in range(0,M):
#    t = open(PATH+"/repLinks"+str(i),"a")
    sorted_com = sorted(Communities[i].iteritems(), key=operator.itemgetter(1),reverse=True)
    t.write("*** Community "+str(i)+'\n')
    for j in range(10):
#        t.write("link "+sorted_com[j][0]+'\n')# here we also want to report the chi2 measure
	t.write("link "+sorted_com[j][0]+' '+str(sorted_com[j][1])+'\n')
t.close()
f.close()
