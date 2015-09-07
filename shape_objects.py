#!/usr/bin/env python3

import math 
import turtle

class Shape:
    def kind(self):
        return "shape"

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

    def draw(self): #drawing the shapes
        pass

class Triangle(Shape):
    def kind(self):
        return "Triangle"
    def invert_area(self, area):
      return math.sqrt((float(area)*4)/math.sqrt(3))
    def dimname(self):
        return "Side"
    def draw(self):
        for i in range(0,3):
            turtle.forward(self.dim) 
            turtle.left(120)


class Square(Shape):
    def kind(self):
        return "Square"
    def invert_area(self, area):
      return float(area**0.5)
    def dimname(self):
        return "Side"
    def draw(self):
        for i in range(0,4):
            turtle.forward(self.dim)
            turtle.left(90)


class Circle(Shape):
    def kind(self):
        return "Circle"
    def invert_area(self, area):
      return math.sqrt(float(area)/math.pi)
    def dimname(self):
        return "Radius"
    def draw(self):
        turtle.circle(self.dim)  



if __name__ == "__main__":
    circ = Circle(500)
    tri= Triangle(500)
    sq=Square(500)
    print(circ)
    print (tri)
    print (sq)
    circ.draw()
    tri.draw()
    sq.draw()
