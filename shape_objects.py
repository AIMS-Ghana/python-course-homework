#!/usr/bin/python

class (Shape):
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
        

class Triangle(Shape):
     def kind(self):
         return "Triangle"
     def dimname(self):
         return "side"
     def invert_area(self, area)
         return(2*(area/(3**0.5))**0.5
    

class Square(Shape):
    def kind(self):
        return "square"
    def dimname(self):
        return "side"
    def invert_area(self, area)
        return(a**0.5)
    

from math import pi

class Circle(Shape):
     def kind(self):
         return "Circle"
     def dimname(self):
         return "radius"
     def invert_area(self, area)
         return(a/pi)**0.5              
    

if __name__ == "__main__":
    circ = Circle(10)
    Triangle = Triangle(8)
    Square = Square(8)
    print(circ)
    print(Triangle)
    print(square)
