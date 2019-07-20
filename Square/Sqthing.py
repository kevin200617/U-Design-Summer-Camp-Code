#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import *

m1 = Motor('outA')
m2 = Motor('outB')
sp = 1000
ts = 250
timeforward = 1.7 #1.7


def moveForward(t):
	m1.run_forever(speed_sp = sp)
	m2.run_forever(speed_sp = sp)
	sleep(t)

def turnRight(t):
	m1.run_forever(speed_sp = -1*ts)
	m2.run_forever(speed_sp =  ts)
	sleep(t)
	
def turnLeft(t):
	m1.run_forever(speed_sp = ts)
	m2.run_forever(speed_sp = -1*ts)
	sleep(t)

def stopMotor():
	m1.stop()
	m2.stop()
	
Sound.speak("3,2,1, Drop it!").wait()
for i in range(3):
	moveForward(timeforward)
	turnLeft(.52)
moveForward(1.5)

stopMotor()
Sound.speak("2 plus 2 is 4, minus one is three, quick maths. Ski, rah, pow pow pow pow pow. Yuh ").wait()


