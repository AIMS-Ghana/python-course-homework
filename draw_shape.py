#!/usr/bin/env python
import sys
import math
import shapes
import turtle


#Drawing triangle with area equals to 50000



def draw_triangle(triangle_side):
    window = turtle.Screen()
  
    tom = turtle.Turtle()
    tom.forward(triangle_side) 
    tom.color('red')
    tom.left(120)
    tom.forward(triangle_side)
    tom.color('red')
    tom.left(120)
    tom.forward(triangle_side)
    window.exitonclick() #to exit 


#Drawing square with area equals 50000

def draw_square(square_side):
    window = turtle.Screen()
    turtle.left(90)
    turtle.forward(square_side)
    turtle.color('green')
    turtle.left(90)
    turtle.forward(square_side)
    turtle.color('green')
    turtle.left(90)
    turtle.forward(square_side)
    turtle.color('green')
    turtle.left(90)
    turtle.forward(square_side)
    turtle.color('green')
    turtle.left(90)
    window.exitonclick() #to exit 


#Drawing circle with area of 50000
def draw_circle(circle_radius):
	window = turtle.Screen()
	circle_drw = turtle.Turtle()
	#circle_drw.speed(100)
	circle_drw.circle(circle_radius)
	window.exitonclick() #to exit 

if __name__ == "__main__":
	triangle = shapes.polygon_check('TRIANGLE',50000)
	triangle_name = triangle[0]
	triangle_side = float(triangle[1])
	draw_triangle(triangle_side)


	square = shapes.polygon_check('SQUARE',50000)
	square_side = float(square[1])
	draw_square(square_side)

	circle = shapes.polygon_check('CIRCLE',50000)
	circle_radius = float(circle[1])
	draw_circle(circle_radius)

def draw(polygon_name,area):
	if polygon_name =="TRIANGLE":
		triangle = shapes.polygon_check('TRIANGLE',area)
		draw_triangle(triangle[1])
	if polygon_name =="SQUARE":
		square = shapes.polygon_check('SQUARE',area)
		draw_square(square[1])
	if polygon_name =="CIRCLE":
		circle = shapes.polygon_check('CIRCLE',area)
		draw_circle(circle[1])
	else:
		pass







