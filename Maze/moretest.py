#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import *
dis = Sensor('in1')
angle = Sensor('in2')
#for motor
m1 = Motor('outA')
m2 = Motor('outB')
#for gyro
sp = 900
angle.mode='GYRO-ANG' # Put the gyro sensor into ANGLE mode.
units = angle.units

#funcations
def stopMoving():
	m1.stop()
	m2.stop()
	
def moveForward(t):
	m1.run_forever(speed_sp = sp)
	m2.run_forever(speed_sp = 0.93*sp)
	sleep(t)	


	
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
	
moveForward(3);
stopMoving();