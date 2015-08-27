#!/usr/bin/python 

import shapes
import turtle
scale = 10


def draw(type,area):
    if type == "TRIANGLE":
       draw_triangle(shapes.triangle(area))
    elif type == "SQUARE":
       a = shapes.square(area)
       draw_rectangle(a,a)
    elif type == "RECTANGLE":
       phi = (1 + 5**(0.5)) / (2)
       a = (area / phi)**(0.5)
       b = a * phi
       draw_rectangle(a,b)
    else:
       draw_circle(shapes.circle(area))


def draw_triangle(s):
    turtle.reset()
    turtle.penup()
    turtle.goto(0,-100)
    turtle.pendown()
    turtle.pensize(4)
    turtle.forward(s/2 * scale)
    turtle.left(120)
    turtle.forward(s * scale)
    turtle.left(120)
    turtle.forward(s * scale)
    turtle.left(120)
    turtle.forward(s/2 * scale)
    turtle.exitonclick()
def draw_circle(s):
    turtle.reset()
    turtle.pensize(4)
    turtle.penup()
    turtle.forward(s * scale)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(s * scale)
    turtle.exitonclick()
def draw_rectangle(a,b):
    turtle.reset()
    turtle.penup()
    turtle.goto(0,-100)
    turtle.pendown()
    turtle.pensize(4)
    turtle.forward(b/2 * scale)
    turtle.left(90)
    turtle.forward(a * scale)
    turtle.left(90)
    turtle.forward(b * scale)
    turtle.left(90)
    turtle.forward(a * scale)
    turtle.left(90)
    turtle.forward(b/2 * scale)
    turtle.exitonclick()
