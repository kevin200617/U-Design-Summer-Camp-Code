#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import *

m1 = Motor('outA')
m2 = Motor('outB')
sp = 500
def moveForward(t):
	m1.run_forever(speed_sp = sp)
	m2.run_forever(speed_sp = sp)
	sleep(t)

moveForward(2.9)

m1.stop()
m2.stop()