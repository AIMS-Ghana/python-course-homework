#!/usr/bin/python3

import sys
import shapes
import turtle


def draw_circle(area):
    radius=shapes.circle_radius(area)	
    turtle.circle(radius)
    turtle.exitonclick()

def draw_square(area):
    side=shapes.square_side(area)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.exitonclick()
	
def draw_triangle(area):
    side=shapes.triangle_side(area)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.exitonclick()

def draw(name,area,fill="black", cont=False):
    turtle.begin_fill()
    #turtle.color ('red')
    #turtle.circle (40, steps = 3)
    turtle.end_fill()
    if name=="CIRCLE":
            draw_circle(area)
    elif name=="SQUARE":
            draw_square(area)
    else:
            draw_triangle(area)
		

if __name__ == "__main__":

	
    area=sys.argv[2]
    name=sys.argv[1]
    draw(name,area)
    
   
