#!/usr/bin/python3
from math import sqrt
import sys
from turtle import *
import shapes

def draw(name, side):
	if name== "TRIANGLE":
		length= shapes.value
		#draw triangle
		canvas = Screen()
		#canvas.setup(400,200)
		turtle = Turtle()
		turtle.forward(side)             
		turtle.left(120)
		turtle.forward(side)    
		turtle.left(120)
		turtle.forward(side)    

		canvas.exitonclick()	

	if name =="SQUARE":
	        side=shapes.value		
		#draw square
		canvas = Screen()
		#canvas.setup(400,200)
		turtle= Turtle()
		turtle.forward(side)         
		turtle.left(90)
		turtle.forward(side)
		turtle.left(90)
		turtle.forward(side)
		turtle.left(90)
		turtle.forward(side)
              	
		canvas.exitonclick()	
	
	if name =="CIRCLE":
		side=shapes.value		
		#draw cicrcle
		canvas = Screen()
		#canvas.setup(400,200)
		turtle = Turtle()
		turtle.forward(side)         
		
              	
		canvas.exitonclick()	
	
if __name__ == "__main__":
	draw("TRIANGLE",100)
	draw("SQUARE",100)
	draw("CIRCLE" ,100)
