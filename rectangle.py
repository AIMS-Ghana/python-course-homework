#!/usr/bin/python3

import sys
from math import *

try:
	global l
	global b
	l = sys.argv[1]
	b = sys.argv[2]

except IndexError:
	print ("invalid arguments entered")
	quit()

def check(l,b):
	try:
		global l1
		global b1

		l1 = float(l)
		b1 = float(b)

		if len(sys.argv) != 3:
			print ("invalid argument entered")
			quit()

		elif l1 <= 0 or b1 <= 0:
			print ("invalid length enthered")
			quit()
		
		else:
			return l1
			return b1

	except ValueError:
		print ("the length and breadth can not be a strings")
		quit()

def area(l,b):
	check(l,b)
	area = l1*b1
	return area

def perimeter(l,b):
	check(l,b)
	perimeter = (l1 + b1)*2
	return perimeter

print ("area " , area(l,b))
print ("perimeter " , perimeter(l,b))

