#!/usr/bin/python

import sys
import shapes
import turtle


def draw_circle(area):
    radius=shapes.circle(a)	
    turtle.circle(radius)
    turtle.exitonclick()

def draw_square(area):
    side=shapes.square(a)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.exitonclick()
	
def draw_triangle(area):
    side=shapes.triangle(a)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.exitonclick()

def draw(name,area):
    if name=="CIRCLE":
            draw_circle(area)
    elif name=="SQUARE":
            draw_square(area)
    elif name=="TRIANGLE":
            draw_triangle(area)
    else :
	 pass

		


if __name__ == "__main__":

	
    area=sys.argv[2]
    name=sys.argv[1]
    draw(name,area)
    
   
