#!/usr/bin/env python3
# so that script can be run from Brickman
'''
This is a working stable code for making the motor run for about 20 seconds
'''
from ev3dev.ev3 import *
from time import sleep;
dis = UltrasonicSensor('in4')
m1 = Motor('outA');
m2 = Motor('outB');
m3 = Motor('outC')
cs = ColorSensor('in1'); 
cs.mode = 'COL-COLOR';
d = 150
def whack():
	m3.run_forever(speed_sp=1000)
	
def moveForward():
	m1.run_forever(speed_sp=-1000);
	m2.run_forever(speed_sp=-1000);

def moveBackward():
	m1.run_forever(speed_sp=1000);
	m2.run_forever(speed_sp=1000);
	
def rotate():
	m1.run_forever(speed_sp=-1000);
	m2.run_forever(speed_sp=700);

moveForward()
time.sleep (.05)	
m1.stop
m2.stop																																																																																																																																																																																																															;	
seconds_to_last = 30;
marked_time = time.time();
condition = True; 
Sound.beep().wait();

Sound.beep().wait();
while(condition):
	print("{} seconds went by".format(time.time() - marked_time));
	if(cs.value() == 1):
		moveBackward();
		time.sleep(.5);
		rotate();
		time.sleep(0.25);
		moveForward();
		whack()
	if(time.time() - marked_time > seconds_to_last):
		condition = False;
	
	moveForward();
	whack()
	if(cs.value() == 1):
		moveBackward();
		time.sleep(.5);
		rotate();
		time.sleep(0.25);
		moveForward();
		whack()
	
m1.stop();
m2.stop();
m3.stop()

time.sleep(3);
#sleep(30)   # Give the motor time to move