#!/usr/bin/python
import shapes
import sys
import math
# from turtle import *        # use types in the turtle module
# canvas = Screen()           # get a canvas/screen for a turtle to draw on
# canvas.setup(800,600)
import turtle

turtle.Screen()
g_ratio = (1+ math.sqrt(5))/2 # The golden ratio. phi = 1.61803..

def draw(d, r, col, x, y):  # Make turtle t draw a square with sides of length, size.
    turtle.penup()
    turtle.goto(x, y)
    turtle.begin_fill()
    turtle.color(col)
    turtle.setheading(r)
    for i in range(4):
        turtle.pendown()
        turtle.forward(d)
        turtle.left(90)
        turtle.end_fill()

    # t.goto(-34.00,)
    #  draw(shapes.check("SQUARE"))


# wn.title("SHAPES")


shapes = turtle.Turtle()


# draw(20)

def draw_triangle(edge_len, r, col, x, y):
    # turtle = turtle.Turtle()
    turtle.up()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(float(r))
    turtle.begin_fill()
    turtle.color(col)
    turtle.setheading(r)
    turtle.forward(edge_len)
    turtle.left(90)
    turtle.forward(edge_len* g_ratio)
    turtle.left(90)
    turtle.forward(edge_len)
    turtle.left(90)
    turtle.forward(edge_len* g_ratio)
    turtle.end_fill()
    turtle.setup(800, 600)
    turtle.end_fill()
    # turtle.color('purple')
    # turtle.fill(2)
    # turtle.triangle(edge_len)
    # turtle.fill(0)


# wn = turtle.Screen()
# draw_triangle(50)
# draw_triangle(shapes.check("TRIANGLE",ar))

def Rect(t, r, col, x, y):
    Rct = turtle.Turtle()  # create a new turtle named mike
    Rct.shape("turtle")
    Rct.up()
    Rct.goto(x, y)
    Rct.pendown()
    Rct.setheading(r)
    Rct.begin_fill()
    Rct.color(col)
    Rct.forward(t)
    Rct.left(90)
    Rct.forward(t)
    Rct.left(90)
    Rct.forward(t)
    Rct.left(90)
    Rct.forward(t)
    Rct.fill(32)
    Rct.color()


turtle.setup(800, 600)


# wn.title("RECTANGLE")
# Rect(60)
# Rect(shapes.check("RECTANGLE"),)


def CIRC(size, r, col, x, y):
    CIRCLE = turtle.Turtle()  # create a new turtle named CIRCLE
    CIRCLE.shape("turtle")  # set shape's shape
    CIRCLE.up()
    CIRCLE.goto(x,y)
    CIRCLE.down()
    CIRCLE.setheading(r)
    CIRCLE.color(col)
    CIRCLE.fill(2)
    CIRCLE.circle(size)
    CIRCLE.fill(0)


turtle.setup(800, 600)
# wn = turtle.Screen()
# wn.title("CIRCLE")
# CIRC(shapes.check("CIRCLE"))
# CIRC(80)  # call with draw_square function with turtle, alex, and size, 250

turtle.exitonclick()
