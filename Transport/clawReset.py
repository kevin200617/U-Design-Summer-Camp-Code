 #!/usr/bin/env python3
from ev3dev.ev3 import *
from time import *
dis = UltrasonicSensor('in1')
touch = TouchSensor('in2')
angle = GyroSensor('in3')
cs = ColorSensor('in4'); 
cs.mode = 'COL-COLOR';
#for motor
m1 = Motor('outA')
m2 = Motor('outB')
m3 = Motor('outC')
#for gyro
sp = 900
angle.mode='GYRO-ANG' # Put the gyro sensor into ANGLE mode.
units = angle.units
path = 1
d = 40
b = 2 # time for grabBall and realseBall
#funcations
def stopMoving():
	m1.stop()
	m2.stop()
def moveForward():
	m1.run_forever(speed_sp = sp)
	m2.run_forever(speed_sp = sp)
	sleep(.1)	
	
def turnRight(turnAngle):
	degree = angle.value()
	Sound.beep().wait();
	while(degree-angle.value() > -turnAngle):
		m1.run_forever(speed_sp=100);
		m2.run_forever(speed_sp=-100);
	stopMoving();
	
def turnLeft(turnAngle):
	degree = angle.value()
	Sound.beep().wait();
	while(degree-angle.value() < turnAngle):
		m1.run_forever(speed_sp=-100);
		m2.run_forever(speed_sp=100);
	stopMoving();
def grabBall():
	m3.run_forever(speed_sp = -900)
	sleep(b)#b varbile is for time
	m3.stop()
def releaseBall():
	m3.run_forever(speed_sp = 900)
	sleep(b)
	m3.stop()
def moveBackward(t):
	m1.run_forever(speed_sp=-900);
	m2.run_forever(speed_sp=-900);
	sleep(t)
turnLeft(85)
	
