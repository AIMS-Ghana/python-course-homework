#!/usr/bin/python3
from math import sqrt
import sys
from turtle import *
import shapes

def draw(name, area):
	if name== "TRIANGLE":
		#length= shapes.value
		#draw triangle
		canvas = Screen()
		#canvas.setup(400,200)
		grant = Turtle()
		grant.forward(area)          # make grant draw a square
		grant.left(120)
		grant.forward(area)
		grant.left(120)
		grant.forward(area)

		grant.exitonclick()	

	if name =="SQUARE":
		#draw square
		canvas = Screen()
		#canvas.setup(400,200)
		grant = Turtle()
		grant.forward(area)         
		grant.left(90)
		grant.forward(area)
		grant.left(90)
		grant.forward(area)
		grant.left(90)
		grant.forward(area)
              	
		grant.exitonclick()	
	
	if name =="CIRCLE":
		#draw cicrcle
		canvas = Screen()
		#canvas.setup(400,200)
		grant = Turtle()
		grant.forward(area)         
		
              	
		grant.exitonclick()	
	
if __name__ == "__main__":
	draw("TRIANGLE",100)
	draw("SQUARE",100)
	
