#!/usr/bin/python
import turtle 

import shapes   

#draw a triangle
def triangle_shaper(side):
	turtle.begin_fill()
	turtle.color("yellow")
	turtle.forward(side)
	turtle.left(120)
	turtle.forward (side)
	turtle.left(120)
	turtle.forward(side)
	turtle.left(120)
	turtle.left(side)
	turtle.end_fill()
	turtle.left(60)
	

#draw a circle
def circle_shaper(radius):
	turtle.begin_fill()
	turtle.color("red")
	turtle.circle(radius)
	turtle.end_fill()
	turtle.left(60)
	

#draw a square
def square_shaper(side):
	turtle.left(60)
	turtle.begin_fill()
	turtle.color("green")
	turtle.right(90)
	turtle.forward(side)
	turtle.right(90)
	turtle.forward(side)
	turtle.right(90)
	turtle.forward(side)
	turtle.right(90)
	turtle.forward(side)
	turtle.end_fill()
	turtle.done()
	
if __name__ == "__main__":
	square_shaper(50)
	triangle_shaper(50)
	circle_shaper(10)
	
def draw(name,side,color):
	if name =="TRIANGLE":
		triangle_shaper(side,color('yellow'))
	if name =="SQUARE":
		square_shaper(side,color('green'))
	if name =="CIRCLE":
		circle_shaper(side,color('red'))
	else:
		pass




