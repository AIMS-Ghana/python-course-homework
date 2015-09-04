#!/usr/bin/python
from math import *
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

class Triangle:
	def kind(self):
    	    return "Triangle"
	def invert_area(self, area):
	        return (sqrt((area*4)/sqrt(3)))
	def dimname(self):
	        return "side"
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
	def draw(self,turt):
        	import turtle
        	l = self.dim
        	turtle.forward(l)
		turtle.left(120)
		turtle.forward(l)
		turtle.left(120)
		turtle.forward(l)
        	turtle.exitonclick()

class Square:
	def kind(self):
		return "Square"
    	def invert_area(self, area):
        	return (sqrt(area))
	def dimname(self):
        	return "side"

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
	def draw(self,turt):
        	import turtle
        	l = self.dim
        	turtle.forward(l)
		turtle.left(90)
		turtle.forward(l)
		turtle.left(90)
		turtle.forward(l)
		turtle.left(90)
		turtle.forward(l)
        	turtle.exitonclick()

class Circle:
   
    def kind(self):
        return "circle"

    def invert_area(self, area):
        return sqrt (area / pi)

    def dimname(self):
        return "radius"

    def __init__(self, area):
        self.area = area
        self.dim = self.invert_area(area)

    strformat = "{}, area: {}, {}: {}"

    def __str__(self):
        return Circle.strformat.format(
          self.kind(),
          self.area,
          self.dimname(),
          self.dim
        )

    def draw(self,turt):
        import turtle
        l = self.dim
        turtle.circle(l)
        turtle.exitonclick()


if __name__ == "__main__":
	obj = Triangle(10000)
    	print (obj)
    	obj.draw(obj)
	obj = Square(10000)
    	print (obj)
    	obj.draw(obj)
	obj = Circle(10000)
    	print (obj)
    	obj.draw(obj)
