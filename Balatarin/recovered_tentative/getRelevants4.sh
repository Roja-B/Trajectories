#!/bin/bash

dirnames=$(ls Results/)
#dirnames=$(ls /media/data3/roja/Balatarin/CompleteRun/Results/)
#dirnames=$(ls ./test)
for dirname in $dirnames; do
#       test=$(ls /media/data3/roja/Balatarin/CompleteRun/ResultsJaccard30day14slide/$dirname/community*)
#       echo $test
#       numcoms=$(ls /media/data3/roja/Balatarin/CompleteRun/Results/$dirname/community* |wc -l)
        numcoms=$(ls Results/$dirname/community* |wc -l)
        echo $((numcoms-1))
        PathName=Results
#       PatheName=/media/data3/roja/Balatarin/CompleteRun/Results/$dirname/
        echo $PathName
#       python links_group_hash.py $PathName $dirname
        python contingencytable.py $PathName $dirname $((numcoms-1))
#       python communityvotecounts.py $dirname $((numcoms-1))
#       python expected.py $dirname $((numcoms-1))
#       python chi2.py $dirname $((numcoms-1))
#       python representativeLink.py $dirname $((numcoms-1))
#       python makeLinkURL.py $dirname $((numcoms-1))
#       python findLinkDomain.py $dirname $((numcoms-1))
done

