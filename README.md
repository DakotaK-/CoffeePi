# brewPi

A set of Scripts and programs to designed for brewing coffee with a RaspberryPi connected to offee maker through a relay.

## Getting Started

You will need a RaspberryPi hooked up to a relay through whatever GPIO you wish to use. Note the GPIO pins BCM number, not the board number.
The pin used in my testing was BCM 21, the far top right pin if you look at the board from the top. This was just used for simplicity in remembering the location.



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

