#!/bin/bash

Num=9
i=1
while [ $i -lt $Num ]; do
        rm ./Work/PersonInfo$i.txt
        rm ./Work/Votes$i.txt 
	i=$((i + 1))
done
