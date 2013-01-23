#!/bin/bash
dirnames=$(ls Results/)
PathName=Results
for dirname in $dirnames; do
	mv $PathName/$dirname/RelevantLinks/totalWordCounts $PathName/$dirname/RelevantLinks/WordCounts
	rm $PathName/$dirname/RelevantLinks/links.txtnoPunct
done
