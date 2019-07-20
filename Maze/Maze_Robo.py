#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import *

#defining sensor I/O
ts = Sensor('in1')
us = Sensor('in2')
gy = Sensor('in3')
d = 16 #distance from wall parameter
w = 1 
us.mode = 'US-DIST-CM'
distance = us.value()/10
#for motor
m1 = Motor('outA')
m2 = Motor('outB')
sp = 1000
#for gyro
gy = Sensor('in3')
ts = TouchSensor()

gy.mode='GYRO-ANG' # Put the gyro sensor into ANGLE mode.

units = gy.units
#funcations

def turnLeft():
	angle = gy.value()
	while (angle < 90):
		m1.run_forever(speed_sp = sp) #cheak here if there is a turning issue
		m2.run_forever(speed_sp = -1*sp)
		sleep(.1)
	
	if (angle <= 90): #expirment with this, Cheak if it will work if it is equel to 90
		print("angle is equel to 90")
		stop()
def turnRight():
	angle = gy.value()
	while (angle < 90):
		m1.run_forever(speed_sp = -1*sp) #cheak here if there is a turning issue
		m2.run_forever(speed_sp = sp)
		sleep(.1)
	
	if (angle <= 90): #expirment with this, Cheak if it will work if it is equel to 90
		print("angle is equel to 90")
		stop()	
def moveForward(t):
	m1.run_forever(speed_sp = sp)
	m2.run_forever(speed_sp = sp)
	sleep(t)	
if (distance <= d): # making distance into a binary value
	w = 1
	print ("Distance is more than:")
	print (d)
else: 
	w = 0
	print ("Distance is less than")
	print (d)


while (True):
	while (ts.value() != 1): #move forwards while there is not wall
		moveForward(.1)
	#touch sensor values
	if (ts.value() == 1): #if there is a wall, stop all motors
		stop()
		if (w == 1): #if there is a wall to the right, (This all means that there is a wall to the right and front
			turnLeft()
		else:
			turnRight() #these three lines are basically all the logic
exit();
