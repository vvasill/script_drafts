#!/bin/sh
cd ./crop/pub/
for FILE in *_cr.JPG; 
do
	fn='./'$( echo $FILE | cut -d "_" -f 1 )'.jpg'
	mv $FILE $fn
done
