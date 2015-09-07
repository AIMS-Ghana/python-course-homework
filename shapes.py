#!/usr/bin/python
import sys
from math import*
import circle
import rectangle
import triangle
def side_triangle_func(s):
	return (2*sqrt(s/(sqrt(3))))
def side_square_func(s):
	return sqrt(s)
def radius_circle_func(s):
	return sqrt(s/pi)
if __name__=='__main__':
	v=sys.argv[1]
	s=float(sys.argv[2])
	assert s>0 ,"there is an error"
	assert v=="TRIANGLE" or v=="SQUARE" or v=="CIRCLE", "...error indicating no input..."
	if(v=="TRIANGLE"):
		u=side_triangle_func(s)
		print"equilateral",v," area",s," side=",u
	elif(v=="SQUARE"):
		u=side_square_func(s)
		print v,"area",s,"side:",u
	else:
		u=radius_circle_func(s)
		print v,"area",s,"radius:",u

