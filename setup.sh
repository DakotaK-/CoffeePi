#!/bin/bash

# Moved all nessecary files to ~/brewPi, for easy installation
echo Moving all files to home directory ~/brewPi
echo
mkdir ~/brewPi
mv ./brewScripts ~/brewPi
mv ./README.md ~/brewPi
echo Files Moved!
echo

# Makes all files nessecary exectuable
echo Making all files executable.
echo
chmod +x ~/brewPi/brewScripts/brewLauncher.py
chmod +x ~/brewPi/brewScripts/brewCoffee.py
chmod +x ~/brewPi/brewScripts/brewLoop.py
chmod +x ~/brewPi/brewScripts/brewSchedule.sh
chmod +x ~/brewPi/brewScripts/brewStartup.sh
chmod +x ~/brewPi/brewScripts/.brewCommand.sh
chmod +x ~/brewPi/brewScripts/.commandbrewCoffee.py
echo All files now exectuable
echo

# Asks for user to designate GPIO pin in BCM format for usage
echo choose GPIO to use from output using the BCM number. Default used is 21
echo Note! To change later, you will need to change the number in ~/brewPi/brewScripts/bcm
read varbcm
echo
echo $varbcm > ~/brewPi/brewScripts/bcm

# Initializes brewTime to kill
echo kill > ~/brewPi/brewScripts/brewTime
echo bcm has been successfully set to $varbcm
echo brewTime has been initialized
echo

# Will append custome alias commands to ~/.bash_aliases for easy usage.
echo Will now setup alias commands in ~/.bash_aliases
sleep 3s
echo  >> ~/.bash_aliases
echo \#Below are the aliase commands from brewPi >> ~/.bash_aliases
echo alias brewLauncher='~/brewPi/brewScripts/brewLauncher.py'
echo alias brewCoffee='~/brewPi/brewScripts/.commandbrewCoffee.py'
echo alias brewTime='~/brewPi/brewScripts/brewSchedule.sh'
echo alias brewStartup='~/brewPi/brewScripts/brewStartup.sh'
echo alias brewHelp='echo Usage: brewLauncher, brewCoffee, brewTime, and brewStartup'
echo \#Above are the aliase commands from brewPi >> ~/.bash_aliases
echo Custom Commands installed in ~/.bash_aliases

echo Use brewHelp to see usage
sleep 4
echo

# Cleans up install folder, but removing it's self directory. Including this script.
echo Setup succesful, will now cleanup
cd -P ..
rm -R $OLDPWD
echo $OLDPWD removed
echo cleanup done
sleep 1

#resets terminal window to allow custome command usage.
reset

exit
