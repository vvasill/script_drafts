#!/bin/bash

cd '/media/vasiliy/PENDRIVE'

cat md5sum.txt | while read sum_line
do
	str=( $sum_line )
	name=${str[1]}

	check_line=$( md5sum $name )

	if [[ $check_line == $sum_line ]]
	then
		echo 'ok'
	else
		echo 'FAIL'
	fi
done
