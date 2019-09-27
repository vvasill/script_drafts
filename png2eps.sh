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
	name=$( echo $file | cut -d "." -f 2 )
	out='.'$name'.eps'
	
	#converting
	convert $file $out

	echo 'file '$file' is converted'
done
