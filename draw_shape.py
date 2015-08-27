#!/usr/bin/python
import  math 
import sys
import shapes
import turtle

def draw_circle(radius):
    #canvas = Screen()
    win=turtle.screen()
   # r=shapes.circle_side(area)
    turtle.circle(radius)
    #canvas.exitonclick()

def draw_square(side):
    #s=shapes.square_side(area)
    #canvas = Screen()
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    #canvas.exitonclick()


def draw_triangle(side):
   # s=shapes.triangle_side(area)
    #canvas = Screen()
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
   # canvas.exitonclick()

if __name__ == "main__":
    draw_triangle(shapes.triangle_side(400))
    draw_square(shapes.square_side(400))
    draw_circle(shapes.circle_radius(300))

