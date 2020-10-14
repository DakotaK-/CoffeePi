# brewPi

A set of Scripts and programs to designed for brewing coffee with a RaspberryPi connected to offee maker through a relay.

## Getting Started

You will need a RaspberryPi hooked up to a relay through whatever GPIO you wish to use. Note the GPIO pins BCM number, not the board number.
The pin used in my testing was BCM 21, the far top right pin if you look at the board from the top. This was just used for simplicity in remembering the location.

### Installing

**This is all very homebrew, and I suggest an understanding to be able to edit the files yourself if you wish to use/build off this.**
**Use caution when installing, this likly will not receieve any more support and is here for viewing**

Download as a zip anywhere on the RaspberryPi distro.
Make the setup.sh executable with the following, in the same directory as it.

```
chmod +x ./setup.sh
```

Then run the setup.sh with the following

```
./setup.sh
```
It will install all files in to your home directory located in ~/brewPi
It will also ask you what BCM pin.


Now all you need to run whenever you want to brew coffee is ~/brewPi/brewScripts/brewLauncher.py


### Usage

brewPi can be used in many ways, however the easiest way is through the brewLauncher.
The brewLauncher will give you three options

####  1) brewCoffee
This will send a signle to brew coffee imediatly. Usage is simple.

####  2) brewTime
This will allow you to change the brewTime or rather the scheduled time for it to automatically brew.
The time must be put in 24 hr time, and is based on the time on the RaspberryPi. It also needs to be formated as %H:%M:%S
ex.
```
13:04:12
```
You can also pass two other arugments
```
kill
```
will end the current loop, and require you to run brewStartup to re start the schedule, and
```
stop
```
will simple cause the loop to not trigger, and dose not require brewStartup to start the schedule again.

#### 3) brewStartup
This must be called before you can use the schedule function. It will startup the schedule loop in the background and ask for a time, view above for the following argument you can use.

### Changing settings
Many settings can be changed, but must be done through editing the files.

#### BCM Pin
Changing the bcm pin will require to to manually edit the bcm file this can be done with the following.
```
nano ~/brewPi/brewScripts/bcm
```
Change the file to whatever bcm pin you wish to use.
<kbd>Control</kbd> + <kbd>X</kbd> to exit, and then _y_ to save.

#### makeCoffee()
You may be required to edit the makeCoffee() function in ~/brewPi/brewScripts/brewCoffee.py to better fit your coffee maker.
The default code sends a pulse to the activate the coffee maker button once, due to my Coffee make automatically turning off. 
However if yours dosent you may need to _send one pulse to turn on, and one to turn off,_ or _turn it on for a set amount of time, then turn it off._

The following function is written as below
```python
def makeCoffee():
    GPIO.output(bcm, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(bcm, GPIO.LOW)
    GPIO.cleanup()
```

it must end with GPIO.cleanup(), and the pin should be set to GPIO.LOW at the end to turn off the pin.
use bcm in place of the pin, and change the bcm file if needed.
You can change the pule duration, make it pulse twice just using GPIO.output(), and time.sleep()
note that time.sleep() will be in seconds unless otherwise delcared.
