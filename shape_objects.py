#!/usr/bin/python
import math

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
             

class Triangle(Shape):
      def kind(self):
            return "Triangle"

      def invert_area(self, area):
            return math.sqrt(float(area*4)/math.sqrt(3))

      def dimname(self):
               return "sides"


class Square(Shape):
    def kind(self):
        return "Square"

    def invert_area(self, area):
        return (area)**0.5

    def dimname(self):
        return "sides"

class Circle(Shape):
    def kind(self):
        return "Circle"

    def invert_area(self, area):
        return (area/math.pi)*0.5

    def dimname(self):
        return "radius"

        

if __name__ == "__main__":
    circ = Circle(10)
    Squa= Square(5)
    Trigl=Triangle(5)
    print(circ)
    print(Trigl)
    print(Squa)

