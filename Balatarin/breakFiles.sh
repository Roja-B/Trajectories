#!/bin/bash

filenames=$(ls string*)
for filename in $filenames; do
	csplit -z --prefix=portion_$filename $filename '/\!\|strict/' '{*}' 
#	csplit -z --prefix=portion_$filename $filename '/strict/' '{*}'

done


