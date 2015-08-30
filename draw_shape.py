<<<<<<< HEAD
#!/usr/bin/env python3

import sys
from turtle import *
from shapes import *
if __name__=="__main__":
	a=sys.argv[1]
	b=sys.argv[2]
	if a=="square":
		color('red', 'yellow')
		begin_fill()
		forward(square_side(b))
		left(90)
		forward(square_side(b))
		left(90)
		forward(square_side(b))
		left(90)
		forward(square_side(b))
		end_fill()
		done()
	elif a=="Equilateral triangle":
		color('red', 'yellow')
		begin_fill()
		forward(triangle_side(b))
		left(120)
		forward(triangle_side(b))
		left(120)
		forward(triangle_side(b))
		end_fill()
		done()
	elif a=="Circle":
		color('red', 'yellow')
		begin_fill()
		circle(circle_side(b))
		end_fill()
		done()
	else:
		print("error, wrong shape")	
	
