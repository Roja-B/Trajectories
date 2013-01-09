#!/bin/bash

filenames=$(ls portion*)
for filename in $filenames; do
#	echo $filename
	grep -v '^[0-9]' $filename > cleaned$filename
done


