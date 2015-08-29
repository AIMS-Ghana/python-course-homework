#!/usr/bin/python3

import sys
from math import *

if __name__ == "__main__":
	try:
		global r	
		r = sys.argv[1]

	except IndexError:
		print ("invalid arguments entered")
		quit()

def check(r):
	try:
		r1 = float(r)
	
		if __name__ == "__main__":		
			if len(sys.argv) != 2:
				print ("invalid argument entered. just enter the radius")
				quit()
			else:
				pass
		elif float(r1) <= 0:
			print ("radius can not be less than or equal to zero")
			quit()
		else:
			pass
	except ValueError:
		print ("invalid radius. radius can not be a string")
		quit()

def area(r):
	check(r)
	r1 = float(r)
	area = pi*(r1**2)
	return area

def perimeter(r):
	check(r)
	r1 = float(r)
	perimeter = 2*pi*r1
	return perimeter

if __name__ == "__main__":
	print ("area ",area(r))
	print ("perimeter ",perimeter(r))
