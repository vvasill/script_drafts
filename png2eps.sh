#!/bin/sh

#####################################################
#
# script for png to eps convertion
# 
#####################################################

cd $1

for file in $(find './' -name '*.png');
do
	#new name creating
	out=$( echo $file | sed 's/png/eps/' )
	
	echo $out
	
	#converting
	convert $file $out

	echo 'file '$file' is converted'
done
