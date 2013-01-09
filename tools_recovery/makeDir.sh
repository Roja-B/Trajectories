#!/bin/bash

mkdir VertexCom\ base
cp VertexCom\ base* VertexCom\ base

Num=$(ls VertexCom\ base | wc -l)
echo "number of communities is $Num"
i=0
while [ $i -lt $Num ]; do
	mkdir VertexCom\ $i
	cp VertexCom\ $i* VertexCom\ $i
	i=$((i + 1))
done
