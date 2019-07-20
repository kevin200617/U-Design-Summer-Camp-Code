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
cs = ColorSensor('in1'); 
cs.mode = 'COL-COLOR';
touch = TouchSensor('in2')
def moveForward():
	m1.run_forever(speed_sp=900);
	m2.run_forever(speed_sp=900);

def moveBackward():
	m1.run_forever(speed_sp=-900);
	m2.run_forever(speed_sp=-900);
	
def rotate():
	m1.run_forever(speed_sp=-900);
	m2.run_forever(speed_sp=230);

Sound.beep().wait();
while (touch.value() == 0):
	Sound.speak("please press my buttons").wait()
	print("no code running")
Sound.beep().wait()
moveForward()
time.sleep(.7)
seconds_to_last = 65;
marked_time = time.time(); 
condition = True;
while(condition):
	print("{} seconds went by".format(time.time() - marked_time));
	if(cs.value() == 1):
		moveBackward();
		time.sleep(.7);
		rotate();
		time.sleep(0.15);
		moveForward();

	if(time.time() - marked_time > seconds_to_last):
		condition = False;
	
	moveForward();
	if(cs.value() == 1):
		moveBackward();
		time.sleep(.7);
		rotate();
		time.sleep(0.15);
		moveForward();
	
m1.stop();
m2.stop();

time.sleep(3);
#sleep(30)   # Give the motor time to move