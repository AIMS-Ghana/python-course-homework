#!/usr/bin/python
#draw shapes of circle, equilateral triangle and square
import sys
import turtle
import shapes
import math
def draw_triangle(side):
	shape = turtle.Screen()
	window=turtle.Turtle()
	window.foward(side)
	window.left(120)
	turtle.foward(side)
	turtle.left(120)
	turtle.foward(side)
	turtle.left(120)
	shape.exitonclick()
draw_triangle(side)
def draw_square(width):
	shape = turtle.Screen()
	turtle.foward(width)
	turtle.left(90)
	turtle.foward(width)
	turtle.left(90)
	turtle.foward(width
	turtle.left(90)
	shape.exitonclick()
draw_square(width)
def draw_circle():	
	begin_fill()
while True:
    forward("CIRCLE")
    left(1)
    if abs(pos()) < 1:
        break
end_fill()
done()
draw_circle(radius)
def main():
	draw_triangle(side)
	draw_square(width)
	draw_circle(radius)
if __name__=="__main__":
	main()
