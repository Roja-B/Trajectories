#!/bin/bash

dirnames=$(ls /media/E/E/../../..)

for dirname in $dirnames; do
	grep -l noPunct /media/E/E/$dirname/*
#        filenames=$(ls $dirname)
#	for filename in $filenames; do
#		grep -l noPunct $dirname/$filename
#	done
done

