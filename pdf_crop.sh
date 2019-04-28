#!/bin/bash

check=odd
count=0

for file in *.pdf
do
	(( count++ ))
	pdfcrop $file './out/'$file 
	
	if [[ $count == 'odd' ]]
	then
		pdf270 './out/'$file -o './out/rot_'$file
		count=even
	else 
		pdf90 './out/'$file -o './out/rot_'$file
		count=odd
	fi

	mv './out/rot_'$file './out/'$file
	#pdftk './out/rot_'$file  multibackground $count'.pdf' output './out/'$file
	#rm './out/rot_'$file 
done

#pdftk astro_he_cover.pdf multibackground astro_he_001.pdf output outfile.pdf
