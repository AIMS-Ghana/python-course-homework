#!/usr/bin/python
import sys
x=float(sys.argv[1])
y=float(sys.argv[2])
#calculating the area of rectangle
def area (x,y):
	check(x,y)
	return x*y
# calculating the perimeter of the rectangle
def perimeter(x,y):
	check(x,y)
	return 2*(x+y)
print "area{},perimeter{}".format(area(x,y),perimeter(x,y))
 
