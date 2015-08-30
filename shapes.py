#!/usr/bin/python
# A program that prints the area and the perimeter of a triangle.
# im.save("rectangle.png")
import turtle
import math
def circle(radius):
    turtle.up()
    # go to (0, radius)
    turtle.goto(0,radius)
    turtle.down()
    turtle.color("black")
    # number of times the y axis has been crossed
    times_crossed_y = 0
    x_sign = 1.0
    while times_crossed_y <= 1:
        # move by 1/360 circumference
        turtle.forward(2*math.pi*radius/360.0)
        # rotate by one degree (there will be
        # approx. 360 such rotations)
        turtle.right(1.0)
        # we use the copysign function to get the sign
        # of turtle's x coordinate
        x_sign_new = math.copysign(1, turtle.xcor())
        if(x_sign_new != x_sign):
            times_crossed_y += 1
        x_sign = x_sign_new
    circle()
    area = math.pi*radius*radius
    turtle.done()
    return (a/math.pi)**0.5

def draw_square():
    canvas = Screen()
    canvas.setup(400,200)
    sarah = Turtle()
    sarah.forward(50)          # make sarah draw a square
    sarah.left(90)
    sarah.forward(50)
    sarah.left(90)
    sarah.forward(50)
    sarah.left(90)
    sarah.forward(50)
    sarah.left(90)
    area = left*left
    return a**0.5
    canvas.exitonclick()

def draw_triangle():
    window = turtle.Screen()
    window.bgcolor("green") #background color
    tom = turtle.Turtle()
    tom.forward(100)
    tom.left(120)
    tom.forward(100)
    tom.left(120)
    tom.forward(100)
    area = (left*left*(3**0.5))/4
    window.exitonclick() #to exit
    draw_triangle()
    return 2*math.sqrt(a(math.sqrt(3)))

import sys
if __name__ == "__main__":
    #name = {"CIRCLE": circle, "SQUARE": draw_square, "TRIANGLE": draw_triangle}
    area=float(sys.argv[2])
    name = list("CIRCLE", "SQUARE", "TRIANGLE")
    if name == CIRCLE:
        print (area/math.pi)**0.5
    elif name == SQUARE:
        print area**0.5
    elif name == TRIANGLE:
        print 2*math.sqrt(a(math.sqrt(3)))
    else:
        pass





