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
	
def draw_triangle(are):
	side=shapes.triangle_side(area)
	turtle.forward(side)
	turtle.left(120)
	turtle.forward(side)
	turtle.left(120)
	turtle.forward(side)
	turtle.exitonclick()		


if __name__ == "__main__":

	
	area=sys.argv[2]
	name=sys.argv[1]
	def draw(name,area):
		if name=="CIRCLE":
			draw_circle(area)
		elif name=="SQUARE":
			draw_square(area)
		else:
			draw_triangle(area)
            
	#draw_triangle(shapes.triangle_side(7000))
	#draw_square(shapes.square_side(7000))
	#draw_circle(shapes.circle_radius(7000))	

