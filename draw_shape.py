#!/usr/bin/python
import sys
import shapes
import turtle





def draw_circle(radius, fill='black'):
    turtle.color(fill)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

    turtle.exitonclick()
     

def draw_square(side, fill='red'):
    turtle.color(fill)
    turtle.begin_fill()
    
   
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)  
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)  
    turtle.end_fill()
	
    turtle.exitonclick()
 

def draw_triangle(side, fill='green', cont=True):
    turtle.color(fill)
    turtle.begin_fill()
    
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.end_fill()

    turtle.exitonclick()

def draw(name, area, fill='black', cont=True):

    if name == "TRIANGLE":
       draw_triangle(area)
    elif name == "CIRCLE": 
       draw_circle(area)  
    elif name == "SQUARE":
       draw_square(area)
    if not cont:
       turtle.exitonclick()


if __name__ == "__main__":
	draw_triangle(shapes.triangle_side(9000))
	draw_square(shapes.square_side(5000))
	draw_circle(shapes.circle_radius(3000))


