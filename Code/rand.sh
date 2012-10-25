#!/bin/bash


dirnames=$(ls /media/data3/roja/Balatarin/CompleteRun/ResultsJaccard30day14slide/)
for dirname in $dirnames; do
	numcoms=$(ls /media/data3/roja/Balatarin/CompleteRun/ResultsJaccard30day14slide/$dirname/community* |wc -l)
	echo $((numcoms-1))
	python contingencytable.py $dirname $((numcoms-1))
done

