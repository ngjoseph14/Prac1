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

# Logic that you write

def main():
	time.sleep(.001)

# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:

	GPIO.setmode(GPIO.BCM)

	chan_list_in = [23, 24]
	GPIO.setup(chan_list_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.add_event_detect(23,GPIO.RISING,callback=increment,bouncetime=150)
	GPIO.add_event_detect(24,GPIO.RISING,callback=decrement,bouncetime=150)
	
	chan_list_out = [17, 22, 27]
	GPIO.setup(chan_list_out, GPIO.OUT)
	GPIO.output(chan_list_out, GPIO.LOW)

        while True:
        	main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except:
      	GPIO.cleanup()
       	print("Some other error occurred")
        print(e.message)
