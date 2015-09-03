#!/usr/bin/env python3

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

from math import *

class Triangle:
	def kind(self):
		return "Triangle"
	def invert_area(self, area):
		return sqrt (4 * area/ sqrt (3))

	def __init__(self, area):
		self.area = area
		self.side = self.invert_area(area)

	def dimname(self):
		return "side"

	strformat = "{}, area: {}, {}: {}"

	def __str__(self):
		return Triangle.strformat.format(
			self.kind(),
			self.area,
			self.dimname(),
			self.side
			)
	def draw (self,turt):
		import turtle
		s = self.side
		turtle.forward(s)
		turtle.left(120)
		turtle.forward(s)
		turtle.left(120)
		turtle.forward(s)
		turtle.exitonclick()


class Square:
	def kind(self):
		return "Square"
	def invert_area(self, area):
		return sqrt(area)

	def __init__(self, area):
		self.area = area
		self.side = self.invert_area(area) 

	def dimname(self):
		return "side"

	strformat = "{}, area: {}, {}: {}"

	def __str__(self):
		return Square.strformat.format(
			self.kind(),
			self.area,
			self.dimname(),
			self.side
			)
	def draw (self,turt):
		import turtle
		s = self.side
		turtle.forward(s)
		turtle.left(90)
		turtle.forward(s)
		turtle.left(90)
		turtle.forward(s)
		turtle.left(90)
		turtle.forward(s)
		turtle.exitonclick()


class Circle:
	def kind(self):
		return "Circle"
	def invert_area(self, area):
		return sqrt(area / pi)

	def __init__(self, area):
		self._area = area
		self._radius = self.invert_area(area)

	def dimname(self):
		return "radius"

	strformat = "{}, area: {}, {}: {}"

	def __str__(self):
		return Circle.strformat.format(
			self.kind(),
			self._area,
			self.dimname(),
			self._radius
			)
	def draw (self,turt):
		import turtle
		r = self._radius
		turtle.circle(r)
		turtle.exitonclick()

if __name__ == "__main__":
	for I in [Triangle,Square,Circle]:
		K = I(1000)
		print(K)
		K.draw(K) 
