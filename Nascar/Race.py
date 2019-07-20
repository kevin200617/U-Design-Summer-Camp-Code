#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import *

m1 = Motor('outA')
m2 = Motor('outB')
sp = 1000
btn = Button()


def moveForward(t):
	m1.run_forever(speed_sp = sp)
	m2.run_forever(speed_sp = sp)
	sleep(t)

def stopMoving():
	m1.stop()
	m2.stop()

Sound.beep().wait();


def up(state):
	if state:
		print('Up button pressed')
		Sound.beep().wait()
		Sound.beep().wait()
		moveForward(4.5) #change the 3 to whatever you want
		stopMoving()
		exit()
	else:
		print('Up button released')

btn.on_up = up

while True:
	btn.process() # Check for currently pressed buttons. 
	sleep(0.01)  # buttons state will be checked every 0.01 second
	
exit()
