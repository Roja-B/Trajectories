#!/bin/bash

filenames=$(ls community*)
for filename in $filenames; do
	mkdir Dir_$filename
	xargs -a $filename mv -t Dir_$filename
done


