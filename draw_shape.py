#!/usr/bin/python

import turtle
import shapes

def circle_shaper(radius):
        turtle.begin_fill()
        turtle.color("pink")
        turtle.circle(radius)
        turtle.end_fill()
        turtle.exitonclick()

def triangle_shaper(side):
        turtle.begin_fill()
        turtle.color("blue")
        turtle.forward(side)
        turtle.right(120)
        turtle.forward(side)
        turtle.right(120)
        turtle.forward(side)
        turtle.right(120)
        turtle.end_fill()
        turtle.exitonclick()

def square_shaper(side): 
	turtle.begin_fill() 
	turtle.color("indigo") 
	turtle.right(90) 
	turtle.forward(side) 
	turtle.right(90) 
	turtle.forward(side) 
	turtle.right(90) 
	turtle.forward(side) 
	turtle.right(90) 
	turtle.forward(side) 
	turtle.end_fill() 
	turtle.exitonclick()
	 
if __name__ == "__main__": 
	square_shaper(100) 
	triangle_shaper(100) 
	circle_shaper(50) 
	 
def draw(name,side,color): 
	if name =="TRIANGLE": 
		triangle_shaper(side,color('yellow')) 
	if name =="SQUARE": 
		square_shaper(side,color('green')) 
	if name =="CIRCLE": 
		circle_shaper(side,color('red')) 
	else: 
	     pass 




 
