#!/usr/bin/python3

import sys
from math import *

try:
	global a
	global b
	global c

	a = sys.argv[1]
	b = sys.argv[2]
	c = sys.argv[3]

except IndexError:
	print ("invalid argument entered")
	quit()
except NameError:
	print ("invalid argument entered")
	quit()

def check_and_init(a,b,c):
	if len(sys.argv) != 4:
		print ("invalid number of sides entered. The number of sides should be 3")
		quit()
	else:
		try:	
			global a1
			global b1
			global c1
			global S
			global A2
					
			a1 = float(a)
			b1 = float(b)
			c1 = float(c)

			s = (a1 + b1 + c1)/2
			A2 = s*(s - a1)*(s - b1)*(s - c1)
			
			return a1
			return b1
			return c1
			return s
			return A2

			
		except ValueError:
			print ("the length can not be a string")
			quit()
def check(a1,b1,c1):
	if A2 <= 0:
		print ("invalid triangle entered. The lengths violate the triangle ineqaulity")
		quit()
	elif a1 <= 0 or b1 <= 0 or c1 <= 0:
		print ("length can not be negative or none-zero")
		quit()
	else:
		pass


def perimeter(a,b,c):
	check_and_init(a,b,c)
	check(a1,b1,c1)
	perimeter = a1 + b1 + c1
	return perimeter

		
def area(a,b,c):
	check_and_init(a,b,c)
	check(a1,b1,c1)
	area = sqrt(A2)
	return area

print("area " , area(a,b,c))
print("perimeter " , perimeter(a,b,c))
