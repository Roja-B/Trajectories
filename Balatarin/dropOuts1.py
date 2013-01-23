# This program
# Parameters:
Delta_t = 4
PATH ="/media/data3/roja/Balatarin/CompleteRun/W30S14"
N = 12
# "Dates" file is a product of this code: makeDates.py
f = open("Dates","r")
# save sets of users active in each time window in an array
activeUsers = dict()
cycle = 1
for line in f:
        date = line.strip()
        date = date.replace("-","")
        filename = PATH+"/Results/1005"+date+"/AllUsers"
        f1 = open(filename,"r")
        users = set()
        for line in f1:
                users.add(line.strip())
        activeUsers[cycle] = users
        cycle += 1
f.close()
MAXDATE = len(activeUsers)
for cycle in activeUsers.keys():
        # Compute number of users who "drop out" after Delta_t cycles
        # Dropping out means they are not active for N cycles after that.
        u1 = activeUsers[cycle]
        dropped = u1
        for t in range(cycle+Delta_t,cycle+Delta_t+N):
                if t > MAXDATE : break
                u2 = activeUsers[t]
                dropped = dropped - u2
#       print cycle, len(dropped),len(u1)       
        percent_dropped = float(len(dropped))/float(len(u1))
print "Delta t = ", Delta_t
print "N = ", N


