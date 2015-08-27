#!/usr/bin/python3

import sys
import turtle
import shapes

def draw(name,area, fill ="black", cont=false):
	if name== "TRIANGLE":
		#side_length= shapes.value
		#draw triangle
		turtle.setup(400,200)
		turtle =Turtle()
		turtle.forward(side)             
		turtle.left(120)
		turtle.forward(side)    
		turtle.left(120)
		turtle.forward(side)    
		if not cont:
		
			turtle.exitonclick()	

	if name =="SQUARE":
	        #side=shapes.value		
		#draw square
		
		turtle.setup(400,200)
		turtle=Turtle()
		turtle.forward(side)         
		turtle.left(90)
		turtle.forward(side)
		turtle.left(90)
		turtle.forward(side)
		turtle.left(90)
		turtle.forward(side)
              	
		turtle.exitonclick()	
	
	if name =="CIRCLE":
		#radius=shapes.value		
		#draw cicrcle
		
		turtle.setup(400,200)
		turtle = Turtle()
		turtle.forward(radius)         
		
             	
		turtle.exitonclick()	
	
if __name__ == "__main__":
	draw("TRIANGLE",100)
	draw("SQUARE",100)
	draw("CIRCLE" ,100)
