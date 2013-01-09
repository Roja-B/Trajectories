#/numusers=$(wc -l ./Work/PersonInfo.txt)
#       echo $numusers > "numusers.txt"
#       numvotes=$(wc -l ./Work/Votes.txt)
#       echo "number of votes  $numvotes"
#       echo $numusers'\n'$numvotes> "META.txt"

#dirnames=$(ls /media/data3/roja/Balatarin/CompleteRun/ResultsJaccard30day14slide/)
dirnames=$(ls ./test)
for dirname in $dirnames; do
        numcoms=$(ls test/$dirname/community* |wc -l)
        echo $((numcoms-1))
        python links_group_hash.py $dirname
        python contingencytable.py $dirname $((numcoms-1))
        python communityvotecounts.p $dirname $((numcoms-1))
        python expected.py
        python chi2.py
        python representativeLink.py
        python makeLinkURL.py
        python findLinkDomain.py

done

