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

import googlemaps
import sys
import time
import json
api = googlemaps.Client(key='AIzaSyD-N-kTKBqfodgjss0D11npHEhYyoG-_gQ')

def main():
	start = "4 Colby Street, Somerville, MA"
	end = "357 Boston Avenue, Medford, MA"
	mode = "walking"
	directions = api.directions(start, end, mode)
	# print json.dumps(directions, indent=4)
	parse_directions(directions)
	right_turn()
	time.sleep(3)
	left_turn()
	time.sleep(3)
	keep_going()
	time.sleep(3)
	wrong_way()

def parse_directions(directions):
	directions = directions[0]
	directions = directions["legs"]
	default = None
	for i in range(len(directions)):
		if directions[i]["distance"]:
			print "Total distance:"
			dist = directions[i]["distance"]
			dist = dist['text']
			print dist
# this code is based off the linksprite buzzer info I found online, can change

def right_turn():
	print("Right Turn Signal:")
	buzz(1,2)
	

def left_turn():
	print("Left Turn Signal:")
	buzz(1,3)

def keep_going():
	print("Keep going signal:")
	buzz(0.5,1)

def wrong_way():
	print("Wrong way signal:")
	buzz(4, 5)

def buzz(duration, freq):
	for i in range(freq):
		print("Buzz!")
	


if __name__ == '__main__':
	main()