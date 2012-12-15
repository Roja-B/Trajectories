#!/bin/bash

x=1
y=30

while [ $x -le $y ]
do
#  python extract_bipartite_pro.py 12/$x/2008 30
  python bipartiteMongo.py 09/$x/2006 30 # first vote is on 2006-08-14
  x=$(( $x + 14 ))
done


