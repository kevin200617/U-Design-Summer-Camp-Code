#!/usr/bin/env python3
# so that script can be run from Brickman
'''
This is a working stable code for making the motor run for about 20 seconds
'''
from ev3dev.ev3 import *
from time import sleep;

m1 = Motor('outA');
m2 = Motor('outB');
m3 = Motor('outC')
def whack():
	m3.run_forever(speed_sp=1000)
Sound.beep().wait();

Sound.beep().wait();

whack()
sleep(5)
m3.stop
#sleep(30)   # Give the motor time to move