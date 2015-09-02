#!/usr/bin/python
from turtle import*
import shapes
import sys
def draw(a,b):
	if(a=="SQUARE"):
		l=shapes.side_triangle_func(b)
		forward(l)
		left(90)
		forward(l)
		left(90)
		forward(l)
		left(90)
		forward(l)
		exitonclick()
	elif(a=="TRIANGLE"):
		l=shapes.side_triangle_func(b)	
		forward(l)
		left(120)
		forward(l)
		left(120)
		forward(l)
		exitonclick()
	else:
		l=shapes.radius_circle_func(b)
		circle(l)
		exitonclick()
if __name__=='__main__':
	a=sys.argv[1]
	b=float(sys.argv[2])
	assert b>0 ,"there is an error"
	assert a=="TRIANGLE" or a=="SQUARE" or a=="CIRCLE", "...error indicating no input..."
	draw(a,b)	

		

