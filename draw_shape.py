#!/usr/bin/python3

import shapes
import turtle
scale = 1


def draw(type, area, fill = 'black', cont = False):
    turtle.color(fill)
    if type == "TRIANGLE":
       draw_triangle(shapes.triangle(area),fill)
    elif type == "SQUARE":
       a = shapes.square(area)
       draw_rectangle(a,a,fill)
    elif type == "RECTANGLE":
       phi = (1 + 5**(0.5)) / (2)
       a = (area / phi)**(0.5)
       b = a * phi
       draw_rectangle(a,b,fill)
    else:
       draw_circle(shapes.circle(area),fill)
    if not cont:
        turtle.exitonclick()


def draw_triangle(s,fill):
    turtle.fillcolor(fill)
    turtle.begin_fill()
    turtle.forward(s/2 * scale)
    turtle.left(120)
    turtle.forward(s * scale)
    turtle.left(120)
    turtle.forward(s * scale)
    turtle.left(120)
    turtle.forward(s/2 * scale)
    turtle.end_fill()

def draw_circle(s,fill):
    turtle.fillcolor(fill)
    turtle.begin_fill()
    turtle.circle(s * scale)
    turtle.end_fill()

def draw_rectangle(a,b,fill):
    turtle.fillcolor(fill)
    turtle.begin_fill()
    turtle.forward(b/2 * scale)
    turtle.left(90)
    turtle.forward(a * scale)
    turtle.left(90)
    turtle.forward(b * scale)
    turtle.left(90)
    turtle.forward(a * scale)
    turtle.left(90)
    turtle.forward(b/2 * scale)
    turtle.end_fill()
