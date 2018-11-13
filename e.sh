#/bin/bash

list="skype gnome-software update-notifier evolution"

for name in $list
do	
	ps aux | grep $name | awk '{print $2}' > PID_list
	cat PID_list | while read -r PID
	do
		echo $PID
		kill -s 15 $PID
	done
	rm PID_list
	echo $name
done
