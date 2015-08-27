#!/usr/bin/python
import turtle
from shape

def ngon(n, side):
    turn = 180 - (n - 2)* 180.0/2
for i in range (n - 1)
    turtle.forward (side)
    turtle.right (turn)
    turtle.forward (side)

def circle (radius):
     turtle.circle(radius)
    
def triangle(side):
    ngon (3, side)

def square(side):
    ngon(4,side)

figs = {'CIRCLES': circle, 'SQUARE':square, 'TRIANGLE':triangle}

def draw(shape,area,fill ="black",cont=false):
    dim =shape.figure_check(shape,area)
    turtle.color
    figs[shape](dim)
    turtle.exitonclick()

import sys
if __name__ == "__main__":
   side_triangle = shapes.figure_check('TRIANGLE' ,70000)
   draw('TRIANGLE' ,side_triangle)
   side_square=shapes.figure_check('SQUARE' ,70000)
   radius_circle=shapes.figure_check('CIRCLE ,70000)
   draw('CIRCLE' ,radius_circle)
