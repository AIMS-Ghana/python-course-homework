#!/usr/bin/python
import sys
if (len (sys.argv) != 2 and len (sys.argv) != 3):
	print "Error!"
elif len (sys.argv) == 2:
	if float (sys.argv [1]) < 0:
		print "Error!"
	else :
		area = float (sys.argv [1]) ** 2
		perimeter = float (sys.argv [1]) * 4
		print "area " + str (area) + "\nperimeter " + str (perimeter) 
elif len (sys.argv) == 3:
	if float (sys.argv [1]) < 0 or float (sys.argv [2]) < 0:
		print "Error!"
	else :
		area = float (sys.argv [1]) * float (sys.argv [2])
		perimeter = (float (sys.argv [1]) + float (sys.argv [2])) * 2
		print "area " + str (area) + "\nperimeter " + str (perimeter)

