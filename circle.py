#!/usr/bin/python
import sys
import math

#print(sys.argv[1])

r=int(sys.argv[1])
if(r<0):
	print("Error, you have been type an negative number. Retry")
	pass
else:
	area=math.pi*r**2
	perimeter=math.pi*2*r
	print"area ", area
	print "perimeter",perimeter
