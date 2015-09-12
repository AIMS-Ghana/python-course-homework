#!/usr/bin/env python

#!/usr/bin/python
#draw shapes of circle, equilateral triangle and square
import sys
import turtle
import math


def draw_triangle(side, col, angle, x, y):
	    turtle.ht()
            turtle.penup()
	    turtle.goto(x, y)
            turtle.pendown()
	    turtle.begin_fill()
            turtle.color(col)
            turtle.left(angle)
	    turtle.forward(side)     
	    turtle.left(120)
	    turtle.forward(side) 
	    turtle.left(120)
	    turtle.forward(side)
	    turtle.end_fill()	    

def draw_square(side, col, angle, x, y ):
            turtle.ht()
            turtle.penup()
	    turtle.goto(x, y)
            turtle.pendown()
	    turtle.begin_fill()
            turtle.color(col)
            turtle.left(angle)
            turtle.forward(side)
	    turtle.left(90)  
	    turtle.forward(side)
	    turtle.left(90)
	    turtle.forward(side)
	    turtle.left(90) 
            turtle.forward(side) 
	    turtle.end_fill()

def draw_circle(radius, col, angle, x, y):
	    turtle.ht()
            turtle.penup()
	    turtle.goto(x, y)
            turtle.pendown()
	    turtle.begin_fill()
            turtle.color(col)
            turtle.left(angle)
	    turtle.circle(radius)
	    turtle.end_fill()  
def draw_rectangle(side,b,col, angle, x, y):
	    turtle.ht()
            turtle.penup()
	    turtle.goto(x, y)
            turtle.pendown()
	    turtle.begin_fill()
            turtle.color(col)
            turtle.left(angle)
	    turtle.forward(side+b)
	    turtle.left(90)
	    turtle.forward(side)
	    turtle.left(90)  
	    turtle.forward(side+b)
	    turtle.left(90)
	    turtle.forward(side)
	    turtle.left(90)  
	    turtle.end_fill()





