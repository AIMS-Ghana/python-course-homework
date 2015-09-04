#!/usr/bin/env python
import sys
import math
import shapes
import turtle
import shape_objects

#Drawing triangle with area equals to 50000



def draw_triangle(triangle_side,fill="black"):
    window = turtle.Screen()
  
    tom = turtle.Turtle()
    tom.color(fill)
    tom.fill(True)
    tom.begin_fill()

    tom.forward(triangle_side) 
   
    tom.left(120)
    tom.forward(triangle_side)
    #tom.color('red')
    tom.left(120)
    tom.forward(triangle_side)
    tom.end_fill()
    window.exitonclick() #to exit 


#Drawing square with area equals 50000

def draw_square(square_side,fill="red"):
    window = turtle.Screen()
    turtle.color(fill)
    turtle.fill(True)
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(square_side)
    
    turtle.left(90)
    turtle.forward(square_side)
   
    turtle.left(90)
    turtle.forward(square_side)
    
    turtle.left(90)
    turtle.forward(square_side)
   
    turtle.left(90)
    turtle.end_fill()
    #window.exitonclick() #to exit 


#Drawing circle with area of 50000
def draw_circle(circle_radius,fill="blue"):
	window = turtle.Screen()
	circle_drw = turtle.Turtle()
	circle_drw.color(fill)
        circle_drw.fill(True)
        circle_drw.begin_fill()
	#circle_drw.circle(circle_radius)
	#circle_drw.pos(10, 10)
	
	while True:
		
		circle_drw.forward(circle_radius)
		#turtle.color('blue')
		circle_drw.left(-1.15)
		if abs(circle_drw.pos())<1:
			break


        circle_drw.end_fill()
	#window.exitonclick() #to exit 

if __name__ == "__main__":
	
	circle = shapes.polygon_check('CIRCLE',50)
	circle_radius = float(circle[1])
	draw_circle(circle_radius)

	square = shapes.polygon_check('SQUARE',50000)
	square_side = float(square[1])
	draw_square(square_side)


	triangle = shapes.polygon_check('TRIANGLE',50000)
	triangle_name = triangle[0]
	triangle_side = float(triangle[1])
	draw_triangle(triangle_side)


	

	

def draw(polygon_name,area,fill="black",cont=False):
	if polygon_name =="TRIANGLE":
		triangle = shapes.polygon_check('TRIANGLE',area)
		draw_triangle(triangle[1],fill)
	if polygon_name =="SQUARE":
		square = shapes.polygon_check('SQUARE',area)
		draw_square(square[1],fill)
	if polygon_name =="CIRCLE":
		circle = shapes.polygon_check('CIRCLE',area)
		draw_circle(circle[1],fill)
	else:
		pass






