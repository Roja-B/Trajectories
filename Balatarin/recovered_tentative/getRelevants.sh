#!/bin/bash

dirnames=$(ls Results/)
#dirnames=$(ls /media/data3/roja/Balatarin/CompleteRun/Results/)
#dirnames=$(ls ./test)
for dirname in $dirnames; do
#	test=$(ls /media/data3/roja/Balatarin/CompleteRun/ResultsJaccard30day14slide/$dirname/community*)
#	echo $test
#	numcoms=$(ls /media/data3/roja/Balatarin/CompleteRun/Results/$dirname/community* |wc -l)
	numcoms=$(ls Results/$dirname/community* |wc -l)
	echo $((numcoms-1))
	PathName=Results
#	PatheName=/media/data3/roja/Balatarin/CompleteRun/Results/$dirname/
#	echo $PathName
#	python links_group_hash.py $PathName $dirname
#	python contingencytable.py $PathName $dirname $((numcoms-1))
#	python communityvotecounts.py $PathName $dirname $((numcoms-1))
#	python expected.py $PathName $dirname $((numcoms-1))
#	python chi2.py $PathName $dirname $((numcoms-1))
#	python representativeLink.py $PathName $dirname $((numcoms-1))
#	python makeLinkURL.py $PathName $dirname $((numcoms-1))
#	python findLinkDomain.py $PathName $dirname $((numcoms-1))
	mkdir $PathName/$dirname/RelevantLinks
	mv $PathName/$dirname/repLinks.txt $PathName/$dirname/RelevantLinks
	mv $PathName/$dirname/ExpectedVotes.txt $PathName/$dirname/RelevantLinks
	mv $PathName/$dirname/linkVoteCounts.txt $PathName/$dirname/RelevantLinks
	mv $PathName/$dirname/links.txt $PathName/$dirname/RelevantLinks
	mv $PathName/$dirname/communityVoteCounts.txt $PathName/$dirname/RelevantLinks
	mv $PathName/$dirname/contingencyTable.txt $PathName/$dirname/RelevantLinks
	mv $PathName/$dirname/repDomains.txt $PathName/$dirname/RelevantLinks
	mv $PathName/$dirname/Chi2.txt $PathName/$dirname/RelevantLinks
done

