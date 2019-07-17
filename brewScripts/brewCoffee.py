#!/usr/bin/env python3

"""
shebang uses python. Note must change to the following for python3:
!/usr/bin/env python3
"""


"""
Place this file in home directory with:
    $ mv MakeFuckingCoffee.py ~/
Mark this file as executable with:
    $ chmod +x ~/MakeFuckingCoffee.py
Finally to run do:
    $ ./MakeFuckingCoffee.py
"""

#imports the raspberry pi GPIO system & time
#import RPi.GPIO as GPIO
import time

#Sets syntax to BCM rather than Board
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarning(False)

#The set bcm pin used to signle
with open('bcm', 'r') as file:
    bcm = file.read()

#Sets up and initalizes BCM 26 for output
#GPIO.setup(bcm, GPIO.out, inital=GPIO.LOW)


def makeCoffee():
    #Might need to change depending on the coffee maker. If it is just a quick press, or to hold a connection.
    #Sets GCM 26 to high for 0.5s
    '''
    GPIO.output(bcm, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(bcm, GPIO.LOW)
    GPIO.cleanup()
    '''

    print(bcm)
    print("Coffee is brewing!! ^_^ ")
