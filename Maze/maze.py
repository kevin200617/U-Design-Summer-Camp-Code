#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import *
dis = UltrasonicSensor('in1')
angle = GyroSensor('in3')
#for motor
m1 = Motor('outA')
m2 = Motor('outB')
#for gyro
sp = 900
angle.mode='GYRO-ANG' # Put the gyro sensor into ANGLE mode.
units = angle.units
path = 1
d = 180
n =1
#funcations
def stopMoving():
	m1.stop()
	m2.stop()
	
def moveForward():
	m1.run_forever(speed_sp = sp)
	m2.run_forever(speed_sp = 0.93*sp)
	sleep(.1)	


	
def turnRight(turnAngle):
	degree = angle.value()
	Sound.beep().wait();
	while(degree-angle.value() > -turnAngle):
		m1.run_forever(speed_sp=150);
		m2.run_forever(speed_sp=-150);
	stopMoving();


		
def turnLeft(turnAngle):
	degree = angle.value()
	Sound.beep().wait();
	while(degree-angle.value() < turnAngle):
		m1.run_forever(speed_sp=-150);
		m2.run_forever(speed_sp=150);
	stopMoving();
	
while (n == 1):
	if (path == 1):	#straight
		moveForward()
		sleep(.1)
		while (path == 1):
			if (dis.value()< d):
				#print(dis.value())
				path = path + 1
				stopMoving()
				break
				
	if (path == 2):	#left
		turnLeft(75)
		sleep(.1)
		path =  path + 1
				
	if (path == 3):	#straight
		moveForward()
		sleep(.1)
		while (path == 3):
			if (dis.value()< d):
				#print(dis.value())
				path = path + 1
				stopMoving()
				break
				
	if (path == 4):	#right
		turnRight(80)
		sleep(.1)
		path =  path + 1
				
	if (path == 5):	#straight
		moveForward()
		sleep(.1)
		while (path == 5):
			if (dis.value()< d):
				#print(dis.value())
				path = path + 1
				stopMoving()
				break
				
	if (path == 6):	#left
		turnLeft(75)
		sleep(.1)
		path =  path + 1
				
	if (path == 7):	#straight
		moveForward()
		sleep(.1)
		while (path == 7):
			if (dis.value()< d):
				#print(dis.value())
				path = path + 1
				stopMoving()
				break
				
	if (path == 8):	#left
		turnLeft(75)
		sleep(.1)
		path =  path + 1
				
	if (path == 9):	#straight
		moveForward()
		sleep(.1)
		while (path == 9):
			if (dis.value()< d):
				#print(dis.value())
				path = path + 1
				stopMoving()
				break
				
	if (path == 10):	#right
		turnRight(80)
		sleep(.1)
		path =  path + 1
		
	if (path == 11):	#straight
		moveForward()
		sleep(.1)
		while (path == 11):
			if (dis.value()< d):
				#print(dis.value())
				path = path + 1
				stopMoving()
				break
	if (path == 12):	#right
		turnRight(70)
		sleep(.1)
		path =  path + 1
		
	if (path == 13):	#straight
		m1.run_forever(speed_sp = sp)
		m2.run_forever(speed_sp = 0.93*sp)
		sleep(1)
		stopMoving()
		n = n + 1
		break