#!/bin/bash

filenames=$(ls py*)
for filename in $filenames; do
	strings $filename > string_$filename
done


