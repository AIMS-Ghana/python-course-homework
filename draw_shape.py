#!/usr/bin/python
import turtle 

#draw a triangle
def triangle_sharper(length):
	turtle.forward(length)
	turtle.left(120)
	turtle.forward (length)
	turtle.left(120)
	turtle.forward(length)
	turtle.left(120)
	turtle.left(length)
	turtle.exitonclick()

#draw a circle
def circle_sharper(length):
	turtle.circle(length)
	turtle.exitonclick()

#draw a square
def square_sharper(length):
	turtle.right(90)
	turtle.forward(length)
	turtle.right(90)
	turtle.forward(length)
	turtle.right(90)
	turtle.forward(length)
	turtle.right(90)
	turtle.forward(length)
	turtle.done()
if __name__ == "__main__":
	square_sharper(50)
	triangle_sharper(50)
	circle_sharper(10)
	
def draw(name,length):
	if name =="TRIANGLE":
		triangle_sharper(length)
	if name =="SQUARE":
		square_sharper(length)
	if name =="CIRCLE":
		circle_sharper(length)
	else:
		pass




