#!/usr/bin/env python3

#All brewScripts are should be located in ./brewScripts

from brewCoffee import makeCoffee
import subprocess

def brewLauncher():
    print("brewLauncher v1.0    (no updates expected)")
    print("")
    print("1) brewCoffee    2) brewTime     3) brewStartup      else) exit")
    option = input("Please Select an option by inputing the coresponding number: ")
    if option is "1":
        makeCoffee()
        print("Attempting to brew coffee!")
        print("Will now exit!")
        exit()
    elif option is "2":
        subprocess.call("brewSchedule.sh")
    elif option is "3":
        subprocess.call("brewStartup.sh")
        exit()
    else:
        exit()

brewLauncher()
