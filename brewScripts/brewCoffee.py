#!/usr/bin/env python3"

#imports the raspberry pi GPIO system & time
import RPi.GPIO as GPIO
import time

#Sets syntax to BCM rather than Board
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#The set bcm pin used to signle
with open('bcm', 'r') as file:
    bcm = int(file.read())

#Sets up and initalizes BCM 26 for output
GPIO.setup(bcm, GPIO.OUT)
GPIO.output(bcm, GPIO.LOW)


def makeCoffee():
    #Might need to change depending on the coffee maker. If it is just a quick press, or to hold a connection.
    #Sets GCM to high for 2s
    GPIO.output(bcm, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(bcm, GPIO.LOW)
    GPIO.cleanup()

    print("Coffee is brewing!! ^_^ ")
