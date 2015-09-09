#!/usr/bin/python
import shapes
import sys
import math

import turtle

# The golden ratio. phi = 1.61803..

def draw(d, r, col, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(r)
    turtle.begin_fill()
    turtle.pendown()
    for i in range(4):
        turtle.color(col)
        turtle.forward(d)
        turtle.left(90)
    turtle.end_fill()




shapes = turtle.Turtle()



def draw_triangle(s, r, col, x, y):
    # turtle = turtle.Turtle()
    turtle.up()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(float(r))
    turtle.begin_fill()
    turtle.color(col)
    turtle.setheading(r)
    turtle.forward(s)
    turtle.left(120)
    turtle.forward(s)
    turtle.left(120)
    turtle.forward(s)
    turtle.left(120)
    turtle.forward(s)
    turtle.end_fill()





# wn = turtle.Screen()
# draw_triangle(50)
# draw_triangle(shapes.check("TRIANGLE",ar))

def Rect(t, r, col, x, y):

    Rct = turtle.Turtle()
    #Rct.shape("turtle")
    Rct.up()
    Rct.goto(x, y)
    Rct.pendown()
    Rct.begin_fill()
    Rct.color(col)
    Rct.setheading(r)
    Rct.forward(t)
    Rct.left(90)
    Rct.forward(t)
    Rct.left(90)
    Rct.forward(t)
    Rct.left(90)
    Rct.forward(t)
    Rct.end_fill()




# wn.title("RECTANGLE")
# Rect(60)
# Rect(shapes.check("RECTANGLE"),)


def CIRC(size, r, col, x, y):

    CIRCLE = turtle.Turtle()
    CIRCLE.up()
    CIRCLE.goto(x,y)
    CIRCLE.down()
    CIRCLE.setheading(r)
    CIRCLE.color(col)
    CIRCLE.fill(2)
    CIRCLE.circle(size)
    CIRCLE.fill(0)

