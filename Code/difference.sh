#!/bin/bash

filenames=$(ls cleaned*)
for filename1 in $filenames; do
	n_min=10000
	f="none"
	for filename2 in $filenames;do
		if [ $filename2 == $filename1 ]; then
			 continue 
		fi
		n=$(diff $filename1 $filename2|wc -l)
		if [ $n -lt $n_min -o $n -eq 0 ]
		then
			n_min=$n
			f=$filename2
#			echo $n $filename2
		fi
	done
        echo $filename1 $f $n_min >> Diff.txt
done



