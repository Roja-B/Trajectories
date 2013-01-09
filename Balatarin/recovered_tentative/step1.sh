#!/bin/bash

bfilenames=$(ls /media/data3/roja/Balatarin/CompleteRun/bipartite/)
ufilenames=$(ls /media/data3/roja/Balatarin/CompleteRun/unipartite/)

for filename in $ufilenames; do
        dirname=$(echo $filename | tr -dc "[:digit:]")
        mkdir ./ResultsJaccard30day14slide/$dirname
        cp /media/data3/roja/Balatarin/CompleteRun/unipartite/$filename ./ResultsJaccard30day14slide/$dirname/unipartite.txt
done
	
for filename in $bfilenames; do
        dirname=1005$(echo $filename | tr -dc "[:digit:]")  
        echo $dirname
        cp /media/data3/roja/Balatarin/CompleteRun/bipartite/$filename ./ResultsJaccard30day14slide/$dirname/bipartite.txt
done
dnames=$(ls /media/data3/roja/Balatarin/CompleteRun/ResultsJaccard30day14slide/)
for dname in $dnames; do
	echo $dname
	cp *.R ./ResultsJaccard30day14slide/$dname/
	cd ResultsJaccard30day14slide/$dname/
	R --save < main_balatarin.R
	cd ../..
done


