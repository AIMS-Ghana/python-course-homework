#!/usr/bin/env python3

from math import sqrt
import sys
class Shape:
    def kind(self):
        return "Shape"

    def invert_area(self, area):
        return area

    def dimname(self):
        return "HUH?"

    def __init__(self, area):
        self.__area = area
        self.__dim = self.invert_area(area)

    strformat = "{}, area: {}, {}: {}"

    def __str__(self):
        return Shape.strformat.format(
          self.kind(),
          self.__area,
          self.dimname(),
          self.__dim
        )

    def draw(turt):
        pass

class Triangle(Shape):
    def kind(self):
        return "Triangle"
    def invert_area(self, area):
        return (sqrt(area*4)/(sqrt(3)))
    def dimname(self):
        return "triangle_side"
    pass

class Square(Shape):
    def kind(self):
        return "Square"
    def invert_area(self, area):
        return (area/4)
    def dimname(self):
        return "square_side"
    pass

from math import pi

class Circle(Shape):
    def kind(self):
        return "Circle"
    def invert_area(self, area):
        return sqrt(area/pi)
    def dimname(self):
        return "Circle_radius"
    pass

if __name__ == "__main__":
    circ= Circle(20)
    tri = Triangle(40)
    square = Square(16)
    print(circ, tri, square)

import turtle
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
	square_shaper(16)
	triangle_shaper(40)
	circle_shaper(20)
	
def draw(name,side,color):
	if name =="TRIANGLE":
		triangle_shaper(side,color('yellow'))
	if name =="SQUARE":
		square_shaper(side,color('green'))
	if name =="CIRCLE":
		circle_shaper(side,color('red'))
	else:
		pass

