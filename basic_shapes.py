
#!/usr/local/bin/python3
import triangle
import rectangle
import circle
print("Equilateral Triangle, side 4:")
print("a: {0}, p: {1}".format(triangle.area(4,4,4), triangle.perimeter(4,4,4)))
print("Square, side 4:")
print("a: {0}, p: {1}".format(rectangle.area(4,4), rectangle.perimeter(4,4)))
print("Rectange, sides 4, 5:")
print("a: {0}, p: {1}".format(rectangle.area(4,5), rectangle.perimeter(4,5)))
print("Circle, radius 3:")
print("a: {0}, p: {1}".format(circle.area(3), circle.perimeter(3)))
