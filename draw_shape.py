#!/usr/bin/python3
import turtle

from shapes import calc_shape

def circle(radius):
    turtle.circle(radius)

def n_sides(n, side):
    turn = 180 - (n-2)*180.0/n
    for i in range(n-1):
        turtle.forward(side)
        turtle.right(turn)
    turtle.forward(side)

def triangle(side):
    n_sides(3,side)

def square(side):
    n_sides(4,side)

figs = {
    'CIRCLE':circle,
    'SQUARE':square,
    'TRIANGLE':triangle
}

def draw(shape, area, fill="blue", cont=False):
    dim = calc_shape(shape, area)
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
