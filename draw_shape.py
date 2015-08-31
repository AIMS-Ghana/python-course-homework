#!usr/local/bin/python3
import turtle
import shape
import maths
import sys


def draw_shape():
    window= turtle.screen()
    window.bdcalor("red")
    turtle= turtle.turtle()
    turtle.shape("turtle")
    turtle.color("yellow")
    turtle.speed(2)
window.exitonclick()
draw_shape()

def circle(radius):
    turtle.circle(radius)

def ngon(n, side):
    turtle.forwad(side)
    turtle.right(30)
    turtle.forward(side)
window.exitonclick()
draw_circle()

def triangle(side):
    ngon(3,side)
    turtle.right(120)
    turtle.forwad(side)
    turtle.right(120)
    turtle.forwad(side)
    turtle.right(120)
    turtle.forwad(side)
window.exitonclick()
draw_triangle()

def square(side):
    ngon(4,side)
    turtle.right(90)
    turtle.forwad(l)
    turtle.right(90)
    turtle.forwad(l)
    turtle.right(90)
    turtle.forwad(l)
    turtle.right(90)
    turtle.forwad(l)
window.exitonclick()
draw_square()
figs = {
    'circle':circle,
    'square':square,
    'triangle':triangle
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


	

