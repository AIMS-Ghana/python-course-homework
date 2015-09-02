#!usr/local/bin/python3
import turtle
import shape
import math
import sys


def draw_shape():
    turtle.bdcalor("red")
    turtle= turtle.turtle()
    turtle.shape("turtle")
    turtle.color("yellow")
    turtle.speed(2)
    turtle.exitonclick()

def CIRCLE(radius):
    turtle.circle(radius)

def n_side(n, side):
    turtle.forwad(side)
    turtle.right(30)
    turtle.forward(side)
    tuutle.exitonclick()
draw_CIRCLE()

def TRIANGLE(side):
    n_side(3,side)
    turtle.right(120)
    turtle.forwad(side)
    turtle.right(120)
    turtle.forwad(side)
    turtle.right(120)
    turtle.forwad(side)
    turtle.exitonclick()
draw_TRIANGLE()

def SQUARE(side):
    ngon(4,side)
    turtle.right(90)
    turtle.forwad(l)
    turtle.right(90)
    turtle.forwad(l)
    turtle.right(90)
    turtle.forwad(l)
    turtle.right(90)
    turtle.forwad(l)
    turtle.exitonclick()
draw_SQUARE()
figs = {
    'CIRCLE':circle,
    'SQUARE':square,
    'TRIANGLE':triangle
}

def draw(shape, area):
    dim = compute(shape, area)
    figs[shape](dim)
    turtle.exitonclick()


import sys 

if __name__ == "__main__":
    shape = sys.argv[1]
    area = float(sys.argv[2])
    draw(shape, area)


	

