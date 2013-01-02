#!/bin/bash

dirnames=$(ls)
for dirname in $dirnames; do
        filenames=$(ls $dirname)
	for filename in $filenames; do
		grep -l abc $dirname/$filename
	done
done

