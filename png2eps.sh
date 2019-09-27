#!/bin/sh

#####################################################
#
# script for png to eps convertion
# 
#####################################################

cd $1
res_dir='./result'
if [ ! -d $res_dir ]; then mkdir $res_dir; fi

for file in $(find './' -name '*.png');
do
	#new name creating
	name=$( echo $file | cut -d "." -f 2 )
	out=$res_dir'/'$( echo ${name##*/} )'.eps'
	
	#converting
	convert $file $out

	echo 'file '$file' is converted'
done
