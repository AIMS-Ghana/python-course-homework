#!/usr/bin/env python
# Make all the "turtle" commands available to us.
import sys
import shapes
import turtle


# Create a new turtle.

screen = turtle.getscreen()
def draw_triangle(area):
	side = shapes.triangle_side(area)
	n = 3
	int_angle = ((n-2)*180.0)/n
	turn = 180 - int_angle
	polygon = turtle.Turtle()
	polygon.begin_fill()
	polygon.color('blue')
	for i in range(1,n+1):
		polygon.forward(side)
		polygon.left(turn)
	polygon.end_fill()
	polygon.exitonclick()	

def draw_square(area): #draw square
	side = shapes.square_side(area)
	n = 4
	int_angle = ((n-2)*180.0)/n
	turn = 180 - int_angle
	polygon = turtle.Turtle()
	polygon.begin_fill()
	polygon.color('green')
	for i in range(1,n+1):
		polygon.forward(side)
		polygon.left(turn)
	polygon.end_fill()
	turtle.exitonclick()	
	
def draw_circle(area): #draw circle
	radius = shapes.circle_radius(area)
	polygon = turtle.Turtle()
	polygon.begin_fill()
	polygon.color('red')
	circle = turtle.circle(radius)
	polygon.end_fill()
	turtle.exitonclick()
	
def draw(shape,area):
	if shape == 'TRIANGLE':
		draw_triangle(area)
	if shape == 'SQUARE':
		draw_square(area)
	if shape == 'CIRCLE':
		draw_circle(area)
	else:
		pass

#draw(sys.argv[1],int(sys.argv[2]))
draw("CIRCLE", 5000)
draw("SQUARE", 5000)
draw("TRIANGLE", 5000)
