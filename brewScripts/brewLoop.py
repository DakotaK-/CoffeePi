#!/usr/bin/env python3

from datetime import datetime, date, timedelta
import ./brewCoffee.py
import time
import threading

run = False

def timeCheck():
    run = True
    while run is True:
        now = datetime.strftime(datetime.now(), "%H:%M:%S")
        with open('brewTime', 'r') as file:
            brewTime = file.read()

        print(brewTime)

        if now == brewTime:
            makeCoffee()
            print("Brewing")
            break

        else:
            print(now)
        time.sleep(1)
    time.sleep(3)
    timeCheck(brewTime)

timeCheck()
