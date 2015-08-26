#!/usr/bin/env python
import sys
import math
import shapes
import turtle


#Drawing triangle with area equals to 50000



def draw_triangle(triangle_side):
    #window = turtle.Screen()
  
    tom = turtle.Turtle()
    tom.forward(triangle_side) 
    tom.color('red')
    tom.left(120)
    tom.forward(triangle_side)
    tom.color('red')
    tom.left(120)
    tom.forward(triangle_side)
    #window.exitonclick() #to exit 


#Drawing square with area equals 50000

def draw_square(square_side):
    #window = turtle.Screen()
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
    #window.exitonclick() #to exit 


#Drawing circle with area of 20
def draw_circle(circle_radius):
	window = turtle.Screen()
	circle_drw = turtle.Turtle()
	circle_drw.speed(20)
	#circle_drw.pos(10, 10)
	
	while True:
		
		circle_drw.forward(circle_radius)
                turtle.color('blue')
		circle_drw.left(-1.15)
		if abs(circle_drw.pos())<1:
			break
	window.exitonclick() #to exit 

if __name__ == "__main__":
	triangle = shapes.polygon_check('TRIANGLE',50000)
	triangle_name = triangle[0]
	triangle_side = float(triangle[1])
	draw_triangle(triangle_side)


	square = shapes.polygon_check('SQUARE',50000)
	square_side = float(square[1])
	draw_square(square_side)

	circle = shapes.polygon_check('CIRCLE',20)
	circle_radius = float(circle[1])
	draw_circle(circle_radius)

def draw(polygon_name,area):
	if polygon_name =="TRIANGLE":
		draw_triangle(area)
	if polygon_name =="SQUARE":
		draw_square(area)
	if polygon_name =="CIRCLE":
		draw_circle(area)
	else:
		pass







