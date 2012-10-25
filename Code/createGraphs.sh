#!/bin/bash

x=1
y=30

while [ $x -le $y ]
do
  python extract_bipartite_pro.py 12/$x/2008 30
  x=$(( $x + 14 ))
done


