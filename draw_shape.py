#!/usr/bin/python

import sys

import turtle # Necessary module to draw

from shapes import side

def draw (name, area):
	turtle.ht ()
	if name == "SQUARE":
		side1 = side (3, area)		
		turtle.forward (side1)
		turtle.left (90)
		turtle.forward (side1)
		turtle.left (90)
		turtle.forward (side1)
		turtle.left (90)
		turtle.forward (side1)
		turtle.home ()
	if name == "TRIANGLE":
		side1 = side (1, area)
		turtle.forward (side1)
		turtle.left (120)
		turtle.forward (side1)
		turtle.left (120)
		turtle.forward (side1)
		turtle.home ()
	if name == "CIRCLE":
		side1 = side (2, area)
		turtle.circle (side1)
		turtle.home ()
	turtle.exitonclick()		
draw ("SQUARE", 100)
