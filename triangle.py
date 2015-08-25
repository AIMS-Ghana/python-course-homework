#!/usr/bin/python
import sys
import math
if len (sys.argv) != 4:
	print "Error!"
elif len (sys.argv) == 4:
	if float (sys.argv [1]) < 0 or float (sys.argv [2]) < 0 or float (sys.argv [3] < 0):
		print "Error!"	
	else :
		p = (float (sys.argv [1]) + float (sys.argv [2]) + float (sys.argv [3])) / 2	
		area = math.sqrt (p * (p - float (sys.argv [1])) * (p - float (sys.argv [2])) * (p - float (sys.argv [3])))
		perimeter = float (sys.argv [1]) + float (sys.argv [2]) + float (sys.argv [3])	
		print "area " + str (area) + "\nperimeter " + str (perimeter)
