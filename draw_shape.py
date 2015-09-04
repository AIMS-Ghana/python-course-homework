#!/usr/bin/python
#draw shapes of circle, equilateral triangle and square
import sys
import turtle
#import shapes
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
def draw(a,b):	
    draw_triangle(b)
    draw_square(b)
    draw_circle(b)

