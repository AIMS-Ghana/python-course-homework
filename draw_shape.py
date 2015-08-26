#!/usr/bin/python
import sys
import shapes
import turtle
def draw (name, area):
	turtle.ht ()
	if name == "SQUARE":
		side = shapes.side (3, area)		
		turtle.forward (side)
		turtle.left (90)
		turtle.forward (side)
		turtle.left (90)
		turtle.forward (side)
		turtle.left (90)
		turtle.forward (side)
		turtle.home ()
	if name == "TRIANGLE":
		side = shapes.side (1, area)
		turtle.forward (side)
		turtle.left (120)
		turtle.forward (side)
		turtle.left (120)
		turtle.forward (side)
		turtle.home ()
	if name == "CIRCLE":
		side = shapes.side (2, area)
		turtle.circle (side)
		turtle.home ()
	turtle.exitonclick()		
if __name__ == "__main__":
	name = str (sys.argv [1])
	area = float (sys.argv [2])
	draw (name, area)
