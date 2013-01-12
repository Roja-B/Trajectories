#!/bin/bash
bfilenames=$(ls /media/data2/roja/Balatarin/CompleteRun/bipartite/)
ufilenames=$(ls /media/data2/roja/Balatarin/CompleteRun/unipartite/)
for filename in $ufilenames; do
        dirname=$(echo $filename | tr -dc "[:digit:]")
        mkdir ./Results/$dirname
        cp /media/data2/roja/Balatarin/CompleteRun/unipartite/$filename ./Results/$dirname/unipartite.txt
done
for filename in $bfilenames; do
        dirname=1005$(echo $filename | tr -dc "[:digit:]")  
        echo $dirname
        cp /media/data2/roja/Balatarin/CompleteRun/bipartite/$filename ./Results/$dirname/bipartite.txt
done
dnames=$(ls /media/data2/roja/Balatarin/CompleteRun/Results/)
for dname in $dnames; do
	echo $dname
	cp *.R ./Results/$dname/
	cd Results/$dname/
	R --save < main_balatarin.R
	cd ../..
done
mv Results/NumComsAndModularities Work
