#!/usr/bin/env python

# Beginnings of Raspberry Pi/ Google Maps code
# by: Hannah Voelker for BME 193 EDP
# Before running, in terminal: pip install python-gmaps
# http://python-gmaps.readthedocs.io/en/latest/gmaps.html#module-gmaps.directions
# Also need to install Raspberry Pi OS

# Goals of the script:
# Get directions
# Continually utilize phone GPS to get current location, update in realtime (this is the hard part)
# Translate direction to signals to the Pi

from gmaps import Geocoding
import sys
import RPi.GPIO as GPIO
api = Geocoding(api_key='AIzaSyD-N-kTKBqfodgjss0D11npHEhYyoG-_gQ')
pd = 27 # data pin

def main():
	setup()
	# these can be incorporated in a later stage
	# start = sys.argv[1]
	# end = sys.argv[2]
	# mode = sys.argv[3]
	# api.Directions(start, end, mode)
	right_turn()
	time.sleep(3)
	left_turn()
	time.sleep(3)
	keep_going()
	time.sleep(3)
	wrong_way()

# this code is based off the linksprite buzzer info I found online, can change

def right_turn():
	buzz(1,5)
	time.sleep(1)
	buzz(1,5)

def left_turn():
	buzz(2,10)

def keep_going():
	buzz(0.5,20)

def wrong_way():
	buzz(4, 5)
	time.sleep(0.5)
	buzz(4, 5)
	time.sleep(0.5)
	buzz(4,5)
	
# freq in Hz
def buzz(duration, freq):
	GPIO.output(pd, 0)
	for i in range(1,duration):
		GPIO.output(pd, 1)
		time.sleep(0.001)
		GPIO.output(pd, 0)
		time.sleep(1.0/freq)

	GPIO.output(pd, 0)

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pd, GPIO.OUT)
	GPIO.output(pd, 0)


def buzzPwm(duration, freq):
	p = GPIO.PWM(pd,freq)
	p.start(50)
	time.sleep(float(duration)/1000)
	p.stop()


if __name__ == '__main__':
	main()
