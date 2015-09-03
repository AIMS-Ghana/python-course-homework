#!/usr/bin/python
#equilateral triangle, find side,print area and side
#square,find side, print area and side
#circle:find radius, print area and radius
import math
import sys	
def triangle(b):
	side=math.sqrt((float(b)*4)/math.sqrt(3))#heros formula calculation of the area to get the side
	return side
def square(b):
	value=math.sqrt(float(b))
	return value
def circle(b):
	radius=math.sqrt(float(b)/math.pi)
	return radius
def check(a,b):
	if a=="TRIANGLE":
		return triangle(b)
	elif a=="SQUARE":
		return square(b)
	elif a=="CIRCLE":
		return circle(b)
	else:
		return "wrong shape"	

def shape_print(a, b):
	if a=="TRIANGLE":
		print 'equilateral triangle, area: ',b,'side: ',check(a,b)
	elif a=="SQUARE":
		print 'area: ',b,'side:',check(a,b)
	elif a=="CIRCLE":
		print 'area: ',b,'side:',check(a,b)
if __name__=="__main__":
	a=sys.argv[1]
	b=sys.argv[2]
	shape_print(a,b)
		
