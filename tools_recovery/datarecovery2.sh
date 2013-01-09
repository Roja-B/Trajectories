#!/bin/bash

filenames=$(ls)
for filename in $filenames; do
	strings $filename > string_$filename
done


