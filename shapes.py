#!/usr/bin/python
import math

def side (x, y):
	if x == 1:
		side = math.sqrt (4 * float (y)/ math.sqrt (3))
	if x == 2:
		side = math.sqrt(float (y) / 3.14)
	if x == 3:
		side = math.sqrt(y)
	return side


if __name__ == "__main__":
	import sys
	if len (sys.argv) < 3:
		print "Incomplete"
	elif len (sys.argv) == 3:
		c = float (sys.argv [2])
		if str (sys.argv [1]) != "TRIANGLE" and str (sys.argv [1]) != "CIRCLE" and str (sys.argv [1]) != "SQUARE":
			print "Undefined"
		elif str (sys.argv [1]) == "TRIANGLE":
			print "equilateral TRIANGLE, area {} , side {}".format (c, side (1, c))
		elif str (sys.argv [1]) == "CIRCLE":
			print "CIRCLE, area {} , radius {}".format (c, side (2, c))
		elif str (sys.argv [1]) == "SQUARE":
			print "SQUARE, area {} , side {}".format (c, side (3, c))
	elif len (sys.argv) > 3:
		print "Too many inormation"

