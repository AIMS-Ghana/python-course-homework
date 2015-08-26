#!/usr/bin/python

from math import sqrt
import sys

from turtle import *
import shapes

def draw(area):
	if name== "TRIANGLE":
		length= shapes.value
		#draw triangle
		canvas = Screen()
		#canvas.setup(400,200)
		turtle = Turtle()
		turtle.forward(area)          # make sarah draw a square
		turtle.left(120)
		turtle.forward(area)
		turtle.left(120)
		turtle.forward(area)

		canvas.exitonclick()	

	if name =="SQUARE":
	        length=shapes.value		
		#draw square
		canvas = Screen()
		#canvas.setup(400,200)
		turtle= Turtle()
		turtle.forward(area)         
		turtle.left(90)
		turtle.forward(area)
		turtle.left(90)
		turtle.forward(area)
		turtle.left(90)
		turtle.forward(area)
              	
		canvas.exitonclick()	
	
	if name =="CIRCLE":
		lenght=shapes.value		
		#draw cicrcle
		canvas = Screen()
		#canvas.setup(400,200)
		kweku = Turtle()
		kweku.forward(length)         
		
              	
		canvas.exitonclick()	
	
if __name__ == "__main__":
	draw("TRIANGLE",100)
	draw("SQUARE",100)
	
