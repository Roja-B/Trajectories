#!/bin/bash
dirnames=$(ls Results/)
#dirnames=$(ls /media/data3/roja/Balatarin/CompleteRun/Results/)
#dirnames=$(ls ./test)
for dirname in $dirnames; do
        numcoms=$(ls Results/$dirname/community* |wc -l)
        echo $((numcoms-1))
        PathName=Results
#       PatheName=/media/data3/roja/Balatarin/CompleteRun/Results/$dirname/
#       echo $PathName
        python links_group_hash.py $PathName $dirname
        python contingencytable.py $PathName $dirname $((numcoms-1))
        python communityvotecounts.py $PathName $dirname $((numcoms-1))
        python expected.py $PathName $dirname $((numcoms-1))
        python binomial.py $PathName $dirname $((numcoms-1))
        python representativeLink.py $PathName $dirname $((numcoms-1))
        python makeLinkURL.py $PathName $dirname $((numcoms-1))
        python findLinkDomain.py $PathName $dirname $((numcoms-1))
        mkdir $PathName/$dirname/RelevantLinks_h
        mv $PathName/$dirname/repLinks.txt $PathName/$dirname/RelevantLinks
        mv $PathName/$dirname/ExpectedVotes.txt $PathName/$dirname/RelevantLinks
        mv $PathName/$dirname/linkVoteCounts.txt $PathName/$dirname/RelevantLinks
        mv $PathName/$dirname/links.txt $PathName/$dirname/RelevantLinks
        mv $PathName/$dirname/communityVoteCounts.txt $PathName/$dirname/RelevantLinks
        mv $PathName/$dirname/contingencyTable.txt $PathName/$dirname/RelevantLinks
        mv $PathName/$dirname/RepLinkDomains* $PathName/$dirname/RelevantLinks
        mv $PathName/$dirname/Chi2.txt $PathName/$dirname/RelevantLinks
done
cp Work/NumComsAndModularities Results

