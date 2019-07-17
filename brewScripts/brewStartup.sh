#!/bin/bash

echo "kill" > ./brewScripts/brewTime.txt
sleep 4s
echo Type in a date in 24hr time in form %H:%M:%S.
echo use \"kill\" to deactivate brewSchedule, and \"off\" to turn off.
echo
read vartime
echo $vartime > ./brewScripts/brewTime
echo brewTime set to $vartime
#nohup ./brewScripts/brewLoop.py &
echo brewLoop started
echo
echo processes have been sucessfully started
echo will now exit
exit
