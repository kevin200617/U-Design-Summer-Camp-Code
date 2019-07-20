#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import *
dis = Sensor('in1')
angle = Sensor('in2')
#for motor
m1 = Motor('outA')
m2 = Motor('outB')
#for gyro
sp = 1000
gy.mode='GYRO-ANG' # Put the gyro sensor into ANGLE mode.
units = gy.units

def turnRight:
	degree = angle.val()
	print(degree)
	while (degree >90):
		m1.run_forever(speed_sp = sp)
		m2.run_forever(speed_sp = -1*sp)
		sleep(.1)
		degree = angle.val()
		print("in while statment turnRight")
		print("degrees ="
		print(degree)
turnRight()
