#!/usr/bin/python
import shapes
import sys
import math
import turtle

def draw_square(area): 
	side = shapes.square(area) 
	turtle.forward(side)
	turtle.left(90)
	turtle.forward(side)
   	turtle.left(90)
   	turtle.forward(side)
   	turtle.left(90)
	turtle.forward(side)

def draw_triangle(area):
	side = shapes.triangle(area)
	turtle.forward(side)
   	turtle.left(120)
   	turtle.forward(side)
   	turtle.left(120)
   	turtle.forward(side)
   	turtle.left(120)
	turtle.forward(side)
	
def draw_circle(area):
	radius = shapes.circle(area)
	turtle.circle(radius)
       
def draw(name, area):
    if name == "CIRCLE":
       draw_circle(area)    	  
    elif name == "SQUARE":
       draw_square(area)
    elif name == "TRIANGLE":
       draw_triangle(area)
    else:
	pass
if __name__ == "__main__":
	draw(name, area)
	for i in range(3):
            i.draw()

