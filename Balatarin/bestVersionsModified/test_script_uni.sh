#!/bin/bash -e
index=0
window=30
end=61
#mkdir /media/data2/roja/Balatarin/CompleteRun/unipartite/W30S14T
while [ $index -le $end ]
do
  python makeUnipartiteGraph_pro.py $index $window W30S14T
  index=$(( $index + 14 ))
  echo $index
done
