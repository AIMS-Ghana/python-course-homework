#!/usr/bin/env python

#!/usr/bin/python
#draw shapes of circle, equilateral triangle and square
import sys
import turtle
import shapes
import math
def draw_triangle(side):
    window = turtle.Screen()
    turtle.begin_fill()
    turtle.forward(side) 
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.end_fill()
    window.exitonclick()

def draw_square(width):
    win = turtle.Screen()
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.end_fill()
    win.exitonclick() #to exit

def draw_circle(rad):	
	window = turtle.Screen()
	turtle.begin_fill()
	circle_drw = turtle.Turtle()
	circle_drw.speed(20)
        circle_drw.circle(rad)
	turtle.end_fill()
	window.exitonclick() 
if __name__=="__main__":
	draw_triangle(100)
	draw_square(100)
	draw_circle(20)





'''
import shapes
import turtle

def circle(radius):
    turtle.circle(radius)
def ngon(n, side):
    turn = 180 - (n-2)*180.0/n
    for i in range(n-1):
        turtle.forward(side)
        turtle.right(turn)
    turtle.forward(side)

def triangle(side):
    ngon(3,side)

def square(side):
    ngon(4,side)

#defining shapes dictionary
shapes = {
    'CIRCLE':circle,
    'SQUARE':square,
    'TRIANGLE':triangle,
}

def compute():
	return (shape, area)
def draw(shape, area):
    dim = compute(shape, area)
    shapes[shape](dim)
    turtle.exitonclick()

import sys

if __name__ == "__main__":
    shape= sys.argv[1]
    area = float(sys.argv[2])
    draw(shape, area)

'''
