#!/usr/bin/env python

import sys
import math
import shapes
import turtle

def draw_triangle(area):
	#draw triangle
	canvas=turtle.Screen() # Create a playground for turtles
	#canvas.setup(400,200)
	turtle.begin_fill()
	turtle.colour('purple')
	turtle.forward.(area)        
	turtle.left(120)
	turtle.forward(area)
	turtle.left(120)
	turtle.forward(area)
	turtle.end_fill()
	canvas.exitonclick()	

def draw_square(area):
	#draw square
	canvas=turtle.Screen() # create a playground for turtles
	#canvas.setup(400,200)
	turtle.begin_fill()
	turtle.colour('green')
	turtle.forward(area)         
	turtle.left(90)
	turtle.forward(area)
	turtle.left(90)
	turtle.forward(area)
	turtle.left(90)
	turtle.forward(area)
	turtle.end_fill()     	
	canvas.exitonclick()	
	
def draw_circle(radius): #draw circle
	canvas = turtle.Screen() # create a playground for turtles
	#canvas.setup(400,200)
	turtle.begin_fill()
	turtle.colour('yellow')
	turtle.forward(radius) 
	turtle.end_fill()        
        canvas.exitonclick()

 

if __name__ == "__main__":
	draw_triangle(60)
	draw_square(60)
	draw_circle(50)
	
def draw(name,side,colour)
	if name == ('TRIANGLE'):
		draw_triangle(area,colour('purple'))
	if name == ('SQUARE'):
		draw_square(area,colour('green'))
	if name == ('CIRCLE'):
		draw_circle(radius,colour('yellow'))
else:
	pass
	
	draw_function("TRIANGLE",100)
	draw_function("SQUARE",100)
	draw_function("CIRCLE")
	
