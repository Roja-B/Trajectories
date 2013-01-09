/media/data3/roja/Balatarin/CompleteRun/step1.sh
utf-8
U3210
#"! 
done
        cd ../..
        R --save < main_balatarin.R
        cd Results/$dname/
        cp *.R ./Results/$dname/
        echo $dname
for dname in $dnames; do
dnames=$(ls /media/data3/roja/Balatarin/CompleteRun/Results/)
done
        cp /media/data3/roja/Balatarin/CompleteRun/bipartite/$filename ./Results/$dirname/bipartite.txt
        echo $dirname
        dirname=1005$(echo $filename | tr -dc "[:digit:]")
for filename in $bfilenames; do
done
        cp /media/data3/roja/Balatarin/CompleteRun/unipartite/$filename ./Results/$dirname/unipartite.txt
        mkdir ./ResultsJaccard30day14slide/$dirname
        dirname=$(echo $filename | tr -dc "[:digit:]")
for filename in $ufilenames; do
ufilenames=$(ls /media/data3/roja/Balatarin/CompleteRun/unipartite/)
bfilenames=$(ls /media/data3/roja/Balatarin/CompleteRun/bipartite/)
#!/bin/bash

