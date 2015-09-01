#!/usr/bin/python
import shapes
import sys
import math
#from turtle import *        # use types in the turtle module
#canvas = Screen()           # get a canvas/screen for a turtle to draw on
#canvas.setup(800,600)
import turtle



def draw_square(t, size):  #Make turtle t draw a square with sides of length, size.

    for i in range(4):
        t.forward(size)
        t.left(90)

turtle.setup(800, 600)
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("SHAPES")

shapes = turtle.Turtle()

draw_square(shapes, 20)  # call with draw_square function with turtle, alex, and size, 250

wn.exitonclick()






'''
import turtle
turtle.shape("turtle")  # set square's shape
SQUARE = Turtle()           #sets turtle's name to SQUARE
SQUARE.forward ( 90 )
SQUARE.right ( 90 )
SQUARE.forward ( 90 )
SQUARE.right ( 90 )
SQUARE.forward ( 90 )
SQUARE.right ( 90 )
SQUARE.forward ( 90)


TRIANGLE= Turtle()             # create a new turtle named mike
TRIANGLE.shape("turtle")        # set Triangle's shape
TRIANGLE.goto ( 0 , 60 )
TRIANGLE.forward ( 70 )
TRIANGLE.left ( 120 )
TRIANGLE.forward ( 70 )
TRIANGLE.left ( 120 )
TRIANGLE.forward ( 70)



CIRCLE= Turtle()             # create a new turtle named CIRCLE
CIRCLE.shape("turtle")        # set shape's shape
CIRCLE.up ( )
CIRCLE.goto ( 0 , 35 )
CIRCLE.down ( )
CIRCLE.color('red')
CIRCLE.fill ( 1 )
CIRCLE.circle ( 20 )
CIRCLE.fill ( 0 )


mike = Turtle()             # create a new turtle named mike
mike.shape("turtle")        # set mike's shape
mike.color("green")        # set mike's color to green
mike.forward(30)            # move mike forward 30 pixels
mike.right(90)              # turn mike right 90 degrees
mike.forward(50)            # move mike forward 50 pixels

'''


