#!/bin/bash

#####################################################
#
# script for pdf construction
# 
#####################################################

path='../astro_he/add'
cd $path
if [ ! -d './out' ]; then mkdir './out'; fi

check=odd
count=0

for file in *.pdf
do
	(( count++ ))
	echo $count
	### page crop ###
	pdfcrop $file './out/'$file >/dev/null 2>&1
	
	### page rotation ###
	if [[ $check == 'odd' ]]
	then
		pdf270 './out/'$file -o './out/rot_'$file >/dev/null 2>&1
		check=even
	else 
		pdf90 './out/'$file -o './out/rot_'$file >/dev/null 2>&1
		check=odd
	fi

	mv './out/rot_'$file './out/'$file

	### page numbering ###
	#pdftk './out/rot_'$file  multibackground $count'.pdf' output './out/'$file
	#rm './out/rot_'$file 
done

### pdf constructing ###
#pdftk *.pdf cat output out.pdf
