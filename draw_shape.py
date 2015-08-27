#!usr/local/bin/python3
import turtle
from shape import compute

def draw_square():
    window= turtle.screen()
    window.bdcalor("red")
    turtle= turtle.turtle()
    turtle.shape "turtle"
    turtle.calor "yellow"
    turtle.speed(2)
window.exitonclick()
draw_square()

def circle(radius):
    turtle.circle(radius)

def ngon(n, side):
    turtle.forwad(side)
    turtle.right(30)
    turtle.forward(side)

def triangle(side):
    ngon(3,side)
    turtle.right(120)
    turtle.forwad(120)

def square(side)
    ngon(4,side)
    turtle.right(90)
    turtle.forwad(100)
    turtle.right(90)
    turtle.forwad(100)
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


	

