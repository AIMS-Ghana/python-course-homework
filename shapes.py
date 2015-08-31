#!/usr/bin/python3

from math import *
import sys

if __name__ == "__main__":
	try:
		global shape
		global area

		shape = sys.argv[1]
		area = float(sys.argv[2])

	except ValueError:
		print("Invalid area entered")
		quit()

	except IndexError:
		print("no shape and area entered")
		quit()

def check(area):
	if area <= 0:
		print ("Invalid area entered")
		quit()

def sq_side(area):
	check(area)
	return sqrt(area)

def tri_side(area):
	check(area)
	return (2*sqrt(area))/(3**(0.25))

def c_side(area):
	check(area)
	return sqrt(area/pi)

def side_calc(shape,area):
	side_ftns = {"CIRCLE":c_side, "TRIANGLE":tri_side, "SQUARE":sq_side}

	try :
		return side_ftns[shape](area)
	except:
		print ("wrong fig entered")
		quit()

if __name__ == "__main__":
	print (shape, " area : {0}, side {1}".format(area, side_calc(shape,area)))





