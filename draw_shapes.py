#!/usr/bin/python
import sys
import shapes
import turtle


def draw_circle(area):
    radius = shapes.circle_radius(area)	
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.exitonclick()

def draw_square(area):
    side = shapes.square_side(area)
    turtle.begin_fill()
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.end_fill()
    turtle.exitonclick()
	
def draw_triangle(area):
    side = shapes.triangle_side(area)
    turtle.color("blue")
    turtle.begin_fill()
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.end_fill()
    turtle.exitonclick()

def draw(name,area):
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
    
   


