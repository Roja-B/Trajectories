

        _date = "100"+_date.replace("-","")
        print _date
        f=open(PATH+"/{0}/communityStats".format(_date),"r")

        f.readline()
        for line in f:
                line = line.strip()
                #density = line.split(' ')[3]
                size = line.split(' ')[1]
                community = line.split(' ')[0]
                print community,com
                if community == com:
                        f.close()
                        return size

