#!/usr/bin/python3

import sys
import shapes
import turtle


def draw_circle(area):
    #turtle.color(fill)
    #turtle.begin_fill()
    radius=shapes.circle_radius(area)	
    turtle.circle(radius)
    #turtle.end_fill()
    #goto
    turtle.exitonclick()

def draw_square(area):
    #turtle.color(fill)
    #turtle.begin_fill()
    side=shapes.square_side(area)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    #turtle.end_fill()
    turtle.exitonclick()
	
def draw_triangle(area):
    #turtle.color(fill)
    #turtle.begin_fill()
    side=shapes.triangle_side(area)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    #turtle.end_fill()
    turtle.exitonclick()

def draw(name,area,fill="black",cont=True):
    if name=="CIRCLE":
            draw_circle(area)
    elif name=="SQUARE":
            draw_square(area)
    else:
            draw_triangle(area)

		


if __name__ == "__main__":

	
    area=sys.argv[2]
    name=sys.argv[1]
    draw(name,area,fill='black')
    
   
