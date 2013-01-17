#!/bin/bash
dirnames=$(ls Results/)
for dirname in $dirnames; do
	PathName=Results
        numcoms=$(ls Results/$dirname/community* |wc -l)
	echo $dirname $((numcoms-1))>> DirNamesAndComs
#	rm $PathName/$dirname/RelevantLinks/NoLow*
done
