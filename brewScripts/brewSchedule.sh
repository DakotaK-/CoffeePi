#!/bin/bash
echo Input time in to change to in form of %H:%M:%S
echo type \"off\" to turn off, and \"kill\" to end the process
read -p 'Enter: ' time
echo $time > ./brewScripts/brewTime
echo brewTime set to $time
echo will now exit!
exit
