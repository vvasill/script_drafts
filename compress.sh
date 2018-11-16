#!/bin/sh
cd $1
mkdir './crop'
for FILE in *.JPG; 
do
	out='./crop/out_'$FILE
	convert $FILE -resize 50% $out
done
