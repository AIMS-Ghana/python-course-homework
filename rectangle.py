#!/usr/bin/python
import sys
area=""
perimeter=""
rectangle="area {0}, perimeter={1}"
u=float (sys.argv[1])
v=float (sys.argv[2])
p= u * v
height=2 * u * v
area=str(p)
perimeter=str(height)
print(rectangle.format(area,perimeter))
