#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <Nathan>
Student Number: <JSPNAT003>
Prac: <Prac_1>
Date: <18/04/1998>
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
from itertools import product

# Logic that you write
i = 0
a = [[0,1],[0,1],[0,1]]
b = list(product(*a))			#creates a list of binary values from 0 to 7 when converted to integers

def increment(channel):			#defined increment fucntion to increase value by 1 integer
	global i
	i+=1				#adds an integer of 1
	if i == 8:
		i = 0			#changes value to the lower limit when higher limit has been exceeded
	GPIO.output(17, b[i][0])
	GPIO.output(22, b[i][1])
	GPIO.output(27, b[i][2])

def decrement(channel):			#defined decrement function to decrease value by 1 integer
	global i
	i-=1				#subtracts an integer of 1
	if i == -1:
		i = 7			#changes value to the upper limit if lower limit has been exceeded
	GPIO.output(17, b[i][0])
	GPIO.output(22, b[i][1])
	GPIO.output(27, b[i][2])

def main():
	time.sleep(.001)

# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:

	GPIO.setmode(GPIO.BCM)		#sets numbering of pins to the BCM numbering system

	chan_list_in = [23, 24]
	GPIO.setup(chan_list_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)			#sets the pins to input and set default value to pull down - 0
	GPIO.add_event_detect(23,GPIO.RISING,callback=increment,bouncetime=150)		#add rising edge detection and initiate callback function increment
	GPIO.add_event_detect(24,GPIO.RISING,callback=decrement,bouncetime=150)		#add rising edge detection and initiate callback function decrement
	
	chan_list_out = [17, 22, 27]
	GPIO.setup(chan_list_out, GPIO.OUT)			#sets the pins to output mode
	GPIO.output(chan_list_out, GPIO.LOW)			#sets the pins' default value to low

        while True:
        	main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except:
      	GPIO.cleanup()
       	print("Some other error occurred")
        
