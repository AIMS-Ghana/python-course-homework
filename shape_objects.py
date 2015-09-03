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

#####################################################################################

class Triangle(Shape):
     def kind(self):
        return "Triangle"
     
     def invert_area(self, area):
        return (4*area/3**(1/2.0))**(1/2.0)

     def dimname(self):
        return "2d"
       

class Square(Shape):
     def kind(self):
        return "Square"
     
     def invert_area(self, area):
        return area**(1/2.0)

     def dimname(self):
        return "2d"
       
       
       

from math import pi

class Circle(Shape):
     def kind(self):
        return "Circle"
     
     def invert_area(self, area):
        return (area/pi)**(1/2.0)

     def dimname(self):
        return "2d"
     
         
       
      

#############################################################

if __name__ == "__main__":
    circ = Circle(10)
    triangle = Triangle(4)
    square = Square(4)

    print(circ)
    print(triangle)
    print(square)
