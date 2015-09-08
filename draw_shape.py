#!/usr/bin/python


import turtle

from shapes import compute

def circle(radius):
    turtle.circle(radius)


def triangle(side):
    turtle.triangle(side)

def square(side):
    turtle.square(side)

figs = {
    'CIRCLE':circle,
    'SQUARE':square,
    'TRIANGLE':triangle
}

def draw(shape, area, fill="black", cont=False):
    dim = compute(shape, area)
    turtle.color(fill)
    turtle.begin_fill()
    figs[shape](dim)
    turtle.end_fill()
    if not cont:
        turtle.exitonclick()

import sys

if __name__ == "__main__":
    shape = sys.argv[1]
    area = float(sys.argv[2])
    draw(shape, area)
