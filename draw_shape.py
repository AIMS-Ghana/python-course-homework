#!/usr/bin/env python


#draw shapes of circle, equilateral triangle and square
import sys
import turtle
#import shapes 
import math


def draw_triangle(side):
    
    turtle.forward(side) 
    turtle.left(120)
    turtle.forward(side) 
    turtle.left(120)
    turtle.forward(side) 
   
   
def draw_square(width):
   turtle.forward(width)
   turtle.left(90)
   turtle.forward(width)
   turtle.left(90)
   turtle.forward(width)
   turtle.left(90)


def draw_circle(rad):	
	#window = turtle.Screen()
    circle_drw = turtle.Turtle()
    circle_drw.speed(20)
    circle_drw.circle(rad)
	

def draw(a,b):
    window = turtle.Screen()
    draw_circle(b)
    draw_square(b)
    draw_triangle(b)
    window.exitonclick()

def compute(shape, area):
	return (shape, area)   

