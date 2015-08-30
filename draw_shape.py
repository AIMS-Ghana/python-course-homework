#!/usr/bin/env python

import shapes
import turtle

def circle(radius):
    turtle.circle(radius)
def ngon(n, side):
    turn = 180 - (n-2)*180.0/n
    for i in range(n-1):
        turtle.forward(side)
        turtle.right(turn)
    turtle.forward(side)

def triangle(side):
    ngon(3,side)

def square(side):
    ngon(4,side)

#defining shapes dictionary
shapes = {
    'CIRCLE':circle,
    'SQUARE':square,
    'TRIANGLE':triangle,
}

def compute():
	return (shape, area)
def draw(shape, area):
    dim = compute(shape, area)
    shapes[shape](dim)
    turtle.exitonclick()

import sys

if __name__ == "__main__":
    shape= sys.argv[1]
    area = float(sys.argv[2])
    draw(shape, area)


