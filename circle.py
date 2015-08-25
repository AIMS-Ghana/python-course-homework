#!/usr/bin/python

import sys

r = float(sys.argv[1])
pi = 3.14

# perimeter = float(sys.argv[1])+float(sys.argv[2])+float(sys.argv[3])

area = pi * (r**2)
perimeter = (2 * pi * r)

print("the area is:", area)
print("the perimeter is:", perimeter)

