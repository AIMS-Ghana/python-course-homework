#!/usr/bin/python

import sys

i = float(sys.argv[1])
j = float(sys.argv[2])

# perimeter = float(sys.argv[1])+float(sys.argv[2])+float(sys.argv[3])

Area = i * j
perimeter = (2 * i) + (2 * j)

print("the area is:", Area)
print("the perimeter is:", perimeter)

