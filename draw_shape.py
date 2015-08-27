#!/usr/bin/python
from turtle import*
import shapes
import sys
def draw(a,b):
	if(b=="SQUARE"):
		l=shapes.side_triangle_func(a)
		forward(l)
		left(90)
		forward(l)
		left(90)
		forward(l)
		left(90)
		forward(l)
		exitonclick()
	elif(b=="TRIANGLE"):
		l=shapes.side_triangle_func(a)	
		forward(l)
		left(120)
		forward(l)
		left(120)
		forward(l)
		exitonclick()
	else:
		l=shapes.radius_circle_func(a)
		circle(l)
		exitonclick()
if __name__=='__main__':
	b=sys.argv[1]
	a=float(sys.argv[2])
	assert a>0 ,"there is an error"
	assert b=="TRIANGLE" or b=="SQUARE" or b=="CIRCLE", "...error indicating no input..."
	draw(a,b)	

		

