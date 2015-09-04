#!/usr/bin/env python3
import math

class Shape:
    def kind(self):
        return "Shape"

    def invert_area(self, area):
       return area

    def dimname(self):
        return "HUH?"

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

    def draw(turt):
        pass
import turtle
class Triangle(Shape):
   def kind(self):
        return "triangle"
   def invert_area(self, area):
       return math.sqrt(float((area)*4)/math.sqrt(3))
   def dimname(self):
        return "side"
   def draw(turt):
   	for i in range(0,4):
	    turt=turtle.Turtle()
	    turt.foward(self.dim)
	    turt.left(90)

class Square(Shape):
    def kind(self):
        return "square"
    def dimname(self):
        return "side"
    def invert_area(self, area):
       return area**0.5
    def draw(turt):
    	for i in range(0,4):
	     turt=turtle.Turtle()
	     turt.foward(self.dim)
	     turt.left(90)
	
from math import pi

class Circle(Shape):
    def kind(self):
        return "circle"
    def dimname(self):
        return "radius"
    def invert_area(self, area):
       return float(math.sqrt(area/math.pi)) 
'''
    def draw(turt):
 turt=turtle.turtle(self.dim)
	turt.circle(self.dim)
import turtle
'''
if __name__ == "__main__":
    circ = Circle(10)
    sq=Square(5)
    tri=Triangle(5)
    print(circ)
    print(sq)
    print(tri)
   # circ.draw(turtle)
    sq.draw()
    tri.draw()
