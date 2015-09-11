
#!/usr/bin/env python

import sys
from turtle import *
#from shapes import *
import math


def square_side(area):
	return area**0.5


def triangle_side(area):
	return 2*(area / 3**0.5)**0.5



def circle_radius(area):
	return (area/ math.pi)**0.5

def draw_polygon (Shape, area):
	if Shape =="square":
		color('red')
		begin_fill()
		forward(square_side(area))
		left(90)
		forward(square_side(area))
		left(90)
		forward(square_side(area))
		left(90)
		forward(square_side(area))
		end_fill()
		done()
	elif Shape =="Equilateral triangle":
		color('yellow')
		begin_fill()
		forward(triangle_side(area))
		left(120)
		forward(triangle_side(area))
		left(120)
		forward(triangle_side(area))
		end_fill()
		done()
	elif Shape =="Circle":
		color('red')
		begin_fill()
		circle(circle_radius(area))
		end_fill()
		done()
	else:
		print("error, wrong shape")	
if __name__=="__main__":
	import sys
	Shape = sys.argv[1]
	area = sys.argv[2]
		return draw_polygon(Shape , area)


#if __name__=="__main__":
#	a=sys.argv[1]
#	b=sys.argv[2]
	
