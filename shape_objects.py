#!/usr/bin/python
import math
import csv
import turtle
class Shape:
    def kind(self):
        return "Shape"

    def invert_area(self, area):
        return area

    def dimname(self):
        return "Shape"

    def __init__(self, area):
        self.area = area
        self.dim = self.invert_area(area)

    strformat = "{}, area: {}, {}: {}"

    def __str__(self):
        return Shape.strformat.format(
          self.kind(),
          self.area,
          self.dimname(),
          self.dim
        )

    def draw(self):
        pass
#from math import pi
#import math
class Triangle(Shape):
	def kind(self):
        	return "Triangle"
	def invert_area(self, area):
        	return 2*area/(3**0.5)**0.5
	def dimname(self):
        	return "side"    
	def draw(self):		
		turtle.color('red')		
		turtle.begin_fill
		turtle.forward(self.area)
		turtle.left(120)
		turtle.forward(self.area)
		turtle.left(120)
		turtle.forward(self.area)
		turtle.end_fill
		turtle.exitonclick()

class Square(Shape):
	def kind(self): #, x , y, color):
		return "Square"	
	def invert_area(self, area):
        	return math.sqrt(area)
        	return "sq_side"    
	def draw(self):
	  	  for i in range(3):
			turtle.color('blue')		
			turtle.begin_fill() 
			turtle.forward(self.area)
			turtle.left(90)
		#turtle.forward(self.area)
		#turtle.left(90)
		#turtle.forward(self.area)
		#turtle.left(90)
		#turtle.forward(self.area)
		
class Circle(Shape):
	def kind(self):
        	return "Circle"
	def invert_area(self, area):
        	return math.sqrt(area/math.pi)
	def dimname(self):
        	return "radius"
	def draw(self):
		turtle.color('yellow')	
		turtle.begin_fill()        	
			
		turtle.circle(self.area)	
		turtle.end_fill()
class Rectangle(Shape):
	def kind(self):
        	return "Rectangle"
	def invert_area(self, area):
        	length = math.sqrt((area)/1.618)	
		width = math.sqrt((area)*1.618)
	def dimname(self, length, width):
        	return 'length','width '   
	def draw(self):
	     	
		for i in range(4):
			turtle.color('green')		
			turtle.begin_fill()			
			turtle.forward(self.area)
			turtle.left(90)
		

if __name__ == "__main__":
	circ = Circle(100)
	tri  = Triangle(100)
	sq  = Square(100)    	
	rec  = Rectangle(100) 	
	#print(tri)
	#print(circ)
	#print(sq)
	print(rec)
	circ.draw()
	sq.draw()
	tri.draw()
	rec.draw()

