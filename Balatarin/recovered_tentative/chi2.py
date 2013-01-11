#!/usr/lib/python3.0
'''create the table of chi^2 values between links and communities'''
import sys
PATH = sys.argv[1]
dirname = sys.argv[2]
PATH = PATH+'/'+dirname
#PATH = "./ResultsJaccard30day14slide/"+dirname
#PATH = "test/"+dirname
M = int(sys.argv[3])
#PATH = raw_input('Enter data path: ')
#M = int(raw_input('Enter the number of communities: '))
try:
        e = open(PATH+'/ExpectedVotes.txt',"r")
        o = open(PATH+'/contingencyTable.txt',"r")
        t = open(PATH+'/Chi2.txt',"w")
except:
        print 'error opening file'
n = 0
for line1,line2 in zip(e,o):
#       line2 = o.readline()
#       print line1
#       print line2
#       print ('--------------------------------------')
#       E = []
#       O = []  
        line1 = line1.strip()
        line2 = line2.strip()
        link_id = line2.split('\t')[0]
        t.write(link_id)
        for i in range(0,M):
#               expectedString = line1.split('\t')[i]
#               print expectedString
#               E = float(expectedString)       
                E=float(line1.split('\t')[i])
                if (E==0) : E = 0.0000000001
                O=float(line2.split('\t')[i+1])
                if (O-E)< 0 : chi = 0
                else: chi = round((O-E)**2/E,5)
                t.write('\t'+str(chi))
        t.write('\n')
e.close()
o.close()
t.close()

