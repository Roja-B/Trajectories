#!/bin/bash

Num=$(ls /media/data3/roja/balatarin/bipartite/ | wc -l)
while [ $i -lt $Num ]; do
        mkdir ./Results$i
        cp /media/data3/roja/balatarin/bipartite/PersonInfo$i.txt ./Work/bipartite_edgelist.txt
        cp ./tempWork/Votes$i.txt ./Work/unipartite.txt
#       numusers=$(wc -l ./Work/PersonInfo.txt)
#       echo $numusers > "numusers.txt"
#       numvotes=$(wc -l ./Work/Votes.txt)
#       echo "number of votes  $numvotes"
#       echo $numusers'\n'$numvotes> "META.txt"
        wc -l ./Work/PersonInfo.txt > "./Work/META.txt"
        wc -l ./Work/Votes.txt >> "./Work/META.txt"
        echo $(wc -l ./Work/votes_sorted.txt)
        mv ./Work/votes_grouped.txt Results$i/
        mv ./Work/votes_sorted.txt Results$i/
        mv ./Work/votes_ready_for_R.txt Results$i/
        mv ./Work/unipartite_edgelist.txt Results$i/
        mv ./Work/true_membership.txt Results$i/
        cp ./myRComFiles/* ./Results$i/
        i=$((i + 1))
done
