#!/usr/bin/python
#draw shapes of circle, equilateral triangle and square
import sys
import turtle
#import shapes
import math
def draw_triangle(side,fill,angle,x,y):
    turtle.penup()
    turtle.ht()
    turtle.setpos(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(fill)
    turtle.left(angle)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.end_fill()
    

def draw_square(width,fill,angle,x,y):
    turtle.penup()
    turtle.ht()
    turtle.setpos(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(fill)
    turtle.left(angle)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.end_fill()

def draw_circle(rad,fill,angle,x,y):	
    turtle.penup()
    turtle.ht()
    turtle.setpos(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(fill)
    turtle.left(angle)
    turtle.circle(rad)
    turtle.end_fill()

def draw_rect(a,b,fill,angle,x,y):
    turtle.penup()
    turtle.ht()
    turtle.setpos(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(fill)
    turtle.left(angle)
    turtle.forward(a+b)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a+b)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.end_fill()

def draw(a,b):	
    draw_triangle(b)
    draw_square(b)
    draw_crcle(b)

