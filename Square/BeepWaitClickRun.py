#!/usr/bin/env python3
'''
The line above #!/usr/bin/env python3 has to be there
if you want to be able to run the code directly from the robot's
File Browser.

It has to be the very first line and no typo is allowed.

Make sure this file is in chmod 755
Ensure the EOL of this file is for Unix
Check to see if the file runs by opening Putty and do 
ls to see if file is green
Then type python3 filename.py to open the file to ensure there is no error
'''

#this line imports the ev3 library of code written by some programmer
#we use their library of code by calling it and the star means 
#import all the functions in the ibrary 
from ev3dev.ev3 import *

#similarly, we import the set of code written for the time library
#that way we can control the timing of the robot later on.
from time import *;

#This line tells the robot to beep and wait for the beep to 
#finish before moving on to the next line.
Sound.beep().wait();

#This line creates a variable btn to store the Buttons functions.
btn = Button()

# Do something when state of any button changes:
# This function is contains lines that can be used later on for 
# the up button.  In our case, when it is released, we make the robot beep
# twice and print out "Good bye" then end the progrqm.
def up(state):
    if state:
        print('Up button pressed');
        Sound.beep().wait();
        Sound.beep().wait();
        print("Good bye");
        exit();
    else:
        print('Up button released')

   
#Ths line is saying that when the button is up, call the up function above
#note that if you change the name of the function above to endProgr(state):
#then you will have to modify the line to btn.on_up = endProgram
btn.on_up = up

#This is a while loop that repatedly checks to see if anything is happening
#to the buttons.
while True:  # This loop checks buttons state continuously, 
             # calls appropriate event handlers
    btn.process() # Check for currently pressed buttons. 
    # If the new state differs from the old state, 
    # call the appropriate button event handlers.
    sleep(0.01)  # buttons state will be checked every 0.01 second

# If running this script via SSH, press Ctrl+C to quit
# if running this script from Brickman, long-press backspace button to quit
#technically, the next line will never be reached, do you kno why?
exit();
