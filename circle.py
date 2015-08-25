#!/usr/bin/python
import sys
pi = 3.14
if len (sys.argv) != 2:
	print "Error!"
if len (sys.argv) == 2:
	if float (sys.argv [1]) < 0:
		print "Error!"
	else:
		area = (float (sys.argv [1]) ** 2) * pi
		perimeter = float (sys.argv [1]) * 2 * pi
		print "area " + str (area) + "\nperimeter " + str (perimeter) 

