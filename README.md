# Interfacing with the Panasonic AMG8833 Evaluation Kit

Building the following chain **sensor->arduino->processing** 


Added a function to make a 2d array representation of the data stream .  

## Required Libraries (included in data folder)
1. Wire.h
2. Grideye.h

## Circuit Connections
Arduino Pin | Sensor board Pin
------------|-----------------
A4(SCL)     |       D14
A5(SDA)     |       D15
5V          |       5V
GND         |       GND


## Output
![Output Image](/data/output.png)


### Get here: https://www.mouser.in/new/panasonic/panasonic-grid-eye-infrared-array-sensors/
