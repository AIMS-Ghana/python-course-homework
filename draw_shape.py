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
		uche = Turtle()
		uche.forward(area)         # make sarah draw a square
		uche.left(120)
		uche.forward(area)
		uche.left(120)
		uche.forward(area)

		canvas.exitonclick()	

	if name =="SQUARE":
		#draw square
		canvas = Screen()
		#canvas.setup(400,200)
		uche = Turtle()
		uche.forward(area)         
		uche.left(90)
		uche.forward(area)
		uche.left(90)
		uche.forward(area)
		uche.left(90)
		uche.forward(area)
              	
		canvas.exitonclick()	
	
	if name =="CIRCLE":
		#draw cicrcle
		canvas = Screen()
		#canvas.setup(400,200)
		uche = Turtle()
		uche.forward(area)         
		
              	
		canvas.exitonclick()	
	
if __name__ == "__main__":
	draw("TRIANGLE",100)
	draw("SQUARE",100)
	
