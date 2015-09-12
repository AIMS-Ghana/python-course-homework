#!/usr/bin/env python

class Shape:
    def kind(self):
        return "Shape"

    def invert_area(self, area):
        return area

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
	pass
            

class Triangle(Shape):
    def kind(self):
	    return "Triangle"
    def invert_area(self,area):
             return (2*(float( area))**0.5)/3**0.25
    def draw(self,turt):
            turtle.color("blue")
            turtle.begin_fill()
            turtle.forward(self.dim)
            turtle.left(120)
            turtle.forward(self.dim)
            turtle.left(120)
            turtle.forward(self.dim)
            turtle.end_fill()

class Square(Shape):
    def kind(self):
	    return "Square"
    def invert_area(self,area):
             return (area**2)

    def draw(self,turt):
        turtle.color("yellow")
        turtle.begin_fill()
        turtle.forward(self.dim)
        turtle.left(90)
        turtle.forward(self.dim)
        turtle.left(90)  
        turtle.forward(self.dim)
        turtle.left(90)
        turtle.forward(self.dim)
        turtle.left(90) 
        turtle.end_fill()

from math import pi

class Circle(Shape):
	def kind(self):
	    return "Circle"

	def dimname(self):
            return "Radius"

        def invert_area(self,area):
             return (area/pi)**0.5

        def draw(self,turt):
            turtle.color("green")
            turtle.begin_fill()
            turtle.circle(self.dim)
            turtle.end_fill()
         
if __name__ == "__main__":
    import turtle
    circ = Circle(10000)
    triag = Triangle(100)
    squa = Square(10)  
    print (triag)
    print(circ)
    print(squa)
    circ.draw(turtle)
    triag.draw(turtle)
    squa.draw(turtle)
   
